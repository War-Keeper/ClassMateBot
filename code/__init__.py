# This is a Sample test file
# TODO test the todo functionality of github actions
def sqr(x):
    return x * x


def test_answer1():
    assert sqr(3) == 9


def upper_case(x):
    return x.upper()


def test_answer2():
    assert upper_case('software') == 'SOFTWARE'


def check_length(x):
    return len(x)


def test_answer3():
    return check_length('abc') == 3
