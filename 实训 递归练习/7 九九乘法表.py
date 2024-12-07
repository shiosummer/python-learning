def jjcfb(i,j):
    if i<j and i<10 and j<10:
        print(f'{i}×{j}={i * j}', end='\t')
        return jjcfb(i+1,j)
    elif i==j:
        print(f'{i}×{j}={i * j}', end='\n')
        return jjcfb(1,j+1)

if __name__ == '__main__':
    jjcfb(1,1)