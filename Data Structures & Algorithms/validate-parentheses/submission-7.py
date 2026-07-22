class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        n = len(s) / 2
        for i, val in enumerate(s):
            if (val == '(' or val == '[' or val == '{'):
                x.append(val)
            else:
                if len(x) <= 0:
                    return False
                a = x.pop()
                if a == '(' and val != ')':
                    return False
                if (a == '{' and val != '}'):
                    return False
                if (a == '[' and val != ']'):
                    return False
        if len(x) > 0:
            return False
        return True