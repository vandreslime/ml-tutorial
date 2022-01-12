from  helpers import increment


def test_increment():
    expected = 11
    actual = increment(10)

    assert expected == actual


def test_increment_negative():
    expected = -1
    actual = increment(-2)

    assert expected == actual
