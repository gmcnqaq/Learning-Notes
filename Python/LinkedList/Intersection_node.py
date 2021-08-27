from Python.LinkedList.basis.linked_list import ListNode, build_linked_list


# LeetCode 160
# 输入两个链表，找出它们的第一个公共节点。

def intersection_node(head1: ListNode, head2: ListNode) -> ListNode:
    h1, h2 = head1, head2
    while h1 != h2:
        h1 = h1.next if h1 else head2
        h2 = h2.next if h2 else head1
    return h1


if __name__ == '__main__':
    nums1 = [4, 1]
    nums2 = [5, 0, 1]
    nums_common = [8, 4, 5]
    l1 = build_linked_list(nums1)
    l2 = build_linked_list(nums2)
    common_list = build_linked_list(nums_common)
    l1.connect(common_list.head)
    l2.connect(common_list.head)
    print(l1.to_list())
    print(l2.to_list())
    inter_node = intersection_node(l1.head, l2.head)
    print(inter_node)
