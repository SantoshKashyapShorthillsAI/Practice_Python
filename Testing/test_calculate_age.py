from src.calculate_age import *

def test_get_age():
    yyyy,mm,dd=map(int,"1996/07/11".split("/"))
    age=get_age(yyyy,mm,dd)
    assert age==28