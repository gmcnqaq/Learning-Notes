# 只出现一次的数字 II
# LeetCode 137
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
# 示例 1：
# 输入：nums = [2,2,3,2]
# 输出：3
# 示例 2：
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
import collections
from typing import List


def single_number(nums: List[int]) -> int:
    freq = collections.Counter(nums)
    ans = [num for num, occ in freq.items() if occ == 1][0]
    return ans


if __name__ == '__main__':
    nums = [0, 1, 0, 1, 9, 8, 9, 8, 12]
    print(single_number(nums))