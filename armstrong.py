num=int(input("enter a number:"))
p=len(str(num))
n=num
sum=0
while(num>0):
    sum=sum+(num%10)**p
    num//=10
if n==sum:
    print("number is armstrong")
else:
    print("number is not armstrong")