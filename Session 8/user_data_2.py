data = {
    "name":"Hossein",
    "age": "15",
    "email":"hossein@example.com"
}

def validate_data(name, age, email):
    if not isinstance(name, str) or not name:
        raise ValueError("Invalid name")
    if isinstance(age, str):
        age = int(age)
    if not isinstance(age, int) or age < 0:
        raise ValueError("Invalid age")

    if not isinstance(email, str) or "@" not in email:
        raise ValueError("Invalid email")

if __name__ == "__main__":
    try:
        validate_data(**data)

        print(f"The user data: {data}")
    except ValueError as err:
        print(f"A validation error occured: {err}")