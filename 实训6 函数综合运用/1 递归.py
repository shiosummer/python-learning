def func(n):
    if n==1:
        return 1
    else:
        return n*func(n-1)
n = int(input('请输入一个整数：'))
print(f'{n}!={func(n)}')