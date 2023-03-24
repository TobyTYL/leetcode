# Day 28

- [x] LC 93, 78, 90

# LC 93. Restore IP Addresses

Description:

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 
Example 1:

```
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

Ans:

```py
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
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

# LC 78. Subsets

Description:

Given an integer array nums of unique elements, return all possible subsets (the power set).

Example 1:

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

Ans:

```py
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        result = []
    
        def back_tracking(self, nums, start_index):
            size = len(nums)
            # 收集子集，要放在终止添加的上面，否则会漏掉自己
            result.append(ans[:])
            if start_index >= size:
                return
            for i in range(start_index, size):
                ans.append(nums[i])
                back_tracking(self, nums, i+1)
                ans.pop()
        if result:
            result.append("[]")
        back_tracking(self, nums, 0)
        return result
```

# LC 90. Subsets II

Description:

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

Example 1:

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

Ans:
```py
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        result = []
        def back_tracking(self, nums, start_index):
            size = len(nums)
            result.append(ans[:])
            if start_index >= size:
                return
            for i in range(start_index, size):
                # nums[i] == nums[i-1]：剪枝，树层去重
                if i > start_index and nums[i] == nums[i-1]:
                # 当前后元素值相同时，跳入下一个循环，去重
                    continue
                ans.append(nums[i])
                back_tracking(self, nums, i+1)
                ans.pop()
        # 注意要sort
        nums.sort()
        back_tracking(self, nums, 0)
        return result
```