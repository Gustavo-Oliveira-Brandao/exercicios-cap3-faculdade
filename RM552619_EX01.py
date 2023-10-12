print('Olá, bem vindo ao app!')

faturamento = float(input('Por favor informe qual o seu faturamento anual: '))

level = int(input('Por favor nos informe qual o seu nível de assinatura:\n'
                  '1 - Basic;\n'
                  '2 - Silver;\n'
                  '3 - Gold;\n'
                  '4 - Platinum.\n'))
bonus = 0

if level == 1:
    bonus = faturamento * 0.3
elif level == 2:
    bonus = faturamento * 0.2
elif level == 3:
    bonus = faturamento * 0.1
elif level == 4:
    bonus = faturamento * 0.05

print('Você deve pagar {}'.format(bonus))

input("\nAperte enter se deseja fechar o programa...")
