# Day 22

- [x] LC 235, 701, 450

# LC 235. Lowest Common Ancestor of a Binary Search Tree
Description:

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Ideal: 利用BST的特性，左移或右移
Ans:
```py
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Version for binary tree
        # if not root or root == p or root == q:
        #     return root
        
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        
        # if left and right:
        #     return root
        # if left:
        #     return left
        # return right

        # Second version for binary search tree

        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root
```

# LC 701. Insert into a Binary Search Tree

Description:

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:

<img src = "https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg">

```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
```

## Ideal: When the root is None, we can insert the node.

Ans:

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # preorder
        if root == None:
            node = TreeNode(val)
            return node
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root
        
```

# LC 450. Delete Node in a BST

Description: 

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:

<img src = "https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg">

```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```

<img src = "https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg">


## Ideal:

* 重点考虑要删除的节点有左孩子，又有右孩子的情况
* 具体做法，找到该节点(root)的右孩子中最小的节点(p) -- 右孩子中最左的孩子节点
* 将root的左孩子放到p节点的左边

Ans:

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            # 当前节点的右子树为空，返回当前的左子树
            if not root.right:
                return root.left
            node = root.right
            # 左右子树都不为空，找到右孩子的最左节点 记为p
            # 找到比目前根节点大最小的数字（p)
            while node.left:
                node = node.left
            # 将当前节点的左子树挂在p的左孩子上
            node.left = root.left
            # 当前节点的右子树替换掉当前节点，完成当前节点的删除
            root = root.right
        return root
```