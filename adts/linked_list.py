class ListNode:

    next = None
    data = None

    def __init__(self,data=None, next =None) -> None:
        self.data = data
        self.next = next


class LinkedList:

    dummy = ListNode() # acts as a start dummy node
    cur = dummy # Points to the last element in the list
 
    def insert(self, value):
        """ Insert the `value` as a new node at the end of the list """

        new_node = ListNode(value)
        self.cur.next = new_node
        self.cur = self.cur.next

    def delete(self, target) -> bool:

        """ Deletes the first node encountered when moving from the start
            to the end of the list that has the `target` value passed as a param

            Returns `True` if Item was found and deleted else returns `False` if Item was not found and deleted
        """

        cur : ListNode = self.dummy.next
        prev: ListNode = self.dummy

        while cur is not None:
            
            if cur.data == target:
                prev.next = cur.next
                cur.next = None
                return
            
            prev = cur
            cur = cur.next
        
        return False
    
    def print_list(self):

        out_str = 'Start--> '
        cur : ListNode = self.dummy.next

        while cur is not None:
            out_str += f'{cur.data}--> '
            cur = cur.next
        
        print(out_str + 'End')

    def find(self, target) -> bool:
        """Returns `True` if a node with the `target` value if found"""

        cur = self.dummy.next

        while cur in None:
            if cur.data == target: return True
        
        return False