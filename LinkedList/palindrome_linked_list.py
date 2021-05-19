from linked_list_basis import ListNode, build_linked_list


# LeetCode 234
# 回文链表
# 请判断一个链表是否为回文链表。
# 示例 1:
# 输入: 1->2
# 输出: false
# 示例 2:
# 输入: 1->2->2->1
# 输出: true

# 双指针
def is_palindrome(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    fast = None
    while slow:
        temp = slow.next
        slow.next = fast
        fast = slow
        slow = temp
    while fast:
        if fast.val != head.val:
            return False
        else:
            head = head.next
            fast = fast.next
    return True


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 3, 2, 1]
    l = build_linked_list(nums)
    print(l.to_list())
    print(is_palindrome(l.head))
    print(l.to_list())
