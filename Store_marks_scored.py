n=int(input("Enter the no of students :="))
l1=[]
for i in range(n):
    a=input("Enter the FDS insem marks of students :=")
    l1.append(a)
l=[]
for i in l1:
    if(i=="A"):
        l.append(i)
    else:
        l.append(int(i))    
l2=[]
ab=0
for i in l:
    if i=="A":
        ab=ab+1
    else:
         l2.append(i)
sum=0
for i in l2:
    sum=sum+i
print("average of marks is :=",sum/n)
print("minimum marks :=",min(l2))
print("maximum marks :=",max(l2))
print("No of absent students :=",ab)
k=int(input("enter the marks which most repeated :="))
print("frequency of ", k ,":=",l2.count(k))
        
