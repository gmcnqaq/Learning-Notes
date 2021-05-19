# LFU 缓存
# LeetCode 460

# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
# 实现 LFUCache 类：

# LFUCache(int capacity) - 用数据结构的容量capacity 初始化对象
# int get(int key)- 如果键存在于缓存中，则获取键的值，否则返回 -1。
# void put(int key, int value)-
# 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。

# 注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。
# 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
# 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。
from collections import defaultdict


class LFUCache(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(list)
        self.min_freq = 0
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self.increase_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key not in self.key_to_val:
            if self.size >= self.capacity:
                self.remove_min_freq_key()
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1].append(key)
            self.size += 1
            self.min_freq = 1
        else:
            self.key_to_val[key] = value
            self.increase_freq(key)

    def remove_min_freq_key(self):
        key_list = self.freq_to_keys.get(self.min_freq)
        # 最先插入的那个 key 就是被淘汰的 key
        delete_key = key_list.pop(0)
        if not key_list:
            self.freq_to_keys.pop(self.min_freq)
        # 更新 KV 表和 KF 表
        self.key_to_val.pop(delete_key)
        self.key_to_freq.pop(delete_key)
        self.size -= 1

    def increase_freq(self, key):
        # 更新 KF 表
        freq = self.key_to_freq.get(key)
        self.key_to_freq[key] += 1
        # 更新 FK 表
        # 将 key 从 freq 对应的列表中删除，然后加入到 freq + 1 的列表中
        self.freq_to_keys.get(freq).remove(key)
        self.freq_to_keys[freq + 1].append(key)
        # 如果 freq 对应的列表空了，移除这个 freq
        if not self.freq_to_keys.get(freq):
            self.freq_to_keys.pop(freq)
            if freq == self.min_freq:
                self.min_freq += 1


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
