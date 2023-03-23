# Day 27

- [x] LC 39, 40, 131

# LC 39. Combination Sum

Description: 
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the  frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example:
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```


Ans:

```py
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        result = []
        def back_tracking(self, candidates, target, sum_v, start_index):
            if sum_v == target:
                # 因为是shallow copy，所以不能直接传入self.path
                result.append(path[:])
                return
                
            # 因为本题没有组合数量限制，所以只要元素总和大于target就算结束
            if sum_v > target:
                return

            # 单层递归逻辑 
            for i in range(start_index, len(candidates)):
                sum_v += candidates[i]
                path.append(candidates[i])
                # 注意递归逻辑，i递归之后还是加i
                back_tracking(self, candidates, target, sum_v, i)
                # 回溯
                sum_v -= candidates[i]
                path.pop()
        back_tracking(self, candidates, target, 0, 0)
        return result
```

# LC 40. Combination Sum II

Description: 

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

Ans:

```py
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def combinationSum2(self, candidates, target):
        '''
        类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        '''
        self.paths.clear()
        self.path.clear()
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates, target, sum_, start_index):
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:])
            return
        
        # 单层递归逻辑
        for i in range(start_index, len(candidates)):
            # 剪枝，同39.组合总和
            if sum_ + candidates[i] > target:
                return
            
            # 跳过同一树层使用过的元素
            if i > start_index and candidates[i] == candidates[i-1]:
                continue
            
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i+1)
            self.path.pop()             # 回溯，为了下一轮for loop
            sum_ -= candidates[i]       # 回溯，为了下一轮for loop

# second
class Solution(object):
    def __init__(self):
        self.result = []
        self.path = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        def back_tracking(candidates, start_index, target, sum_v):
            if sum_v > target:
                return
            if sum_v == target:
                self.result.append(self.path[:])
                return
            for i in range(start_index, len(candidates)):
                # 跳过同一树层使用过的元素
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                if sum_v + candidates[i] > target:
                    return
                sum_v += candidates[i]
                self.path.append(candidates[i])
                back_tracking(candidates, i+1, target, sum_v)
                sum_v -= candidates[i]
                self.path.pop()
            


        back_tracking(candidates, 0, target, 0)
        return self.result
```

# LC 131. Palindrome Partitioning

Description:

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.


Example 1:

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

Ans:

```py
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        path = []
        result = []
        # 因为同一个集合里切割，所以用start_index
        def back_tracking(self, s, start_index):
            if start_index == len(s):
                result.append(path[:])
                return
            # 单层递归
            for i in range(start_index, len(s)):
                # 判断是否palindrom
                temp = s[start_index:i+1]
                if temp == temp[::-1]:
                    path.append(temp)
                    back_tracking(self, s, i+1)   # 递归纵向遍历：从下一处进行切割，判断其余是否仍为回文串
                    path.pop()
                else:
                    continue    
        back_tracking(self, s, 0)
        return result
```

