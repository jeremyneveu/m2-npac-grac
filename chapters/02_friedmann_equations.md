---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---

L'Univers en expansion
======================

Dans le chapitre précédent, par de simples considérations géométriques, nous sommes parvenus à écrire la forme de la métrique solution de l'équation 
d'Einstein pour un Univers homogène et isotrope. D'un tenseur inconnu à 10 composantes (car la métrique est un 
tenseur symétrique) nous avons abouti à la métrique FLRW qui ne contient qu'une seule fonction inconnue $a(t)$. 
Pour maintenant décrire la dynamique de l'Univers, et non plus sa géométrie, il faut résoudre l'équation d'Einstein pour comprendre comment
le contenu en matière et en énergie agit sur l'expansion l'Univers via le facteur d'échelle $a(t)$.


Le tenseur énergie-impulsion
----------------------------

Le tenseur énergie-impulsion $T^\mu\nu$ de l'équation d'Einstein décrit la densité d'énergie et les flux de quantités de mouvements en mécanique relativiste. C'est un tenseur d'ordre 2, construit à partir du vecteur 4-impulsion, qui prend la forme suivante :
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

Or dans notre hypothèse d'Univers de symétrie maximale, on peut démontrer deux propriétés importantes concernant les vecteurs et les tenseurs d'ordre 2 {cite:p}`Weinberg1972`[p. 392].

:::{prf:property} Symétrie des tenseurs d'ordre 2
Dans un espace de symétrie maximale, les tenseurs d'ordre 2 de forme invariante par une isométrie de l'espace sont proportionnels au tenseur métrique.
:::

Par conséquent, mathématiquement on peut introduire $\rho(t)$ et $p(t)$ deux fonctions telles que le tenseur énergie-impulsion se simplifie en :
$$ T_{tt} =  \rho(t) c^2, \quad T_{it} = 0, \quad T_{ij} =  p(t) \gamma_{ij}$$
De manière plus élégante, on peut introduire le vecteur 4-vitesse $U^\mu$ comobile défini par :
$$ U^t = 1, \quad U^i = 0 $$
et obtenir une écriture compacte pour le tenseur énergie-impulsion d'un Univers homogène et isotrope :
:::{math}
:label: eq:def-Tmunu
T_{\mu\nu} = (\rho c^2 + p) U_\mu U_\nu + p g_{\mu\nu} 
:::

Comment interpréter ces considérations mathématiques ? Tout d'abord, le fait que $U^i = 0$ montre que le système physique étudié est au repos dans les coordonnées comobiles, 
comme attendu. Puis si on compare l'équation [](#eq:def-Tmunu) avec [](#stress-energy-tensor-meaning) alors on identifie $\rho$
à la densité d'énergie et $p$ à la pression cinétique (flux de quantité de mouvement à travers une surface).
Enfin, le tenseur énergie-impulsion $T^{\mu\nu}$ s'identifie à celui d'un <wiki:perfect_fluide>. Cela signifie que dans un Univers homogène
et isotrope la matière peut être décrite comme un milieu continu, dont le mouvement peut être décrit sans prendre en compte
des effets de viscosité et de conduction thermique (il est donc adiabatique).

:::{note} Tenseur énergie-impulsion d'un fluide parfait {cite:p}`Weinberg1972`[p. 48]

Etudions un fluide parfait, c'est-à-dire un ensemble de particules dont le libre parcours moyen est petit devant les distances 
auxquelles on l'étudie, et sans viscosité. Etant donné la définition d'un tenseur énergie-impulsion, dans le référentiel $\mathcal{R}'$ où
le fluide parfait est au repos on peut écrire :
$$ T'^{ij} = p \delta^{ij}, \quad T'^{i0} = T'^{0i} = 0, \quad T'^{00} = \rho c^2 $$
où explicitement $\rho$ est la densité d'énergie propre du fluide et $p$ sa pression cinétique (donc un flux de quantité de mouvement à travers une surface).
Dans un autre référentiel, celui d'un observateur de l'écoulement par exemple, ce tenseur énergie-impulsion se réécrit :
$$ T^{\mu\nu} = \Lambda^{\mu}_{\;\alpha} \Lambda^{\nu}_{\;\beta} T^{\alpha\beta} $$
avec $\Lambda^\mu_{\;\alpha}$ la transformation de Lorentz définie par l'équation [](#eq:lorentz2). Plus explicitement :
$$ T^{ij} = p \delta^{ij} + (p + \rho c^2) \frac{v^i v^j}{c^2- v^2}, \quad T^{i0} = (p + \rho c^2) \frac{c v ^i}{c^2  - v^2}, \quad T^{00} = \frac{\rho c^4  + p v^2}{c^2  - v^2} $$
Définissons la quatre vitesse en coordonnées comobiles ainsi :
$$ \vec U =\frac{ \dd \vec x }{c \dd \tau} = \frac{\vec v / c }{ \sqrt{1-v^2}}, \quad U^0 = \frac{\dd t }{\dd  \tau} =  \frac{1 }{ \sqrt{1-v^2}}, \quad U_ \mu U ^\mu = -c^2  $$
alors le tenseur s'écrit :
$$T_{\mu\nu} = (\rho c^2 + p) U_\mu U_\nu + p \eta_{\mu\nu}$$

L'équation [](#eq:def-Tmunu) correspond donc bien à la définition d'un tenseur énergie-impulsion pour un fluide parfait dans le cadre relativiste.

Remarquons que dans un espace-temps plat, la conservation du tenseur énergie-impulsion d'un fluide parfait permet de retrouver l'équation de Navier-Stokes sans viscosité et sans forces extérieures, 
et l'équation de conservation de la matière.
Pour simplifier, ramenons-nous au cas d'un fluide incompressible donc $\dd \rho / \dd t = 0$ et non relativiste donc $p / \rho c^2 \propto (v/c)^2 \ll 1$. Alors :
$$ 0 = \frac{\partial T^{\mu\nu}}{\partial x^\beta} \Rightarrow
\left\lbrace\begin{align*}
& \alpha = i:\ & 0 = & \vec\nabla p + \rho \frac{\partial \vec v}{\partial t} +  \rho (\vec v \cdot \vec\nabla)(\vec v)  \\
& \alpha = 0:\ & 0 = & \rho \vec \nabla \vec v + \frac{\partial \rho}{\partial t} 
\end{align*}\right.
$$

:::


Dans une base cartésienne, le tenseur énergie-impulsion prend la forme simple :
$$\label{eq:tmunu_fluide}
T^{\mu\nu} = \begin{pmatrix}
-\rho c^2 g^{00} & 0 & 0 & 0 \\
0 & p g^{11} & 0 & 0 \\ 
0 & 0 & p g^{22} & 0 \\ 
0 & 0 & 0 & p g^{33}  \\ 
\end{pmatrix}.
$$




Les équations de Friedmann
---------------------------

Résoudre l'équation d'Einstein [](#eq:einstein2) consiste à en trouver une métrique solution,
compte tenu de la répartition en matière et énergie codée dans $T^{\mu\nu}$.
Supposer les principes d'homogénéité et d'isotropie pour ce tenseur,
impose que la métrique est la
métrique de Friedmann-Lemaître-Robertson-Walker (FLRW), utilisant le jeu
de coordonnées comobiles sphériques usuel $(ct, \sigma, \theta, \phi)$:
$$\begin{aligned}\label{eq:flrw}
g_{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & \frac{a^2(t)}{1-k\sigma^2} & 0 & 0 \\ 
0 & 0 & a^2(t)\sigma^2 & 0 \\ 
0 & 0 & 0 & a^2(t) \sigma^2 \sin^2 \theta  \\ 
\end{pmatrix},\end{aligned}
$$ 
où $a(t)$ est une fonction inconnue. Le paramètre d'échelle $a(t)$ peut être obtenu en résolvant
l'équation d'Einstein connaissant le contenu du tenseur
énergie-impulsion de l'Univers $T^{\mu\nu}$ et la valeur de $k$. 



En utilisant la métrique FLRW
[](#eq:flrw),
calculons pour l'exemple la connexion affine suivante à partir de
l'équation [](#eq:connexion):
$$\begin{aligned}
\Gamma^1_{\ 01} & = \frac{1}{2} g^{1 \mu} \left( \partial_0 g_{1\mu} + \partial_1 g_{0 \mu} - \partial_\mu g_{01} \right) \\
& = \frac{1}{2} g^{1 1} \left( \partial_t g_{11} + \partial_r g_{01} - 0 \right) \text{ car }\forall \mu \neq 1, g^{1\mu}=0\text{ (voir encadré)}\\
& = \frac{1}{2} \frac{1-k\sigma^2}{a^2} \left( \frac{2 \dot{a} a}{1-k\sigma^2} + 0 \right) \\
& = \frac{\dot a}{ca} = \frac{H}{c}.
\end{aligned}$$


Pour la métrique FLRW, son inverse est simplement:
$$
g^{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & \frac{1-k\sigma^2}{a^2(t)} & 0 & 0 \\ 
0 & 0 & \frac{1}{a^2(t)\sigma^2}  & 0 \\ 
0 & 0 & 0 & \frac{1}{a^2(t) \sigma^2 \sin^2 \theta}   \\ 
\end{pmatrix}.
$$

De la même manière, on obtient les autres connexions affines, puis les
tenseurs de Riemann et Ricci. Au final, le tenseur d'Einstein est
diagonal et vaut: 
$$\begin{aligned}
G_{00} & =  - 3 \left( \frac{\dot{a}^2}{c^2 a^2}+ \frac{k}{a^2} \right), \\
G_{ij} & = \frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{c^2 a^2}g_{ij} \text{ pour } i=j\neq 0.
\end{aligned}$$
A partir de l'équation d'Einstein
[](#eq:einstein2) et du tenseur énergie-impulsion
[](#eq:tmunu_fluide), on obtient pour la coordonnée $00$ et pour
les coordonnées spatiales $ij$: 
$$\begin{aligned}
G_{\mu\nu}-\Lambda g_{\mu\nu} & = -8\pi G_N T_{\mu\nu}/c^4 \\
\Leftrightarrow  & \left\lbrace
\begin{array}{rl}
    \text{00: } &  \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{c^2 k}{a^2} \right) = 8\pi G_N \rho + c^2 \Lambda} \\
    ij\text{: } &   \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{a^2} = - \frac{8\pi G_N}{c^2 } p + c^2 \Lambda }
\end{array}
\right.\end{aligned}$$ 
Ce sont les deux équations de Friedmann. Les voici maintenant exprimées en fonction du paramètre de Hubble
$H=\dot{a}/a$ : 
$$\label{eq:friedmann}
\left\lbrace
\begin{array}{rl}
    \text{00: } & \displaystyle{H^2 = \frac{8\pi G_N \rho}{3} + \frac{c^2 \Lambda}{3} - \frac{c^2 k}{a^2}}\\
    ij\text{: } &  \displaystyle{2\dot{H} + 3H^2 = - \frac{8\pi G_N}{c^2 } p + c^2 \Lambda - \frac{c^2 k}{a^2}}
\end{array}
\right.
$$
La première équation de Friedmann relie explicitement
l'évolution du facteur d'échelle $a(t)$ au contenu énergétique de
l'Univers. De plus, en soustrayant ces deux équations et en combinant le
résultat avec la dérivée temporelle de la première, on peut obtenir
l'équation de conservation de l'énergie que l'on obtiendrait aussi
directement en calculant $T^{\mu\nu}_{\;\;;\mu}=0$ dans la métrique
FLRW : 
$$\label{eq:conservation_energie}
\dot{\rho} = -3 H(c^2 \rho  + p )
$$

Le tenseur énergie-impulsion inclut la matière non-relativiste et
relativiste. La matière relativiste est généralement nommée rayonnement
car aujourd'hui le rayonnement de photons du CMB est largement dominant
dans cette composante. La matière non relativiste n'exerce pas de
pression donc $p_m=0$ et : 
$$
\label{eq:conservation_energie_matiere}
\dot{\rho}_m = -3 H\rho_m \Rightarrow \rho_m = \rho_m^0 a^{-3}.
$$
Cette  dernière relation traduit bien le fait que si une boîte de côté $a$
contenant une certaine quantité de matière voit la longueur de ses côtés
doubler, alors la densité de matière est bien divisée par $2^3$. Pour le
rayonnement, $\rho_r = 3 p_r$ donc :
$$\label{eq:conservation_energie_radiation}
\dot{\rho}_r = -4 H\rho_r \Rightarrow \rho_r = \rho_r^0 a^{-4}.
$$ 
Le raisonnement avec une boîte cubique de côté $a$ s'applique aussi ici,
mais si toutes les longueurs doublent, alors la longueur d'onde du
rayonnement aussi donc son énergie est divisée par 2. On retrouve bien
une diminution de la densité d'énergie de rayonnement en $2^4$.

L'équation d'état $w(z)$ associée à une composante de l'Univers est
définie par le rapport de sa pression et de sa densité d'énergie
$w=p/\rho$.

-   La matière non relativiste n'exerce pas de pression sur son milieu
    extérieur d'où $p_m=0$ donc $w_m=0$.

-   La matière relativiste exerce quant à elle une pression sur son
    milieu de valeur $p_r = c^2 \rho_r / 3 $ d'où $w_r=1/3$.

-   Pour la constante cosmologique, on identifie dans
    l'équation [](#eq:friedmann) une densité d'énergie
    $\rho_\Lambda = \Lambda/8\pi G_N$ et une pression
    $p_\Lambda = - \Lambda / 8\pi G_N$ d'où une équation d'état
    constante et négative $w_\Lambda = -1$.



Les paramètres cosmologiques
----------------------------

On peut définir une densité critique, qui correspondrait à la densité
que l'on doit avoir dans un univers homogène et isotrope en expansion de
courbure spatiale nulle (cf
équation [](#eq:friedmann)): 
$$\rho_c(t) = \frac{3H^2(t)}{8\pi G_N}.$$ 
Il est commode de définir aussi sa valeur actuelle:
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
courbure: 
$$\rho_k(t) = - \frac{3k}{8\pi G_N a^2(t)}.$$
On voit que la densité d'énergie associée à la constante cosmologique étant constante
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
2\dot{H} + 2H^2 = \frac{2\ddot{a}}{a} = -\frac{8\pi G_N}{3}\left(c^2 \rho _{\mathrm{tot}} + 3p_{\mathrm{tot}}\right).
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
La première équation de Friedmann s'écrit alors simplement avec $\rho=\rho_m+\rho_r$:
$$1 = \Omega_m(t) + \Omega_r(t) + \Omega_\Lambda(t) + \Omega_k(t)$$

```{math}
:label: eq:friedmann2
\bar H^2 (t) \equiv \frac{H^2(t)}{H_0^2} = \Omega_m^0 a^{-3}(t) + \Omega_r^0 a^{-4}(t) + \Omega_\Lambda^0 +  \Omega_k^0 a^{-2}(t).
```
Ce modèle d'Univers liant la prédiction de son expansion $\bar H(z)$ à
son contenu composé d'une constante cosmologique, de matière et de
radiation, est appelé modèle $\Lambda$CDM ($\Lambda$ pour la constante
cosmologique et CDM pour *Cold Dark Matter*).



Paramètre de décélération
-------------------------



Modélisations de l'énergie noire
-------------------------------
