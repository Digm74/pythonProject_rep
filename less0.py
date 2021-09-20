num1: str  =  input ( 'Введите первое число:' )
num2  =  input ( 'Введите второе число:' )
Operation  =  input ( 'Вид математической операции:' )
if  Operation  ==  '+' :
    print ( 'результат сложения:' , int ( num1 ) +  int ( num2 ))
elif  Operation  ==  '-' :
    print ( 'результат вычитания:' , int ( num1 ) -  int ( num2 ))
elif  Operation  ==  '*' :
    print ( 'результат умножения:' , int ( число1 ) *  int ( число2 ))
elif  Operation  ==  '/' :
    print ( 'результат деления:' , int ( num1 ) /  int ( num2 ))
elif  Operation  ==  '//' :
    print ( "результат целочисленного деления:" , int ( num1 ) //  int ( num2 ))
elif  Operation  ==  '%' :
    print ( "результат деления с остатком:" , int ( num1 ) %  int ( num2 ))
elif  Operation  ==  '**' :
    print ( "результат возведения в степень:" , int ( num1 ) **  int ( num2 ))