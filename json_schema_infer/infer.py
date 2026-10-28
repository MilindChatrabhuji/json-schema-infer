from typing import Any, Dict

def infer_type(val: Any) -> Dict[str, Any]:
    if val is None:
        return {"type": "null"}
    elif isinstance(val, bool):
        return {"type": "boolean"}
    elif isinstance(val, int):
        return {"type": "integer"}
    elif isinstance(val, float):
        return {"type": "number"}
    elif isinstance(val, str):
        if "@" in val and "." in val:
            return {"type": "string", "format": "email"}
        return {"type": "string"}
    elif isinstance(val, list):
        if not val:
            return {"type": "array", "items": {}}
        return {"type": "array", "items": infer_type(val[0])}
    elif isinstance(val, dict):
        return infer_json_schema(val)
    return {"type": "string"}

def infer_json_schema(data: Dict[str, Any], title: str = "Root") -> Dict[str, Any]:
    """Infers standard JSON schema from a dictionary."""
    properties = {}
    required = []

    for k, v in data.items():
        properties[k] = infer_type(v)
        required.append(k)

    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": title,
        "type": "object",
        "properties": properties,
        "required": required
    }
