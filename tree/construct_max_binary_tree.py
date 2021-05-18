from binary_tree_basis import BinaryTree, BinaryTreeNode
from binary_tree_basis import preorder_morris


# 最大二叉树
# LeetCode 654
# 给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：
#
# 二叉树的根是数组 nums 中的最大元素。
# 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
# 右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
# 返回有给定数组 nums 构建的 最大二叉树 。

# 输入：nums = [3,2,1,6,0,5]
# 输出：[6,3,5,null,2,0,null,null,1]
# 解释：递归调用如下所示：
# - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
#     - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
#         - 空数组，无子节点。
#         - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
#             - 空数组，无子节点。
#             - 只有一个元素，所以子节点是一个值为 1 的节点。
#     - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
#         - 只有一个元素，所以子节点是一个值为 0 的节点。
#         - 空数组，无子节点。
#           6
#        /    \
#       3      5
#        \    /
#         2  0
#          \
#           1
# 对于构造二叉树的问题，根节点要做的就是想办法把自己构造出来
def rec_construct_max_binary_tree(nums):
    if not nums:
        return None
    max_num = max(nums)
    max_idx = nums.index(max_num)
    root = BinaryTreeNode(max_num)
    root.left = rec_construct_max_binary_tree(nums[0:max_idx])
    root.right = rec_construct_max_binary_tree(nums[max_idx + 1:])
    return root


def rec1_construct_max_binary_tree(nums):
    if not nums:
        return None
    return build(nums, 0, len(nums) - 1)


def build(nums, low, high):
    if low > high:
        return None
    max_idx, max_num = -1, float('-inf')
    for i in range(low, high + 1):
        if max_num < nums[i]:
            max_idx = i
            max_num = nums[i]
    root = BinaryTreeNode(max_num)
    root.left = build(nums, low, max_idx - 1)
    root.right = build(nums, max_idx + 1, high)
    return root


# 单调栈解法。
#
# 以测试案例为例，一个输入序列：[3, 2, 1, 6, 0, 5]。 设置一个辅助栈，从大到小存储。 过程如下：
#
# 首先入栈3
# 2 比 3 小，入栈
# 1 比 2 小，入栈
# 6 大于1，因此要弹出1，1在2和6之间选择二者之间较小的元素作为父节点，因此选择2。1在2的右侧，使得1作为2的右子节点
# 弹出1后，6仍然比2大，同理2要在3和6之间选择一个作为父节点。3比6小，因此选择3。2在3的右侧，因此2作为3的右子节点
# 同理弹出3，让3作为6的左子节点
# 入栈6
# 入栈0
# 入栈5的时候比0大，要弹出0，选择5作为父节点，并且0是5的左孩子
# 弹出5，左侧是6，作为5的父节点
# 6最后弹出，就是根节点
def iter_construct_max_binary_tree(nums):
    if not nums:
        return None
    stack, curr = [], None
    for num in nums:
        curr = BinaryTreeNode(num)
        while stack and stack[-1].val < curr.val:
            top = stack.pop()
            if stack and stack[-1].val < curr.val:
                stack[-1].right = top
            else:
                curr.left = top
        stack.append(curr)
    # 遍历结束，栈中可能还有一些元素
    while stack:
        curr = stack.pop()
        if stack:
            stack[-1].right = curr

    return curr


if __name__ == '__main__':
    A = BinaryTree()
    arr = [3, 2, 1, 6, 0, 5]
    A.root = rec_construct_max_binary_tree(arr)
    print(preorder_morris(A.root))
    A.root = rec1_construct_max_binary_tree(arr)
    print(preorder_morris(A.root))
    A.root = iter_construct_max_binary_tree(arr)
    print(preorder_morris(A.root))
