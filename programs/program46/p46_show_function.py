from p46_data_dic import country_capitals,country_languages
def showcountryinfo():
    num = 0
    for k,v in country_capitals.items():
        num += 1
        country = k
        capital = v
        languages = country_languages.get(country)
        output = '{} country : {:<12} | capital : {:<12} | languages : {:<12}'.format(num,country, capital, languages)
        print(output)
def showallcountry():
    for k,v in country_capitals.items():
        print(k)
def showalllanguages():
    for k,v in country_languages.items():
        print(v)