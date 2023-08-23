quant_sexo_masculino = int (input ('Digite a quantidade de alunos do sexo masculino: '))
quant_sexo_feminino = int (input ('Digite a quantidade de alunos do sexo feminino: '))

total_alunos = quant_sexo_masculino + quant_sexo_feminino
porcentmasc = quant_sexo_masculino / total_alunos * 100
porcentfemi = quant_sexo_feminino / total_alunos * 100

print ('O total de alunos é ', total_alunos)
print ('A porcentagem de alunos é ', porcentmasc,'%')
print ('A porcentagem de alunas é ', porcentfemi,'%')
