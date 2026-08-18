#Crie um programa em Python que: Peça ao usuário duas notas para dois alunos (total de 4 notas). Calcule a média de cada aluno. Exiba para cada aluno a mensagem correspondente: "Aprovado" se a média for maior ou igual a 7
#; "Recuperação" se a média for maior ou igual a 5 e menor que 7; "Reprovado" se a média for menor que 5.

nota1Aluno1 = float(input('Aluno 1: Digite a primeira nota: '))
nota2Aluno1 = float(input('Aluno 1: Digite a segunda nota: '))

nota1Aluno2 = float(input('Aluno 2: Digite a primeira nota: '))
nota2Aluno2 = float(input('Aluno 2: Digite a segunda nota: '))


mediaAluno1 = (nota1Aluno1 + nota2Aluno1) / 2
mediaAluno2 = (nota2Aluno1 + nota2Aluno2) / 2

if mediaAluno1 >= 7:
    print("Aprovado")
elif mediaAluno1 >= 5:
    print("Recuperação")
else:
    print("Reprovado")

if mediaAluno2 >= 7:
    print("Aprovado")
elif mediaAluno2 >= 5:
    print("Recuperação")
else:
    print("Reprovado")