import helpers


def test_increment():
    expected = 11
    actual = helpers.increment(10)

    assert expected == actual


def test_increment_negative():
    expected = -1
    actual = helpers.increment(-2)

    assert expected == actual
