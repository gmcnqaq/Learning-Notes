# 分割等和子集
# LeetCode 416
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 示例 1：
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
# 示例 2：
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
def can_partition(nums):
    total = sum(nums)
    if total & 1:
        return False
    n = len(nums)
    total //= 2
    dp = [[False] * (total + 1) for _ in range(n + 1)]
    # base case
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if j - nums[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    return dp[n][total]


def can_partition_compress(nums):
    total, n = sum(nums), len(nums)
    if total & 1:
        return False
    total //= 2
    # dp = [False] * (total + 1)
    # dp[0] = True
    # for i in range(n):
    #     for j in range(total, 0, -1):
    #         if j - nums[i] >= 0:
    #             dp[j] = dp[j] or dp[j - nums[i]]
    dp = [True] + [False] * total
    for i, num in enumerate(nums):
        for j in range(total, num - 1, -1):
            dp[j] |= dp[j - num]
    return dp[total]


if __name__ == '__main__':
    # arr = [1, 5, 11, 5]
    arr = [1, 2, 3, 6]
    # arr = [9, 1, 2, 4, 10]
    print(can_partition(arr))
    print(can_partition_compress(arr))


