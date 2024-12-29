#Arquivo para a função de dividir as strings

def meio(frase):
    if len(frase) % 2 == 0:
        indicemeio = len(frase) // 2
        palavra_meio = frase[indicemeio]
        return palavra_meio
    
    
if __name__ == '__main__':
    frase = str('Meio maior dois quatro')
    frase.split()
    print(frase)
    print(meio(frase))