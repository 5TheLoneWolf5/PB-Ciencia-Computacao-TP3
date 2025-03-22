import multiprocessing

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
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

    @staticmethod
    def _parallel_search(node, target):
        if node is None:
            return False

        print(f"Checking node: {node.value}")
        if node.value == target:
            print("Valor encontrado.")
            return True

        # Recursively search in left and right subtrees sequentially
        left_found = BinaryTree._parallel_search(node.left, target)
        if left_found:
            return True
        right_found = BinaryTree._parallel_search(node.right, target)
        return right_found

    @staticmethod
    def parallel_search(node, target):
        if node is None:
            return False

        if node.value == target:
            print(f"Checking node: {node.value}")
            print("Valor encontrado.")
            return True

        with multiprocessing.Pool(processes=2) as pool:
            results = pool.starmap(
                BinaryTree._parallel_search,
                [(node.left, target), (node.right, target)]
            )

        return any(results)

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

if __name__ == "__main__":
    tree = BinaryTree()

    for value in [50, 43, 32, 56, 3, 45, 27, 60]:
        tree.add(value)

    print(tree.postorder())

    target = 60

    found = BinaryTree.parallel_search(tree.root, target)
    if not found:
        print("Valor encontrado!")