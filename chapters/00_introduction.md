---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---

Introduction succincte à la Relativité Générale
=============================================

Rappels de Relativité Restreinte
--------------------------------

Le principe sous-jacent à la théorie de la Relativité Restreinte est que les lois de la physique doivent être invariantes par changement de 
système de coordonnées d'espace-temps. Dans le cas spécial de la théorie de l'électromagnétisme de Maxwell, il apparaît une vitesse invariante par changement
de système de coordonnées. Cette vitesse s'identifie à la célérité de la lumière, vitesse maximale pouvant être atteinte par une particule de masse nulle. Si 
la théorie électromagnétique n'avait pas été écrite en 1905, un argument aurait aussi pu être qu'il doit exister une vitesse maximale dans l'Univers si on pense qu'aucun 
transport d'information ne peut être instantané. A ce moment là, la vitesse pivot de la théorie de la Relativité Restreinte aurait été la vitesse de l'interaction
qui se propage le plus rapidement. Ce qui dans notre Univers revient à l'interaction électromagnétique {cite:p}`landau1989théorie`.

Soit un système de coordonnées $x^\alpha$, où la coordonnée $\alpha=0$ correspond au temps $ct$ et les coordonnées $\alpha=1,2,3$ correspondent
aux coordonnées cartésiennes $x^1,x^2, x^3$.  Dans ce cours, nous emploierons les lettres grecques pour les composantes allant de 0 à 3 et les 
lettres latines pour les composantes spatiales allant de 1 à 3. Pour passer à un autre système de coordonnées $x'^\alpha$, on introduit la transformation de 
Lorentz $\Lambda^\alpha_\beta$ définie par :
```{math}
:label: eq:boost

x'^{\alpha} = \Lambda^\alpha_{\;\beta} x^\alpha + a^\alpha,
```
où $a^\alpha$ est une simple translation temporelle et spatiale. On définit la métrique de Minkowski :
```{math}
:label: eq:minkowski

\eta_{\alpha\beta} = \begin{pmatrix}
-1 & 0& 0& 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix}

```
de telle sorte qu'en coordonnées cartésiennes on puisse définir l'intervalle espace-temps ainsi entre deux coordonnées spatio-temporelles proches :
$$ \dd s^2 = - c^2 \dd t^2 + \dd \vec x^2 = \eta_{\alpha}\dd x^\alpha \dd x^\beta $$
Pour assurer que $c$ est invariant par changement de système de coordonnées, la transformation de Lorentz doit assurer la conservation de l'intervalle espace-temps[^consc] donc :
$$\label{eq:dscons}
\dd s'^2 =  \eta_{\alpha\beta}\dd x'^\alpha \dd x'^\beta = \eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta} \eta_{\alpha\beta} \dd x'^\gamma \dd x'^\delta = \eta_{\gamma\delta} $$

De la symétrie [](#eq:dscons} on peut démontrer que la transformation de Lorentz entre deux référentiels dont l'un se déplace à la vitesse $\vec v = v \vec e_{1}$ par rapport à l'autre doit s'écrire :
```{math}
:label: eq:lorentz

\Lambda^{\alpha}_{\;\beta} = \begin{pmatrix}
\gamma & -\beta\gamma & 0& 0 \\
-\beta\gamma & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix},\quad \beta = \frac{v}{c},\quad \gamma = \frac{1}{\sqrt{1 - \beta^2}}

```
Si on inclus des rotations de l'espace, avec un référentiel se déplaçant à la vitesse $\vec v$ constante par rapport à un autre référentiel,
le tenseur $\Lambda^\alpha_{\;\beta}$ s'écrit :
```{math}
:label: eq:lorentz2

\Lambda^0_{\;0} = \gamma,\quad \Lambda^i_{\;0} = \gamma v_i / c,\quad \Lambda^0_{\;j} = \gamma v_j / c,\quad \Lambda^i_{\;j} = \delta_{ij} + v_i v_j \frac{\gamma - 1}{v^2}
```

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
$\eta_{\mu\nu}$. Le tenseur métrique inverse est défini par:
$$g^{\mu\nu} = \eta^{\alpha\beta} \frac{\partial x'^\mu}{\partial x^\alpha} \frac{\partial x'^\nu}{\partial x^\beta}.$$
En effet, par définition on a bien: 
$$\begin{aligned}
g^{\nu\rho}g_{\mu\nu} & = \eta^{\alpha\beta} \frac{\partial x'^\nu}{\partial x^\alpha} \frac{\partial x'^\rho }{\partial x^\beta} \eta_{\gamma\delta} \frac{\partial x^\gamma}{\partial x'^\mu} \frac{\partial x^\delta}{\partial x'^\nu} \\
& = \delta^\delta_\alpha  \eta^{\alpha\beta} \frac{\partial x'^\rho }{\partial x^\beta} \eta_{\gamma\delta} \frac{\partial x^\gamma}{\partial x'^\mu} \text{ avec } \frac{\partial x'^\nu}{\partial x^\alpha}\frac{\partial x^\delta}{\partial x'^\nu} = \delta^\delta_\alpha \\
& = \frac{\partial x'^\rho}{\partial x^\beta}\frac{\partial x^\beta}{\partial x'^\mu} = \delta^\rho_\mu,\end{aligned}$$
où $\delta^\rho_\mu$ est le symbole de Kronecker ($\delta^\rho_\mu=1$ si $\rho=\mu$, 0 sinon).
On pourrait par la suite montrer que  $\Gamma^\nu_{\ \mu\rho}$ peut ne s'écrire qu'à l'aide d'un seul système
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
faible nous permet de négliger $\dd\vec x/\dd\tau$ devant $c\dd t/\dd\tau$.
D'après le Principe d'Équivalence, on a vu qu'il existe un système de
coordonnées inertielles $\left(ct,\vec x'\right)$[^2] tel que l'équation
du mouvement [](#eq:eqm2) soit aussi valable dans cette nouvelle situation
avec champ gravitationnel. On a alors au premier ordre dans un champ de
gravité faible et quasi-stationnaire :
$$
\frac{\dd^2x'^\mu}{\dd\tau^2} + \Gamma^\mu_{\ 00}\left(c\frac{\dd t}{\dd\tau}\right)^2=0, \qquad \Gamma^\mu_{\ 00} \approx -\frac{1}{2}g^{\mu\nu}\frac{\partial g_{00}}{\partial x'^\nu}.
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
\frac{\dd^2\vec x'}{\dd t^2} = \frac{1}{2}c^2\vec{\nabla} h_{00}.
$$ 
Or on sait que dans la limite newtonienne on a :
$$\frac{\dd^2\vec x'}{\dd t^2} = -\vec{\nabla} \phi, \qquad \phi=-\frac{G_N M}{r},$$
avec $\phi$ le potentiel gravitationnel engendré par une masse $M$ à une
distance $r$ ($G_N$ étant la constante de Newton). En comparant avec
[](#eq:vers_einstein), on a $h_{00}=-2\phi/c^2+\text{constante}$. Or
le système de coordonnées choisi doit être cartésien à l'infini
(hypothèse de faible perturbation), donc $h_{00}=-2\phi/c^2$ et :
$$\label{eq:g00}
g_{00}=-\left(1+\frac{2\phi}{c^2}\right),
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
d'énergie du tenseur énergie-impulsion de la matière $T_{00}$: $T_{00} = \rho c^2$ (voir chapitre [](./02_friedmann_equations.md)), donc avec l'équation
[](#eq:g00) on peut obtenir :
$$
\nabla^2 g_{00}=-\frac{8\pi G_N}{c^4} T_{00}.
$$ 
On peut alors imaginer qu'il existe un tenseur $G_{\mu\nu}$ combinant des dérivées premières et
secondes de la métrique $g_{\mu\nu}$ généralisant cette dernière
équation à toutes les coordonnées tel que 
$$\label{eq:einstein1}
G_{\mu\nu}=-\frac{8\pi G_N}{c^4} T_{\mu\nu}.
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
$$G^{\mu\nu}_{\;\;\;;\mu}=0\quad\text{(identité de Bianchi)}.$$

:::{important}

L'identité de Bianchi et l'équation d'Einstein
[](#eq:einstein1) impose la conservation de l'énergie, par
conséquent directement issue de propriétés géométriques :
$$\label{eq:conservation_energie_tenseur}
T^{\mu\nu}_{\;\;\;;\mu}=0
$$
:::

Par l'identité de Bianchi, on voit aussi que l'équation d'Einstein peut
être définie à une constante près[^3] tout en gardant la conservation de l'énergie. Cette constante est 
aujourd'hui appelée constante cosmologique. Voici l'équation d'Einstein sous sa forme définitive {cite:p}`Einstein1917` :
$$\label{eq:einstein2}
\fbox{$ G_{\mu\nu}-\Lambda g_{\mu\nu} = -\frac{8\pi G_N}{c^4} T_{\mu\nu} $}
$$



[^consc]: On doit conserver $\vert \dd \vec x' / \dd t'\vert = c$ pour la propagation d'un rayon lumineux donc $\dd s^2 = 0$.

[^1]: A travers cette définition, on a choisi une métrique de signature
    $(-,+,+,+)$ que nous garderons par la suite.

[^2]: Par la suite, l'indice $0$ des tenseurs correspondra donc à la
    coordonnée temporelle, tandis que les indices suivants
    correspondront aux coordonnées spatiales.

[^3]: Car on a aussi $g^{\mu\nu}_{\;\;;\mu}=0$.

[^4]: 1 parsec (pc) = 3.262 années-lumière = 3.086e16 m. 100 $\approx$
    années-lumière.

[^5]: Ces considérations historiques sont développées dans la référence
    {cite:t}`Astier2012`.

[^6]: Des calculs plus précis tenant compte des problèmes de
    renormalisation montrent que le désaccord peut être ramener de 120 à
    une cinquantaine d'ordres de grandeur, ce qui reste énorme
    {cite:p}`Martin2012`.

