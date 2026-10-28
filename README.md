# JSON Schema Infer 🔍

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0-brightgreen.svg)](https://github.com/MilindChatrabhuji/json-schema-infer)

A fast, **zero-dependency** Python library that automatically infers standard JSON Schemas, generates production-ready **Pydantic v2 models**, and creates **TypeScript interfaces** from arbitrary raw JSON data or Python dictionaries.

---

## 🚀 Quickstart

### 1. Infer JSON Schema

```python
from json_schema_infer import infer_json_schema

payload = {
    "order_id": 9921,
    "customer": "Sarah Connor",
    "total": 149.99,
    "items": ["t-800_cpu", "plasma_rifle"]
}

schema = infer_json_schema(payload, title="OrderPayload")
print(schema)
```

### 2. Auto-Generate Pydantic v2 Models

```python
from json_schema_infer import generate_pydantic_model

code = generate_pydantic_model(schema, class_name="OrderModel")
print(code)
```

**Output:**
```python
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class OrderModel(BaseModel):
    order_id: int
    customer: str
    total: float
    items: List[str]
```

### 3. Generate TypeScript Interfaces

```python
from json_schema_infer import generate_typescript_interface

ts_code = generate_typescript_interface(schema, interface_name="IOrder")
print(ts_code)
```

---

## 🧪 Testing

```bash
python -m pytest tests
```

---

## 📄 License
MIT License. Created by [Milind Chatrabhuji](https://github.com/MilindChatrabhuji).
