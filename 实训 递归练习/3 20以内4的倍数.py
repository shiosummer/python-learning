def beishu(i):
    if i<=20:
        if i%4==0:
            print(i)
            return beishu(i+1)
        else:
            return beishu(i+1)
if __name__ == '__main__':
    beishu(1)