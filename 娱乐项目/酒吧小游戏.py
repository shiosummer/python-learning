import random
#判断人数是否足够开始游戏 并生成游玩人数下的所有骰子的结果
player = int(input('请输入玩耍的人数：'))
if player <= 1 :
    print('人数不足，无法开始游戏')

else:#为每个玩家生成5个骰子并保存到表格
    result = ''
    for i in range(player):
        rolls = []
        for j in range(5):
            rolls.append(random.randrange(1, 7))
            rolls.sort()
        result += f'{rolls}\n'

    #开始猜骰子
    guess_number = 1
    guess_much = 0
    keep_on = 'Y'
    while keep_on :
        if keep_on.upper() != 'Y' and keep_on.upper() != 'N':
            keep_on = input('重新输入是否继续猜数Y/N\n')

        elif keep_on.upper() == 'Y':
            #完成骰子大小的猜测
            guess_number1 = int(input('你要猜的骰子大小为(1~6)\n(需大于等于之前猜的)\n'))
            while guess_number1 < guess_number:
                guess_number1 = int(input('请重新输入你要猜的骰子大小为(1~6)\n(需大于等于之前猜的)\n'))

            #判定是否需要重置猜测数量并为目前猜测骰子大小重新赋值
            if guess_number1 > guess_number:
                guess_much = 0
            else:
                guess_much = guess_much
            guess_number = guess_number1

            #完成骰子大小的个数的猜测
            guess_much1 = int(input(f'你猜测{guess_number1}有多少个：\n(需大于之前猜的)\n'))
            while guess_much1 <= guess_much:
                guess_much1 = int(input(f'请重新输入你猜测的{guess_number}的个数\n(需大于之前猜的)\n'))
            guess_much = guess_much1

        #是否结束猜数循环 以及判断胜负 决定接受惩罚的玩家
            keep_on = input('是否继续猜数Y/N\n')
        else:
            many = result.count(str(guess_number))
            if many >= guess_much:
                print('你输了，请接受惩罚')
                print(result)
                break
            else:
                print('你赢了，前一位玩家接受惩罚')
                print(result)
                break