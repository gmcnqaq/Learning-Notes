from typing import List

from binary_tree_basis import BinaryTree, BinaryTreeNode
from binary_tree_basis import preorder_morris, inorder_morris


# 从前序与中序遍历序列构造二叉树
# LeetCode 105
# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#      3
#     / \
#    9   20
#       / \
#     15   7
def rec_build_tree(preorder, inorder):
    return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


def build(preorder, pre_left, pre_right, inorder, in_left, in_right):
    if pre_left > pre_right:
        return None
    root_val = preorder[pre_left]
    root_idx = inorder.index(root_val)
    left_size = root_idx - in_left
    root = BinaryTreeNode(root_val)
    root.left = build(preorder, pre_left + 1, pre_left + left_size,
                      inorder, in_left, root_idx - 1)
    root.right = build(preorder, pre_left + left_size + 1, pre_right,
                       inorder, root_idx + 1, in_right)
    return root


def rec1_build_tree(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    # 也可以提前建一个字典 快速查找 index
    root_idx = inorder.index(root_val)
    root = BinaryTreeNode(root_val)
    root.left = rec1_build_tree(preorder[1: root_idx + 1], inorder[:root_idx])
    root.right = rec1_build_tree(preorder[root_idx + 1:], inorder[root_idx + 1:])
    return root


# 对于前序遍历中的任意两个连续节点 u 和 v，根据前序遍历的流程，我们可以知道 u 和 v 只有两种可能的关系：
# v 是 u 的左儿子。这是因为在遍历到 u 之后，下一个遍历的节点就是 u 的左儿子，即 v；
# u 没有左儿子，并且 v 是 u 的某个祖先节点（或者 u 本身）的右儿子。如果 u 没有左儿子，那么下一个遍历的节点就是 u 的右儿子。如果 u 没有右儿子，我们就会向上回溯，直到遇到第一个有右儿子
# （且 u 不在它的右儿子的子树中）的节点 u_a ，那么 v 就是 u_a的右儿子。

# 我们归纳出上述例子中的算法流程：
#
# 我们用一个栈和一个指针辅助进行二叉树的构造。初始时栈中存放了根节点（前序遍历的第一个节点），指针指向中序遍历的第一个节点；
#
# 我们依次枚举前序遍历中除了第一个节点以外的每个节点。如果 index 恰好指向栈顶节点，那么我们不断地弹出栈顶节点并向右移动 index，并将当前节点作为最后一个弹出的节点的右儿子；如果 index
# 和栈顶节点不同，我们将当前节点作为栈顶节点的左儿子；
#
# 无论是哪一种情况，我们最后都将当前的节点入栈。

def iter_build_tree(preorder, inorder):
    if not preorder:
        return None
    root = BinaryTreeNode(preorder[0])
    stack: List[BinaryTreeNode] = [root]
    inorder_index = 0
    for i in range(1, len(preorder)):
        preorder_val = preorder[i]
        node = stack[-1]
        if node.val != inorder[inorder_index]:
            node.left = BinaryTreeNode(preorder_val)
            stack.append(node.left)
        else:
            while stack and stack[-1].val == inorder[inorder_index]:
                node = stack.pop()
                inorder_index += 1
            node.right = BinaryTreeNode(preorder_val)
            stack.append(node.right)

    return root


if __name__ == '__main__':
    A = BinaryTree()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    A.root = rec_build_tree(preorder, inorder)
    print(preorder_morris(A.root))
    print(inorder_morris(A.root))
    A.root = rec1_build_tree(preorder, inorder)
    print(preorder_morris(A.root))
    print(inorder_morris(A.root))
    A.root = iter_build_tree(preorder, inorder)
    print(preorder_morris(A.root))
    print(inorder_morris(A.root))

