import fltk

def fenetre(n,m):
    fltk.cree_fenetre(n,m)
    fltk.__canevas.root.title("Chats et souris – Éditeur de plateau")
    while True:
        ev = fltk.donne_ev()
        if fltk.type_ev(ev) == 'Quitte':
            break
        fltk.mise_a_jour()
    fltk.ferme_fenetre()

if __name__ == "__main__":
    fenetre(850, 500)