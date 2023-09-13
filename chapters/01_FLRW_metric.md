La métrique de Friedmann-Lemaître-Robertson-Walker
================================





Principes cosmologiques
-----------------------

Dans la cosmologie contemporaine, l'équation d'Einstein
[](#eq:einstein2) est donc l'équation de base pour décrire
l'évolution de l'Univers. Pour poursuivre les calculs, il faut cependant
rajouter deux hypothèses.

1.  l'Univers est homogène : la métrique ne dépend donc pas de la
    position dans l'espace, donc aucune position n'est particulière dans
    l'Univers. Cette affirmation, issue du principe Copernicien, n'est
    que statistiquement vraie car localement on observe bien que la
    matière a formé des grumeaux (planètes, étoiles, galaxies,\...) au
    milieu de larges vides. Cependant l'observation de l'Univers à
    grande échelle montre que l'Univers est bien globalement homogène à
    des échelles plus grandes que la distance moyenne
    inter-galactique[^4] 100 (voir
    figure [](#fig:sdss) et par exemple {cite:t}`Scrimgeour2012` pour une
    mesure de l'homogénéité de l'Univers par comptage de galaxies).

2.  l'Univers est isotrope: aucune direction n'est privilégiée. Ainsi,
    des observations effectuées dans deux directions différentes du ciel
    sont équivalentes. Ceci est bien vérifié par l'observation du fond
    diffus cosmologique micro-onde (CMB) dont la température est mesurée
    identique dans toutes les directions de l'espace à des fluctuations
    de température $\delta \theta$ de l'ordre de
    $\delta \theta / \theta \approx 10^{-5}$ près (voir
    figure [](#fig:cmb_planck) et par exemple
    {cite:t}`ThePlanckCollaboration2013XIII` pour une vérification du principe
    d'isotropie utilisant l'effet Sunyaev-Zeldovich).


```{figure} ../images/sdss_pie2.jpg
:name: fig:sdss
:align: center
:width: 60%

Répartition des galaxies détectées par l'expérience Sloan Digital Sky
Survey (SDSS), en fonction du redshift $z$ (cette notion sera définie
plus loin, mais peut être liée à une notion de distance, $z=0$ étant
notre position).
```


```{figure} ../images/CMB_planck.jpg
:name: fig:cmb_planck
:align: center
:width: 70%

Carte de température du fond diffus cosmologique micro-onde (CMB)
observée par le satellite Planck. L'écart relatif observé entre la
température des points chauds (rouges) ou froids (bleus) par rapport à
la moyenne est de l'ordre de $\delta \theta / \theta \approx 10^{-5}$.
```

Maximally symmetric spaces
------------------


Supposer les principes d'homogénéité et d'isotropie pour ce tenseur,
impose que la métrique devra aussi respecter ces propriétés. Une
solution de l'équation d'Einstein respectant ces conditions est la
métrique de Friedmann-Lemaître-Robertson-Walker (FLRW), utilisant le jeu
de coordonnées sphériques usuel $(ct, r, \theta, \phi)$:
$$\begin{aligned}\label{eq:flrw}
g_{\mu\nu} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \frac{a^2(t)}{1-kr^2} & 0 & 0 \\ 
0 & 0 & a^2(t)r^2 & 0 \\ 
0 & 0 & 0 & a^2(t) r^2 \sin^2 \theta  \\ 
\end{pmatrix},\end{aligned}
$$ 
où $a(t)$ est une fonction inconnue du
temps appelée paramètre d'échelle, et $k$ une constante qui par un choix
particulier d'unités pour $r$ peut prendre les valeurs $+1$, 0 et $-1$.
Suivant les valeurs de $k$, on a trois espaces de dimension 3 possibles
(voir figure [](#fig:espaces)): $$k = \left\lbrace
\begin{array}{rl}
 +1 & \text{3-sphère} \\
 0 & \text{espace\ plat} \\
 -1 & \text{3-hyperboloïde} \\
\end{array}
\right.$$ Le paramètre d'échelle $a(t)$ peut être obtenu en résolvant
l'équation d'Einstein connaissant le contenu du tenseur
énergie-impulsion de l'Univers $T^{\mu\nu}$ et la valeur de $k$. Une
remarque: dans la métrique FLRW, c'est la quantité $a(t)r$ qui a la
dimension d'une longueur, et non directement la coordonnée radiale $r$.
Cette dernière s'exprime en \"mètres par $a(t)$\": son unité varie donc
dans le temps. La coordonnée $r$ (ainsi que les coordonnées angulaires
$\theta$ et $\phi$) sont des coordonnées dites comobiles car elles
décrivent des positions indépendantes du facteur d'échelle $a(t)$. Nous
y reviendrons plus loin.

Pour un Univers sphérique, le facteur d'échelle $a(t)$ est le rayon de
courbure. Un Univers sphérique dynamique correspond donc à un univers
possédant un rayon de courbure variable dans le temps. Un espace plat ne
possède pas d'échelle caractéristique, la valeur de $a(t)$ n'a donc pas
de sens physique. La quantité ayant un sens physique pour un tel univers
est le paramètre de Hubble qui quantifie la vitesse de variation du
facteur d'échelle : $$\fbox{$\displaystyle H = \frac{\dot a}{a} $}$$
avec le point $\dot{}$ exprimant une dérivée par rapport au temps $t$.
Dans le but d'alléger les notations, la dépendance temporelle des
paramètres ne sera pas toujours explicitée, de sorte que $a(t)=a$. On
désignera les paramètres évalués au temps présent $t_0$ par l'indice ou
l'exposant 0 si bien que $a(t_0)=a_0$. Il est toujours possible de
changer de système de coordonnées de sorte que $a_0=1$. Nous
travaillerons systématiquement avec cette convention et omettrons
généralement le terme $a_0$ des équations, sauf pour des raisons
dimensionnelles.

```{list-table} Représentation des équivalents à deux dimensions des trois espaces solution des principes cosmologiques: la 2-sphère, le plan, le 2-hyperboloïde.
:header-rows: 0
:name: fig:espaces

* - ```{image} ../images/sphere.jpeg
    :alt: sphere
    :width: 95%
    :align: center
    ```
  - ```{image} ../images/plan.jpeg
    :alt: plan
    :width: 100%
    :align: center
    ```
  - ```{image} ../images/hyperboloid.jpeg
    :alt: hyperboloid
    :width: 90%
    :align: center
    ```
```


Coordonnées comobiles
---------------------




Le décalage spectral, ou redshift
----------------------------------

Pour mesurer la valeur des différents paramètres de densité dans notre
Univers, il faut avoir accès au paramètre d'échelle $a(t)$. Ceci est
possible par la mesure du décalage spectral de la lumière venant de
sources distantes. Dans la métrique FLRW, plaçons-nous par convention au
centre $r=0$, et considérons un objet situé aux coordonnées comobiles
$\left(r_E,\theta_E,\phi_E\right)$, émettant une onde électromagnétique
à l'instant $t_E$ (voir [](#fig:distances_croquis)). Le front d'onde est paramétré par
la coordonnée comobile $r(t)$. Pour cette onde, voyageant à la vitesse
de la lumière, dans la métrique FLRW on a, à tout instant:
$$\label{eq:ds2_lumiere}
d\tau^2=0=-c^2 dt^2+\frac{a^2(t)}{1-kr^2}dr^2.$$ Posons $t_0$ l'instant
de la réception de cette onde en $r=0$, alors grâce à l'équation
précédente on a la relation: $$\label{eq:comobile}
\chi(t_0)\equiv \int_{t_E}^{t_0} \frac{cdt}{a(t)} = \int_0^{r_E}\frac{dr}{\sqrt{1-kr^2}} = \left\lbrace
\begin{array}{cl}
    \arcsin r_E & \text{ si } k=+1 \\
    r_E & \text{ si } k=0 \\
    \text{arcsh } r_E & \text{ si } k=-1 
\end{array}
\right. .$$ 
Cette dernière intégrale est appelée distance comobile car
elle fait abstraction des effets de l'expansion de l'Univers dans le
calcul de la longueur parcourue par la lumière. En effet, elle a la même
dimension que $r$ donc s'exprime en m/$a(t)$.

```{figure} ../images/distances2.png
:name: fig:distances_croquis
:align: center
:width: 50%

Notations pour le calcul du redshift et des distances cosmologiques en coordonnées comobiles.
```

Pour une onde électromagnétique de période $T$,
l'expression [](#eq:ds2_lumiere) étant valable à tout instant, on peut
calculer la même intégrale pour l'onde émise à l'instant $t_E+T_E$ et
reçue à l'instant $t_0+T_0$ (on suppose donc que la période $T$ va
varier au cours du temps): $$\label{eq:comobileT}
\int_{t_E+T_E}^{t_0+T_0} \frac{cdt}{a(t)}= \int_0^{r_E}\frac{dr}{1-kr^2}.$$
Par égalité des
expression [](#eq:comobile) et
[](#eq:comobileT), comme la période $T$ est petite devant les
variations du facteur d'échelle $a(t)$ pour les ondes électromagnétiques
usuelles, on obtient: 
$$\begin{aligned}
\int_{t_E+T_E}^{t_0+T_0} \frac{cdt}{a(t)} & =\int_{t_E}^{t_0} \frac{cdt}{a(t)}  \\
\int_{t_E+T_E}^{t_E} \frac{cdt}{a(t)} & =\int_{t_0+T_0}^{t_0} \frac{cdt}{a(t)} \\
\Leftrightarrow \frac{cT_0}{a(t_0)} & = \frac{c T_E}{a(t_E)}  \\
\Leftrightarrow \frac{\lambda_0}{\lambda_E} & = \frac{a(t_0)}{a(t_E)}\label{eq:redshift2}
\end{aligned}
$$
Directement, si l'espace est en expansion alors $a(t_E) < a(t_0)$ et la
longueur d'onde reçue $\lambda_0$ est donc supérieure à la longueur
d'onde émise $\lambda_E$. On définit alors le décalage spectral,
communément appelé *redshift* en raison du fait que la quasi-totalité
des spectres des galaxies observées sont décalées vers le rouge, par:
$$\label{eq:redshift}
 \fbox{$ \displaystyle{z = \frac{\lambda_0-\lambda_E}{\lambda_E} \Leftrightarrow 1+z = \frac{a_0}{a(t_E)}} $}.$$
Le décalage spectral est à la fois directement lié au paramètre
d'échelle $a(t)$, mais aussi à une grandeur expérimentale directement
mesurable sur le spectre d'émission des objets distants. En effet, en
regardant la position des raies d'absorption et d'émission des objets
lointains, on peut en déduire leurs décalages spectraux par rapport aux
mêmes éléments chimiques situés sur Terre, au repos. Cette donnée
expérimentale est donc souvent associée à la définition des distances en
cosmologie.