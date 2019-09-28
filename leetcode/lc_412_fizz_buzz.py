"""
No. 412 | Fizz Buzz | Easy

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”. For numbers which are multiples of
both three and five output “FizzBuzz”.

Example:
    n = 6,
    Return: ["1", "2", "Fizz", "4", "Buzz", "Fizz"]
"""


def fizz_buzz(n):
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
