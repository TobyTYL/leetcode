# Day 11

- [x] Task: LC 20, 1047, 150

# LC 20. Valid Parentheses

### Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example:

```
Input: s = "()"
Output: true
```

## Ideal: Using Stack, or dictionary


Ans:
```py
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack = []
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            # not stack 判断是否还有元素在stack中，stack[-1] stack中最后一个元素
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        return True if not stack else False
```

# LC 1047. Remove All Adjacent Duplicates In String

### Description:

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.


## Ideal: Stack, 注意要判断stack是否为空，最终将其join在一起



__Example 1:__

```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
```


Ans:
```python
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            # 注意要判断stack
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
```

