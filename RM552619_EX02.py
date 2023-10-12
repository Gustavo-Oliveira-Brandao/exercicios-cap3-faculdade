print('Olá, bem vindo ao app!')

print('Por favor informe quantos votos cada dia da semana obteve')
segunda = int(input('Segunda-feira: '))
terca = int(input('Terça-feira: '))
quarta = int(input('Quarta-feira: '))
quinta = int(input('Quinta-feira: '))
sexta = int(input('Sexta-feira: '))

max_votos = max(segunda, terca, quarta, quinta, sexta)
dia_escolhido = ""
empate = 0

if segunda == max_votos:
    dia_escolhido = "segunda"
    empate += 1
if terca == max_votos:
    dia_escolhido = "terça"
    empate += 1
if quarta == max_votos:
    dia_escolhido = "quarta"
    empate += 1
if quinta == max_votos:
    dia_escolhido = "quinta"
    empate += 1
if sexta == max_votos:
    dia_escolhido = "sexta"
    empate += 1

verificar_empate = "1"
if verificar_empate not in str(empate):
    print("Houve um empate e o dia não pôde ser escolhido, por favor tente novamente.")
else:
    print("O dia mais votado foi {} com {} votos!".format(dia_escolhido, max_votos))

input("\nAperte enter se deseja fechar o programa...")
