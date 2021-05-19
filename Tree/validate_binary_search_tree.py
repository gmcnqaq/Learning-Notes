from binary_tree_basis import BinaryTree
from binary_tree_basis import inorder_morris, build_tree_level


# 验证二叉搜索树
# LeetCode 98
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
# 示例1:
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#     根节点的值为 5 ，但是其右子节点值为 4 。
def is_valid_bst(root):
    return check(root, float('-inf'), float('inf'))


def check(node, lower, upper):
    if not node:
        return True
    val = node.val
    if val <= lower or val >= upper:
        return False
    return check(node.right, val, upper) & check(node.left, lower, val)


def is_valid_bst_morris(root):
    p1, prev = root, float('-inf')
    while p1:
        p2 = p1.left
        if p2:
            while p2.right and p2.right != p1:
                p2 = p2.right
            if not p2.right:
                p2.right = p1
                p1 = p1.left
                continue
            else:
                p2.right = None
        if p1.val <= prev:
            return False
        prev = p1.val
        p1 = p1.right
    return True


if __name__ == '__main__':
    A = BinaryTree()
    # arr1 = [5, 1, 4, None, None, 3, 6]
    arr1 = [5, 4, 6, None, None, 3, 7]
    # arr2 = [2, 1, 3]
    arr2 = [1, 1, None]
    A.root = build_tree_level(arr1)
    print(inorder_morris(A.root))
    print(is_valid_bst(A.root))
    print(is_valid_bst_morris(A.root))
    A.root = build_tree_level(arr2)
    print(inorder_morris(A.root))
    print(is_valid_bst(A.root))
    print(is_valid_bst_morris(A.root))
