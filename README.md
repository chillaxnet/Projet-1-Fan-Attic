# Chats et souris – Projet 1

Projet 1 – L1 Maths-Informatique, Université Gustave Eiffel, semestre 1 (2026-2027).

Nous développons en **Python 3**, avec la bibliothèque graphique **`fltk`** exclusivement, une version logicielle du jeu de plateau **Chats et souris** pour le client fictif **Game Fan-Attic**, une association de passionnés de jeux.

Le projet est réalisé en équipe de 3 et simule une relation client / équipe de développement : cahier des charges (V1 et V2), deux rendez-vous avec le client, rapport, livraison du programme et soutenance/recette en janvier 2027.

## Le jeu

Chats et souris se joue à deux joueurs ou plus. À tour de rôle, un joueur crée une grille de cartes de couleur et cache dessus des chats et des souris. Les autres joueurs, en équipe, doivent ensuite tous les retrouver en perdant le moins de vies possible.

Le jeu comporte donc deux phases :

1. **l'édition de la grille** (livrable 1) ;
2. **le défi** (livrables suivants).

### Règles de construction d'une grille

Pour $n$ couleurs choisies :

- la grille contient exactement $n^2$ cartes, avec $n$ cartes par couleur ;
- dans chaque couleur, une seule carte cache un chat et une seule carte cache une souris, les autres sont vides ;
- il ne peut pas y avoir deux chats sur la même ligne ou la même colonne ;
- la même règle s'applique aux souris ;
- un chat et une souris de la même couleur ne peuvent pas être sur deux cases adjacentes, diagonales comprises.

## Livrable 1 : l'éditeur de plateau

Le programme permet de construire un plateau de jeu et de le visualiser dans une fenêtre `fltk`.

1. **Lancement.** Une fenêtre s'ouvre, demande le nombre de couleurs $n$ (5 par défaut) et affiche une grille vide de $n^2$ cases.
2. **Sélection d'une carte.** Un clic sur un type de carte dans la zone de sélection la met en évidence.
3. **Placement d'une carte.** Un clic sur une case de la grille y affiche la carte sélectionnée.
4. **Modification.** Un clic droit sur une carte posée la retire de la grille et la remet dans la zone de sélection.
5. **Messages.** Un message s'affiche en bas de la fenêtre et l'action est refusée si :
   - la case est occupée ;
   - il n'y a plus de carte de ce type ;
   - deux chats (ou deux souris) sont sur la même ligne ou colonne ;
   - un chat et une souris de même couleur sont voisins, diagonales comprises.
6. **Fin de l'édition.** Le bouton « Valider » n'est actif que lorsque la grille est complète. Un clic retourne les cartes face cachée.

> **Hors périmètre du livrable 1 :** la sauvegarde, la phase de défi (retourner les cartes, vies, jetons) et le calcul des scores.

### Prochains livrables (prévision)

- **Livrable 2 :** phase de défi (retourner les cartes, vies, jetons).
- **Livrable final :** jeu complet conforme au sujet, avec toutes les fonctionnalités demandées.

Ces éléments seront précisés dans les versions suivantes du cahier des charges, en tenant compte des retours du client.

### Pistes d'amélioration (à discuter avec le client)

- plusieurs niveaux de difficulté ;
- choix libre des couleurs ;
- sons et effets sonores.

## Technologies et installation

- **Langage :** Python 3
- **Interface graphique :** `fltk` uniquement (le module `fltk.py` est fourni dans ce dépôt, rien à installer)
- **Système recommandé :** Windows 11 (compatible macOS et Linux)
- **Outils de développement :** Visual Studio Code, Git Bash
- **Outils de travail :** dépôt GitHub partagé, Discord

### Lancer le programme

```bash
git clone https://github.com/chillaxnet/Projet-1-Fan-Attic.git
cd Projet-1-Fan-Attic
python NOM_DU_FICHIER.py
```

## Planning

| Rendez-vous | Date approximative | Ordre du jour | Livrable présenté |
|---|---|---|---|
| Rendez-vous 1 | 27 novembre 2026 | Présentation du CDC V1, démonstration de l'éditeur de plateau, retours du client | Livrable 1 : éditeur de plateau |
| Rendez-vous 2 | 11 décembre 2026 | Bilan du RDV 1, présentation du CDC V2, démonstration de la phase de jeu | Livrable 2 |
| Soutenance / recette | Janvier 2027 | Présentation du programme final et du rapport, évaluation selon le CDC final | Programme final |

## Équipe

| Membre | Rôle(s) |
|---|---|
| BELHADJ MAHAMMED Ahmed | Chef de projet, développement, interface graphique, tests |
| POMMEREAU Tony | Développement, interface graphique, tests |
| BOYACI Hasan | Développement, tests, rédaction |

Le code est écrit exclusivement par les trois membres de l'équipe. Aucun code externe n'est réutilisé, à l'exception de la bibliothèque `fltk`, utilisée selon sa propre licence. L'IA générative n'est pas utilisée pour produire le code livré, seulement ponctuellement pour expliquer ou vérifier des notions.

## Données

Le programme ne collecte ni ne stocke de données personnelles. Si une donnée doit être sauvegardée, elle le sera sur le stockage de la machine utilisée, et non sur un serveur distant.

## Licence

Code publié sous licence **MIT**. Copyright © 2026 Ahmed BELHADJ MAHAMMED, Tony POMMEREAU, Hasan BOYACI.

Le client est libre d'utiliser, de modifier et de réutiliser le code, à condition de conserver cette mention de copyright.
