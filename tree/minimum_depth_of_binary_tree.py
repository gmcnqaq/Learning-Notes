from binary_tree_basis import BinaryTree, build_tree_level


# 二叉树的最小深度
# LeetCode 111

# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明：叶子节点是指没有子节点的节点。
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
def min_depth(root):
    if not root:
        return 0
    queue = [(root, 1)]
    while queue:
        curr, h = queue.pop(0)
        if not curr.left and not curr.right:
            return h
        if curr.left:
            queue.append((curr.left, h + 1))
        if curr.right:
            queue.append((curr.right, h + 1))


if __name__ == '__main__':
    A = BinaryTree()
    arr = [1, 2, 3, 4, 5]
    A.root = build_tree_level(arr)
    print(min_depth(A.root))
