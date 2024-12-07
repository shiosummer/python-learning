i=1
j=1
while 1<=i<10:
    while 1<=j<i+1:
        print(f'{j}×{i}={i*j}',end='\t')
        j=j+1
    print()
    i=i+1
    j=1