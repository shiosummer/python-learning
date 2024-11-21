import random
shot=random.randrange(1,7)
input('请按回车击发第一发子弹')
for i in range(1,7):
    if i!=shot:
        print(f'{i}/6 未击发子弹')
        input('请按回车击发第下一发子弹')
    else:
        print(f'{i}/6 击发子弹！你死了！！')
        break