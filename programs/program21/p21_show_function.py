def showcountryinfo():
    from p21_data_dic import country_capitals , country_languages
    num = 0
    for k,v in country_capitals.items():
        num += 1
        country = k
        capital = v
        languages = country_languages.get(country)
        output = '{} country : {:<12} | capital : {:<12} | {} languages : {:<12}'.format(num, country, country, capital, languages)
        print(output)

def showallcountry():
    from p21_data_dic import country_capitals
    for k,v in country_capitals.items():
        print(k)
def showalllanguages():
    from p21_data_dic import country_languages
    for k,v in country_languages.items():
        print(v)