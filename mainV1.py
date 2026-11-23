
import fltk


def fenetre(n, m, cases = 6, taille = 75):
    fltk.cree_fenetre(n, m)
    fltk.__canevas.root.title("Chats et souris – Éditeur de plateau")
    case = []
    for i in range(cases):
        for j in range(cases):
            x = j * taille
            y = i * taille
            fltk.rectangle(x, y, x+taille, y+taille, couleur="black", remplissage="white")
    while True:
        ev = fltk.donne_ev()
        if fltk.type_ev(ev) == 'Quitte':
            break
        elif fltk.type_ev(ev) == 'ClicGauche':
            x = fltk.abscisse(ev)
            y = fltk.ordonnee(ev)
            colonne = x // taille
            ligne = y // taille
            if 0 <= ligne < cases and 0 <= colonne < cases:
                x1 = colonne * taille
                y1 = ligne * taille
                if (ligne, colonne) not in case:
                    case.append((ligne, colonne))
                    fltk.rectangle(x1, y1, x1 + taille, y1 + taille, couleur="black", remplissage="blue")
                else :
                    fltk.texte(850/2, 480, "Case déjà sélectionnée", couleur="red", ancrage="center")
        fltk.efface(fltk.texte(850/2, 480, "Case déjà sélectionnée", couleur="red", ancrage="center"))

               
        fltk.mise_a_jour()
    fltk.ferme_fenetre()

if __name__ == "__main__":
    fenetre(850, 500)
