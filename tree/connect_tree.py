from binary_tree_basis import BinaryTreeNode, BinaryTree
from binary_tree_basis import preorder_morris, build_tree_level


class Node(BinaryTreeNode):
    def __init__(self, next=None):
        super().__init__()
        self.next = next


def rec_connect(root):
    if not root:
        return root
    connect_2nodes(root.left, root.right)
    return root


def connect_2nodes(node1, node2):
    if not (node1 or node2):
        return node1
    node1.next = node2
    connect_2nodes(node1.left, node1.right)
    connect_2nodes(node1.right, node2.left)
    connect_2nodes(node2.left, node2.right)


def iter_connect(root):
    if not root:
        return root
    leftmost = root
    while leftmost:
        # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
        head = leftmost
        while head:
            head.left.next = head.right
            # 在上一层将下一层的不同双亲的节点连接
            if head.next:
                head.right.next = head.next.left
            head = head.next
        # 去下一层的最左节点
        leftmost = leftmost.left
    return root


if __name__ == '__main__':
    A = BinaryTree()
    nums = [1, 2, 3, 4, 5, 6, 7]
    A.root = build_tree_level(nums)
    print(preorder_morris(A.root))
