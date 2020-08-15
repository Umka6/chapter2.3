
try:
    d = {'a':1, 'b':2,'c':3}
    result = d['d']
except KeyError:
    print('Такого ключа не существует')
else:
    print('result is',result)