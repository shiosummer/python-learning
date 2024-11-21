def shape(x):
    for i in range(1,x+1):
        space = x-i
        string1 = 2*i-1
        print(' '*space+'*'*string1)
h = int(input('请输入金字塔的高'))
shape(h)