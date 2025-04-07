from lib.house import *

def test_house():
    house1 = House(137, 'white')
    assert house1.get_details() == 'House number 137 has 2 floors and a white door'
    house1.repaint_door('blue')
    assert house1.door_colour == 'blue'