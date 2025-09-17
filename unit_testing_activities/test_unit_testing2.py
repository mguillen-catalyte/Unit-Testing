from unit_testing2 import sleep_in


def test_is_weekday_not_vacation():
    assert sleep_in(True, False) == False


def test_is_weekday_is_vacation():
    assert sleep_in(True, True) == True


def test_not_weekday_is_vacation():
    assert sleep_in(False, True) == True


def test_not_weekday_not_vacation():
    assert sleep_in(False, False) == True
