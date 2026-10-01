n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

result = []

# Add all non-zero elements first
for i in range(n):
    if arr[i] != 0:
        result.append(arr[i])

# Add zeros at the end
for i in range(n):
    if arr[i] == 0:
        result.append(arr[i])

print("Array after rearranging:")
print(result)