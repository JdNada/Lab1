from pydantic import BaseModel, EmailStr, field_validator
from dataclasses import dataclass
class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @dataclass
    class User:
        name: str
        email: str
        account_id: int
@field_validator("account_id")
def validate_account_id(cls, value):
    if value <= 0:
        raise ValueError(f"account_id must be positive: {value}")
    return value
user_data = {
    'name': 'Salah',
    'email': 'salah@gmail.com',
    'account_id': 1234
}
#creer l objet user
user = User(**user_data)
#exporter en json string
user_json_str = user.model_dump_json()
print(user_json_str)
#exporter en dict python
user_json_obj = user.model_dump()
print(user_json_obj)
# JSON string correct pour recréer un User
json_str = '{"name": "Salah", "email": "Salah@gmail.com", "account_id": 1234}'
user = User.model_validate_json(json_str)
x: int = 0
y: str = "hello"

print(user.name)
print(user.email)
print(user.account_id)
print(x)
print(y)
