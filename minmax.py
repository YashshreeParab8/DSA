#find min and max number from an array
# arr=[10,34,45,6,8,20,25,19]
# min=arr[0]
# max=arr[0]
# for num in arr:
#     if num<min:
#         min=num
#     if num>max:
#         max=num
# print("Minimum:",min)
# print("Maximum:",max)

#find second min and second max
arr=[10,34,45,6,8,20,25,19]
min=arr[0]
max=arr[0]
for num in arr:
    if num<min:
        smin=min
        min=num
    if num>max:
        smax=max
        max=num
print("Minimum:",min)
print("Second min:",smin)
print("Maximum:",max)
print("Second max:",smax)