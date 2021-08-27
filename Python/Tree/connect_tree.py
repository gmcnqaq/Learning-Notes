from binary_tree_basis import BinaryTreeNode, BinaryTree
from binary_tree_basis import preorder_morris, build_tree_level


# LeetCode 116
# 填充每个节点的下一个右侧节点指针
# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有 next 指针都被设置为 NULL。

# 输入：root = [1,2,3,4,5,6,7]
# 输出：[1,#,2,3,#,4,5,6,7,#]
# 解释：你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。


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
