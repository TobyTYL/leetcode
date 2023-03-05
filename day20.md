# Day 20

- [x] LC 654, 617, 700, 98

# LC 654. Maximum Binary Tree

__Description:__

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

 

__Example 1:__

<img src = "https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg">


```
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.
```
## Ideal:

* Follow the rules, and implement it

Ans:
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # if not nums:
        #     return None
        # maxvalue = max(nums)
        # index = nums.index(maxvalue)
        
        # root = TreeNode(maxvalue)

        # left = nums[:index]
        # right = nums[index + 1:]

        # root.left = self.constructMaximumBinaryTree(left)
        # root.right = self.constructMaximumBinaryTree(right)
        # return root

        if not nums:
            return None
        maxvalue = max(nums)
        max_index = nums.index(maxvalue)
        left = nums[:max_index]
        right = nums[max_index+1:]
        root = TreeNode(maxvalue)

        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root
```

# LC 617. Merge Two Binary Trees

__Description:__

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/02/05/merge.jpg">

```
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
```

Ans:
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        # 假如节点为None，检查另一个节点是否存在
        # 存在的话录入为新节点
        # 不存在为None


        if not root1:
            return root2
        if not root2:
            return root1
       
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

```

# LC 700. Search in a Binary Search Tree

__Description:__

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg">

```
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
```

### Ideal: This is a binary search tree, so left always be smaller than the parents node and right node's value

Ans:
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # 1. 终止条件
        # 只需要返回节点就可以，因为下面连着的是一颗树或None
        if (root == None) or (root.val == val):
            return root

        # 2. traversal
        # 比根节点小的话，向左遍历
        # 比根节点大，向右遍历，这是因为bst的特性
        node = TreeNode(None)
        if val < root.val:
            node = self.searchBST(root.left, val)
        if val > root.val:
            node = self.searchBST(root.right, val)
        return node
```

# LC 98. Validate Binary Search Tree

__Description:__

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys greater than the node's key.
* Both the left and right subtrees must also be binary search trees.


Example 1:

<img src = "https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg">

```
Input: root = [2,1,3]
Output: true
```

Ans:
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # inorder
   # 规律: BST的中序遍历节点数值是从小到大. 
   # cur_max 记录了当前节点前一个节点的数值

   # array way
        stack = []
        cur = root
        pre = None
        while cur or stack:
            if cur: # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else: # 逐一处理节点
                cur = stack.pop()
                if pre and cur.val <= pre.val: # 比较当前节点和前节点的值的大小
                    return False
                pre = cur 
                cur = cur.right
        return True


# Second
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        def traversal(root):
            if not root:
                return
            
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)
            
            return result
        traversal(root)
        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return False
        print(result)
        return True

```