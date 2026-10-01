# n=int(input("Enter number of elements:"))
# arr=[]
# for i in range(n):
#     num=int(input("Enter elements:"))
#     arr.append(num)
# print(arr)
# n1=int(input("Enter a number to search:"))
# p_index = 0
# for j in range(0,len(arr)-1) :
#     for i in arr :
#         if i == num :
#             no_present = True
#             p_index = j

# if no_present :
#     print(f"number is present in the array at position {p_index}")
# else :
#     print("number is not present in the array")
n = int (input("Enter the size of array (n) :"))
arr =[]
for i in range (0,n,+1):
    a = int (input("Enter the element of array :"))
    arr.append(a)
print(arr)

is_present = False
num = int(input("enter number to search : "))
p_index = 0
for j in range(0,len(arr)-1) :
    for i in arr :
        if i == num :
            is_present = True
            p_index = j

if is_present :
    print(f"number is present in the array at position {p_index}")
else :
    print("number is not present in the array")