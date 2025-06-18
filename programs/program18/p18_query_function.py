def querycap(country):
    from p18_data_dic import country_capitals
    print(country_capitals.get(country))
def querylanguages(country):
    from p18_data_dic import country_languages
    print(country_languages.get(country))