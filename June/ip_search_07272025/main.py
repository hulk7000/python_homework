from function import *
def main():
    while True:
        print("\n📋 enter a number：")
        print("1. show all information")
        print("2. search from vlan")
        print("3. check status down from global")
        print("4. search from ip")
        print("5. check status up from vlan")
        print("6. check status from ip")
        print("7. exit")
        choice = input("请输入选项编号（1-6）：").strip()

        if choice == "1":
            showallinfo()
        elif choice == "2":
            vlan = input("search from vlan：").strip()
            showvlan(vlan)
        elif choice == "3":
            checkstatusdown()
        elif choice == "4":
            checkip()
        elif choice == "5":
            showalllanguage()
        elif choice == "6":

        elif choice == "7":
            print("exit")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()
