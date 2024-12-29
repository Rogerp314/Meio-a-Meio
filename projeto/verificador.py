#Arquivo de tratamento de erros

def verificar(msg):
    while True:
        frase = str(input(msg)).split()
        #Verificando se a variável está vazia
        if frase == '':
            print('\033[31m[ERROR] Digite algo para o programa continuar.\033[m')
        else:
            return frase
            
            
if __name__ == '__main__':
    print(verificar('Digite uma frase: '))
    