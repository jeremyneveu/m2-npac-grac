---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---

L'Univers en expansion
======================

Dans le chapitre précédent, par de simples considérations géométriques, nous sommes parvenus à écrire la forme de la métrique solution de l'équation d'Einstein pour un Univers homogène et isotrope. D'un tenseur inconnu à 10 composantes (car la métrique est un tenseur symétrique), par des arguments de symétrie nous avons abouti à la métrique FLRW qui ne contient qu'une seule fonction inconnue $a(t)$. Pour maintenant décrire la dynamique de l'Univers, et non plus sa géométrie, il faut résoudre l'équation d'Einstein pour comprendre comment le contenu en matière et en énergie agit sur l'expansion l'Univers via le facteur d'échelle $a(t)$.


Le tenseur énergie-impulsion
----------------------------

Le tenseur énergie-impulsion $T^{\mu\nu}$ de l'équation d'Einstein décrit la densité d'énergie et les flux de quantités de mouvements en mécanique relativiste. C'est un tenseur d'ordre 2, construit à partir du vecteur 4-impulsion, qui prend la forme suivante :
\begin{equation}
T^{\mu\nu}=\begin{pmatrix} 
T^{00}= \text{energy density}\,\,\,\,
& cT^{01}=\text{energy flux  through }x_1=\text{cst}\,\,\,\,\,
& cT^{02}=\text{energy flux  through }x_2=\text{cst}\,\,\,\,\,
& cT^{03}=\text{energy flux through }x_3=\text{cst}
\\  T^{10}c^{-1}=\text{density of }p_1\,\,\,\,\,\,\,
& T^{11}= \text{flux of }p_1\text{ through }x_1=\text{cst}\,\,\,\,\,\,\,
&  T^{12}= \text{flux of }p_1\text{ through }x_2=\text{cst}\,\,\,\,\,\,\,
&  T^{13}= \text{flux of }p_1\text{ through }x_3=\text{cst}
\\  T^{20}c^{-1}=\text{density of }p_2\,\,\,\,\,\,\,
& T^{21}= \text{flux of }p_2\text{ through }x_1=\text{cst}\,\,\,\,\,\,\,
&  T^{22}= \text{flux of }p_2\text{ through }x_2=\text{cst}\,\,\,\,\,\,\,
&  T^{31}= \text{flux of }p_2\text{ through }x_3=\text{cst}
\\  T^{30}c^{-1}= \text{density of }p_3\,\,\,\,\,\,\,
& T^{31}= \text{flux of }p_3\text{ through }x_1=\text{cst}\,\,\,\,\,\,\,
&  T^{32}= \text{flux of }p_3\text{ through }x_2=\text{cst}\,\,\,\,\,\,\,
&  T^{33}= \text{flux of }p_3\text{ through }x_3=\text{cst}
\end{pmatrix}
\label{stress-energy-tensor-meaning}
\end{equation}

Or dans notre hypothèse d'Univers de symétrie maximale, rappelons tout d'abord qu'on peut définir un temps cosmique, universel,  en utilisant l'évolution de l'Univers comme une horloge (densité de matière, température du CMB...). Les hypersurfaces de l'espace-temps paramétrées par ce temps universel sont alors eux-mêmes des sous-espaces de symétrie maximale. Les tenseurs représentants des observables cosmologiques de tels sous-espaces de symétrie maximale doivent alors être de _forme invariante_ c'est-à-dire qu'ils doivent prendre les mêmes valeurs à une date $t$ quelque soit le choix du système de coordonnées choisi (si on passe de $x^\mu$ à $x'^\mu$, on doit retrouver $T_{\mu\nu} = T'_{\mu\nu}$ pour retrouver la même densité d'énergie) {cite:p}`Weinberg1972`[p. 408]. On peut démontrer alors une propriété importante concernant la forme que doivent prendre les tenseurs de ces sous-espaces {cite:p}`Weinberg1972`[p. 392].

:::{prf:property} Forme des tenseurs de forme invariante
Un tenseur de forme invariante dans un espace de symétrie maximale :
- est constant si c'est un scalaire,
- est nul si c'est un vecteur,
- est proportionnel au tenseur métrique si c'est un tenseur d'ordre 2.
:::

Par conséquent, mathématiquement on peut introduire $\epsilon(t)$ et $p(t)$ deux fonctions telles que le tenseur énergie-impulsion se simplifie en :
$$\begin{align}
T_{00} & =  \epsilon(t)\quad  \text{(scalaire)} \\
T_{i0} & = T_{0i} = 0 \quad  \text{(vecteur)} \\
T_{ij} & =  P(t) \gamma_{ij}\quad \text{(tenseur d'ordre 2)}
\end{align}$$

De manière plus élégante, on peut introduire le vecteur $U^\mu$ défini par :
$$ U^0 = 1, \quad U^i = 0 $$
et obtenir une écriture compacte pour le tenseur énergie-impulsion d'un Univers homogène et isotrope :
:::{math}
:label: eq:def-Tmunu2
T_{\mu\nu} = (\epsilon + P) U_\mu U_\nu + P g_{\mu\nu}
:::

:::{math}
:label: eq:def-Tmunu
T^{\mu\nu} = (\epsilon + P) U^\mu U^\nu + P g^{\mu\nu} = \begin{pmatrix}
-\epsilon g^{00} & 0 & 0 & 0 \\
0 & P g^{11} & 0 & 0 \\ 
0 & 0 & P g^{22} & 0 \\ 
0 & 0 & 0 & P g^{33}  \\ 
\end{pmatrix} 
:::

Comment interpréter ces considérations mathématiques ? Tout d'abord, si on compare l'équation [](#eq:def-Tmunu) avec [](#stress-energy-tensor-meaning) alors on identifie $\epsilon$
à la densité d'énergie et $p$ à la pression cinétique (flux de quantité de mouvement à travers une surface). Enfin, le tenseur énergie-impulsion $T^{\mu\nu}$ s'identifie à celui d'un <wiki:perfect_fluide>. Cela signifie que dans un Univers homogène et isotrope la matière peut être décrite comme un milieu continu, dont le mouvement peut être décrit sans prendre en compte des effets de viscosité et de conduction thermique (il est donc adiabatique). Aussi $U^\mu$ s'identifie alors à la 4-vitesse comobile du fluide, donc le fait que $U^i = 0$ montre que le système physique étudié est au repos dans les coordonnées comobiles, comme attendu. 

:::{note} Tenseur énergie-impulsion d'un fluide parfait {cite:p}`Weinberg1972`[p. 48]

Etudions un fluide parfait, c'est-à-dire un ensemble de particules dont le libre parcours moyen est petit devant les distances  auxquelles on l'étudie, et sans viscosité. Etant donné la définition d'un tenseur énergie-impulsion, dans le référentiel $\mathcal{R}'$ où
le fluide parfait est au repos on peut écrire :
$$ T'^{ij} = P \delta^{ij}, \quad T'^{i0} = T'^{0i} = 0, \quad T'^{00} = \rho c^2 $$
où explicitement $\rho$ est la densité _massique_ propre du fluide et $p$ sa pression cinétique (donc un flux de quantité de mouvement à travers une surface). Dans un autre référentiel, celui d'un observateur de l'écoulement par exemple, ce tenseur énergie-impulsion se réécrit :
$$ T^{\mu\nu} = \Lambda^{\mu}_{\;\alpha} \Lambda^{\nu}_{\;\beta} T^{\alpha\beta} $$
avec $\Lambda^\mu_{\;\alpha}$ la transformation de Lorentz définie par l'équation [](#eq:lorentz2). Plus explicitement :
$$ T^{ij} = P \delta^{ij} + (P + \rho c^2) \frac{v^i v^j}{c^2- v^2}, \quad T^{i0} = (P + \rho c^2) \frac{c v ^i}{c^2  - v^2}, \quad T^{00} = \frac{\rho c^4  + P v^2}{c^2  - v^2} $$
Définissons la quatre vitesse en coordonnées comobiles ainsi :
$$ \vec U =\frac{ \dd \vec x }{c \dd \tau} = \frac{\vec v / c }{ \sqrt{1-v^2}}, \quad U^0 = \frac{\dd t }{\dd  \tau} =  \frac{1 }{ \sqrt{1-v^2}}, \quad U_ \mu U ^\mu = -c^2  $$
alors le tenseur s'écrit :
$$T^{\mu\nu} = (\rho c^2 + P) U^\mu U^\nu + P \eta^{\mu\nu}$$

L'équation [](#eq:def-Tmunu) correspond donc bien à la définition d'un tenseur énergie-impulsion pour un fluide parfait dans le cadre relativiste.

Remarquons que dans un espace-temps plat, la conservation du tenseur énergie-impulsion d'un fluide parfait permet de retrouver l'équation de Navier-Stokes sans viscosité et sans forces extérieures, et l'équation de conservation de la matière. Pour simplifier, ramenons-nous au cas d'un fluide incompressible donc $\dd \rho / \dd t = 0$ et non relativiste donc $p / \rho c^2 \propto (v/c)^2 \ll 1$. Alors :
$$ 0 = \frac{\partial T^{\mu\nu}}{\partial x^\beta} \Rightarrow
\left\lbrace\begin{align*}
& \alpha = i:\ & 0 = & \vec\nabla P + \rho \frac{\partial \vec v}{\partial t} +  \rho (\vec v \cdot \vec\nabla)(\vec v)  \\
& \alpha = 0:\ & 0 = & \rho \vec \nabla \vec v + \frac{\partial \rho}{\partial t} 
\end{align*}\right.
$$

:::

Dans une base cartésienne, le tenseur énergie-impulsion prend la forme simple :
$$\label{eq:tmunu_fluide}
T_{\mu\nu}  =  \begin{pmatrix}
\epsilon & 0 & 0 & 0 \\
0 & P a^2(t) & 0 & 0 \\ 
0 & 0 & P a^2(t) & 0 \\ 
0 & 0 & 0 & P a^2(t)  \\ 
\end{pmatrix} .
$$


Les équations de Friedmann
---------------------------

Résoudre l'équation d'Einstein [](#eq:einstein2) consiste à en trouver une métrique solution, compte tenu de la répartition en matière et énergie codée dans $T^{\mu\nu}$. Supposer les principes d'homogénéité et d'isotropie pour ce tenseur, impose que la métrique est la métrique de Friedmann-Lemaître-Robertson-Walker (FLRW), utilisant le jeu de coordonnées comobiles sphériques usuel $(ct, \sigma, \theta, \phi)$:
$$\begin{aligned}\label{eq:flrw}
g_{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & \frac{a^2(t)}{1-k\sigma^2} & 0 & 0 \\ 
0 & 0 & a^2(t)\sigma^2 & 0 \\ 
0 & 0 & 0 & a^2(t) \sigma^2 \sin^2 \theta  \\ 
\end{pmatrix},\end{aligned}
$$ 
où $a(t)$ est une fonction inconnue. Le paramètre d'échelle $a(t)$ peut être obtenu en résolvant l'équation d'Einstein connaissant le contenu du tenseur énergie-impulsion de l'Univers $T^{\mu\nu}$ et la valeur de $k$. Pour la métrique FLRW, son inverse est simplement:
$$
g^{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & \frac{1-k\sigma^2}{a^2(t)} & 0 & 0 \\ 
0 & 0 & \frac{1}{a^2(t)\sigma^2}  & 0 \\ 
0 & 0 & 0 & \frac{1}{a^2(t) \sigma^2 \sin^2 \theta}   \\ 
\end{pmatrix}.
$$

En utilisant la métrique FLRW
[](#eq:flrw),
calculons pour l'exemple la connexion affine suivante à partir de l'équation [](#eq:connexion):
$$\begin{aligned}
\Gamma^1_{\ 01} & = \frac{1}{2} g^{1 \mu} \left( \partial_0 g_{1\mu} + \partial_1 g_{0 \mu} - \partial_\mu g_{01} \right) \\
& = \frac{1}{2} g^{1 1} \left(\frac{\partial g_{11}}{c\partial t} + \partial_\sigma g_{01} - 0 \right) \text{ car }\forall \mu \neq 1, g^{1\mu}=0\\
& = \frac{1}{2} \frac{1-k\sigma^2}{a^2} \left( \frac{2 \dot{a} a}{c(1-k\sigma^2)} + 0 \right) \\
& = \frac{\dot a}{ca} = \frac{H}{c}.
\end{aligned}$$


De la même manière, on obtient les autres connexions affines, puis les tenseurs de Riemann et Ricci. Au final, le tenseur d'Einstein est diagonal et vaut: 
$$\begin{aligned}
G_{00} & =  - 3 \left( \frac{\dot{a}^2}{c^2 a^2}+ \frac{k}{a^2} \right), \\
G_{ij} & = \frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{c^2 a^2}g_{ij} \text{ pour } i=j\neq 0.
\end{aligned}$$
A partir de l'équation d'Einstein [](#eq:einstein2) et du tenseur énergie-impulsion [](#eq:tmunu_fluide), on obtient pour la coordonnée $00$ et pour les coordonnées spatiales $ij$: 
$$\begin{aligned}
G_{\mu\nu}-\Lambda g_{\mu\nu} & = -8\pi G_N T_{\mu\nu}/c^4 \\
\Leftrightarrow  & \left\lbrace
\begin{array}{rl}
    \text{00: } &  \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{c^2 k}{a^2} \right) = 8\pi G_N \rho + c^2 \Lambda} \\
    ij\text{: } &   \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{a^2} = - \frac{8\pi G_N}{c^2 } P + c^2 \Lambda }
\end{array}
\right.\end{aligned}$$ 
Ce sont les deux équations de Friedmann. Les voici maintenant exprimées en fonction du paramètre de Hubble
$H=\dot{a}/a$ : 
$$\label{eq:friedmann}
\left\lbrace
\begin{array}{rl}
    \text{00: } & \displaystyle{H^2 = \frac{8\pi G_N \rho}{3} + \frac{c^2 \Lambda}{3} - \frac{c^2 k}{a^2}}\\
    ij\text{: } &  \displaystyle{2\dot{H} + 3H^2 = - \frac{8\pi G_N}{c^2 } P + c^2 \Lambda - \frac{c^2 k}{a^2}}
\end{array}
\right.
$$
La première équation de Friedmann relie explicitement l'évolution du facteur d'échelle $a(t)$ au contenu énergétique de  l'Univers. De plus, en soustrayant ces deux équations et en combinant le résultat avec la dérivée temporelle de la première, on peut obtenir l'équation de conservation de l'énergie que l'on obtiendrait aussi directement en calculant $T^{\mu\nu}_{\;\;\;;\mu}=0$ dans la métrique FLRW : 
$$\label{eq:conservation_energie}
\fbox{$\dot{\epsilon} = -3 H( \epsilon  + P )$}
$$

:::{exercise}

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


Show that $\Gamma^0_{\ ij} = \dot{a}a/c \delta_{ij}$ and $\Gamma^j_{\ 0i}=\dot{a}/(ac)\delta^j_i$, with the latin index standing for the spatial coordinates $i=1,2,3$. The other Christoffel symbols are null.

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


Show that $R_{00}=3\ddot{a}/(ac^2)$ and $R_{ij}=-(\ddot{a}a+2\dot{a}^2)\delta_{ij}/c^2$.

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

Show that $R=-6\left(\ddot{a}/a+(\dot{a}/a)^2\right)/c^2$ and finally that $G_{\mu\nu}=R_{\mu\nu}-g_{\mu\nu}R/2$ is:
\begin{equation}
G_{\mu\nu}={1 \over c^2}\begin{pmatrix} 3{\dot{a}^2\over a^2} & 0 & 0 & 0 \\ 0 &-2\ddot{a}a-\dot{a}^2 & 0 & 0 \\ 0&0& -2\ddot{a}a-\dot{a}^2 &0 \\ 0&0&0&-2\ddot{a}a-\dot{a}^2  \end{pmatrix}
\label{Einstein-cosmo-tensor}
\end{equation}

From the Einstein equation $G_{\mu\nu} - \Lambda g_{\mu\nu} = -8\pi G T_{\mu\nu}/c^4$ write the Friedmann equations:
\begin{equation} \left\lbrace
\begin{array}{l}
   \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{c^2k}{a^2} \right) = 8\pi G_N \rho + c^2 \Lambda} \\
    \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{a^2} = - 8\pi G_N P/c^2 + c^2 \Lambda }
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
G_{\mu\nu} - \Lambda g_{\mu\nu}  = -\frac{8\pi G_N}{c^4}T_{\mu\nu}
\end{equation}
\begin{align}
\label{Friedmann1}
3{\dot{a}^2 \over a^2}&=& 8 \pi G_N \rho + c^2 \Lambda\\
2{\ddot{a} \over a} + {\dot{a}^2 \over a^2}& =& - {8 \pi G_N \over c^2}P + c^2 \Lambda
\label{align}
\end{align}


Write the two Friedmann equations in term of the Hubble parameter $H=\dot{a}/a$ instead of $a$.
\begin{equation} \left\lbrace
\begin{array}{l}
   \displaystyle{3 H^2+ \frac{3kc^2}{a^2} = 8\pi G_N \rho + c^2\Lambda} \\
    \displaystyle{2\dot{H} + 3H^2 + \frac{c^2k}{a^2} = - 8\pi G_N P/c^2 + c^2\Lambda }
\end{array}
\right.
\end{equation}
using $\ddot{a}/a=\dot{H}+H^2$. 

From the two Friedmann equations, find the energy conservation equation law $\dot{\rho} c^2 = -3 H(\rho c^2 + p )$.

\begin{align}
8\pi G \dot{\rho} & = 6\dot{H}H - \frac{6c^2 k \dot{a}}{a^3} \\
& = 3H \left[-8\pi G_N P / c^2 + c^2 \Lambda - 3 H^2 - \frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi G_N P / c^2 -8 \pi G_N \rho + 2\frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi G_N P / c^2 -8 \pi G_N \rho \right]
\end{align}
and $\dot{\rho} c^2 = -3 H(\rho c^2 + p )$. 
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
$$ \dd(a^3 \epsilon) = - P \dd (a^3) + T \dd S \Rightarrow 3 \dot{a} a^2 \epsilon + a^3 \dot{\epsilon} = - 3 p \dot{a} a^2  + T \frac{\dd S}{\dd t}\Rightarrow \dot{\epsilon} = -3\frac{\dot{a}}{a}(p+\epsilon) +T \frac{\dd S}{\dd t} $$
Donc 
$$\frac{\dd S}{\dd t} = 0$$
et l'expansion est isentropique. C'est attendu étant donné que pour un Univers homogène et isotrope le tenseur énergi-impulsion est celui d'un fluide parfait donc sans viscosité ni transfert de chaleur.
:::




Inventaire cosmologique
-----------------------

Le tenseur énergie-impulsion inclut la matière non-relativiste et relativiste. La matière relativiste est généralement nommée rayonnement car aujourd'hui le rayonnement de photons du CMB est largement dominant dans cette composante. 

### Matière

La matière non relativiste n'exerce pas de pression donc 
$$P_m=0,$$
et : 
$$
\label{eq:conservation_energie_matiere}
\dot{\rho}_m = -3 H\rho_m \Rightarrow \rho_m = \rho_m^0 \left(\frac{a_0}{a}\right)^{3}.
$$
Cette  dernière relation traduit bien le fait que si une boîte de côté $a$ contenant une certaine quantité de matière voit la longueur de ses côtés doubler, alors la densité de matière est bien divisée par $2^3$. 

### Photons et neutrinos

Pour la matière relativiste (photons, neutrinos), 
$$P_r =  \frac{1}{3} \epsilon_r,$$
donc :
$$\label{eq:conservation_energie_radiation}
\dot{\epsilon}_r = -4 H\epsilon_r \Rightarrow \epsilon_r = \epsilon_r^0 \left(\frac{a_0}{a}\right)^{4}.
$$ 
Le raisonnement avec une boîte cubique de côté $a$ s'applique aussi ici, mais si toutes les longueurs doublent, alors la longueur d'onde du rayonnement aussi donc son énergie est divisée par 2. On retrouve bien une diminution de la densité d'énergie de rayonnement en $2^4$.


:::{note} Equation d'état du gaz parfait
Pour un gaz parfait, on rappelle que l'équation d'état est :
$$ P = \rho_n k_B T  $$
avec $T$ sa température, $\rho_n$ la densité particulaire et $k_B$ la constante de Boltzmann.
S'il est à basse température (i.e. non relativiste) alors on a $\epsilon \approx m c^2 \rho_n$ et on veut $P / \epsilon = k_B T \ll 1/3$ soit :
$$ T \ll m c^2 / 3 k_B $$
Pour un gaz d'hydrogène, $T \ll 10^{12}\,$K. Donc on voit que la matière telle qu'on la connait est non relativiste aujourd'hui et même bien avant le CMB.

:::


:::{note} Hypothèse de non interaction

Nous avons utilisé l'équation [](#eq:conservation_energie) pour en déduire que la matière non relativiste possède une densité qui évolue en $a^{-3}$ alors que la matière relativiste évolue en $a^{-4}$. Le lecteur attentif aura peut-être remarqué que la densité et la pression de l'équation [](#eq:conservation_energie) sont pourtant la somme des densités et pressions relativistes et non relativistes. Est-ce que dans un Univers possédant ces deux composantes les équations [](#eq:conservation_energie_matiere)et [](#eq:conservation_energie_radiation) sont-elles encore valables ?

L'équation [](#eq:conservation_energie) peut se déduire d'un raisonnement thermodynamique qui peut nous être utile ici. L'expansion de l'Univers étant adiabatique, la variation d'entropie liée à l'expansion est nulle donc $\dd S = 0$. Le premier principe de la thermodynamique sur un volume $V$ d'Univers donne :
$$\label{eq:conservation_energie_thermo}
\dd U = -P \dd V + T \dd S \Leftrightarrow \dd \left(\epsilon_m V + \epsilon_r V  \right) = -\frac{1}{3}\epsilon_r \dd V$$
Si les deux composantes n'interagissent pas entre elles, alors cette dernière équation peut se scinder en ses deux composantes,  comme deux systèmes thermodynamiques indépendants :
$$\dd \left(\epsilon_m V\right) = 0, \quad \dd \left(\epsilon_r V  \right) = -\frac{1}{3}\epsilon_r \dd V$$
Si elles interagissaient, ceci ne serait pas vrai. De ceux deux équations, on en déduit de nouveau les équations [](#eq:conservation_energie_matiere) et [](#eq:conservation_energie_radiation).

:::




### Constante cosmologique

Dans les équations de Friedmann [](#eq:friedmann), il est possible d'interpréter la constante cosmologique $\Lambda$ et la courbure $k$ en terme de densités d'énergie au même titre que la densité d'énergie $\rho$ du tenseur énergie-impulsion. 

La densité d'énergie associée à la constante cosmologique est parfois appelée densité d'énergie noire, en raison des étranges propriétés associées à cette dernière :
$$\epsilon_\Lambda(t) = \rho_\Lambda c^2 =  \frac{c^4 \Lambda}{8\pi G_N} = \text{ constante }.$$ 
On voit que la densité d'énergie associée à la constante cosmologique étant constante dans le temps, cette dernière possède un comportement bien singulier : quelque soit la taille de l'Univers, il y a toujours autant d'énergie par unité de volume. Elle n'est donc pas diluée comme toute énergie ordinaire lorsque celui-ci est en expansion. De plus, grâce à la seconde équation de Friedmann, on voit que la pression associée à la constante cosmologique serait 
$$P_\Lambda = - \epsilon_\Lambda,$$
soit une pression négative ! Dans la physique ordinaire, un des rares phénomènes où interviennent des pressions négatives est la cavitation (<wiki:Pressure#Negative_pressures). En posant $\rho_{\mathrm{tot}}=\rho + \rho_\Lambda$ (et $p_{\mathrm{tot}}=p + p_\Lambda$) puis en combinant les deux équations de Friedmann [](#eq:friedmann) de façon à éliminer le terme de courbure, on  obtient :
\begin{equation}\label{eq:ddota}
2\dot{H} + 2H^2 = \frac{2\ddot{a}}{a} = -\frac{8\pi G_N}{3}\left( \epsilon _{\mathrm{tot}} + 3P_{\mathrm{tot}}\right).
\end{equation}
On constate que l'expansion de l'Univers s'accélère ($\ddot{a}>0$) si
$P_{\mathrm{tot}}<-\epsilon_{\mathrm{tot}}/3$. L'Univers étant constitué
essentiellement de matière non relativiste et de rayonnement, la condition précédente devient équivalente à 
$$
\ddot{a} > 0 \Leftrightarrow \epsilon_\Lambda > \epsilon_r + \epsilon_m/2$$
En conclusion, si la constante cosmologique domine le contenu en énergie de l'Univers, alors elle engendre une telle pression négative que ce dernier entre en _expansion accélérée_.

:::{note} Quelle unité pour $\Lambda$ ?

Comme $\epsilon_\Lambda$ est une densité d'énergie, on en déduit que $\Lambda$ a la dimension de l'inverse du carré d'une longueur. Pour résumé,
$$\label{eq:dimensions}
\left[a\right] = \mathsf{L},\quad \left[\rho \right] = \mathsf{M}\cdot \mathsf{L}^{-3}, \quad \left[\epsilon \right] = \left[p \right] = \mathsf{M}\cdot \mathsf{L}^{-1} \cdot \mathsf{T}^{-2}\quad \left[\Lambda \right] = \mathsf{L}^{-2} $$
$$\left[ g_{\mu\nu} \right] = [1,\mathsf{L}^{2},\mathsf{L}^{2},\mathsf{L}^{2}] $$
:::


### Courbure


La densité d'énergie associée à l'énergie de courbure s'identifie à : 
$$\epsilon_k(t) =\rho_k(t) c^2 = - \frac{3 c^4 k  }{8\pi G_N a^2(t)}.$$
De même, son effet en terme de pression est :
$$P_k = \frac{c^4 k}{8\pi G_N a^2(t)}.$$

Les paramètres cosmologiques
----------------------------

### Paramètres d'équation d'état


L'équation d'état $w$ associée à une composante de l'Univers est définie par le rapport de sa pression et de sa densité d'énergie
$$\label{eq:def-w}
\fbox{$w=P/\epsilon.$}
$$

-   La matière froide non relativiste n'exerce pas de pression sur son milieu
    extérieur d'où $P_m=0$ donc $w_m=0$.

-   La matière relativiste exerce quant à elle une pression sur son
    milieu de valeur $P_r =  \epsilon_r / 3 $ d'où $w_r=1/3$.

-   Pour la constante cosmologique, on a $p_\Lambda = - \epsilon_\Lambda$ donc son équation d'état est
    constante et négative $w_\Lambda = -1$.

-   La courbure assimilée à un fluide parfait aurait un paramètre d'équation d'état $w_k=1/3$.


### Paramètres de densité d'énergie

On peut définir une densité critique, qui correspondrait à la densité que l'on doit avoir dans un univers homogène et isotrope en expansion de courbure spatiale nulle (cf équation [](#eq:friedmann)) : 
$$\rho_c(t) = \frac{3H^2(t)}{8\pi G_N}.$$ 
Il est commode de définir aussi sa valeur actuelle :
$$\rho_{c}^0 = \frac{3H^2_0}{8\pi G_N} = 1.1 \times 10^{-29} \left( \frac{H_0}{75\text{ km/s/Mpc}}\right)^2\text{ g/cm}^3 \approx 6 \text{ protons/m}^3.$$
où $H_0$ est la constante de Hubble.

On définit les paramètres de densité (sans dimension) en normalisant les densités d'énergie par la densité critique, soit :
$$\Omega_m(t) = \frac{\rho_m(t)}{\rho_c(t)},\quad \Omega_\Lambda(t) = \frac{c^2 \Lambda}{3H^2(t)}, \quad \Omega_k(t) = -\frac{c^2 k}{a^2(t)H^2(t)}$$
$$\Omega_m^0 = \frac{\rho_m^0}{\rho_c^0},\quad \Omega_\Lambda^0 = \frac{c^2 \Lambda}{3H^2_0}, \quad \Omega_k^0 = -\frac{c^2 k}{a_0^2 H^2_0}.$$
La première équation de Friedmann s'écrit alors simplement :
$$\label{eq:omega_sum}
1 = \Omega_m(t) + \Omega_r(t) + \Omega_\Lambda(t) + \Omega_k(t)
$$

```{math}
:label: eq:friedmann2
\bar H^2 (t) \equiv \frac{H^2(t)}{H_0^2} = \Omega_m^0 \left(\frac{a_0}{a(t)}\right)^{3} + \Omega_r^0 \left(\frac{a_0}{a(t)}\right)^{4} + \Omega_\Lambda^0 +  \Omega_k^0 \left(\frac{a_0}{a(t)}\right)^{2}.
```
Ce modèle d'Univers liant la prédiction de son expansion $\bar H(z)$ à son contenu composé d'une constante cosmologique, de matière et de radiation, est appelé modèle $\Lambda$CDM ($\Lambda$ pour la constante cosmologique et CDM pour *Cold Dark Matter*) dans le cas $k=0$ (Univers plat). C'est le modèle standard de la cosmologie.

Dans le cadre d'un Univers plat, les valeurs mesurées par le satellite _Planck_  combinées aux supernovae de type Ia et les oscillations acoustiques de baryons donnent [](doi:10.1051/0004-6361/201833910) :
$$\label{eq:omegas_planck}
\Omega_m^0 = 0.3111 \pm 0.0056, \quad \Omega_\Lambda^0 = 0.6889 \pm 0.0056$$ pour un Univers plat. Si la courbure est un paramètre libre (on parle d'extension au modèle standard $\Lambda$CDM), on mesure :
$$\Omega_k^0 = 0.0007\pm 0.0037$$
donc l'Univers semble essentiellement plat.

### Modélisations de l'énergie noire

Quelle est la véritable nature de l'énergie noire ? Est-ce la manifestation de l'énergie du vide ? Une seconde constante fondamentale de la gravitation ?
Ou bien une nouvelle cinquième force ? La manifestation de dimensions spatiales supplémentaires ? Ces questions sur la nature
de l'énergie noire n'ont pour le moment pas de réponses, mais depuis la découverte de l'expansion accélérée en 1998 {cite:p}`Riess1998,Perlmutter1999`
de nouveaux relevés cosmologiques sont en cours pour mesurer précisément l'équation d'état de l'énergie noire $w_{DE}$ : tant qu'on mesure
$w_{DE} = w_\Lambda=-1$ alors l'accélération de l'expansion peut s'expliquer avec un unique paramètre qui est la valeur de $\Lambda$. 
Si les mesures s'écartent significativement de $-1$, alors des modèles plus complexes seront à tester.

C'est pourquoi aujourd'hui, en plus du modèle standard $\Lambda$CDM, les cosmologistes testent des modèles empiriques qui cherchent des écarts au modèle standard :
- Flat $w$CDM : modèle d'Univers plat avec comme paramètres  libres $\Omega_m^0$, $\Omega_r^0$ et $w_{DE}$;
- $w$CDM : modèle de courbure quelconque avec comme paramètres  libres $\Omega_m^0$, $\Omega_r^0$, $\Omega_\Lambda^0$ et  $w_{DE}$;
- $w_0w_a$CDM : modèle où le paramètre d'équation d'état de l'énergie noire est donnée par deux paramètres libres :
$$w_{DE}(a) = w_0 + \left(1 - \frac{a}{a_0}\right)w_a$$
dont les valeurs mesurées par le satellite _Planck_ combinées aux supernovae de type Ia et les oscillations acoustiques de baryons donnent [](doi:10.1051/0004-6361/201833910):
$$w_0 = −0.957 \pm 0.080, \quad w_a = −0.29^{+0.32}_{ −0.26}$$ 
L'enjeu majeur pour les relevés cosmologiques futurs est de mesurer $w_a$ avec une meilleure précision, afin de mesurer les variations de l'accélération de l'expansion de l'Univers.



:::{exercise} Evolution des densités d'énergie et interprétation
:label: exo:rhos

1. Démontrer la formule [](#eq:conservation_energie).
2. Trouver l'évolution de la densité de matière $\rho_m$ en fonction de $a$. Même question pour la densité de rayonnement $\rho_r$. 
On rappelle que $P_m=0$ pour la matière non relativiste et $P_r=\epsilon_r/3$ pour le rayonnement.
3. A partir d'un raisonnement sur un cube comobile qui se dilate, avec des arguments physiques sur des nombres de galaxies,
retrouvez le même résultat.
4. Pour un fluide parfait dont l'équation d'état $w$ est constante ($P=w\rho c^2$), donner l'évolution de sa densité d'énergie.
5. Identifier le terme $\Lambda g_{\mu\nu}$ avec le tenseur énergie-contrainte d'un fluide parfait. Trouver la densité d'énergie $\rho_\Lambda$ 
et la pression $P_\Lambda$ exercées par la constante cosmologique ainsi que son équation d'état.
6. À partir de ces dernières questions, réfléchissez au comportement de la densité d'énergie liée au vide. Considérons une chambre à piston cylindrique de section $A$ "remplie" d'énergie du vide. Le piston est tiré sur une distance linéaire $\dd x$.  Montrez que l'énergie créée par le retrait du piston est égale au travail effectué par le vide, à condition que :
\begin{equation}
 p_{\rm vac} = - \rho_{\rm vac} c^2 
 \end{equation} % voir Hobson exo piston 15,5 p422
Cette équation d'état du vide peut être établie à l'aide de la théorie quantique des champs. Elle montre donc que, dans ce cas, la densité d'énergie du vide est constante lorsque le piston se retire.

:::

:::{solution} exo:rhos
:class: dropdown

1. \begin{align}
8\pi G_N \dot{\rho} & = 6\dot{H}H - \frac{6c^2 k \dot{a}}{a^3} \\
& = 3H \left[-8\pi G_N P / c^2 + c^2 \Lambda - 3 H^2 - \frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi G_N P / c^2 -8 \pi G \rho + 2\frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi G_N P / c^2 -8 \pi G \rho \right]
\end{align}
et $\dot{\rho} c^2 = -3 H(\rho c^2 + P )$. 


2. En utilisant la définition du paramètre de Hubble $H = (\dd a/\dd t)/a$, nous pouvons transformer les dérivées temporelles en dérivées par rapport au facteur d'échelle $a$ (ou décalage vers le rouge $z$) :
\begin{equation}
\frac{\dd}{\dd t}=Ha\frac{\dd}{\dd a}
\end{equation}
La formule de conservation de l'énergie se transforme en :
\begin{equation}
a\frac{\dd\rho}{da} = -3 (\rho c^2 + P)
\end{equation}
En ce qui concerne la matière non relativiste, $P_m=0$ donc :
\begin{equation}
\frac{\dd\rho_m}{\rho_m} = -3 \frac{\dd a}{a} \Rightarrow \rho_m(a) = \rho_m^0 \left(\frac{a_0}{a}\right)^3
\end{equation}
En ce qui concerne le rayonnement, $P_r=\rho_r c^2 / 3$ donc :
\begin{equation}
\frac{\dd\rho_r}{\rho_r} = -4 \frac{\dd a}{a} \Rightarrow \rho_r(a) = \rho_r^0 \left(\frac{a_0}{a}\right)^4
\end{equation}


3. 
```{list-table} Conservation de l'énergie pour la matière et le rayonnement dans un univers en expansion.
:header-rows: 0
:name: fig:cubes

* - ```{image} ../images/cube_galaxies.svg
    :alt: galaxies
    :width: 100%
    :align: center
    ```
  - ```{image} ../images/cube_waves.svg
    :alt: light
    :width: 100%
    :align: center
```

Dans le cube isolé, l'énergie et la matière se conservent. Ainsi, en ce qui concerne les galaxies présentes dans un cube en expansion, nous pouvons écrire que leur nombre est conservé par l'expansion de la manière suivante :
\begin{equation}
N_{\rm gal} = \rho_m^0 a_0^3 = \rho_m(a) a^3 \Rightarrow \rho_m(a) = \rho_m^0 \left(\frac{a_0}{a}\right)^3
\end{equation}
Considérons une onde électromagnétique dans un cube en expansion. La longueur d'onde physique $\lambda$ augmente mais la longueur d'onde en coordonnées $\lambda/a$ est conservée. La conservation de l'énergie de rayonnement dans un cube en mouvement s'écrit :
\begin{equation}
a_0 \frac{h c}{\lambda_0} = a \frac{h c}{\lambda}
\end{equation}
La densité d'énergie est alors
\begin{equation}
\rho_r(a) = \frac{(hc/\lambda)}{a^3} = \frac{a_0(hc/\lambda_0)}{a^4} = \rho_r^0 \left(\frac{a_0}{a}\right)^4
\end{equation}
Le comportement en $a^{-4}$ est donc dû à la dilatation de la longueur d'onde du photon.

4. On montre que
\begin{align}
\dot{\rho}c +3\frac{\dot{a}}{ac}(\rho c^2+P)=0 & \Leftrightarrow \dot{\rho}c =-3\frac{\dot{a}}{ac}(1+w)\rho c^2=0 \\
& \Leftrightarrow \frac{d\rho}{\rho} = -3(1+w) \frac{da}{a} \\
& \Rightarrow \rho = \rho_0 \left( \frac{a}{a_0}\right)^{-3(1+w)}
\end{align}

5. En utilisant l'équation d'Einstein, en passant le terme $\Lambda$ du côté du tenseur énergie-contrainte de l'équation, nous identifions cette contribution comme un fluide parfait :
\begin{equation}
\Lambda g_{\mu\nu} = \frac{8\pi G_N}{c^4} \begin{pmatrix} \rho_\Lambda c^2 & 0 & 0 & 0 \\ 0 &a^2 p_\Lambda & 0 & 0 \\ 0&0&a^2 p_\Lambda &0 \\ 0&0&0&a^2 p_\Lambda \end{pmatrix}
\end{equation}
Nous obtenons :
\begin{align}
\Lambda & = \frac{8\pi G_N}{c^4} \rho_\Lambda c^2 \Leftrightarrow \rho_\Lambda c^2 = c^4 \Lambda / 8\pi G_N \\
-a^2 \Lambda & = \frac{8\pi G_N}{c^4} a^2 P_\Lambda \Leftrightarrow p_\Lambda = - c^4 \Lambda / 8 \pi G_N = - \rho_\Lambda c^2
\end{align}
Pour la constante cosmologique, l'équation d'état est constante et sa valeur est $w=-1$. En utilisant la question précédente, nous avons :
\begin{equation}
\rho = \rho_0 \left( \frac{a}{a_0}\right)^{-3(1+w)} = \rho_0
\end{equation}
La densité d'énergie associée à la constante cosmologique est constante tout au long de l'expansion de l'univers.

6. L'énergie créée par le retrait du piston est :
\begin{equation}
\dd U = \dd\left(\rho_{\rm vac} c^2 V\right) = c^2 V \dd\rho_{\rm vac} + \rho_{\rm vac} c^2 \dd V
\end{equation}
Pour une transformation adiabatique, le premier principe de la thermodynamique donne :
\begin{equation}
\dd U = \delta W = -P_{\rm vac} \dd V
\end{equation}
En supposant que $P_{\rm vac}= - \rho_{\rm vac} c^2$, pour la densité d'énergie du vide nous avons $d\rho_{\rm vac} = 0$ et le premier principe $ dU = \delta W$ est vérifié.


Absence of a preferred reference frame (i.e. the Relativity principle) means that the energy-momentum tensor for vacuum T(vac)μν=diag(ρ,p,p,p) is the same for every observer. There is only one tensor of rank 2 which is invariant with respect to Lorentz transformations---it is the unit tensor ημν=diag(1,−1,−1,−1). That is why the Lorentz-invariant energy-momentum tensor must be proportional to the metric and therefore
pvac=−ρvac.

:::


:::{exercise} Ordres de grandeur
:label: exo:densities

Transformer les valeurs de l'équation [](#eq:omegas_planck) en densité de masse et en densité d'énergie.

:::


:::{solution} exo:densities

Suppose that density of the dark energy as cosmological constant is equal to the present critical density, ρΛ=ρcr. What is then the total amount of dark energy inside the Solar System? Compare this number with M⊙c2

ρcr≃10−29  g/cm3;R≃50a.u.;1 a.u.≃1.5×1011m;EDESS/c2≃0.2⋅1014 kg;M⊙≃2⋅1030 kg;EDESSM⊙c2≃10−17.

Transform Lambda into a length: Length = sqrt(1/Lambda) = ....

:::



