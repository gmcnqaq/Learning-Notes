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


# 反思：计算第 k 小的元素，或者说是找到排名为 k 的元素，如果想要达到对数级别的复杂度，关键在于每个节点得知道他自己的排名
# 这样，如果查找排名为 k 的元素，当前节点的排名为 m
# 如果 m == k，返回当前节点
# 如果 m < k，那么就应该去左子树找，去左子树搜索第 k 个元素
# 如果 m > k，那么就应该去右子树找，去右子树搜索第 k - m - 1 个元素

# 如果要让当前节点知道自己的排名，则需要正确的记录以自己为根的这颗二叉树有多少个节点（size）

if __name__ == '__main__':
    A = BinaryTree()
    arr = [3, 1, 4, None, 2]
    A.root = build_tree_level(arr)
    print(kth_smallest(A.root, 3))
