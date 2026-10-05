#program to print pattern:
# A 
# B C 
# D E F 
n=int(input("Enter number of rows:"))
num=0
for i in range(n):
    for j in range (i+1):
        print(chr(65+num), end=" ")
        num+=1
    print()