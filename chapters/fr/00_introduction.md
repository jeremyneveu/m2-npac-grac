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

### Principe de Relativité Restreinte

A la fin du XIXe siècle, la théorie de l'électromagnétisme de Maxwell s'impose pour décrire les phénomènes électriques et magnétiques. Mieux, elle prédit l'existence des ondes électromagnétiques qui sont découvertes en 1888 par Heinrich Hertz. Leur étude montre qu'elles ont toutes les propriétés connues des ondes lumineuses (réflexion et réfraction, interférences, polarisation et diffraction) et surtout la même célérité $c = 1/\sqrt{\epsilon_0\mu_0}$ qui surgit des équations de Maxwell. Ondes hertziennes et lumineuses sont donc des ondes électromagnétiques, mais l'électromagnétisme de Maxwell ne dit rien du référentiel dans lequel cette célérité serait définie. Par ailleurs, l'expérience de Michelon et Morley (1887) <wiki:Expérience_de_Michelson_et_Morley> montre que la vitesse de la lumière ne semble pas se composer avec la vitesse de la Terre autour du Soleil, alors que celle de Fizeau (1849) <wiki:Expérience_de_Fizeau> montre qu'elle se compose partiellement avec celle d'un fluide en mouvement. On comprend donc que la théorie électromagnétique s'accorde mal avec la mécanique newtonienne et semble avoir besoin d'être rafistolée au gré de résultats expérimentaux contradictoires. 

:::{figure} ../../images/michelson_morley_setup.svg
:name: fig-michelson-morley
:width: 100%

Schéma de l'expérience de Michelson-Morley (1887). La lumière est divisée en deux faisceaux perpendiculaires qui parcourent des distances égales avant de se recombiner au détecteur. L'absence de franges d'interférence démontre l'invariance de la vitesse de la lumière.
:::

Plutôt que d'entreprendre ce chemin hasardeux qui aurait fait perdre la puissance prédictive de la théorie lorsque des corps sont en mouvements, Albert Einstein propose une approche révolutionnaire dans son célèbre article de 1905 *Sur l'électrodynamique des corps en mouvement* {cite:p}`Einstein1905`. Il postule que la célérité de la lumière est la même en tout référentiel et remet donc en cause la composition galiléenne des vitesses, et même les notions d'espace et de temps. Le principe fondamental de cette nouvelle physique est le principe de relativité restreinte.

:::{important} Principe de Relativité Restreinte

Les lois de la physique sont identiques dans tous les référentiels galiléens. 
:::

Si une loi physique semble vraie dans un référentiel inertiel, aux incertitudes expérimentales près définissant son domaine de validité, alors elle doit rester vraie dans un autre référentiel galiléen. C'est par exemple le cas du principe fondamental de la dynamique de Newton. Cependant, imposer cela à la théorie de l'électromagnétisme pose un sérieux problème, car il faut remettre en cause la composition galiléenne des vitesses pour les ondes électromagnétiques.

### Transformations de Lorentz

*Si la théorie électromagnétique est vérifiée dans un référentiel galiléen, quelles sont les transformations de coordonnées spatio-temporelles pouvant laisser cette célérité invariante?*
Soit deux évènements de coordonnées spatio-temporelles $(t_1,x_1,y_1,z_1)$ et $(t_2, x_2, y_2, z_2)$ dans un référentiel $\mathcal{R}$ liés entre eux par l'échange d'un signal lumineux, alors :
$$ c^2(t_2-t_1)^2 = (x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2 $$
Imposer la constance de la vitesse implique dans un autre référentiel $\mathcal{R}'$ galiléen on vérifie aussi : 
$$ c^2(t'_2-t'_1)^2 = (x'_2-x'_1)^2 + (y'_2-y'_1)^2 + (z'_2-z'_1)^2 $$
Il apparait donc judicieux de définir l'intervalle espace-temps pour un intervalle entre deux évènements infiniment proches :
$$ \dd s^2 = -c^2 \dd t^2 + \dd x^2 + \dd y^2 + \dd z^2 $$

Soit un quadri-vecteur de coordonnées $x^\alpha$, où la composante $\alpha=0$ correspond au temps[^x0] $ct$ (avec $c$ la fameuse célérité maximale et $t$ le temps) et les composantes $\alpha=1,2,3$ correspondent aux coordonnées cartésiennes $x,y,z$. Dans ce cours, nous emploierons les lettres grecques pour les composantes allant de 0 à 3 et les lettres latines pour les composantes spatiales allant de 1 à 3. On définit la métrique de Minkowski :
\begin{equation}\label{eq:minkowski}
\eta_{\alpha\beta} = \begin{pmatrix}
-1 & 0& 0& 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix}
\end{equation}
de telle sorte qu'en coordonnées cartésiennes on puisse définir l'intervalle espace-temps ainsi entre deux coordonnées spatio-temporelles proches :
$$ \dd s^2 = - c^2 \dd t^2 + \dd \vec x^2 = \eta_{\alpha\beta}\dd x^\alpha \dd x^\beta $$

:::{important} Conventions de ce cours
- Signature métrique : $(-,+,+,+)$
- Indices grecs : 0,1,2,3 (espace-temps)
- Indices latins : 1,2,3 (espace seulement)
:::

Pour passer à un autre système de coordonnées $x'^\alpha$, on introduit la transformation de Lorentz $\Lambda^\alpha_{\;\beta}$ ainsi :
\begin{equation}\label{eq:boost}
x'^{\alpha} = \Lambda^\alpha_{\;\beta} x^\beta + a^\alpha,
\end{equation}
où $a^\alpha$ est une simple translation temporelle et spatiale. 

Quelle forme doit prendre cette transformation linéaire[^linearity]? Pour assurer que la vitesse de la lumière est invariante par changement de système de coordonnées $x'^{\alpha}$, on doit conserver $\vert \dd \vec x' / \dd t'\vert = c' = c$ pour la propagation d'un rayon lumineux donc $\dd s'^2=\dd s^2 = 0$. La transformation de Lorentz doit donc assurer la conservation de l'intervalle espace-temps:
$$
\dd s'^2 =  \eta_{\alpha\beta}\dd x'^\alpha \dd x'^\beta = \eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta}  \dd x^\gamma \dd x^\delta = \eta_{\gamma\delta} \dd x^\gamma \dd x^\beta = \dd s^2
$$
D'où la relation de fermeture:
$$
\label{eq:dscons}
\eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta} =  \eta_{\gamma\delta}
$$

A partir de la relation constitutive [](#eq:dscons), on peut démontrer que les transformations de Lorentz forment un groupe défini par $\Lambda^{0}_{\;0}\geqslant 1$ et $\mathrm{det}\;\Lambda=+1$. Quelques calculs plus tard (voir {cite:t}`raimond` ou {cite:t}`langlois2013RG` par exemple), on montre que la transformation des coordonnées entre deux référentiels dont l'un se déplace à la vitesse $\vec v = v \vec e_{1}$ s'écrit de façon unique :
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
pour garantir la constance de la célérité de la lumière dans tous les référentiels galiléens.

Si on inclut des rotations de l'espace, avec un référentiel se déplaçant à la vitesse $\vec v$ constante par rapport à un autre référentiel, les composantes du tenseur $\Lambda^\alpha_{\;\beta}$ s'écrivent finalement :
\begin{equation}\label{eq:lorentz2}
\Lambda^0_{\;0} = \gamma,\quad \Lambda^i_{\;0} = -\gamma v_i / c,\quad \Lambda^0_{\;j} = -\gamma v_j / c,\quad \Lambda^i_{\;j} = \delta_{ij} +  (\gamma - 1)  \frac{v_i v_j}{v^2}
\end{equation}

:::{note} Lien entre lumière et relativité
Pourquoi la vitesse de la lumière spécialement devrait être invariante ? Quel est le lien entre la lumière et une nouvelle écriture de la mécanique ? Comme la lumière est véhiculée par le photon, une particule de masse nulle, c'est aussi la vitesse maximale pouvant être atteinte dans notre Univers. Si la théorie électromagnétique n'avait pas été écrite en 1905, un argument aurait aussi pu être qu'il doit exister une vitesse maximale dans l'Univers si on pense qu'aucun transport d'information ne peut être instantané. A ce moment là, le principe de relativité impose que cette vitesse limite doit être la même dans tous les référentiels inertiels et la célérité pivot de la théorie de la Relativité Restreinte aurait été la vitesse de l'interaction qui se propage le plus rapidement. Ce qui dans notre Univers se trouve être l'interaction électromagnétique {cite:p}`landau1989theory`. Dans les deux approches, le principe de Relativité Restreinte impose qu'il existe une vitesse maximum $c$ invariante par changement de système de coordonnées. 
:::

Les transformations de Lorentz imposent que non seulement la vitesse de la lumière ne se compose pas avec la vitesse d'un observateur ou d'une source, mais aussi qu'elle est indépassable. Or la force de gravitation se propage instantanément à distance infinie dans la théorie newtonienne. Le déplacement d'une masse est instantanément ressenti gravitationnellement dans tout l'Univers. Après avoir dû réécrire les équations de la cinématique pour préserver les équations de Maxwell, Einstein s'attelle pendant les 10 années suivantes à reformuler la théorie de la gravitation newtonienne pour qu'elle rentre dans ce nouveau cadre. L'ingrédient principal de sa démarche est le constat que masse gravitationnelle et masse inertielle sont identiques, ce qui est indice du fait que la gravitation pourrait être décrite par un effet cinématique.

De Newton à la Relativité Générale
----------------------------------

La Relativité Générale est la théorie de la gravitation à la base de la cosmologie moderne. Elle donne une explication géométrique à la force gravitationnelle introduite par Newton trois siècles auparavant. Dans cette théorie, tomber par terre n'est plus dû à un vecteur force malheureusement orienté vers le sol, mais à la déformation de l'espace-temps provoquée par la Terre. Formulée ainsi, la Relativité Générale semble bien compliquée pour peu de choses. Mais les principes généraux à la base de cette théorie et la richesse de ses implications (dont la théorie newtonienne) en font la théorie phare pour décrire la gravitation. Au long de cette section, nous allons introduire pas à pas plusieurs concepts de la Relativité Générale tels que l'équation des géodésiques, la métrique et la dérivée covariante, pour aboutir à l'équation d'Einstein de la Relativité Générale, base de la cosmologie moderne. Cette introduction est largement inspirée de {cite:t}`Weinberg1972` et {cite:t}`Gourgoulhon2013`. 

### Le Principe d'Équivalence

Dans le principe fondamental de la dynamique énoncé par Newton, pourquoi la masse intervenant dans le terme d'inertie est-elle rigoureusement la même que celle intervenant dans la gravitation newtonienne ? Cette égalité troublante entre masse inertielle et masse gravitationnelle, validée par des siècles d'expérimentations (pendules de Newton, balance d'Eötvös, etc.) singularise la gravitation par rapport aux autres interactions telles la force de Coulomb qui dépend de la charge électrique donc des corps considérés. Cela suggère que la gravitation n'est pas une propriété des corps eux-mêmes mais de l'espace dans lequel ils se meuvent. 

:::{tip} Expériences d'Eötvös (1889)
:class: dropdown

Dans cette expérience réalisée en 1889, Eötvös montre qu'une masse de bois et une masse de platine subissent la même force gravitationnelle à $10^{-9}$ près, en observant la torsion d'une balance {cite:p}`VonEotvos1890`. Cette dernière compare le couple exercé par la force gravitationnelle (dépendante de la masse gravitationnelle) et le couple exercé par la force centrifugre due à la rotation de la Terre (dépendande de la masse intertielle). Voir une description de l'expérience ici <wiki:Eötvös_experiment>.
:::

Considérons une masse ponctuelle soumise à un champ gravitationnel externe uniforme et constant $\vec g$ et à des forces non gravitationnelles $\vec f_{\rm ng}$. Alors le principe fondamental de la dynamique appliqué dans un référentiel galiléen $\mathcal{R}$ à cet objet nous permet de prédire sa position $\vec x$ à un instant $t$ par la résolution de l'équation différentielle :
$$m_i\frac{\dd^2\vec x}{\dd t^2} = m_g\vec g + \vec f_{\rm ng}$$ 
avec $m_g$ la masse gravitationnelle et $m_i$ la masse intertielle.
Plaçons nous dans un référentiel (non galiléen) accéléré $\mathcal{R}'$ par rapport au référentiel galiléen initial avec une accélération d'entrainement $\vec a_e$. Dans $\mathcal{R}'$ muni des coordonnées $(t, x')$, le principe fondamental de la dynamique s'écrit avec une force intertielle $-m\vec a_e$ (aussi appelée force fictive car venant d'un effet cinématique) due à l'accélération d'entrainement :
$$m_i\frac{\dd^2\vec x'}{\dd t^2} = m_g\vec g  -m_i\vec a_e + \vec f_{\rm ng}$$
Grâce à l'égalité entre masse intertielle et masse gravitationnelle $m_i=m_g=m$, on remarque qu'on peut faire un choix *particulier* de référentiel $\mathcal{R}'$ tel que $\vec g = \vec a_e$, tel que le principe fondamental de la dynamique s'écrit comme s'il n'y avait ni accélération et ni gravitation :
$$m\frac{\dd ^2\vec x'}{\dd t^2} = \vec f_{\rm ng}$$
Les lois de la physique apparaissent donc identiques pour un observateur lié à un référentiel galiléen considérant que l'objet subit une force de gravité et pour un observateur lié à un référentiel en chute libre et considérant que l'objet ne subit pas de force gravitationnelle. L'effet gravitationnel a été inscrit dans un changement de coordonnées $\vec x' = \vec x - g t^2/2$. Et si cette démarche était possible pour tout champ gravitionnel, au moins localement dans une région où $\vec g$ est quasi-constant et pendant une durée d'expérience où $\vec g$ est quasi-stationnaire ? Le Principe d'Équivalence formulé par Einstein prend acte de l'équivalence entre gravitation et accélération due à l'égalité des masses inertielle et gravitationnelle, du moins pour des champs gravitationnels qui varient faiblement dans le temps et l'espace, et l'élève en principe de construction pour les lois physiques.

:::{important} Le Principe d'Équivalence

*A chaque point de l'espace-temps dans un champ gravitationnel arbitraire il est possible de choisir un système local particulier de coordonnées inertielles tel que, dans une région suffisamment petite autour du point en question, toutes les lois de la nature prennent la même forme que dans un système de coordonnées cartésien non accéléré et sans gravitation* {cite:p}`Weinberg1972`. 
:::

C'est donc une généralisation du principe de relativité restreinte à tous les référentiels, en présence de gravitation ou non. Ce principe est vérifié expérimentalement avec une très bonne précision, notamment par le *Lunar Laser Ranging* {cite:p}`Williams2004` et par le satellite MICROSCOPE avec une précision de $2.7\times 10^{−15}$ {cite:p}`Microscope2022`.

### Équations du mouvement

Appliquons le Principe d'Équivalence au problème d'un objet massif en chute libre. Pour cet objet, il existe donc localement un système de coordonnées *particulier* tel que l'équation de sa trajectoire $x'^\mu$ s'écrive de la même manière que si le référentiel était non accéléré et sans gravitation :
\begin{equation}\label{eq:eqm1}
\frac{\dd^2 x'^\mu}{\dd\tau^2}=0,
\end{equation}
avec $\dd\tau$ le temps propre[^tau] :
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
$$
\Gamma^\nu_{\ \mu\rho} \equiv \frac{\partial x^\nu}{\partial x'^\lambda}\frac{\partial^2 x'^\lambda}{\partial x^\mu \partial x^\rho}.$$
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
:class: dropdown

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
donc l'espace reste euclidien après rotation. De façon équivalente on aurait pu obtenir la métrique $g_{\mu\nu}$ en étudiant la conservation d'un élément de longueur par rotation :
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
Si elles sont présentes, les forces autres que la gravitation s'appliquant à la particule test peuvent s'ajouter au membre de droite de l'équation [](#eq:eqm3) :
$$\label{eq:eqm4}
\boxed{\frac{\dd^2x^\nu}{\dd \tau^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd \tau}\frac{\dd x^\rho}{\dd \tau}=\frac{f_{\rm ng}^\mu}{m}}
$$
avec $m$ la masse de l'objet et $f_{\rm ng}^\mu$ le vecteur contravariant des forces non gravitationnelles s'appliquant à une particule massive[^2prime]. La bonne écriture du principe fondamental de la dynamique selon le Principe d'Equivalence est donc l'équation [](#eq:eqm4), car on peut montrer que cette dernière est bien invariante par une transformation locale de système de coordonnées (démonstration {cite:t}`Weinberg1972`[p. 102]) et se réduit au principe fondamental de la dynamique en l'absence de gravitation (connexion affine nulle) . 

:::{tip} Equation du mouvement pour les particules de masse nulle
:class: dropdown

Pour une particule sans masse, comme le photon ou le neutrino, le temps propre défini par l'équation [](#eq:proper-time) est nul. A la place de $\tau$ on peut alors utiliser une autre abscisse curviligne, telle la coordonnée $s = x^0$ pour paramétrer la trajectoire de la courbe. Par un raisonnement similaire on aboutit à cette équation du mouvement :
$$
\label{eq:eqm3}
\frac{\dd^2x^\nu}{\dd \lambda^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd \lambda}\frac{\dd x^\rho}{\dd \lambda}=0.
$$
:::

### Dérivée covariante

De manière générale, on veut dorénavant que les écritures des équations de la physique soit invariantes par changement de coordonnées et en présence ou non de gravitation. On définit ainsi une version alternative du Principe d'Equivalence pour guider la construction des équations physiques en Relativité Générale.

:::{note} Principe de Covariance Générale {cite:t}`Weinberg1972`[p. 91]

Les lois de la physique doivent respecter deux contraintes:
- les équations sont covariantes, i.e. elles restent de forme invariante selon un changement de coordonnées $x^\mu \to x'^\mu$;
- les équations sont valables en l'absence de gravitation; c'est-à-dire qu'elles sont conformes aux
lois de la Relativité Restreinte lorsque le tenseur métrique est égal au tenseur de Minkowski
et lorsque la connexion affine $\Gamma^\nu_{\ \mu\rho}$ s'annule.

:::

Comment se transforment les différents objets en physique lors d'un changement de coordonnées ? Tout d'abord, les nombres scalaires ne changent pas : ils sont invariants par changement de coordonnées (comme une température, une densité, $\pi$, etc.). Les vecteurs $V^\mu$ (contravariants) se transforment selon l'équation :
\begin{equation}\label{eq:Vtransfo}
V'^\mu = V^\nu \frac{\partial x'^\mu}{\partial x^\nu}
\end{equation}
car la projection des coordonnées du vecteur selon les vecteurs de base des deux systèmes sont différentes.

:::{tip} Transformation d'un vecteur
:class: dropdown

Soit le vecteur accélération de pesanteur $\vec g$, et un référentiel cartésien $\mathcal{R} = (\vec e_x, \vec e_y)$ tel que $\vec g = - g \vec e_y$. Dans un référentiel $\mathcal{R}'$ tourné d'un angle $\theta$ par rapport au référentiel $\mathcal{R}$, ses nouvelles coordonnées se trouvent facilement par rotation des vecteurs de base:
$$ 
\vec g = -g \vec e_y = -g (\cos \theta \vec e'_y + \sin \theta \vec e'_x) 
$$
Si on applique la formule [](#eq:Vtransfo), on retrouve bien la même chose :
\begin{align*}
\vec g \cdot \vec e'_x & = (\vec g \cdot \vec e_x) \frac{\partial x'}{\partial x} +  (\vec g \cdot \vec e_y) \frac{\partial x'}{\partial y}  =  0 - g \sin \theta \\
\vec g \cdot \vec e'_y & = (\vec g \cdot \vec e_x) \frac{\partial y'}{\partial x} +  (\vec g \cdot \vec e_y) \frac{\partial y'}{\partial y}  =  0 - g \cos \theta \\
\end{align*}
Le facteur $\partial x'^\nu / \partial x^\mu$ est appelé le Jacobien de la transformation.
:::


De manière plus générale, on définit les tenseurs comme les objets qui se transforment selon une généralisation de l'équation [](#eq:Vtransfo). Voici une écriture avec deux indices contravariant et un indice covariant :
$$
T'^{\mu\nu}_{\ \ \ \ \ \lambda} = T^{\kappa\rho}_{\ \ \ \ \sigma} \frac{\partial x'^\mu}{\partial x^\kappa}\frac{\partial x'^\nu}{\partial x^\rho} \frac{\partial x^\lambda}{\partial x'^\sigma}
$$

Si une équation physique est homogène en ces indices d'Einstein et est formée de tenseurs, alors elle remplit la première condition du Principe de Covariance Générale.

En physique, beaucoup d'équations sont locales et donc invoquent des dérivées. Le soucis qui se présentent alors est que la dérivée d'un vecteur ne se transforme hélas pas comme un tenseur. En effet, en dérivant [](#eq:Vtransfo) on obtient :
$$
\frac{\partial V'^\mu}{\partial x'^\lambda} = V^\nu \frac{\partial^2 x'^\mu}{\partial x'^\lambda \partial x^\nu}  + \frac{\partial V^\nu}{\partial x'^\lambda} \frac{\partial x'^\mu}{\partial x^\nu}
= V^\nu \frac{\partial^2 x'^\mu}{\partial x^\rho \partial x^\nu}  \frac{\partial x^\rho}{\partial x'^\lambda} + \frac{\partial V^\nu}{\partial x^\lambda} \frac{\partial x^\rho}{\partial x'^\lambda}   \frac{\partial x'^\mu}{\partial x^\nu}
$$
Le premier terme semble respecter les transformationes tensorielles mais pas le second. Ce dernier ressemble par contre beaucoup à la définition du la connexion affine. Ceci amène à définir la dérivée covariante $V^\nu{}_{;\mu}$ d'un vecteur $V^\nu$ par rapport à la coordonnée $x'^\mu$ :
$$
\boxed{V^\mu{}_{;\lambda} \equiv \frac{\partial V^\mu}{\partial x^\lambda} + \Gamma^\mu_{\ \lambda\rho}V^\rho}
$$
Le premier terme correspond à la variation ordinaire d'un vecteur si on le déplace dans son voisinage. Le second terme prend en compte les changements du systèmes de coordonnées lui aussi déplacé, car le symbole de Christoffel décrit les changements des vecteurs de base du référentiel. Cette définition de la dérivée se réduit à la simple dérivée partielle dans un référentiel sans gravitation i.e. de Minkowski (connexion affine nulle).

:::{figure} ../../images/covariant_derivative.svg

Illustration de la variation d'un vecteur $V^\mu$ (cyan) dans le voisinage d'une base $(e_\mu, e_\nu)$ d'un espace courbe. Suite à un déplacement dans son voisinage (ici le long de $e_\mu$), le vecteur change de taille (premier terme de la dérivée covariante) et la base qui définit ses projections donc ces coordonnées change également. La dérivée covariante calcule la variation des composantes du vecteur $V^\mu$ due à ces deux changements.
::: 

Cette définition de la dérivée en Relativité Générale exprime correctement la variation d'un vecteur le long d'une coordonnée dans un espace courbe. Ce vecteur variation se transforme bien comme un tenseur contravariant par un changement de coordonnées (contrairement à la dérivée usuelle): le vecteur variation $V^\mu{}_{;\lambda}$ est donc correctement défini pour tout système de coordonnées. 

Pour illustrer toute sa profondeur, voici la définition de la dérivée covariante $DV^\mu/D\tau$ non pas par rapport à une coordonnée, mais le long d'une courbe quelconque paramétrée par le temps propre $\tau$ (invariant par changement de coordonnées) :
$$
\frac{DV^\mu}{D\tau} \equiv \frac{\dd V^\mu}{\dd\tau} + \Gamma^\mu_{\ \nu\lambda}\frac{\dd x^\lambda}{\dd\tau} V^\nu.$$
Posons $U^\mu$ le vecteur vitesse $\dd x^\mu/\dd\tau$. L'équation du mouvement [](#eq:eqm4) s'écrit alors très simplement
$$
\boxed{\frac{DU^\mu}{D\tau}=\frac{f_{\rm ng}^\mu}{m}}
$$ 
Cette équation ainsi écrite rappelle fortement le principe fondamentale de la dynamique, mais place la mécanique dans un cadre relativiste, invariant par tout changement de systèmes de coordonnées et en présence de gravitation. La notion de dérivée covariante est donc bien appropriée aux calculs de Relativité Générale et remplace bien la dérivée usuelle dans ce cadre. 

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
\frac{\dd^2x^\mu}{\dd\tau^2} + \Gamma^\mu_{\ 00}\left(c\frac{\dd t}{\dd\tau}\right)^2=0, \qquad \Gamma^\mu_{\;\;00} \approx -\frac{1}{2}\eta^{\mu\nu}\frac{\partial g_{00}}{\partial x^\nu}.
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
*Comme le tenseur d'Einstein $G_{\mu\nu}$ contient des dérivées secondes de la métrique, l'équation d'Einstein lie la courbure de l'espace-temps (donc les trajectoires des corps) à son contenu en énergie et matière.*


De plus, $G_{\mu\nu}$ apparaît être de divergence nulle. C'est l'identité de Bianchi :
$$G^{\mu\nu}_{\;\;\;;\mu}=0.$$

:::{important} Conservation de $T^{\mu\nu}$

L'identité de Bianchi et l'équation d'Einstein [](#eq:einstein1) impose la conservation de l'énergie, par conséquent directement issue de propriétés géométriques :
$$
\label{eq:conservation_energie_tenseur}
T^{\mu\nu}_{\;\;\;;\mu}=0
$$
:::

Par l'identité de Bianchi, on voit aussi que l'équation d'Einstein peut être définie à une constante près[^gmunu] tout en gardant la conservation de l'énergie. Cette constante est aujourd'hui appelée constante cosmologique. Voici l'équation d'Einstein sous sa forme définitive {cite:p}`Einstein1917` :
$$
\label{eq:einstein2}
\boxed{G_{\mu\nu}-\Lambda g_{\mu\nu} = -\frac{8\pi \GN}{c^4} T_{\mu\nu}}
$$


:::{important} A retenir

- La Relativité Générale s'est construite sur le Principe d'Equivalence, exploitant la coincidence qu'est l'égalité apparente entre masse gravitationnelle et masse inertielle.
- Les lois physiques doivent être invariantes par changement de système de coordonnées et en présence ou non de gravitation, laquelle devient partie intégrante de la métrique de l'espace-temps.
- L'équation des géodésiques est l'équivalent RG de la seconde loi de Newton, quand l'équation d'Einstein est l'équivalent de l'équation de Poisson de la gravitation newtonienne.

:::

:::{seealso}  Pour approfondir

- Histoire de la gravitation et expériences fondatrices : {cite:t}`Weinberg1972`[chap.1]
- Démonstration des transformations de Lorentz : {cite:t}`raimond` ou J.M Levi-Leblond <doi:10.1119/1.10490> https://web.physics.utah.edu/~lebohec/P3740/levy-leblond_ajp_44_271_76.pdf 
- Métrique et exemples simples : {cite:t}`langlois2013RG`
- Dérivée covariante : {cite:t}`Weinberg1972`[chap.4]
- Effet Einstein et GPS : {cite:t}`Gourgoulhon2013` 

:::



[^tau]: A travers cette définition, on a choisi une métrique de signature $(-,+,+,+)$ que nous garderons par la suite. 

[^x0]: Par la suite, l'indice $0$ des tenseurs correspondra donc à la coordonnée temporelle, tandis que les indices suivants correspondront aux coordonnées spatiales.

[^linearity]: La linéarité est imposée par l'invariance de la physique par translation dans l'espace et le temps {cite:p}`raimond`.

[^inv]: Sachant que $\frac{\partial x'^\rho}{\partial x^\mu} \frac{\partial x^\mu}{\partial x'^\nu} = \delta^\rho_\nu$, car $\frac{\partial x'^\rho}{\partial x^\mu}$ est la Jacobien de la transformation de coordonnées $x^\mu \to x'^\nu $ et le second facteur est son inverse.

[^2prime]: Si étudie une particule de masse nulle, il suffit de remplacer $f_{\rm ng}^\mu/m$ par le modèle de l'interaction s'appliquant à cette particule.

[^gmunu]: Car on a aussi $g^{\mu\nu}{}_{;\mu}=0$.
