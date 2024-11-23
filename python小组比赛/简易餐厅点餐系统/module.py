import csv

date = 'dishes.txt'
order = {
    "items": [],  # 存储已点菜品的信息，如 {"dish_name": "宫保鸡丁", "quantity": 2}
    "total_price": 0  # 总价
}

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
    dishes.append({"name": name, "price": price, "stock": stock})
    save_dishes()
    print(f"成功添加菜品：{name} (价格: {price}, 库存: {stock})")
###添加菜品到列表dishes和dishes.txt中###

def edit_price(name, price, stock):
    for dish in dishes:
        if dish["name"] == name:
            dish["price"] = price
            dish["stock"] = stock
            save_dishes()
            print(f"{name} 的价格已更新为{price}，库存已更新为{stock}")
            return
    print(f"未找到名为 {name} 的菜品。")
###修改菜品的价格和库存并保存到列表dishes和dishes.txt中###

def view_menu():
    print_tpye=int(input('请选择您需要的菜单排序方式\n1.原始菜单\n2.按价格排序\n3.按菜品排序\n'))
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