import multiprocessing

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_sequential(node, target):
    if node is None:
        return False

    print(node.value)
    if node.value == target:
        print("Valor encontrado.")
        return True

    if dfs_sequential(node.left, target):
        return True
    if dfs_sequential(node.right, target):
        return True
    return False

def dfs_parallel(node, target):
    if node is None:
        return False

    print(node.value)
    if node.value == target:
        print("Valor encontrado.")
        return True

    with multiprocessing.Pool(processes=2) as pool:
        results = pool.starmap(dfs_sequential, [(node.left, target), (node.right, target)])

    return any(results)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    target = 5

    dfs_parallel(root, target)