#输入需要原本支付的金额
Cost = float(input('请输入您的消费金额（元）：'))

#分支 计算 输出
while Cost:
    if Cost>=10000:
        Pay = Cost-0.25*Cost
        print(f'您需要支付的金额为{Pay}元')
        break
    elif 8000<=Cost<10000:
        Pay = Cost-0.2*Cost
        print(f'您需要支付的金额为{Pay}元')
        break
    elif 5000<=Cost<8000:
        Pay = Cost-0.15*Cost
        print(f'您需要支付的金额为{Pay}元')
        break
    elif 2000<=Cost<5000:
        Pay = Cost-0.1*Cost
        print(f'您需要支付的金额为{Pay}元')
        break
    elif 0<=Cost<2000:
        Pay = Cost
        print(f'您需要支付的金额为{Pay}元')
        break
    else:
        Cost = float(input('请重新输入正确的消费金额（元）：'))