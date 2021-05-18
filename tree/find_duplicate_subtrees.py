from binary_tree_basis import BinaryTree
from binary_tree_basis import preorder_morris

# 寻找重复的子树
# LeetCode 652
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
# 两棵树重复是指它们具有相同的结构以及相同的结点值。

# 示例 1：
#
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# 下面是两个重复的子树：
#
#       2
#      /
#     4
# 和
#
#     4
# 因此，你需要以列表的形式返回上述重复子树的根结点。
import collections


# 解法一：
# 两个问题
# 1. 如何指导以某个节点为根的这颗二叉树长啥样 ----> 序列化
# 2. 如何指导是否重复，其他节点长啥样 ---> count
def find_duplicate_subtrees(root):
    count = collections.Counter()
    ans = []

    def serialize(node):
        if not node:
            return "#"
        serial = "{},{},{}".format(node.val, serialize(node.left), serialize(node.right))
        count[serial] += 1
        if count[serial] == 2:
            ans.append(node)
        return serial

    serialize(root)
    return ans


# 解法二：
# 假设每棵子树都有一个唯一标识符：只有当两个子树的 id 相同时，认为这两个子树是相同的。
# 一个节点 node 的左孩子 id 为 x，右孩子 id 为 y，那么该节点的 id 为 (node.val, x, y)。
# 如果三元组 (node.val, x, y) 第一次出现，则创建一个这样的三元组记录该子树。如果已经出现过，则直接使用该子树对应的 id。
def find1_duplicate_subtrees(root):
    if not root:
        return None
    trees = collections.defaultdict()
    trees.default_factory = trees.__len__
    count = collections.Counter()
    ans = []

    def lookup(node):
        if node:
            uid = trees[node.val, lookup(node.left), lookup(node.right)]
            count[uid] += 1
            if count[uid] == 2:
                ans.append(node)
            return uid

    lookup(root)
    return ans
