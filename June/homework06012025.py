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



#10
#10

# def get_capital():
#     while True:
#         country = input("Enter a country name (or type 'exit' to quit): ").strip()
#         if country.lower() == 'exit':
#             print("Goodbye!")
#             break
#         capital = country_capitals.get(country)
#     if capital:
#             print(f"The capital of {country} is {capital}.")
#     else:
#             print(f"Sorry, I don't have the capital for '{country}'.")
#
#
# if __name__ == "__main__":
#     get_capital()
