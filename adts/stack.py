class StackItem:

    data = None
    next = None

    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class Stack:

    top_dummy = StackItem()

    def is_empty(self) -> bool:
        return self.top_dummy.next == None

    def push(self, value):
        new_item = StackItem(value)
        new_item.next = self.top_dummy.next
        self.top_dummy.next = new_item
    
    def pop(self):

        if not self.is_empty():
            top_item : StackItem = self.top_dummy.next
            self.top_dummy.next = top_item.next
            top_item.next = None
            return top_item.data
        
        print('Stack is Empty!')

    def print_stack(self):
        cur : StackItem = self.top_dummy.next

        while cur is not None:
            print(cur.data)
            cur = cur.next