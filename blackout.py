"""
    Author: Ari Sanders
    Assignment: Blackout Math
    Date: 9/30/14
"""

import operator

def compute(s):
    """
        Computes the value of a string including operators
        s = string to compute
    """
    if not s[0].isdigit() or not s[-1].isdigit():
        #If the equation begins or ends with an operator, consider it invalid
        return None
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    #Using a dictionary of operators allows me to convert from a string
    num = [""]#List of number strings
    ops = []#List of operator strings
    atEnd = False#Whether or not we've done the whole string
    n = 0#Which number string/operator we're up to
    while atEnd == False:
        for i in s:
            if i.isdigit():
                num[n] += i
            else:
                ops.append(i)
                s = s[len(num[n]) + 1:]
                n += 1
                num.append("")
                break
        else:
            atEnd = True
    n = int(num[0])
    for i in range(0, len(ops)):
        n = operators[ops[i]](n, int(num[i + 1]))
    return n

def evaluate(s):
    """
        Evaluates whether an equation string is true or false
        s = string to evaluate
    """
    s = s.split("=")
    return compute(s[0]) == compute(s[1])

def solve(s):
    """
        Solves a blackout challenge via brute-forcing it
        s = string to solve
    """
    for i in range(0, len(s) - 1):
        if s[i] == "=" or s[i + 1] == "=":
            #If the current or previous charater is =, skip
            continue
        for j in range(i + 1, len(s) - 1):
            if (s[j] == "=" or s[j + 1] == "="
                #If the current or previous character is =, skip
                or ((s[i - 1] == "+" or s[i - 1] == "-" or s[i - 1] == "*" or s[i - 1] == "/")
                    and (s[j + 1] == "+" or s[j + 1] == "-" or s[j + 1] == "*" or s[j + 1] == "/"))
                #If blacking out consecutive characters results in two consecutive operators, skip
                or ((s[i - 1] == "+" or s[i - 1] == "-" or s[i - 1] == "*" or s[i - 1] == "/")
                    and (s[i + 1] == "+" or s[i + 1] == "-" or s[i + 1] == "*" or s[i + 1] == "/"))
                #If blacking out the first character results in two consecutive operators, skip
                or ((s[j - 1] == "+" or s[j - 1] == "-" or s[j - 1] == "*" or s[j - 1] == "/")
                    and (s[j + 1] == "+" or s[j + 1] == "-" or s[j + 1] == "*" or s[j + 1] == "/"))
                #If blacking out the second character results in two consecutive operators, skip
                ):
                continue
            ans = evaluate(s[:i] + s[i + 1:j] + s[j + 1:])
            if ans == True:
                return s[:i] + s[i + 1:j] + s[j + 1:]

def main():
    """
        Tests the previous functions
    """
    print("22-11*4 =",compute("22-11*4")," (expect 44)")
    print("+11*4 =",compute("+11*4")," (expect None)")
    print("22-11*4 ?= 7*5+9",evaluate("22-11*4=7*5+9")," (expect True)")
    print("solving 288/24*6=18*13*8 :", solve("288/24*6=18*13*8"))
    print("solving 168/24+8=11*3-16 :", solve("168/24+8=11*3-16"))

main()
