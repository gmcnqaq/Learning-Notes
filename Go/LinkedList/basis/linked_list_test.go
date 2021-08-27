package basis

import (
	"fmt"
	"testing"
)

func TestLinkedList_Add(t *testing.T) {
	list := NewLinkedList(nil)
	list.Append(1)
	list.Append('a')
	list.Append("123")
	fmt.Printf("当前链表长度为：%d\n", list.Length())
	list.ShowList()
}

func TestLinkedList_IsEmpty(t *testing.T) {
	list1 := NewLinkedList(nil)
	list2 := NewLinkedList(nil)
	list1.Append(1)
	if err := list1.IsEmpty(); err != false {
		t.Fatalf("list1 should not be empty, but IsEmpty %t got\n", err)
	}
	if err := list2.IsEmpty(); err != true {
		t.Fatalf("list2 should be empty, but IsEmpty %t got\n", err)
	}
}

func TestCreateLinkedList(t *testing.T) {
	arr := []Object{1, 2, 3, "123", "456"}
	fmt.Println(len(arr))
	fmt.Println(arr)
	list := CreateLinkedList(arr, len(arr))
	list.ShowList()
}
