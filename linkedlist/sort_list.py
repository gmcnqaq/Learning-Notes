import heapq
from linked_list_basis import ListNode, build_linked_list


# LeetCode 148
# 排序链表
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 示例 1：
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
# 示例 2：
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
# 示例 3：
# 输入：head = []
# 输出：[]

# 自顶向下归并排序
# 找到链表的中点，以中点为分解，将链表拆分为两个子链表，对子链表排序，然后合并
def sort_list_td(head: ListNode) -> ListNode:
    def merge(head: ListNode, tail: (ListNode, None)) -> ListNode:
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return merge_two_lists(merge(head, mid), merge(mid, tail))

    return merge(head, None)


def merge_two_lists(head1: ListNode, head2: ListNode) -> ListNode:
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


# 自底向上归并排序
# 首先获得链表的长度，然后将链表拆分成子链表进行合并
# 1. 用 sub_length 表示每次要排序的子链表的长度，初始时候 sub_length = 1
# 2. 每次将链表拆分成若干长度为 sub_length 的子链表（最后一个子链表的长度可以小于 sub_length），按照每两个子链表一组进行合并，合并后即可得到若干个长度为 subLength×2 的有序子链表
# 3. 将 sub_length 的长度加倍，直至有序子链表的长度大于或等于 length
def sort_list_dt(head: ListNode) -> ListNode:
    if not head:
        return head
    length = 0
    node = head
    while node:
        length += 1
        node = node.next
    dummy_node = ListNode(-1, head)
    sub_length = 1
    while sub_length < length:
        prev, curr = dummy_node, dummy_node.next
        while curr:
            head1 = curr
            for i in range(1, sub_length):
                if curr.next:
                    curr = curr.next
                else:
                    break
            head2 = curr.next
            curr.next = None
            curr = head2
            for i in range(1, sub_length):
                if curr and curr.next:
                    curr = curr.next
                else:
                    break
            succ = None
            if curr:
                succ = curr.next
                curr.next = None

            merged = merge_two_lists(head1, head2)
            prev.next = merged
            while prev.next:
                prev = prev.next
            curr = succ
        sub_length <<= 1
    return dummy_node.next


# 也可以猴子补丁加堆排
def sort_list_monkey(head: ListNode) -> ListNode:
    def __lt__(self, other):
        return self.val < other.val

    ListNode.__lt__ = __lt__
    heap = []
    dummy_node = ListNode(-1)
    curr = dummy_node
    while head:
        heapq.heappush(heap, head)
        head = head.next
    while heap:
        curr.next = heapq.heappop(heap)
        curr = curr.next
    curr.next = None
    return dummy_node.next


if __name__ == '__main__':
    nums = [-1, 5, 3, 4, 0]
    l = build_linked_list(nums)
    # l.head = sort_list_td(l.head)
    l.head = sort_list_dt(l.head)
    # l.head = sort_list_monkey(l.head)
    print(l.to_list())
