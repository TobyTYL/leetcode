# Day 12
- [x] LC 77, 216, 17, 39

# LC 77. Combinations

Description:

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
```

## Ideal: 
* 组合是无序的，例如1，2和2，1是一样的，元素不能被重复使用


Ans:
```py
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        path = []
        result = []
        def back_tracking(n, k, startindex):
            if len(path) == k:
                result.append(path[:])
                return
            # 单层递归逻辑
            for x in range(startindex, n+1):
                path.append(x)
                back_tracking(n, k, x+1) # 递归
                path.pop() # 回溯
        back_tracking(n, k, 1)
        return result
```

# LC 216. Combination Sum III
Description:

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example:
```
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
```

## Ideal:


Ans:
```py
class Solution:
    def __init__(self):
        self.res = []
        self.sum_now = 0
        self.path = []

    def combinationSum3(self, k, n):
        self.backtracking(k, n, 1)
        return self.res

    def backtracking(self, k, n, start_num):
        if self.sum_now > n:  # 假如大于n，后面的就不需要循环了->剪枝
            return
        if len(self.path) == k:  # len(path)==k时不管sum是否等于n都会返回
            if self.sum_now == n:
                self.res.append(self.path[:])
            return
        for i in range(start_num, 10 - (k - len(self.path)) + 1):
            self.path.append(i)
            self.sum_now += i
            self.backtracking(k, n, i + 1)
            self.path.pop()
            self.sum_now -= i
```

# LC 17. Letter Combinations of a Phone Number


Description:

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

Ans:
```py
class Solution(object):
    def __init__(self):
        self.result = []
        self.ans = ''
        self.dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        # index 是digits的下标
        def back_tracking(self, digits, index):
            if index == len(digits):
                self.result.append(self.ans)
                return
            # 某一个按键对应的字母集
            letters = self.dic[digits[index]]
            for i in letters:
                self.ans += i
                back_tracking(self, digits, index+1)
                # 回溯
                self.ans = self.ans[:-1]
        back_tracking(self, digits, 0)
        return self.result

```

# LC 39. Combination Sum

Description:

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

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

## Ideal:

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


## Ideal: 
* 去重 要排序
* 定义一个数组：used[0, 0, 0]，用过了就加1

Example:

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

# LC 131. Palindrome Partitioning
Description: 
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example:
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

## Ideal: 
* 用切割线分开
* 判断是否为palindrom
* 切割线到s的结尾为止


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

# LC 93. Restore IP Addresses

Description:

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.


Ans:
```py
        global results, path
        results = []
        path = []
        self.backtracking(s,0)
        return results

    def backtracking(self,s,index):
        global results,path
        if index == len(s) and len(path)==4:
            results.append('.'.join(path)) # 在连接时需要中间间隔符号的话就在''中间写上对应的间隔符
            return
        for i in range(index,len(s)):
            if len(path)>3: break          # 剪枝
            temp = s[index:i+1]
            if (int(temp)<256 and int(temp)>0 and temp[0]!='0') or (temp=='0'):
                path.append(temp)
                self.backtracking(s,i+1)
                path.pop() 
```