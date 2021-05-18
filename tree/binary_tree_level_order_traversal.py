from binary_tree_basis import BinaryTree, build_tree_level


# 102. 二叉树的层序遍历
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 示例：
# 二叉树：[3, 9, 20, null, null, 15, 7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层序遍历结果：
# [[3], [9, 20], [15, 7]]
def level_order(root):
    if not root:
        return []
    queue, res = [root], []
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.pop(0)
            level_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level_nodes)
    return res


if __name__ == '__main__':
    A = BinaryTree()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    A.root = build_tree_level(arr)
    print(level_order(A.root))
