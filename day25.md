# Day 25

- [x] LC 216, 17

# LC 216. Combination Sum III

Description: 

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

* Only numbers 1 through 9 are used.
* Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:

```
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
```

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
    # k是个数，n是target sum
    def backtracking(self, k, n, start_num):
        # 剪枝操作
        if self.sum_now > n:  # 假如大于n，后面的就不需要循环了->剪枝
            return
        # 终止条件
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

<img src = "https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png">


Example 1:

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