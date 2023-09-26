---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---

Introduction succincte à la Relativité Générale
=============================================

De Newton à la Relativité Générale
----------------------------------

La Relativité Générale est la théorie de la gravitation à la base de la
cosmologie moderne. Elle donne une explication géométrique à la force
gravitationnelle introduite par Newton trois siècles auparavant. Dans
cette théorie, une chute n'est plus due à un vecteur force
malheureusement orienté vers un sol dur, mais à la déformation de
l'espace-temps engendrée par la Terre. Formulée ainsi, la Relativité
Générale semble bien compliquée pour peu de choses. Mais les principes
généraux à la base de cette théorie et la richesse de ses implications
(dont la théorie newtonienne) en font la théorie phare pour décrire la
gravitation. Le long de cette section, nous allons introduire pas à pas
plusieurs concepts de la Relativité Générale tels que la dérivée
covariante et le tenseur de Riemann, pour aboutir à l'équation
d'Einstein de la Relativité Générale, base de la cosmologie moderne.
Cette introduction est largement inspirée de {cite:t}`Weinberg1972` et
{cite:t}`Gourgoulhon2013`. 

### Le Principe d'Équivalence

Dans le principe fondamental de la dynamique énoncé par Newton, pourquoi
la masse intervenant dans le terme d'inertie est-elle rigoureusement la
même que celle intervenant dans la gravitation newtonienne ? Cette
coïncidence troublante singularise la gravitation par rapport aux autres
interactions, et suggère qu'elle n'est pas une propriété des corps
eux-mêmes mais de l'espace dans lequel ils se meuvent. Considérons une
masse ponctuelle de masse $m$ soumise à un champ gravitationnel externe
uniforme et constant $\vec g$ et à aucune autre force. Alors le principe
fondamental de la dynamique appliqué dans un référentiel galiléen à cet
objet nous permet de prédire sa position $\vec x$ à un instant $t$ par une équation différentielle à intégrer :
$$m\frac{\dd^2\vec x}{\dd t^2} = m\vec g$$ 
Plaçons nous dans le référentiel
(non galiléen) de l'objet par la transformation de coordonnées suivante :
$$\vec x' = \vec x - \frac{1}{2}\vec g t^2, \qquad t'=t$$ 
Alors dans ce référentiel la force gravitationnelle est comme \"absorbée\" par le
terme inertiel :
$$m\frac{\dd^2\vec x}{\dd t^2} = m\vec g \Leftrightarrow m\frac{\dd ^2\vec x'}{\dd t'^2} = 0.$$
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

Appliquons le Principe d'Équivalence à un objet massif en chute libre. Pour cet
objet, il existe donc localement un système de coordonnées *particulier*
$x^\mu$ tel que l'équation de son mouvement s'écrive de la même manière
que si le référentiel était non accéléré et sans gravitation :
\begin{equation}\label{eq:eqm1}
\frac{\dd^2 x^\mu}{\dd\tau^2}=0,
\end{equation}
avec $\dd\tau$ le temps propre[^1] :
$$\label{eq:proper-time}
\dd\tau^2 \equiv -\eta_{\mu\nu} \dd x^\mu \dd x^\nu.
$$ 
Le tenseur $\eta_{\mu\nu}$ est la métrique de Minkowski utilisée en Relativité Restreinte. D'après le
Principe d'Équivalence, cette équation est aussi valable dans un certain
voisinage de l'objet en question. Il existe donc un autre système de
coordonnées plus général $x'^\mu$ dans lequel réécrire cette équation.
Cherchons la forme qu'elle prendrait pour ces coordonnées $x'^\mu$ :
$$0=\frac{\dd^2 x^\mu}{\dd\tau^2}=\frac{d}{\dd\tau}\left(\frac{\partial x^\mu}{\partial x'^\nu} \frac{\dd x'^\nu}{\dd\tau}\right) = \frac{\partial x^\mu}{\partial x'^\nu} \frac{\dd^2x'^\nu}{\dd\tau^2} + \frac{\partial^2 x^\mu}{\partial x'^\nu \partial x'^\rho}\frac{\dd x'^\nu}{\dd\tau}\frac{\dd x'^\rho}{\dd\tau}.$$
Après multiplication par $\partial x'^\nu/\partial x^\mu$, on obtient la
nouvelle équation du mouvement dans le système de coordonnées $x'^\mu$ :
$$\label{eq:eqm2}
\frac{\dd^2x'^\nu}{\dd\tau^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x'^\mu}{\dd\tau}\frac{\dd x'^\rho}{\dd\tau}=0,
$$
où $\Gamma^\nu_{\ \mu\rho}$ est la connexion affine définie par:
$$\Gamma^\nu_{\ \mu\rho} \equiv \frac{\partial x'^\nu}{\partial x^\lambda}\frac{\partial^2 x^\lambda}{\partial x'^\mu \partial x'^\rho}.$$
Le temps propre se réécrit :
$$\dd\tau^2=-\eta_{\mu\nu} \dd x^\mu \dd x^\nu = -g_{\mu\nu} \dd x'^\mu \dd x'^\nu$$
ce qui définit ainsi le tenseur métrique $g_{\mu\nu}$ :
$$g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial x^\alpha}{\partial x'^\mu} \frac{\partial x^\beta}{\partial x'^\nu}$$
$g_{\mu\nu}$ décrit la géométrie de l'espace-temps dans le nouveau
système de coordonnées $x'^\mu$ et remplace la métrique cartésienne
$\eta_{\mu\nu}$. On pourrait par la suite montrer que
$\Gamma^\nu_{\ \mu\rho}$ peut ne s'écrire qu'à l'aide d'un seul système
de coordonnées et du tenseur métrique : 
$$\label{eq:connexion}
\Gamma^\nu_{\ \mu\rho} = \frac{1}{2}g^{\lambda\nu}\left( \frac{\partial g_{\lambda\rho}}{\partial x'^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x'^\rho}  - \frac{\partial g_{\mu\rho}}{\partial x'^\lambda} \right)
$$

Pour une particule sans masse, comme le photon ou le neutrino, le temps propre défini par l'équation [](#eq:proper-time) s'annule. A 
la place de $\tau$ on peut alors utiliser la coordonnée $s = x^0$ pour paramétrer la trajectoire de la courbe et par un raisonnement 
similaire on aboutit à cette équation du mouvement :
$$\label{eq:eqm3}
\frac{\dd^2x'^\nu}{\dd s^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x'^\mu}{\dd s}\frac{\dd x'^\rho}{\dd s}=0.
$$
Si elles sont présentes, les forces autres que la gravitation s'appliquant à la particule test peuvent s'ajouter au membre de droite 
de l'équation [](#eq:eqm3).

:::{note} Dérivée covariante

La connexion affine $\Gamma^\nu_{\ \mu\rho}$ intervient par ailleurs
dans la définition de la dérivée covariante $V^\nu{}_{;\mu}$ d'un
vecteur $V^\nu$ par rapport à la coordonnée $x'^\mu$ :
$$
V^\nu{}_{;\mu} \equiv \partial_\mu V^\nu + \Gamma^\nu_{\ \mu\rho}V^\rho
$$
Cette définition de la dérivée en Relativité Générale exprime
correctement la variation d'un vecteur le long d'une coordonnée dans un
espace non plat. Elle se transforme de la même manière qu'un vecteur par
un changement de coordonnées, contrairement à la dérivée usuelle: le
vecteur variation est donc correctement défini. Pour illustrer toute sa
profondeur, voici la définition de la dérivée covariante $DV^\mu/D\tau$
non pas par rapport à une coordonnée, mais le long d'une courbe
quelconque paramétrée par le temps propre $\tau$ (invariant par
changement de coordonnées) :
$$\frac{DV^\mu}{D\tau} \equiv \frac{\dd V^\mu}{\dd\tau} + \Gamma^\mu_{\ \nu\lambda}\frac{\dd x^\lambda}{\dd\tau} V^\nu.$$
L'équation du mouvement [](#eq:eqm2) s'écrit alors très simplement
$$\frac{DU^\mu}{D\tau}=0,$$ 
avec $U^\mu$ le vecteur vitesse $\dd x^\mu/\dd\tau$. Cette équation ainsi écrite rappelle fortement
l'équation du mouvement initiale [](#eq:eqm1). La notion de dérivée covariante est donc bien appropriée aux calculs de
Relativité Générale et remplace bien la dérivée usuelle dans ce cadre. 
Notons que pour un vecteur covariant, la dérivée covariante s'écrit :
$$\label{eq:dcov-cov}
\frac{DV_\mu}{D\tau} \equiv \frac{\dd V_\mu}{\dd\tau} - \Gamma^\nu_{\ \mu\lambda}\frac{\dd x^\lambda}{\dd\tau} V_\nu.
$$
:::


### Vers l'équation d'Einstein

Armés de ces outils, allons maintenant vers une dérivation simple de
l'équation d'Einstein qui résume la gravitation à une déformation de
l'espace-temps par la matière. Commençons par nous intéresser à une
particule massive se déplaçant lentement dans un champ gravitationnel
faible, constant mais quelconque cette fois. L'hypothèse de vitesse
faible nous permet de négliger $\dd\vec x/\dd\tau$ devant $\dd t/\dd\tau$.
D'après le Principe d'Équivalence, on a vu qu'il existe un système de
coordonnées inertielles $\left(ct,\vec x'\right)$[^2] tel que l'équation
du mouvement [](#eq:eqm2) soit aussi valable dans cette nouvelle situation
avec champ gravitationnel. On a alors au premier ordre dans un champ de
gravité faible et quasi-stationnaire :
$$
\frac{\dd^2x'^\mu}{\dd\tau^2} + \Gamma^\mu_{\ 00}\left(\frac{\dd t}{\dd\tau}\right)^2=0, \qquad \Gamma^\mu_{\ 00} \approx -\frac{1}{2}g^{\mu\nu}\frac{\partial g_{00}}{\partial x'^\nu}.
$$

Dans l'hypothèse d'un champ gravitationnel faible, on peut adopter une
métrique presque cartésienne :
$$g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad \vert h_{\mu\nu}\vert\ll 1,$$
et on obtient au premier ordre : 
$$\left\lbrace
\begin{array}{rl}
    \mu=1,2,3\ : & \displaystyle{\frac{\dd^2\vec x'}{\dd\tau^2} = \frac{1}{2}\left(\frac{\dd t}{\dd\tau}\right)^2\vec{\nabla} h_{00} } \\
    \mu=0\ : &  \displaystyle{\frac{\dd^2t}{\dd\tau^2} = 0.}
\end{array}
\right.$$ 
D'après la deuxième équation on en déduit que $\dd t/\dd\tau$ est
une constante et donc la première équation donne :
$$\label{eq:vers_einstein}
\frac{\dd^2\vec x'}{\dd t^2} = \frac{1}{2}\vec{\nabla} h_{00}.
$$ 
Or on sait que dans la limite newtonienne on a :
$$\frac{\dd^2\vec x'}{\dd t^2} = -\vec{\nabla} \phi, \qquad \phi=-\frac{G_N M}{r},$$
avec $\phi$ le potentiel gravitationnel engendré par une masse $M$ à une
distance $r$ ($G_N$ étant la constante de Newton). En comparant avec
[](#eq:vers_einstein), on a $h_{00}=-2\phi+\text{constante}$. Or
le système de coordonnées choisi doit être cartésien à l'infini
(hypothèse de faible perturbation), donc $h_{00}=-2\phi$ et :
$$\label{eq:g00}
g_{00}=-(1+2\phi),
$$ 
L'élément $g_{00}$ correspondant à la composante temporelle
de la métrique, le battement des horloges dépend par conséquent de
l'intensité du champ gravitationnel. Ceci correspond à l'effet Einstein,
la seule conséquence de la Relativité Générale aujourd'hui utilisée
technologiquement (dans le GPS, voir [](#fig:effet_einstein)).


```{figure} ../images/effet_eintein.svg
:name: fig:effet_einstein
:align: center
:width: 90%

Illustration de l'effet Einstein. Un photon tombant dans un puits
gravitationnel gagne de l'énergie donc sa fréquence augmente. De façon
équivalente, on peut dire que les horloges dans un champ gravitationnel
retardent par rapport à des horloges identiques situées en dehors. Les
récepteurs GPS doivent prendre en compte cet effet pour en déduire leur
position par rapport aux satellites.
```

Cet exercice sur une particule ponctuelle nous apprend que le champ
gravitationnel est finalement contenu dans la métrique, et que cette
métrique dépend donc de la présence de matière. Il est donc possible
d'imaginer une généralisation de ce constat. Le potentiel newtonien est
déterminé par l'équation de Poisson $\nabla^2\phi = 4\pi G_N \rho$, où
$\rho$ est la densité volumique de masse. Cette dernière correspond à la densité
d'énergie du tenseur énergie-impulsion de la matière $T_{00}$ (voir
encadré: $T_{00} = -\rho g_{00} \approx \rho$), donc avec l'équation
[](#eq:g00) on peut obtenir  :
$$
\nabla^2 g_{00}=-8\pi G_N T_{00}.
$$ 
On peut alors imaginer qu'il existe un tenseur $G_{\mu\nu}$ combinant des dérivées premières et
secondes de la métrique $g_{\mu\nu}$ généralisant cette dernière
équation à toutes les coordonnées tel que 
$$\label{eq:einstein1}
G_{\mu\nu}=-8\pi G_N T_{\mu\nu}.
$$ 
Cette dernière équation correspond à une première version de l'équation d'Einstein. Ce raisonnement ne nous a
permis que d'intuiter sa forme, mais une autre démonstration plus
rigoureuse permet d'obtenir l'expression du tenseur d'Einstein
$G_{\mu\nu}$ : 
$$
G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R
$$
avec $R_{\mu\nu}$ le tenseur de Ricci et $R$ la courbure scalaire (trace
du tenseur de Ricci $R^\mu_\mu$), eux-mêmes obtenus par le tenseur de
Riemann $R^\mu_{\ \nu\alpha\beta}$ : 
$$
\begin{aligned}
R^\mu_{\ \nu\alpha\beta} & = -\partial_\alpha \Gamma^\mu_{\ \nu\beta} +  \partial_\beta \Gamma^\mu_{\ \nu\alpha} - \Gamma^\mu_{\ \alpha\sigma}\Gamma^\sigma_{\ \nu\beta} + \Gamma^\mu_{\ \beta\sigma}\Gamma^\sigma_{\ \nu\alpha} \\
R_{\mu\nu} & =R^\alpha_{\ \mu\alpha\nu}.
\end{aligned}
$$

$G_{\mu\nu}$ apparaît être de divergence nulle car :
$$G^{\mu\nu}_{\ \ ;\mu}=0$ (identité de Bianchi).$$

:::{important}

L'identité de Bianchi et l'équation d'Einstein
[](#eq:einstein1) impose la conservation de l'énergie, par
conséquent directement issue de propriétés géométriques :
$$\label{eq:conservation_energie_tenseur}
T^{\mu\nu}_{\ \ ;\mu}=0
$$
:::

Par l'identité de Bianchi, on voit aussi que l'équation d'Einstein peut
être définie à une constante près[^3] tout en gardant la conservation de l'énergie. Cette constante est 
aujourd'hui appelée constante cosmologique. Voici l'équation d'Einstein sous sa forme définitive {cite:p}`Einstein1917` :
$$\label{eq:einstein2}
\fbox{$ G_{\mu\nu}-\Lambda g_{\mu\nu} = -8\pi G_N T_{\mu\nu} $}
$$



Cosmological facts
===================


Cosmology is the study of the evolution of the Universe on large scales. Here, large means on scales much larger than the typical distances between galaxies, that is tens of Mpc. But why would such a science even be needed? When did it become clear that observations do not agree with an infinite, homogeneous and stationary Universe? Both from the observational and the theoretical point of view, one can say that cosmology was born in the beginning of the $20^{\mathrm{th}}$ century. But interestingly, unanswered questions (whose answers lie in modern cosmology) appeared much earlier than that.

### Olbers' paradox

Olbers' paradox can be stated quite simply: "Why is the night sky dark?". The question is actually much older than Olbers formulation (1823). Kepler (for example) was wondering the same thing as early as 1610. The paradox arises when considering a homogeneous stationary and infinite universe. Then the content of the universe can be described with a constant number density $n$ of sources of light of luminosity $L$. The flux received by an observer from a source of light located at a distance $r$ is then ${L \over 4 \pi r^2}$. Summing over all sources, the total flux is:

\begin{equation}\label{eq:olbers}
F=\int_0^\infty {n\,L \over 4 \pi r^2} 4 \pi r^2 dr = + \infty.
\end{equation}


Allowing for the fact that stars are not point-like and can screen other stars further along the line of sight, we get a night sky that should be as bright as the typical surface of a star. Neither Kepler nor Olbers gave a satisfactory answer to the paradox. Kepler assumed that there were no
stars beyond a certain distance, which conflicts with homogeneity but was reasonable at the time, and Olbers assumed that light was absorbed along the way by interstellar gas, which would induce an increase in the temperature of the gas and break
the assumption that the Universe is stationary. The point is that Olbers paradox cannot be resolved in a homogeneous, stationary and infinite universe. Modern cosmology solves it by
getting rid of stationary Universe assumption. Let's also mention that until only 20 years ago another solution was to postulate a universe 
with a fractal content (thus getting rid of homogeneity without introducing a center). While this is compatible with observations up to scales of a few tens of Mpc, recent galaxy surveys show that homogeneity is reached on $> 100$ Mpc scales.

### Hubble-Lemaître law

First Lemaître in 1926, in a little known paper written in French, then Edwin Hubble in 1929, found a correlation between the distance of nearby galaxies and their radial velocities. The distances were estimated using Cepheid stars when the image resolution was good enough that individual star could be identified. Indeed,
Cepheid stars have an average intrinsic luminosity that can be measured from the period of its fluctuation. Measuring the received flux then yields the distance (assuming negligible absorption along the line of sight). In other cases, much more approximate estimators of the distance were used. Although no reference is given in the original paper, the radial velocities were most likely obtained through measurements of the Doppler shift of spectral lines by V. M. Slipher. Lemaître and Hubble's insight was to recognize that the receding velocities (corrected from the Sun's own velocity) were proportional to the distance of the galaxies:

$$ v=H_0 d $$

$H_0$ is called the Hubble constant. Hubble's original estimation of $H_0$ was wildly wrong (more than $7$ times the current value), mainly because of the strongly underestimated distances of the most distant galaxies in his sample. Nevertheless, this was the first observational hint that the universe as a whole is expanding  homogeneously. Modern cosmology still probes this relation, using different but equivalent quantities, applied to the case type Ia supernovae whose distances can be
accurately computed (they have a well known peak luminosity). The original and modern versions of the velocity-distance relation are shown in fig. \ref{hubble}.

See equation [](#eq:olbers).

See Hubble's paper [](10.1007/s00016-020-00263-z)



```{figure} fig/hubble.png
:name: fig:hubble
:alt: hubble
:align: center


The original velocity-distance diagram by Hubble (1929). On the right, a modern version (credit: Ned Wright, compiled with data from Betoule et al. 2014) of the diagram, The black dots area binned representation of a sample of 740 supernovae of type Ia.
```


See Figure [](#fig:hubble).


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
