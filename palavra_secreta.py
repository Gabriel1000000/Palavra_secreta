import random
import os
from unidecode import unidecode

def nome_progama():
    os.system('cls')
    print('*************************************')
    print('Bem-Vindo ao jogo da palavra secreta!')
    print('*************************************')

def quantas_palavras():
    quantidade_opcao = int(input('Informe quantas palavras deseja colocar no jogo: '))
    #cria uma lista de nomes fonecidos pelo usuario 
    for i in range(quantidade_opcao):
        segredo=input('informe uma palavra: ').lower()
        segredo = unidecode(segredo)
        palavras.append(segredo)

def parabenisacao(palavra_secreta, tentativa):
    os.system('cls')
    if tentativa < 2:
        print('Parabens você acertou a palavra secreta!')
        print(f'A palavra secreta era: {palavra_secreta}')
        print(f'Restando {tentativa} tentativa de 3 para acertar a palavra!')    
    else:
        print('Parabens você acertou a palavra secreta!')
        print(f'A palavra secreta era: {palavra_secreta}')
        print(f'Restando {tentativa} tentativas de 3 para acertar a palavra!')

def errou(tentativa):
    print('_______________________________________________________________________')
    if tentativa < 2:
        print('Essa letra não está na palavra secreta.')
        print(f'Você tem {tentativa} tentativa de 3 para você acertar a palavra!')    
    else:
        print('Essa letra não está na palavra secreta.')
        print(f'Você tem {tentativa} tentativas de 3 para acertar a palavra!')
    print('_______________________________________________________________________')


def acerte_palavra():
    tentativa = 3
    palavra_secreta = random.choice(palavras)
    quantidade_palavra = len(palavra_secreta)
    revelar = '-'*quantidade_palavra
    letra_repetida = []
    os.system('cls')
    print('Informe uma letra para revelar a plavra secreta!')
    print(revelar)
    while tentativa > 0:
        chute = input('Informe uma letra: ').lower()# Convertendo para minúsculas para evitar diferenciação entre maiúsculas e minúsculas
        chute = unidecode(chute)
        if chute in letra_repetida:
            tentativa-=1
            print('_____________________________________________________')
            print('Você já tentou essa letra. Tente novamente!')
            print(f'Você tem apenas, {tentativa} tentativas. Boa sorte!')
            print('_____________________________________________________')
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
            errou(tentativa)
    if tentativa == 0:
        print('PEDEU O JOGO!')
        print(f'A palavra secreta era essa: {palavra_secreta}')
                

def main():
     os.system('cls')
     nome_progama()
     quantas_palavras()
     acerte_palavra()


if __name__ == '__main__': 
    palavras=[]
    main()