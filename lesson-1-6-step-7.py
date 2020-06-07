n = int(input())
classes = {}

for i in range(n):
    raw = input().split(":")
    if len(raw) > 1:
        classes[raw[0].strip()] = []
        for x in raw[1].split():
            classes[raw[0].strip()].append(x)
    else:
        classes[raw[0].strip()] = []


q = int(input())
requests = []

for i in range(q):
    raw = input().split()
    requests.append(raw)

del raw


def find_parents(class1, class2, _classes):
    if class2 not in _classes:
        return "No"
    elif class1 == class2:
        if class2 in _classes:
            return "Yes"
        else:
            return "No"
    else:
        for _class in _classes:
            if class2 == _class:
                if class1 in _classes[_class]:
                    return "Yes"
                else:
                    for i in _classes[_class]:
                        if find_parents(class1, i, _classes) == "Yes":
                            return "Yes"
                return "No"


for request in requests:
    print(find_parents(request[0], request[1], classes))
