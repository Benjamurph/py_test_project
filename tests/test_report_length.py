from lib.report_length import *

def test_report_length():
    assert report_length('hi') == 'This string was 2 characters long.'
    assert report_length('') == 'This string was 0 characters long.'