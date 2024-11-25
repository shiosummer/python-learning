library_list={'item':[],'total_price':0}
def start():
    num,name,price,stock=input('请输入图书的书号,书名,单价,数量(以逗号分隔):').split(',')
    library_list['item'].append({'num': num, 'name': name, 'price': float(price), 'stock': int(stock)})
    tf = input('是否继续输入图书(Y/N):').upper()
    if tf != 'Y' and tf != 'N':
        tf = input('是否继续输入图书(Y/N):').upper()
    elif tf == 'Y':
        start()
    else:
        for item in library_list['item']:
            print(f'书号:{item['num']}-书名:{item['name']}-单价:{item['price']},数量:{item['stock']}')
            library_list['total_price'] += item['price'] * item['stock']
        print(f'总价:{library_list['total_price']}')

if __name__ == '__main__':
    start()
