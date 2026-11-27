# Q.1 Online Examination Result Management- An examination department
# stores student examination scores in a BST. Each score is inserted as a node.

# Tasks:
# 1. Insert the following examination scores out of 100 into the BST.
# 45, 78, 32, 89, 56, 92, 67, 34, 85, 73, 61, 98
# 2. Display scores in ascending order.
# 3. Find the highest and lowest scores.
# 4. Count the number of students scoring above 50.
# 5. Search for a particular score.
# 6. Find the average of all scores.

class Node:
    def __init__(self,value):
        self.left=None
        self.score=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.cnt=0


    def insert(self,new_node):
        if self.root is None:
            self.root=new_node
            return

        else:
            temp=self.root
            while True:
                if new_node.score<temp.score:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return
                        
                    else:
                        temp=temp.right

    def inorder(self,root): #left-root-right
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.score, end=" ")
            self.inorder(root.right)

    def finminmax(self,root):
        if root is None:
            print("\nTree is empty")
            return
        else:
            temp=self.root
            while temp.left:
                temp=temp.left
            print("\nLowest score:",temp.score)

            temp=self.root
            while temp.right:
                temp=temp.right
            print("\nHighest score:",temp.score)

    def count_abv_50(self,root):
        if root is None:
            return
        else:
            self.count_abv_50(root.right)
            if root.score>50:
                self.cnt+=1
                self.count_abv_50(root.right)

    def search(self, value): 
        temp=self.root
        while temp:
            if value==temp.score:
                return True
            elif value<temp.score:
                temp=temp.left
            else:
                temp=temp.right
        return False

    def sum_count(self,root):
        if root is None:
            return
        else:
            self.sum_count(root.left)
            self.total+=root.score
            self.count+=1
            self.sum_count(root.right)

    def average(self):
        if self.root is None:
            print("tree is empty")
            return
        else:
            arr=[self.root]
            count=0
            total=0

            while count<len(arr):
                temp=arr[count]
                count+=1
                total+=temp.score
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            print("\nAverage",total/count)

b1=BST()
b1.insert(Node(45))
b1.insert(Node(78))
b1.insert(Node(32))
b1.insert(Node(89))
b1.insert(Node(56))
b1.insert(Node(92))
b1.insert(Node(67))
b1.insert(Node(34))
b1.insert(Node(85))
b1.insert(Node(73))
b1.insert(Node(61))
b1.insert(Node(98))

print("\nScores in ascending:")
b1.inorder(b1.root)

b1.finminmax(45)

b1.count_abv_50(b1.root)
print("Number of Students scoring above 50:",b1.cnt)

key=int(input("Enter the score to search:"))
if b1.search(key):
    print("\n Score found")
else:
    print("\nScore not found")
b1.average()