class BinaryTreeNode(object):
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'Binary Tree Node (val: {self.val})'

    __repr__ = __str__


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def find_val_level(self, val):
        if not val:
            return None
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None


def build_tree_level(nums):
    if not nums:
        return None
    root = BinaryTreeNode(nums[0])
    queue = [root]
    i, length = 1, len(nums)
    while i < length:
        parent = queue.pop(0)
        left = nums[i]
        i += 1
        if left is not None:
            parent.left = BinaryTreeNode(left)
            queue.append(parent.left)
        right = nums[i]
        i += 1
        if right is not None:
            parent.right = BinaryTreeNode(right)
            queue.append(parent.right)
    return root


# 递归
def rec_preorder(root):
    # base case
    if not root:
        return []
    return [root.val] + rec_preorder(root.left) + rec_preorder(root.right)


def rec_inorder(root):
    if not root:
        return []
    return rec_inorder(root.left) + [root.val] + rec_inorder(root.right)


def rec_postorder(root):
    if not root:
        return []
    return rec_postorder(root.left) + rec_postorder(root.right) + [root.val]


# 使用栈进行迭代
def iter_preorder(root):
    if not root:
        return []
    stack, res = [root, ], []
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:  # 右孩子入栈
            stack.append(curr.right)
        if curr.left:  # 左孩子入栈
            stack.append(curr.left)
    return res


def iter_postorder(root):
    if not root:
        return []
    stack, res = [root, ], []
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return res[::-1]


def level_order(root):
    if not root:
        return []
    queue, res = [root], []
    while queue:
        curr = queue.pop(0)
        res.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return res


# 迭代模板
# 先将根节点 curr 和所有左孩子入栈，直至 curr 为空， 然后每弹出一个栈顶元素，就到达他的右孩子
def iter1_preorder(root):
    if not root:
        return []
    curr, stack, res = root, [], []
    while curr or stack:
        while curr:  # 根节点和左孩子入栈
            res.append(curr.val)
            stack.append(curr)
            curr = curr.left
        temp = stack.pop()  # 每弹出一个元素就到达右孩子
        curr = temp.right
    return res


def iter_inorder(root):
    if not root:
        return []
    curr, stack, res = root, [], []
    while curr or stack:
        while curr:  # curr 入栈，并到达最左端的叶子结点
            stack.append(curr)
            curr = curr.left
        temp = stack.pop()
        res.append(temp.val)
        curr = temp.right
    return res


def iter1_postorder(root):
    if not root:
        return []
    curr, stack, res = root, [], []
    while curr or stack:
        while curr:  # 先到达最右端
            res.append(curr.val)
            stack.append(curr)
            curr = curr.right
        temp = stack.pop()
        curr = temp.left
    return res[::-1]


# Morris 遍历
# 整体思路就是 以某个根结点开始，找到它左子树的最右侧节点之后与这个根结点进行连接
# Morris 遍历的核心思想是利用树的大量空闲指针，实现空间开销的极限缩减。其前序遍历规则总结如下：
# 1. 新建临时节点，令该节点为 root；
# 2. 如果当前节点的左子节点为空，将当前节点加入答案，并遍历当前节点的右子节点；
# 3. 如果当前节点的左子节点不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点：（当前节点的左子树中找到当前节点在中序遍历下的前驱节点 ==> 左子树的最右侧节点）
# 3.1 如果前驱节点的右子节点为空，将前驱节点的右子节点设置为当前节点。然后将当前节点加入答案，并将前驱节点的右子节点更新为当前节点。当前节点更新为当前节点的左子节点。
# 3.2 如果前驱节点的右子节点为当前节点，将它的右子节点重新设为空。当前节点更新为当前节点的右子节点。
# 4. 重复步骤 2 和步骤 3，直到遍历结束。
def preorder_morris(root):
    if not root:
        return []
    res = []
    p1 = root  # 当前开始遍历的节点
    while p1:
        p2 = p1.left  # 记录当前节点的左子树
        if p2:
            # 找到当前左子树的最右侧节点，且这个节点应该在指向根节点之前，否则整个节点又回到了根节点
            while p2.right and p2.right != p1:
                p2 = p2.right
            # 这个时候如果最右侧这个节点的右指针没有指向根节点，创建连接然后往下一个左子树的根节点进行连接操作
            if not p2.right:
                res.append(p1.val)
                p2.right = p1
                p1 = p1.left
                continue
            # 当左子树的最右侧节点有指向根结点，此时说明我们已经回到了根结点并重复了之前的操作，同时在回到根结点的时候我们应该已经处理完 左子树的最右侧节点 了，把路断开。
            else:
                p2.right = None
        else:
            res.append(p1.val)
        p1 = p1.right  # 一直往右边走
    return res


def inorder_morris(root):
    if not root:
        return []
    res = []
    p1 = root
    while p1:
        p2 = p1.left
        if p2:
            while p2.right and p2.right != p1:
                p2 = p2.right
            if not p2.right:
                p2.right = p1
                p1 = p1.left
                continue
            else:
                p2.right = None
        res.append(p1.val)
        p1 = p1.right
    return res


def postorder_morris(root):
    def add_path(node):
        cnt = 0
        while node:
            cnt += 1
            res.append(node.val)
            node = node.right
        i, j = len(res) - cnt, len(res) - 1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1

    if not root:
        return []
    res = []
    p1 = root
    while p1:
        p2 = p1.left
        if p2:
            while p2.right and p2.right != p1:
                p2 = p2.right
            if not p2.right:
                p2.right = p1
                p1 = p1.left
                continue
            else:
                p2.right = None
                add_path(p1.left)
        p1 = p1.right
    add_path(root)
    return res


# Binary Search Tree
def is_in_bst(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    if root.val < target:
        return is_in_bst(root.right, target)
    if root.val > target:
        return is_in_bst(root.left, target)


# def bst(root, target):
#     if root.val == target:
#         # 找到目标，做点什么
#     if root.val > target:
#         bst(root.left, target)
#     if root.val < target:
#         bst(root.right, target)
def insert_into_bst(root, target):
    if not root:
        return BinaryTreeNode(target)
    if root.val < target:
        root.right = insert_into_bst(root.right, target)
    if root.val > target:
        root.left = insert_into_bst(root.left, target)
    return root


def delete_bst_node(root, target):
    if not root:
        return None  # 说明要删除的元素未找到
    if target < root.val:
        root.left = delete_bst_node(target, root.left)  # 左子树递归删除
    elif target > root.val:
        root.right = delete_bst_node(target, root.right)  # 右子树递归删除
    else:  # 说明已经找到要删除的结点了
        if not root.left:  # 只有右子树或者没有子结点
            return root.right
        elif not root.right:  # 只有左子树
            return root.left
        else:  # 有左右两个结点
            temp = find_min_bst(root.right)  # 在右子树中找到最小的元素
            # 一般不这么操作， val 域 可能会是一个复杂的数据结构，这里简化
            root.val = temp.val
            root.right = delete_bst_node(temp.val, root.right)
    return root


def find_min_bst(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root


# 求二叉树的节点数
# 普通二叉树
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# 满二叉树
def count_nodes_perfect(root):
    if not root:
        return 0
    h, curr = 0, root
    while curr:
        curr = curr.left
        h += 1
    # 节点总数就是 2^h - 1
    return pow(2, h) - 1


# 完全二叉树
def count_nodes_complete(root):
    l, r = root, root
    hl, hr = 0, 0
    while l:
        l = l.left
        hl += 1
    while r:
        r = r.right
        hr += 1
    # 如果左右子树的高度相同，则是一棵满二叉树
    if hr == hl:
        return pow(2, hl) - 1
    # 如果左右高度不同，则按照普通二叉树的逻辑计算
    # 一棵完全二叉树的两棵子树，至少有一棵是满二叉树
    return 1 + count_nodes_complete(root.left) + count_nodes_complete(root.right)


if __name__ == '__main__':
    node = BinaryTreeNode(1)
    print(node)
    A = BinaryTree()
    nums = [1, 2, None, 4, 5, 6, 7]
    A.root = build_tree_level(nums)
    print('前序遍历：', preorder_morris(A.root))
    print('中序遍历：', inorder_morris(A.root))
    print('后序遍历：', postorder_morris(A.root))
    print('层次遍历：', level_order(A.root))
