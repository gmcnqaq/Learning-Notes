package basis

import "fmt"

type Object interface{}

type ListNode struct {
	Val  Object
	Next *ListNode
}

func NewListNode(Val Object, Next *ListNode) *ListNode {
	return &ListNode{
		Val:  Val,
		Next: Next,
	}
}

type LinkedList struct {
	Head *ListNode
}

func NewLinkedList(head *ListNode) *LinkedList {
	return &LinkedList{Head: head}
}

func CreateLinkedList(arr []Object, n int) *LinkedList {
	dummy := NewListNode(-1, nil)
	curr := dummy
	for i := 0; i < n; i++ {
		curr.Next = NewListNode(arr[i], nil)
		curr = curr.Next
	}
	list := NewLinkedList(dummy.Next)
	return list
}

func (l *LinkedList) IsEmpty() bool {
	if l.Head == nil {
		return true
	} else {
		return false
	}
}

func (l *LinkedList) Length() int {
	cnt := 0
	head := l.Head
	for head != nil {
		cnt++
		head = head.Next
	}
	return cnt
}

func (l *LinkedList) Append(val Object) {
	newNode := NewListNode(val, nil)
	if l.IsEmpty() {
		l.Head = newNode
	} else {
		head := l.Head
		for head.Next != nil {
			head = head.Next
		}
		head.Next = newNode
	}
}

func (l *LinkedList) Add(val Object) {
	node := NewListNode(val, nil)
	node.Next = l.Head
	l.Head = node
}

func (l *LinkedList) Insert(idx int, val Object) {
	if idx < 0 {
		fmt.Printf("the index %d is less than or equal to 0, the element will be inserted into the head of the linked list instead\n", idx)
		l.Add(val)
	} else if idx > l.Length() {
		fmt.Printf("the index %d is larger than the length of the linked list %d, the element will be inserted at the end of the linked list instead\n", idx, l.Length())
		l.Append(val)
	} else {
		cnt := 0
		head := l.Head
		for cnt < idx-1 {
			head = head.Next
			cnt++
		}
		node := NewListNode(val, nil)
		node.Next = head.Next
		head.Next = node
	}
}

func (l *LinkedList) Remove(val Object) bool {
	head := l.Head
	flag := false
	if head.Val == val {
		l.Head = head.Next
		flag = true
	} else {
		for head.Next != nil {
			if head.Next.Val == val {
				head.Next = head.Next.Next
				flag = true
			}
			head = head.Next
		}
	}
	return flag
}

func (l *LinkedList) ShowList() {
	if !l.IsEmpty() {
		head := l.Head
		for head != nil {
			fmt.Printf("%#v ", head.Val)
			head = head.Next
		}
		fmt.Printf("\n")
	}
}

func (l *LinkedList) Contain(val Object) bool {
	head := l.Head
	for head != nil {
		if head.Val == val {
			return true
		}
		head = head.Next
	}
	return false
}
