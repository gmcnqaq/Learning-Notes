# 跳跃游戏
# LeetCode 55
# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。
#
# 示例1：
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例2：
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
def can_jump(nums):
    n = len(nums)
    far = 0
    for i in range(n - 1):
        # 不断计算能够跳到的最远距离
        far = max(far, i + nums[i])
        # 可能碰到 0 了
        if far <= i:
            return False
    return far >= n - 1


def can_jump1(nums):
    n, far = len(nums), 0
    for i in range(n):
        if i <= far:
            far = max(far, i + nums[i])
            if far >= n - 1:
                return True
    return False


if __name__ == '__main__':
    arr = [0]
    print(can_jump(arr))
    print(can_jump1(arr))
