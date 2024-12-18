row=int(input("Enter the no of elements in row"))
column=int(input("Enter the no of elements in column"))
A=[]
for i in range(row):
    p=[]
    for j in range(column):
         a=int(input("Enter the no of element in position " +str(i)+ ","+str(j)))
         p.append(a)
    A.append(p)
print("Matrix is :=",A)
for i in A:
    print(i)
k=[]
for i in A:
    a1=min(i)
    k.append(a1)
b=min(k)
for i in A:
    if b in i:
        c=i.index(b)
    else:
        pass
Q=[]
for i in A:
    l=i[c]
    Q.append(l)
c1=max(Q)
print("SADDLE POINT IS :=",c1)
