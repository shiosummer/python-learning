for i in range(1,101):
    include=str(i).find('7')
    if i%7==0:
        print(f'{i} *',end='\n')
    elif include>=0:
        print(f'{i} *',end='\n')
    else:
        print(i,end=' ')