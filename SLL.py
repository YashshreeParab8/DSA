class Node :
  def  __init__(self,value):
    self.data = value
    self.next = None

class SLL :
  def __init__(self):
    self.head = None

  def append(self,new_node):
    if (self.head == None):
      self.head = new_node
    else:
      temp = self.head
      while (temp.next):
        temp = temp.next
      temp.next = new_node

  def insert(self,new_node,pos):
    if pos == 1: #to insert node at first position
      new_node.next = self.head
      self.head = new_node
    else: #to insert node from 2nd to last position
      p=1
      temp = self.head
      while(p!=pos-1):
        temp = temp.next
        p+=1
      new_node.next = temp.next
      temp.next = new_node

  #find and delete middle element
  def findmid_del(self):
      temp = temp1 = self.head
      prev=None
      while temp1 and temp1.next:
        prev = temp
        temp = temp.next
        temp1 = temp1.next.next
        print("Middle node:",temp.data)
        prev.next = temp.next
        temp=None

  def delfirst_last(self):
    temp1=self.head
    temp1 = None
    prev = None
    temp = self.head=self.head.next
    while(temp.next):
      prev = temp
      temp = temp.next
    prev.next=None
    temp = None

  def delete(self, value):
      temp=self.head
      prev=None
      if temp.data==value:
        self.head=self.head.next
      else:
        while(temp.data!=value and temp!=None):
          prev=temp
          temp=temp.next
          if temp==None:
            print("value is not present in the list")
            return
        prev.next=temp.next
        temp=None

  def reverse(self):
    prev = None
    curr = self.head
    while(curr):
      nxt = curr.next   
      curr.next = prev  
      prev = curr       
      curr = nxt        
    self.head = prev

  def sum_consecutive(self):
    temp = self.head
    while(temp.next):
      print(temp.data, "+", temp.next.data, "=", temp.data + temp.next.data)
      temp = temp.next
 

  def print(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next 

list1 = SLL()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

print("Original list:")
list1.print()
 
list1.insert(Node(15),2)
print("\nAfter insert:")
list1.print()

list1.delfirst_last()
list1.print()

list1.delete(30)
print("\nAfter delete:")
list1.print()
 

list1.reverse()
print("\nAfter reverse:")
list1.print()
 
print("\nSum of consecutive nodes:")
list1.sum_consecutive()

list1.findmid_del()
list1.print()