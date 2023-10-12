print('Olá, bem vindo ao app!')

minuto = int(input('Por favor insira o minuto atual da sua máquina para que seja possivel revelar a senha: '))

resultado = 1
count = 1
while count <= minuto:
    resultado *= count
    count += 1

print("A senha é LIBERDADE{}".format(resultado))

input("\nAperte enter se deseja fechar o programa...")
