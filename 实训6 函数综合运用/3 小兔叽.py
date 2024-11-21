def rabbit(month):
    if month<=2:
        return 1
    else:
        return rabbit(month-1)+rabbit(month-2)
month=12
print(f'一年后一共有{rabbit(month)}对小兔子')