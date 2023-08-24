Le modèle standard de la cosmologie
===================================

De Newton à la Relativité Générale
----------------------------------

La Relativité Générale est la théorie de la gravitation à la base de la
cosmologie moderne. Elle donne une explication géométrique à la force
gravitationnelle introduite par Newton trois siècles auparavant. Dans
cette théorie, une chute n'est plus due à un vecteur force
malheureusement orienté vers le sol, mais à la déformation de
l'espace-temps engendrée par la Terre. Formulée ainsi, la Relativité
Générale semble bien compliquée pour peu de choses. Mais les principes
généraux à la base de cette théorie et la richesse de ses implications
(dont la théorie newtonienne) en font la théorie phare pour décrire la
gravitation. Le long de cette section, nous allons introduire pas à pas
plusieurs concepts de la Relativité Générale tels que la dérivée
covariante et le tenseur de Riemann, pour aboutir à l'équation
d'Einstein de la Relativité Générale, base de la cosmologie moderne.
Cette introduction est largement inspirée de {cite:t}`Weinberg1972` et
{cite:t}`Gourgoulhon2013`. La convention usuelle $\hbar=c=1$ sera suivie sauf
si nécessaire.

### Le Principe d'Équivalence

Dans le principe fondamental de la dynamique énoncé par Newton, pourquoi
la masse intervenant dans le terme d'inertie est-elle rigoureusement la
même que celle intervenant dans la gravitation newtonienne? Cette
coïncidence troublante singularise la gravitation par rapport aux autres
interactions, et suggère qu'elle n'est pas une propriété des corps
eux-mêmes mais de l'espace dans lequel ils se meuvent. Considérons une
masse ponctuelle de masse $m$ soumise à un champ gravitationnel externe
uniforme et constant $\vec g$ et à aucune autre force. Alors le principe
fondamental de la dynamique appliqué dans un référentiel galiléen à cet
objet nous permet de prédire sa position $\vec x$ à un instant $t$:
$$m\frac{d^2\vec x}{dt^2} = m\vec g$$ Plaçons nous dans le référentiel
(non galiléen) de l'objet par la transformation de coordonnées suivante:
$$\vec x' = \vec x - \frac{1}{2}\vec g t^2, \qquad t'=t$$ Alors dans ce
référentiel la force gravitationnelle est comme \"absorbée\" par le
terme inertiel:
$$m\frac{d^2\vec x}{dt^2} = m\vec g \Leftrightarrow m\frac{d^2\vec x'}{dt'^2} = 0.$$
Les lois de la physique apparaissent donc identiques pour un observateur
lié à un référentiel galiléen considérant que l'objet subit une force de
gravité et pour un observateur lié à un référentiel uniformément
accéléré et considérant que l'objet ne subit pas de force
gravitationnelle. La force de gravité ressentie par une masse ponctuelle
est donc (localement) équivalente au choix d'un référentiel uniformément
accéléré par rapport à un référentiel galiléen. Pourtant les deux
référentiels ne sont pas équivalents par une transformation de
référentiel galiléen. Le Principe d'Équivalence formulé par Einstein
prend acte de ce constat, et l'étend à des champs gravitationnels qui
varient faiblement dans le temps et l'espace. Il stipule que *à chaque
point de l'espace-temps dans un champ gravitationnel arbitraire il est
possible de choisir un système local de coordonnées inertielles tel que,
dans une région suffisamment petite autour du point en question, toutes
les lois de la nature prennent la même forme que dans un système de
coordonnées cartésien non accéléré et sans gravitation* {cite:p}`Weinberg1972`.
Ce principe est vérifié expérimentalement avec une très bonne précision,
notamment par le *Lunar Laser Ranging* {cite:p}`Williams2004`.

### Équations du mouvement

Appliquons le Principe d'Équivalence à un objet en chute libre. Pour cet
objet, il existe donc localement un système de coordonnées *particulier*
$x^\mu$ tel que l'équation de son mouvement s'écrive de la même manière
que si le référentiel était non accéléré et sans gravitation:
\begin{equation}\label{eq:eqm1}
\frac{d^2x^\mu}{d\tau^2}=0,
\end{equation}
avec $d\tau$ le temps propre[^1]:
$$d\tau^2 \equiv -\eta_{\mu\nu} dx^\mu dx^\nu.$$ 
$\eta_{\mu\nu}$ est la métrique de Minkowski utilisée en Relativité Restreinte. D'après le
Principe d'Équivalence, cette équation est aussi valable dans un certain
voisinage de l'objet en question. Il existe donc un autre système de
coordonnées plus général $x'^\mu$ dans lequel réécrire cette équation.
Cherchons la forme qu'elle prendrait pour ces coordonnées $x'^\mu$:
$$0=\frac{d^2 x^\mu}{d\tau^2}=\frac{d}{d\tau}\left(\frac{\partial x^\mu}{\partial x'^\nu} \frac{dx'^\nu}{d\tau}\right) = \frac{\partial x^\mu}{\partial x'^\nu} \frac{d^2x'^\nu}{d\tau^2} + \frac{\partial^2 x^\mu}{\partial x'^\nu \partial x'^\rho}\frac{dx'^\nu}{d\tau}\frac{dx'^\rho}{d\tau}.$$
Après multiplication par $\partial x'^\nu/\partial x^\mu$, on obtient la
nouvelle équation du mouvement dans le système de coordonnées $x'^\mu$:
$$\label{eq:eqm2}
\frac{d^2x'^\nu}{d\tau^2} + \Gamma^\nu_{\ \mu\rho}\frac{dx'^\mu}{d\tau}\frac{dx'^\rho}{d\tau}=0,$$
où $\Gamma^\nu_{\ \mu\rho}$ est la connexion affine définie par:
$$\Gamma^\nu_{\ \mu\rho} \equiv \frac{\partial x'^\nu}{\partial x^\lambda}\frac{\partial^2 x^\lambda}{\partial x'^\mu \partial x'^\rho}.$$
Le temps propre se réécrit:
$$d\tau^2=-\eta_{\mu\nu} dx^\mu dx^\nu = -g_{\mu\nu} dx'^\mu dx'^\nu$$
ce qui définit ainsi le tenseur métrique $g_{\mu\nu}$:
$$g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial x^\alpha}{\partial x'^\mu} \frac{\partial x^\beta}{\partial x'^\nu}$$
$g_{\mu\nu}$ décrit la géométrie de l'espace-temps dans le nouveau
système de coordonnées $x'^\mu$ et remplace la métrique cartésienne
$\eta_{\mu\nu}$. On pourrait par la suite montrer que
$\Gamma^\nu_{\ \mu\rho}$ peut ne s'écrire qu'à l'aide d'un seul système
de coordonnées et du tenseur métrique: $$\label{eq:connexion}
\Gamma^\nu_{\ \mu\rho} = \frac{1}{2}g^{\lambda\nu}\left( \frac{\partial g_{\lambda\rho}}{\partial x'^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x'^\rho}  - \frac{\partial g_{\mu\rho}}{\partial x'^\lambda} \right)$$

La connexion affine $\Gamma^\nu_{\ \mu\rho}$ intervient par ailleurs
dans la définition de la dérivée covariante $V^\nu{}_{;\mu}$ d'un
vecteur $V^\nu$ par rapport à la coordonnée $x'^\mu$:
$$V^\nu{}_{;\mu} \equiv \partial_\mu V^\nu + \Gamma^\nu_{\ \mu\rho}V^\rho$$
Cette définition de la dérivée en Relativité Générale exprime
correctement la variation d'un vecteur le long d'une coordonnée dans un
espace non plat. Elle se transforme de la même manière qu'un vecteur par
un changement de coordonnées, contrairement à la dérivée usuelle: le
vecteur variation est donc correctement défini. Pour illustrer toute sa
profondeur, voici la définition de la dérivée covariante $DV^\mu/D\tau$
non pas par rapport à une coordonnée, mais le long d'une courbe
quelconque paramétrée par le temps propre $\tau$ (invariant par
changement de coordonnées):
$$\frac{DV^\mu}{D\tau} \equiv \frac{dV^\mu}{d\tau} + \Gamma^\mu_{\ \nu\lambda}\frac{dx^\lambda}{d\tau} V^\nu.$$
L'équation du mouvement [](#eq:eqm2) s'écrit alors très simplement
$$\frac{DU^\mu}{D\tau}=0,$$ 
avec $U^\mu$ le vecteur vitesse $dx^\mu/d\tau$. Cette équation ainsi écrite rappelle fortement
l'équation du mouvement initiale
[](#eq:eqm1). La notion de dérivée covariante est donc bien appropriée aux calculs de
Relativité Générale et remplace bien la dérivée usuelle dans ce cadre.

### Vers l'équation d'Einstein

Armés de ces outils, allons maintenant vers une dérivation simple de
l'équation d'Einstein qui résume la gravitation à une déformation de
l'espace-temps par la matière. Commençons par nous intéresser à une
particule massive se déplaçant lentement dans un champ gravitationnel
faible, constant mais quelconque cette fois. L'hypothèse de vitesse
faible nous permet de négliger $d\vec x/d\tau$ devant $dt/d\tau$.
D'après le Principe d'Équivalence, on a vu qu'il existe un système de
coordonnées inertielles $\left(ct,\vec x'\right)$[^2] tel que l'équation
du mouvement [](#eq:eqm2) soit aussi valable dans cette nouvelle situation
avec champ gravitationnel. On a alors au premier ordre dans un champ de
gravité faible et quasi-stationnaire:
$$\frac{d^2x'^\mu}{d\tau^2} + \Gamma^\mu_{\ 00}\left(\frac{dt}{d\tau}\right)^2=0, \qquad \Gamma^\mu_{\ 00} \approx -\frac{1}{2}g^{\mu\nu}\frac{\partial g_{00}}{\partial x'^\nu}.$$

Dans l'hypothèse d'un champ gravitationnel faible, on peut adopter une
métrique presque cartésienne:
$$g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad \vert h_{\mu\nu}\vert\ll 1,$$
et on obtient au premier ordre: $$\left\lbrace
\begin{array}{rl}
    \mu=1,2,3\ : & \displaystyle{\frac{d^2\vec x'}{d\tau^2} = \frac{1}{2}\left(\frac{dt}{d\tau}\right)^2\vec{\nabla} h_{00} } \\
    \mu=0\ : &  \displaystyle{\frac{d^2t}{d\tau^2} = 0.}
\end{array}
\right.$$ D'après la deuxième équation on en déduit que $dt/d\tau$ est
une constante et donc la première équation donne:
$$\label{eq:vers_einstein}
\frac{d^2\vec x'}{dt^2} = \frac{1}{2}\vec{\nabla} h_{00}.$$ Or on sait
que dans la limite newtonienne on a:
$$\frac{d^2\vec x'}{dt^2} = -\vec{\nabla} \phi, \qquad \phi=-\frac{G_N M}{r},$$
avec $\phi$ le potentiel gravitationnel engendré par une masse $M$ à une
distance $r$ ($G_N$ étant la constante de Newton). En comparant avec
[](#eq:vers_einstein), on a $h_{00}=-2\phi+\text{constante}$. Or
le système de coordonnées choisi doit être cartésien à l'infini
(hypothèse de faible perturbation), donc $h_{00}=-2\phi$ et:
$$\label{eq:g00}
g_{00}=-(1+2\phi),$$ 
$g_{00}$ correspondant à la composante temporelle
de la métrique, le battement des horloges dépend par conséquent de
l'intensité du champ gravitationnel. Ceci correspond à l'effet Einstein,
la seule conséquence de la Relativité Générale aujourd'hui utilisée
technologiquement (dans le GPS, voir
[](#fig:effet_einstein)).


```{figure} ../images/effet_eintein.png
:name: fig:effet_einstein
:align: center
:width: 90%

Illustration de l'effet Einstein. Un photon tombant dans un puits
gravitationnel gagne de l'énergie donc sa fréquence augmente. De façon
équivalente, on peut dire que les horloges dans un champ gravitationnel
retardent par rapport à des horloges identiques situées en dehors. Les
récepteurs GPS doivent prendre en compte cet effet pour en déduire leur
position par rapport aux
satellites.
```

Cet exercice sur une particule ponctuelle nous apprend que le champ
gravitationnel est finalement contenu dans la métrique, et que cette
métrique dépend donc de la présence de matière. Il est donc possible
d'imaginer une généralisation de ce constat. Le potentiel newtonien est
déterminé par l'équation de Poisson $\nabla^2\phi = 4\pi G_N \rho$, où
$\rho$ est la densité massique. Cette dernière correspond à la densité
d'énergie du tenseur énergie-impulsion de la matière $T_{00}$ (voir
encadré: $T_{00} = -\rho g_{00} \approx \rho$), donc avec l'équation
[](#eq:g00) on peut obtenir 
$$
\nabla^2 g_{00}=-8\pi G_N T_{00}.
$$ 
On peut alors imaginer qu'il existe un tenseur $G_{\mu\nu}$ combinant des dérivées premières et
secondes de la métrique $g_{\mu\nu}$ généralisant cette dernière
équation à toutes les coordonnées tel que 
$$\label{eq:einstein1}
G_{\mu\nu}=-8\pi G_N T_{\mu\nu}.
$$ 
Cette dernière équation correspond à
une première version de l'équation d'Einstein. Ce raisonnement ne nous a
permis que d'intuiter sa forme, mais une autre démonstration plus
rigoureuse permet d'obtenir l'expression du tenseur d'Einstein
$G_{\mu\nu}$: 
$$
G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R
$$
avec $R_{\mu\nu}$ le tenseur de Ricci et $R$ la courbure scalaire (trace
du tenseur de Ricci $R^\mu_\mu$), eux-mêmes obtenus par le tenseur de
Riemann $R^\mu_{\ \nu\alpha\beta}$: $$\begin{aligned}
R^\mu_{\ \nu\alpha\beta} & = -\partial_\alpha \Gamma^\mu_{\ \nu\beta} +  \partial_\beta \Gamma^\mu_{\ \nu\alpha} - \Gamma^\mu_{\ \alpha\sigma}\Gamma^\sigma_{\ \nu\beta} + \Gamma^\mu_{\ \beta\sigma}\Gamma^\sigma_{\ \nu\alpha} \\
R_{\mu\nu} & =R^\alpha_{\ \mu\alpha\nu}.\end{aligned}$$

$G_{\mu\nu}$ apparaît être de divergence nulle car
$G^{\mu\nu}_{\ \ ;\mu}=0$ (identité de Bianchi). Une conséquence de
cette propriété et de l'équation d'Einstein
[](#eq:einstein1) est la conservation de l'énergie, par
conséquent directement issue de propriétés géométriques:
$$\label{eq:conservation_energie_tenseur}
T^{\mu\nu}_{\ \ ;\mu}=0
$$
On voit alors que l'équation d'Einstein peut
être définie à une constante près[^3], aujourd'hui appelée constante
cosmologique, tout en satisfaisant la conservation de l'énergie. Voici
l'équation d'Einstein sous sa forme définitive {cite:p}`Einstein1917`:
$$\label{eq:einstein2}
\fbox{$ G_{\mu\nu}-\Lambda g_{\mu\nu} = -8\pi G_N T_{\mu\nu} $}
$$

Le tenseur énergie-impulsion $T^{\mu\nu}$ décrit le contenu en énergie
de l'espace-temps. En fait, il ne décrit que l'énergie et l'impulsion
associée à la matière ou à toute autre forme de champ non
gravitationnel, comme le champ électromagnétique. Pour un fluide parfait
en l'absence de gravitation, ce tenseur s'écrit sous la forme:
$$T^{\mu\nu} = p g^{\mu\nu} + (p+\rho)U^\mu U^\nu,$$ où $p$ et $\rho$
sont respectivement la pression et la densité d'énergie du fluide
(mesurables par un observateur localement dans le référentiel du
fluide), et $U^\mu$ est la valeur locale du quadri-vecteur vitesse $dx^\mu/d\tau$.

Pour un fluide statique, la normalisation de la quadri-vitesse donne:
$$
g_{\mu\nu}U^\mu U^\nu = -1 \Rightarrow U^0 = (-g^{00})^{1/2},\ U^i=0\ \mathrm{ pour\ }i=1,2,3.
$$
Le tenseur énergie-impulsion prend alors la forme simple
$$\label{eq:tmunu_fluide}
T^{\mu\nu} = \begin{pmatrix}
-\rho g^{00} & 0 & 0 & 0 \\
0 & p g^{11} & 0 & 0 \\ 
0 & 0 & p g^{22} & 0 \\ 
0 & 0 & 0 & p g^{33}  \\ 
\end{pmatrix}.
$$

La Relativité Générale en action
--------------------------------

Le principe de moindre action est un principe de base de la physique. La
dynamique d'un système peut généralement être résumée dans une intégrale
appelée action $\mathcal{S}$, qui minimisée donne les équations du
mouvement du système. La plupart des équations fondamentales de la
physique peuvent être formulées à partir du principe de moindre action.

L'intégrant correspond au Lagrangien $\mathcal{L}$, ou à la densité
Lagrangienne. C'est la quantité scalaire qui code de manière concise les
équations du mouvement du système. L'avantage d'une telle formulation en
physique est qu'elle permet de manipuler des quantités scalaires venant
de différentes théories, et de disposer de théorèmes reliant les
symétries d'un système à ses quantités conservées (théorème de Noether
{cite:t}`Noether1918`).

L'équation d'Einstein
[](#eq:einstein2) sans matière est une équation du mouvement qui
peut être formulée sous la forme d'action, l'action d'Einstein-Hilbert:
$$\label{eq:action_eh}
 \mathcal{S}_{\mathrm{EH}}= -\frac{1}{16\pi G_N} \int  d^4 x \sqrt{-g}( R - \Lambda ),$$
où $R$ est le scalaire de Ricci. Cette action contient les deux termes
scalaires les plus simples invariants selon un changement de
coordonnées, construits à partir de la métrique $g_{\mu\nu}$. L'action
pour décrire un Univers avec matière et gravitation est alors simplement
l'addition des actions de la matière $\mathcal{S}_m$ et
d'Einstein-Hilbert: $$\label{ref:action}
\mathcal{S} = \mathcal{S}_{\mathrm{EH}} + \mathcal{S}_m,\qquad \mathcal{S}_m = \int  d^4 x \sqrt{-g} \mathcal{L}_m,$$
où $\mathcal{L}_m$ est le Lagrangien de la matière (regroupant tous les
champs physiques, forces incluses, sauf la gravitation). On voit là tout
l'intérêt de l'expression des équations sous forme d'action, car pour
décrire un Univers avec un champ scalaire supplémentaire particulier ou
toute autre théorie physique additionnelle, il suffit de rajouter son
écriture sous forme d'action à l'action totale décrivant ce modèle
d'Univers. Il est donc commode en physique de partir de l'écriture
simple d'une action, puis de la minimiser pour en déduire les équations
du mouvement et la dynamique du système, i.e. l'évolution de l'Univers
et le comportement de ses différentes composantes (matière, rayonnement,
etc\...).

Appliquons cette méthode à l'action $\mathcal{S}$. Cette méthode sera
ensuite reprise dans les chapitres suivants dans le cadre d'Univers avec
différents champs scalaires. Considérons une variation infinitésimale de
la métrique $g_{\mu\nu} \rightarrow g_{\mu\nu} + \delta g_{\mu\nu}$, où
$\delta g_{\mu\nu}$ est arbitraire, mais s'annule à l'infini. On peut
alors définir le tenseur énergie-impulsion de la matière introduit plus
haut comme le résultat de la minimisation de $\mathcal{S}_m$:
$$\begin{aligned}
\delta \mathcal{S}_m & = \int d^4 x \left( \frac{1}{2} \sqrt{-g} g^{\mu\nu} \delta g_{\mu\nu} \mathcal{L}_m + \sqrt{-g} \delta \mathcal{L}_m  \right) = \frac{1}{2} \int d^4 x \sqrt{-g} T^{\mu\nu} \delta g_{\mu\nu} \\
T^{\mu\nu} & = \frac{2}{\sqrt{-g}} \frac{\delta \sqrt{-g}\mathcal{L}_m}{\delta g_{\mu\nu}} = 2 \frac{\delta \mathcal{L}_m}{\delta g_{\mu\nu}} + g^{\mu\nu} \mathcal{L}_m\label{eq:tmunu}\end{aligned}$$

À partir des équations
[](#eq:action_eh),
[](#ref:action) et
[](#eq:tmunu), on
démontre que la minimisation de l'action totale $\mathcal{S}$ redonne
l'équation d'Einstein
[](#eq:einstein2), comme étant l'équation du mouvement de la
métrique $g_{\mu\nu}$.

### Principes cosmologiques

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

### Les équations de Friedmann

Résoudre l'équation d'Einstein
[](#eq:einstein2) consiste à en trouver une métrique solution,
compte tenu de la répartition en matière supposée dans $T^{\mu\nu}$.
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


En utilisant la métrique FLRW
[](#eq:flrw),
calculons pour l'exemple la connexion affine suivante à partir de
l'équation [](#eq:connexion):
$$\begin{aligned}
\Gamma^1_{\ 01} & = \frac{1}{2} g^{1 \mu} \left( \partial_0 g_{1\mu} + \partial_1 g_{0 \mu} - \partial_\mu g_{01} \right) \\
& = \frac{1}{2} g^{1 1} \left( \partial_t g_{11} + \partial_r g_{01} - 0 \right) \text{ car }\forall \mu \neq 1, g^{1\mu}=0\text{ (voir encadré)}\\
& = \frac{1}{2} \frac{1-kr^2}{a^2} \left( \frac{2 \dot{a} a}{1-kr^2} + 0 \right) \\
& = \frac{\dot a}{a} = H.
\end{aligned}$$

Le tenseur métrique inverse est défini par:
$$g^{\mu\nu} = \eta^{\alpha\beta} \frac{\partial x'^\mu}{\partial x^\alpha} \frac{\partial x'^\nu}{\partial x^\beta}.$$
En effet, par définition on a bien: $$\begin{aligned}
g^{\nu\rho}g_{\mu\nu} & = \eta^{\alpha\beta} \frac{\partial x'^\nu}{\partial x^\alpha} \frac{\partial x'^\rho }{\partial x^\beta} \eta_{\gamma\delta} \frac{\partial x^\gamma}{\partial x'^\mu} \frac{\partial x^\delta}{\partial x'^\nu} \\
& = \delta^\delta_\alpha  \eta^{\alpha\beta} \frac{\partial x'^\rho }{\partial x^\beta} \eta_{\gamma\delta} \frac{\partial x^\gamma}{\partial x'^\mu} \text{ avec } \frac{\partial x'^\nu}{\partial x^\alpha}\frac{\partial x^\delta}{\partial x'^\nu} = \delta^\delta_\alpha \\
& = \frac{\partial x'^\rho}{\partial x^\beta}\frac{\partial x^\beta}{\partial x'^\mu} = \delta^\rho_\mu,\end{aligned}$$
où $\delta^\rho_\mu$ est le symbole de Kronecker ($\delta^\rho_\mu=1$ si
$\rho=\mu$, 0 sinon).

Pour la métrique FLRW, son inverse est simplement:
$$
g^{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & \frac{1-kr^2}{a^2(t)} & 0 & 0 \\ 
0 & 0 & \frac{1}{a^2(t)r^2}  & 0 \\ 
0 & 0 & 0 & \frac{1}{a^2(t) r^2 \sin^2 \theta}   \\ 
\end{pmatrix}.
$$

De la même manière, on obtient les autres connexions affines, puis les
tenseurs de Riemann et Ricci. Au final, le tenseur d'Einstein est
diagonal et vaut: $$\begin{aligned}
G_{00} & =  - 3 \left( \frac{\dot{a}^2}{a^2}+ \frac{k}{a^2} \right), \\
G_{ij} & = \frac{2\ddot{a}a + \dot{a}^2 + k}{a^2}g_{ij} \text{ pour } i=j\neq0.\end{aligned}$$
A partir de l'équation d'Einstein
[](#eq:einstein2) et du tenseur énergie-impulsion
[](#eq:tmunu_fluide), on obtient pour la coordonnée $00$ et pour
les coordonnées spatiales $ij$: 
$$\begin{aligned}
G_{\mu\nu}-\Lambda g_{\mu\nu} & = -8\pi G_N T_{\mu\nu} \\
\Leftrightarrow  & \left\lbrace
\begin{array}{rl}
    \text{00: } &  \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{k}{a^2} \right) = 8\pi G_N \rho + \Lambda} \\
    ij\text{: } &   \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + k}{a^2} = - 8\pi G_N p + \Lambda }
\end{array}
\right.\end{aligned}$$ 
Ce sont les deux équations d'Einstein. On les
appellera équation d'Einstein ($00$) et équation d'Einstein ($ij$) par
la suite. Elles sont plus connues sous le nom d'équation de Friedmann
lorsqu'elle sont exprimées en fonction du paramètre de Hubble
$H=\dot{a}/a$: 
$$\label{eq:friedmann}
\left\lbrace
\begin{array}{rl}
    \text{00: } & \displaystyle{H^2 = \frac{8\pi G_N \rho}{3} + \frac{\Lambda}{3} - \frac{k}{a^2}}\\
    ij\text{: } &  \displaystyle{2\dot{H} + 3H^2 = - 8\pi G_N p + \Lambda - \frac{k}{a^2}}
\end{array}
\right.$$ La première équation de Friedmann relie explicitement
l'évolution du facteur d'échelle $a(t)$ au contenu énergétique de
l'Univers. De plus, en soustrayant ces deux équations et en combinant le
résultat avec la dérivée temporelle de la première, on peut obtenir
l'équation de conservation de l'énergie que l'on obtiendrait aussi
directement en calculant $T^{\mu\nu}_{\ \ ;\mu}=0$ dans la métrique
FLRW: $$\label{eq:conservation_energie}
\dot{\rho} = -3 H(\rho + p )$$

Le tenseur énergie-impulsion inclut la matière non-relativiste et
relativiste. La matière relativiste est généralement nommée rayonnement
car aujourd'hui le rayonnement de photons du CMB est largement dominant
dans cette composante. La matière non relativiste n'exerce pas de
pression donc $p_m=0$ et: $$\label{eq:conservation_energie_matiere}
\dot{\rho}_m = -3 H\rho_m \Rightarrow \rho_m = \rho_m^0 a^{-3}.$$ Cette
dernière relation traduit bien le fait que si une boîte de côté $a$
contenant une certaine quantité de matière voit la longueur de ses côtés
doubler, alors la densité de matière est bien divisée par $2^3$. Pour le
rayonnement, $\rho_r = 3 p_r$ donc:
$$\label{eq:conservation_energie_radiation}
\dot{\rho}_r = -4 H\rho_r \Rightarrow \rho_r = \rho_r^0 a^{-4}.$$ Le
raisonnement avec une boîte cubique de côté $a$ s'applique aussi ici,
mais si toutes les longueurs doublent, alors la longueur d'onde du
rayonnement aussi donc son énergie est divisée par 2. On retrouve bien
une diminution de la densité d'énergie de rayonnement en $2^4$.

L'équation d'état $w(z)$ associée à une composante de l'Univers est
définie par le rapport de sa pression et de sa densité d'énergie
$w=p/\rho$.

-   La matière non relativiste n'exerce pas de pression sur son milieu
    extérieur d'où $p_m=0$ donc $w_m=0$.

-   La matière relativiste exerce quant à elle une pression sur son
    milieu de valeur $p_r = \rho_r / 3$ d'où $w_r=1/3$.

-   Pour la constante cosmologique, on identifie dans
    l'équation [](#eq:friedmann) une densité d'énergie
    $\rho_\Lambda = \Lambda/8\pi G_N$ et une pression
    $p_\Lambda = - \Lambda / 8\pi G_N$ d'où une équation d'état
    constante et négative $w_\Lambda = -1$.

### Le modèle $\Lambda$CDM

On peut définir une densité critique, qui correspondrait à la densité
que l'on doit avoir dans un univers homogène et isotrope en expansion de
courbure spatiale nulle (cf
équation [](#eq:friedmann)): $$\rho_c(t) = \frac{3H^2(t)}{8\pi G_N}.$$ Il
est commode de définir aussi sa valeur actuelle:
$$\rho_{c}^0 = \frac{3H^2_0}{8\pi G_N} = 1.1 \times 10^{-29} \left( \frac{H_0}{75\text{ km/s/Mpc}}\right)^2\text{ g/cm}^3 \approx 6 \text{ protons/m}^3.$$
où $H_0$ est la constante de Hubble.

Dans les équations de Friedmann
[](#eq:friedmann), il est possible d'interpréter la constante
cosmologique $\Lambda$ et la courbure $k$ en terme de densités d'énergie
au même titre que la densité d'énergie $\rho$ du tenseur
énergie-impulsion. La densité d'énergie associée à la constante
cosmologique est parfois appelée densité d'énergie noire, en raison des
étranges propriétés associées à cette dernière:
$$\rho_\Lambda(t) = \frac{\Lambda}{8\pi G_N} = \text{ constante },$$ et
celle associée à la variable $k$ est appelée densité d'énergie de
courbure: $$\rho_k(t) = - \frac{3k}{8\pi G_N a^2(t)}.$$ On voit que la
densité d'énergie associée à la constante cosmologique étant constante
dans le temps, cette dernière a un comportement bien singulier: quelque
soit la taille de l'Univers, il y a toujours autant d'énergie par unité
de volume. Elle n'est donc pas diluée comme toute énergie ordinaire
lorsque celui-ci est en expansion. De plus, grâce à la seconde équation
de Friedmann, on voit que la pression associée à la constante
cosmologique serait $p_\Lambda = - \rho_\Lambda$, soit une pression
négative! En posant $\rho_{\mathrm{tot}}=\rho + \rho_\Lambda$ (et
$p_{\mathrm{tot}}=p + p_\Lambda$) puis en combinant les deux équations
de Friedmann [](#eq:friedmann) de façon à éliminer le terme de courbure, on
obtient:
$$
2\dot{H} + 2H^2 = \frac{2\ddot{a}}{a} = -\frac{8\pi G_N}{3}\left(\rho _{\mathrm{tot}} + 3p_{\mathrm{tot}}\right).
$$
On constate que l'expansion de l'Univers s'accélère ($\ddot{a}>0$) si
$p_{\mathrm{tot}}<-\rho_{\mathrm{tot}}/3$. L'Univers étant constitué
essentiellement de matière non relativiste et de rayonnement, on a
$\rho = \rho_m + \rho_r$, et la condition précédente devient équivalente
à $\rho_\Lambda > \rho_r + \rho_m/2$. En conclusion, si la constante
cosmologique domine le contenu en énergie de l'Univers, alors elle
engendre une telle pression négative que ce dernier entre en expansion
accélérée.

On définit les paramètres de densité en normalisant les densités
d'énergie par la densité critique, soit
$$\Omega_m(t) = \frac{\rho_m(t)}{\rho_c(t)},\quad \Omega_\Lambda(t) = \frac{\Lambda}{3H^2(t)}, \quad \Omega_k(t) = -\frac{k}{a^2(t)H^2(t)}$$
$$\Omega_m^0 = \frac{\rho_m^0}{\rho_c^0},\quad \Omega_\Lambda^0 = \frac{\Lambda}{3H^2_0}, \quad \Omega_k^0 = -\frac{k}{H^2_0}.$$
La première équation de Friedmann s'écrit alors simplement avec
$\rho=\rho_m+\rho_r$:
$$1 = \Omega_m(t) + \Omega_r(t) + \Omega_\Lambda(t) + \Omega_k(t)$$
$$\label{eq:friedmann2}
\bar H^2 (t) \equiv \frac{H^2(t)}{H_0^2} = \Omega_m^0 a^{-3}(t) + \Omega_r^0 a^{-4}(t) + \Omega_\Lambda^0 +  \Omega_k^0 a^{-2}(t).$$
Ce modèle d'Univers liant la prédiction de son expansion $\bar H(z)$ à
son contenu composé d'une constante cosmologique, de matière et de
radiation, est appelé modèle $\Lambda$CDM ($\Lambda$ pour la constante
cosmologique et CDM pour *Cold Dark Matter*).

### Le décalage spectral, ou redshift

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
cosmologie. Par exemple, par un changement de variable défini par
l'équation [](#eq:redshift), la distance comobile s'écrit simplement:
$$\chi(z) = \frac{1}{a_0}\int_0^z \frac{c dz}{H(z)}$$

De plus, la première équation de Friedmann se réécrit ainsi en fonction
du décalage spectral:
$$\bar H^2 (z) = \Omega_m^0 (1+z)^3 + \Omega_r^0 (1+z)^4 + \Omega_\Lambda^0 +  \Omega_k^0 (1+z)^2$$
avec $a_0=1$.

(sec:distances)=
### Distances dans l'Univers

La distance propre est la distance que l'on pourrait mesurer
effectivement à un instant $t$ entre deux objets situés en $r_1$ et
$r_2$. Elle est donc homogène à une longueur. Sans perdre en généralité,
on peut choisir $r_1=0$ et $r_2=r$. La distance propre est alors définie
naturellement par:
$$d(t) \equiv \int_{0}^{r} \sqrt{-g_{rr}}dr' = \int_{0}^{r}\frac{a(t) dr'}{\sqrt{1-kr'^2}} = a(t)\chi(t) = a(t)\left\lbrace
\begin{array}{cl}
    \arcsin r_E & \text{ si } k=+1 \\
    r_E & \text{ si } k=0 \\
    \text{arcsh } r_E & \text{ si } k=-1 
\end{array}
\right. ,$$ et s'exprime bien en unités de longueur. A la date $t_0$
aujourd'hui, cette distance s'exprime simplement en fonction du décalage
spectral: $$d(z)=a_0\chi(z)=\int_0^z\frac{c dz}{H(z)}.$$ La notion de
distance propre est illustrée [](#fig:distances).

```{figure} ../images/distances3.png
:name: fig:distances
:align: center
:width: 100%

Distance propre entre la Terre et la Galaxie d'Andromède. (a)
Aujourd'hui, la distance mesurée entre la Terre et la Galaxie
d'Andromède est de $a_0 r = 2.5 \times 10^6$ années-lumière dans un
espace plat. (b) A une autre date $t$, cette distance évolue et vaut
$a(t) r$. (c) Distance propre dans un espace
sphérique.
```

Considérons une source située en $r_E$, émettant à l'instant $t_E$ $n_E$
photons de fréquence moyenne $\nu_E$ (se reporter encore à la
[](#fig:distances_croquis)). Sa luminosité est:
$$L_E = \frac{n_E h\nu_E}{dt_E}.$$ 
Alors le flux surfacique reçu par un
observateur est: 
$$\Phi_0 = \frac{n_0 h \nu_0}{dt_0 dS}.$$ 
La surface sur laquelle se répartit, à l'instant $t_0$, le flux émis est:
$$S = \int_0^{2\pi} \int_0^\pi \sqrt{-g} d\theta d\phi = \int_0^{2\pi} \int_0^\pi a^2(t_0)r^2(t_0)\sin^2\theta d\theta d\phi = 4 \pi a^2_0 r^2_E.$$
avec $r(t_0)=r_E$. Or à partir de l'équation
[](#eq:redshift2), on a
$\nu_E = \nu_0 a(t_0)/a(t_E) = \nu_0 (1+z)$ et $dt_E = dt_0/(1+z)$. Le
nombre de photons émis $n_E$ intercepté par la surface collectrice de
taille $dS$ est $n_0 = n_E dS/(4 \pi a^2_0 r^2_E)$, d'où le flux reçu:
$$\Phi_0 = \frac{n_0 h \nu_0}{dt_0 dS} =  \frac{h \nu_0 n_E}{dt_0 4 \pi a^2_0 r^2_E} = \frac{L_E}{4 \pi a^2_0 r^2_E(1+z)^2}.$$
Dans un espace statique et plat, la luminosité apparente d'une source au
repos à distance $d_L$ serait $L_E/4\pi d_L^2$. On peut donc définir la
distance de luminosité d'une source $d_L(z)$ par:
$$\Phi_0 = \frac{L_E}{4 \pi d_L^2(z)} \Rightarrow d_L(z) = a_0 r_E (1+z) = a_0 (1+z)\left\lbrace
\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \text{sh } \chi(z) & \text{ si } k=-1 
\end{array}
\right. .$$

Dernière distance importante en cosmologie, la distance angulaire d'un
objet $D_A(z)$. Soit un objet de taille transverse $D$ situé en
$r=r_E,t=t_E$ et observé en $r=0,t=t_0$. Dans l'espace comobile, il
serait vu sous un angle $\delta \approx D /r_E$ (avec $\delta\ll 1$). On
définit la distance angulaire comobile ou distance transverse comobile
simplement par:
$$d_A(z) = \frac{D}{\delta} = r_E = \left\lbrace\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \text{sh } \chi(z) & \text{ si } k=-1 
\end{array}
\right. .$$ Dans un espace non statique, son diamètre apparent à $t_0$
est $D'=D a_0/a_E$ et l'objet est à une distance $a_0 r_E$: il est donc
vu sous un angle $\delta' = D'/a_0 r_E$ . La distance angulaire $D_A(z)$
est la distance sous laquelle son diamètre apparent serait à nouveau $D$
et vu sous le même angle $\delta'$:
$$\delta' = \frac{D}{D_A(z)} = \frac{D'}{a_0 r_E}$$
$$\Rightarrow D_A(z)=a(t_E) r_E=\frac{a_0 r_E}{1+z} = \frac{a_0}{1+z}d_A(z)=\frac{d_L(z)}{(1+z)^2}= \frac{a_0}{1+z} \left\lbrace\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \text{sh } \chi(z) & \text{ si } k=-1 
\end{array}
\right. .$$

L'Univers aujourd'hui
---------------------

Jusqu'à présent, nous avons construit un modèle d'Univers, à partir des
principes d'équivalence, d'homogénéité et d'isotropie. Nous n'avons
jamais eu à supposer la valeur de tel ou tel paramètre, ni introduit de
mesures expérimentales. Ce modèle est-il donc en accord avec les
observations? Quelles sont les valeurs des paramètres du modèle qui
s'accordent aux mesures actuelles?

### D'un Univers statique à un Univers en expansion

A la publication de l'article d'Einstein finalisant la Relativité
Générale en 1917 {cite:p}`Einstein1917`, pour les scientifiques de l'époque
l'Univers n'était composé que de notre galaxie et probablement d'un vide
au-delà. Il était statique, immuable, éternel, autrement dit sans
histoire. La Galaxie d'Andromède était encore appelé Nébuleuse
d'Andromède et n'était alors qu'un objet diffus situé dans notre propre
galaxie. Pour satisfaire cette vision d'un Univers statique, Einstein
propose que la constante cosmologique vaille:
$$\Lambda = 4 \pi  G_N \rho.$$ En effet, reprenons le système
d'équations de
Friedmann [](#eq:friedmann) avec $\dot{a}=0$. Alors pour un Univers
composé d'étoiles de faible vitesse ($p\approx 0$), grâce à la seconde
équation on a directement $\Lambda = k/a^2$. Puis avec la première
équation, on obtient alors;
$$0 = \frac{8 \pi G_N \rho}{3} - \frac{2k}{3a^2} \Rightarrow k=+1\text{ et } \forall t, a(t)=\frac{1}{\sqrt{4 \pi  G_N \rho}},$$
d'où $\Lambda = 4 \pi  G_N \rho$ (voir
[](#fig:constante) où $\kappa=8\pi G_N$). On a donc bien une
solution pour un Univers statique, donc d'âge infini, sans frontière et
fermé puisque de géométrie sphérique, ce qui correspond à la vision de
l'Univers de l'époque.

```{figure} ../images/constante_cosmologique.png
:name: fig:constante
:align: center
:width: 100%

Introduction de la constante cosmologique dans l'article historique
{cite:t}`Einstein1917`, solution d'un Univers
statique.
```

Cependant, dans les années 1920, les frontières de l'Univers commencent
à faire débat. Certains scientifiques comme Shapley affirment que les
nébuleuses connues alors se situent dans notre galaxie, alors que
d'autres comme Curtis commencent à soutenir que certaines se situent en
dehors. La question est résolue en 1923 par l'astronome Edwin Hubble par
la découverte d'étoiles Céphéides dans la Galaxie d'Andromède. Les
Céphéides sont des étoiles variables dont la période de variation est
directement liée à leur luminosité intrinsèque. Cette relation
découverte par Henrietta Swan Leavitt permet ainsi de connaître la
distance de luminosité des nébuleuses contenant de telles étoiles, en
mesurant leur variabilité. D'un coup, des objets que l'on croyait situés
dans notre galaxie se retrouvent en dehors. Par exemple, la Galaxie
d'Andromède se retrouve propulsée à parsecs ({cite:t}`Hubble1929M31` et
[](#fig:hubble_m31)), bien au-delà des amas globulaires
gravitant autour de notre galaxie à quelques kiloparsecs de distance.


```{figure} ../images/hubble_m31_abstract.jpg
:name: fig:hubble_m31
:align: center
:width: 100%

A gauche, en-tête de l'article de Hubble sur la mesure de la distance
de la Galaxie d'Andromède (M31). A droite, plaque photographie
historique où Hubble a identifié une étoile variable dans la Galaxie
d'Andromède (indiqué par le \"N\").
```

Dans le même temps, de nombreuses mesures spectroscopiques de ces
nébuleuses ont été réalisées, entre autres par Vesto Slipher, qui en a
déduit les décalages spectraux. De plus, Friedmann montre en 1922 qu'un
Univers en expansion peut être une solution de l'équation d'Einstein. En
1929, dans un autre fameux article {cite:t}`Hubble1929`, Hubble assemble les
décalages spectraux et les distances de luminosité de 22 galaxies
([](#fig:hubble)). Le résultat est sans appel: plus les galaxies
sont lointaines, plus elle s'éloignent vite (la vitesse radiale de
l'objet pouvant être déduite du décalage spectral par la formule de
Doppler). Hubble établit une loi de proportionnalité entre ces deux
quantités, appelée loi de Hubble: 
$$c z = H_0 d_L(t_0),$$ 
avec $H_0$ la constante de Hubble, mesurée alors à 530 km/s/Mpc. Un tel comportement
ne peut s'expliquer que d'une seule manière: l'espace qui nous sépare
des galaxies est en expansion. Cependant, il faut noter que dès 1927,
dans un article publié en français dans une revue belge, Georges
Lemaître compare la théorie d'un univers en expansion aux mesures de
distances et redshifts de 42 galaxies et parvient deux ans plus tôt aux
mêmes conclusions que Hubble {cite:p}`Lemaitre1927` avec
$H_0=625 km/s/Mpc$. Mais c'est Hubble qui est passé à la
postérité, la version traduite en anglais de l'article de Lemaître
{cite:p}`Lemaitre1931` omettant curieusement l'ensemble de son travail
d'analyse des données et le calcul de $H_0$
{cite:p}`VanDenBergh2011; Block2012`.

```{figure} ../images/hubble_diagram.png
:name: fig:hubble
:align: center
:width: 70%

Premier \"diagramme de Hubble\", établi dans {cite:t}`Hubble1929`, montrant une relation de proportionnalité entre distance
de luminosité d'une galaxie et sa vitesse radiale.
```

### Le scénario du Big Bang

Si l'Univers grandit aujourd'hui, alors hier il était plus petit et plus
dense, donc plus chaud. Si on poursuit le raisonnement, alors compte
tenu de la constante de Hubble mesurée aujourd'hui et dans le modèle
standard de la cosmologie, il y a 13.8 milliards d'années environ
l'Univers était infiniment petit, infiniment chaud et infiniment dense.
Un tel scénario pour la naissance de l'Univers est appelé Big Bang.

A partir du moment où l'Univers est raisonnablement plus froid
($10^{-11}$ secondes après cet \"instant zéro\"), les lois de la
physique connues peuvent s'appliquer, et des prédictions
observationnelles peuvent être faites si l'Univers est bien né d'un Big
Bang. En plus du constat que l'Univers est en expansion, deux autres
preuves observationnelles liées à cette phase chaude de l'Univers sont
venues soutenir cette hypothèse.

ans après le Big Bang, l'Univers est constitué d'un plasma chaud et
dense d'électrons libres, de noyaux atomiques, et de photons issus du
rayonnement de corps noir du plasma. Les photons interagissent alors
fortement avec les électrons libres par diffusion Thomson, et leur libre
parcours moyen est très court, de l'ordre de la distance moyenne entre
quelques particules. L'Univers en expansion se refroidissant, il existe
une température en dessous de laquelle les électrons se combinent aux
noyaux pour former les atomes. L'interaction entre les photons et les
électrons cesse alors, et le rayonnement de corps noir du plasma
primordial est libre de se propager: c'est le rayonnement de fond diffus
cosmologique, émis ans après le Big Bang. Il a été prédit en 1948 par
Ralph Alpher, Robert Herman {cite:p}`Alpher1948` et George Gamow {cite:p}`Gamow1948`,
et découvert fortuitement par Arno Penzias et Robert Wilson en 1964
{cite:p}`Penzias1965a; Penzias1965b`. Ce rayonnement dit fossile a été
refroidi par l'expansion et est aujourd'hui très bien observé, à une
température $T_{\mathrm{CMB}}=2.725 K$ {cite:p}`Mather1999`. C'est
le meilleur rayonnement de corps noir jamais détecté (voir
[](#fig:cmb_cn)).


```{figure} ../images/cmb_cn.jpg
:name: fig:cmb_cn
:align: center
:width: 70%

Intensité du rayonnement du fond diffus cosmologique en fonction de la
fréquence. Un excellent accord est trouvé entre un modèle de corps noir
à 2.725K et les différentes mesures expérimentales, en particulier celles
venant du satellite COBE {cite:p}`Mather1999`.
```


La seconde preuve expérimentale vient de la mesure de l'abondance des
éléments chimiques dans l'Univers. Dans le scénario du Big Bang,
l'Univers n'a été assez chaud que pendant 200 secondes pour forger des
noyaux chimiques à partir de la soupe primordiale de protons et de
neutrons. Après, l'Univers est devenu trop froid pour permettre la
fusion des nucléons. Dans ce scénario, on peut donc prédire la quantité
de noyaux formés à la fin de ce court intervalle de temps: 75% environ
sont des noyaux d'hydrogène (donc des protons n'ayant pas eu le temps de
réagir), 25% des noyaux d'hélium 4 (le second élément stable le plus
léger), puis des traces de noyaux de lithium. Le reste des éléments sera
forgé plus tard dans la nucléosynthèse stellaire.

Le scénario du Big Bang est donc appuyé par de solides preuves
expérimentales, qu'un modèle d'Univers stationnaire aurait du mal à
expliquer. Le modèle $\Lambda$CDM avec $\dot{a}\neq0$ peut donc
maintenant être confronté aux données expérimentales actuelles, afin
d'en déterminer la valeur des paramètres.

### La partie sombre du modèle standard

Après la découverte de l'expansion de l'Univers par Hubble, la constante
cosmologique d'Einstein pour modéliser un Univers statique a été
simplement mise de côté. Le défi des astrophysiciens étaient alors de
mesurer précisément cette expansion, à travers le constante de Hubble
$H_0$ et le paramètre de décélération $q_0$. Ce dernier a été introduit
pour décrire la relation entre distance de luminosité et redshift avec
l'idée que la vitesse d'expansion de l'Univers devait forcément
décroître au cours du temps du fait des interactions gravitationnelles
attractives entre les galaxies:
$$d_L(t_0) = \frac{c}{H_0}\left(z + \frac{1}{2}(1-q_0)^2 z^2 + \ldots \right), \qquad q_0 = \left[\frac{a \ddot{a}}{\dot{a}^2}\right]_{t=0}.$$
Pour mesurer cette décélération, l'enjeu est de mesurer la quantité de
matière dans l'Univers à travers le paramètre de densité de matière
$\Omega_m^0$. Différentes sondes sont utilisées à cette fin. En
particulier, en 1990 l'exploitation des données du relevé de galaxies
APM suggère que ce paramètre vaut au plus 0.3 {cite:p}`Maddox1990`. Puis en
1993, la mesure de la fraction de baryons dans les amas de galaxies
associée à la mesure de la densité de baryons venant de la
nucléosynthèse primordiale amène à la même conclusion {cite:p}`White1993`.
Cependant, des considérations théoriques liées au problème de
l'inflation (voir encadré en fin de chapitre) suggèrent que l'Univers
doit être plat, donc que la densité de matière doit être égale à la
densité critique ($\Omega_m^0 = 1$). Certaines mesures vont dans ce sens
et argumente que l'Univers a bien la densité critique
{cite:p}`Loh1986; Nusser1993`. En 1997, les cosmologistes considéraient donc
deux types de modèles pour expliquer l'Univers actuel: un univers
sous-critique avec une densité de matière faible ou un univers dominé
par la matière à la densité critique[^5]. Pour concilier univers
critique et $\Omega_m^0 \approx 0.3$, il commence alors à être suggéré
de réintroduire la constante cosmologique {cite:p}`Efstathiou1990`.

En 1998, deux équipes (Supernova Cosmology Project (SCP) menée par Saul
Perlmutter et High-z Supernova Search Team menée par Brian Schmidt) se
lancent dans l'observation des supernovæ de type Ia afin de mesurer
précisément le paramètre $q_0$. A l'aide de cette nouvelle sonde, la
relation distance-luminosité obtenue est très précise et permet
d'accéder à l'évolution de l'Univers à des redshifts lointains et jamais
explorés ($z\approx 0.7$). Le résultat déduit de ces données est majeur:
l'expansion de l'Univers ne décélère pas comme attendu mais accélère.
Non seulement la densité de matière de l'Univers n'est pas égale à la
densité critique, mais il faut rajouter un ingrédient aux modèles
cosmologiques d'alors afin d'expliquer cette accélération de
l'expansion. C'est le grand retour de la constante cosmologique. Aucun
des modèles considérés à l'époque ne permet d'expliquer ces
observations, mais les deux équipes constatent qu'un modèle d'univers
contenant de la matière et une constante cosmologique le permet
(références {cite:t}`Riess1998; Perlmutter1999` et voir la
[](#fig:snIa) tirée de la référence {cite:t}`Perlmutter2003`). Les
données venant des supernovæ de type Ia combinées à des mesures
ultérieures venant du fond diffus cosmologique apportent en plus de cela
une autre information : l'Univers est plat et
$\Omega_\Lambda^0\approx0.7$. Non seulement la constante cosmologique
n'est pas nulle, mais elle occupe pas moins de 70% du contenu en énergie
de l'Univers pour contrer la gravitation aux échelles cosmologiques et
étirer l'espace-temps de plus en plus vite.


```{figure} ../images/perlmutter.jpg
:name: fig:snIa
:align: center
:width: 100%

Gauche: les mesures des distances de luminosité de 42 supernovae
lointaines de type Ia montrent un bon accord avec un modèle $\Lambda$CDM
avec $\Omega_\Lambda^0\approx0.7$ et $\Omega_m^0\approx0.3$ (ligne
bleue). Droite: contours de probabilités des paramètres du modèle
$\Lambda$CDM pour différentes sondes; on voit que sur la ligne
$\Omega_\Lambda^0=0$, fond diffus cosmologique et amas étaient en
désaccord; l'apport des supernovæ a permis de redécouvrir la constante
cosmologique. (Figures tirées de la référence
{cite:t}`Perlmutter2003`)
```

Sauf qu'autour de la constante cosmologique se nichent de nombreux
problèmes, en particulier si on l'interprète au niveau microscopique
comme une manifestation de l'énergie du vide. Les estimations de cette
énergie sont $10^{120}$ fois supérieures à la valeur observée pour
$\rho_\Lambda$ {cite:p}`Weinberg1989`. On doit donc supposer qu'il existe un
mécanisme dans la nature qui annule l'énergie du vide, ou plutôt qui en
laisse $10^{-120}$ fois moins *exactement*[^6]. Cet ajustement fin des
paramètres cosmologiques pour ne laisser précisément que ce qu'il faut
d'énergie du vide pour que l'Univers ait pu vivre 13.8 milliards
d'années est troublant. C'est le problème du \"fine tuning\". Le modèle
standard de la cosmologie est donc obligé de s'accommoder d'une forme
d'énergie inconnue et possiblement contenue dans une constante
$\Lambda$, dorénavant appelée énergie noire.

Les déboires du modèle standard de la cosmologie ne s'arrêtent pas là.
En 1933, en étudiant l'amas de Coma, l'astrophysicien Fred Zwicky montre
que la masse déduite du mouvement des sept galaxies qui le composent est
400 fois plus grande que la masse déduite du comptage des objets
lumineux. Cette mesure est répétée en 1936 sur l'amas de la Vierge et
donne cette fois un facteur 200. Ces mesures toutefois un peu imprécises
tombent dans l'oubli jusque dans les années 1970, lorsque l'astronome
Vera Rubin constate que la vitesse de rotation des étoiles de la Galaxie
d'Andromède est bien plus élevée que ne le suggère sa masse lumineuse
observée {cite:p}`Rubin1970`. Le constat est vite répété sur de nombreuses
galaxies: une partie de la matière constituant la galaxie est donc une
matière sombre, échappant alors à toute détection.

Pour la constante cosmologique, on a $w_\Lambda = -1$. Au cas où
l'énergie noire ne serait pas suffisamment bien décrite par la simple
constante cosmologique $\Lambda$, on utilise le modèle FWCDM qui décrit
un Univers plat (F pour \"flat\") d'équation d'état $w_\Lambda$ pour
l'énergie noire constante mais a priori différente de $-1$ (pour le W)
et de matière non relativiste (CDM pour \"cold dark matter\").

Pour l'énergie noire ainsi paramétrée, l'équation de conservation de
l'énergie [](#eq:conservation_energie) donne:
$$
\dot{\rho}_{\Lambda} = -3\frac{\dot{a}}{a}\left(1+w_\Lambda\right)\rho_{\Lambda} \Leftrightarrow  \frac{\rho_{\Lambda}(z)}{\rho_{\Lambda}^0} =  \left(\frac{a}{a_0}\right)^{-3(1+w_\Lambda)} = (1+z)^{-3(1+w_\Lambda)}.$$
L'équation de Friedmann pour cette modélisation est alors:
$$\bar H^2 (z)  = \Omega_m^0 (1+z)^3 + \Omega_r^0 (1+z)^4 + \Omega_\Lambda^0 (1+z)^{-3(1+w_\Lambda)}.$$

La recherche de cette matière noire s'est alors concentrée sur la
recherche de matière ordinaire émettant ailleurs que dans le domaine
visible, ou même simplement obscure. Avec le satellite ROSAT dans les
années 1990, des cartographies aux rayons X du gaz chaud dans les amas
de galaxies (n'émettant pas dans le visible) mettent en évidence que
celui-ci constitue bien une part importante de la matière jusqu'alors
invisible des amas. Mais cette part n'est pas assez importante pour
expliquer la dynamique de l'amas. Au contraire, la valeur mesurée de la
température du gaz implique que l'amas est bien plus massif que l'on ne
le croît pour pouvoir accélérer les particules du gaz aux températures
constatées {cite:p}`David1994`. Les recherches s'orientent alors vers la
recherche de petits objets compacts sombres tels que les naines brunes.
Les programmes MACHO et EROS n'en détectent que trop peu: à peine 10% de
ce qu'il faudrait pour expliquer la totalité de la masse invisible de
notre galaxie {cite:p}`Alcock1998`.

Le coup de grâce intervient par la mesure des abondances relatives des
éléments légers dans l'Univers et l'étude du fond diffus cosmologique,
où il apparaît quel les baryons issus de la nucléosynthèse (hydrogène et
hélium) ne représentent en fait que 5% de la densité d'énergie totale,
alors que 32% de matière sont requis. En effet, les fluctuations de
température du fond diffus cosmologique sont seulement de l'ordre de
$\Delta T/T \approx 10^{-5}$, ce qui est insuffisant pour expliquer
qu'elles aient pu être les germes des grandes structures à elles seules.
Dans ces conditions, ces dernières n'auraient pas pu se former aussi
vite sans un coup de pouce gravitationnel de la matière noire. Dans le
modèle standard de la cosmologie, on suppose donc que la matière noire
existe depuis les origines de l'Univers et a eu le temps pendant ans
avant le découplage de former des puits gravitationnels et de s'y
agglomérer. En effet, n'étant pas couplées (ou trop peu) à la radiation
par nature, les fluctuations de densité de la matière noire primordiale
n'oscillent pas mais s'effondrent gravitationnellement sans frein de la
part du rayonnement. Ces puits gravitationnels préformés au découplage
ont pu constituer les véritables germes des grandes structures de
l'Univers, dans lesquels la matière enfin libérée du rayonnement a pu
s'accumuler rapidement et former les grandes structures de l'Univers.
Une part importante de la matière serait donc non-baryonique, et noire.

```{figure} ../images/bulletcluster.jpg
:name: fig:bullet
:align: center
:width: 70%

Observation de l'amas du Boulet dans le visible, aux rayons X (rouge)
et évaluation de la répartition de la masse dans l'amas par lentille
gravitationnelle (bleu). On observe que l'essentiel de la masse ne se
trouve pas là où se concentre le gaz chaud émettant dans les rayons X et
qui constitue l'essentiel de la matière baryonique de l'amas: dans la
collision des deux amas, les composantes baryonique et non baryonique se
sont dissociées.
```

Un autre indice de l'existence de la matière noire provient de l'étude
de l'amas du Boulet dans la constellation de la Carène {cite:p}`Clowe2006`. Cet
amas est le fruit de la collision entre deux amas de galaxies. On a déjà
mentionné que l'essentiel de la masse des amas est constitué de gaz
chaud ionisé. Celui-ci est bien détecté aux rayons X, où deux lobes de
gaz issus des deux amas sont détectés (en rouge sur
la [](#fig:bullet)). Ces deux masses de gaz ont bien entendu
interagi durant leur collision, et se sont freinées mutuellement. En
revanche, lorsque l'on s'intéresse à la répartition de la masse mesurée
par effet de lentille gravitationnelle, on s'aperçoit que l'essentiel de
la masse est concentré dans deux lobes bien distincts (en bleu) qui ne
se superposent pas au gaz chaud émettant dans les rayons X et qui
constitue l'essentiel de la masse visible. Dans la collision, les gaz
chauds des deux amas se sont freinés mutuellement, tandis qu'une matière
sombre a elle continué sur son élan et s'est dissociée de l'essentiel de
la matière baryonique. Ceci constitue un indice observationnel que le
mystère de la matière noire réside bien dans l'existence d'une matière
non baryonique et non dans une modification des lois de la gravité
(comme dans la théorie MOND).

S'il existe des indices expérimentaux qui accréditent l'existence d'une
matière noire non baryonique, celle-ci n'a été perçue que par ses effets
gravitationnels. Aucune détection d'une particule de matière noire n'a
été rapportée à ce jour, ni de ses éventuels produits de désintégration
(rayons gamma notamment).

```{figure} ../images/planck_pie.jpg
:name: fig:planck_pie
:align: center
:width: 80%

Mesures des paramètres de densité de la matière ordinaire, de la
matière noire et de l'énergie noire. Les mesures du satellite Planck
ayant été publiées en milieu de ma thèse, il est aussi intéressant
d'avoir en tête les valeurs précédentes mesurées par le satellite
WMAP.
```


```{figure} ../images/omega_lcdm.png
:name: fig:omega_lcdm
:align: center
:width: 80%

Évolution des paramètres de densité $\Omega_i(z)$ en fonction du
décalage spectral $z$ pour un Univers $\Lambda$CDM en utilisant les valeurs des
paramètres mesurés par le satellite Planck.
```

Aujourd'hui, la meilleure mesure des proportions relatives de matière
ordinaire, de matière noire et d'énergie noire a été réalisée par le
satellite Planck en étudiant le fond diffus cosmologique
(référence {cite:t}`PlanckCollaboration2013XVI` et
[](#fig:planck_pie)). Au cours de l'histoire de l'Univers, trois
périodes se succèdent
([](#fig:omega_lcdm)): dans l'Univers primordial la radiation
domine pour laisser la place à la matière peu après la recombinaison à
$z\approx1090$, et enfin à l'énergie noire aujourd'hui. 95% de l'Univers
est donc en fait constitué de formes d'énergie et de matière encore
inconnues. Le modèle standard de la cosmologie est certes en très bon
accord avec les observations actuelles, mais au prix de l'introduction
de ces deux composantes obscures. Ceci met aussi à mal le modèle
standard de la physique des particules, qui ne contient aucune forme de
matière non baryonique qui pourrait expliquer la nature de la matière
noire. Sur cette question, l'infiniment grand rejoint l'infiniment
petit.

:::{note} Problème de la platitude
Aujourd'hui, on mesure que notre
espace-temps est plat. Regardons l'impact de ce constat sur l'évolution
de la densité d'énergie totale au cours de l'histoire de l'Univers avec
la première équation de Friedmann:
$$H^2(a) = \frac{8\pi G_N\rho_{\mathrm{tot}}(t)}{3} - \frac{k}{a^2} \Leftrightarrow \left(\frac{1}{\Omega_{\mathrm{tot}}(t)} -1 \right) \rho_{\mathrm{tot}}(t) a^2 = \frac{-3k}{8\pi G_N}=\rho_k^0 \approx 0$$
Le membre de droite de l'équation est *constant dans le temps* et mesuré
quasi nul aujourd'hui. Or dans le passé le terme
$\rho_{\mathrm{tot}}(t) a^2$ était $10^{60}$ fois plus grand. Par
conséquent, pour compenser on doit avoir $\Omega_{\mathrm{tot}}(t)=1$
dans le passé avec une précision d'environ de $10^{-60}$, ce qui
implique des conditions initiales très finement ajustées, donc non
naturelles.
:::

:::{note} Problème de l'horizon
Le diamètre de l'Univers observable est de:
$$d(\infty) = \int_0^\infty\frac{c dz}{H(z)}=\frac{2c}{H_0}=2\times13.8\text{ milliards d'années-lumière}$$
dans un espace plat. Cela correspond à peu près au diamètre de la sphère
d'émission du rayonnement fossile. Or sur cette sphère, chaque point de
l'espace n'a vécu que ans, donc n'a pu interagir qu'avec d'autres points
situés au maximum à années-lumière. Par conséquent, deux points
d'émission du rayonnement de fond diffus cosmologique diamétralement
opposés n'ont pu interagir, or ils ont la même température à $10^{-5}$
degrés près. A sa naissance, l'Univers est-il né avec une température
strictement égale en tout point de l'espace (peu naturel), ou y a-t-il
eu un mécanisme dans les tous premiers instants qui a permis
d'homogénéiser cette température?
:::

:::{note} La solution de l'inflation
La période d'inflation, toute première
étape après la naissance de l'Univers, aurait vu la taille de l'Univers
grandir de façon exponentielle pendant un court intervalle de temps.
Ainsi les deux régions diamétralement opposées du ciel aurait en fait
été en contact thermique avant que l'inflation ne les sépare. De plus,
celle-ci aurait dilué toute courbure initiale pour former un espace
plat, et magnifié les fluctuations quantiques primordiales pour générer
les fluctuations thermiques $\delta \theta / \theta \approx 10^{-5}$ du
fond diffus cosmologique.
:::

[^1]: A travers cette définition, on a choisi une métrique de signature
    $(-,+,+,+)$ que nous garderons par la suite.

[^2]: Par la suite, l'indice $0$ des tenseurs correspondra donc à la
    coordonnée temporelle, tandis que les indices suivants
    correspondront aux coordonnées spatiales.

[^3]: Car on a aussi $g^{\mu\nu}_{\ \ ;\mu}=0$.

[^4]: 1 parsec (pc) = 3.262 années-lumière = 3.086e16 m. 100 $\approx$
    années-lumière.

[^5]: Ces considérations historiques sont développées dans la référence
    {cite:t}`Astier2012`.

[^6]: Des calculs plus précis tenant compte des problèmes de
    renormalisation montrent que le désaccord peut être ramener de 120 à
    une cinquantaine d'ordres de grandeur, ce qui reste énorme
    {cite:p}`Martin2012`.
