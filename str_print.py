name='Igor'
lname='Devochko'
age=47
print('''Программа показывает возможности "Pythona"''')
#-----------------------------------------------------------------------
print('Вариант 1:')
print('''print('Ученик {0} {1} --- {2} лет.'.format(name,lname,age))
print('Почему {0} {1} изучает Python в {2} лет?'.format(name,lname,age))''')
print('РЕЗУЛЬТАТ -->')
print('*'*70)
print('Ученик {0} {1} --- {2} лет.'.format(name,lname,age))
print('Почему {0} {1} изучает Python в {2} лет?'.format(name,lname,age))
print('*'*70)
#-----------------------------------------------------------------------
print('Вариант 2:')
print('Тот же самый вывод без использования метода format(): ', )
print('''print('Ученик', name, '', lname, ' ---- ', age,  'лет.')
print('Почему' , name, '', lname, 'изучает Python в', age, 'лет?')''')
print('РЕЗУЛЬТАТ -->')
print('*'*70)
print('Ученик', name, '', lname, ' ---- ', age,  'лет.')
print('Почему' , name, '', lname, 'изучает Python в', age, 'лет?')
#-----------------------------------------------------------------------
print('Вариант 3:')
print('Без использования цифр в фигурных скобках')
print('''print('Ученик {} {} --- {} лет.'.format(name,lname,age))
print('Почему {} {} изучает Python в {} лет?'.format(name,lname,age))''')
print('РЕЗУЛЬТАТ -->')
print('*'*70)
print('Ученик {} {} --- {} лет.'.format(name,lname,age))
print('Почему {} {} изучает Python в {} лет?'.format(name,lname,age))
print('*'*70)
print('Метод format() может использоваться и для более детальных обозначений'
      '1. отображает десятичное число (.) с точностью в 3 знака для плавающих: '
      '''print('{0:.3}'.format(1/3))''')
print('{0:.3}'.format(1/3))
print('''Или print('{0:.4}'.format(10/1.91))''')
print('{0:.4}'.format(10/1.91))
print('2. заполняет подчёркиваниями (_) с центровкой текста (^) по ширине 11: '
      '''{0:_^11}'.format('hello')''')
print('{0:_^11}'.format('hello'))
print('3. по ключевым словам: ')
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))
