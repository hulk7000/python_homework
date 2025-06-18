from p16_show_function import showcountryinfo, showallcountry, showalllanguages
from p16_query_function import querycap, querylanguage

def main():
    while True:
        print("\n📋 请选择功能：")
        print("1. 显示所有国家信息")
        print("2. 查询某国家首都")
        print("3. 查询某国家语言")
        print("4. 显示所有国家")
        print("5. 显示所有语言")
        print("6. 退出")

        choice = input("请输入选项编号（1-6）：").strip()

        if choice == "1":
            showcountryinfo()
        elif choice == "2":
            country = input("请输入国家名：").strip()
            querycap(country)
        elif choice == "3":
            country = input("请输入国家名：").strip()
            querylanguage(country)
        elif choice == "4":
            showallcountry()
        elif choice == "5":
            showalllanguages()
        elif choice == "6":
            print("退出程序，再见！")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()