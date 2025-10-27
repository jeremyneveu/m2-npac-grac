---
short_title: L'Univers en expansion
authors:
  - jneveu
keywords: cosmological distances, scale factor, dark energy
---

L'Univers en expansion
======================

Dans le chapitre précédent, par de simples considérations géométriques, nous sommes parvenus à écrire la forme de la métrique solution de l'équation d'Einstein pour un Univers homogène et isotrope. D'un tenseur inconnu à 10 composantes (car la métrique est un tenseur symétrique), par des arguments de symétrie nous avons abouti à la métrique FLRW qui ne contient qu'une seule fonction inconnue du temps $a(t)$. Pour maintenant décrire la dynamique de l'Univers, et non plus sa géométrie, il faut résoudre l'équation d'Einstein afin de comprendre comment le contenu en matière et en énergie agit sur l'expansion de l'Univers via le facteur d'échelle $a(t)$.


Le tenseur énergie-impulsion
----------------------------

### Définition en Relativité Restreinte

Pour un ensemble de $N$ particules, en interaction ou non entre elles ou avec l'extérieur, la densité de quadri-impulsion $p^\mu$ de cet ensemble est définie par {cite:p}`Weinberg1972`[p. 43]:
$$
\sum_n p_n^{\mu}c\ \delta^{(3)}(\vec x - \vec x_n(t)) = T^{\mu 0}(t, \vec x) 
$$
où $\vec x_n(t)$ et $p_n^{\mu}(t)=(E_n/c, \vec p_n)$ sont les positions et quadri-impulsions de la particule $n$ à l'instant $t$. La densité de courant d'impulsion[^vecj] à travers une surface de normale $\vec e_i$ est quant à lui :
$$
\sum_n p_n^{\mu} \frac{\dd x_n^i(t)}{\dd t} \delta^{(3)}(\vec x - \vec x_n(t)) = T^{\mu i}(t, \vec x)
$$
Ces deux définitions peuvent être combinées pour obtenir un tenseur à deux indices :
$$
T^{\mu \nu}(t, \vec x) = \sum_n p_n^{\mu} \frac{\dd x_n^\nu(t)}{\dd t} \delta^{(3)}(\vec x - \vec x_n(t))
$$
avec $x_n^0(t)=ct$. Dans le référentiel où cet ensemble de particules est au repos, l'énergie d'une particule massive est $E_n= \gamma_n m^2 c^2$ (avec $\gamma_n$ son facteur de Lorentz) et son impulsion est $\vec p_n c = \gamma_n m \vec v_n c$: on démontre alors que $p_n^\mu c = E_n (\dd x_n^\mu /c \dd t)$[^pcphoton]. D'où l'écriture du tenseur énergie-impulsion en tant que tenseur symétrique en relativité restreinte :
$$
T^{\mu \nu}(t, \vec x) = c^2 \sum_n \frac{p_n^{\mu} p_n^{\nu}}{E_n} \delta^{(3)}(\vec x - \vec x_n(t))\label{eq:TmunuGaz}
$$



:::{figure} ../../images/tmunu_def.svg

Le tenseur énergie-impulsion représente les densités de courants de quadri-impulsions $p^\mu$ et la densité d'énergie $\epsilon$ dans un volume local d'espace-temps. Si le système physique étudié dans ce volume local n'est soumis à aucune force qui travaille hormis la gravitation, alors on a l'équation de conservation $T^{\mu\nu}_{\;\;\;;\mu}=0$.
:::

Le tenseur énergie-impulsion $T^{\mu\nu}$ de l'équation d'Einstein décrit la densité d'énergie et les flux volumiques de quantité de mouvements en mécanique relativiste. C'est un tenseur d'ordre 2, construit à partir du vecteur 4-impulsion, qui prend la forme suivante :
\begin{equation}
T^{\mu\nu}=\begin{pmatrix} 
T^{00}= \text{energy density}\,\,\,\,
& T^{01}=\text{energy/c flux through }x_1\,\,\,\,\,
& T^{02}=\text{energy/c flux through }x_2\,\,\,\,\,
& T^{03}=\text{energy/c flux through }x_3
\\  T^{10}=c\times \text{density of }p_1\,\,\,\,\,\,\,
& T^{11}= \text{flux of }p_1\text{ through }x_1\,\,\,\,\,\,\,
&  T^{12}= \text{flux of }p_1\text{ through }x_2\,\,\,\,\,\,\,
&  T^{13}= \text{flux of }p_1\text{ through }x_3
\\  T^{20}=c\times\text{density of }p_2\,\,\,\,\,\,\,
& T^{21}= \text{flux of }p_2\text{ through }x_1\,\,\,\,\,\,\,
&  T^{22}= \text{flux of }p_2\text{ through }x_2\,\,\,\,\,\,\,
&  T^{31}= \text{flux of }p_2\text{ through }x_3
\\  T^{30}= c\times\text{density of }p_3\,\,\,\,\,\,\,
& T^{31}= \text{flux of }p_3\text{ through }x_1\,\,\,\,\,\,\,
&  T^{32}= \text{flux of }p_3\text{ through }x_2\,\,\,\,\,\,\,
&  T^{33}= \text{flux of }p_3\text{ through }x_3
\end{pmatrix}
\label{stress-energy-tensor-meaning}
\end{equation}

Quelques remarques sur les composantes de ce tenseur :
* $T^{00}$ est la densité d'énergie $\epsilon$ locale, généralement c'est la composante dominante du tenseur énergie-impulsion;
* $T^{ii}$ représentent les flux de quantité de mouvement à travers une surface de normale colinéaire donc la pression cinétique $P$ exercée par le système physique dans la direction $\vec e_i$;
* $T^{ij},\ i \neq j$ représentent les densités de courant d'impulsion perpendiculairement aux directions des impulsions, donc des phénomènes de viscosité ou de cisaillement.


### Hydrodynamique en relativité


Plaçons nous dans le référentiel où l'ensemble de particules est en moyenne au repos, et considérons-le comme un fluide. C'est-à-dire qu'on l'étudie à des échelles bien supérieures au libre parcours moyen des particules. Supposons maintenant que ce fluide est parfait (<wiki:perfect_fluid>) : il ne possède aucune viscosité et aucune conductivité thermique {cite:p}`Weinberg1972`[p. 48]. Étant donné la définition d'un tenseur énergie-impulsion, dans le référentiel $\mathcal{R}'$ où le fluide parfait est au repos on peut écrire que le tenseur doit prendre la forme :
$$ T'^{\mu\nu}_{\rm PF} = \begin{pmatrix}
\epsilon & 0 & 0 & 0 \\
0 & P  & 0 & 0 \\ 
0 & 0 & P  & 0 \\ 
0 & 0 & 0 & P   \\ 
\end{pmatrix}
$$
En effet, si sa viscosité est nulle alors il ne peut y avoir de transfert d'impulsion latéralement à la direction des impulsions (car un écoulement visqueux se caractérise par de la diffusion de quantité de mouvement), donc $T^{ij} = 0$ si $i\neq j$. De même, si le fluide n'a aucune conductivité thermique alors il n'y a pas de flux d'énergie donc $T'^{0i}=T'^{i0}=0$. Sur la diagonale de la partie spatiale du tenseur, on retrouve la pression cinétique (un flux de quantité de mouvement à travers une surface dans le sens de l'impulsion). Les trois termes sont égaux pour un fluide parfait car une anisotropie des pressions supposent des transferts de quantité de mouvements donc de la viscosité (dite de volume <wiki:Volume_viscosity>). L'hypothèse de fluide parfait simplifie donc fortement la structure du tenseur énergie-impulsion. 

Ensuite, dans un référentiel inertiel quelconque, par exemple un laboratoire où l'on observe ce fluide parfait s'écoulant localement à vitesse $\vec v$, son tenseur énergie-impulsion se réécrit :
$$ T^{\mu\nu} = \Lambda^{\mu}_{\;\alpha} \Lambda^{\nu}_{\;\beta} T'^{\alpha\beta} $$
avec $\Lambda^\mu_{\;\alpha}$ la transformation de Lorentz définie par l'équation [](#eq:lorentz2). Plus explicitement :
$$ T^{ij}_{\rm PF} = P \delta^{ij} + (P + \epsilon) \frac{v^i v^j}{c^2- v^2}, \quad T^{i0}_{\rm PF} = (P + \epsilon) \frac{c v ^i}{c^2  - v^2}, \quad T^{00}_{\rm PF} = \frac{\epsilon c^2  + P v^2}{c^2  - v^2} \label{eq:TijV} $$
Définissons la quadri-vitesse adimensionée ainsi :
$$ \vec U =\frac{\ \dd \vec x }{c\dd \tau} = \frac{\vec v/c }{ \sqrt{1-(v/c)^2}}, \quad U^0 = \frac{c\dd t }{c\dd  \tau} =  \frac{1}{ \sqrt{1-(v/c)^2}}, \quad U_ \mu U ^\mu = -1  $$
alors le tenseur s'écrit :
$$ T^{\mu\nu}_{\rm PF} = (\epsilon + P) U^\mu U^\nu + P \eta^{\mu\nu}$$
Si le fluide est au repos, $U^\mu=(1,0,0,0)$ et on retrouve :
$$ T'^{\mu\nu}_{\rm PF} = \begin{pmatrix}
\epsilon & 0 & 0 & 0 \\
0 & P\eta^{11}  & 0 & 0 \\ 
0 & 0 & P\eta^{22}  & 0 \\ 
0 & 0 & 0 & P\eta^{33}   \\ 
\end{pmatrix}
$$

:::{note} Equation de Navier-Stokes
:class: dropdown

Pour simplifier, ramenons-nous au cas d'un fluide incompressible donc $\dd \rho / \dd t = 0$ et non relativiste donc $P / \rho c^2 \propto (v/c)^2 \ll 1$. Alors la dérivée de l'équation [](#eq:TijV) aboutit à :
$$ 0 = \frac{\partial T^{\mu\nu}}{\partial x^\nu} \Rightarrow
\left\lbrace\begin{align*}
& \mu = i:\ & 0 = & \vec\nabla P + \rho \frac{\partial \vec v}{\partial t} +  \rho (\vec v \cdot \vec\nabla)(\vec v)  \\
& \mu = 0:\ & 0 = & \rho \vec \nabla \vec v + \frac{\partial \rho}{\partial t} 
\end{align*}\right.
$$
La conservation du tenseur énergie-impulsion d'un fluide parfait permet de retrouver l'équation de Navier-Stokes sans viscosité et sans forces extérieures, et l'équation de conservation de la matière. 

Dans le cas de la Relativité Générale, on utilise la dérivée covariante au lieu de la dérivée partielle. A ce moment-là, les symboles de Christofell qui apparaissent vont traduire les forces gravitationnelles et intertielles, l'équivalent du terme $\rho \vec g$ de l'équation de Navier-Stokes habituelle.

:::

On voit que $T^{\mu\nu}_{\rm PF}$ est bien un tenseur car il se transforme comme un tenseur par un changement de coordonnées. Toute équation physique qui s'exprime sous la forme de tenseurs en Relativité Restreinte prend exactement la même forme dans un référentiel local d'un espace-temps courbe. Par conséquent, le tenseur énergie-impulsion peut s'écrire dans n'importe quelle métrique et se définit ainsi en Relativité Générale :
$$ \boxed{ T^{\mu\nu}_{\rm PF} = (\rho c^2 + P) U^\mu U^\nu + P g^{\mu\nu} }$$
Si le système physique étudié dans ce volume local n'est soumis à aucune force qui travaille hormis la gravitation, alors on a l'équation de conservation $T^{\mu\nu}_{\;\;\;;\mu}=0$, C'est un jeu de quatre équations qui représentent l'équation de conservation locale de l'énergie et de l'impulsion. 


### Tenseur énergie-impulsion cosmologique

Après ce préambule sur la définition du tenseur énergie-impulsion et son expression pour un fluide parfait, recherchons quelle est la forme de ce tenseur pour l'Univers aux grandes échelles, en appliquant le principe cosmologique. Si l'Univers est homogène et isotrope, alors les termes non diagonaux sont nuls car sinon ils sont à l'origine d'anisotropies. Sur la diagonale, les termes spatiaux doivent être égaux pour respecter l'isotropie de l'Univers (même pression cinétique dans toutes les directions). De plus l'homogénéité impose que le tenseur ne dépent pas de la position $\vec x$ mais seulement du temps. Par conséquent, le tenseur énergie-impulsion cosmologique s'écrit :
$$ T^{\mu\nu}_{\rm COSMO} = \begin{pmatrix}
\epsilon(t) & 0 & 0 & 0 \\
0 & P(t)g^{11}  & 0 & 0 \\ 
0 & 0 & P(t)g^{22}  & 0 \\ 
0 & 0 & 0 & P(t)g^{33}   \\ 
\end{pmatrix} = T'^{\mu\nu}_{\rm PF} \label{eq:def-Tmunu}
$$
Avec ces hypothèses, on en déduit que le tenseur énergie-impulsion cosmologique est le même que celui d'un fluide parfait homogène dans son référentiel au repos. Le comportement de la matière dans un Univers homogène et isotrope peut donc se décrire comme celle d'un fluide parfait, c'est-à-dire qu'on ne s'attend à observer aucun phénomène de viscosité ou de flux d'énergie. Cela implique que les transformations de la matière lors de l'évolution cosmologique de l'Univers sont _adiabatiques_. Le fluide étant au repos, on peut considérer que la quadri-vitesse de la matière aux échelles cosmologiques dans le référentiel d'observateurs comobiles s'écrit $U^0=1,\ U^i = 0$ et on obtient :
$$ \boxed{ T^{\mu\nu}_{\rm COSMO} = (\epsilon + P) U^\mu U^\nu + P g^{\mu\nu},\quad U^\mu=(1, 0,0,0) }\label{eq:def-Tmunu2}$$

En utilisant la métrique FLRW, solution d'un univers homogène et isotrope également, pour un univers plat avec une paramétrisation cartésienne, le tenseur énergie-impulsion prend la forme simple :
\begin{equation}
\label{eq:tmunu_fluide}
T^{\mu\nu}  =  
\begin{pmatrix}
\epsilon & 0 & 0 & 0 \\
0 & P/a^2(t) & 0 & 0 \\ 
0 & 0 & P/a^2(t) & 0 \\ 
0 & 0 & 0 & P/a^2(t)  \\ 
\end{pmatrix}.
\end{equation}


```{note} Démontration plus formelle
:class: dropdown

Dans notre hypothèse d'Univers de symétrie maximale, rappelons tout d'abord qu'on peut définir un temps cosmique, universel,  en utilisant l'évolution physique de l'Univers comme une horloge (densité de matière, température du CMB...). Les hypersurfaces de l'espace-temps paramétrées par ce temps universel sont alors elles-mêmes des sous-espaces de symétrie maximale. Les tenseurs $\mathcal{T}$ représentant des observables cosmologiques de tels sous-espaces de symétrie maximale doivent alors être de _forme invariante_ c'est-à-dire qu'ils restent les mêmes fonctions des coordonnées spatiales à une date $t$ quelque soit le choix du système de coordonnées choisi : si on passe d'un système $x^\rho$ à $x'^\rho$, on doit avoir $\mathcal{T}'_{\mu\nu\ldots}(x'^\rho) = \mathcal{T}_{\mu\nu\ldots}(x'^\rho)$. Intuitivement, si $\mathcal{T}$ est le tenseur énergie-impulsion cela revient entre autre à demander que la densité d'énergie soit identique en tout point pour tout choix de système de coordonnées {cite:p}`Weinberg1972`[p. 409]. 

On peut démontrer alors une propriété importante concernant la forme que doivent prendre les tenseurs de ces sous-espaces {cite:p}`Weinberg1972`[p. 392]. Un tenseur de forme invariante dans un espace de symétrie maximale :
- est indépendant de la position si c'est un scalaire,
- est nul si c'est un vecteur,
- est proportionnel au tenseur métrique si c'est un tenseur d'ordre 2.


:::{tip} Démonstration pour un tenseur scalaire {cite:p}`Weinberg1972`[p. 392]
:class: dropdown

Si $\mathcal{T}^{\mu\nu\ldots}$ se transforme comme un tenseur et est de forme invariante, alors :
$$
\label{eq:form_invariant}
\mathcal{T}_{\mu\nu\ldots}(x^\rho) =
\frac{\partial x'^\lambda}{\partial x^\mu}\frac{\partial x'^\sigma}{\partial x^\nu}\cdots \mathcal{T}'_{\lambda\sigma\ldots}(x'^\rho) = \frac{\partial x'^\lambda}{\partial x^\mu}\frac{\partial x'^\sigma}{\partial x^\nu}\cdots \mathcal{T}_{\lambda\sigma\ldots}(x'^\rho)
$$
Pour un tenseur scalaire $\mathcal{S}(x^\mu)$ :
$$
\label{eq:scalar_form_invariant}
\mathcal{S}(x^\rho) = \mathcal{S}(x'^\rho)
$$
Soit une transformation spatiale infinitésimale :
$$x'^\rho = x^\rho + \epsilon \xi^\rho(x),\quad \vert\epsilon\vert \ll 1$$
alors l'équation [](#eq:scalar_form_invariant) devient au premier ordre :
$$
0 = \xi^\lambda(x) \frac{\partial \mathcal{S}(x)}{\partial x^\lambda}
$$
Comme $\mathcal{S}$ est maximallement symétrique, on a le droit de choisir n'importe quelle transformation $\xi^\lambda$ non nulle, donc :
$$
\frac{\partial \mathcal{S}(x)}{\partial x^\lambda} = 0
$$
donc $\mathcal{S}$ de forme invariante n'est pas une fonction des coordonnées d'espaces.
:::

Par conséquent, mathématiquement on peut introduire $\epsilon(t)$ et $P(t)$ deux fonctions du temps telles que le tenseur énergie-impulsion se simplifie en :
$$ \begin{align}
T^{00} & =  \epsilon(t) &\quad  \text{(scalaire)} \\
T^{i0} & = T^{0i} = 0 & \quad  \text{(vecteur)} \\
T^{ij} & =  P(t) \gamma^{ij}& \quad \text{(tenseur d'ordre 2)}
\end{align} $$

Comment interpréter ces considérations mathématiques ? Tout d'abord, si on compare ces termes avec [](#stress-energy-tensor-meaning) alors on identifie $\epsilon$ à la densité d'énergie et $P$ à la pression cinétique (flux de quantité de mouvement à travers une surface)[^epsP]. Le tenseur énergie-impulsion $T^{\mu\nu}$ obtenu s'identifie à celui d'un fluide parfait. 

```

Les équations de Friedmann
---------------------------

Résoudre l'équation d'Einstein [](#eq:einstein2) consiste à en trouver une métrique solution, compte tenu de la répartition en matière et énergie codée dans $T^{\mu\nu}$. Supposer les principes d'homogénéité et d'isotropie pour ce tenseur, impose que la métrique est la métrique de Friedmann-Lemaître-Robertson-Walker (FLRW), utilisant le jeu de coordonnées comobiles sphériques usuel $(ct, \sigma, \theta, \phi)$:
$$
\begin{aligned}\label{eq:flrw}
\displaystyle g_{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & \dfrac{a^2(t)}{1-k\sigma^2} & 0 & 0 \\ 
0 & 0 & a^2(t)\sigma^2 & 0 \\ 
0 & 0 & 0 & a^2(t) \sigma^2 \sin^2 \theta  \\ 
\end{pmatrix},\end{aligned}
$$ 
où $a(t)$ est une fonction inconnue. Le paramètre d'échelle $a(t)$ peut être obtenu en résolvant l'équation d'Einstein connaissant le contenu du tenseur énergie-impulsion de l'Univers $T^{\mu\nu}$ et la valeur de $k$. Pour la métrique FLRW, son inverse est simplement:
$$
g^{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & \dfrac{1-k\sigma^2}{a^2(t)} & 0 & 0 \\ 
0 & 0 & \dfrac{1}{a^2(t)\sigma^2}  & 0 \\ 
0 & 0 & 0 & \dfrac{1}{a^2(t) \sigma^2 \sin^2 \theta}   \\ 
\end{pmatrix}.
$$

En utilisant la métrique FLRW [](#eq:flrw), calculons pour l'exemple la connexion affine suivante à partir de l'équation [](#eq:connexion):
$$
\begin{aligned}
\Gamma^1_{\ 01} & = \frac{1}{2} g^{1 \mu} \left( \partial_0 g_{1\mu} + \partial_1 g_{0 \mu} - \partial_\mu g_{01} \right) \\
& = \frac{1}{2} g^{1 1} \left(\frac{\partial g_{11}}{c\partial t} + \partial_\sigma g_{01} - 0 \right) \text{ car } \forall \mu \neq 1, g^{1\mu}=0\\
& = \frac{1}{2} \frac{1-k\sigma^2}{a^2} \left( \frac{2 \dot{a} a}{c(1-k\sigma^2)} + 0 \right) \\
& = \frac{\dot a}{ca} = \frac{H}{c}.
\end{aligned}
$$

De la même manière, on obtient les autres connexions affines, puis les tenseurs de Riemann et Ricci. Au final, le tenseur d'Einstein est diagonal et vaut: 
$$
\begin{aligned}
G_{00} & =  - 3 \left( \frac{\dot{a}^2}{c^2 a^2}+ \frac{k}{a^2} \right), \\
G_{ij} & = \frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{c^2 a^2}g_{ij} \text{ pour } i=j\neq 0.
\end{aligned}
$$
A partir de l'équation d'Einstein [](#eq:einstein2) et du tenseur énergie-impulsion [](#eq:tmunu_fluide), on obtient pour la coordonnée $00$ et pour les coordonnées spatiales $ij$: 
$$
\begin{aligned}
G_{\mu\nu}-\Lambda g_{\mu\nu} & = -8\pi \GN T_{\mu\nu}/c^4 \\
\Leftrightarrow  & \left\lbrace
\begin{array}{rl}
    \text{00: } &  \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{c^2 k}{a^2} \right) = 8\pi \GN \rho + c^2 \Lambda} \\
    ij\text{: } &   \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{a^2} = - \frac{8\pi \GN}{c^2 } P + c^2 \Lambda }
\end{array}
\right.\end{aligned}
$$ 
Ce sont les deux équations de Friedmann. Les voici maintenant exprimées en fonction du paramètre de Hubble
$H=\dot{a}/a$ : 
$$
\label{eq:friedmann}
\left\lbrace
\begin{array}{rl}
    \text{00: } & \displaystyle{H^2 = \frac{8\pi \GN \rho}{3} + \frac{c^2 \Lambda}{3} - \frac{c^2 k}{a^2}}\\
    ij\text{: } &  \displaystyle{2\dot{H} + 3H^2 = - \frac{8\pi \GN}{c^2 } P + c^2 \Lambda - \frac{c^2 k}{a^2}}
\end{array}
\right.
$$
La première équation de Friedmann relie explicitement l'évolution du facteur d'échelle $a(t)$ au contenu énergétique de  l'Univers. De plus, en soustrayant ces deux équations et en combinant le résultat avec la dérivée temporelle de la première, on peut obtenir l'équation de conservation de l'énergie que l'on obtiendrait aussi directement en calculant $T^{\mu\nu}_{\;\;\;;\mu}=0$ dans la métrique FLRW : 
$$
\label{eq:conservation_energie}
\boxed{\dot{\epsilon} = -3 H( \epsilon  + P )}
$$

:::{exercise}
:label: exo:friedmann

In this exercise, we use the FLRW metric in cartesian coordinates, and the corresponding stress energy tensor for a perfect fluid:
\begin{equation}
g_{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & a^2(t) & 0 & 0 \\
0 & 0& a^2(t) & 0 \\
0 & 0& 0& a^2(t)  \\
\end{pmatrix}\qquad 
T_{\mu\nu}=\begin{pmatrix} \rho c^2 & 0 & 0 & 0 \\ 0 &a^2 P & 0 & 0 \\ 0&0&a^2 P &0 \\ 0&0&0&a^2 P \end{pmatrix}
\label{stress-energy-cosmo-tensor}
\end{equation}
We recall the following formula for the Christoffel and Riemann tensors:
\begin{align}
\Gamma^\kappa_{\ \mu\nu} &= \frac{1}{2}g^{\kappa\lambda}\left( g_{\mu\lambda,\nu}+g_{\lambda\nu,\mu}-g_{\mu\nu,\lambda} \right) \\
R^{\mu}_{\ \nu\alpha\beta} &= -\Gamma^\mu_{\ \nu\beta,\alpha} + \Gamma^\mu_{\ \nu\alpha,\beta} - \Gamma^\lambda_{\ \nu\beta}\Gamma^\mu_{\ \lambda\alpha} + \Gamma^\lambda_{\ \nu\alpha}\Gamma^\mu_{\ \lambda\beta} \\
R_{\mu\nu}& = R^\rho_{\ \mu\rho\nu} = -\Gamma^\rho_{\ \mu\nu,\rho} + \Gamma^\rho_{\ \mu\rho,\nu} - \Gamma^\rho_{\ \rho\lambda}\Gamma^\lambda_{\ \mu\nu} + \Gamma^\rho_{\ \nu\lambda}\Gamma^\lambda_{\ \mu\rho} \\
R &= g^{\mu\nu}R_{\mu\nu}
\end{align}
with $_{,\mu}$ the derivative $\partial / \partial x^\mu$.


1. Show that $\Gamma^0_{\ ij} = \dot{a}a/c \delta_{ij}$ and $\Gamma^j_{\ 0i}=\dot{a}/(ac)\delta^j_i$, with the latin index standing for the spatial coordinates $i=1,2,3$. The other Christoffel symbols are null.
2. Show that $R_{00}=3\ddot{a}/(ac^2)$ and $R_{ij}=-(\ddot{a}a+2\dot{a}^2)\delta_{ij}/c^2$.
3. Show that $R=-6\left(\ddot{a}/a+(\dot{a}/a)^2\right)/c^2$ and finally that $G_{\mu\nu}=R_{\mu\nu}-g_{\mu\nu}R/2$ is:
\begin{equation}
G_{\mu\nu}={1 \over c^2}\begin{pmatrix} 3{\dot{a}^2\over a^2} & 0 & 0 & 0 \\ 0 &-2\ddot{a}a-\dot{a}^2 & 0 & 0 \\ 0&0& -2\ddot{a}a-\dot{a}^2 &0 \\ 0&0&0&-2\ddot{a}a-\dot{a}^2  \end{pmatrix}
\label{Einstein-cosmo-tensor}
\end{equation}
4. Write the two Friedmann equations in term of the Hubble parameter $H=\dot{a}/a$ instead of $a$.
5. From the two Friedmann equations, find the energy conservation equation law $\dot{\rho} c^2 = -3 H(\rho c^2 + P)$.

:::{solution} exo:friedmann
:class: dropdown

1. Let's compute the Christoffel symbols:
\begin{align}
\Gamma^{0}_{\mu\nu} & = \frac{1}{2}g^{0\lambda}\left( g_{\mu\lambda,\nu}+g_{\lambda\nu,\mu}-g_{\mu\nu,\lambda} \right) \\
 & = \frac{1}{2}g^{00}\left( g_{\mu 0,\nu}+g_{0\nu,\mu}-g_{\mu\nu,0} \right) \\
  & = \frac{1}{2}g^{00}\left( g_{0 0,\nu}+g_{00,\mu}-g_{\mu\nu,0} \right) \\
  & = \frac{1}{2}(-1)\times\left( 0+ 0 -g_{\mu\nu,0} \right) \\
  & = \frac{1}{2}g_{\mu\nu,0}
\end{align}
We find:
\begin{equation}
\Gamma^{0}_{ij} =  -\frac{1}{2}g_{ij,0} =   -\frac{1}{2}\frac{\partial (-a^2(t))}{c\partial t} \delta_{ij}= \frac{\dot{a}a}{c} \delta_{ij}
\end{equation}
with $\delta_{ij}$ the Kronecker symbol such that $\delta_{ij}=1$ only if $j=i$. It is a number (not a matrix). Then:
\begin{align}
\Gamma^{j}_{0i} & = \frac{1}{2}g^{j\lambda}\left( g_{0\lambda,i}+g_{\lambda i,0}-g_{0i,\lambda} \right) \\
 & = \frac{1}{2}g^{jk}\left( g_{0k,i}+g_{ki,0}-g_{0i,k} \right) \\
  & = \frac{1}{2}g^{jk}\left( 0+g_{ki,0}-0 \right) \\
  & = \frac{1}{2}g^{jk}\times\left( \frac{-2a\dot{a}}{c}\delta_{ik} \right)  \\
  & = g^{jk}\times\left( +\frac{\dot{a}}{ac}g_{ik} \right)  \\
  & = \frac{\dot{a}}{ac}\delta^j_i
\end{align}
with $\delta^j_i$ the identity matrix ($\delta^i_i = 3$, but $\delta_{ii}=1$).

2. Now the Ricci tensors :
\begin{align}
R_{00} & = -\Gamma^\rho_{\ 00,\rho} + \Gamma^\rho_{\ 0\rho,0} - \Gamma^\rho_{\ \rho\lambda}\Gamma^\lambda_{\ 00} + \Gamma^\rho_{\ 0\lambda}\Gamma^\lambda_{\ 0\rho} \\
& = 0 + \Gamma^\rho_{\ 0\rho,0} + 0 + \Gamma^\rho_{\ 0\lambda}\Gamma^\lambda_{\ 0\rho} \\
& =  + \Gamma^i_{\ 0i,0} + 0 + \Gamma^i_{\ 0j}\Gamma^j_{\ 0i} \\
& = 3\frac{\ddot{a}a-\dot{a}^2}{a^2 c^2} +  \left(\frac{\dot{a}}{ac}\right)^2 \delta^i_j \delta^j_i\\
& = 3\frac{\ddot{a}a-\dot{a}^2}{a^2 c^2} + 3 \left(\frac{\dot{a}}{ac}\right)^2\\
& = 3 \frac{\ddot{a}}{ac^2}
\end{align}
\begin{align}
R_{ij} & = -\Gamma^\rho_{\ ij,\rho} + \Gamma^\rho_{\ i\rho,j} - \Gamma^\rho_{\ \rho\lambda}\Gamma^\lambda_{\ ij} + \Gamma^\rho_{\ i\lambda}\Gamma^\lambda_{\ j\rho} \\
& = -\Gamma^0_{\ ij,0} + 0 -\Gamma^k_{\ k0}\Gamma^0_{\ ij}+\Gamma^0_{\ ik}\Gamma^k_{\ j0} + \Gamma^k_{\ i0} \Gamma^0_{\ jk} \\
& = -\frac{\ddot{a}a+\dot{a}^2}{c^2}\delta_{ij} -\frac{\dot{a}}{ac}\frac{\dot{a}a}{c}\delta^k_k \delta_{ij} +  \frac{\dot{a}}{ac}\frac{\dot{a}a}{c} \delta_{ik}\delta^k_j +  \frac{\dot{a}}{ac}\frac{\dot{a}a}{c} \delta_{jk}\delta^k_i\\
& = -\frac{\ddot{a}a+\dot{a}^2}{c^2}\delta_{ij} -3\frac{\dot{a}}{ac}\frac{\dot{a}a}{c} \delta_{ij} + 2 \frac{\dot{a}}{ac}\frac{\dot{a}a}{c} \delta_{ij}\\
& = -\frac{a^2}{c^2}\left(\frac{\ddot{a}}{a}+2\frac{\dot{a}^2}{a^2}\right)\delta_{ij}
\end{align}
with $\delta_{ik}\delta^k_j=\delta_{ij}$ and $\delta^k_k=3$.

3. Now the Einstein tensor :
From the Einstein equation $G_{\mu\nu} - \Lambda g_{\mu\nu} = -8\pi G T_{\mu\nu}/c^4$ write the Friedmann equations:
\begin{equation} \left\lbrace
\begin{array}{l}
   \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{c^2k}{a^2} \right) = 8\pi \GN \rho + c^2 \Lambda} \\
    \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{a^2} = - 8\pi \GN P/c^2 + c^2 \Lambda }
\end{array}
\right.
\end{equation}
(here we admit the Friedmann equations with an arbitrary curvature $k$).

\begin{align}
R &= g^{\mu\nu}R_{\mu\nu} \\
& = g^{00}R_{00} + g^{ij}R_{ij}\\
& = -1\times\left( 3 \frac{\ddot{a}}{ac^2}\right) -  g^{ij}\delta_{ij} \frac{a^2}{c^2}\left(\frac{\ddot{a}}{a}+2\frac{\dot{a}^2}{a^2}\right) \\
& = -1\times\left( - 3 \frac{\ddot{a}}{ac^2}\right)  -\frac{\delta^i_i}{a^2} \frac{a^2}{c^2}\left(\frac{\ddot{a}}{a}+2\frac{\dot{a}^2}{a^2}\right) \\
& = -6 \left(\frac{\ddot{a}}{ac^2} + \frac{\dot{a}^2}{a^2c^2}\right) \\
\end{align}
with $g^{ij}=\delta^{ij}/a^2$ and $\delta^i_i=3$.
\begin{align}
G_{00} &= R_{00}-g_{00}R/2 \\
& = 3 \frac{\ddot{a}}{ac^2} - \frac{6}{2}\left(\frac{\ddot{a}}{ac^2} + \frac{\dot{a}^2}{a^2c^2}\right) \\
& =- 3 \frac{\dot{a}^2}{a^2c^2} 
\end{align}
\begin{align}
G_{ij} &= R_{ij}-g_{ij}R/2 \\
& =-\frac{a^2}{c^2}\left(\frac{\ddot{a}}{a}+2\frac{\dot{a}^2}{a^2}\right)\delta_{ij} -(a^2\delta_{ij})\times \frac{-6}{2}\left(\frac{\ddot{a}}{ac^2} + \frac{\dot{a}^2}{a^2c^2}\right) \\
& = a^2\left(2\frac{\ddot{a}}{ac^2}+ \frac{\dot{a}^2}{a^2c^2}\right) \delta_{ij}
\end{align}
Using the definition of $ T_{\mu\nu}$, we obtain directly the two Friedmann equations:
\begin{equation}
G_{\mu\nu} - \Lambda g_{\mu\nu}  = -\frac{8\pi \GN}{c^4}T_{\mu\nu}
\end{equation}
\begin{align}
\label{Friedmann1}
3{\dot{a}^2 \over a^2}&=& 8 \pi \GN \rho + c^2 \Lambda\\
2{\ddot{a} \over a} + {\dot{a}^2 \over a^2}& =& - {8 \pi \GN \over c^2}P + c^2 \Lambda
\label{align}
\end{align}

4. Using $H=\dot a / a$:
\begin{equation} \left\lbrace
\begin{array}{l}
   \displaystyle{3 H^2+ \frac{3kc^2}{a^2} = 8\pi \GN \rho + c^2\Lambda} \\
    \displaystyle{2\dot{H} + 3H^2 + \frac{c^2k}{a^2} = - 8\pi \GN P/c^2 + c^2\Lambda }
\end{array}
\right.
\end{equation}
using $\ddot{a}/a=\dot{H}+H^2$. 

5. And finally the energy-momentum tensor conservation:
\begin{align}
8\pi G \dot{\rho} & = 6\dot{H}H - \frac{6c^2 k \dot{a}}{a^3} \\
& = 3H \left[-8\pi \GN P / c^2 + c^2 \Lambda - 3 H^2 - \frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi \GN P / c^2 -8 \pi \GN \rho + 2\frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi \GN P / c^2 -8 \pi \GN \rho \right]
\end{align}
and $\dot{\rho} c^2 = -3 H(\rho c^2 + P)$. 
This is the same result as in the $T^{\beta \alpha}_{\,\,\,\,\,\,;\alpha}=0$ computation (as expected).


:::

:::{exercise} Evolution de l'entropie
:label: exo:expansion_isentropique

A partir du premier principe de la thermodynamique et de l'équation [](#eq:conservation_energie), retrouver que l'expansion  de l'Univers est isentropique.

:::

:::{solution} exo:expansion_isentropique
:class: dropdown

$$\dd U = T \dd S - P \dd V $$
$$U = a^3 \epsilon, \quad V = a^3$$
$$ \dd(a^3 \epsilon) = - P \dd (a^3) + T \dd S \Rightarrow 3 \dot{a} a^2 \epsilon + a^3 \dot{\epsilon} = - 3 P \dot{a} a^2  + T \frac{\dd S}{\dd t}\Rightarrow \dot{\epsilon} = -3\frac{\dot{a}}{a}(P+\epsilon) +T \frac{\dd S}{\dd t} $$
Donc 
$$\frac{\dd S}{\dd t} = 0$$
et l'expansion est isentropique. C'est attendu étant donné que pour un Univers homogène et isotrope le tenseur énergie-impulsion est celui d'un fluide parfait donc sans viscosité ni transfert de chaleur. L'évolution est donc adiabatique ($\delta Q=0$).
:::




Inventaire cosmologique
-----------------------

Le tenseur énergie-impulsion inclut la matière non-relativiste et relativiste. La matière relativiste est généralement nommée rayonnement car aujourd'hui le rayonnement de photons du CMB est largement dominant dans cette composante. 

### Matière

La matière non relativiste n'exerce pas de pression donc 
$$P_m=0,$$
puis : 
$$
\label{eq:conservation_energie_matiere}
\dot{\rho}_m = -3 H\rho_m \Rightarrow \rho_m = \rho_m^0 \left(\frac{a_0}{a}\right)^{3}.
$$
Cette  dernière relation traduit bien le fait que si une boîte de côté $a$ contenant une certaine quantité de matière voit la longueur de ses côtés doubler, alors la densité de matière est bien divisée par $2^3$. 

### Photons et neutrinos

Pour la matière relativiste (photons, neutrinos), 
$$P_r =  \frac{1}{3} \epsilon_r,$$
donc :
$$
\label{eq:conservation_energie_radiation}
\dot{\epsilon}_r = -4 H\epsilon_r \Rightarrow \epsilon_r = \epsilon_r^0 \left(\frac{a_0}{a}\right)^{4}.
$$ 
Le raisonnement avec une boîte cubique de côté $a$ s'applique aussi ici, mais si toutes les longueurs doublent, alors la longueur d'onde du rayonnement aussi donc son énergie est divisée par 2. On retrouve bien une diminution de la densité d'énergie de rayonnement en $2^4$.


:::{note} Equation d'état du gaz parfait

Pour un gaz parfait, on rappelle que l'équation d'état est :
$$ P = \rho_n k_B T  $$
avec $T$ sa température, $\rho_n$ la densité particulaire et $k_B$ la constante de Boltzmann.
S'il est à basse température (i.e. non relativiste) alors on a $\epsilon \approx m c^2 \rho_n$ et on veut :
$$\frac{P}{\epsilon} = \frac{k_B T}{mc^2} \ll \frac{1}{3}$$ 
donc $ T \ll m c^2 / 3 k_B $. Pour un gaz d'hydrogène, $T \ll 10^{12}\,$K. Donc on voit que la matière telle qu'on la connait est non relativiste aujourd'hui et même bien avant le CMB.

:::

:::{note} Hypothèse de non interaction
:class: dropdown

Nous avons utilisé l'équation [](#eq:conservation_energie) pour en déduire que la matière non relativiste possède une densité qui évolue en $a^{-3}$ alors que la matière relativiste évolue en $a^{-4}$. Le lecteur attentif aura peut-être remarqué que la densité et la pression de l'équation [](#eq:conservation_energie) sont pourtant la somme des densités et pressions relativistes et non relativistes. Est-ce que dans un Univers possédant ces deux composantes les équations [](#eq:conservation_energie_matiere) et [](#eq:conservation_energie_radiation) sont-elles encore valables ?

L'équation [](#eq:conservation_energie) peut se déduire d'un raisonnement thermodynamique qui peut nous être utile ici. L'expansion de l'Univers étant adiabatique, la variation d'entropie liée à l'expansion est nulle donc $\dd S = 0$. Le premier principe de la thermodynamique sur un volume $V$ d'Univers donne :
$$\label{eq:conservation_energie_thermo}
\dd U = -P \dd V + T \dd S \Leftrightarrow \dd \left(\epsilon_m V + \epsilon_r V  \right) = -\frac{1}{3}\epsilon_r \dd V$$
Si les deux composantes n'interagissent pas entre elles, alors cette dernière équation peut se scinder en ses deux composantes,  comme deux systèmes thermodynamiques indépendants :
$$\dd \left(\epsilon_m V\right) = 0, \quad \dd \left(\epsilon_r V  \right) = -\frac{1}{3}\epsilon_r \dd V$$
Si elles interagissaient, ceci ne serait pas vrai. De ces deux équations, on en déduit de nouveau les équations [](#eq:conservation_energie_matiere) et [](#eq:conservation_energie_radiation).

:::




### Constante cosmologique

Dans les équations de Friedmann [](#eq:friedmann), il est possible d'interpréter la constante cosmologique $\Lambda$ et la courbure $k$ en terme de densités d'énergie au même titre que la densité d'énergie $\rho$ du tenseur énergie-impulsion. 

La densité d'énergie associée à la constante cosmologique est parfois appelée densité d'énergie noire, en raison des étranges propriétés associées à cette dernière :
$$\epsilon_\Lambda(t) = \rho_\Lambda c^2 =  \frac{c^4 \Lambda}{8\pi \GN} = \text{ constante }.$$ 
On voit que la densité d'énergie associée à la constante cosmologique étant constante dans le temps, cette dernière possède un comportement bien singulier : quelque soit la taille de l'Univers, il y a toujours autant d'énergie par unité de volume. Elle n'est donc pas diluée comme toute énergie ordinaire lorsque celui-ci est en expansion. De plus, grâce à la seconde équation de Friedmann, on voit que la pression associée à la constante cosmologique serait :
$$P_\Lambda = - \epsilon_\Lambda,$$
soit une pression négative ! Dans la physique ordinaire, un des rares phénomènes où interviennent des pressions négatives est la cavitation (<wiki:Pressure#Negative_pressures>). En posant $\epsilon_{\mathrm{tot}}=\epsilon + \epsilon_\Lambda$ (et $P_{\mathrm{tot}}=P + P_\Lambda$) puis en combinant les deux équations de Friedmann [](#eq:friedmann) de façon à éliminer le terme de courbure, on  obtient :
\begin{equation}
\label{eq:ddota}
2\dot{H} + 2H^2 = \frac{2\ddot{a}}{a} = -\frac{8\pi \GN}{3}\left( \epsilon _{\mathrm{tot}} + 3P_{\mathrm{tot}}\right).
\end{equation}
On constate que l'expansion de l'Univers s'accélère ($\ddot{a}>0$) si $P_{\mathrm{tot}}<-\epsilon_{\mathrm{tot}}/3$. L'Univers étant constitué essentiellement de matière non relativiste et de rayonnement, la condition précédente devient équivalente à :
$$
\ddot{a} > 0 \Leftrightarrow \epsilon_\Lambda > \epsilon_r + \epsilon_m/2$$
En conclusion, si la constante cosmologique domine le contenu en énergie de l'Univers, alors elle engendre une telle pression négative que ce dernier entre en _expansion accélérée_.

:::{note} Un point sur les unités

Comme $\epsilon_\Lambda$ est une densité d'énergie, on en déduit que $\Lambda$ a la dimension de l'inverse du carré d'une longueur : 
$$
\label{eq:dimensions}
\left[a\right] = \mathsf{L},\quad \left[\rho \right] = \mathsf{M}\cdot \mathsf{L}^{-3}, \quad \left[\epsilon \right] = \left[P \right] = \mathsf{M}\cdot \mathsf{L}^{-1} \cdot \mathsf{T}^{-2}\quad \left[\Lambda \right] = \mathsf{L}^{-2} $$
Concernant le tenseur métrique FLRW, ses compostantes ont des unités diverses tout comme le vecteur position associé:
$$
\left[ g_{\mu\nu} \right] = [1,\mathsf{L}^{2},\mathsf{L}^{2},\mathsf{L}^{2}],\quad \left[(ct,\sigma,\theta,\phi)\right] = [(\mathsf{L},1,1,1)] $$
Le tenseur énergie-impulsion $T^{\mu\nu}$ dans FLRW également contient des composantes homogènes à des densités d'énergie et d'autres en $\left[P/a^2 \right]$. Il ne faut pas être trop troublé par les unités physiques diverses présentes dans les tenseurs, car ce ne sont que des tenseurs donc l'encodage d'une fonction vectorielle. Les observables physiques doivent être des champs _scalaires_ issus de l'application de ses tenseurs, donc invariants par changement de système de coordonnées (contrairement aux composantes du tenseur). Par exemple, les longueurs sont définies par $\dd s = \sqrt{g_{\mu\nu}\dd x^\mu \dd x^\nu}$ pour des déplacements $\dd x^\mu$, la pression est définie par le bilan de flux de moment cinétique selon les 3 directions spatiales $P=T^i_{\ \ \ i}/3$, et les relations entre densité d'énergie et pression sont données par les équations de conservation _scalaires_ issues de  $T^{\mu \nu}_{\,\,\,\,\,\,;\mu}=0$.
:::


### Courbure

La densité d'énergie associée à l'énergie de courbure s'identifie à : 
$$
\epsilon_k(t) =\rho_k(t) c^2 = - \frac{3 c^4 k  }{8\pi \GN a^2(t)}.$$
De même, son effet en terme de pression est :
$$P_k = \frac{c^4 k}{8\pi \GN a^2(t)}.$$


Les paramètres cosmologiques
----------------------------

### Paramètres d'équation d'état

L'équation d'état $w$ associée à une composante de l'Univers est définie par le rapport de sa pression et de sa densité d'énergie :
$$
\label{eq:def-w}
\boxed{w=P/\epsilon}
$$

-   La matière froide non relativiste n'exerce pas de pression sur son milieu extérieur d'où $P_m=0$ donc $w_m=0$.

-   La matière relativiste exerce quant à elle une pression sur son milieu de valeur $P_r =  \epsilon_r / 3 $ d'où $w_r=1/3$.

-   Pour la constante cosmologique, on a $P_\Lambda = - \epsilon_\Lambda$ donc son équation d'état est constante et négative $w_\Lambda = -1$.

-   La courbure assimilée à un fluide parfait aurait un paramètre d'équation d'état $w_k=1/3$.


### Paramètres de densité d'énergie

On peut définir une densité critique, qui correspondrait à la densité que l'on doit avoir dans un univers homogène et isotrope en expansion de courbure spatiale nulle et contenant seulement de la matière non relativiste (cf équation [](#eq:friedmann)) : 
$$
\rho_c(t) = \frac{3H^2(t)}{8\pi \GN}.$$ 
Il est commode de définir aussi sa valeur actuelle :
$$
\rho_{c}^0 = \frac{3H^2_0}{8\pi \GN} = 1.1 \times 10^{-29} \left( \frac{H_0}{75\text{ km/s/Mpc}}\right)^2\text{ g/cm}^3 \approx 6 \text{ protons/m}^3.
$$
où $H_0$ est la constante de Hubble.

On définit les paramètres de densité (sans dimension) en normalisant les densités d'énergie par la densité critique, soit :
$$
\Omega_m(t) = \frac{\rho_m(t)}{\rho_c(t)},\quad \Omega_\Lambda(t) = \frac{c^2 \Lambda}{3H^2(t)}, \quad \Omega_k(t) = -\frac{c^2 k}{a^2(t)H^2(t)}
$$
$$
\Omega_m^0 = \frac{\rho_m^0}{\rho_c^0},\quad \Omega_\Lambda^0 = \frac{c^2 \Lambda}{3H^2_0}, \quad \Omega_k^0 = -\frac{c^2 k}{a_0^2 H^2_0}.
$$
La première équation de Friedmann s'écrit alors simplement :
$$
\label{eq:omega_sum}
1 = \Omega_m(t) + \Omega_r(t) + \Omega_\Lambda(t) + \Omega_k(t)
$$

:::{math}
:label: eq:friedmann2
\bar H^2 (t) \equiv \frac{H^2(t)}{H_0^2} = \Omega_m^0 \left(\frac{a_0}{a(t)}\right)^{3} + \Omega_r^0 \left(\frac{a_0}{a(t)}\right)^{4} + \Omega_\Lambda^0 +  \Omega_k^0 \left(\frac{a_0}{a(t)}\right)^{2}.
:::
Ce modèle d'Univers liant la prédiction de son expansion $\bar H(z)$ à son contenu composé d'une constante cosmologique, de matière et de radiation, est appelé modèle $\Lambda$CDM ($\Lambda$ pour la constante cosmologique et CDM pour *Cold Dark Matter*) dans le cas $k=0$ (Univers plat). C'est le modèle standard de la cosmologie.


### Modélisations de l'énergie noire

Quelle est la véritable nature de l'énergie noire ? Est-ce la manifestation de l'énergie du vide ? Une seconde constante fondamentale de la gravitation ? Ou bien une nouvelle cinquième force ? La manifestation de dimensions spatiales supplémentaires ? Ces questions sur la nature de l'énergie noire n'ont pour le moment pas de réponses, mais depuis la découverte de l'expansion accélérée en 1998 {cite:p}`Riess1998,Perlmutter1999` de nouveaux relevés cosmologiques sont en cours pour mesurer précisément l'équation d'état de l'énergie noire $w_{DE}$ : tant qu'on mesure $w_{DE} = w_\Lambda=-1$ alors l'accélération de l'expansion peut s'expliquer avec un unique paramètre qui est la valeur de $\Lambda$. Si les mesures s'écartent significativement de $-1$, alors des modèles plus complexes seront à tester.

C'est pourquoi aujourd'hui, en plus du modèle standard $\Lambda$CDM, les cosmologistes testent des modèles empiriques qui cherchent des écarts au modèle standard :
- Flat $w$CDM : modèle d'Univers plat avec comme paramètres  libres $\Omega_m^0$, $\Omega_r^0$ et $w_{DE}$;
- $w$CDM : modèle de courbure quelconque avec comme paramètres  libres $\Omega_m^0$, $\Omega_r^0$, $\Omega_\Lambda^0$ et  $w_{DE}$;
- $w_0w_a$CDM : modèle où le paramètre d'équation d'état de l'énergie noire est donnée par deux paramètres libres :
$$
w_{DE}(a) = w_0 + \left(1 - \frac{a}{a_0}\right)w_a$$

L'enjeu majeur pour les relevés cosmologiques actuels et futurs est de mesurer $w_a$, afin de mesurer les variations de l'accélération de l'expansion de l'Univers.


Distances cosmologiques
------------

La cosmologie est une science observationnelles. Il faut inférer les propriétés de l'Univers sans pouvoir se déplacer ou refaire l'expérience du Big Bang, mais à partir de nos observations seulement. Les paramètres cosmologiques sont liés au taux d'expansion de l'Univers $H(z)$. Donc pour pouvoir les estimer nous devons être capable de mesurer $H(z)$. Ce taux d'expansion est présent dans les distances propres et comobiles définies [Sec. {number}](#distance-propre-et-distance-comoving), mais celles-ci ne sont pas mesurables. 

:::{warning}

Ni la distance propre ni la distance comobile ne sont mesurables car elles supposent de pouvoir s'affranchir de l'expansion de l'Univers. Or, en cosmologie, on veut mesurer des distances et leur évolution pour en déduire le comportement de $a(t)$ et donc le comportement du contenu de l'Univers. Traditionnellement, la cosmologie utilise les photons comme messagers venant des galaxies les plus lointaines. L'observation des astres lumineux peut nous conduire à déterminer des distances selon au moins deux de leurs aspects: leur luminosité et leur taille apparente. On peut ainsi définir deux distances basées sur l'observation des flux lumineux $\Phi$ et des tailles angulaires $\delta$ :
$$
\Phi = \frac{L}{4\pi D_L^2}, \qquad \delta = \frac{l}{D_A}
$$
où $L$ est la luminosité intrinsèque d'un objet (en watts) et $l$ une taille physique (en mètres).

:::


### Distance de Hubble

Avec les paramètres $c$ et $H_0$, il est possible de construire une quantité homogène à une longueur. Cette distance typique en cosmologie est appelée *distance de Hubble* et vaut :
$$
D_H = \frac{c}{H_0} = 3000\,\text{Mpc/}h
$$
où $h$ est usuellement défini par :
$$
H_0 = 100\,h\,\text{km/s/Mpc}
$$
Donc pour $h=0.7$, on trouve $D_H \approx 4.3 \,\text{Gpc} \approx 14 \,\text{Gly}$. Cette valeur va apparaître pour toutes les distances (non comobiles) définies ci-après.


### Distance de luminosité 

Dans un espace statique et plat, le flux lumineux apparent $\Phi_0$ d'une source au repos à distance $D_L$ serait $L_E/4\pi D_L^2$. On propose donc de définir la distance de luminosité d'une source $D_L(z)$ en cosmologie par :
$$
\Phi_0 \equiv \frac{L_E}{4 \pi D_L^2(z)}
$$

:::{figure} ../../images/distances3.svg
:name: fig:distances_croquis_DL
:align: center
:width: 40%

Notations pour le calcul de la distance de luminosité.
:::


Considérons une source située en $\sigma_E$, émettant $\delta N_E$ photons de fréquence moyenne $\nu_E$ à l'instant $t_E$ pendant un temps $\delta t_E$ (se reporter à la [](#fig:distances_croquis_DL)). Sa luminosité est :
$$
L_E = h\nu_E \frac{\delta N_E }{\delta t_E}.$$ 
Alors le flux surfacique reçu par un observateur possédant un télescope d'ouverture $A$ est : 
$$
\Phi_0 = h \nu_0\frac{\delta N_0 }{A \delta t_0}.$$ 
La surface sur laquelle se répartit, à l'instant $t_0$, le flux émis est:
$$
S = \int_0^{2\pi} \int_0^\pi \sqrt{-g} \dd\theta \dd\phi = \int_0^{2\pi} \int_0^\pi a^2(t_0)\sigma^2(t_0)\sin\theta \dd\theta \dd\phi = 4 \pi a^2_0 \sigma^2_E.
$$
avec $\sigma(t_0)=\sigma_E$.
Le nombre de photons émis $\delta N_E$ intercepté par la surface collectrice de taille $A$ est donc :
$$
\delta N_0 = \delta N_E \frac{A}{4 \pi a^2_0 \sigma^2_E}.$$
Or à partir de l'équation [](#eq:redshift2), on a :
$$\nu_E = \nu_0 a_0/a(t_E) = \nu_0 (1+z)$$
et aussi :
$$\delta t_E = \delta t_0/(1+z).$$
D'où le flux reçu :
$$\Phi_0 = h \nu_0\frac{\delta N_0 }{A \delta t_0 } = h \nu_0  \frac{\delta N_E}{4 \pi a^2_0 \sigma^2_E \delta t_0 } = \frac{L_E}{4 \pi a^2_0 \sigma^2_E(1+z)^2}.$$

On en déduit l'expression de la distance de luminosité dans un univers courbe et en expansion, fonction des paramètres cosmologiques et le redshift :
$$
\Rightarrow D_L(z) = a_0 \sigma_E (1+z) = a_0 (1+z)
\left\lbrace
\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \text{sh } \chi(z) & \text{ si } k=-1 
\end{array}
\right. 
$$

Le facteur d'échelle aujourd'hui $a_0$ n'est pas accessible via les équations de Friedmann qui ne donnent que le taux d'expansion. En revanche, il s'exprime en fonction des paramètres cosmologiques et $H_0$ :
\begin{equation}
\Omega_k^0 = - \frac{kc^2}{H_0^2 a_0^2} \Rightarrow a_0 = \left\lbrace\begin{array}{l}
    \displaystyle{\frac{c}{H_0\sqrt{-\Omega_k^0}}}  \text{ if } k=+1 \\
    \text{indéterminé mais usuellement valant } 1 \text{ if } k=0 \\
    \displaystyle{\frac{c}{H_0\sqrt{\Omega_k^0}}}  \text{ if } k=-1 
\end{array}
\right.
\end{equation}
Ainsi :
\begin{equation}
\displaystyle{\chi(z) = \left\lbrace\begin{array}{cl}
    \displaystyle{H_0\sqrt{-\Omega_k^0}\int_0^z\frac{dz}{H(z)}}  & \text{ if } k=+1 \\
    \displaystyle{\frac{1}{a_0}\int_0^z\frac{cdz}{H(z)}} & \text{ if } k=0 \\
    \displaystyle{H_0\sqrt{\Omega_k^0}\int_0^z\frac{dz}{H(z)} } & \text{ if } k=-1 
\end{array}
\right.}
\end{equation}

$$
D_L(z) = (1+z) \left\lbrace
\begin{array}{cl}
    \displaystyle \frac{c}{H_0 \sqrt{-\Omega_k^0}} \sin\left[ H_0  \sqrt{-\Omega_k^0} \int_0^z \frac{\dd z}{H(z)} \right] & \text{ si } k=+1 \\
    \displaystyle \int_0^z \frac{c\dd z}{H(z)}  & \text{ si } k=0 \\
    \displaystyle \frac{c}{H_0 \sqrt{\Omega_k^0}} \sh\left[ H_0  \sqrt{\Omega_k^0} \int_0^z \frac{\dd z}{H(z)} \right] & \text{ si } k=-1 \\
\end{array}
\right. 
.$$

On a donc obtenu un lien entre une mesure de distance obtenue par la mesure du flux $\Phi_0$ d'un astre, et un modèle cosmologique fonction de paramètres à déterminer. La mesure des flux d'objets de luminosité intrinsèque $L_E$ connue permet donc d'estimer les paramètres cosmologiques.

### Distances angulaires


:::{figure} ../../images/angular_distance.svg
:name: fig:angular_distance
:align: center
:width: 100%

Distance angulaire d'un objet de taille physique transverse $l$.
:::


Dernière distance importante en cosmologie, la distance angulaire d'un objet $D_A(z)$. Dans un espace statique et plat, l'angle apparent $\delta$ d'un objet de taille physique $l$ au repos à distance $D_A$ serait $l/D_A$. On propose donc de définir la distance angulaire $D_A(z)$ en cosmologie par :
$$
\delta = \frac{l}{D_A(z)}
$$

Comment cette distance se modélise dans la métrique FLRW? Soit un objet de taille transverse physique $l$ situé en $\sigma=\sigma_E,t=t_E$ et observé aujourd'hui en $\sigma=0,t=t_0$. 

Dans l'espace physique, l'angle $\delta$ est le même que dans l'espace comobile (on passe de l'un à l'autre par une homothétie), mais aussi le même à la réception et à l'émission. L'angle sous lequel est vu l'objet est donc dans tous les cas, et pour toute courbure (voir [](#fig:projection_polaire)) : 
$$
\delta = \frac{l}{a_E \sigma_E} = \frac{l (a_0/a_E)}{a_0 \sigma_E}  = \frac{l_c}{\sigma_E}
$$
avec $l_c = l / a_E$ la taille comobile de l'objet à l'émission $t_E$. On propose de définir la distance angulaire comobile ou distance transverse comobile simplement par :
$$d_A(z) = \frac{l_c}{\delta} = \sigma_E = \left\lbrace\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \sinh \chi(z) & \text{ si } k=-1 
\end{array}
\right. .$$
On en déduit aussi l'expression de la distance angulaire dans un univers courbe et en expansion, fonction des paramètres cosmologiques et du redshift :
$$
\Rightarrow D_A(z) \equiv\frac{l}{\delta} =  a(t_E) \sigma_E=\frac{a_0 \sigma_E}{1+z} = \frac{a_0}{1+z}d_A(z)=\frac{D_L(z)}{(1+z)^2}$$
$$D_A(z) = \frac{a_0}{1+z}
\left\lbrace
\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \sinh \chi(z) & \text{ si } k=-1 
\end{array}
\right.$$

$$D_A(z) = \frac{1}{1+z}
\left\lbrace
\begin{array}{cl}
    \displaystyle \dfrac{c}{H_0 \sqrt{-\Omega_k^0}} \sin\left[ H_0  \sqrt{-\Omega_k^0} \int_0^z \dfrac{\dd z}{H(z)} \right] & \text{ si } k=+1 \\
    \displaystyle \int_0^z \dfrac{c \dd z}{H(z)}  & \text{ si } k=0 \\
    \displaystyle \dfrac{c}{H_0 \sqrt{\Omega_k^0}} \sh\left[ H_0  \sqrt{\Omega_k^0} \int_0^z \dfrac{\dd z}{H(z)} \right] & \text{ si } k=-1 \\
\end{array}
\right. 
$$
D'après l'exercice [](#exo:sphere-comoving), on voit que l'usage de $\sigma$ au lieu de $\chi$ est bien adapté aux trois types de courbures d'Univers dans ces définitions des distances.

:::{note} Loi de Hubble-Lemaître

A bas redshift $z\ll 1$, on retrouve la loi de Hubble-Lemaître pour les trois courbures :
$$D_L(z) \approx \frac{cz}{H_0} \approx D_A(z)$$
avec $cz$ la vitesse apparente de récession par rapport à la Terre.

:::


:::{important} Les mesures des paramètres cosmologiques

Dans le cadre d'un Univers plat, les mesures angulaires réalisées par le satellite _Planck_ sur le fond diffus cosmologique, combinées aux mesures de flux des supernovae de type Ia, et les distances angulaires des oscillations acoustiques de baryons permettent d'inférer le contenu en matière et énergie noire pour un univers plat aujourd'hui ([](doi:10.1051/0004-6361/201833910)) :
$$
\label{eq:omegas_planck}
\Omega_m^0 = 0.3111 \pm 0.0056, \quad \Omega_\Lambda^0 = 0.6889 \pm 0.0056
$$

Si la courbure est un paramètre libre du modèle (on parle d'extension au modèle standard $\Lambda$CDM), on mesure :
$$
\Omega_k^0 = 0.0007\pm 0.0037
$$
ce qui est compatible avec un univers strictement plat[^flat], ou courbe mais avec avec un rayon de courbure très important puisque $\Omega_k^0 \approx k/a_0^2$.

Si on propose un modèle à deux paramètres pour l'énergie noire, on obtient ([](doi:10.1051/0004-6361/201833910)) :
$$
w_0 = −0.957 \pm 0.080, \quad w_a = −0.29^{+0.32}_{ −0.26}
$$ 

:::







:::{important} A retenir

- Le Principe Cosmologique implique que la matière doit être décrite comme un fluide parfait, et donc que ses transformations sont adiabatiques.

- L'évolution de l'Univers en fonction de son contenu en matière et de sa géoémtrie est codée dans les équations de Friedmann
\begin{equation*}
\left\lbrace
\begin{array}{l}
    \displaystyle{H^2 = \frac{8\pi \GN \rho}{3} + \frac{c^2 \Lambda}{3} - \frac{c^2 k}{a^2}},\\
    \displaystyle{2\dot{H} + 3H^2 = - \frac{8\pi \GN}{c^2 } P + c^2 \Lambda - \frac{c^2 k}{a^2}}.
\end{array}
\right.
\end{equation*}

- Ces deux équations contiennent l'équation de conservation du tenseur énergie-impulsion
\begin{equation*}
\dot{\epsilon} = -3 H(\epsilon + P). 
\end{equation*}

- On définit le paramètere d'équation d'état pour une composante $X$ de l'Univers comme le rapport de sa pression et de sa densité d'énergie $w_X = P_X/\epsilon_X$. Son paramètre de densité est $\Omega_X = \rho_X / \rho_c$ avec $\rho_c = 3H^2/8\pi\GN$ la densité critique.

- Les distances de luminosité et angulaire relie des observables physiques (flux lumineux et angles) aux propriétés intrinsèques de l'objet osbervé et à des distances intégrales de $1/H(a)$.

::: 


:::{seealso}  Pour approfondir

- Démontration de la structure des tenseurs de forme invariante : {cite:t}`Weinberg1972`[p. 392]

- Hydrodynamique en relativité : <wiki:Fluid_solution>

- Fluides imparfaits (visqueux) : {cite:t}`Weinberg1972`[p. 53], {cite:t}`Weinberg1971Fluids`,  {cite:t}`LandauFluids`

:::




[^vecj]: En électromagnétisme, la quantité de charge passant à travers une surface $\dd \vec S$ pendant une durée $\dd t$ est $\dd q = e n (\vec v \dd t)\cdot \dd \vec S$ avec $n$ la densité de particules: on définit alors le courant volumique de charge par $\vec j = e n \vec v$. La définition du courant volumique pour la quadri-impulsion (au lieu de la charge électrique) est identique.

[^pcphoton]: Pour une particule sans masse, on a directement $E_n = \vert \vec p_n \vert c$.

[^epsP]: Le choix des notations pour ces fonctions mathématiques n'a pas été fait par hasard...

[^flat]: On ne pourra _stricto sensus_ jamais mesuré que l'Univers est plat ($k=0$), mais que les mesures sont compatibles avec l'hypothèse d'un univers plat.

