from um import count
#piyushgopal
def test_count():
    assert count("um") == 1
    assert count('album') == 0
    #piyushgopal
    assert count("Um, thanks, um...") == 2
