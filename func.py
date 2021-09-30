# x = 50
# def func():
#     global x
#     print('x равно', x)
#     x = 2
#     print('Заменяем глобальное значение x на', x)
# func()
# print('Значение x составляет', x)




x=6
def fun_out():
    #global x
    x = 2
    print('x равно', x)
    def func_in():
        #nonlocal x
        #global x
        x = 5
    func_in()
    print('Локальное x сменилось на', x)
fun_out()


