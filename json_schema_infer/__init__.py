"""
json-schema-infer: Zero-dependency JSON schema inference and Pydantic v2 code generation.
"""
__version__ = "0.1.0"

from .infer import infer_json_schema
from .codegen import generate_pydantic_model, generate_typescript_interface

__all__ = ["infer_json_schema", "generate_pydantic_model", "generate_typescript_interface"]
