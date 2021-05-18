# 最大子序和
# LeetCode 53
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：
# 输入：nums = [1]
# 输出：1
# 示例 3：
# 输入：nums = [0]
# 输出：0
def max_subarray(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    return max(dp)


def max_subarray_compress(nums):
    n = len(nums)
    dp0 = nums[0]
    dp1, res = 0, dp0
    for i in range(1, n):
        dp1 = max(nums[i], nums[i] + dp0)
        dp0 = dp1
        res = max(dp1, res)
    return res


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(arr))
    print(max_subarray_compress(arr))
