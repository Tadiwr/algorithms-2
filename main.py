from adts.linked_list import LinkedList
from adts.stack import Stack
from adts.queue import Queue
from adts.binary_tree import BinaryTree

my_list = LinkedList()
st = Stack()
q = Queue()
tree = BinaryTree()

tree.insert(100)
tree.insert(25)
tree.insert(150)
tree.insert(6)
tree.insert(169)

tree.deletetree(169)

tree.print_tree_post()