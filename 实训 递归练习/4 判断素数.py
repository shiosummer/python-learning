def sushu(i,num):
    if i<num and num%i == 0:
        print(f'{num}不是素数')
        return
    elif i !=num and num%i != 0:
        print(f'{num}是素数')
        return
    return sushu(i+1,num)

if __name__ == '__main__':
    sushu(2,int(input('请输入一个整数')))