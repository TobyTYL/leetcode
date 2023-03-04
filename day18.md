# Day 18

- [x] LC 513, 112, 106

# LC 513. Find Bottom Left Tree Value


Description:
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:

<img src = "https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg">

```
Input: root = [2,1,3]
Output: 1
```

## Ideal: First to get the max depth, and then take the left ndoe value

Ans:
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        max_depth = -float("INF")
        leftmost_val = 0

        def __traverse(root, cur_depth): 
            nonlocal max_depth, leftmost_val
            # 终止条件
            if not root.left and not root.right: 
                # 更新最深深度
                if cur_depth > max_depth: 
                    max_depth = cur_depth
                    leftmost_val = root.val  
            # 左，假设为空就不进行这个if statement
            if root.left: 
                cur_depth += 1
                __traverse(root.left, cur_depth)
                #回到根节点
                cur_depth -= 1
            # 右
            if root.right: 
                cur_depth += 1
                __traverse(root.right, cur_depth)
                cur_depth -= 1
        __traverse(root, 0)
        return leftmost_val
```

# LC 112. Path Sum

Description: 
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg">

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
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
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        count = targetSum
        def traversal(root, count):
            # 1. 终止条件
            # 合法路径
            if root.left == None and root.right == None and count == 0:
                return True
            # 不合法路径
            if (not root.left) and (not root.right):
                return False  # 遇到叶子节点，计数不为0
            
            # 递归逻辑
            if root.left:
                count -= root.left.val
                # 返回值为True的话，所以左方向有我们想要的路径，所以要继续return true
                if traversal(root.left, count):
                    return True
                count += root.left.val

            if root.right:
                count -= root.right.val
                if traversal(root.right, count):
                    return True
                count += root.right.val
            return False

        if root == None:
            return False
        else:
            return traversal(root, targetSum - root.val)

```

# LC 113. Path Sum II

Description: 

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg">

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
```

Ans:
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traversal(cur_node, remain): 
            if not cur_node.left and not cur_node.right:
                if remain == 0: 
                    result.append(path[:])
                return

            if cur_node.left: 
                path.append(cur_node.left.val)
                traversal(cur_node.left, remain-cur_node.left.val)
                path.pop()

            if cur_node.right: 
                path.append(cur_node.right.val)
                traversal(cur_node.right, remain-cur_node.right.val)
                path.pop()

        result, path = [], []
        if not root: 
            return []
        path.append(root.val)
        traversal(root, targetSum - root.val)
        return result
```

# LC 106. Construct Binary Tree from Inorder and Postorder Traversal

Description:
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/02/19/tree.jpg">

```
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 后序确定顶点（后序的最后一个节点）
        # 中序确定左右节点（顶点分割左右边）
                 # 第一步: 特殊情况讨论: 树为空. 或者说是递归终止条件
        if not postorder:
            return 

        # 第二步: 后序遍历的最后一个就是当前的中间节点
        root_val = postorder[-1]
        root = TreeNode(root_val)
        
        # 第三步: 找切割点.
        root_index = inorder.index(root_val)

        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
        # ⭐️ 重点1: 中序数组大小一定跟后序数组大小是相同的. 
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder): len(postorder) - 1]


        # 第六步: 递归
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        # 第七步: 返回答案
        return root 
```