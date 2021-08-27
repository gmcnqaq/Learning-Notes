# 最长递增子序列
# LeetCode 300
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
# 示例 1：
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
def length_of_lis(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def length_of_lis_bisect(nums):
    d = []
    for n in nums:
        if not d or n > d[-1]:
            d.append(n)
        else:
            l, r = 0, len(d) - 1
            loc = r
            while l <= r:
                mid = l + (r - l) // 2
                if d[mid] >= n:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            d[loc] = n
    return len(d)


"""
def bisect_length_lis(nums):
    n = len(nums)
    top = [0] * n
    piles = 0
    for i in range(n):
        # 要处理的扑克牌
        poker = nums[i]
        # 搜索左侧边界的二分查找
        left, right = 0, piles
        while left < right:
            mid = left + (right - left) // 2
            if top[mid] >= poker:
                right = mid
            else:
                left = mid + 1
        # 没找到合适的牌堆，新建一堆
        if left == piles:
            piles += 1
        # 把这张牌放到牌堆顶
        top[left] = poker
    # 牌堆数就是 LIS 的长度
    return piles
"""

if __name__ == '__main__':
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(length_of_lis(arr))
    print(length_of_lis_bisect(arr))
