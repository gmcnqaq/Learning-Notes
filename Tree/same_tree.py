from binary_tree_basis import BinaryTree
from binary_tree_basis import build_tree_level


# 100.
# 相同的树
# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# 示例 1：
# 输入：p = [1, 2, 3], q = [1, 2, 3]
# 输出：true
# 示例 2：
# 输入：p = [1, 2], q = [1, null, 2]
# 输出：false
def is_same_tree_dfs(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree_dfs(p.left, q.left) and is_same_tree_dfs(p.right, q.right)


def is_same_tree_bfs(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False

    queue1, queue2 = [p], [q]
    while queue1 and queue2:
        node1 = queue1.pop(0)
        node2 = queue2.pop(0)
        if node1.val != node2.val:
            return False
        l1, r1 = node1.left, node1.right
        l2, r2 = node2.left, node2.right
        if (not l1) ^ (not l2):
            return False
        if (not r1) ^ (not r2):
            return False
        if l1:
            queue1.append(l1)
        if r1:
            queue1.append(r1)
        if l2:
            queue2.append(l2)
        if r2:
            queue2.append(r2)
    return not queue1 and not queue2


if __name__ == '__main__':
    A = BinaryTree()
    B = BinaryTree()
    arr1 = [1, 2, 3, 4, 5]
    # arr2 = [2, 1, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5]
    A.root = build_tree_level(arr1)
    B.root = build_tree_level(arr2)
    print(is_same_tree_dfs(A.root, B.root))
    print(is_same_tree_bfs(A.root, B.root))