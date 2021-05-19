from linked_list_basis import ListNode, build_linked_list


# LeetCode 92
# 反转链表 II

# 给你单链表的头指针 head 和两个整数left 和 right ，其中left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
# 示例 1：
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 示例 2：
# 输入：head = [5], left = 1, right = 1
# 输出：[5]

# 头插法
def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    if not head:
        return head
    dummy = ListNode(-1, head)
    prev_node = dummy
    for _ in range(left - 1):
        prev_node = prev_node.next
    curr_node = prev_node.next
    for _ in range(right - left):
        next_node = curr_node.next
        curr_node.next = next_node.next
        next_node.next = prev_node.next
        prev_node.next = next_node
    return dummy.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    L = build_linked_list(nums)
    print(L.to_list())
    L.head = reverse_between(L.head, 2, 4)
    print(L.to_list())
