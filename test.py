# x = [1, 2, 3]
# print(id(x))
# print(type(id(x)))
# print(id([1, 2, 3]))
#
# x = [1, 2, 3]
# y = x
# y.append(4)
#
# s = "123"
# t = s
# t = t + "4"
#
# print(str(x) + " " + s)
#
# a = []
#
# def foo(arg1, arg2):
#   a.append("foo")
#
# foo(a.append("arg1"), a.append("arg2"))
#
# print(a)
#


def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res


print(s(21))
