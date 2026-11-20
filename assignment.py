class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # 1. Push
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # 2. Pop
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        temp = self.top
        self.top = self.top.next
        print("Popped element:", temp.data)
        return temp.data

    # 3. Display
    def display(self):
        if self.isempty():
            print("Stack is empty")
            return
        print("Stack elements (top to bottom):")
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next

    # 4. Reverse a string using a stack
    def reverse_string(self, text):
        s = Stack()
        for ch in text:
            s.push(ch)
        result = ""
        while not s.isempty():
            result += s.top.data
            s.top = s.top.next
        return result

    # 5. Reverse the stack using another stack
    def reverse_stack(self):
        if self.isempty():
            print("Stack is empty")
            return
        temp_stack = Stack()
        while not self.isempty():
            temp_stack.push(self.top.data)
            self.top = self.top.next
        self.top = temp_stack.top
        print("Stack reversed")


# ---------- Calling every function ----------
st = Stack()

print("1. Push")
st.push(10)
st.push(100)
st.push(45)
print("Pushed 10, 100, 45")

print("\n3. Display")
st.display()

print("\n2. Pop")
st.pop()

print("\n3. Display after pop")
st.display()

print("\n4. Reverse String using Stack")
text = "hello"
print("Original string:", text)
print("Reversed string:", st.reverse_string(text))

print("\n5. Reverse Stack using another Stack")
st.reverse_stack()

print("\n3. Display after reversing stack")
st.display()