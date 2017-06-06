import cenum


@cenum.cenum()
class A(object):
    a
    b
    c = 10
    d


def test_cenum():
    assert A.a == 0
    assert A.b == 1
    assert A.c == 10
    assert A.d == 11
