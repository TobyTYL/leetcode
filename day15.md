# Day 15

- [x] LC 102, 107 199, 637, 429, 515, 116, 117, 104, 111, 226, 101

# LC 102. Binary Tree Level Order Traversal

Description: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

<img src = "https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg">

Example:
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```
## Ideal: Level order traversal by using deque

Ans:
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        if not root:
            return results
        
        from collections import deque
        que = deque()
        # initialize it with the root node 
        que.append(root)

        # 因为是2d array，所以这是计算一共有多少层
        # 只要这个queue里面有东西就一直运行
        while que:
            # how many elements in this queue currently
            qLen = len(que)
            # empty list for the how many nodes in this layer
            level = []

            for i in range(qLen):
                # cur 只会是同一层的节点，每次遍历可能都会更新cur
                cur = que.popleft()
                level.append(cur.val)
                # 把下一层的子节点加到queue中
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            # for loop结束，这一层的遍历就结束
            results.append(level)

        return results


```

# LC 107. Binary Tree Level Order Traversal II
 
 Description: Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg">

```
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
```

### Ideal: return the reversal order with the LC 102 (result[::-1])


# LC 199. Binary Tree Right Side View

Description:
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

<img src = "https://assets.leetcode.com/uploads/2021/02/14/tree.jpg">

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        from collections import deque
        if not root:
            return []
        
        # deque相比list的好处是，list的pop(0)是O(n)复杂度，deque的popleft()是O(1)复杂度

        quene = deque([root])
        out_list = []

        while quene:
            # 每次都取最后一个node就可以了
            node = quene[-1]
            out_list.append(node.val)

            # 执行这个遍历的目的是获取下一层所有的node
            for _ in range(len(quene)):
                # 弹出当前node后，要把下一层它的子孩子加入到队列中
                node = quene.popleft()
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
        
        return out_list
```

# LC 429. N-ary Tree Level Order Traversal

 Description: 
 
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

<img src = "https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png">

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
```

Ans:

```py
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        from collections import deque
        if not root:
            return []

        quene = deque([root])
        out_list = []

        while quene:
            level = []
            # 执行这个遍历的目的是获取下一层所有的node
            for _ in range(len(quene)):
                # 弹出当前node后，要把下一层它的子孩子加入到队列中
                node = quene.popleft()
                level.append(node.val)
                if node.children:
                    quene.extend(node.children)

            out_list.append(level)
        return out_list
```

# LC 116. Populating Next Right Pointers in Each Node

Description: You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example:
<img src = "https://assets.leetcode.com/uploads/2019/02/14/116_sample.png">

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

## Ideal: 在单层遍历的时候记录一下本层的头部节点，然后在遍历的时候让前一个节点指向本节点就可以了

Ans:

```py
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        results = []
        if not root:
            return None
        
        from collections import deque
        que = deque([root])
        
        while que:
            size = len(que)
            
            for i in range(size):
                cur = que.popleft()

                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                if i == size - 1:
                    break
                # always connect to the next node
                cur.next = que[0]
        return root

```

# LC 104. Maximum Depth of Binary Tree

Description: 

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

<img src = "https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg">

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        results = []
        if not root:
            return 0
        
        from collections import deque
        que = deque([root])
        count = 0
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            count += 1
        return count
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

        return self.getHeight(root)
    def getHeight(self, node):
        if node == None: return 0
        result = 0
        len_left = self.getHeight(node.left)
        len_right = self.getHeight(node.right)
        if (node.left == None and node.right != None):
            return 1 + len_right
        if (node.left != None and node.right == None):
            return 1 + len_left
        result = 1 + min(len_left, len_right)
        return result

```

# LC 226. Invert Binary Tree

Description:
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
<img src = "https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg">

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
```

2. Level order traversal
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        from collections import deque
        if not root:
            return root
        que = deque([root])
        while que:
            for i in range(len(que)):
                cur = que.popleft()
                # 左右互换
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root
```