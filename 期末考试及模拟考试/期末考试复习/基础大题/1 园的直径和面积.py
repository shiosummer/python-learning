def round(r,s,d):
    pi=3.14
    s=s=pi*r**2
    d=2*r
    return s,d

if __name__ == '__main__':
    s,d=round(int(input('请输入半径r:')),0,0)
    print(f'圆的面积为{s},直径为{d}')