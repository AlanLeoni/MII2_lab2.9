from img_lib_v0_6 import(
    Immagine, 
    affianca, 
    cerchio, 
    immagine_vuota, 
    rettangolo, 
    ruota, 
    sovrapponi, 
    cambia_punto_riferimento, 
    componi, 
    salva_immagine,
    visualizza_immagine)

# uso raggio come unita' di riferimento
RAGGIO: int = 300
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)
GRIGIO = (84, 84, 84)

def crea_sfondo() -> Immagine:
    sfondo_grigio = cerchio(RAGGIO, GRIGIO)
    sfondo_bianco = cerchio((RAGGIO * 95 // 100), BIANCO)
    sfondo: Immagine = sovrapponi(sfondo_bianco, sfondo_grigio)
    return sfondo
#visualizza_immagine(crea_sfondo(), debug = True)

def crea_lancetta_secondi(angolo: int) -> Immagine:
    altezza_lancetta = RAGGIO * 2 // 100
    pallino_lancetta = cambia_punto_riferimento(cerchio(RAGGIO *8 // 100, ROSSO),"middle", "middle")
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 25 // 100, altezza_lancetta, ROSSO)), "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 60 // 100, altezza_lancetta, ROSSO)), "left", "middle")
    lancetta_orizzontale = affianca(
        lancetta_testa, affianca(lancetta_coda, pallino_lancetta))
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    lancetta_secondi = ruota(lancetta_verticale, -(angolo))
    return lancetta_secondi
#visualizza_immagine(crea_lancetta_secondi(5), debug=True)
def angolo_secondi(secondi: int) -> int:
    angolo = secondi * 6
    return angolo


def crea_lancetta_minuti(angolo: int) -> Immagine:
    altezza_lancetta = RAGGIO * 10 // 100
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 20 // 100, altezza_lancetta, NERO)), "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 85 // 100, altezza_lancetta, NERO)), "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    lancetta_minuti = ruota(lancetta_verticale, -(angolo))
    return lancetta_minuti
# visualizza_immagine(crea_lancetta_minuti(5), debug=True)

def angolo_minuti(minuti: int) -> int:
    angolo = minuti * 6
    return angolo

# accetta input ore 12h e 24h
def angolo_ore(ore: int) -> int:
    angolo = (ore * 30) % 360
    return angolo


def crea_lancetta_ore(angolo: int) -> Immagine:
    altezza_lancetta = RAGGIO * 12 // 100
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 20 // 100, altezza_lancetta, NERO)), "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 60 // 100, altezza_lancetta, NERO)), "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    lancetta_ore = ruota(lancetta_verticale, -(angolo))
    return lancetta_ore
# visualizza_immagine(crea_lancetta_ore(45), debug=True)


def crea_tacca_minuti() -> Immagine:
    altezza_tacca = RAGGIO * 3 // 100
    testa_tacca = rettangolo(RAGGIO * 82 // 100, altezza_tacca, BIANCO)
    coda_tacca = rettangolo(RAGGIO * 8 // 100, altezza_tacca, NERO)
    tacca_minuti = cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")
    return tacca_minuti


def crea_tacche_minuti() -> Immagine:
    gradi = 6
    quadrante_prec = immagine_vuota()
    for tacca in range(0, 360, gradi):
        tacca_quadrante = ruota(crea_tacca_minuti(), tacca)
        quadrante_minuti = componi(quadrante_prec, tacca_quadrante)
        quadrante_prec = quadrante_minuti
    return quadrante_minuti
# visualizza_immagine(crea_tacche_minuti(), debug=True)


def crea_tacca_cinque_minuti() -> Immagine:
    altezza_tacca = RAGGIO * 8 // 100
    testa_tacca = rettangolo(RAGGIO * 70 // 100, altezza_tacca, BIANCO)
    coda_tacca = rettangolo(RAGGIO * 20 // 100, altezza_tacca, NERO)
    tacca_minuti = cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")
    return tacca_minuti


def crea_tacche_cinque_minuti() -> Immagine:
    gradi = 30
    quadrante_prec = immagine_vuota()
    for tacca in range(0, 360, gradi):
        tacca_quadrante = ruota(crea_tacca_cinque_minuti(), tacca)
        quadrante_cinque_minuti = componi(quadrante_prec, tacca_quadrante)
        quadrante_prec = quadrante_cinque_minuti
    return quadrante_cinque_minuti
# visualizza_immagine(crea_tacche_cinque_minuti(), debug=True)


def crea_quadrante() -> Immagine:
    quadrante = componi(
        componi(crea_tacche_cinque_minuti(), crea_tacche_minuti()), crea_sfondo())
    return quadrante


# visualizza_immagine(crea_quadrante(), debug=True)


def crea_orologio(ore: int, minuti: int, secondi: int) -> Immagine:
    ore_minuti = componi(crea_lancetta_ore(angolo_ore(ore)), crea_lancetta_minuti(angolo_minuti(minuti)))
    lancette = componi(crea_lancetta_secondi(angolo_secondi(secondi)), ore_minuti)
    orologio = componi(lancette, crea_quadrante())
    return orologio

salva_immagine("orologio_ore_minuti_secondi", crea_orologio(4, 10, 45))
#visualizza_immagine(crea_orologio(4, 10, 45))