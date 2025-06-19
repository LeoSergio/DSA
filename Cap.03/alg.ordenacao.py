
#algoritmo Bubble sort
'''
é um algoritmo de ordenação simples que funciona comparando
cada elemento com o proximo elemento, e trocando de lugar 
se estiverem em ordem incorreta. ou seja ordenar em ordem crescente ou decrescente

declarar uma variavel array com os numeros aleatorios
exibir o array
ordene em crescente e decrescente
1 a 100 e 100 a 1
'''
print('Algoritimo de ordenação simples')
number = [3,1,99,63,17,12,0]

for i in range(len(number)):
    for j  in range(len(number) -1 ):
        if number[j] > number[j + 1]:
            number[j], number [j + 1] = number[j + 1], number[j]
print("lista ordenada")
print(number)

    