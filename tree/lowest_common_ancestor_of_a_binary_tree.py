from binary_tree_basis import BinaryTree
from binary_tree_basis import build_tree_level


# 二叉树的最近公共祖先
# LeetCode 236
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 示例 1：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
# 示例 2：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
# 示例 3：
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left is not None and right is not None:
        return root
    if not left and not right:
        return None
    return right if not left else left


if __name__ == '__main__':
    A = BinaryTree()
    arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    A.root = build_tree_level(arr)
    p = A.find_val_level(5)
    q = A.find_val_level(4)
    lca = lowest_common_ancestor(A.root, p, q)
    print(lca)
