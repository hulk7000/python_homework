from p20_data_dic_capitals import country_capitals
from p20_data_dic_languages import country_languages

def showcountryinfo():
    num = 0
    output = []
    for k,v in country_capitals.items():
        num += 1
        country = k
        capital = v
        language = country_languages.get(k)
        line = '{} country : {:<12} | capital : {:<12} | language : {:<12}'.format(num, country,capital,language)
        output.append(line)
    return '\n'.join(output)
def showallcountry():
    output = []
    for k,v in country_capitals.items():
        line = k
        output.append(line)
    return '\n'.join(output)
def showalllanguages():
    output = []
    for k,v in country_languages.items():
        line = v
        output.append(line)
    return '\n'.join(output)


