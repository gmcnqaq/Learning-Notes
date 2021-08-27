# LeetCode 912
# 排序数组
# 示例 1：
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
import time
import random
from typing import List
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} : {} ms'.format(func.__name__, (end - start) * 1000))
        return r

    return wrapper


# 交换排序

# 冒泡排序
# 每次找出一个最大的元素
# 时间复杂度度 O(n^2), 最好O(n)，空间复杂度 O(1)，稳定
@timethis
def bubble_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n - 1):  # 排序 n - 1 次
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# 选择排序
# 每次选出最小的元素
# 选择排序不受输入数据的影响，即在任何情况下时间复杂度不变。选择排序每次选出最小的元素，因此需要遍历 n-1 次。
# 时间复杂度 O(n^2)，最好 O(n^2)，空间复杂度 O(1)，不稳定
@timethis
def selection_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


# 插入排序
# 插入排序如同打扑克一样，每次将后面的牌插到前面已经排好序的牌中。
# 时间复杂度 O(n^2)，最好 O(n)，空间复杂度 O(1)，稳定
@timethis
def insertion_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        curr_num, prev_idx = nums[i + 1], i  # curr_num 保存当前插入的数
        while prev_idx >= 0 and curr_num < nums[prev_idx]:  # 将比 curr_num 大的元素向后移动
            nums[prev_idx + 1] = nums[prev_idx]
            prev_idx -= 1
        nums[prev_idx + 1] = curr_num
    return nums


# 希尔排序
# 希尔排序是插入排序的一种更高效率的实现。它与插入排序的不同之处在于，它会优先比较距离较远的元素。

# 【例子】对于待排序列 {44，12，59，36，62，43，94，7，35，52，85}，我们可设定增量序列为 {5，3，1}。
# 【解析】第一个增量为 5，因此 {44，43，85}、{12，94}、{59，7}、{36，35}、{62，52} 分别隶属于同一个子序列，子序列内部进行插入排序；然后选取第二个增量3，因此 {43，35，94，62}、{
# 12，52，59，85}、{7，44，36} 分别隶属于同一个子序列；最后一个增量为 1，这一次排序相当于简单插入排序，但是经过前两次排序，序列已经基本有序，因此此次排序时间效率就提高了很多。

# 希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列。
# 时间复杂度 O(n^1.3)，最好 O(n)，最坏 O(n^2)，空间复杂度 O(1)，不稳定
@timethis
def shell_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1  # 动态定义间隔序列
    while gap > 0:
        for i in range(gap, n):
            curr_num, prev_idx = nums[i], i - gap
            while prev_idx >= 0 and curr_num < nums[prev_idx]:
                nums[prev_idx + gap] = nums[prev_idx]
                prev_idx -= gap
            nums[prev_idx + gap] = curr_num
        gap //= 3
    return nums


# 归并排序
# 典型的分而治之思想的算法
# 自上而下的递归和自下而上的迭代
# 时间复杂度 O(nlogn),最好 O(nlogn)，空间复杂度 O(n)，稳定
def merge_sort(nums: List[int]) -> List[int]:
    def merge(nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                res.append(nums1.pop(0))
            else:
                res.append(nums2.pop(0))
        res += nums1 if nums1 else nums2
        return res

    n = len(nums)
    if n <= 1:
        return nums
    mid = n // 2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


# 快速排序
# 分而治之思想
# 时间复杂度 O(nlong)，最坏 O(n^2)，最好 O(nlogn)，空间复杂度 O(nlogn)，不稳定
def quick_sort(nums: List[int]) -> List[int]:
    randomized_quick_sort(nums, 0, len(nums) - 1)
    return nums


def randomized_quick_sort(nums: List[int], left: int, right: int):
    if left > right:
        return
    mid = randomized_partition(nums, left, right)
    randomized_quick_sort(nums, left, mid - 1)
    randomized_quick_sort(nums, mid + 1, right)


def randomized_partition(nums: List[int], left: int, right: int) -> int:
    pivot = random.randint(left, right)
    nums[pivot], nums[right] = nums[right], nums[pivot]
    i = left - 1
    for j in range(left, right):
        if nums[j] < nums[right]:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i


if __name__ == '__main__':
    nums = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print(bubble_sort(nums[:]))
    print(selection_sort(nums[:]))
    print(insertion_sort(nums[:]))
    print(shell_sort(nums[:]))
    print(merge_sort(nums[:]))
    print('quick_sort')
    print(quick_sort(nums[:]))
