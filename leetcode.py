"""
Solutions for problem on leetcode.com

Author: Liu Chunlin (chll) | <chunlins@outlook.com>
Created: 2018-01-17, modified at 2018-04-03
License: MIT LICENSE

FORMATER:
    No. $problem_number | $problem_title | $difficulty
    $description
    $solution_one
    $code_one
    ...
    $testcase

CONTENTS:
    * Problems
    * Collections
    * Solutions
"""
""" 
Problems
    NO. 001 | Two Sum | Easy
    No. 020 | Valid Parenthese | Easy
"""
"""
** TOP INTERVIEW QUESTIONS **
https://leetcode.com/explore/interview/card/top-interview-questions-easy/
"""


"""
No. 11 | Container With Most Water | Media

Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
# MySolution, iterate over start and end pointer
def maxArea(self, height):
    count, area = len(height), []
    for start in range(0, count):
        for end in range(start, count):
            hightof = min(height[start], height[end])
            lengthof = end - start
            area.append(hightof * lengthof)
    
    return max(area)

# MySolution, iterate over axis length
def maxArea(self, height):
    area = []
    for axis in range(1, len(height)):
        water = [min(height[i], height[i - axis]) 
                 for i in range(axis, len(height))]
        area.append(max(water) * axis)
        
    return max(area)


"""
No. 020 | Valid Parenthese | Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.

Input:
  '(', '{}', '{}', '{()]}, '{()}()]]'
"""

def isValid(self, s):
    valid = True
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    if len(s) % 2 == 1:
        valid = False

    for ch in s:
        if ch in brackets.keys():
            stack.append(ch)
        else:
            if len(stack) == 0:
                valid = False
                continue
            check = stack.pop()
            if check != brackets.get(ch):
                valid = False

    return valid


"""
No. 412 | Fizz Buzz | Easy

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
    n = 6,
    Return: ["1", "2", "Fizz", "4", "Buzz", "Fizz"]
"""

def fizzBuzz(n):
    """ n: int / return: List[str] """
    if n <= 0:
        return []
    
    result = [str(number) for number in range(n + 1)]
    for index in range(0, n + 1, 3):
        result[index] = 'Fizz'
    for index in range(0, n + 1, 5):
        result[index] = 'Buzz'
    for index in range(0, n + 1, 15):
        result[index] = 'FizzBuzz'
    
    return result[1:]
