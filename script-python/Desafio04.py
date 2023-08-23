tempo= float(input('Digite o tempo gasto (HH:MM): '))
velocidade = int(input('Digite a velocidade média: '))
distancia = tempo * velocidade
litros_usados = distancia / 12
print ('A distância é: ',distancia, 'Gasolina usada: ',litros_usados)
