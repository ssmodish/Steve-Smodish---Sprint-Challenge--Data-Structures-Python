class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # send current node value to cb
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
        # start a queue
        queue = []
        # add this node to the queue
        queue.append(self)
        # while there are items in the queue
        while len(queue) > 0:
            # dequeue the oldest node
            current_item = queue.pop(0)
            # send the value to the cb
            cb(current_item.value)
            # add any children to the queue
            if current_item.left is not None:
                queue.append(current_item.left)
            if current_item.right is not None:
                queue.append(current_item.right)




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
bst.insert(3)
bst.insert(4)
bst.insert(10)
bst.insert(9)
bst.insert(11)
bst.breadth_first_for_each(cb)
print(arr)
