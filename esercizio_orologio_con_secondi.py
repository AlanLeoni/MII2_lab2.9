"""
Costruzione di un orologio stile FFS con ore, minuti e secondi
In particolare le funzioni permettono di:
- creare la lancetta dei secondi
- creare un orologio stile FFS con indicazione su ore, minuti e secondi
"""
from img_lib_v0_6 import(
    Immagine, 
    affianca, 
    cerchio, 
    rettangolo, 
    ruota,  
    cambia_punto_riferimento, 
    componi, 
    salva_immagine,
    visualizza_immagine
    )

from esercizio_orologio import(
    crea_lancetta_ore,
    angolo_ore,
    crea_lancetta_minuti,
    angolo_minuti,
    crea_quadrante
    )


RAGGIO: int = 300
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)


def crea_lancetta_secondi(angolo: int) -> Immagine:
    """
    Crea la lancetta dei secondi in posizione ore 0
    
    :param angolo: angolo di apertura della lancetta
    :returns: una lancetta ruotata
    """
    altezza_lancetta = RAGGIO * 2 // 100
    pallino_lancetta = cambia_punto_riferimento(
        cerchio(RAGGIO *8 // 100, ROSSO), 
        "middle", "middle")
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 25 // 100, altezza_lancetta, ROSSO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 60 // 100, altezza_lancetta, ROSSO)),
        "left", "middle")
    lancetta_orizzontale = affianca(
        lancetta_testa, affianca(lancetta_coda, pallino_lancetta))
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    return ruota(lancetta_verticale, -(angolo))


def angolo_secondi(secondi: int) -> int:
    """
    Definisce il grado di rotazione rispetto ai secondi
    
    :param secondi: la posizione della lancetta
    :returns: l'angolo di apertura della lancetta rispetto alla posizione 0
    """
    angolo = secondi * 6
    return angolo


def crea_orologio(ore: int, minuti: int, secondi: int) -> Immagine:
    ore_minuti = componi(crea_lancetta_ore(angolo_ore(ore)), 
                         crea_lancetta_minuti(angolo_minuti(minuti)))
    lancette = componi(crea_lancetta_secondi(angolo_secondi(secondi)),
                       ore_minuti)
    return componi(lancette, crea_quadrante())

salva_immagine("orologio_ore_minuti_secondi", crea_orologio(4, 10, 45))