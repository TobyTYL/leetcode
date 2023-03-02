# Day 17

- [x] LC 110, 257, 404

# LC 110. Balanced Binary Tree
Description:
Given a binary tree, determine if it is 

Example 1:

<img src = "https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg">

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

## Ideal: Postorder (left, right, mid)
* 求高度：后序：通过左右孩子的情况返回给父节点，父节点再根据左右孩子的高度加1
* 求深度：前序：一直向下遍历


Ans:
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.getHeight(root) != -1:
            return True
        else: 
            return False
    def getHeight(self, root):
        # 终止条件，最底下的高度是0
        if root == None: 
            return 0
        len_left = self.getHeight(root.left)
        # -1代表已经有不满足平衡二叉树的条件了
        if len_left == -1: 
            return -1
        len_right = self.getHeight(root.right)
        if len_right == -1: 
            return -1
        result = 0
        if abs(len_right - len_left) > 1:
            result = -1
        else:
            result = 1 + max(len_left, len_right)
        return result
```

# LC 257. Binary Tree Paths

Description: 

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.


Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg">

```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

Ans:
jiji
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = ''
        result = []
        if not root: return result
        self.traversal(root, path, result)
        return result


    def traversal(self, cur, path, result):
        path += str(cur.val)
        # 若当前节点为leave，直接输出
        if not cur.left and not cur.right:
            result.append(path)

        if cur.left:
            # + '->' 是隐藏回溯
            self.traversal(cur.left, path + '->', result)
        
        if cur.right:
            self.traversal(cur.right, path + '->', result)

```

# LC: 404. Sum of Left Leaves

Description:
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 
Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg">

```
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
```

## Ideal: preorder


Ans:
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        left_sum = self.sumOfLeftLeaves(root.left)
        if root.left != None and root.left.left == None and root.left.right == None:
            left_sum = root.left.val
        right_sum = self.sumOfLeftLeaves(root.right)
        ans = left_sum + right_sum
        return ans
```

