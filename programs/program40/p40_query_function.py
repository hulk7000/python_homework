from p40_data_dic import country_capitals,country_languages
def querycap(country):
    print(country_capitals.get(country,"no country found in our database"))
def querylanguage(country):
    print(country_languages.get(country,"no country found in our database"))