def find_index(obj, index):
    print(obj[index])
if __name__ == '__main__':
    # find_index([1,2,2,3,3,43],10)
    #IndexError: list index out of range

    # find_index('hulk','hulk')
    #TypeError: string indices must be integers, not 'str'

    # find_index(10,'qytang')
    # TypeError: 'int' object is not subscriptable

try:
    find_index('djakdfk','dajfda')
except IndexError:
    print('Hulk : Index error')
except TypeError as e:
    print(e)
    print('Hulk : Type error')
    if ' object is not subscriptable' in str(e):
        print("Hulk : object is not int")
    elif 'string indices must be integers' in str(e):
        print("Hulk : index must be integers")
    else:
        print("Hulk : other error")
else:
    print('')
finally:print('everything is fine')