
import fltk
IMAGES = ["assets/chat.png", "assets/souris.png", None]

def taille_grille(defaut=5):
    saisie = input("Entrez le nombre de couleurs (5 par défaut) : ")
    if saisie == "":
        return defaut
    return int(saisie)

def clic_selection(x, y, cases, x0, t):
    if x >= x0:
        k = (x - x0) // t
        i = y // t
        if 0 <= i < cases and 0 <= k < 3:
            return (i, k)
    return None

def dessiner_zone(cases, liste_couleurs, x0, t):
    for i in range(cases):
        for k in range(3):
            x = x0 + k*t
            y = i * t
            fltk.rectangle(x, y, x+t, y+t, couleur="black", remplissage=liste_couleurs[i])
            if IMAGES[k] is not None:
                fltk.image(x + t/2, y + t/2, IMAGES[k], largeur=t-10, hauteur=t-10, ancrage="center")
            else:
                fltk.texte(x + t/2, y + t/2, " ", couleur="black", ancrage="center")

def fenetre(n, m, cases=5, taille = 75):
    liste_couleurs = ["blue", "red", "green", "yellow", "orange"]
    cases = taille_grille()
    fltk.cree_fenetre(n, m)
    x0 = cases * taille+20
    t = 50
    dessiner_zone(cases, liste_couleurs, x0, t)
    fltk.__canevas.root.title("Chats et souris – Éditeur de plateau")
    case = []
    for i in range(cases):
        for j in range(cases):
            x = j * taille
            y = i * taille
            fltk.rectangle(x, y, x+taille, y+taille, couleur="black", remplissage="white")
    selection = None
    while True:
        ev = fltk.donne_ev()
        if fltk.type_ev(ev) == 'Quitte':
            break
        elif fltk.type_ev(ev) == 'ClicGauche':
            fltk.efface("msg")
            x = fltk.abscisse(ev)
            y = fltk.ordonnee(ev)
            choix = clic_selection(x, y, cases, x0, t)
            if choix is not None:
                selection = choix
                fltk.efface("surbrillance")
                i, k = choix
                fltk.rectangle(x0 + k*t, i*t, x0 + k*t + t, i*t + t,couleur="black", epaisseur=4, tag="surbrillance")
            else:
                colonne = x // taille
                ligne = y // taille
                if 0 <= ligne < cases and 0 <= colonne < cases:
                    if selection is None:
                        fltk.texte(n/2, 480, "Choisis d'abord une carte", couleur="red", ancrage="center", tag="msg")
                    elif (ligne, colonne) in case:
                        fltk.texte(n/2, 480, "Case déjà sélectionnée", couleur="red", ancrage="center", tag="msg")
                    
                    else:
                        case.append((ligne, colonne))
                        x1 = colonne * taille
                        y1 = ligne * taille
                        fltk.rectangle(x1, y1, x1 + taille, y1 + taille,couleur="black", remplissage=liste_couleurs[selection[0]])
                        if IMAGES[selection[1]] is not None:
                            fltk.image(x1 + taille/2, y1 + taille/2, IMAGES[selection[1]], largeur=taille-10, hauteur=taille-10, ancrage="center")        
        elif fltk.type_ev(ev) == 'ClicDroit':
            fltk.efface("msg")
            x = fltk.abscisse(ev)
            y = fltk.ordonnee(ev)
            colonne = x // taille
            ligne = y // taille
            if (ligne, colonne) in case:
                case.remove((ligne, colonne))
                x1 = colonne * taille
                y1 = ligne * taille
                fltk.rectangle(x1, y1, x1 + taille, y1 + taille, couleur="black", remplissage="white")
        fltk.mise_a_jour()

if __name__ == "__main__":
    fenetre(850, 500)
