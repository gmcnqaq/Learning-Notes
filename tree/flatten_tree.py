from binary_tree_basis import BinaryTree
from binary_tree_basis import inorder_morris, build_tree_level


# 二叉树展开为链表
# LeetCode 114
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。

# 函数的定义：输入一个节点 root，那么以 root 为根的二叉树就会被拉平为一条链表
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
def rec_flatten(root):
    """
     Do not return anything, modify root in-place instead.
    """
    if not root:
        pass
    else:
        rec_flatten(root.left)
        rec_flatten(root.right)
        # 此时左右子树已经被拉为一条链表
        left, right = root.left, root.right
        # 将左子树作为右子树
        root.left = None
        root.right = left
        # 将原先的右子树接到当前右子树的末端
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = right


# 问题转化为寻找前驱节点
def iter_flatten(root):
    if not root:
        return root
    curr = root
    while curr:
        if curr.left:
            pre = nxt = curr.left
            while pre.right:
                pre = pre.right
            pre.right = curr.right
            curr.left = None
            curr.right = nxt
        curr = curr.right


if __name__ == '__main__':
    A = BinaryTree()
    nums = [1, 2, 5, 3, 4, None, 6]
    A.root = build_tree_level(nums)
    print(inorder_morris(A.root))
    rec_flatten(A.root)
    print(inorder_morris(A.root))
    B = BinaryTree()
    B.root = build_tree_level(nums)
    iter_flatten(B.root)
    print(inorder_morris(B.root))
