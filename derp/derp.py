"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates preorder expressions 
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Sean Strout (sps@cs.rit.edu)

Author: Ari Sanders
"""

from derp_node import *
import operator
    
##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """parse: list(String) -> Node
    From an infix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    
    if tokens == []:
        raise Exception("Empty list")
    token = tokens[0]
    tokens = tokens[1:]
    if token.isdigit():
        return LiteralNode(int(token))
    elif token.isidentifier():
        return VariableNode(token)
    else:
        left = parse(tokens)
        right = parse(tokens)
    if token == "*":
        return MultiplyNode(left, right)
    if token == "//":
        return DivideNode(left, right)
    if token == "+":
        return AddNode(left, right)
    if token == "-":
        return SubtractNode(left, right)
    raise Exception("Invalid expression")

##############################################################################
# infix
##############################################################################
        
def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    
    list = []
    infixRec(node, list)

operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
types = {"AddNode": "+", "SubtractNode": "-", "MultiplyNode": "*", "DivideNode": "/"}

def infixRec(node, list):
    if not node:
        return list
    varType = type(node)
    print(str(varType)[18:][:-2])
    if isinstance(node, LiteralNode):
        list.append(node.val)
    elif isinstance(node, VariableNode):
        list.append(node.name)
    else:
        list.insert(0, "(")
        infixRec(node.left, list)
        list.append(str(types[str(varType)[18:][:-2]]))
        infixRec(node.right, list)
        list.append(")")
    print(list)
 
##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    
    list = infix(node)
    n = 0
    for i in range(0, len(list)):
        if item == "(" or item == ")":
            continue
        if item.isdigit():
            number = item
        elif item.isidentifier():
            number = symTbl[item]
        operators[ops[i + 1]](n, int(num[i + 1]))
        i += 2
    
##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v1.0 :)")
    
    inFile = input("Herp, enter symbol table file: ")
    
    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    dict = {}
    for line in open(inFile):
        if not line.strip():
            break
        line = line.strip().split()
        dict[line[0]] = line[1]
    
    print("Herp, enter prefix expressions, e.g.: + 10 20 (RETURN to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break
            
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        list = []
        for item in prefixExp.split():
            list.append(item)
        
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
        root = parse(list)
            
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        inFix = infix(root)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression:", inFix)
        
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.
        result = evaluate(infix, dict)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation:", result)
         
    print("Goodbye Herp :(")
    
if __name__ == "__main__":
    main()
