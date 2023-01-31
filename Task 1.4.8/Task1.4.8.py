#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

n=int (input(" Insert number"))
m=int (input(" Insert number"))
k=int (input(" Insert number"))

print('yes' if k%n==0 or k%m==0 and k<n*m else 'no')

