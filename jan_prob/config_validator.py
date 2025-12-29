from typing import Any, Dict, List, Tuple
import json
from pathlib import Path

JsonDict = Dict[str, Any]
SchemaDict = Dict[str, Any]


class ConfigValidator:

    def __init__(self, schema: SchemaDict):
        self.schema = schema

    def validate_config(self, config: JsonDict) -> Dict[str, Any]:
        """Top-level API: validate full config, return result dict."""
        errors: List[str] = []
        fixed_config = {}

        # Validate each top-level key defined in schema
        for key, subschema in self.schema.items():
            value = config.get(key)
            path = key
            valid_value, field_errors = self._validate_node(value, subschema, path)
            if field_errors:
                errors.extend(field_errors)
            if valid_value is not None:
                fixed_config[key] = valid_value

        # Optionally keep unknown keys from config
        for key, value in config.items():
            if key not in self.schema:
                fixed_config[key] = value

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "fixed_config": fixed_config
        }

    def _validate_node(self, value: Any, schema: SchemaDict, path: str) -> Tuple[Any, List[str]]:
        """Recursively validate a single node (object or leaf)."""
        errors: List[str] = []
        expected_type = schema.get("type")

        if expected_type == "object":
            if value is None:
                # Missing object: if required, report; else, default to {}
                # Here we assume top-level objects are required if in schema
                errors.append(f"{path}: required object missing")
                return None, errors

            if not isinstance(value, dict):
                errors.append(f"{path}: expected object, got {type(value).__name__}")
                return None, errors

            properties = schema.get("properties", {})
            required_fields = schema.get("required", [])

            fixed_obj = {}

            # Check required fields
            for field in required_fields:
                if field not in value:
                    errors.append(f"{path}.{field}: required field missing")

            # Validate each property
            for field, subschema in properties.items():
                child_value = value.get(field)
                child_path = f"{path}.{field}"
                valid_child, child_errors = self._validate_node(child_value, subschema, child_path)
                if child_errors:
                    errors.extend(child_errors)
                if valid_child is not None:
                    fixed_obj[field] = valid_child

            # Keep unknown fields as-is (optional design choice)
            for field, v in value.items():
                if field not in properties:
                    fixed_obj[field] = v

            return fixed_obj, errors

        # Leaf validators
        if value is None:
            # Missing non-object leaf; could support defaults
            if "default" in schema:
                return schema["default"], errors
            else:
                errors.append(f"{path}: required value missing")
                return None, errors

        if expected_type == "string":
            if not isinstance(value, str):
                errors.append(f"{path}: expected string, got {type(value).__name__}")
            else:
                min_len = schema.get("min_length")
                max_len = schema.get("max_length")
                if min_len is not None and len(value) < min_len:
                    errors.append(f"{path}: length must be >= {min_len} (got {len(value)})")
                if max_len is not None and len(value) > max_len:
                    errors.append(f"{path}: length must be <= {max_len} (got {len(value)})")
            return value, errors

        if expected_type == "int":
            if not isinstance(value, int):
                errors.append(f"{path}: expected int, got {type(value).__name__}")
                return value, errors
            min_val = schema.get("min")
            max_val = schema.get("max")
            if min_val is not None and value < min_val:
                errors.append(f"{path}: must be >= {min_val} (got {value})")
            if max_val is not None and value > max_val:
                errors.append(f"{path}: must be <= {max_val} (got {value})")
            return value, errors

        if expected_type == "boolean":
            if not isinstance(value, bool):
                errors.append(f"{path}: expected boolean, got {type(value).__name__}")
            return value, errors

        # Fallback: unknown type in schema
        errors.append(f"{path}: unknown schema type '{expected_type}'")
        return value, errors


# Usage / Test
if __name__ == "__main__":
    raw_config = {
        "database": {
            "host": "localhost",
            "port": 70000,   # invalid (> 65535)
            "timeout": 0     # invalid (< 1)
        },
        "cache": {
            "enabled": "yes",  # invalid type
            "ttl_seconds": 30  # invalid (< 60)
        },
        "limits": {
            "max_connections": 5000  # invalid (> 1000)
        },
        "extra_field": "keep_me"     # unknown, preserved
    }

    validator = ConfigValidator(SCHEMA)
    result = validator.validate_config(raw_config)

    print("Valid:", result["valid"])
    print("Errors:")
    for e in result["errors"]:
        print(" -", e)
    print("Fixed config:")
    print(json.dumps(result["fixed_config"], indent=2))
