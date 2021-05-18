# 最长回文子串
# LeetCode 5
# 给你一个字符串 s，找到 s 中最长的回文子串。

# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"
# 示例 3：
# 输入：s = "a"
# 输出："a"
# 示例 4：
# 输入：s = "ac"
# 输出："a"
def longest_palindrome(s):
    n = len(s)
    if n < 2 or s == s[::-1]:
        return s

    start, max_len = 0, 1
    for i in range(1, n):
        odd = s[i - max_len - 1:i + 1]
        even = s[i - max_len:i + 1]
        if i - max_len - 1 >= 0 and odd == odd[::-1]:
            start = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and even == even[::-1]:
            start = i - max_len
            max_len += 1
    return s[start:start + max_len]

# TODO:
def longest_palindrome_ma(s):
    n = len(s)
    if n < 2:
        return n
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i - 1][j - 1] + 2


if __name__ == '__main__':
    s = 'babad'
    palindrome = longest_palindrome(s)
    print(palindrome)
