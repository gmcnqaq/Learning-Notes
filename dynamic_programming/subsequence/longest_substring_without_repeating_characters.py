# 无重复字符的最长子串
# LeetCode 3
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

# 方法：滑动窗口

# 我们不妨以示例一中的字符串 abcabcbb 为例，找出从每一个字符开始的，不包含重复字符的最长子串，那么其中最长的那个字符串即为答案。
# 对于示例一中的字符串，我们列举出这些结果，其中括号中表示选中的字符以及最长的字符串：
"""
以 (a)bcabcbb 开始的最长字符串为 (abc)abcbb
以 a(b)cabcbb 开始的最长字符串为 a(bca)bcbb
以 ab(c)abcbb 开始的最长字符串为 ab(cab)cbb
以 abc(a)bcbb 开始的最长字符串为 abc(abc)bb
以 abca(b)cbb 开始的最长字符串为 abca(bc)bb
以 abcab(c)bb 开始的最长字符串为 abcab(cb)b
以 abcabc(b)b 开始的最长字符串为 abcabc(b)b
以 abcabcb(b) 开始的最长字符串为 abcabcb(b)
"""


def length_of_longest_substring(s):
    if not s:
        return 0
    left, length, dict_chr = -1, 0, {}
    start = 0
    for curr, value in enumerate(s):
        # 如果出现了重复字符，并且该位置在区间内
        if value in dict_chr and left < dict_chr[value]:
            left = dict_chr[value]  # 左端点指向上一次出现该字符的位置
        else:
            if length < curr - left:
                start = left + 1
                length = curr - left
        dict_chr[value] = curr
    return length, start


if __name__ == '__main__':
    s = 'abcabcbb'
    length, start = length_of_longest_substring(s)
    print(s[start: start + length])
    print(length)
