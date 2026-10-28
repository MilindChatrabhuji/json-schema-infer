from json_schema_infer import infer_json_schema, generate_pydantic_model, generate_typescript_interface

def test_infer_schema():
    sample = {
        "user_id": 101,
        "username": "milind",
        "is_admin": True,
        "score": 98.6,
        "tags": ["python", "ai"]
    }
    schema = infer_json_schema(sample, title="User")
    assert schema["type"] == "object"
    assert schema["properties"]["user_id"]["type"] == "integer"
    assert schema["properties"]["username"]["type"] == "string"
    assert schema["properties"]["is_admin"]["type"] == "boolean"
    assert schema["properties"]["tags"]["type"] == "array"

def test_generate_pydantic_model():
    sample = {"name": "Test", "age": 30}
    schema = infer_json_schema(sample)
    code = generate_pydantic_model(schema, class_name="UserSchema")
    assert "class UserSchema(BaseModel):" in code
    assert "name: str" in code
    assert "age: int" in code

def test_generate_typescript_interface():
    sample = {"title": "Book", "views": 100}
    schema = infer_json_schema(sample)
    ts = generate_typescript_interface(schema, "IBook")
    assert "export interface IBook {" in ts
    assert "title: string;" in ts
    assert "views: number;" in ts
