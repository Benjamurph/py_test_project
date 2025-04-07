from lib.string_builder import *

def test_string_builder():
    string1 = StringBuilder()
    string1.add('hi')
    assert string1.output() == 'hi'
    assert string1.size() == 2
    string1.add('!')
    assert string1.output() == 'hi!'
    assert string1.size() == 3
