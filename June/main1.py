from function1 import *
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
        choice = input("input from（1-6）：").strip()

        if choice == "1":
            showallinfo()
        elif choice == "2":
            showvlan()
        elif choice == "3":
            checkstatusdown()
        elif choice == "4":
            checkip()
        elif choice == "5":
            checkvlanup()
        elif choice == "6":
            checkstatus()
        elif choice == "7":
            print("exit")
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()