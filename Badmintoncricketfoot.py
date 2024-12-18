cricket = []
n = int(input("Enter the number of students who play cricket := "))
for i in range(n):
    k = int(input("Enter the roll no of student who plays cricket := "))
    cricket.append(k)
badminton = []
n1 = int(input("Enter the number of students who play badminton := "))
for i in range(n1):
    k1 = int(input("Enter the roll no of student who plays badminton := "))
    badminton.append(k1)
football = []
n2 = int(input("Enter the number of students who play football := "))
for i in range(n2):
    k2 = int(input("Enter the roll no of student who plays football := "))
    football.append(k2)
total_stud = badminton + cricket + football 

cb = []
for i in cricket:
    cb.append(i)
for i in badminton:
    if i not in cb: 
        cb.append(i)
print("Students roll no who play badminton and cricket =", cb)


bcb = []
for i in cb:
    if (i in cricket) and (i in badminton):
        bcb.append(i)
print("Roll no of students who play both cricket and badminton =", bcb)

ncb = []
for i in range(1, max(total_stud) + 1):  
    if i not in cricket and i not in badminton:
        ncb.append(i)
print("Roll no of students who neither play cricket nor badminton =", ncb)

fc = []
for i in football:
    if i in cricket and i not in badminton:
        fc.append(i)
print("Roll no of students who play cricket and football but not badminton =", fc)
