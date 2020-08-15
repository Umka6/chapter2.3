try:
    a = int(input('Enter the number:'))
    b = int(input('Enter the number:'))
    result = a//b
except ValueError:
    print('Введите числа')
except ZeroDivisionError:
    print('Не делится на ноль')
else:
    print('result is', result)