from binary_tree_basis import BinaryTree
from binary_tree_basis import inorder_morris, build_tree_level


# 把二叉搜索树转换为累加树
# LeetCode 538
# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于node.val的值之和。
#
# 提醒一下，二叉搜索树满足下列约束条件：
#
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。

# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
def convert_bst(root):
    def traverse(root):
        nonlocal total
        if not root:
            return None
        # 利用 BST 中序遍历的特点，修改递归顺序，降序打印节点的值
        traverse(root.right)
        total += root.val
        root.val = total
        traverse(root.left)

    total = 0
    traverse(root)
    return root


# 利用 Morris 遍历的方法，反序中序遍历
def convert_bst_morris(root):
    total = 0
    p1 = root
    while p1:
        p2 = p1.right
        if p2:
            while p2.left and p2.left != p1:
                p2 = p2.left
            if not p2.left:
                p2.left = p1
                p1 = p1.right
                continue
            else:
                p2.left = None
        total += p1.val
        p1.val = total
        p1 = p1.left
    return root


if __name__ == '__main__':
    A = BinaryTree()
    arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    A.root = build_tree_level(arr)
    print(inorder_morris(A.root))
    # A.root = convert_bst(A.root)
    A.root = convert_bst_morris(A.root)
    print(inorder_morris(A.root))
