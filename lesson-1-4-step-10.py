requests_count = int(input())
namespaces = {"global": {"parent": None, "vars": []}}
result = []


def get(namesp, arg):
    if namespaces[namesp]["parent"] is None:
        if arg in namespaces[namesp]["vars"]:
            return namesp
        else:
            return "None"
    elif arg in namespaces[namesp]["vars"]:
        return namesp
    else:
        return get(namespaces[namesp]["parent"], arg)


for i in range(requests_count):
    cmd, namesp, arg = input().split()
    if cmd == "create":
        namespaces[namesp] = {"parent": arg, "vars": []}
    elif cmd == "add":
        namespaces[namesp]["vars"].append(arg)
    elif cmd == "get":
        result.append(get(namesp, arg))

for i in result:
    print(i)
