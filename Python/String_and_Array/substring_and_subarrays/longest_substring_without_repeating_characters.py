# LeetCode 3
# 无重复字符的最长子串
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
#     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 示例 4:
# 输入: s = ""
# 输出: 0


# 滑动窗口

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


def length_of_longest_substring(s: str) -> int:
    left, length = -1, 0
    chr_dict = {}
    for i, c in enumerate(s):
        if c in chr_dict and left < chr_dict[c]:  # 如果出现了重复字符，并且该字符在考虑的区间内
            left = chr_dict[c]
            chr_dict[c] = i
        else:
            chr_dict[c] = i
            length = max(length, i - left)
    print(chr_dict)
    return length


if __name__ == '__main__':
    string = 'abcabcbb'
    # string = 'pwwkew'
    print(length_of_longest_substring(string))
