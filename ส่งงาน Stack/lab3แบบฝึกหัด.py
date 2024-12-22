class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} into stack. Current stack: {self.stack}")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from stack. Current stack: {self.stack}")
            return item
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
# สร้าง Stack
my_stack = Stack()

# ทดสอบการ push ข้อมูล 5 ตัว
items_to_push = [10, 20, 30, 40, 50]
for item in items_to_push:
    my_stack.push(item)

# แสดงข้อมูลบนสุดโดยใช้ peek
print(f"Top item is: {my_stack.peek()}")

# ทดสอบ pop ข้อมูลออก 3 ตัว
for _ in range(3):
    my_stack.pop()

# แสดงข้อมูลที่เหลือใน Stack
print(f"Remaining stack: {my_stack.stack}")
