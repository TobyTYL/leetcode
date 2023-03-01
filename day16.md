# Day 16
- [x] LC 104, 111, 222

# LC 104. Maximum Depth of Binary Tree

## Ideal: 
* 深度用前序遍历, 从上往下
* 高度用后序遍历，用父节点加一求高度，从下往上

Ans:

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 1. 层序遍历
        # results = []
        # if not root:
        #     return 0
        
        # from collections import deque
        # que = deque([root])
        # count = 0
        # while que:
        #     size = len(que)
        #     for i in range(size):
        #         cur = que.popleft()
        #         if cur.left:
        #             que.append(cur.left)
        #         if cur.right:
        #             que.append(cur.right)
        #     count += 1
        # return count

        # 2. 递归
        def getHeight(self, node):
            if node == None:
                return 0
            
            leftDepth = getHeight(self, node.left)
            rightDepth = getHeight(self, node.right)
            height = 1 + max(leftDepth, rightDepth)
            return height
        return getHeight(self, root)
```

# LC 111. Minimum Depth of Binary Tree

Description:

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

<img src = "https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg">

```
Input: root = [3,9,20,null,null,15,7]
Output: 2
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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_depth = 10**9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth) # 获得左子树的最小高度
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth) # 获得右子树的最小高度
        return min_depth + 1
```

# LC 222. Count Complete Tree Nodes

__Description:__

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

<img src = "https://assets.leetcode.com/uploads/2021/01/14/complete.jpg">

```
Input: root = [1,2,3,4,5,6]
Output: 6
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
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root == None: return 0
        # count = 0
        # left_count = self.countNodes(root.left)
        # right_count = self.countNodes(root.right)
        # count = right_count + left_count + 1
        # return count

        # 递归
        def traversal(self, node,count):
            if node == None:
                return 0
            
            leftNum = traversal(self, node.left,count)
            rightNum = traversal(self, node.right,count)
            treeNum = leftNum + rightNum + 1 #中
            return treeNum
        return traversal(self, root, 0)
```