# 二叉树纲领篇
## Note：
二叉树题目的递归解法 __思路__
1. 遍历一遍二叉树得出答案
    * 二叉树中用遍历思路解题时函数签名一般是 void traverse(...)，没有返回值，靠更新外部变量来计算结果
2. 通过分解问题计算出答案
    * 分解问题思路解题时函数名根据该函数具体功能而定，而且一般会有返回值，返回值是子问题的计算结果

* 二叉树的遍历框架
    ```py
    # 二叉树遍历框架
    def traverse(root: TreeNode) -> None:
        if not root:
            return
        # 前序位置
        # 对root的操作
        traverse(root.left)
        # 中序位置
        # 对root的操作
        traverse(root.right)
        # 后序位置
        # 对root的操作
    ```
* 二叉树的递归框架
    ```py
    # 二叉树的递归框架
    def recursion(root: TreeNode) -> ReturnType:
        if not root:
            return None
        # 前序位置
        # 对root的操作
        left = recursion(root.left)
        right = recursion(root.right)
        # 后序位置
        # 对root的操作
        return ReturnType
    ```

* 数据结构的基本存储方式就是链式和顺序两种，基本操作就是增删查改，遍历方式无非迭代和递归。
* 学完基本算法之后，建议从「二叉树」系列问题开始刷，结合框架思维，把树结构理解到位，然后再去看回溯、动规、分治等算法专题，对思路的理解就会更加深刻。

