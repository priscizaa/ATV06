#ATIVIDADE 06 - FUNÇÕES

#1
def boas_vindas():
    print('Bem-vindo(a) à disciplina ALLP')
boas_vindas()

#2
def quadrado(numero):
    return numero ** 2
print(f'O quadrado de 5 é: {quadrado(5)}')

#3
def somar(a, b):
    return a + b
print(f'A soma de 10 + 7 é:  {somar(10, 7)}')

#4
def contagem(inicio=1, fim=5):
    print(f'Contagem de {inicio} até {fim}:')
    for i in range(inicio, fim + 1):
        print(i)
contagem()
contagem(3, 8)

#5
def calcular_imc(peso=70, altura=1.75):
    return peso / (altura ** 2)
imc = calcular_imc()
print(f'IMC padrão: {imc: .2f}')

#6
def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
par_ou_impar(7)
par_ou_impar(10)

#7
def saudacao(nome= 'Visitante'):
    print(f'Olá, {nome}! Seja bem-vindo(a)!')
saudacao()
saudacao('Carla')