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