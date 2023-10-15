from random import randint

itens = ("pedra = 1", "papel = 2", "tesoura = 3")
comp = randint(0,2)
print('''suas opções:
[ 1 ] pedra
[ 2 ] papel 
[ 3 ] tesoura''')
jog = int(input("qual é a sua jogada?: ")) -1

print("-=" * 20)

print(f"computador jogou: {(itens[comp])} !!!")

print("-=" * 20)

print(f"você jogou : {(itens[jog])} !!!")

print("-=" * 20)

if comp == 0:
    if jog == 0:
        print(" empate!")
    elif jog == 1:
        print("parabéns você ganhou!!!")
    elif jog == 2:
        print("sinto muito você perdeu!!")
    else:
        print("JOGADA INVALIDA!")
elif comp == 1:
    if jog == 0:
        print("parabéns você ganhou!!!")
    elif jog == 1:
        print("empate!")
    elif jog == 2:
        print("sinto muito você perdeu!!")
    else:
        print("JOGADA INVALIDA!")
elif comp == 2:
    if jog == 0:
        print("sinto muito você perdeu!!")
    elif jog == 1:
        print("parabéns você ganhou!!!")
    elif jog == 2:
        print("empate!")
    else:
        print("JOGADA INVALIDA!")
else:
    print("jogada extremamente invalida!:(")