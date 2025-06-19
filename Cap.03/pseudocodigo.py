#Aula 1 do capitulo 3: logica de programação no data science
#PSEUDOCODIGO É:
'''
 É O PLANEJAMENTO PARA A RESOLUÇÃO DO PROBLEMA QUE PRECISA SER RESOLVIDO
 OU EXPLICAR UM ALGORITIMO ANTES DE ESCREVER OS CODIGOS, COMO SE FOSSE UMA
 RECEITA, O PASSO A PASSO PARA SOLUCIONAR O PROBLEMA REPORTADO.


'''
'''
O PSEUDOCODIGO PARA CALCULAR A AREA DE UM PARALELOGRAMA:
Exiba "Bem vindo ao calculator de Area do paralelograma"
Peça ao usuario para inserir o comprimento da base
armazene o comprimento da base em uma variavel
peça ao usuario para inserir a altura
armazene a altura em uma variavel
base 8 altura calculo do paralelograma
aramzene em uma variavel o resultado

exiba o resultado
'''

'''
print('Seja bem vindo ao calcuulador de area do paralelograma')
cump = float(input('Digite o comprimento da basse: '))
print(cump)
alt = float(input('Digite a altura: '))
print(alt)

base =  cump * alt
print("o valor da base é: ", base, "M")
'''

#Calculadora simples:
"""
exiba a mensagem de bem vindo a calculadora
pergunte qual a operaçao.
armazene em uma variavel
peça ao usuario para digitar um  numero
armazene em uma variavel
peça para digitar outro numero
armazene em uma variavel
faça o calculo de acordo com a operação

"""

print("bem vindo a calculadora")

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
op = int(input("""
    1-Adição (+)
    2-Subtração(-)
    3-Divisão (/)
    4-Multiplicaçao(*)
                                            
-->  """))
match op:
    case 1:
        resp = num1 + num2
        print('A reeposta é' ,resp)
    case 2:
        resp = num1 - num2
        print('A reeposta é' ,resp)
    case 3:
        resp = num1 / num2
        print('A reeposta é' ,resp)   
    case 4:
        resp = num1 * num2
        print('A reeposta é' ,resp)

print("FIM DO PROGRAMA")


print("A resposta é:", {1: lambda a,b: a+b, 
                        2: lambda a,b: a-b, 
                        3: lambda a,b: a/b if b!=0 else 'Erro', 
                        4: lambda a,b: a*b}.get(op := int(input("1:+ 2:- 3:/ 4:* → ")), 
                        lambda a,b: 'Inválido')(float(input("Num1: ")), float(input("Num2: "))))




