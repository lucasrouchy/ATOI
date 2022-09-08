def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if not s: return None
        ans = 0
        [int(s) for s in ls if s.isdigit()]
        for i in range(len(s)):
            if s[i] == ' ':
                s.strip()
            if s[i] == '-':
                ls = -abs(ls)
            elif s[i] == '+':
                ls = ls
        return ls