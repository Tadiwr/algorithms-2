class TreeNode:

    data = None
    left = None
    right = None

    def __init__(self, data=None) -> None:
        self.data = data


class BinaryTree:

    root = TreeNode()
    out_str = ''

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

        self.out_str += f'{root.data} '

    def print_tree_post(self):
        self.out_str = ''

        if self.is_empty():
            print('Empty Tree')
        else:
            self.post_order(self.root)
            print(self.out_str)

    def search(self, target) -> bool:

        cur = self.root

        while cur:
            if cur.data == target:
                return True
            else:
                if cur.data > target:
                    cur = cur.left
                else:
                    cur = cur.right
        
        return False
    
    def find_parent(self, target):

        cur = self.root

        while cur:

            if cur.data > target:
                if cur.left:
                    if cur.left.data == target:
                        return cur
                    else:
                        cur = cur.left
                else:
                    return None
            else:
                if cur.right:
                    if cur.right.data == target:
                        return cur
                    else:
                        cur = cur.right
                else:
                    return None
            
                
    def deletetree(self, target):

        if target == self.root.data:
            self.root = TreeNode()
        else:
            parent = self.find_parent(target)

            if parent:
                if parent.data > target:
                    parent.left = None
                else:
                    parent.right = None
            else:
                print('Tree was not found')