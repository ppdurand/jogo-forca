from random import randint
from time import sleep
from os import system

def jogo_principal():
    banco_palavras = ['TECLADO', 'COMPUTADOR', 'FACULDADE', 'VIOLA', 'NAMORAR', 'CIMENTO', 'ENTREVISTA','CERTEZA', 'HOSPITAL',
                      'CALCULADORA', 'FACILIDADE', 'PIANO', 'ARARA', 'FAZER', 'CALVO', 'GUERRA', 'RESTAURANTE', 'DINOSSAURO',
                      'SIMPLES', 'LIVRETO', 'JORNAL', 'BIBLIOTECA', 'QUADRADO', 'HEROI', 'JANELA', 'PORTARIA','SECRETARIA',
                      'DIRETORIA', 'TOALHA', 'BOLSA', 'DIAMANTE', 'BRILHANTE', 'MEDALHA', 'BATATA','ESCOLHA', 'AZULEJO',
                      'CATARRO', 'AMARELO', 'ABACAXI', 'PANTANAL', 'CAATINGA', 'CATAPORA', 'PINTURA', 'CHARUTO', 'CELULAR',
                      'PARTITURA', 'LITERATURA', 'CARTEIRA', 'INDIGENA', 'ESTRANGEIRO', 'DISCO', 'IMAGEM']
    palavra = banco_palavras[randint(0, 51)]
    n_chances = 5
    vitoria = False
    digitadas = []

    while vitoria == False:
        if n_chances <= 0:
            print(f'Você perdeu. \nA palavra era {palavra}')
            break

        letra_usuario = input('\nDigite uma letra: ').strip().upper()
        system("cls")

        if len(letra_usuario) > 1:
            print('Você só pode digitar uma letra por vez')
            continue

        digitadas.append(letra_usuario)  # Lista que vai guardar as letras certas e mandar pra var_aux depois
        print(' ')
        if letra_usuario in palavra:
            print(f'A letra {letra_usuario} existe na palavra')
        elif not letra_usuario in palavra:
            print(f'A letra {letra_usuario} não existe na palavra')
            n_chances -= 1
            digitadas.pop()

        var_aux = ''
        for letra in palavra:  # Aqui vai mandar a letra ou '_' pra var_aux, de acordo com a letras que tiverem nas digitadas
            if letra in digitadas:
                var_aux += letra
            else:
                var_aux += '_'

        if var_aux == palavra: #Confere se a palavra está certa
            for n in range(len(palavra)):
                print(f'{var_aux[n]}', end=' ')
            print('\nVocê acertou a palavra, parabéns')
            vitoria = True
        else: #Caso a palavra ainda nao foi descoberta
            for n in range(len(palavra)): 
                print(f'{var_aux[n]}', end=' ')
            print(f'\nChances de errar: {n_chances}')
        


def loading():
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    system("cls")

#Programa Principal
system("cls")
print('=-'*7)
print('JOGO DA FORCA')
print('=-'*7)

escolha_inicial = input('A - JOGAR\nB - INSTRUÇÕES\nQual letra você deseja acessar? ').strip().upper()
if escolha_inicial == 'A':
    system("cls")
    loading()
    jogo_principal()

elif escolha_inicial == 'B':
    system("cls")
    print()
    print('Digita uma letra e lá vai mostrar se tem ou não\nAgora se prepara pro jogo')
    loading()
    jogo_principal()

else:
    system("cls")
    print()
    print('Letra inválida\nDirecionando ao jogo')
    loading()
    jogo_principal()