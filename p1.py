#1/10/26 practical
#1.Write a program to accept N integers into an array and calculate and display the sum of all the elements. 
n=int(input("Enter no. of elements:"))
arr=[]
for i in range(n):
    num=int(input("Enter elements:"))
    arr.append(num)

sum =0
for i in arr:
    sum+=i
print(sum)