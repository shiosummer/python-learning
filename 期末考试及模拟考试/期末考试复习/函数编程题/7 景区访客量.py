data=[200,388,123,456,987,342,767,234,124,345,123,234]
def star_end_avg(star,end):
    month=1
    Sum=0
    for item in data:
        if star<=month<=end:
            Sum+=item
            month=month+1
        else:
            month=month+1
    avg=Sum/(end-star+1)
    return avg
def fk_avg(*args):
    month=1
    Sum=0
    for item in data:
        for item1 in args:
            if month == item1:
                Sum+=item
        month=month+1
    avg=Sum/len(args)
    return avg

if __name__ == '__main__':
    print(data)
    print(f'平均值为{fk_avg(3,4,5)}')
    print(f'开始结束月份之间的平均值为:{star_end_avg(int(input('请输入开始月份:')),int(input('请输入结束月份:')))}')

