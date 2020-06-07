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
#
# def s(a, *vs, b=10):
#     res = a + b
#     for v in vs:
#         res += v
#     return res
#
#
# print(s(21))
#
# t_c = 18
# tmp = "ok"
#
#
# def fahrenheit(t_c):
#     tmp = t_c * 9 / 5
#     return tmp
#
#
# print(fahrenheit(t_c))
# print(tmp)
#
# a = {}
# a = {"1": []}
# a = {"1": [{}]}
#
# print(a)
#
#
# class Counter:
#     def __init__(self):
#         self.count = 0
#
#
# x = Counter()
# print(x.count)
# x.count += 1
# print(x.count)
# y = Counter()
# print(y.count)
#
# class A:
#     val = 1
#
#     def foo(self):
#         A.val += 2
#
#     def bar(self):
#         self.val += 1
#
#
# a = A()
# b = A()
#
# a.bar()
# a.foo()
#
# c = A()
#
# print(a.val)
# print(b.val)
# print(c.val)

# graph = {'A': {'B', 'C'},
#          'B': {'A', 'D', 'E'},
#          'C': {'A', 'F'},
#          'D': {'B'},
#          'E': {'B', 'F'},
#          'F': {'C', 'E'}}
#
#
# def dfs(_graph, start):
#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(_graph[vertex] - visited)
#     return visited
#
#
# print(dfs(graph, 'A'))
# # {'E', 'D', 'F', 'A', 'C', 'B'}
import sys
for path in sys.path:
    print(path)