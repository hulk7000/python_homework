def countryinfo():
    from capitals_dic import country_capitals,country_languages
    num =0
    for k,v in country_capitals.items():
        num+=1
        country = k
        capital = v
        language = country_languages.get(k)
        output = '{} country:{:<10}| capital:{:<10}|language:{:<10}'.format(num,country, capital, language)
        print(output)
def querycap(country):
    from capitals_dic import country_capitals
    print(country_capitals.get(country))
def querylanguage(country):
    from capitals_dic import country_languages
    print(country_languages.get(country))
def showallcountry():
    from capitals_dic import country_capitals
    for k,v in country_capitals.items():
        print(k)
def showalllanguage():
    from capitals_dic import country_languages
    for k,v in country_languages.items():
        print(v)

from homework06012025 import countryinfo, querycap, querylanguage, showallcountry, showalllanguage

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
            countryinfo()
        elif choice == "2":
            country = input("请输入国家名：").strip()
            querycap(country)
        elif choice == "3":
            country = input("请输入国家名：").strip()
            querylanguage(country)
        elif choice == "4":
            showallcountry()
        elif choice == "5":
            showalllanguage()
        elif choice == "6":
            print("退出程序，再见！")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()


#5