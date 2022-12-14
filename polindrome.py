import re
def isPalindrome(s: str) -> bool:
    lower_string = s.lower()
    no_number_string = re.sub(r'\d+','',lower_string)
    no_wspace_string = re.sub(r'[^\w]','', no_number_string)
    lenght = len(no_wspace_string)
    for i in range(lenght//2):
        if no_wspace_string[i] != no_wspace_string[-i-1]:
            return False
    return True


print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('race a car'))
print(isPalindrome(' '))
