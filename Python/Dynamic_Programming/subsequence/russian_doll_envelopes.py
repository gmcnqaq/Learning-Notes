# 俄罗斯套娃信封问题
# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 注意：不允许旋转信封。
# 示例 1：
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
# 示例 2：
# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1

# 解法
# 先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度降序排序。之后把所有的 h 作为一个数组，在这个数组上计算 LIS 的长度就是答案
def max_envelopes(envelopes):
    if not envelopes:
        return 0
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    piles = []
    for n in envelopes:
        if not piles or n[-1] > piles[-1][-1]:
            piles.append(n)
        else:
            l, r = 0, len(piles) - 1
            loc = r
            while l <= r:
                mid = l + (r - l) // 2
                if piles[mid][-1] >= n[-1]:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1

            if piles[loc][-1] != n[-1]:
                piles[loc] = n
    return len(piles), piles


if __name__ == '__main__':
    env = [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]
    # env = [[5, 4], [6, 4], [6, 7], [2, 3]]
    length, envelope = max_envelopes(env)
    print(length)
    print(envelope)
