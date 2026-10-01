n=int(input("Enter number of elements:"))
arr=[]
ecount=0
ocount=0
for i in range(n):
    num=int(input("Enter elements:"))
    arr.append(num)

for i in arr:
    if i%2==0:
        ecount+=1
    else:
        ocount+=1

print("Number of even numbers:",ecount)
print("Number of odd number:",ocount)