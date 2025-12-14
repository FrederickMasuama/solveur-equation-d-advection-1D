# solveur-equation-d-advection-1D

# Solveur équation d'advection

Ce projet porte sur l’implémentation et l’analyse numérique d'un solveur grâce aux schémas de différences finies explicites pour la résolution de l’équation d’advection linéaire unidimensionnelle :

∂
𝑡
𝑢
+
𝑐
 
∂
𝑥
𝑢
=
0
,
𝑐
∈
𝑅
∂
t
	​

u+c∂
x
	​

u=0,c∈R

Cette équation est un modèle fondamental des équations hyperboliques de transport, apparaissant notamment en mécanique des fluides, en acoustique et en dynamique des populations.

L’objectif du projet est double :

* Implémenter un solveur utilisant plusieurs schémas numériques classiques,

* En suite, par un exemple d'application, analyser leur stabilité, précision et convergence, en particulier au regard de la condition

 # Méthodes numériques

 Trois schémas de différences finies ont été implémentés :

* Schéma de Lax–Friedrichs

* Schéma décentré à gauche (upwind gauche)

* Schéma décentré à droite (upwind droite)

Ces schémas sont appliqués sur un maillage uniforme en espace et en temps.
Ils permettent de comparer :

la diffusion numérique,

la propagation des discontinuités,

l’adaptation du schéma au signe de la vitesse d’advection 
𝑐
c.

# Fonctions tests

Les méthodes sont testées sur trois fonctions représentatives :

* Pulsion gaussienne

Fonction régulière

Adaptée à l’analyse de la diffusion et de la précision

* Onde carrée

Fonction discontinue

Permet d’observer la dissipation numérique et la stabilité

* Onde sinusoïdale

Fonction périodique et régulière

Utilisée pour l’étude de la convergence et de l’erreur de phase

# Condition de stabilité et convergence
La stabilité des schémas est étudiée via le nombre de Courant–Friedrichs–Lewy (CFL) :

CFL
=
𝑐
 
Δ
𝑡
Δ
𝑥
CFL=
Δx
cΔt
	​


Les simulations mettent en évidence :

la nécessité du respect de la condition CFL pour les schémas explicites,

les comportements instables lorsque cette condition est violée,

les différences de robustesse entre les schémas.
## Structuration du projet

Le projet contient quatre fichiers .py :
1. solveur, le fichier principal
2. exemples, contenant le script d'exemple d'application appelant le solveur
3. redac_fxt, qui permet à l'utilisateur de rentrer une nouvelle fonction, autre les trois proposées. 
4. test_convergence, qui vérifie la convergence de la méthode par rapport à la condition CFL
## Dépendances

L'utilisation du code nécessite les bibliothèques suivantes :

* numpy 
* matplotlib 


## Paramètres

Les paramètres sont à rentrés manuellement par l'utilisateur: La célérité, le domaine, les conditions aux bords... 
## Résultats

Les scripts génèrent un graphe illustrant la solution analytique,  l'évolution du système d'après la résolution numérique via la méthode des différences finies.  
