ans = 0

s = set()
for obj in objects:
    i = id(obj)
    if i not in s:
        ans += 1
        s.add(i)

print(ans)
