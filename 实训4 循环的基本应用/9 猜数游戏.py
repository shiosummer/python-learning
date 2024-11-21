import random
num = random.randrange(1,10)
print('猜数游戏')
for i in range(3):
    guess = int(input(f'请输入您猜测的数字(还剩{3-i}次机会)\n'))
    if guess<num:
        print('很遗憾 您猜小了')
    elif guess>num:
        print('很遗憾 您猜大了')
    else:
        print('恭喜 猜数正确')