data = 'dishes.txt'
order = {"items": [],"total_price": 0}
# 存储已点菜品的信息，如 {"dish_name": "宫保鸡丁", "quantity": 2}
#计算总价

def load_dishes():
    dishes = []
    with open('dishes.txt', 'r', encoding='utf-8') as f:
        for line in f:
            name,price,stock = line.strip().split(' ')
            dishes.append({"name":name,"price":float(price),"stock":int(stock)})
    return dishes
dishes = load_dishes()
###读取已保存的菜品###

def save_dishes():
    with open('dishes.txt', 'w', encoding='utf-8') as f:
        for dish in dishes:
            f.write(f"{dish['name']} {dish['price']} {dish['stock']}\n")
###用于保存dishes列表中的菜品

def add_dishes(name,price,stock):
    for dish in dishes:
        if dish["name"] == name:
            print('该菜品已存在')
            return
    dishes.append({"name": name, "price": float(price), "stock": int(stock)})
    save_dishes()
    print(f"成功添加菜品：{name} (价格: {price}, 库存: {stock})")
###添加菜品到列表dishes和dishes.txt中###

def edit_price(name, price, stock):
    for dish in dishes:
        if dish["name"] == name:
            dish["price"] = float(price)
            dish["stock"] = int(stock)
            save_dishes()
            print(f"{name} 的价格已更新为{price}，库存已更新为{stock}")
            return
    print(f"未找到名为 {name} 的菜品。")
###修改菜品的价格和库存并保存到列表dishes和dishes.txt中###

def view_menu():
    print_tpye=int(input('\n菜单排序方式：\n1.原始菜单\n2.按价格排序\n3.按菜品排序\n请输入您需要的菜单排序方式：'))
    if print_tpye == 1:
        for dish in dishes:
            print(f'{dish["name"]} 价格-{dish["price"]} 库存-{dish["stock"]}')
    elif print_tpye == 2:
        sorted_dishes = sorted(dishes, key=lambda dish: dish["price"])
        for dish in sorted_dishes:
            print(f'{dish["name"]} 价格-{dish["price"]} 库存-{dish["stock"]}')
    elif print_tpye == 3:
        sorted_dishes = sorted(dishes, key=lambda dish: dish["name"])
        for dish in sorted_dishes:
            print(f'{dish["name"]} 价格-{dish["price"]} 库存-{dish["stock"]}')
###选择菜单排序方式###

def order_menu(name,quantity):
    for dish in dishes:
        if dish['name'] == name:
            if quantity > dish['stock']:
                print('库存不足，点餐失败')
                return
            dish['stock'] -= quantity
            order["items"].append({"name": name, "quantity": quantity, "price": dish["price"]})
            order["total_price"] += quantity * dish["price"]
            save_dishes()
            print(f'点餐成功：{name}×{quantity}')
            return
    print('未找到菜品，请重新点餐')
###定义点餐函数，判断库存是否足够并减去库存，以及计算总价###

def cancel_order(name,cancel_quantity):
    for item in order["items"]:
        if item['name'] == name:
            quantity = item['quantity'] - cancel_quantity
            order["total_price"] -= item['price'] * cancel_quantity
            if quantity > 0:
                item["quantity"] = quantity
                return
            order['items'].remove(item)
    for dish in dishes:
        if dish['name'] == name:
            dish['stock'] += cancel_quantity
            save_dishes()
            print(f'取消点餐成功：{name}×{cancel_quantity}')
            return
    print('订单中未找到该菜品，取消点餐失败')
###确定取消某菜品点餐的数量，并计算剩余还需支付的价格###

def check_order():
    for item in order["items"]:
        print(f'{item['name']} -数量:{item['quantity']} -单价:{item['price']}')
    print(f'菜品总价为:{order["total_price"]}')
###打印订单详情###
def check_pay():
    print('订单详情:')
    if not order["items"]:
        print("您的订单为空，无法结账。")
        return
    check_order()
    input('确认支付？(请按任意键继续)')
    input('付款方式:\n1.微信支付\n2.支付宝支付\n3.银联支付\n4.现金支付\n请选择您的支付方式:')
    input('确认支付？(请按任意键继续)')
    print('支付成功，感谢您的光临')
    print('------------小票------------')
    check_order()
    print('---------------------------')
###选择付款方式确认支付并打印小票###

def load_main_menu():
    import time
    x = 50
    print('-' * 4 + '正在进入Lumine点餐系统' + '-' * 4)
    for i in range(51):
        str1 = '*' * (i//2)
        str2 = '.' * ((x - i)//2)
        str3 = int((i / x) * 100)
        print(f'\r[{str1}{str2}]', end='')
        time.sleep(0.02)
    print('\n' + '-' * 4 + '欢迎使用Lumine点餐系统' + '-' * 4)
###制作一个假进度条载入主菜单###

def exit_system():
    print("\n感谢使用Lumine点餐系统，再见！")
    save_dishes()  # 退出时保存菜品数据
    exit()
###退出点菜系统主菜单###

def usr_password():
    user = input('请输入用户名:')
    for i in range(3):
        if user == 'admin':
            password = input(f'请输入用户密码(剩余次数{3-i})：')
            if password == 'sa123456':
                print(f'管理员登陆成功\n您好,管理员{user}!')
                return 1
    print(f'您好,顾客{user}!')
    return 0
###用户登录(进入管理员界面或顾客界面)###