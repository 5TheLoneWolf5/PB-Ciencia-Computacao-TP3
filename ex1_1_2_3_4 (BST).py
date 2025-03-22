"""

- Exercício 1.1:

In-order: [20, 30, 40, 50, 60, 70, 80]
Pre-order: [50, 30, 20, 40, 70, 60, 80]
Post-order: [20, 40, 30, 60, 80, 70, 50]

- Exercício 1.2:

In-order: [40, 60, 70, 80]

- Exercício 1.3:

Valor 40 existe na estrutura? Resposta: True

- Exercício 1.4:

As árvores criadas satisfazem a propriedade BST?
True
True
False

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add(current.right, value)


    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, current, value):
        if current is None:
            return current

        if value < current.value:
            current.left = self._remove(current.left, value)
        elif value > current.value:
            current.right = self._remove(current.right, value)
        else:
            if current.left is None and current.right is None:
                return None
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            min_larger_node = self._get_min(current.right)
            current.value = min_larger_node.value
            current.right = self._remove(current.right, min_larger_node.value)
        return current

    def _get_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current is not None:
            self._inorder(current.left, result)
            result.append(current.value)
            self._inorder(current.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, current, result):
        if current is not None:
            result.append(current.value)
            self._preorder(current.left, result)
            self._preorder(current.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, current, result):
        if current is not None:
            self._postorder(current.left, result)
            self._postorder(current.right, result)
            result.append(current.value)

    def height(self):
        return self._height(self.root)

    def _height(self, current):
        if current is None:
           return -1
        left_height = self._height(current.left)
        right_height = self._height(current.right)
        return 1 + max(left_height, right_height)

def isTreeBST(current, minval=float("-inf"), maxval=float("inf")):
    if current is None:
        return True

    if not (minval < current.value < maxval):
        return False

    return (isTreeBST(current.left, minval, current.value) and isTreeBST(current.right, current.value, maxval))

if __name__ == "__main__":
    tree = BinaryTree()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.add(value)

    print(tree.inorder())
    print(tree.preorder())
    print(tree.postorder())

    tree.remove(20)
    tree.remove(30)
    tree.remove(50)

    print(tree.inorder())

    toBeFound = 40

    print(f"Valor {toBeFound} existe na estrutura? Resposta: " + str(tree.search(toBeFound)))

    root1 = Node(10)
    root1.left = Node(8)
    root1.left.left = Node(5)
    root1.right = Node(11)
    root1.right.right = Node(15)

    root2 = Node(10)
    root2.left = Node(12)
    root2.left.left = Node(5)
    root2.right = Node(4)
    root2.right.left = Node(1)

    print("As árvores criadas satisfazem a propriedade BST?")

    print(isTreeBST(tree.root))
    print(isTreeBST(root1))
    print(isTreeBST(root2))