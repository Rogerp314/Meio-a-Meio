import verificador as v
import palavra as p

#Programa Principal
while True:
    frase = v.verificar('Digite uma frase: ')
    pala = p.meio(frase)
    print(pala)
    sair = str(input('Deseja sair? [S/N]: ')).lower().strip()[0]
    if sair == 's':
        break