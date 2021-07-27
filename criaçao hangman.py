import random


def escolha_palavra():
    lista_palavras = ['macaco', 'gato', 'cachorro', 'papagaio', 'tartaruga', 'coelho']
    palavra = random.choice(lista_palavras)
    return palavra.upper()


def play(palavra):
    palavra_completa = '_' * len(palavra)
    chutado = False
    letras_chutadas = []
    palavras_chutadas = []
    tentativas = 6
    print(f'JOGO DA FORCA! \nDica: animal com {len(palavra)} letras! ')
    print(enforcado(tentativas))
    print(palavra_completa)
    print('\n')

    while not chutado and tentativas > 0:
        chute = input('Advinhe uma letra ou a palavra: ').upper()
        if len(chute) == 1 and chute.isalpha():
            if chute in letras_chutadas:
                print(f'Você ja tentou, {chute}')
            elif chute not in palavra:
                print(f'{chute} Nao!')
                tentativas -= 1
                letras_chutadas.append(chute)
            else:
                print(chute, 'está na palavra! ')
                letras_chutadas.append(chute)
                palavra_lista = list(palavra_completa)
                indice = [i for i, letra in enumerate(palavra) if letra == chute]
                for index in indice:
                    palavra_lista[index] = chute
                    palavra_completa = ''.join(palavra_lista)
                if '_' not in palavra_completa:
                    chutado = True
        elif len(chute) == len(palavra) and chute.isalpha():
            if chute in palavras_chutadas:
                print(f'Você ja tentou a palavra, {chute}')
            elif chute != palavra:
                print(f'Você errou {chute} não é a palavra certa!')
                tentativas -= 1
                palavras_chutadas.append(chute)
            else:
                chutado = True
                palavra_completa = palavra
        else:
            print('Inválido!')
        print(enforcado(tentativas))
        print(palavra_completa)
        print('\n')
    if chutado:
        print('Parabéns você ganhou!!')
    else:
        print(f'Você perdeu! A palavra era {palavra}')


def enforcado(tries):
    fases = [  # cabeça, tronco e braços e pernas: morte.
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
        # cabeça, tronco e braços, perna
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
        # cabeça, tronco e braços
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
        # cabeça, tronco e braço
        """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
        # cabeça e tronco
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # cabeça
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # vazio
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return fases[tries]


def main():
    palavra = escolha_palavra()
    play(palavra)
    while input('Jogar denovo S/N? ').upper() == 'S':
        palavra = escolha_palavra()
        play(palavra)


if __name__ == '__main__':
    main()
