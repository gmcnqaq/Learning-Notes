# 最长公共子序列
# LeetCode 1143
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
# 示例 1：
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
# 示例 2：
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
# 示例 3：
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    if not m * n:
        return m + n
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # return dp[m][n], dp
    res = []

    def get_lcs(m, n, s):
        while m > 0 and n > 0:
            if text1[m - 1] == text2[n - 1]:
                s += text1[m - 1]
                m -= 1
                n -= 1
            else:
                if dp[m - 1][n] > dp[m][n - 1]:
                    m -= 1
                elif dp[m - 1][n] < dp[m][n - 1]:
                    n -= 1
                else:
                    get_lcs(m - 1, n, s)
                    get_lcs(m, n - 1, s)
                    return
        res.append(s[::-1])

    get_lcs(m, n, '')
    return dp[m][n], ','.join(res)


def longest_common_subsequence_compress(text1, text2):
    m, n = len(text1), len(text2)
    if not m * n:
        return m + n
    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        pre = 0
        for j in range(1, n + 1):
            temp = dp[j]
            if text1[i - 1] == text2[j - 1]:
                dp[j] = pre + 1
            else:
                dp[j] = max(dp[j - 1], dp[j])
            pre = temp
    return dp[n]


# 两个字符串的删除操作
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

# 最终删除的结果就是这两个字符串的最长公共子序列
def min_distance(text1, text2):
    m, n = len(text1), len(text2)
    lcs = longest_common_subsequence_compress(text1, text2)
    return m - lcs + n - lcs


if __name__ == '__main__':
    text1 = 'ABCBDAB'
    text2 = 'BDCABA'
    length, lcs = longest_common_subsequence(text1, text2)
    print(length)
    print(longest_common_subsequence_compress(text1, text2))
    print(lcs)
    print(min_distance(text1, text2))
