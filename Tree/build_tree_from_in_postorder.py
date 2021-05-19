from binary_tree_basis import BinaryTreeNode, BinaryTree
from binary_tree_basis import postorder_morris, inorder_morris


# 从中序与后序遍历序列构造二叉树
# LeetCode 106
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
def rec_build_tree(inorder, postorder):
    def build(in_left, in_right):
        # 如果这里没有节点构造二叉树了，就结束
        if in_left > in_right:
            return None
        # 选择 post_idx 位置的元素作为当前子树根节点
        val = postorder.pop()
        root = BinaryTreeNode(val)
        # 根据 root 所在位置分成左右两棵子树
        index = idx_map[val]
        # 构造右子树
        root.right = build(index + 1, in_right)
        # 构造左子树
        root.left = build(in_left, index - 1)
        return root

    idx_map = {val: idx for idx, val in enumerate(inorder)}
    return build(0, len(inorder) - 1)


def rec1_build_tree(inorder, postorder):
    if not postorder:
        return None
    root_val = postorder[-1]
    root_idx = inorder.index(root_val)
    root = BinaryTreeNode(root_val)
    root.left = rec_build_tree(inorder[:root_idx], postorder[:root_idx])
    root.right = rec_build_tree(inorder[root_idx + 1:], postorder[root_idx: -1])
    return root


if __name__ == '__main__':
    A = BinaryTree()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    A.root = rec1_build_tree(inorder, postorder)
    print(inorder_morris(A.root))
    print(postorder_morris(A.root))
    A.root = rec_build_tree(inorder, postorder)
    print(inorder_morris(A.root))
    print(postorder_morris(A.root))
