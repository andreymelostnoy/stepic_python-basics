s = input()
a = input()
b = input()
cnt = 0

if a in s:
    if a in b:
        print("Impossible")
    elif a != b:
        while a in s:
            s = s.replace(a, b)
            cnt += 1
        print(cnt)
elif a not in s:
    print("0")
