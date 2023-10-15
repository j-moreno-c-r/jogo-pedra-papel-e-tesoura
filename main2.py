from random import randint

# O que sabemos sobre o problema?
# 

itens = ("pedra = 1", "papel = 2", "tesoura = 3")
PEDRA = 0
PAPEL = 1
TESOURA = 2

GANHOU = "parabéns você ganhou!!!"
PERDEU = "sinto muito você perdeu!!"
EMPATE = " empate!"
INVALIDO = "JOGADA INVALIDA!"

OPCOES = '''suas opções:
[ 1 ] pedra
[ 2 ] papel 
[ 3 ] tesoura'''
PERGUNTA = "qual é a sua jogada?: "
RESULTADO = "\n".join([
    "-=" * 20,
    "computador jogou: {computador} !!!",
    "-=" * 20,
    "você jogou : {jogador} !!!",
    "-=" * 20,
    ]
)

print(OPCOES)
jog = int(input(PERGUNTA)) -1
comp = randint(0, 2)


if comp == PEDRA:
    if jog == PEDRA:
        msg = EMPATE
    elif jog == PAPEL:
        msg = GANHOU
    elif jog == TESOURA:
        msg = PERDEU
    else:
        msg = INVALIDO
elif comp == PAPEL:
    if jog == PEDRA:
        msg = PERDEU
    elif jog == PAPEL:
        msg = EMPATE
    elif jog == TESOURA:
        msg = GANHOU
    else:
        msg = INVALIDO
elif comp == TESOURA:
    if jog == PAPEL:
        msg = PERDEU
    elif jog == PEDRA:
        msg = GANHOU
    elif jog == TESOURA:
        msg = EMPATE
    else:
        msg = INVALIDO
else:
    msg = "jogada extremamente invalida!"


print(RESULTADO.format(computador=itens[comp], jogador=itens[jog]))
print(msg)