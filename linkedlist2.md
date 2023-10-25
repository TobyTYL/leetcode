# Day 4 Linked List
- [x] LC 24, 19, 142; Interview question 02.07

## LC 24. Swap Nodes in Pairs

Description: Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example: 

Input: head = [1,2,3,4]

Output: [2,1,4,3]

<img src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg">

### Ideal: Simulated drawing

<img src = "https://code-thinking.cdn.bcebos.com/pics/24.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B91.png">


```python

class Solution(object):
    def swapPairs(self, head):
        dummy_head = ListNode(next = head)
        curr = dummy_head
        while curr.next and curr.next.next:
            temp = curr.next
            temp1 = curr.next.next.next
            curr.next = curr.next.next
            curr.next.next = temp
            curr.next.next.next = temp1
            curr = curr.next.next
        return dummy_head.next


```
__Time complexity__ : O(n)

__Space complexity__ : O(1)


## LC 19. Remove Nth Node From End of List

Description: Given the head of a linked list, remove the nth node from the end of the list and return its head.

<img src = "https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg">

## Ideal: Two pointer

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        head_dummy = ListNode()
        head_dummy.next = head

        slow, fast = head_dummy, head_dummy
        while(n!=0): #fast先往前走n步, 然后和slow一起走
            fast = fast.next
            n -= 1
        while(fast.next!=None):
            slow = slow.next
            fast = fast.next
        #fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next #删除
        return head_dummy.next
```

## Interview question 02/07/2023 (LC 160)

- [ ] Mark. Confused
  
Description: Given the heads of two singly __linked-lists__ headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

<img src = "https://assets.leetcode.com/uploads/2021/03/05/160_statement.png">


<img src = "https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png">

* Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3

* Output: Intersected at '8'

Ideal: 简单来说，就是求两个链表交点节点的指针。

<img src = "https://code-thinking.cdn.bcebos.com/pics/%E9%9D%A2%E8%AF%95%E9%A2%9802.07.%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4_2.png">

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        while cur:         # 求链表A的长度
            cur = cur.next 
            lenA += 1
        cur = headB 
        while cur:         # 求链表B的长度
            cur = cur.next 
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:     # 让curB为最长链表的头，lenB为其长度
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA 
        for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
            curB = curB.next 
        while curA:         #  遍历curA 和 curB，遇到相同则直接返回
            if curA == curB:
                return curA
            else:
                curA = curA.next 
                curB = curB.next
        return None 
```

## LC 142 Linked List Cycle II

- [ ] Mark. Confused

Description: Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example: 

<img src = "https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png">

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

Ideal: 
1. How to identify if there are a circuit in the linked list?
* Two pointers
  
    * fast pointer move 2 steps
    * slow pointer move 1 step
2. Find the entry position
* 从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点， 那么当这两个指针相遇的时候就是 环形入口的节点。

<img src = "https://code-thinking-1253855093.file.myqcloud.com/pics/20220925103433.png">