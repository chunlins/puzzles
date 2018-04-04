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
