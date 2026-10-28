from typing import Dict, Any

def _py_type(prop: Dict[str, Any]) -> str:
    t = prop.get("type", "Any")
    if t == "string":
        return "str"
    elif t == "integer":
        return "int"
    elif t == "number":
        return "float"
    elif t == "boolean":
        return "bool"
    elif t == "array":
        items = prop.get("items", {})
        return f"List[{_py_type(items)}]"
    elif t == "object":
        return "Dict[str, Any]"
    return "Any"

def generate_pydantic_model(schema: Dict[str, Any], class_name: str = "GeneratedModel") -> str:
    """Generates Python code for a Pydantic v2 model."""
    lines = [
        "from pydantic import BaseModel, Field",
        "from typing import Optional, List, Dict, Any",
        "",
        f"class {class_name}(BaseModel):"
    ]
    props = schema.get("properties", {})
    required = set(schema.get("required", []))

    if not props:
        lines.append("    pass")
    else:
        for k, v in props.items():
            py_t = _py_type(v)
            if k in required:
                lines.append(f"    {k}: {py_t}")
            else:
                lines.append(f"    {k}: Optional[{py_t}] = None")

    return "\n".join(lines)

def generate_typescript_interface(schema: Dict[str, Any], interface_name: str = "IGenerated") -> str:
    """Generates TypeScript interface definition."""
    type_map = {
        "string": "string",
        "integer": "number",
        "number": "number",
        "boolean": "boolean",
        "array": "any[]",
        "object": "Record<string, any>"
    }
    lines = [f"export interface {interface_name} {{"]
    props = schema.get("properties", {})
    required = set(schema.get("required", []))

    for k, v in props.items():
        t = v.get("type", "any")
        ts_t = type_map.get(t, "any")
        opt = "" if k in required else "?"
        lines.append(f"  {k}{opt}: {ts_t};")

    lines.append("}")
    return "\n".join(lines)
