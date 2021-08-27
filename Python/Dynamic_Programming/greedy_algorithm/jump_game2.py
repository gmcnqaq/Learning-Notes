# 跳跃游戏 II
# LeetCode 45
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 假设你总是可以到达数组的最后一个位置。
# 示例 1:
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。
# 示例 2:
# 输入: [2,3,0,1,4]
# 输出: 2
def jump(nums):
    n = len(nums)
    end = farthest = 0
    jumps = 0
    for i in range(n - 1):
        if farthest >= i:
            farthest = max(nums[i] + i, farthest)
            if end == i:
                jumps += 1
                end = farthest
    return jumps


if __name__ == '__main__':
    arr = [2, 3, 1, 2, 4, 2, 3]
    print(jump(arr))
