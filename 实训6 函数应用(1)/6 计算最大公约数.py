def maxDivider(a,b):
    while b!=0:
        x = a%b
        a = b
        b = x
    return a
a = int(input('请输入第一个数'))
b = int(input('请输入第二个数'))
print(f'您输入的两数的最大公约数为{maxDivider(a,b)}')