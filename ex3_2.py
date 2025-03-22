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

    def dfs(self):
        result = []
        self._dfs(self.root, result)
        return result

    def _dfs(self, current, result):
        if current is not None:
            self._dfs(current.left, result)
            result.append(current.value)
            self._dfs(current.right, result)

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

    for value in [43, 12, 4, 14, 4, 32]:
        tree.add(value)

    print(tree.dfs())
