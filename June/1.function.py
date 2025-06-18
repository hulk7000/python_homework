def showcountryinfo():
    from dict import country_capitals,country_languages
    num =0
    for k,v in country_capitals.items():
        num+=1
        country = k
        capital = v
        language = country_languages.get(k)
        output = '{} country:{:<10}| capital:{:<10}|language:{:<10}'.format(num,country, capital, language)
        print(output)

def showallcountry():
    from dict import country_capitals
    for k,v in country_capitals.items():
        print(k)
def showalllanguage():
    from dict import country_languages
    for k,v in country_languages.items():
        print(v)
def querycap(country):
    from dict import country_capitals
    print(country_capitals.get(country))
def querylanguage(country):
    from dict import country_languages
    print(country_languages.get(country))

