# UNFINISHED !!!
#
#
# # n = int(input())
# # classes = {}
# #
# # for i in range(n):
# #     raw = input().split(":")
# #     if len(raw) > 1:
# #         classes[raw[0].strip()] = []
# #         for x in raw[1].split():
# #             classes[raw[0].strip()].append(x)
# #     else:
# #         classes[raw[0].strip()] = []
# #
# #
# # m = int(input())
# # errors = []
# #
# # for i in range(m):
# #     raw = input()
# #     errors.append(raw)
# #
# # del raw
#
# classes = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError'],
#            'OSError': [], 'FileNotFoundError': ['OSError']}
# errors = [
#     'ZeroDivisionError', 'OSError', 'ArithmeticError', 'FileNotFoundError']
# result = []
#
#
# def find_parents(_classes, _error):
#     visited, stack = set(), [_error]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#     return visited
#
#
#     # if class2 not in _classes:
#     #     return "No"
#     # elif class1 == class2:
#     #     if class2 in _classes:
#     #         return "Yes"
#     #     else:
#     #         return "No"
#     # else:
#     #     for _class in _classes:
#     #         if class2 == _class:
#     #             if class1 in _classes[_class]:
#     #                 return "Yes"
#     #             else:
#     #                 for i in _classes[_class]:
#     #                     if find_parents(class1, i, _classes) == "Yes":
#     #                         return "Yes"
#     #             return "No"
#
#
# for error in errors:
#     result.append(find_parents(classes, error))
#
# # print(classes)
# # print(requests)
# print(result)

exceptions = {}
throwed_exceptions = []


def found_path(exceptions, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in exceptions:
        return []
    for node in exceptions[start]:
        if node not in path:
            newpath = found_path(exceptions, node, end, path)
            if newpath: return newpath
    return []


n = int(input())
for _ in range(n):
    inpt = input().split()
    child = inpt[0]
    parents = inpt[2:]
    exceptions[child] = parents

m = int(input())
for _ in range(m):
    throwing = input()
    for throwed_exception in throwed_exceptions:
        if len(found_path(exceptions, throwing, throwed_exception)) > 1:
            print(throwing)
            break
    throwed_exceptions.append(throwing)
