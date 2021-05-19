## 子序列解题模板
这类问题一般都是求一个**最长**的子序列，时间复杂度一般都是**O(n^2)**

### 两种思路
1. 第一种思路模板是一个一维的 dp 数组
```
n = len(arr)
dp = [0] * n
for i in range(1, n):
    for j in range(i):
        dp[i] = 最值(dp[i], dp[j] + ...)
```
例子：最长递增子序列
```
def length_of_lis(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```
在这个思路中 dp 数组的定义是：

**在子数组 `array[0...i]` 中， 以 `array[i]` 结尾的目标子序列（最长递增子序列） 的长度是 `dp[i]`**

2. 第二种思路是一个二维的 dp 数组

```
n = len(arr)
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(1, n):
        if arr[i] == arr[j]:
            dp[i][j] == dp[i][j] + ..
        else:
            dp[i][j] = 最值(....)
```
2.1 涉及两个字符串/数组

dp 数组的含义：**在子数组`arr1[0...i]` 和 `arr2[0...j]` 中，我们要求的子序列长度为 `dp[i][j]`**

例子：最长公共子序列 LCS

2.2 只涉及一个字符串/数组

dp 数组的含义：**在子数组 `array[i...j]` 中，我们要求的子序列的长度为 `dp[i][j]`**

例子：最长回文子序列
