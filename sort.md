# Sort

## Easy
- [x] LC 148, 56, 27

__LC 148. Sort List__

__Description:__ 

Given the head of a linked list, return the list after sorting it in ascending order.

Example:

<img src= "https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg">


```
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

# Given the head of a linked list, return the list after sorting it in ascending order.

```py
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Base Case: If the length of the linked list is less than or equal to 1, then the list is already sorted
        if not head or not head.next:
            return head

        # Split the linked list into two halves using "slow and fast pointer" technique to find the midpoint of the linked list
        # To find the mid point, and then seprate the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # The midpoint of the linked list is slow.next
        mid = slow.next
        # Set slow.next to None to separate the left and right halves of the linked list
        slow.next = None



        # Recursively sort the left and right halves of the linked list
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves of the linked list
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        # Append the remaining nodes of the left or right half to the end of the sorted list
        curr.next = left or right

        return dummy.next

```