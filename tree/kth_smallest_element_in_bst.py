from binary_tree_basis import BinaryTree
from binary_tree_basis import build_tree_level


# 二叉搜索树中第K小的元素
# LeetCode 230
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
def kth_smallest(root, k):
    curr, stack = root, []
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        temp = stack.pop()
        k -= 1
        if not k:
            return temp.val
        curr = temp.right


if __name__ == '__main__':
    A = BinaryTree()
    arr = [3, 1, 4, None, 2]
    A.root = build_tree_level(arr)
    print(kth_smallest(A.root, 1))

