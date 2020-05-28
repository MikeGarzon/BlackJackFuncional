from random import shuffle

def baraja():
    return [(n, p) for n in (['A', 'J', 'Q', 'K'] +[str(x) for x in range (2,11)]) for p in ['♠','♥','♣','♦']]

def mezclar(baraja):
    shuffle (baraja)
    return baraja

def sacar_carta(baraja):
    if baraja == []:
        pass
    else:
        print (baraja[0], valor_carta(baraja[0]))

def valor_carta(carta):
    if carta[0] in ['J', 'Q', 'K']:
        return 10
    elif carta[0] == 'A':
        return 1
    else:
        return int(carta[0])

def valor_mano(mano):
    if mano == []:
        return 0
    else:
        print(mano[0]) 
        return valor_carta(mano[0]) + valor_mano(mano[1:])

def valor_mano_recargado(mano):
    print (mano)
    if valor_mano(mano) <=11 and 1 in [valor_carta(x) for x in mano]:
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)


sacar_carta(mezclar(baraja()))
