class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            return None
        value = self.top.data
        self.top = self.top.next
        return value


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    # 1. Enqueue
    def enqueue(self, value):
        new_node = Node(value)
        if self.isempty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # 2. Dequeue
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:      # queue became empty
            self.rear = None
        print("Dequeued element:", temp.data)
        return temp.data

    # 3. Display
    def display(self):
        if self.isempty():
            print("Queue is empty")
            return
        print("Queue elements (front to rear):")
        temp = self.front
        items = []
        while temp:
            items.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(items))

    # 4. Reverse the queue using a stack
    def reverse(self):
        if self.isempty():
            print("Queue is empty")
            return
        s = Stack()
        # Move all elements from queue to stack
        while not self.isempty():
            s.push(self.front.data)
            self.front = self.front.next
        self.rear = None
        # Move them back from stack to queue (order is now reversed)
        while not s.isempty():
            self.enqueue(s.pop())
        print("Queue reversed")

    # 5. Merge two queues into one (originals are left unchanged)
    def merge(self, other):
        merged = Queue()
        temp = self.front
        while temp:
            merged.enqueue(temp.data)
            temp = temp.next
        temp = other.front
        while temp:
            merged.enqueue(temp.data)
            temp = temp.next
        return merged

    # 6. Check if two queues are identical
    def is_identical(self, other):
        t1 = self.front
        t2 = other.front
        while t1 and t2:
            if t1.data != t2.data:
                return False
            t1 = t1.next
            t2 = t2.next
        return t1 is None and t2 is None


# ---------- Calling every function ----------
q1 = Queue()

print("1. Enqueue")
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print("Enqueued 10, 20, 30, 40")

print("\n3. Display")
q1.display()

print("\n2. Dequeue")
q1.dequeue()

print("\n3. Display after dequeue")
q1.display()

print("\n4. Reverse Queue using Stack")
q1.reverse()

print("\n3. Display after reversing queue")
q1.display()

print("\n5. Merge two queues into one")
q2 = Queue()
q2.enqueue(5)
q2.enqueue(15)
print("Queue 1:")
q1.display()
print("Queue 2:")
q2.display()
merged = q1.merge(q2)
print("Merged queue:")
merged.display()

print("\n6. Check if two queues are identical")
q3 = Queue()
q3.enqueue(5)
q3.enqueue(15)
print("Queue 1 and Queue 2 identical?", q1.is_identical(q2))
print("Queue 2 and Queue 3 (5, 15) identical?", q2.is_identical(q3))