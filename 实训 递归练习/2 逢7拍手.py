def seven(i):
    if i<=100:
        if str(i).find('7')>=0:
            print(f'{i}*',end='\n')
        elif i%7==0:
            print(f'{i}*',end='\n')
        else:
            print(f'{i}',end='')
        return seven(i+1)

if __name__ == '__main__':
    seven(1)