# 寻找两个正序数组的中位数
# LeetCode 4
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。
# 示例 1：
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 示例 3：
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
# 示例 4：
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
# 示例 5：
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
def find_median_sorted_arrays(nums1, nums2):
    def get_kth_number(k):
        idx1 = idx2 = 0
        while True:
            if idx1 == m:
                return nums2[idx2 + k - 1]
            if idx2 == n:
                return nums1[idx1 + k - 1]
            if k == 1:
                return min(nums1[idx1], nums2[idx2])

            new_idx1 = min(idx1 + k // 2 - 1, m - 1)
            new_idx2 = min(idx2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[new_idx1], nums2[new_idx2]
            if pivot1 <= pivot2:
                k -= new_idx1 - idx1 + 1
                idx1 = new_idx1 + 1
            else:
                k -= new_idx2 - idx2 + 1
                idx2 = new_idx2 + 1

    m, n = len(nums1), len(nums2)
    total_len = m + n
    if total_len & 1:
        return get_kth_number((total_len + 1) // 2)
    else:
        return (get_kth_number(total_len // 2) + get_kth_number(total_len // 2 + 1)) / 2


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]
    nums2 = [2, 6, 7, 9]
    print(find_median_sorted_arrays(nums1, nums2))