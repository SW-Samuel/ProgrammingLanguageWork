import random

def play():
    print_opening_message()
    secret_word = load_secret_word()
    letters_right = letters_right_com_(secret_word)
    
    hanged = False
    got_it_right = False
    erros = 0
    
    print(letters_right)

    while(not hanged and not got_it_right):
        kick = pede_kick()

        if(kick in secret_word):
            marca_kick_correto(kick,letters_right,secret_word)
        else:
             erros += 1
        hanged = erros == 3
        got_it_right = '_' not in letters_right
        print('\n')
        print(letters_right)
        print(f'\nErros : {erros} / 3')

    if(got_it_right):
        Print_message_winner()
    else:
        Print_message_lost(secret_word)
    print('Fim do jogo')

def print_opening_message():
     print('*********************************')
     print('***Bem vindo ao jogo da Forca!***')
     print('*********************************') 

def load_secret_word():
     arquivo = open('words.txt','r')
     words = []

     for line in arquivo:
        line = line.strip()
        words.append(line)
     arquivo.close()

     number = random.randrange(0,len(words))
     secret_word = words[number].upper()
     return secret_word
     
def letters_right_com_(secret_word):
    return ['_' for letra in secret_word]

def pede_kick():
    kick = input("Qual letra? ")
    kick = kick.strip().upper()
    return kick

def marca_kick_correto(kick,letters_right,secret_word):
    position = 0
    for letra in secret_word:
        if(kick.upper() == letra.upper()):
            letters_right[position] = letra
        position = position + 1

def Print_message_winner():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def Print_message_lost(secret_word):
    print('Puxa, você foi enforcado!')
    print('A palavra era {}'.format(secret_word))

play()
