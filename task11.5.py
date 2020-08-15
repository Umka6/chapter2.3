
try:
    a = [1,4,6,5,7]
    result = a[8]
except IndexError:
    print('Нет в списке')
else:
    print('result is',result)