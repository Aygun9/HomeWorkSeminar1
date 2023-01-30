#1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод

a = int(input( "Insert 3digit number " ) )

FirstDigit= a // 100
SecondDigit=(a//10)%10
ThirdDigit= a%10
result=FirstDigit+SecondDigit+ThirdDigit


print(f'The sum of digits of the number {a} will be {result}')