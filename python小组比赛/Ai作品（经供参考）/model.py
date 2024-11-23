# 数据文件路径
DATA_FILE = "dishes.txt"

# 示例订单数据
order = {
    "items": [],  # 已点菜品的信息
    "total_price": 0  # 总价
}


def load_dishes():
    """从文本文件加载菜品数据"""
    dishes = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for line in file:
                # 每行格式为: 菜品名,价格,库存
                name, price, stock = line.strip().split(",")
                dishes.append({"name": name, "price": int(price), "stock": int(stock)})
    except FileNotFoundError:
        pass  # 文件不存在时返回空列表
    return dishes


def save_dishes():
    """将菜品数据保存到文本文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for dish in dishes:
            # 每行格式为: 菜品名,价格,库存
            file.write(f"{dish['name']},{dish['price']},{dish['stock']}\n")


def add_dish(name, price, stock):
    """添加菜品"""
    for dish in dishes:
        if dish["name"] == name:
            print("该菜品已存在。")
            return
    dishes.append({"name": name, "price": price, "stock": stock})
    save_dishes()
    print(f"成功添加菜品：{name} (价格: {price}, 库存: {stock})")


def view_menu():
    """查看菜单"""
    print("当前菜单（按价格排序）：")
    sorted_dishes = sorted(dishes, key=lambda x: x["price"])
    for dish in sorted_dishes:
        print(f"{dish['name']} - 价格: {dish['price']} - 库存: {dish['stock']}")


def place_order(name, quantity):
    """点餐"""
    for dish in dishes:
        if dish["name"] == name:
            if quantity > dish["stock"]:
                print("库存不足，无法完成订单。")
                return
            dish["stock"] -= quantity
            order["items"].append({"dish_name": name, "quantity": quantity, "price": dish["price"]})
            order["total_price"] += dish["price"] * quantity
            save_dishes()  # 更新库存到文件
            print(f"成功点餐：{name} x {quantity}")
            return
    print("未找到该菜品，请重新输入。")


def cancel_order(name):
    """取消订单"""
    for item in order["items"]:
        if item["dish_name"] == name:
            order["items"].remove(item)
            order["total_price"] -= item["price"] * item["quantity"]
            for dish in dishes:
                if dish["name"] == name:
                    dish["stock"] += item["quantity"]
            save_dishes()  # 更新库存到文件
            print(f"成功取消订单：{name}")
            return
    print("没有找到该菜品在订单中。")


def check_out():
    """结账"""
    if not order["items"]:
        print("您的订单为空，无法结账。")
        return
    print("订单详情：")
    for item in order["items"]:
        print(
            f"{item['dish_name']} - 数量: {item['quantity']} - 单价: {item['price']} - 小计: {item['quantity'] * item['price']}")
    print(f"总价：{order['total_price']} 元")
    input("确认支付？ (按任意键继续)")
    print("支付成功，感谢您的光临！")
    order["items"].clear()
    order["total_price"] = 0


def exit_system():
    """退出系统"""
    print("感谢使用餐厅点餐系统，再见！")
    save_dishes()  # 退出时保存菜品数据
    exit()


def main():
    global dishes
    dishes = load_dishes()  # 程序启动时加载菜品数据
    print("欢迎使用餐厅点餐系统！")
    role = input("请输入您的角色（管理员/顾客）：").strip()

    while True:
        if role == "管理员":
            print("\n管理员功能：")
            print("1. 添加菜品")
            print("2. 查看菜单")
            print("3. 退出系统")
            choice = input("请选择功能：")

            if choice == "1":
                name = input("请输入菜品名称：")
                price = int(input("请输入菜品价格："))
                stock = int(input("请输入菜品库存："))
                add_dish(name, price, stock)
            elif choice == "2":
                view_menu()
            elif choice == "3":
                exit_system()
            else:
                print("无效输入，请重新选择。")
        elif role == "顾客":
            print("\n顾客功能：")
            print("1. 查看菜单")
            print("2. 点餐")
            print("3. 取消订单")
            print("4. 结账")
            print("5. 退出系统")
            choice = input("请选择功能：")

            if choice == "1":
                view_menu()
            elif choice == "2":
                name = input("请输入菜品名称：")
                quantity = int(input("请输入点餐数量："))
                place_order(name, quantity)
            elif choice == "3":
                name = input("请输入要取消的菜品名称：")
                cancel_order(name)
            elif choice == "4":
                check_out()
            elif choice == "5":
                exit_system()
            else:
                print("无效输入，请重新选择。")
        else:
            print("无效角色，请重新输入。")
            role = input("请输入您的角色（管理员/顾客）：").strip()


if __name__ == "__main__":
    main()
