import random
import os

palavras=[]

def nome_progama():
    print('*************************************')
    print('Bem-Vindo ao jogo da palavra secreta!')
    print('*************************************')

def quantas_palavras():
    quantidade_opcao = int(input('Informe quantas palavras deseja colocar no jogo: '))
    #cria uma lista de nomes fonecidos pelo usuario 
    for i in range(quantidade_opcao):
        segredo=input('informe uma palavra: ')
        palavras.append(segredo)

def parabenisacao(palavra_secreta, tentativa):
    os.system('cls')
    print('Parabens você acertou a palavra secreta!')
    print(f'Parabéns! Você adivinhou a palavra: {palavra_secreta}')
    print(f'Restaram {tentativa} tentativas de 3 para acertar a palavra!')

def acerte_palavra():
    tentativa = 3
    palavra_secreta = random.choice(palavras)
    quantidade_palavra = len(palavra_secreta)
    revelar = '-'*quantidade_palavra
    letra_repetida = []

    print(revelar)
    while tentativa > 0:
        chute = input('Informe uma letra: ').lower()# Convertendo para minúsculas para evitar diferenciação entre maiúsculas e minúsculas
        if chute in letra_repetida:
            print('Você já tentou essa letra. Tente novamente!')
            continue
        letra_repetida.append(chute)
        acertou = False
        for i in range(len(palavra_secreta)):
            if chute == palavra_secreta[i]:
                revelar = revelar[:i] + chute + revelar[i+1:]
                acertou = True
        if acertou:
            print(revelar)
            if revelar == palavra_secreta:
                parabenisacao(palavra_secreta, tentativa)
                break
        else:
            tentativa -=1 
            print('Errou')
        if tentativa == 0:
            print('PEDEU O JOGO!')
            break
        

def main():
     os.system('cls')
     nome_progama()
     quantas_palavras()
     acerte_palavra()


if __name__ == '__main__':
    main()