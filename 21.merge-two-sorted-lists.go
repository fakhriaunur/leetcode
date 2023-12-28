/*
 * @lc app=leetcode id=21 lang=golang
 *
 * [21] Merge Two Sorted Lists
 */

package main

import "reflect"

/* *
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start
// func (l *ListNode) isEmpty() bool {
// 	return l.Val == 0 && *l.Next == (ListNode{})
// }

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := &ListNode{}
	curr := dummy

	// for list1.isEmpty() && list2.isEmpty() {
	// for *list1 != (ListNode{}) && *list2 != (ListNode{}) {
	for !reflect.DeepEqual(*list1, ListNode{}) &&
		!reflect.DeepEqual(*list2, ListNode{}) {
		if list1.Val <= list2.Val {
			curr = list1
			list1 = list1.Next
		} else {
			curr = list2
			list2 = list2.Next
		}
		curr = curr.Next
	}

	// if list1.isEmpty() {
	// if *list1 != (ListNode{}) {
	if !reflect.DeepEqual(*list1, ListNode{}) {
		curr.Next = list1
		// } else if list2.isEmpty() {
		// } else if *list2 != (ListNode{}) {
	} else if !reflect.DeepEqual(*list2, ListNode{}) {
		curr.Next = list2
	}

	return dummy.Next
}

// @lc code=end
