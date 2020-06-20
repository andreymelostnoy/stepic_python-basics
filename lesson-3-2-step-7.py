s, t = (input() for _ in range(2))

if s.find(t) == -1:
    print("0")
else:
    index = 0
    cnt = 0
    while index < len(s):
        if s.startswith(t, index):
            cnt += 1
        index += 1
    print(cnt)
