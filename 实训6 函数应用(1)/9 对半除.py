def result(t):
    h = 40
    s = 80
    for i in range (t-1):
        s = s+h
        h = h/2
    return h,s
t = 10
h,s= result(t)
print(f'第十次落地时经过{s}m,反弹{h}m')