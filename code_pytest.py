# login.py

def login(username: str, password: str) -> dict:
    """Mock login function."""
    if username == "admin" and password == "password123":
        return {"status": "success", "message": "Login successful!"}
    return {"status": "failure", "message": "Invalid username or password"}
