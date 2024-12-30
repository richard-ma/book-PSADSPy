from src.basic import Stack
import string


def infixToPostfix(infixexpr):
    prec = dict()
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack()
    postfixList = list()
    
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in string.ascii_uppercase or token in "0123456789": # 如果节点是字母，直接添加到后序列表中
            postfixList.append(token)
        elif token == '(': # 如果节点是左括号，添加到opStack
            opStack.push(token)
        elif token == ')': # 节点是右括号
            topToken = opStack.pop() # opStack出栈
            while topToken != "(": # 节点不是匹配的左括号则一直出栈
                postfixList.append(topToken) # 将所有出栈字符添加到后序列表中
                topToken = opStack.pop()
        else: # 节点是运算符
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]): # opStack不为空且opStack中的栈顶符号优先级高于当前符号
                    postfixList.append(opStack.pop()) # 将opStack栈顶符号添加到后续队列
            opStack.push(token) # 将当前符号添加到opStack
    
    while not opStack.isEmpty(): # 将opStack所有栈中的符号添加到后续列表
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

def postfixEval(postfixExpr):
    operandStack = Stack()
    
    tokenList = postfixExpr.split()
    
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()

def doMath(token, op1, op2):
    if token == '+':
        return op1 + op2
    elif token == '-':
        return op1 - op2
    elif token == '*':
        return op1 * op2
    else:
        return op1 / op2