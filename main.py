cs1 = int(input())
cs2 = int(input())
cs3 = int(input())
if cs1 % 2 == 0:
    c1 = cs1 // 2
else:
    c1 = cs1 // 2 + 1
if cs2 % 2 == 0:
    c2 = cs2 // 2
else:
    c2 = cs2 // 2 + 1
if cs3 % 2 == 0:
    c3 = cs3 // 2
else:
    c3 = cs3 // 2 + 1
print(c1 + c2 + c3)