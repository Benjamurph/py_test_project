from lib.counter import *

def test_counter():
    counter1 = Counter()
    counter1.add(5)
    assert counter1.report() == "Counted to 5 so far."