try:
    a = int(input('Enter the number:'))
    b = int(input('Enter the number:'))
    result = a/b
except ValueError:
    print('Введите числа')
else:
    print('result is,', result)