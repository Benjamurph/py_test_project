from lib.check_codeword import *

def test_check_codeword():
    assert check_codeword('x') == 'WRONG!'
    assert check_codeword('horse') == 'Correct! Come in.'
    assert check_codeword('hone') == 'Close, but nope.'
