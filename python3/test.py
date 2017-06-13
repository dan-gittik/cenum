import cenum


class A(metaclass=cenum.CEnum):
    a
    b
    c = 10
    d


assert A.a == 0
assert A.b == 1
assert A.c == 10
assert A.d == 11
