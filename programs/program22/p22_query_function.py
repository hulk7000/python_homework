def querycap(country):
    from p22_data_dic import country_capitals
    print(country_capitals.get(country))
def querylanguage(country):
    from p22_data_dic import country_languages
    print(country_languages.get(country))