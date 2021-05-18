# 扁平化嵌套列表迭代器
# LeetCode 341
# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
# 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
#
# 示例 1:
# 输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
# 示例 2:
# 输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedInteger(object):
    def __init__(self, val):
        self.val = None
        self.list = None
        if isinstance(val, int):
            self.val = val
        if isinstance(val, list):
            self.list = val

    def is_integer(self):
        return self.val is not None

    def get_integer(self):
        return self.val

    def get_list(self):
        return self.list


def build_nested_list(nums):
    i, n = 0, len(nums)
    while i < n:
        if isinstance(nums[i], int):
            nums[i] = NestedInteger(nums[i])
        else:
            first = nums.pop(i)
            nums.insert(i, NestedInteger(build_nested_list(first)))
        i += 1
    return nums


class NestedIterator(object):
    def __init__(self, nested_list):
        self.stack = nested_list

    def __iter__(self):
        return self

    # 返回下一个整数
    def __next__(self):
        if self.has_next():
            return self.stack.pop(0).get_integer()
        else:
            raise StopIteration

    # 是否还有下一个整数
    def has_next(self):
        while self.stack and not self.stack[0].is_integer():
            first = self.stack.pop(0).get_list()
            for i in range(len(first) - 1, -1, -1):
                self.stack.insert(0, first[i])
        return bool(self.stack)



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


if __name__ == '__main__':
    arr1 = [[1, 1], 2, [3, 3]]
    arr2 = [1, [4, [6]]]
    nested1 = build_nested_list(arr1)
    nested2 = build_nested_list(arr2)
    iter1 = NestedIterator(nested1)
    iter2 = NestedIterator(nested2)
    # while iter2.has_next():
    #     print(iter2.next())
    for i in iter2:
        print(i)

