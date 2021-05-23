# 合并K个升序链表
# LeetCode 23
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 示例 1：
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：
# 输入：lists = []
# 输出：[]
# 示例 3：
# 输入：lists = [[]]
# 输出：[]
import heapq
from linked_list_basis import LinkedList, \
    build_linked_list, \
    ListNode


def merge_k_lists_partition(lists):
    def merge_two_lists(head1, head2):
        if not head1 or not head2:
            return head1 if head1 else head2
        dummy_node = ListNode(-1)
        temp, temp1, temp2 = dummy_node, head1, head2
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        temp.next = temp1 if temp1 else temp2
        return dummy_node.next

    def merge(lists, left, right):
        if left == right:
            return lists[left]
        if left > right:
            return None
        mid = left + (right - left) // 2
        l1 = merge(lists, left, mid)
        l2 = merge(lists, mid + 1, right)
        return merge_two_lists(l1, l2)

    if not lists:
        return None
    n = len(lists)
    return merge(lists, 0, n - 1)


def merge_k_lists_priority_queue(lists):
    heap = []
    dummy_node = ListNode(-1)
    head = dummy_node
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next
    while heap:
        val, idx = heapq.heappop(heap)
        head.next = ListNode(val)
        head = head.next
        if lists[idx]:
            heapq.heappush(heap, (lists[idx].val, idx))
            lists[idx] = lists[idx].next
    return dummy_node.next


# 猴子补丁，自定义排序
def merge_k_lists_monkey(lists):
    def __lt__(self, other):
        return self.val < other.val

    ListNode.__lt__ = __lt__

    heap = []
    dummy = ListNode(-1)
    p = dummy

    for lst in lists:
        if lst:
            heapq.heappush(heap, lst)
    while heap:
        node = heapq.heappop(heap)
        p.next = ListNode(node.val)
        p = p.next
        if node.next:
            heapq.heappush(heap, node.next)

    return dummy.next


if __name__ == '__main__':
    nums = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [build_linked_list(i).head for i in nums]
    lst = LinkedList()
    # lst.head = merge_k_lists_partition(lists)
    # print(lst.to_list())
    # lst.head = merge_k_lists_priority_queue(lists)
    # print(lst.to_list())
    lst.head = merge_k_lists_monkey(lists)
    print(lst.to_list())
