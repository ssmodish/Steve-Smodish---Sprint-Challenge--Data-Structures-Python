class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        print(f"This node's value is: {self.value}")
        cb(self.value)
        # check for a left leaf and if there is one
        if self.left is not None:
            # run DFS on the left leaf
            self.left.depth_first_for_each(cb)
        # check for a right leaf and if there is one
        if self.right is not None:
            # run DFS on the right leaf
            self.right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):
        pass

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value



arr = []
cb = lambda x: arr.append(x)
bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(9)
bst.depth_first_for_each(cb)
print(arr)
