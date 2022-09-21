from itertools import count
from math import factorial


semana = ["lunes","martes","miercoles"]
print(semana[:0])
user_name = "@saman"
if "@" in user_name:
    print (user_name)
else:
    print ("@ + user_name")    
semana_copy = semana
semana_copy[2] = "juernes"
print(semana_copy)
semana.append("viernes")
print(semana)
semana.insert(3,"sabado")
print(semana)
factorial = 1
n = 5
count = 1
while count <= n:
    factorial *= count
    count += 1
print(factorial)
for a in semana:
    print(a)
for index in range(len(semana)):
    semana[index] = semana[index].title()
    print(semana[index])