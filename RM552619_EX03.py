print('Olá, bem vindo ao app!')

alunos_impar = 0
alunos_par = 0
for impar in range(1, 50, 2):
    print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES')
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(impar)))
    alunos_impar += nota
for par in range(2, 51, 2):
    print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES')
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(par)))
    alunos_par += nota

media_impar = alunos_impar/25
media_par = alunos_par/25

print('Média dos alunos impares: {}'.format(media_impar))
print('Média dos alunos pares: {}'.format(media_par))

if media_par > media_impar:
    print("A metade par da turma obteve a maior média")
elif media_impar > media_par:
    print("A metade impar da turma obteve a maior média")
elif media_impar == media_par:
    print("Ambas as metades obtiveram a mesma média")

input("\nAperte enter se deseja fechar o programa...")
