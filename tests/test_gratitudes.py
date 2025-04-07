from lib.gratitudes import *

def test_gratitudes():
    gratitudes1 = Gratitudes()
    gratitudes1.add('family')
    assert gratitudes1.format() == 'Be grateful for: family' 
    gratitudes1.add('and friends')
    assert gratitudes1.format() == 'Be grateful for: family, and friends' 