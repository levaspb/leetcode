def check(strs):
    list_len = len(strs)
    prefix = ''
    for i in range(len(min(strs, key=len))):
        result = True
        for j in range(list_len - 1):
            if strs[j][i] != strs[j+1][i]:
                result = False
                break
        if not result: return prefix
        prefix = prefix + strs[0][i:i+1]
    return prefix

strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(check(strs))
