def jishuhe(sum,num):
    if num > 0 :
        if num%2 != 0:
            sum+=num
            return jishuhe(sum,num-1)
        else:
            return jishuhe(sum,num-1)
    return sum

if __name__ == '__main__':
    num=100
    print(f'{num}内的奇数和为{jishuhe(0,num)}')