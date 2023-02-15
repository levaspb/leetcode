'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
'''

def atoi(s: str) -> int:
    final = ''
    minus = False
    maximum = 2**31
    minimum = -maximum
    no_spaces = s.strip()
    for char in no_spaces:
        if char == "-":
            minus = True
            continue
        if char == "+":
            continue
        if char.isnumeric():
            final = final + char
        else:
            break
    result = int(final)
    if minus and -result < minimum:
        return minimum
    elif minus:
        return -result
    if not minus and result > maximum:
        return maximum
    elif not minus:
        return result

print(atoi('   -34234'))
print(atoi('42'))
print(atoi('4193 with words'))
