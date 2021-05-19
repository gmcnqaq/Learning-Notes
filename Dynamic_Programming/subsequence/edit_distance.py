# 编辑距离
# LeetCode 72
# 给你两个单词 word1 和 word2，请你计算出将 word1转换成 word2 所使用的最少操作数。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符

# 示例1：
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例2：
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')

# 不管是把 s1 变成 s2 还是反过来，结果都是一样的，所以可以只考虑把 s1 变成 s2
# 对一个字符串总共就只有三种操作：插入、删除、替换
# 当两个字符串某个字符相等的时候不用操作
# dp[i][j] 表示 word1 前 i 个字符和 word2 前 j 个字符的编辑距离，有：

# s1[i] == s2[j] 相等，不需要操作 --> dp[i][j] = dp[i - 1][j - 1]
# 插入，直接在 s1[i] 插入一个和 s2[j] 一样的字符，那么就和 s2[j] 匹配了，前移 j，继续跟 i 对比，操作数加一  --> dp[i][j] = dp[i][j - 1] + 1
# 删除直接把 s1[i] 删除，前移 i，继续跟 j 对比，操作数加一 --> dp[i][j] = dp[i - 1][j] + 1
# 替换，直接把 s1[i] 替换成为 s2[j]，同时前移 i, j 继续对比，操作数加一 --> dp[i][j] = dp[i - 1][j - 1] + 1
# base case dp[0][j] = j 和 dp[i][0] = i
def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    # 如果 m 和 n 有一个是空字符串
    if not m * n:
        return m + n
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # base case
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    # 状态转移
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                case_delete = dp[i - 1][j] + 1
                case_insert = dp[i][j - 1] + 1
                case_replace = dp[i - 1][j - 1] + 1
                dp[i][j] = min(case_delete, case_insert, case_replace)
    return dp[m][n]


# 状态压缩
def min_distance_compress(word1, word2):
    m, n = len(word1), len(word2)
    if not m * n:
        return m + n
    dp = [i for i in range(n + 1)]
    for i in range(1, m + 1):
        pre = i - 1
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = pre
            else:
                case_delete = dp[j] + 1
                case_insert = dp[j - 1] + 1
                case_replace = pre + 1
                dp[j] = min(case_delete, case_insert, case_replace)
            pre = temp
    return dp[n]


class Node(object):
    def __init__(self, val=0, choice=0):
        self.val = val
        self.choice = choice

    def __str__(self):
        return f'Node ({self.val}, {self.choice})'

    __repr__ = __str__


def min_distance_operate(word1, word2):
    print(word1, '--->', word2)
    # 0 -> nothing 1 -> delete 2 -> insert 3 -> replace
    m, n = len(word1), len(word2)
    # 如果 m 和 n 有一个是空字符串
    if not m * n:
        return m + n
    dp = [[Node() for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0].val = i
        dp[i][0].choice = 1
    for j in range(1, n + 1):
        dp[0][j].val = j
        dp[0][j].choice = 1
    # 状态转移
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j].val = dp[i - 1][j - 1].val
            else:
                choices = [dp[i - 1][j].val + 1,
                           dp[i][j - 1].val + 1,
                           dp[i - 1][j - 1].val + 1]
                dp[i][j].val = min(choices)
                dp[i][j].choice = choices.index(dp[i][j].val) + 1
    operations = []
    while m > 0 and n > 0:
        if dp[m][n].choice == 0:
            m -= 1
            n -= 1
        if dp[m][n].choice == 1:
            operations.append('delete {}th {}'.format(m, word1[m - 1]))
            m -= 1
        if dp[m][n].choice == 2:
            operations.append('insert {}th {}'.format(m, word2[n - 1]))
            n -= 1
        if dp[m][n].choice == 3:
            operations.append('replace {}th {} to {}'.format(m, word1[m - 1], word2[n - 1]))
            m -= 1
            n -= 1
    return ', '.join(operations)


if __name__ == '__main__':
    str1 = 'I hace a draem'
    str2 = 'I have a dream'
    print(min_distance(str1, str2))
    print(min_distance_compress(str1, str2))
    print(min_distance_operate(str1, str2))


