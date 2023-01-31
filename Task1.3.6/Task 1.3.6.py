#1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет 
# с номером.Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр 
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#  Вам требуется написать программу, которая проверяет счастливость билета.

s= int(input( "Insert ticket number " ) )

a=s//1000    #a=first 3 digit
b=s%1000     #b=last 3 digit

FirstDigitA= a // 100
SecondDigitA=(a//10)%10
ThirdDigitA= a%10
sum1=FirstDigitA+SecondDigitA+ThirdDigitA

FirstDigitb= b // 100
SecondDigitb=(b//10)%10
ThirdDigitb= b%10
sum2=FirstDigitb+SecondDigitb+ThirdDigitb

print('yes' if sum1==sum2 else 'no')



