# 无重叠区间
# LeetCode 435
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
# 注意:
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
#
# 示例 1:
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 示例 2:
# 输入: [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 示例 3:
# 输入: [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
def erase_overlap_interval(intervals):
    # 对 end 按升序排序
    intervals.sort(key=lambda x: x[1])
    # 至少应该有一个区间不想交
    cnt = 1
    x_end = intervals[0][1]
    for interval in intervals:
        start = interval[0]
        if start >= x_end:
            cnt += 1
            x_end = interval[1]
    return len(intervals) - cnt


if __name__ == '__main__':
    arr = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(erase_overlap_interval(arr))
