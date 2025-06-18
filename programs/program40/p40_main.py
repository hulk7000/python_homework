from p40_show_function import showcountryinfo as sci, showallcountry as sac, showalllanguages as sal
from p40_query_function import querycap as qc, querylanguage as ql

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
            sci()
        elif choice == "2":
            country = input("请输入国家名：").strip()
            qc(country)
        elif choice == "3":
            country = input("请输入国家名：").strip()
            ql(country)
        elif choice == "4":
            sac()
        elif choice == "5":
            sal()
        elif choice == "6":
            print("退出程序，再见！")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()