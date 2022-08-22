

from somestuff import myfunc

def test_myfunc_int_is_something():
    assert myfunc(13) == 'something'

def test_myfunc_none_is_none():
    assert myfunc(None) == None