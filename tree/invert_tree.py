from binary_tree_basis import BinaryTree
from binary_tree_basis import preorder_morris, build_tree_level


# 翻转二叉树
# LeetCode 226
# 翻转一棵二叉树。

def rec_invert_tree(root):
    # base case
    if not root:
        return None
    root.left, root.right = root.right, root.left
    rec_invert_tree(root.left)
    rec_invert_tree(root.right)
    return root


def iter_invert_tree(root):
    if not root:
        return None
    queue = [root, ]
    while queue:
        curr = queue.pop(0)
        curr.left, curr.right = curr.right, curr.left
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return root


if __name__ == '__main__':
    A = BinaryTree()
    nums = [4, 2, 7, 1, 3, 6, 9]
    A.root = build_tree_level(nums)
    print(preorder_morris(A.root))
    A.root = rec_invert_tree(A.root)
    print(preorder_morris(A.root))
    A.root = iter_invert_tree(A.root)
    print(preorder_morris(A.root))
