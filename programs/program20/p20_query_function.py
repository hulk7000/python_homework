from p20_data_dic_capitals import country_capitals
from p20_data_dic_languages import country_languages

def querycap(country):
    return country_capitals.get(country,"未找到该国家的首都")
    # print(country_capitals.get(country))
def querylanguage(country):
    return country_languages.get(country,"未找到该国家的语言")
    # print(country_languages.get(country))

