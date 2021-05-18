class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


if __name__ == '__main__':
    a = 1

