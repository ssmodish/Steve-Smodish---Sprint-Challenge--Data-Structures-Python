import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# the BST is the construct (like a node) and the implementation (like a linked list)
    def insert(self, value):
        new_leaf = BinarySearchTree(value)
        if value < self.value:
            if not self.left:
                self.left = new_leaf
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_leaf
            else:
                self.right.insert(value)

    def contains(self, target):
        if target:
            # print(f"bst {self.value} contains {target}")
            if target == self.value:
                # print("returning true")
                return True
            elif target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value



start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
bst = BinarySearchTree(names_1.pop(0))
for name_1 in names_1:
    bst.insert(name_1)


for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

