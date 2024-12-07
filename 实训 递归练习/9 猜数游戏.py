import random
num = random.randrange(1, 10)

def panduan(times,guess):
    if times>=1:
        if guess == num:
            return f'恭喜猜数成功,数字为{num}'
        elif guess > num:
            print(f'您猜大了，往小了猜(还剩{times}次机会)')
            return panduan(times - 1,int(input('请输入您要猜的数:')))
        else:
            print(f'您猜小了，往大了猜(还剩{times}次机会)')
            return panduan(times - 1,int(input('请输入您要猜的数:')))
    else:
        if guess != num:
            return f'很遗憾，次数耗尽，猜数失败,随机数为{num}'
        else:
            return f'恭喜猜数成功,数字为{num}'

if __name__=='__main__':
    print('猜数游戏')
    print(panduan(2,int(input('请输入您要猜的数:'))))