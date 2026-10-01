n=int(input("Enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("Enter elements:"))
    arr.append(num)
uni_num=[]
for i in arr:
    if i not in uni_num:
        uni_num.append(i)
print(uni_num)