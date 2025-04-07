from lib.password_checker import *
import pytest

def test_password_checker():
    password_checker1 = PasswordChecker()
    assert password_checker1.check('12345678') == True
    with pytest.raises(Exception) as e:
        password_checker1.check('1234567')
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'