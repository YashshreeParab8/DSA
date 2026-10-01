n=int(input("Enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("Enter elements:"))
    arr.append(num)
max=arr[0]
smax=arr[0]
min=arr[0]
smin=arr[0]

for i in arr:
    if i<min:
        smin=min
        min=i

for i in arr:
    if i>max:
        smax=max
        max=i
print("minimum",min)
print("second minimum",smin)
print("maximum",max)
print("second maximum",smax)