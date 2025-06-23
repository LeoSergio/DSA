
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
lista1 = [3,1,99,63,17,12,0]

def bubble_sort(arr):
    print('Algoritimo de ordenação simples')
    n = len(arr)
    #para cada elemento i do array
    for i in range(n):
        #para cada elemento j do array
        for j  in range (0, n - i - 1 ):
            #Se o elemento i for maior que elemento j
            if arr[j] > arr[j + 1]:
                #Troque os elementos i e j
                arr[j], arr [j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort(lista1))
    