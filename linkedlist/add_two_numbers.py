from linked_list_basis import LinkedList, ListNode, build_linked_list


# LeetCode 2
# 两数相加
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例 1：
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]

# 加法的进位思想
def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_node = ListNode(-1)
    p = dummy_node
    carry = 0
    while l1 or l2:
        x, l1 = (l1.val, l1.next) if l1 else (0, l1)
        y, l2 = (l2.val, l2.next) if l2 else (0, l2)
        carry, val = divmod(x + y + carry, 10)
        p.next = ListNode(val)
        p = p.next
    if carry:
        p.next = ListNode(carry)
    return dummy_node.next


if __name__ == '__main__':
    nums1 = [2, 4, 9]
    nums2 = [5, 6, 4, 9]
    l1 = build_linked_list(nums1)
    l2 = build_linked_list(nums2)
    res = LinkedList()
    res.head = add_two_numbers(l1.head, l2.head)
    print(res.to_list())
