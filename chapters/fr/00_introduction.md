---
short_title: Relativité Générale
authors:
  - jneveu
keywords: special relativity, general relativity, metric
---

Introduction succincte à la Relativité Générale
=============================================

Rappels de Relativité Restreinte
--------------------------------

:::{important} Principe de Relativité Restreinte

Les lois de la physique sont identiques dans tous les référentiel galiléens. 
:::

Si une loi physique semble vraie dans un référentiel inertiel, alors elle doit rester vraie dans un autre référentiel galiléen. C'est par exemple le cas de la seconde loi de Newton, mais imposer cela à la théorie de l'électromagnétisme a posé un sérieux problème, en remettant en cause la composition galiléenne des vitesses.

Dans le cas spécial de la théorie de l'électromagnétisme de Maxwell, il apparaît une vitesse invariante par changement de système de coordonnées: cette vitesse s'identifie à la célérité de la lumière. Comme la lumière est véhiculée par le photon, particule de masse nulle, c'est aussi la vitesse maximale pouvant être atteinte dans notre Univers. Si la théorie électromagnétique n'avait pas été écrite en 1905, un argument aurait aussi pu être qu'il doit exister une vitesse maximale dans l'Univers si on pense qu'aucun transport d'information ne peut être instantané. A ce moment là, cette vitesse limite doit être la même dans tous les référentiels inertiels et la célérité pivot de la théorie de la Relativité Restreinte aurait été la vitesse de l'interaction qui se propage le plus rapidement. Ce qui dans notre Univers revient à l'interaction électromagnétique {cite:p}`landau1989theory`. Dans les deux approches, le principe de relativité restreinte impose qu'il existe une vitesse maximum $c$ invariante par changement de système de coordonnées. *Si l'électromagnétisme est vérifiée dans un référentiel galiléen, quelles sont les transformations de coordonnées spatio-temporelles pouvant laisser cette célérité invariante?*

Soit un quadri-vecteur de coordonnées $x^\alpha$, où la composante $\alpha=0$ correspond au temps[^2] $ct$ (avec $c$ la fameuse célérité maximale et $t$ le temps) et les composantes $\alpha=1,2,3$ correspondent aux coordonnées cartésiennes $x^1,x^2, x^3$. Dans ce cours, nous emploierons les lettres grecques pour les composantes allant de 0 à 3 et les lettres latines pour les composantes spatiales allant de 1 à 3. Pour passer à un autre système de coordonnées $x'^\alpha$, on introduit la transformation de Lorentz $\Lambda^\alpha_{\;\beta}$ ainsi :
\begin{equation}\label{eq:boost}
x'^{\alpha} = \Lambda^\alpha_{\;\beta} x^\beta + a^\alpha,
\end{equation}
où $a^\alpha$ est une simple translation temporelle et spatiale. On définit la métrique de Minkowski :
\begin{equation}\label{eq:minkowski}
\eta_{\alpha\beta} = \begin{pmatrix}
-1 & 0& 0& 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix}
\end{equation}
de telle sorte qu'en coordonnées cartésiennes on puisse définir l'intervalle espace-temps ainsi entre deux coordonnées spatio-temporelles proches :
$$ \dd s^2 = - c^2 \dd t^2 + \dd \vec x^2 = \eta_{\alpha\beta}\dd x^\alpha \dd x^\beta $$
Pour assurer que la vitesse de la lumière est invariante par changement de système de coordonnées $x'^{\alpha}$, on doit conserver $\vert \dd \vec x' / \dd t'\vert = c$ pour la propagation d'un rayon lumineux donc $\dd s'^2=\dd s^2 = 0$. La transformation de Lorentz doit donc assurer la conservation de l'intervalle espace-temps:
$$
\dd s'^2 =  \eta_{\alpha\beta}\dd x'^\alpha \dd x'^\beta = \eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta}  \dd x'^\gamma \dd x'^\delta = \eta_{\gamma\delta} \dd x^\gamma \dd x^\beta = \dd s^2
$$
D'où la relation de fermeture:
$$
\label{eq:dscons}
\eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta} =  \eta_{\gamma\delta}
$$

A partir de la relation constitutive [](#eq:dscons), on peut démontrer les transformations de Lorentz forment un groupe défini par $\Lambda^{0}_{\;0}\geqslant 1$ and $\mathrm{det}\;\Lambda=+1$. Quelques calculs plus tard (voir {cite:t}`raimond` par exemple), on peut montrer que la transformation de Lorentz entre deux référentiels dont l'un se déplace à la vitesse $\vec v = v \vec e_{1}$ s'écrit de façon unique :
\begin{equation}
\label{eq:lorentz}
\Lambda^{\alpha}_{\;\beta} = 
\begin{pmatrix}
\gamma & -\beta \gamma & 0 & 0 \\
-\beta \gamma & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 
\end{pmatrix},
\quad \beta = \frac{v}{c},\quad \gamma = \frac{1}{\sqrt{1 - \beta^2}}
\end{equation}

Si on inclut des rotations de l'espace, avec un référentiel se déplaçant à la vitesse $\vec v$ constante par rapport à un autre référentiel, les composantes du tenseur $\Lambda^\alpha_{\;\beta}$ s'écrivent finalement :
\begin{equation}\label{eq:lorentz2}
\Lambda^0_{\;0} = \gamma,\quad \Lambda^i_{\;0} = -\gamma v_i / c,\quad \Lambda^0_{\;j} = -\gamma v_j / c,\quad \Lambda^i_{\;j} = \delta_{ij} +  (\gamma - 1)  \frac{v_i v_j}{v^2}
\end{equation}

De Newton à la Relativité Générale
----------------------------------

La Relativité Générale est la théorie de la gravitation à la base de la cosmologie moderne. Elle donne une explication géométrique à la force gravitationnelle introduite par Newton trois siècles auparavant. Dans cette théorie, tomber par terre n'est plus dû à un vecteur force malheureusement orienté vers le sol, mais à la déformation de l'espace-temps provoquée par la Terre. Formulée ainsi, la Relativité Générale semble bien compliquée pour peu de choses. Mais les principes généraux à la base de cette théorie et la richesse de ses implications (dont la théorie newtonienne) en font la théorie phare pour décrire la gravitation. Le long de cette section, nous allons introduire pas à pas plusieurs concepts de la Relativité Générale tels que l'équation des géodésiques, la métrique et la dérivée covariante, pour aboutir à l'équation d'Einstein de la Relativité Générale, base de la cosmologie moderne. Cette introduction est largement inspirée de {cite:t}`Weinberg1972` et {cite:t}`Gourgoulhon2013`. 

### Le Principe d'Équivalence

Dans le principe fondamental de la dynamique énoncé par Newton, pourquoi la masse intervenant dans le terme d'inertie est-elle rigoureusement la même que celle intervenant dans la gravitation newtonienne ? Cette égalité troublante entre masse inertielle et masse gravitationnelle, validée par des siècles d'expérimentations (pendules de Newton, balance d'Eötvös, etc.) singularise la gravitation par rapport aux autres interactions, comme la force de Coulomb qui dépend de la charge électrique donc des corps considérés. Cela suggère que le gravitation n'est pas une propriété des corps eux-mêmes mais de l'espace dans lequel ils se meuvent. 

Considérons une masse ponctuelle de masse $m$ soumise à un champ gravitationnel externe uniforme et constant $\vec g$ et à aucune autre force. Alors le principe fondamental de la dynamique appliqué dans un référentiel galiléen à cet objet nous permet de prédire sa position $\vec x$ à un instant $t$ par la résolution de l'équation différentielle :
$$m\frac{\dd^2\vec x}{\dd t^2} = m\vec g$$ 
Plaçons nous dans le référentiel (non galiléen) de l'objet par la transformation de coordonnées suivante :
$$
\vec x' = \vec x - \frac{1}{2}\vec g t^2, \qquad t'=t$$ 
Alors dans ce référentiel la force gravitationnelle est comme \"absorbée\" par le terme inertiel :
$$m\frac{\dd^2\vec x}{\dd t^2} = m\vec g \Leftrightarrow m\frac{\dd ^2\vec x'}{\dd t'^2} = 0.$$
Les lois de la physique apparaissent donc identiques pour un observateur lié à un référentiel galiléen considérant que l'objet subit une force de gravité et pour un observateur lié à un référentiel uniformément accéléré et considérant que l'objet ne subit pas de force gravitationnelle. La force de gravité ressentie par une masse ponctuelle est donc équivalente au choix d'un référentiel uniformément accéléré par rapport à un référentiel galiléen, au moins localement dans une région où $\vec g$ est quasi-constant et pendant une durée d'expérience où $\vec g$ est quasi-stationnaire. Le Principe d'Équivalence formulé par Einstein prend acte d'éqiuvalence entre gravitation et accélération due à l'égalité des masses inertielle et gravitationnelle, du moins pour des champs champs gravitationnels qui varient faiblement dans le temps et l'espace.

:::{important} Le Principe d'Équivalence

*A chaque point de l'espace-temps dans un champ gravitationnel arbitraire il est possible de choisir un système local de coordonnées inertielles tel que, dans une région suffisamment petite autour du point en question, toutes les lois de la nature prennent la même forme que dans un système de coordonnées cartésien non accéléré et sans gravitation* {cite:p}`Weinberg1972`. 
:::

C'est donc une généralisation du principe de relativité restreinte à tous les référentiels, en présence de gravitation ou non. Ce principe est vérifié expérimentalement avec une très bonne précision, notamment par le *Lunar Laser Ranging* {cite:p}`Williams2004`.

### Équations du mouvement

Appliquons le Principe d'Équivalence au problème d'un objet massif en chute libre. Pour cet objet, il existe donc localement un système de coordonnées *particulier* tel que l'équation de sa trajectoire $x'^\mu$ s'écrive de la même manière que si le référentiel était non accéléré et sans gravitation :
\begin{equation}\label{eq:eqm1}
\frac{\dd^2 x'^\mu}{\dd\tau^2}=0,
\end{equation}
avec $\dd\tau$ le temps propre[^1] :
$$
\label{eq:proper-time}
\dd \tau^2 \equiv -\eta_{\mu\nu} \dd x'^\mu \dd x'^\nu.
$$ 
Le paramètre $\tau$ va nous permettre de paramétrer la courbe $x'^\mu(\tau)$, tel une abscisse curviligne. Dans cette équation il ne joue que le rôle d'une étiquette pour paramétrer les positions successives de l'objet, mais il a l'immense avantage d'être invariant de Lorentz et d'être le temps mesuré par l'observateur dans le référentiel de la particule.

D'après le Principe d'Équivalence, cette équation est aussi valable dans un certain voisinage de l'objet en question avec un autre choix de coordonnées spatio-temporelles. Il existe donc un autre système de coordonnées arbitraire dans lequel on a le droit de réécrire l'équation de sa trajectoire $x^\mu$. Cherchons la forme qu'elle prendrait pour ces coordonnées $x^\mu$ :
$$
0=\frac{\dd^2 x'^\mu}{\dd\tau^2}=\frac{\dd}{\dd\tau}\left(\frac{\partial x'^\mu}{\partial x^\nu} \frac{\dd x^\nu}{\dd\tau}\right) = \frac{\partial x'^\mu}{\partial x^\nu} \frac{\dd^2 x^\nu}{\dd\tau^2} + \frac{\partial^2 x'^\mu}{\partial x^\nu \partial x^\rho}\frac{\dd x^\nu}{\dd\tau}\frac{\dd x^\rho}{\dd\tau}.$$
Après multiplication par $\partial x^\gamma/\partial x'^\mu$, on obtient[^inv] la nouvelle équation du mouvement :
$$
\label{eq:eqm2}
\frac{\dd^2x^\nu}{\dd\tau^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd\tau}\frac{\dd x^\rho}{\dd\tau}=0,
$$
où $\Gamma^\nu_{\ \mu\rho}$ est la *connexion affine* définie par:
$$\Gamma^\nu_{\ \mu\rho} \equiv \frac{\partial x^\nu}{\partial x'^\lambda}\frac{\partial^2 x'^\lambda}{\partial x^\mu \partial x^\rho}.$$
Le temps propre se réécrit:
$$
\dd \tau^2=-\eta_{\mu\nu} \dd x'^\mu \dd x'^\nu = -g_{\mu\nu} \dd x^\mu \dd x^\nu
$$
ce qui définit ainsi le tenseur métrique $g_{\mu\nu}$:
$$
\boxed{g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial x'^\alpha}{\partial x^\mu} \frac{\partial x'^\beta}{\partial x^\nu}}
$$
Le tenseur $g_{\mu\nu}$ décrit la géométrie de l'espace-temps dans le nouveau système de coordonnées $x^\mu$ et remplace la métrique cartésienne $\eta_{\mu\nu}$. C'est l'objet fondamental de la Relativité Générale car il permet de décrire les distances parcourues dans un espace-temps non euclidien (courbe).

:::{tip} Le tenseur métrique dans des cas simples

* Soit un espace euclidien 2D de métrique $\eta_{\alpha\beta} = \text{diag}(1, 1)$ de coordonnées $\vec X=(x,y)$. On réalise une rotation de l'espace d'un angle $\theta$, passant aux coordonnées $\vec X'=(x',y')$ par :
\begin{equation*}
\left\lbrace\begin{array}{ll}
x' &= x\cos \theta + y \sin \theta \\
y' &= y\cos \theta - x \sin\theta
\end{array}
\right. \Rightarrow g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial X'^\alpha}{\partial X^\mu} \frac{\partial X'^\beta}{\partial X^\nu}
\end{equation*}
Calculons $g_{11}$ pour l'exemple :
\begin{equation*}
g_{11} = \eta_{\alpha\beta} \frac{\partial X'^\alpha}{\partial X^1} \frac{\partial X'^\beta}{\partial X^1} = \left(\frac{\partial x'}{\partial x}\right)^2 +  \left(\frac{\partial y'}{\partial x}\right)^2 = \cos^2 \theta + \sin^2 \theta = 1
\end{equation*}
Après avoir calculer les autres termes, on a :
\begin{equation*}
g_{\mu\nu} = 
\begin{pmatrix}
1 & 0 \\
0& 1
\end{pmatrix}
\end{equation*}
donc l'espace reste euclidien après rotation. De façon équivalente on aurait pu obtenir la métrique $g_{\mu\nu}$ est étudiant la conservation d'un élément de longueur par rotation :
\begin{equation*}
\dd \vec l^2 = \dd x^2 + \dd y^2 = \cdots = (\dd x')^2 + (\dd y')^2.
\end{equation*}

* Soit un espace sphérique 2D de rayon $a$. Une position sur la sphère est donnée par deux angles $\vec \xi = (\theta, \phi)$. Un vecteur élémentaire $\dd \vec l$ sur la sphère a pour longueur :
\begin{equation*}
\dd \vec l^2 = a^2\dd \theta^2 + a^2 \sin^2 \theta \dd \phi^2 = g_{ij} \dd \xi^i \dd \xi^j
\end{equation*}

```{figure} ../../images/sphere_gmunu


```

D'où la métrique sur cet espace courbe :
\begin{equation*}
g_{\mu\nu} = \begin{pmatrix}
a^2 & 0 \\
0& a^2\sin^2\theta
\end{pmatrix}
\end{equation*} 
dont la courbure est la moitié du scalaire de Ricci (voir <wiki:Scalar_curvature>) et vaut $1/a^2 > 0$ comme attendu pour une sphère. 

* Soit un espace-temps euclidien 2D de métrique $\eta_{\alpha\beta} = \text{diag}(1, 1, 1)$ de coordonnées $\vec X=(ct, x,y)$. On réalise une translation galiléenne de l'espace par une vitesse constante $\vec V=V\vec e_x$, passant aux coordonnées $\vec X'=(ct', x',y')$ par :
\begin{equation*}
\left\lbrace\begin{array}{ll}
ct' & = ct \\
x' &= x + Vt \\
y' &= y
\end{array}
\right. 
\Rightarrow g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial X'^\alpha}{\partial X^\mu} \frac{\partial X'^\beta}{\partial X^\nu} \approx 
\begin{pmatrix}
1 & V/c & 0 \\
V/c & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
\end{equation*}



:::




:::{note} Métrique inverse
:class: dropdown

Le tenseur métrique inverse est défini par:
$$
g^{\mu\nu} = \eta^{\alpha\beta} \frac{\partial x^\mu}{\partial x'^\alpha} \frac{\partial x^\nu}{\partial x'^\beta}.$$
En effet, par définition on a bien: 
$$
\begin{aligned}
g^{\nu\rho}g_{\mu\nu} & = \eta^{\alpha\beta} \frac{\partial x^\nu}{\partial x'^\alpha} \frac{\partial x^\rho }{\partial x'^\beta} 
\eta_{\gamma\delta} \frac{\partial x'^\gamma}{\partial x^\mu} \frac{\partial x'^\delta}{\partial x^\nu} \\
& = \delta^\delta_\alpha  \eta^{\alpha\beta} \frac{\partial x^\rho }{\partial x'^\beta} \eta_{\gamma\delta} 
\frac{\partial x'^\gamma}{\partial x^\mu}
\text{ avec } \frac{\partial x^\nu}{\partial x'^\alpha}\frac{\partial x'^\delta}{\partial x^\nu} = \delta^\delta_\alpha \\
& = \frac{\partial x^\rho}{\partial x'^\beta}\frac{\partial x'^\beta}{\partial x^\mu} 
= \delta^\rho_\mu,\end{aligned}$$
où $\delta^\rho_\mu$ est le symbole de Kronecker ($\delta^\rho_\mu=1$ si $\rho=\mu$, 0 sinon). 
:::

On pourrait par la suite montrer que  $\Gamma^\nu_{\ \mu\rho}$ peut ne s'écrire qu'à l'aide d'un seul système de coordonnées et du tenseur métrique : 
$$
\label{eq:connexion}
\Gamma^\nu_{\ \mu\rho} = \frac{1}{2}g^{\lambda\nu}\left( \frac{\partial g_{\lambda\rho}}{\partial x^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x^\rho}  - \frac{\partial g_{\mu\rho}}{\partial x^\lambda} \right)
$$

Pour une particule sans masse, comme le photon ou le neutrino, le temps propre défini par l'équation [](#eq:proper-time) est nul. A la place de $\tau$ on peut alors utiliser une autre abscisse curviligne, telle la coordonnée $\lambda = x^0$ pour paramétrer la trajectoire de la courbe. Par un raisonnement similaire on aboutit à cette équation du mouvement :
$$
\label{eq:eqm3}
\frac{\dd^2x^\nu}{\dd \lambda^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd \lambda}\frac{\dd x^\rho}{\dd \lambda}=0.
$$
Si elles sont présentes, les forces autres que la gravitation s'appliquant à la particule test peuvent s'ajouter au membre de droite de l'équation [](#eq:eqm3) :
$$\label{eq:eqm4}
\boxed{\frac{\dd^2x^\nu}{\dd \lambda^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd \lambda}\frac{\dd x^\rho}{\dd \lambda}=\frac{f^\mu}{m}}
$$
avec $m$ la masse de l'objet et $f^\mu$ le vecteur contravariant des forces non gravitationnelles s'appliquant à une particule massive[^2prime]. La bonne écriture du principe fondamental de la dynamique selon le Principe d'Equivalence est donc l'équation [](#eq:eqm4), car on peut montrer que cette dernière est bien invariante par une transformation locale de système de coordonnées (démonstration {cite:t}`Weinberg1972`[p. 102]). 

### Dérivée covariante

La connexion affine $\Gamma^\nu_{\ \mu\rho}$ intervient par ailleurs dans la définition de la dérivée covariante $V^\nu{}_{;\mu}$ d'un vecteur $V^\nu$ par rapport à la coordonnée $x'^\mu$ :
$$
V^\nu{}_{;\mu} \equiv \partial_\mu V^\nu + \Gamma^\nu_{\ \mu\rho}V^\rho.
$$
Le premier terme correspond à la variation ordinaire d'un vecteur si on le déplace dans son voisinage. Le second terme prend en compte les changements du systèmes de coordonnées lui aussi déplacé, car le symbole de Christoffel décrit les changements des vecteurs de base du référentiel.

:::{figure} ../../images/covariant_derivative.svg

Illustration de la variation d'un vecteur $V^\mu$ (cyan) dans le voisinage d'une base $(e_\mu, e_\nu)$ d'un espace courbe. Suite à un déplacement dans son voisinage (ici le long de $e_\mu$), le vecteur change de taille (premier terme de la dérivée covariante) et la base qui définit ses projections donc ces coordonnées change également. La dérivée covariante calcule la variation des composantes du vecteur $V^\mu$ due à ces deux changements.
::: 

Cette définition de la dérivée en Relativité Générale exprime correctement la variation d'un vecteur le long d'une coordonnée dans un espace courbe. Ce vecteur variation se transforme de la même manière qu'un vecteur contravariant par un changement de coordonnées (contrairement à la dérivée usuelle): le vecteur variation $V^\nu{}_{;\mu}$ est donc correctement défini pour tout système de coordonnées. 

Pour illustrer toute sa profondeur, voici la définition de la dérivée covariante $DV^\mu/D\tau$ non pas par rapport à une coordonnée, mais le long d'une courbe quelconque paramétrée par le temps propre $\tau$ (invariant par changement de coordonnées) :
$$
\frac{DV^\mu}{D\tau} \equiv \frac{\dd V^\mu}{\dd\tau} + \Gamma^\mu_{\ \nu\lambda}\frac{\dd x^\lambda}{\dd\tau} V^\nu.$$
Posons $U^\mu$ le vecteur vitesse $\dd x^\mu/\dd\tau$. L'équation du mouvement [](#eq:eqm4) s'écrit alors très simplement
$$
\boxed{m\frac{DU^\mu}{D\tau}=f^\mu}
$$ 
Cette équation ainsi écrite rappelle fortement le principe fondamentale de la dynamique, mais place la mécanique dans un cadre relativiste et invariant par tout changement de systèmes de coordonnées. La notion de dérivée covariante est donc bien appropriée aux calculs de Relativité Générale et remplace bien la dérivée usuelle dans ce cadre. 

De manière générale, remplacer les dérivées usuelles d'une théorie physique par les dérivées covariantes permet d'aboutir à une écriture des lois physique respectant le principe d'équivalence, donc une invariance par changement de référentiel et en présence de gravitation. Si celle-ci est vraie sans gravitation et localement dans un espace de Minkowski, alors elle reste vraie dans un référentiel quelconque avec gravitation. Par exemple, en l'absence de champ gravitationnel les équation de Maxwell s'écrivent :
$$
\frac{\partial F^{\alpha\beta}}{\partial x^\alpha} = - J^\beta
$$
où $J^\beta$ est le quadri-vecteur courant électrique et $F^{\alpha\beta}$ le tenseur électromagnétique. Si on introduit les tenseurs $F^{\mu\nu}$ et $J^\mu$ tels que ces derniers se réduisent à $F^{\alpha\beta}$ et $J^\beta$ dans un référentiel inertiel de Minkowski, alors la théorie électromagnétique respecte le principe d'équivalence si on utilise la dérivée covariante :
$$
F^{\mu\nu}{}_{;\mu} = - J^\mu
$$
et cette écriture est valide dans tout système de coordonnées puisque vraie dans Minkowski.

:::{note} Dérivée covariante d'un vecteur covariant

Notons que pour un vecteur covariant, la dérivée covariante s'écrit :
$$\label{eq:dcov-cov}
\frac{DV_\mu}{D\tau} \equiv \frac{\dd V_\mu}{\dd\tau} - \Gamma^\nu_{\ \mu\lambda}\frac{\dd x^\lambda}{\dd\tau} V_\nu.
$$
:::


### Vers l'équation d'Einstein

Armés de ces outils, allons maintenant vers une dérivation simple de l'équation d'Einstein qui résume la gravitation à une déformation de l'espace-temps par la matière. Commençons par nous intéresser à une particule massive se déplaçant lentement dans un champ gravitationnel faible, constant mais quelconque cette fois. D'après le Principe d'Équivalence, on a vu qu'il existe un système de coordonnées inertielles $\left(ct',\vec x'\right)$ tel que l'équation du mouvement [](#eq:eqm1) soit encore valable dans un autre référentiel $\left(ct,\vec x\right)$ mais avec champ gravitationnel. L'hypothèse de vitesse faible nous permet de négliger $\dd\vec x/\dd\tau$ devant $c\dd t/\dd\tau$. On a alors au premier ordre dans un champ de gravité faible et quasi-stationnaire :
$$
\frac{\dd^2x^\mu}{\dd\tau^2} + \Gamma^\mu_{\ 00}\left(c\frac{\dd t}{\dd\tau}\right)^2=0, \qquad \Gamma^\mu_{\;\;00} \approx -\frac{1}{2}g^{\mu\nu}\frac{\partial g_{00}}{\partial x^\nu}.
$$

Dans l'hypothèse d'un champ gravitationnel faible, on peut adopter une métrique presque cartésienne :
$$
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad \vert h_{\mu\nu} \vert \ll 1,
$$
et on obtient au premier ordre : 
$$
\left\lbrace
\begin{array}{rl}
    \mu=1,2,3\ : & \displaystyle{\frac{\dd^2\vec x}{\dd\tau^2} = \frac{1}{2}\left(c\frac{\dd t}{\dd\tau}\right)^2\vec{\nabla} h_{00} } \\
    \mu=0\ : &  \displaystyle{\frac{\dd^2 t}{\dd\tau^2} = 0.}
\end{array}
\right.
$$ 
D'après la deuxième équation on en déduit que $\dd t/\dd\tau$ est une constante. Donc on peut diviser la première équation par $\dd t / \dd \tau$ et on obtient :
$$
\label{eq:vers_einstein}
\frac{\dd^2\vec x}{\dd t^2} = \frac{1}{2}c^2\vec{\nabla} h_{00}.
$$ 
Or on sait que dans la limite newtonienne on a :
$$
\frac{\dd^2\vec x}{\dd t^2} = -\vec{\nabla} \phi$$
avec $\phi$ le potentiel gravitationnel (i.e. $\phi=-\GN M /r$ s'il est engendré par une masse $M$ à une distance $r$, $\GN$ étant la constante de Newton). En comparant avec [](#eq:vers_einstein), on a $h_{00}=-2\phi/c^2+\text{constante}$. Or la métrique doit être de Minkowski à l'infini (hypothèse de faible perturbation), donc $h_{00}=-2\phi/c^2$ et :
$$
\label{eq:g00}
g_{00}=-\left(1+\frac{2\phi}{c^2}\right),
$$ 
Par conséquent, la métrique de l'espace-temps va pouvoir contenir les effets gravitationnels. L'élément $g_{00}$ correspondant à la composante temporelle de la métrique, le battement des horloges dépend par conséquent de l'intensité du champ gravitationnel. Ceci correspond à l'effet Einstein, la seule conséquence de la Relativité Générale aujourd'hui utilisée technologiquement (dans le GPS, voir [](#fig:effet_einstein)).


:::{figure} ../../images/effet_eintein.svg
:name: fig:effet_einstein
:align: center
:width: 90%

Illustration de l'effet Einstein. Un photon tombant dans un puits gravitationnel gagne de l'énergie donc sa fréquence augmente. De façon équivalente, on peut dire que les horloges dans un champ gravitationnel retardent par rapport à des horloges identiques situées en dehors. Les récepteurs GPS doivent prendre en compte cet effet pour en déduire leur position par rapport aux satellites.
:::

Cet exercice sur une particule ponctuelle nous apprend que le champ gravitationnel est finalement contenu dans la métrique, et que cette métrique dépend donc de la présence de matière. Il est donc possible d'imaginer une généralisation de ce constat. Le potentiel newtonien est déterminé par l'équation de Poisson :
\begin{equation}\label{eq:poisson}
\nabla^2\phi = 4\pi \GN \rho_m
\end{equation}
où $\rho_m$ est la densité volumique de masse et $\GN$ la constante de Newton. Cette dernière est associée à la densité d'énergie $\epsilon$ du tenseur énergie-impulsion de la matière $T_{00} = \epsilon = \rho_m c^2 $ (voir chapitre [](./02_friedmann_equations.md)), donc avec l'équation [](#eq:g00) on peut obtenir :
$$
\nabla^2 g_{00}=-\frac{8\pi \GN}{c^4} T_{00}.
$$ 
Cette équation n'est pas invariante par transformation de Lorentz, d'où la nécessité de modifier la théorie de la gravitation newtonienne si on admet le principe de relativité restreinte. Les tenseurs sont les bons objets qui peuvent permettre d'atteindre cet objectif. On peut alors imaginer qu'il existe un tenseur $G_{\mu\nu}$ combinant des dérivées premières et secondes de la métrique $g_{\mu\nu}$ généralisant cette dernière équation à toutes les coordonnées tel que 
$$
\label{eq:einstein1}
G_{\mu\nu}=-\frac{8\pi \GN}{c^4} T_{\mu\nu}.
$$ 
Cette dernière équation correspond à une première version de *l'équation d'Einstein*. Ce raisonnement ne nous a permis que d'intuiter sa forme, mais une autre démonstration plus rigoureuse permet d'obtenir l'expression du tenseur d'Einstein $G_{\mu\nu}$ : 
$$
G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R
$$
avec $R_{\mu\nu}$ le tenseur de Ricci et $R$ la courbure scalaire (trace du tenseur de Ricci $R^\mu_{\;\mu}$), eux-mêmes obtenus par le tenseur de Riemann $R^\mu_{\ \nu\alpha\beta}$ : 
$$
\begin{aligned}
R^\mu_{\ \nu\alpha\beta} & = -\partial_\alpha \Gamma^\mu_{\ \nu\beta} +  \partial_\beta \Gamma^\mu_{\ \nu\alpha} - \Gamma^\mu_{\ \alpha\sigma}\Gamma^\sigma_{\ \nu\beta} + \Gamma^\mu_{\ \beta\sigma}\Gamma^\sigma_{\ \nu\alpha} \\
R_{\mu\nu} & =R^\alpha_{\ \mu\alpha\nu}.
\end{aligned}
$$
*Comme le tenseur d'Einstein $G_{\mu\nu}$ contient des dérivées secondes de la métrique, l'équation d'Einstein lie la courbure de l'espace-temps donc les trajectoires des corps à son contenu en énergie et matière.*


De plus, $G_{\mu\nu}$ apparaît être de divergence nulle. C'est l'identité de Bianchi :
$$G^{\mu\nu}_{\;\;\;;\mu}=0.$$

:::{important} Conservation de $T^{\mu\nu}$

L'identité de Bianchi et l'équation d'Einstein [](#eq:einstein1) impose la conservation de l'énergie, par conséquent directement issue de propriétés géométriques :
$$
\label{eq:conservation_energie_tenseur}
T^{\mu\nu}_{\;\;\;;\mu}=0
$$
:::

Par l'identité de Bianchi, on voit aussi que l'équation d'Einstein peut être définie à une constante près[^3] tout en gardant la conservation de l'énergie. Cette constante est aujourd'hui appelée constante cosmologique. Voici l'équation d'Einstein sous sa forme définitive {cite:p}`Einstein1917` :
$$
\label{eq:einstein2}
\boxed{G_{\mu\nu}-\Lambda g_{\mu\nu} = -\frac{8\pi \GN}{c^4} T_{\mu\nu}}
$$


[^1]: A travers cette définition, on a choisi une métrique de signature $(-,+,+,+)$ que nous garderons par la suite. 

[^2]: Par la suite, l'indice $0$ des tenseurs correspondra donc à la coordonnée temporelle, tandis que les indices suivants correspondront aux coordonnées spatiales.

[^inv]: Sachant que $\frac{\partial x'^\rho}{\partial x^\mu} \frac{\partial x^\mu}{\partial x'^\nu} = \delta^\rho_\nu$, car $\frac{\partial x'^\rho}{\partial x^\mu}$ est la Jacobien de la transformation de coordonnées $x^\mu \to x'^\nu $ et le second facteur est son inverse.

[^2prime]: Si étudie une particule de masse nulle, il suffit de remplacer $f^\mu/m$ par le modèle de l'interaction s'appliquant à cette particule.

[^3]: Car on a aussi $g^{\mu\nu}{}_{;\mu}=0$.
