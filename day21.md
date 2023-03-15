# Day 21

- [x] LC 530, 501, 236

# LC 530. Minimum Absolute Difference in BST

Description: Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.


Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg">

```
Input: root = [4,2,6,1,3]
Output: 1
```

## Ideal: 二叉搜索树采用中序遍历，其实就是一个有序数组。

Ans:

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        r = float("inf")
        def traversal(root):
            if not root:
                return None
            if root.left:
                traversal(root.left)
            result.append(root.val)
            if root.right:
                traversal(root.right)
            return result
        
        traversal(root)
        for i in range(len(result)-1): 
            r = min(abs(result[i]-result[i+1]),r)
        return r
```

# LC 501. Find Mode in Binary Search Tree

Description:
* Given the root of a binary search tree (BST) with duplicates,return all the mode(s) (i.e., the most frequently occurred element) in it.
* If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
* The left subtree of a node contains only nodes with keys less than or equal to the node's key.
* The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
* Both the left and right subtrees must also be binary search trees.
 

Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg">

```
Input: root = [1,null,2,2]
Output: [2]
```

## Ideal: 用map统计频率

Ans: 
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        resultList = []
        dictionary = {}
        
        def dfs(root):
            if root == None:
                return None
            if (root.val in dictionary):
                dictionary[root.val] += 1
            else:
                dictionary[root.val] = 1
            dfs(root.left)
            dfs(root.right)
        
        
        dfs(root)
        maximum = 0
        for k, v in dictionary.items():
            if (dictionary[k] > maximum):
                maximum = v
        
        for k, v in dictionary.items():
            if v == maximum:
                resultList.append(k)
        return resultList
            
```

# LC 236. Lowest Common Ancestor of a Binary Tree

Description: 

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 
Example 1:

<img src = "https://assets.leetcode.com/uploads/2018/12/14/binarytree.png">


```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

Ans:
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        if left:
            return left
        return right

```

