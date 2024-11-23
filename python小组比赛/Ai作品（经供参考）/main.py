# main.py
from model import load_dishes, save_dishes, add_dish, view_menu, place_order, cancel_order, check_out


def main():
    dishes = load_dishes()  # 加载菜品数据
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
                add_dish(dishes, name, price, stock)
            elif choice == "2":
                view_menu(dishes)
            elif choice == "3":
                print("感谢使用餐厅点餐系统，再见！")
                save_dishes(dishes)
                exit()
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
                view_menu(dishes)
            elif choice == "2":
                name = input("请输入菜品名称：")
                quantity = int(input("请输入点餐数量："))
                place_order(dishes, name, quantity)
            elif choice == "3":
                name = input("请输入要取消的菜品名称：")
                cancel_order(dishes, name)
            elif choice == "4":
                check_out()
            elif choice == "5":
                print("感谢使用餐厅点餐系统，再见！")
                save_dishes(dishes)
                exit()
            else:
                print("无效输入，请重新选择。")
        else:
            print("无效角色，请重新输入。")
            role = input("请输入您的角色（管理员/顾客）：").strip()


if __name__ == "__main__":
    main()
