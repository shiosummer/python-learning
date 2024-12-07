def sanweishu(i,j,k):
    if i<5 and j<5 and k<5:
        if i!=j and i!=k and j!=k:
            print(f'{i}{j}{k}')
        return sanweishu(i,j,k+1)
    elif k==5:
        return sanweishu(i,j+1,1)
    elif j==5:
        return sanweishu(i+1,1,1)
    elif i==5:
        return

if __name__ == '__main__':
    sanweishu(1,1,1)