# Given a string with parenthesis, check if they are balanced.
#  ((a+b)*c) is valid

def validParenthesis(exp):
    stack = []
    opening = {'(': ')', '{': '}', '[': ']'}
    
    for token in exp:
        if token in opening:
            stack.append(token)
        elif token in opening.values():
            if not stack or opening[stack.pop()] != token:
                return False
    return len(stack) == 0

print(validParenthesis("{(a+b)*c}"))      # ✅ True
print(validParenthesis("{(a+b]*c}"))      # ❌ False
print(validParenthesis("((a+b)*c"))       # ❌ False
print(validParenthesis("((a+b)*c)"))      # ✅ True
