def money(n):
    if n==1:
        return 100
    else:
        return 20+money(n-1)
n=5
print(f'第五个人有{money(n)}元')