row = int(input("Enter the number of elements in row: "))
column = int(input("Enter the number of elements in column: "))
A = []
for i in range(row):
    p = []
    for j in range(column):
        a = int(input(f"Enter the number of element in position ({i},{j}): "))
        p.append(a)
    A.append(p)
print("Matrix is:")
for i in A:
    print(i)
k = []
for i in A:
    a1 = min(i)
    k.append(a1)
b = min(k)
found_saddle_point = False
for i in A:
    if b in i:
        c = i.index(b)
        found_saddle_point = True
        break
if found_saddle_point:
    Q = []
    for i in A:
        l = i[c]
        Q.append(l)
    c1 = max(Q)
    if b == c1:
        print("Saddle point is:", c1)
    else:
        print("Saddle point is not present")
else:
    print("Saddle point is not present")
