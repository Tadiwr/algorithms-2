class TreeNode:

    data = None
    left = None
    right = None

    def __init__(self, data=None) -> None:
        self.data = data


class BinaryTree:

    root = TreeNode()

    def is_empty(self):
        return self.root.data is None

    def insert(self, value):

        if value is None:
            raise ValueError('Cannot insert a None value into the tree')

        if self.is_empty():
            self.root.data = value
        else:
            new_node = TreeNode(value)
            cur : TreeNode = self.root
            prev : TreeNode = cur

            while cur:
                prev = cur

                if cur.data < value:
                    cur = cur.right 
                else:
                    cur = cur.left
            
            if prev.data < value:
                prev.right = new_node
            else:
                prev.left = new_node


    def post_order(self, root:TreeNode):

        if root.left:
            self.post_order(root.left)
        
        if root.right:
            self.post_order(root.right)

        print(root.data)

    def insert_left(self, value):

        if self.is_empty():
            self.root.data = value
        else:
            new_node = TreeNode(value)
            cur = self.root
            prev = cur

            while cur:
                prev = cur
                cur = cur.left
            
            prev.left = new_node

    def insert_right(self, value):

        if self.is_empty():
            self.root.data = value
        else:
            new_node = TreeNode(value)
            cur = self.root
            prev = cur

            while cur:
                prev = cur
                cur = cur.right
            
            prev.right = new_node