from img_lib_v0_6 import Immagine, affianca, cerchio, immagine_vuota, rettangolo, ruota, visualizza_immagine, sovrapponi, cambia_punto_riferimento

# uso raggio come unita' di riferimento
RAGGIO: int = 300

def crea_sfondo() -> Immagine:
  sfondo_grigio = cerchio(RAGGIO, "grey")
  sfondo_bianco = cerchio((RAGGIO * 95 //100), "white")
  sfondo: Immagine = sovrapponi(sfondo_bianco, sfondo_grigio)
  return sfondo
#visualizza_immagine(crea_sfondo())

def crea_lancetta_minuti(angolo: int) -> Immagine:
    altezza_lancetta = RAGGIO * 10 // 100
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 10 // 100, altezza_lancetta, "black")),"right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 90 // 100, altezza_lancetta, "black")), "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    lancetta_minuti = ruota(lancetta_verticale, -(angolo))
    return lancetta_minuti

def crea_lancetta_ore(angolo: int) -> Immagine:
    altezza_lancetta = RAGGIO * 12 // 100
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 10 // 100, altezza_lancetta, "black")),"right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 70
                    // 100, altezza_lancetta, "black")), "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    lancetta_ore = ruota(lancetta_verticale, -(angolo))
    return lancetta_ore
#visualizza_immagine(crea_lancetta_ore(45), debug=True)

def crea_tacca_minuti() -> Immagine:
    altezza_tacca = RAGGIO * 3 // 100
    testa_tacca = rettangolo(RAGGIO * 80 // 100, altezza_tacca, "white")
    coda_tacca = rettangolo(RAGGIO * 10 // 100, altezza_tacca, "black")
    tacca_minuti = cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")
    return tacca_minuti
visualizza_immagine(crea_tacca_minuti(), debug=True)

def crea_tacche_minuti() -> Immagine:
    gradi = 6
    quadrante_prec = cambia_punto_riferimento(immagine_vuota(), "middle", "middle")
    for i in range(0, 360, 6):
        tacca_quadrante = ruota(crea_tacca_minuti(), gradi)
        gradi = gradi + gradi
        quadrante_minuti = sovrapponi(quadrante_prec, tacca_quadrante)
        quadrante_prec = quadrante_minuti
    return quadrante_prec
        
visualizza_immagine(crea_tacche_minuti(), debug=True)
        
# def crea_tacche_cinque_minuti() -> Immagine:
#     altezza_tacca = RAGGIO * 8 // 100
#     testa_tacca = rettangolo(RAGGIO * 60 // 100, altezza_tacca, "white")
#     coda_tacca = rettangolo(RAGGIO * 30 // 100, altezza_tacca, "black")
#     tacche_cinque_minuti = cambia_punto_riferimento(
#       affianca(testa_tacca, coda_tacca), "left", "middle")
#     return tacche_cinque_minuti
