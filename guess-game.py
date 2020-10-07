from random import randint

computador = randint(0, 10)
print('I am your computer... Think of a number between 0 and 10')
print('')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('What is your hunch? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('More... try it one more time')
        else:
            print('Less... try it one more time')
print('You got it with {} attempts!! CONGRATULATIONS'.format(palpites))
