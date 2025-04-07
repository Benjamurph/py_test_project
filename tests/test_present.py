from lib.present import *
import pytest

def test_present():
    present1 = Present()
    with pytest.raises(Exception) as e:
        present1.unwrap()
    error_message = str(e.value)
    assert error_message == 'No contents have been wrapped.'
    present1.wrap('phone')
    with pytest.raises(Exception) as e:
        present1.wrap('watch')
    error_message2 = str(e.value)
    assert error_message2 == "A contents has already been wrapped."
