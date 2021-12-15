from esercizio_orologio_con_secondi import(
    crea_orologio
)

from img_lib_v0_6 import crea_gif

def crea_animazione_orologio(ore: int, minuti: int, secondi: int):
    lista_orologi = [
        crea_orologio(ore, minuti, passo)
        for passo in range(0, secondi)
    ]
    return crea_gif("animazione_orologio",lista_orologi, 1)

crea_animazione_orologio(4, 10, 40)
