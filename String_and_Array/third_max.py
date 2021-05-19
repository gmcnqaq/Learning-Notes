# 第三大的数
# LeetCode 414
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

# 输入：[3, 2, 1]
# 输出：1
# 输入：[2, 2, 3, 1]
# 输出：1
# 解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
# 此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。

# 解法一：
def comp_third_max(nums):
    first = second = third = float('-inf')
    for num in nums:
        if num > third:
            if num < second:
                third = num
            elif num > second:
                if num < first:
                    third = second
                    second = num
                elif num > first:
                    third = second
                    second = first
                    first = num
    if third == float('-inf'):
        return first
    else:
        return third


# 维护一个大小为 3 的小顶堆
import heapq


def heap_third_max(nums):
    nums = set(nums)
    res = []
    for num in nums:
        heapq.heappush(res, num)
        if len(res) > 3:
            heapq.heappop(res)
    if len(res) < 3:
        for _ in range(len(res) - 1):
            heapq.heappop(res)
    return heapq.heappop(res)


# nlargest
def builtin_third_max(nums):
    nums = set(nums)
    three = heapq.nlargest(3, nums)
    return three[0] if len(three) < 3 else three[-1]


if __name__ == '__main__':
    arr = [2, 2, 3, 1]
    print(comp_third_max(arr))
    print(heap_third_max(arr))
    print(builtin_third_max(arr))
    arr = [1, 2, 2]
    print(comp_third_max(arr))
    print(heap_third_max(arr))
    print(builtin_third_max(arr))
