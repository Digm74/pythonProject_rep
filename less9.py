while True:
    a = input()
    if a == 'exit':
        break           # ПРИ ВЫПОЛНЕНИИ ДАННОГО ОПЕРАТОРА ПРОИСХОДИТ ВЫХОД ИЗ ЦИКЛА
    if len(a)<6:
        continue        # ПРИ ВЫПОЛНЕНИИ ДАННОГО ОПЕРАТОРА ПРОИСХОДИТ ПЕРЕХОД В НАЧАЛО ЦИКЛА
    print(a, len(a))
