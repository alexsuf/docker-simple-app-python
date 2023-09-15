import calendar

print ('Добро пожаловать! \n')

year = int(input('Введите год: '))
month = int(input('Номер месяца: '))

print(calendar.month(year, month))

print('See you later!')