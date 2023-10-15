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

"""
TABELA DA VITORIA
GANHADOR
PEDRA TESOURA
TESOURA PAPEL
PAPEL PEDRA

"""

def jogo(comp, jog):  
    if comp == jog:
        return EMPATE

    msg = PERDEU
    
    if comp == PEDRA:
        if jog == PAPEL:
            msg = GANHOU
    elif comp == PAPEL:
        if jog == TESOURA:
            msg = GANHOU
    elif comp == TESOURA:
        if jog == PEDRA:
            msg = GANHOU

    return msg

def entrada(valor):
    n = int(valor) -1
    if n not in (PEDRA, PAPEL, TESOURA):
        return INVALIDO

    return n
    
def main():
    print(OPCOES)
    jog = entrada(input(PERGUNTA))
    comp = randint(0, 2)    

    if type(jog) is str:
        print(jog)
        return

    msg = jogo(comp, jog)
    print(msg)
    print(RESULTADO.format(computador=itens[comp], jogador=itens[jog]))
    print(msg)


def test():
    assert jogo(comp=PEDRA, jog=PEDRA) == EMPATE
    assert jogo(comp=PAPEL, jog=PAPEL) == EMPATE
    assert jogo(comp=TESOURA, jog=TESOURA) == EMPATE

    assert jogo(comp=PEDRA, jog=PAPEL) == GANHOU
    assert jogo(comp=TESOURA, jog=PEDRA) == GANHOU
    assert jogo(comp=PAPEL, jog=TESOURA) == GANHOU
    
    assert jogo(comp=PEDRA, jog=TESOURA) == PERDEU
    assert jogo(comp=PAPEL, jog=PEDRA) == PERDEU
    assert jogo(comp=TESOURA, jog=PAPEL) == PERDEU

    assert entrada("1") == PEDRA
    assert entrada("2") == PAPEL
    assert entrada("3") == TESOURA
    assert entrada("0") == INVALIDO
    assert entrada("4") == INVALIDO
    
    print("Tudo certo.")

main()
#test()