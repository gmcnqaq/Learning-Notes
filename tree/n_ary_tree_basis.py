class NaryTreeNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __str__(self):
        return f'N-ary Tree Node (val: {self.val})'

    __repr__ = __str__()


class NaryTree(object):
    def __iter__(self, root=None):
        self.root = root


def build_tree_level(nums):
    pass


def preorder_rec(root):
    if not root:
        return []
    res = [root.val]
    for child in root.children:
        res.extend(preorder_rec(child))
    return res


def preorder_rec1(root):
    res = []

    def helper(root):
        if not root:
            return None
        res.append(root.val)
        for child in root.children:
            helper(child)

    helper(root)
    return res


def preorder_iter(root):
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        stack.extend(curr.children[::-1])
    return res


