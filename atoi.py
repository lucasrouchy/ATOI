import sys


def myAtoi(s: str) -> int:
    MaxNum = 2 ** 31 -1
    MinNum = -2 ** 31

    s = s.strip()
    flag = 1
    i = 0
    num = 0
    if not s: return num
    if s[0] == '-':
        flag = -1
        i += 1
    elif s[0] == '+':
        i += 1
    while i < len(s) and s[i].isdigit():
        cur = ord(s[i]) - ord('0')
        if num > MaxNum // 10 or (num == MaxNum // 10 and cur > 7):
            return MaxNum if flag == 1 else MinNum
        num = num * 10 + cur
        i += 1

    num = flag * num
    return num 

myAtoi("42")
myAtoi("       -442")
myAtoi("4193 with words")





# i, base, flag = 0, 0, 1
#         if not (set(s) & set('0123456789')):
#             return 0
#         # int(s) for s in str.split() if s.isdigit()
#         while s[i] == ' ':
#             i += 1
        
#         if s[i] == '-' or s[i] == '+':
#             flag = -1 * (s[i] == '-')
#             i+= 1
        
#         while i < len(s) and '0' <= s[i] <= '9':
#             if (base > (sys.maxsize // 10) or (base == (sys.maxsize // 10) and (ord(s[i]) - ord('0')) > 7)) :
            
#                 if flag == 1:
#                     return sys.maxsize
#                 else: 
#                     return -(sys.maxsize) - 1

#                 base = 10 * base
#                 base += (ord(s[i]) - ord('0'))
#                 i += 1
#         return base * flag

# s = "42"
# myAtoi(s)