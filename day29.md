# Day 29

- [x] LC 491, 46, 47

# LC 491. Increasing Subsequences

Description:

Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in any order.

Example 1:

```
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
```

Ans:
```py
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        ans = []
        def back_tracking(nums, start_index):
            # at least two elements
            if len(ans) > 1:
                result.append(ans[:])
            # 终止条件
            if start_index == len(nums):
                return
            # 要分卡写，因为并不是终止条件
            # if start_index == len(nums) and len(ans) > 1:
            #     result.append(ans[:])
            #     return
            # 去枝，不要出现重复的分支，例如【4，6，7，7】中的7，将第一个7放入set，后面再出现7就不会重复了 
            usage_list = set()
            for i in range(start_index, len(nums)):
                # 递增的，所以判断是否大于ans中最后一个元素
                if ans and nums[i] < ans[-1] or nums[i] in usage_list: 
                    continue
                usage_list.add(nums[i])
                ans.append(nums[i])
                back_tracking(nums, i+1)
                ans.pop()

        back_tracking(nums, 0)
        return result
```

# LC 46. Permutations

Description:

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

Ideal:

<img src = "https://code-thinking-1253855093.file.myqcloud.com/pics/20211027181706.png">


Ans:
```py   
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def permute(self, nums):
        '''
        因为本题排列是有序的，这意味着同一层的元素可以重复使用，但同一树枝上不能重复使用(usage_list)
        所以处理排列问题每层都需要从头搜索，故不再使用start_index
        '''
        usage_list = [False] * len(nums)
        self.backtracking(nums, usage_list)
        return self.paths

    def backtracking(self, nums, usage_list):
        # Base Case本题求叶子节点
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(0, len(nums)):  # 从头开始搜索
            # 若遇到self.path里已收录的元素，跳过
            if usage_list[i] == True:
                continue
            usage_list[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, usage_list)     # 纵向传递使用信息，去重
            self.path.pop()
            usage_list[i] = False
```

# LC 47. Permutations II

Description:

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

```
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]
```

Ans:
```py
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
         # res用来存放结果
        if not nums: return []
        res = []
        used = [0] * len(nums)
        def backtracking(nums, used, path):
            # 终止条件
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtracking(nums, used, path)
                    path.pop()
                    used[i] = 0
        # 记得给nums排序
        backtracking(sorted(nums),used,[])
        return res
```