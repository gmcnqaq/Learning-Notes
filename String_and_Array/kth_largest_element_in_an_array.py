# LeetCode 215
# 数组中的第K个最大元素
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 示例 1:
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例2:
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
import heapq
import random
from typing import List


# 维护大小为 k 的最小堆
def find_kth_largest_heap(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)


# 快速选择算法
def find_kth_largest_quick(nums: List[int], k: int) -> int:
    n = len(nums)
    low, high = 0, n - 1
    # 索引转化
    k = n - k
    while low <= high:
        p = partition(nums, low, high)
        if p < k:
            low = p + 1
        elif p > k:
            high = p - 1
        else:
            return nums[p]
    return -1


def partition(nums: List[int], low: int, high: int):
    # 将 nums[low] 作为默认的分界点 pivot
    pivot = nums[low]
    while flag := (low < high):
        while flag and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]  # 比基准小的交换到前面
        while flag and nums[low] <= pivot:
            low += 1
        nums[high] = nums[low]  # 比基准大交换到后面
    nums[low] = pivot # 基准值的正确位置
    return low


def shuffle(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        rand = random.randint(i, n - 1)
        nums[i], nums[rand] = nums[rand], nums[i]
    return nums


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(find_kth_largest_heap(nums, k))
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(find_kth_largest_heap(nums, k))
