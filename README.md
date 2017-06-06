# Enum

A nifty decorator that allows C-style enums definitions in Python:

```python
@enum()
class A:
    a
    b
    c = 10
    d

assert A.a == 0
assert A.b == 1
assert A.c == 10
assert A.d == 11
```
