# 最长回文子序列
# LeetCode 516
# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
# 示例 1:
# 输入: "bbbab"
# 输出: 4
# 一个可能的最长回文子序列为 "bbbb"。
# 示例 2:
# 输入: "cbbd"
# 输出: 2
# 一个可能的最长回文子序列为 "bb"。
def longest_palindrome_subsequence(s):
    if not s:
        return 0
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    print(dp)
    return dp[0][n - 1]


def longest_palindrome_subsequence_compress(s):
    if not s:
        return 0
    n = len(s)
    dp = [1] * n
    for i in range(n - 2, -1, -1):
        pre = 0
        for j in range(i + 1, n):
            temp = dp[j]
            if s[i] == s[j]:
                dp[j] = pre + 2
            else:
                dp[j] = max(dp[j], dp[j - 1])
            pre = temp
    return dp[n - 1]


if __name__ == '__main__':
    s = 'bbbab'
    print(longest_palindrome_subsequence(s))
    print(longest_palindrome_subsequence_compress(s))
