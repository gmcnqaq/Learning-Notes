from binary_tree_basis import BinaryTree, BinaryTreeNode
from binary_tree_basis import preorder_morris, build_tree_level


# 二叉树的序列化与反序列化
# LeetCode 297
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
class Codec(object):
    def serialize_pre(self, root):
        """
        Encode a binary tree to a single string
        :param root:BinaryTreeNode
        :return:str
        """
        if not root:
            return '#'
        serial = '{},{},{}'.format(root.val, self.serialize_pre(root.left),
                                   self.serialize_pre(root.right))
        return serial

    def deserialize_pre(self, data):
        if not data:
            return None
        nodes = data.split(',')
        root = self.build_tree(nodes, 0)
        return root

    def build_tree(self, data, idx):
        val = data.pop(idx)
        if val == '#':
            return None
        root = BinaryTreeNode(int(val))
        if idx == -1:
            root.right = self.build_tree(data, idx)
        root.left = self.build_tree(data, idx)
        if idx == 0:
            root.right = self.build_tree(data, idx)
        return root

    def serialize_post(self, root):
        if not root:
            return '#'
        serial = '{},{},{}'.format(self.serialize_post(root.left),
                                   self.serialize_post(root.right), root.val)
        return serial

    def deserialize_post(self, data):
        if not data:
            return None
        nodes = data.split(',')
        root = self.build_tree(nodes, -1)
        return root

    def serialize_level(self, root):
        if not root:
            return '#'
        queue = [root]
        res = []
        while queue:
            curr = queue.pop(0)
            if not curr:
                res.append('#')
                continue
            res.append(str(curr.val))
            queue.append(curr.left)
            queue.append(curr.right)
        return ','.join(res)

    def deserialize_level(self, data):
        if not data:
            return None
        values = [int(i) if i != '#' else None for i in data.split(',')]
        root = BinaryTreeNode(values[0])
        queue = [root]
        i, nodes_len = 1, len(values)
        while i < nodes_len:
            node = queue.pop(0)
            if values[i] is not None:
                left = BinaryTreeNode(values[i])
                queue.append(left)
                node.left = left
            i += 1
            if i >= nodes_len:
                break
            if values[i] is not None:
                right = BinaryTreeNode(values[i])
                queue.append(right)
                node.right = right
            i += 1
        return root


if __name__ == '__main__':
    A = BinaryTree()
    # arr = [1, 2, 3, None, 4]
    arr = [1, 2, 3, None, None, 4, 5, 6, 7]
    A.root = build_tree_level(arr)
    print(preorder_morris(A.root))
    codes = Codec()
    serial = codes.serialize_pre(A.root)
    print(serial)
    A.root = codes.deserialize_pre(serial)
    print(preorder_morris(A.root))
    serial = codes.serialize_post(A.root)
    print(serial)
    A.root = codes.deserialize_post(serial)
    print(preorder_morris(A.root))
    serial = codes.serialize_level(A.root)
    print(serial)
    A.root = codes.deserialize_level(serial)
    print(preorder_morris(A.root))
