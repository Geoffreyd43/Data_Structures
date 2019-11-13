def reverse_polish(postfix_str):

    stack = []

    index = 0

    while index < postfix_str.__len__():
        if postfix_str[index] != '+' and postfix_str[index] != '*':
            stack.append(postfix_str[index])
        else:
            second = stack.pop()
            first = stack.pop()

            temp = '(' + first + ' ' + postfix_str[index] + ' ' + second + ')'
            stack.append(temp)

        index += 1

    return stack.pop()


print(reverse_polish('ab+'))
print(reverse_polish('abc++'))
print(reverse_polish('ab*c+'))
print(reverse_polish('ab+cd+*'))