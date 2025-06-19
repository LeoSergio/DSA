#lab1 Primeiros passos na linnguagem python parte 1
numeros = list(range(1,101))

for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)




#lab1 Primeiros passos na linnguagem python parte 2
pares_div4 = [number for number in numeros if number %2 == 0 and number%4 == 0] #list

print(pares_div4)

#list comprehension(é uma forma de reduzir o codigo e simpficar 
#o codigo e pode até deixar o codigo mais rapido em tempo de execução)

