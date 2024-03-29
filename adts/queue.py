class QueueItem:

    data = None
    next = None

    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class Queue:

    front_dummy = QueueItem
    rear_dummy = front_dummy

    def is_empty(self) -> bool:
        return self.front_dummy is self.rear_dummy

    def enqueue(self, value):
        new_item = QueueItem(value)
        self.rear_dummy.next = new_item
        self.rear_dummy = self.rear_dummy.next

    def dequeue(self):
        if not self.is_empty():
            front_item : QueueItem = self.front_dummy.next
            self.front_dummy.next = front_item.next
            front_item.next = None

            return front_item.data
        
        print('Queue is Empty! Cannot Dequeue')

    def print_queue(self):

        if self.is_empty():
            print('Queue is Empty')
            return

        out_str = ''
        cur : QueueItem = self.front_dummy.next

        while cur:
            out_str += f'{cur.data} '
            cur = cur.next

        print(out_str)
