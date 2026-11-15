from fltk import *

def fenetre(n,m):
    cree_fenetre(n,m)
    while True:
        ev = donne_ev()
        if type_ev(ev) == 'Quitte':
            break
        mise_a_jour()
    ferme_fenetre()

fenetre(500,500)