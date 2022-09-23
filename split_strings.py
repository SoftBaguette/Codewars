'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
'''

def solution(s):

    output = []

    if len(s) % 2 != 0:
        s += "_"

    while len(s) != 0:
        output.append(s[:2:])
        s = s[2:]

    return output