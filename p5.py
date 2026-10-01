#reverse array
N = int(input("Enter the number of elements: "))

arr = []

for i in range(N):
    num = int(input("Enter element: "))
    arr.append(num)

print("Elements in reverse order:")

for i in range(N - 1, -1, -1):
    print(arr[i], end=" ")