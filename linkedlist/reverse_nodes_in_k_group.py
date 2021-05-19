from linked_list_basis import ListNode, build_linked_list


# LeetCode 25
# K 个一组翻转链表
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
def reverse_k_group(head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    # 区间[temp1, temp2) 包含 k 个待反转元素
    temp1 = temp2 = head
    for i in range(k):
        if not temp2:
            return head
        temp2 = temp2.next
    new_head = reverse(temp1, temp2)
    temp1.next = reverse_k_group(temp2, k)
    return new_head


def reverse(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l1
    prev = None
    while l1 != l2:
        temp = l1.next
        l1.next = prev
        prev = l1
        l1 = temp
    return prev


def reverse_k_group_iter(head: ListNode, k: int):
    stack = []
    dummy = p = ListNode(-1)

    while head:
        for i in range(k):
            if not head:
                return dummy.next
            stack.append(head)
            head = head.next
        while stack:
            cur = stack.pop()
            p.next = cur
            p = cur
        p.next = head
    return dummy.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    k = 2
    l = build_linked_list(nums)
    l.head = reverse_k_group(l.head, k)
    print(l.to_list())
    l.head = reverse_k_group_iter(l.head, 2)
    print(l.to_list())
