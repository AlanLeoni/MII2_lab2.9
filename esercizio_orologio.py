from img_lib_v0_6 import Immagine, affianca, cerchio, immagine_vuota, rettangolo, ruota, visualizza_immagine, sovrapponi, cambia_punto_riferimento, componi, salva_immagine

# uso raggio come unita' di riferimento
RAGGIO: int = 300
COLORE_SCURO = (0, 0, 0)
COLORE_CHIARO = (255, 255, 255)
COLORE_SECONDI = "red"


def crea_sfondo() -> Immagine:
    sfondo_grigio = cerchio(RAGGIO, "grey")
    sfondo_bianco = cerchio((RAGGIO * 95 // 100), "white")
    sfondo: Immagine = sovrapponi(sfondo_bianco, sfondo_grigio)
    return sfondo
#visualizza_immagine(crea_sfondo(), debug = True)


def crea_lancetta_minuti(angolo: int) -> Immagine:
    altezza_lancetta = RAGGIO * 10 // 100
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 20 // 100, altezza_lancetta, COLORE_SCURO)), "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 90 // 100, altezza_lancetta, COLORE_SCURO)), "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    lancetta_minuti = ruota(lancetta_verticale, -(angolo))
    return lancetta_minuti

def angolo_minuti(minuti: int) -> int:
    angolo = minuti * 6
    return angolo


def angolo_ore(ore: int) -> int:
    angolo = ore * 30
    return angolo


def crea_lancetta_ore(angolo: int) -> Immagine:
    altezza_lancetta = RAGGIO * 12 // 100
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 10 // 100, altezza_lancetta, COLORE_SCURO)), "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 70
                    // 100, altezza_lancetta, "black")), "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    lancetta_ore = ruota(lancetta_verticale, -(angolo))
    return lancetta_ore
# visualizza_immagine(crea_lancetta_ore(45), debug=True)


def crea_tacca_minuti() -> Immagine:
    altezza_tacca = RAGGIO * 2 // 100
    testa_tacca = rettangolo(RAGGIO * 86 // 100, altezza_tacca, COLORE_CHIARO)
    coda_tacca = rettangolo(RAGGIO * 4 // 100, altezza_tacca, COLORE_SCURO)
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
    altezza_tacca = RAGGIO * 4 // 100
    testa_tacca = rettangolo(RAGGIO * 80 // 100, altezza_tacca, COLORE_CHIARO)
    coda_tacca = rettangolo(RAGGIO * 10 // 100, altezza_tacca, COLORE_SCURO)
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


def crea_orologio(ore: int, minuti: int) -> Immagine:
    orologio = componi(
        componi(crea_lancetta_ore(angolo_ore(ore)), crea_lancetta_minuti(angolo_minuti(minuti))), crea_quadrante())
    return orologio
salva_immagine("orologio", crea_orologio(5, 10))
