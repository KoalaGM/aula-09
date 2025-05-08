# lst_valores = []


# for i in range(5):
#     num = int(input('Informe o numero: '))
#     lst_valores.append(num)

# print(f'Os números são {lst_valores}')


# While
lst_nomes = []
resposta = ''

while resposta != 'n':
    nome = input('Informe o nome: ')
    lst_nomes.append(nome)

    resposta = input('Quer continuar? [s/n]: ')[0].lower()

print(f'Os nomes foram {lst_nomes}')


lst_nomes2 = []
while True:
    nome = input('Informe o nome: ')
    lst_nomes2.append(nome)

    resposta = input('Quer continuar? [s/n] ').lower()
    if resposta == 'n':
        break