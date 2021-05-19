class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'Linked List Node (val: {self.val})'

    __repr__ = __str__


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def size(self):
        cnt = 0
        head = self.head
        while head:
            cnt += 1
            head = head.next
        return cnt

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            head = self.head
            while head.next:
                head = head.next
            head.next = new_node

    def add(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        res = []
        head = self.head
        while head:
            res.append(head.val)
            head = head.next
        return res

    def connect(self, head1):
        head = self.head
        while head.next:
            head = head.next
        head.next = head1


def build_linked_list(nums=[]):
    L = LinkedList()
    for num in nums:
        L.append(num)
    return L


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    l = build_linked_list(nums)
    print(l.to_list())
    print(l.size())
    l.append(5)
    l.add(0)
    print(l.to_list())
