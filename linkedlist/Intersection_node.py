from linked_list_basis import *


# LeetCode 160
# 输入两个链表，找出它们的第一个公共节点。

def intersection_node(head1: ListNode, head2: ListNode) -> ListNode:
    h1, h2 = head1, head2

    while h1 != h2:
        h1 = h1.next if h1 else head2
        h2 = h2.next if h2 else head1

    return h1


if __name__ == '__main__':
    l1, l2 = LinkedList(), LinkedList()
    for i in range(3):
        l1.append(i)
    for i in range(2):
        l2.append(i)
    print(l1.to_list())
    print(l2.to_list())
    inter_node = intersection_node(l1.head, l2.head)
