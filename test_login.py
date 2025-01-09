# test_login.py
import pytest
from code_pytest import login

@pytest.mark.parametrize(
    "username, password, expected_status, expected_message",
    [
        ("admin", "password123", "success", "Login successful!"),  # Valid credentials
        ("admin", "wrongpassword", "failure", "Invalid username or password"),  # Invalid password
        ("user", "password123", "failure", "Invalid username or password"),  # Invalid username
        ("", "", "failure", "Invalid username or password"),  # Empty fields
    ],
)
def test_login(username, password, expected_status, expected_message):
    """Test the login function with various inputs."""
    result = login(username, password)
    assert result["status"] == expected_status
    assert result["message"] == expected_message
