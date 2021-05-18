from binary_tree_basis import BinaryTree
from binary_tree_basis import build_tree_level


# 对称二叉树
# LeetCode 101
# 判断一棵二叉树是不是对称的
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true

def rec_is_symmetric(root):
    if not root:
        return True

    def dfs(left, right):
        # 两个节点都为空
        if not (left or right):
            return True
        # 两个节点有一个一空
        if not (left and right):
            return False
        # 两个节点的值不相等
        if left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)
    return dfs(root.left, root.right)


def iter_is_symmetric(root):
    if not root or not (root.left or root.right):
        return True
    queue = [root.left, root.right]
    while queue:
        left = queue.pop(0)
        right = queue.pop(0)
        # 如果两个节点都为空就继续循环，两者有一个为空就返回false
        if not (left or right):
            continue
        if not (left and right):
            return False
        if left.val != right.val:
            return False

        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
    return True


if __name__ == '__main__':
    A = BinaryTree()
    nums = [1, 2, 2, 3, 4, 4, 3]
    A.root = build_tree_level(nums)
    print(rec_is_symmetric(A.root))
    print(iter_is_symmetric(A.root))
    B = BinaryTree()
    arr = [1, 2, 2, None, 3, None, 3]
    B.root = build_tree_level(arr)
    print(iter_is_symmetric(B.root))
