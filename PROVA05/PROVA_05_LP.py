

num_alunos = int(input("Digite o número de alunos: "))


soma_medias = 0

for i in range(num_alunos):
 
     nome = input(f"Digite o nome do aluno {i+1}: ")
    

     nota1 = float(input(f"Digite a primeira nota de {nome}: "))
     nota2 = float(input(f"Digite a segunda nota de {nome}: "))
     nota3 = float(input(f"Digite a terceira nota de {nome}: "))
    

     media = (nota1 + nota2 + nota3) / 3

     if media >= 7.0:
         status = "Aprovado"
     else:
         status = "Reprovado"
    
     print(f"\nAluno: {nome}")
     print(f"Notas: {nota1}, {nota2}, {nota3}")
     print(f"Média: {media:.2f}")
     print(f"Status: {status}\n")
    
   
     soma_medias += media


media_geral = soma_medias / num_alunos


print(f"Média geral da turma: {media_geral:.2f}")
