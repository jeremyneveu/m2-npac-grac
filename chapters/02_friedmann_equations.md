Friedmann equations
===================


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




Les équations de Friedmann
---------------------------

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



Les paramètres cosmologiques
___________________________________



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



Paramètre de décélération
-------------------------



Modélisations de l'énergie noire
-------------------------------
