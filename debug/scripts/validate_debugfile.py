#!/usr/bin/env python3
"""Validate the stable, provider-neutral parts of Debugfile.yml version 1."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: install it in the active Python environment.")


REQUIRED = {
    "version": int,
    "context": dict,
    "services": list,
    "channels": list,
    "reproduction": dict,
    "verification": dict,
    "records": dict,
}
AUTHORITIES = {"executable", "canonical", "supporting", "historical"}
CHANNEL_KINDS = {
    "logs",
    "traces",
    "metrics",
    "errors",
    "deployments",
    "audit",
    "database",
    "runtime",
}
LOCATOR_PREFIXES = (
    "env:",
    "profile:",
    "connector:",
    "secret-manager:",
    "keychain:",
    "instructions:",
)
SECRET_KEYS = re.compile(r"(?:credential|password|secret|token|api[_-]?key)", re.I)
SECRET_VALUES = re.compile(r"(?:AKIA[0-9A-Z]{16}|gh[opsu]_[A-Za-z0-9]{20,}|-----BEGIN .*PRIVATE KEY-----)")


def mapping(value: Any, location: str, errors: list[str]) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    errors.append(f"{location} must be a mapping")
    return {}


def unique_ids(items: Any, location: str, errors: list[str]) -> None:
    if not isinstance(items, list):
        errors.append(f"{location} must be a list")
        return
    seen: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{location}[{index}] must be a mapping")
            continue
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id.strip():
            errors.append(f"{location}[{index}].id must be a non-empty string")
        elif item_id in seen:
            errors.append(f"{location} contains duplicate id {item_id!r}")
        else:
            seen.add(item_id)


def check_adapter(item: dict[str, Any], location: str, errors: list[str]) -> None:
    adapter = item.get("adapter")
    if adapter is None:
        return
    adapter = mapping(adapter, f"{location}.adapter", errors)
    if bool(adapter.get("cli")) != bool(adapter.get("skill")):
        errors.append(f"{location}.adapter must name both cli and skill")


def check_path(value: Any, root: Path, location: str, warnings: list[str]) -> None:
    if not isinstance(value, str):
        return
    relative = value.removeprefix("path:")
    if ":" in relative or any(character in relative for character in "*?[]"):
        return
    if not (root / relative).exists():
        warnings.append(f"{location} points to missing repository path {relative!r}")


def check_secrets(value: Any, location: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}.{key}"
            if SECRET_KEYS.search(str(key)) and child is not None:
                if not isinstance(child, str) or not child.startswith(LOCATOR_PREFIXES):
                    errors.append(f"{child_location} must be a credential locator, not a value")
            check_secrets(child, child_location, errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            check_secrets(child, f"{location}[{index}]", errors)
    elif isinstance(value, str) and SECRET_VALUES.search(value):
        errors.append(f"{location} looks like an inline secret")


def validate(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [str(exc)], warnings
    if not isinstance(data, dict):
        return ["Debugfile root must be a mapping"], warnings

    for field, expected in REQUIRED.items():
        value = data.get(field)
        if not isinstance(value, expected):
            errors.append(f"{field} must be {expected.__name__}")
    if data.get("version") != 1:
        errors.append("version must be 1")

    context = mapping(data.get("context"), "context", errors)
    sources = context.get("sources", [])
    unique_ids(sources, "context.sources", errors)
    if isinstance(sources, list):
        for index, source in enumerate(sources):
            if not isinstance(source, dict):
                continue
            location = f"context.sources[{index}]"
            if source.get("authority") not in AUTHORITIES:
                errors.append(f"{location}.authority must be one of {sorted(AUTHORITIES)}")
            check_adapter(source, location, errors)
            source_config = mapping(source.get("source"), f"{location}.source", errors)
            if not source_config.get("type") or not source_config.get("location"):
                errors.append(f"{location}.source must name type and location")
            if source_config.get("type") != "repository" and not source.get("last_verified"):
                warnings.append(f"{location} is external but has no last_verified date")
            if source_config.get("type") == "repository":
                check_path(source_config.get("location"), path.parent, f"{location}.source.location", warnings)

    services = data.get("services")
    if isinstance(services, list):
        if any(not isinstance(item, dict) for item in services):
            errors.append("every service must be a mapping")
        names = [item.get("name") for item in services if isinstance(item, dict)]
        if any(not isinstance(name, str) or not name.strip() for name in names):
            errors.append("every service must have a non-empty name")
        if len(names) != len(set(names)):
            errors.append("service names must be unique")
        for index, service in enumerate(services):
            if not isinstance(service, dict):
                continue
            if not isinstance(service.get("environments"), list):
                errors.append(f"services[{index}].environments must be a list")
            check_path(service.get("source"), path.parent, f"services[{index}].source", warnings)

    channels = data.get("channels")
    unique_ids(channels, "channels", errors)
    if isinstance(channels, list):
        for index, channel in enumerate(channels):
            if not isinstance(channel, dict):
                continue
            location = f"channels[{index}]"
            if channel.get("kind") not in CHANNEL_KINDS:
                errors.append(f"{location}.kind must be one of {sorted(CHANNEL_KINDS)}")
            if not channel.get("provider"):
                errors.append(f"{location}.provider is required")
            if not isinstance(channel.get("environments"), list):
                errors.append(f"{location}.environments must be a list")
            if not channel.get("use_when"):
                errors.append(f"{location}.use_when is required")
            check_adapter(channel, location, errors)
            access = mapping(channel.get("access"), f"{location}.access", errors)
            if not access.get("method"):
                errors.append(f"{location}.access.method is required")
            check_path(access.get("instructions"), path.parent, f"{location}.access.instructions", warnings)
            check_path(access.get("config"), path.parent, f"{location}.access.config", warnings)

    records = data.get("records")
    if isinstance(records, dict):
        check_adapter(records, "records", errors)
    check_secrets(data, "Debugfile", errors)
    return errors, warnings


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_debugfile.py <path/to/Debugfile.yml>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if path.name != "Debugfile.yml":
        print("error: expected a file named Debugfile.yml", file=sys.stderr)
        return 1
    errors, warnings = validate(path)
    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1
    print("Debugfile is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
