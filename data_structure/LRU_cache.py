# LRU 缓存机制
# LeetCode 146
# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以正整数作为容量capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value)如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
class DLintNode(object):
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = DLintNode()
        self.tail = DLintNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.make_recently(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLintNode(key, value)
            self.add_recently(node)
            self.cache[key] = node
            if self.size > self.capacity:
                # 删除该节点
                least_recently = self.remove_least_recently()
                # 并同时删除哈希表中对应的项
                self.cache.pop(least_recently.key)
        else:
            node = self.cache[key]
            node.val = value
            self.make_recently(node)

    def make_recently(self, node):
        self.delete_node(node)
        self.add_recently(node)

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def add_recently(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def remove_least_recently(self):
        node = self.head.next
        self.delete_node(node)
        return node
