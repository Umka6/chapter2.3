try:
    a = [3,55,446,37,21,4]
    result = a[9]

    print(a.pop(8))

except IndexError:
    print('Такого индекса не существует')
else:
    print(result)

a = ['Kirill','Taalai','Daniyar','Turat','Aito','Alexandr','Adinai','Umut']
