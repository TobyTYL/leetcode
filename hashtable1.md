# Day 6

- [x] Task: LC 242, 349, 202, 1
- [x] 当我们遇到了要快速判断一个元素是否出现集合里的时候，就要考虑哈希法了。

## LC 242. Valid Anagram

Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

Ideal: 创建一个数组类型的Hash Table

* record = [0] * 26
* 遍历s，每次一个字母出现就加1
* 同理t，每次一个字母出现就减1
* 遍历record，假设里面26个位置都为零，renturn True

Answer:

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashtable or the length of 26 array
        record = [0] * 26
        for i in s:
            record[ord(i) - ord("a")] += 1
        for j in t:
            record[ord(j) - ord("a")] -= 1
        for g in record:
            if g != 0:
                return False
        return True

```

## LC 349. Intersection of Two Arrays

Description: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example: 
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

Ideal: 

two for loops, but first for loop to record the value. Built a hash table, and iteral the second array to search the intersection
Answer:

```py
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        val_dict = {}
        ans = []
        for num in nums1:
            val_dict[num] = 1

        for num in nums2:
            if num in val_dict.keys() and val_dict[num] == 1:
                ans.append(num)
                val_dict[num] = 0
        
        return ans
     
```

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        # 找到两个集合的交集
        intersection = set1.intersection(set2)
        
        return list(intersection)

```

## LC 202. Happy Number

Description: Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example:

```
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

Ideal:

* 用一个helper fucntion来计算平方值
* 创建一个set
* n = call helper funciton
* 假设n出现在set中，return false
* 不然就往set中添加数值
* 记得用while True来循环

Answer: 

```python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #关键：sum可能会重合，例如一直出现36，3^2 + 6^6 = 45, 4^2 + 5^2 = 36
        def calculate_happy(n):
            sumv = 0
            for i in str(n):
                i = int(i)
                sumv += i**2
            return sumv
        # 空set
        record = set()
        while True:
            n = calculate_happy(n)
            if n == 1:
                return True
            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)
```

```py
class Solution:
    def helper(self, n: int) -> int:
        result = 0
        for i in str(n):
            i = int(i)
            result += i**2
        return result
    def isHappy(self, n: int) -> bool:
    # 用一个helper fucntion来计算平方值
    
    # 创建一个set
        ans = set()
        
        while True:
            sum_v = self.helper(n)
            if sum_v in ans:
                return False
            elif sum_v == 1:
                return True
            else:
                ans.add(sum_v)
                n = sum_v
    # n = call helper funciton
    # 假设n出现在set中，return false
    # 不然就往set中添加数值
    # 记得用while True来循环

```

## LC 1. Two Sum
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
Ideal: 

* 

Ans:
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        records = dict()

        for index, value in enumerate(nums):  
            # 遍历当前元素，并在map中寻找是否有匹配的key
            if target - value in records:   
                return [records[target- value], index]
            # 遍历当前元素，并添加到dict里
            records[value] = index    
        print(records)
        # dont find the pair
        return []
```

