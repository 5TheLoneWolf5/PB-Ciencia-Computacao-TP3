import multiprocessing
import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def update_max(node, shared_max, lock):
    if node is None:
        return

    with lock:
        if node.value > shared_max.value:
            shared_max.value = node.value

    jobs = []
    if node.left:
        p_left = multiprocessing.Process(target=update_max, args=(node.left, shared_max, lock))
        jobs.append(p_left)
        p_left.start()
    if node.right:
        p_right = multiprocessing.Process(target=update_max, args=(node.right, shared_max, lock))
        jobs.append(p_right)
        p_right.start()

    for job in jobs:
        job.join()

if __name__ == '__main__':
    multiprocessing.freeze_support() 

    manager = multiprocessing.Manager()

    shared_max = manager.Value('i', -sys.maxsize - 1)
    lock = manager.Lock()

    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(17)
    root.right.right = Node(25)

    update_max(root, shared_max, lock)
    print("Valor máximo: ", shared_max.value)
