---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---


La métrique de Friedmann-Lemaître-Robertson-Walker
================================


Principes cosmologiques
-----------------------



```{iframe} https://www.youtube.com/embed/UTlYUxucEZA?si=WZpcAuL1ElZuyvf6
:name: fig:sdss
:align: center
:width: 60%

Galaxy distribution compiled by the eBOSS survey. Every dot in this "pie" diagram is a galaxy, color coded by type: green for nearby galaxies, magenta and red for old red galaxies, 
blue for young blue galaxies, yellow and white for quasars. Credit: A. Raichoor (EPFL) / A. Ross (Ohio State Univ.) / SDSS Collaboration
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

Pour être en mesure de construire un modèle de l'Univers, c'est-à-dire une construction théorique capable de décrire le contenu de l'Univers et son évolution, il faut parvenir 
à résoudre l'équation d'Einstein de la Relativité Générale. Cependant, jusqu'à quel niveau de détail est-il nécessaire d'aller pour le décrire suffisamment bien aux grandes échelles ? 
On se doute que paramétrer l'équation d'Einstein jusqu'à inclure l'échelle du système solaire est à la fois illusoire et non nécessaire. Quelle est 
la structure de l'Univers aux plus grandes échelles ? Ici la nature nous fait un beau cadeau, qui va simplifier considérablement l'écriture d'un modèle cosmologique à partir des équations
de la Relativité Générale.

:::{important}
À des échelles suffisamment grandes, l'univers est spatialement homogène et isotrope.
:::

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
    identique  à $2.725\pm0.002$ {cite:p}`Mather1999` dans toutes les directions de l'espace. Seules des fluctuations 
    de température de l'ordre de $10^{-5}$ sont détectés sur cette image de l'Univers jeune (voir
    figure [](#fig:cmb_planck) et par exemple
    {cite:t}`ThePlanckCollaboration2013XIII` pour une vérification du principe
    d'isotropie utilisant l'effet Sunyaev-Zeldovich).


Ignorer complètement ce qui se passe à des échelles "insuffisamment" grandes est la première étape pour
construire une solution cosmologique à la Relativité Générale. Muni de ces faits osbervationnels, nous imposerons l'homogénéité et l'isotropie à la métrique
métrique et à la distribution de la matière (c'est-à-dire au tenseur contrainte-énergie).

:::{note} A propos de l'homogénéité de l'Univers
:class: dropdown 

Avant de présenter cette solution cosmologique, il est intéressant de se demander pourquoi
le principe cosmologique devrait s'appliquer. Alors que la gravité, la force dominante qui façonne
les structures à grande échelle de l'univers, tend à détruire l'homogénéité (une région légèrement sur-dense dans un univers homogène attirera la matière et deviendra de plus en plus sur-dense), il faut de plus en plus de temps pour y parvenir.
il faut de plus en plus de temps pour y parvenir à mesure que l'on s'approche des grandes échelles. Comme les grandes échelles
semblent plus homogènes dans les observations, on peut supposer que l'univers était beaucoup plus homogène dans le passé à toutes les échelles et qu'il le devient de moins en moins sous l'action de la gravité.
Mais pourquoi était-il homogène à l'origine ? Une réponse logique est qu'une interaction autre que la gravité y a contribué (comme, par exemple, la pression dans un gaz parfait). Cependant, la Relativité Générale stipule qu'aucune interaction ne peut se propager plus vite que la vitesse de la lumière. Nous verrons
que dans une théorie où l'évolution de l'univers découle d'un Big Bang initial, cela crée 
une difficulté potentielle : l'homogénéisation ne devrait être possible que jusqu'à des échelles égales à la distance parcourue par un photon entre le Big Bang et aujourd'hui.
:::


Univers de symétrie maximale
------------------

Etant donné le principe cosmologique, on cherche à déterminer la forme que doit prendre la métrique d'un Univers de symétrie maximale, c'est-à-dire un Univers dont les propriétés sont invariantes par rotation et translation {cite:p}`Weinberg1972`[p. 379].


### Métrique d'un Univers isotrope

Une définition mathématique précise d'un espace-temps spatialement homogène et isotrope est qu'il peut être folié avec une famille d'hyper-surfaces de type espace à un paramètre, homogènes et isotropes. 
La définition d'une foliation impose que chaque feuille de la foliation, une hyper-surface de type espace dans notre cas, soit une classe d'équivalence où l'équivalence peut être énoncée comme ayant la même valeur du paramètre. 
Si nous appelons ce paramètre le temps, nous voyons que nous avons un temps universel en tout point de l'espace. 
Le terme $g_{00}$ de la métrique ne dépend alors pas des coordonnées spatiales, mais seulement du temps. 

De plus, il est facile de vérifier que la ligne du monde de tout observateur qui peut vérifier
est _perpendiculaire_ (telle que définie par la métrique) aux surfaces spatiales. En effet, en simplifiant à un espace-temps 2D, si la métrique a la forme 
\begin{equation}
g=\begin{pmatrix} g_{00} & g_{01}  \\ g_{01} & g_{11} \end{pmatrix}
\end{equation}
alors l'équation des trajectoires de type lumière est 

$$\dd s^2=0=g_{00}c^2\dd t^2+2g_{01}\,c\,\dd x\,\dd t+g_{11}\dd x^2$$

On peut alors vérifier, en résolvant l'équation de $\dd t$, que si $g_{01} \neq 0$, deux $\dd x$ opposés donnent deux valeurs différentes de $\dd t$ positif. 
C'est-à-dire qu'un observateur recevra à des moments différents les impulsions lumineuses émises 
simultanément par deux sources situées à la même distance dans des directions opposées. Cela 
Cela rompt évidemment l'isotropie. Les termes $g_{0i}$ et $g_{i0}$ de la métrique sont donc nuls.

En combinant les deux résultats précédents, l'intervalle espace-temps peut être écrit sous la forme suivante :
\begin{equation}
\dd s^2= -g_{00}(t) c^2 \dd t^2 + \dd l^2
\end{equation}
où $\dd l$ est un élément de longueur ne dépendant que des coordonnées spatiales. La métrique prend donc la forme :
\begin{equation}
g_{\mu\nu}=\begin{pmatrix} -g_{00}(t) c^2& 0 & 0 & 0 \\ 0 & \gamma_{11} & \gamma_{12} & \gamma_{13} \\ 
0&\gamma_{21} & \gamma_{22} & \gamma_{23} \\ 0&\gamma_{31} & \gamma_{32} & \gamma_{33} \end{pmatrix}
\end{equation}
où $\gamma_{ij}$ est la métrique spatiale, qui peut dépendre du temps et de la position.

:::{attention} Convention de signature pour la métrique
Dans ce cours, comme dans beaucoup de cours de cosmologie, la [signature](https://en.wikipedia.org/wiki/Metric_signature) choisie pour la métrique est $(-,+,+,+)$. 
En effet, en cosmologie on manipule beaucoup des distances donc il est plus commode d'avoir des éléments de longueur positifs. En physique théorique
des hautes énergies, la métrique $(+,-,-,-)$ est souvent préférée. Une compilation des différentes signatures utilisées est présentée
[ici](https://en.wikipedia.org/wiki/Sign_convention).

:::


### Géométrie d'un Univers maximallement symétrique

Trouvons maintenant une forme explicite pour $\dd l^2$. Un Univers de symétrie maximale (homogène et isotrope) doit posséder une courbure constante.
Cela se comprend assez intuitivement mais aussi se démontre en Relativité Générale  {cite:p}`Weinberg1972` [p. 381].
Notons $a$ le rayon de courbure associé, et soit $\vec x = (x^1, x^2, x^3)$ un vecteur position
dans l'espace 3D, de norme :
$$r^2 = \Vert \vec x \Vert^2 = \gamma_{ij} x^i x^j$$
On a donc :
\begin{equation}
\dd l^2 = \gamma_{ij} \dd x^i \dd x^j, \quad \text{avec}\quad i=1,2,3
\end{equation}


Tout d'abord, si cet espace possède une courbure nulle, alors l'élément de métrique $\dd l$ s'écrit simplement :
\begin{equation}
\dd l^2 =   \delta_{ij}\dd x^i \dd x^j  = \dd \vec x^2 
\end{equation}

Travaillons maintenant sur le cas où la courbure est non nulle. Pour décrire la courbure d'une surface avec des notions de géométries habituelles, 
étudions-la dans un espace avec une dimension supplémentaire.
Si nous plaçons cet espace 3D non euclidien dans un espace 4D _euclidien_ (non courbé) avec des coordonnées $(x^1, x^2, x^3, w)$, 
l'hyper-surface 3D non euclidienne de courbure gaussienne positive constante $a^{-2}$ peut être décrite par l'équation suivante :
- pour une 3-sphère de rayon $a$ : 
\begin{equation}
r^2 + w^2= a^2
\end{equation}
- pour un 3-hyperboloïde de courbure $a$ :
\begin{equation}
r^2 - w^2= -a^2
\end{equation}

Les deux derniers cas de courbures strictement positive ou négative sont donc définis par _l'équation de contrainte_ :
```{math}
:label: eq_hyp_sph
r^2 \pm w^2= \pm a^2 
```

:::{tip} Notion de courbure
:class: dropdown

Si ces raisonnements vous troublent, rappelez-vous que c'est comme décrire la courbure d'un cercle de rayon $R$ 
(objet à une dimension car il n'y a qu'une seule direction de déplacement sur cet objet)
dans un plan à l'aide d'une second dimension, donc deux coordonnées $x$ et $y$ telles que :
$$x^2 + y^2 = R^2$$ 
ou celle d'une sphère (deux dimensions) dans un espace avec une troisième dimension, donc trois coordonnées $(x,y,z)$ telles que :
$$x^2 + y^2 + z^2 = R^2$$
:::

La distance infinitésimale entre deux points dans l'espace 4D euclidien peut être écrite :
\begin{equation}
\dd l^2=\dd \vec x^2 \pm \dd w^2
\end{equation}

Si ces deux points sont contraints d'être positionné sur notre espace 3D non euclidien, la différentiation de l'équation
eq. [](#eq_hyp_sph) donne la relation $r\dd r \pm w\dd w=0$, donc, en injectant de nouveau l'équation [](#eq_hyp_sph), on obtient :
\begin{equation}
(\vec x \cdot \dd \vec x)^2=(w\dd w)^2 \Rightarrow (\dd w)^2= \frac{(\vec x \cdot \dd \vec x)^2}{w^2} = \frac{(\vec x \cdot \dd \vec x)^2}{a^2 \mp r^2}
\end{equation}
La distance infinitésimale entre 2 points de l'espace 3D non euclidien de courbure non nulle constante $a^{-2}$ est alors :
\begin{equation}
\dd l^2= \dd \vec x^2 \pm \frac{(\vec x \cdot \dd \vec x)^2}{a^2\mp r^2} 
\end{equation}

A cette étape, nous pouvons maintenant combiner le résultat obtenu pour les deux courbures non nulles avec le cas euclidien en introduisant
le _paramètre de courbure_ $k$ :
```{math}
:label: K-def

k = \left\lbrace
\begin{array}{rl}
 +1 & \text{3-sphère} \\
 0 & \text{espace\ plat} \\
 -1 & \text{3-hyperboloïde} \\
\end{array}\right.
```
On a ainsi pour les trois géométries possibles d'un Univers maximallement symétrique :
\begin{equation}
\dd l^2= \dd \vec x^2 + k\frac{ (\vec x \cdot \dd \vec x)^2}{a^2 - k r^2}
\end{equation}

Enfin, notons que le rayon de courbure peut a priori être une fonction du temps[^gammat]. On introduit la variable rééchelonnée $\sigma=r/a(t)$, et nous obtenons une nouvelle expression :
\begin{equation}
\dd l^2= a^2(t) \left(\dd \vec \sigma^2 + k\frac{(\vec \sigma \cdot \dd \vec \sigma)^2}{1 - k \sigma^2} \right)
\end{equation}

Il est alors possible de fixer $g_{00}$ à 1 quitte à redéfinir la variable temps[^g00]. La métrique de Friedmann-Lemaître-Robertson-Walker décrivant un Univers homogène 
et isotrope s'écrit finalement :
```{math}
:label: FLRW-metric

\dd s^2=-c^2\dd t^2 + a^2(t) \left(\dd \vec \sigma^2 + k\frac{(\vec \sigma \cdot \dd \vec \sigma)^2}{1 - k \sigma^2} \right)
```

La métrique de Friedmann-Lemaître-Robertson-Walker (FLRW) constitue le cadre de base du modèle cosmologique standard. Les hypothèses d'homogénéité
et d'isotropie ont directement conduit à une métrique décrivant un univers avec seulement trois géométries possibles 
(plat, 3-sphère, 3-hyperboloid) et un facteur d'échelle $a(t)$ affectant les distances. Notez que, grâce à l'imposition des symétries d'homogénéité et d'isotropie, nous avons réduit l'écriture de la
métrique $g_{\mu\nu}$ (qui est un tenseur symétrique) constituée a priori de 10 composantes indépendantes inconnues à un tenseur possédant une seule fonction inconnue $a(t)$.


:::{important} Où sont les unités ?
L'élément de distance $\dd s$ possède la dimension d'une longueur, par conséquent tous les terms de l'équation [](#FLRW-metric) aussi. 

Certains ouvrages proposent que le facteur d'échelle soit une fonction du temps sans dimension, et que $\sigma$ garde la dimension d'une longueur, 
normalisée par $a(t)$. Ceci permet de tout définir en particulier en posant qu'aujourd'hui le facteur d'échelle vaut $a_0=1$, mais alors il faut redéfinir
$k$ (avec $w$) et lui donner l'unité d'une courbure (inverse d'une distance au carré).

Dans ce cours, nous allons abondamment traiter des distances en cosmologie, et dans ce cas il est plus commode de penser que le facteur d'échelle est 
homogène à une longueur, et que les coordonnées spatiales $\vec \sigma$ forment un vecteur sans dimension. 
Le paramètre de courbure $k$ est alors sans dimension également.

:::


Il est important de comprendre la signification physique du facteur d'expansion $a(t)$. Tout d'abord, d'après l'équation [](#FLRW-metric), ce facteur
relie la distance propre (physique) $r$ et la distance de coordonnées $\sigma$ par $\dd r=a(t)\dd \sigma$. 
Deux particules dont les coordonnées spatiales sont fixes verront leur distance physique augmenter (ou diminuer) avec le temps. 

Pour un Univers sphérique, le facteur d'échelle $a(t)$ représente également son rayon de
courbure. Un Univers sphérique dynamique correspond donc à un univers
possédant un rayon de courbure variable dans le temps. Un espace plat ne
possède pas d'échelle caractéristique, la valeur de $a(t)$ n'a donc pas
de sens physique. La quantité ayant un sens physique pour un tel univers
est le paramètre de Hubble qui quantifie la vitesse de variation du
facteur d'échelle : 
```{math}
:label: H-def

\fbox{$\displaystyle H(t) = \frac{\dot a(t)}{a(t)} $}
```
avec le point $\dot{}$ exprimant une dérivée par rapport au temps $t$.
Dans le but d'alléger les notations, la dépendance temporelle des
paramètres ne sera pas toujours explicitée, de sorte que $a(t)=a$. On
désignera les paramètres évalués au temps présent $t_0$ par l'indice ou
l'exposant 0 si bien que $a(t_0)=a_0$. 
Dans la suite, nous travaillerons dans le système où $a_0$ _n'est pas fixé_ à 1. 

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

```{note} Que signifie vivre dans un espace courbé ?
La [](#fig:espaces) représente des surfaces 2D plongées dans des espaces 3D. Mais comment se représenter que nous vivrions dans une 3-sphère ? Et qu'est-ce 
que cela implique ? Vivre dans un espace courbé implique que la somme des angles d'un triangle n'est pas égale à 180°: elle est supérieure pour une 3-sphère et inférieure pour
un 3-hyperboloid. C'est ainsi que les deux triangles bleus [](#fig:triangles_on_sphere)
ont une somme de leurs angles supérieures à 180°. Dans une 3-sphère nous pouvons avoir l'impression que deux objets sont éloignés angulairement, alors qu'en en fait leur distance qui les sépare
est plus petite que ce qu'elle serait dans un espace plat. Et ceci dans toutes les directions de l'espace. 

En résumé, vivre dans un espace courbé signifie que la relation entre angles et longueurs est déformée par rapport à notre intuition euclidienne, en 
tous cas sur des distance cosmologiques.


:::{figure} ../images/triangles_on_sphere.svg
:name: fig:triangles_on_sphere 
:align: center

Prenons deux galaxies: elles forment un triangle avec la Terre, qui, dans une 3-sphère, possède trois angles dont la somme est supérieure à 180°. Il repose
sur une 2-sphère, hyperplan de la 3-sphère (surface $w=cste$). L'intersection avec le plan passant également par ces trois points définit les géodésiques par lesquelles la lumière nous parvient. 
Pour toute paire de points, on peut ainsi définir un tel triangle reposant sur une 2-sphère (bleu et cyan par exemple).
:::

```

Coordonnées comobiles
---------------------

Il est important de noter que tous les observateurs ne voient pas l'Univers comme isotrope, mais seulement les 
observateurs dits "comobiles", qui sont localement au repos avec l'essentiel de la matière dans leur voisinage. 
Nous, par exemple, ne sommes pas des observateurs mobiles : lorsque nous observons la température du CMB, la 
première caractéristique que nous voyons est un grand dipôle, qui est le résultat du mouvement particulier de notre 
galaxie (et de notre groupe de galaxies). Si on pouvait retrancher ce mouvement propre par rapport au référentiel du CMB, alors cela 
ferait de nous des observateurs comobiles. Ainsi, on peut définir un système de coordonnées associés à des observateurs
sans mouvements propres, dont les distances relatives n'augmentent qu'avec le facteur d'échelle $a(t)$ {cite:p}`Weinberg1972`[p. 409].

### Coordonnées sphériques

Dans la métrique FLRW où l'expansion de l'Univers est factorisée par un facteur d'échelle $a(t)$, les coordonnées 
spatiales $\vec \sigma$ sont appelées _coordonnées comobiles_. 
Il existe une grande liberté dans le choix des coordonnées comobiles. On privilégie souvent
les coordonnées sphériques $(ct, r, \theta, \phi)$ avec l'observateur (nous-mêmes) à l'origine, telles que :
```{math}

\begin{aligned}
\sigma_1 &= \sigma \sin \theta \cos \phi \\
\sigma_2 &= \sigma \sin \theta \sin \phi \\
\sigma_3 &= \sigma \cos \theta
\end{aligned}
```
Après des calculs simples mais longs (voir notebook et [ici](`https://en.wikipedia.org/wiki/Spherical_coordinate_system#Integration_and_differentiation_in_spherical_coordinates`)), dans les trois cas de courbures la métrique FLRW s'écrit :
```{math}
:label: eq:FLRW-metric-spherical

\dd s^2=-c^2\dd t^2 + a^2(t) \left( {1 \over 1-k\sigma^2}\dd \sigma^2 + \sigma^2 \dd \theta^2 + \sigma^2 \sin^2 \theta \dd \phi^2\right)
```

:::{note} Courbure et finitude de l'Univers

Pour la 3-sphère, 3-hyperboloïde et le plan, la courbure de ces surfaces est {cite:p}`Weinberg1972`[p. 412]:
$$ K(t) = \frac{k}{a^2(t)}$$
La 3-hyperboloïde et le plan sont d'extension infinie. En revanche, la 3-sphère est d'extension finie mais reste non bornée : une particule ne rencontrera jamais 
de bord mais on peut définir un volume :
$$V(t) = 2 \pi^2 a^3(t)$$
et un périmètre (longueur d'un méridien) :
$$L(t) = 2 \pi a(t)$$
:::


### Coordonnées cartésiennes

Le cas de l'univers plat simplifie beaucoup les calculs qui suivront. Étant donné qu'une courbure nulle est toujours compatible 
avec les contraintes de plus en plus fortes des observations cosmologiques
nous concentrerons désormais nos développements analytiques sur l'univers plat, en mentionnant des résultats pour le cas général 
lorsque cela est nécessaire. 
Dans le cas de courbure nulle, on peut aussi utiliser les coordonnées comobiles euclidiennes $(ct, x, y, z)$, telles que :
```{math}

\sigma_1  = x,\quad \sigma_2  = y,\quad\sigma_3  = z,\quad\sigma^2  = x^2 + y^2 + z^2
```
La métrique FLRW s'écrit dans un univers plat :
\begin{equation}
g_{\mu\nu}=\begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & a^2(t) & 0 & 0 \\ 0&0& a^2(t)&0 \\ 0&0&0&a^2(t) \end{pmatrix}
\end{equation}

### Distance propre et distance comobile

La _distance propre_ définit la distance physique entre deux objets à un instant $t$. Soit un objet émetteur situé aux coordonnées comobiles $(\sigma_E, \theta_E, \phi_E)$.
Par définition, la distance propre entre cet objet et un observateur situé à l'origine est :
```{math}
:label: eq:dist-prop

d_p(\sigma_E, t) = \int_0^{\sigma_E} \sqrt{g_{\sigma\sigma}}\dd\sigma' = \int_0^{\sigma_E}\frac{a(t)\dd\sigma'}{\sqrt{1-k\sigma'^2}} = a(t) \chi(\sigma_E)
```
où on fait apparaître $\chi(\sigma_E)$ la _distance comobile_ entre cet objet et l'observateur :
```{math}
:label: eq:dist-comobile

\chi(\sigma_E) = \int_0^{\sigma_E}\frac{\dd\sigma'}{\sqrt{1-k\sigma'^2}} = \left\lbrace\begin{array}{cl}
    \arcsin\sigma_E & \text{ si } k=+1  \\
    \sigma_E  & \text{ si } k=0 \\
    \text{arcsh}\,\sigma_E & \text{ si } k=-1 
\end{array}
\right.
```
On voit que la distance propre possède bien l'unité d'une longueur alors que la distance comobile est adimensionnée. Cette dernière représente la distance
dans l'espace des coordonnées et est indépendante de l'expansion de l'Univers. En revanche la distance propre évolue avec le facteur d'échelle.

```{exercise} Coordonnées comobiles sur la sphère
:label: exo:sphere-comobile

Pour se créer une intuition sur la géométrie courbe et les coordonnées comobiles, nous allons étudier une sphère 2D de rayon $a(t)$. 
Sur cette sphère, les coordonnées sont données par l'angle polaire $\chi$ et la longitude $\theta$ (la coordonnée $\phi$ est donc omise par rapport au cas FLRW). 
Considérons qu'un observateur est situé en $(\chi,\theta)=(0, 0)$ et une galaxie en $(\chi, 0)$. 

1. Représenter une sphère et tracer le méridien $\theta = 0$. Placer les quantités suivantes : l'observateur, la galaxie, $a(t)$, $\chi$, la distance propre entre l'observateur et la galaxie $d_p$. 
Relier ces quantités à la coordonnée $\sigma$ et à l'expression de $d_p$.


2. Considérons maintenant deux galaxies à la même coordonnées $\chi$, séparées par la distance propre $l$. Montrer que l'angle $\theta$ 
($\theta \ll 1$) sous lequel elles sont observées sur la sphère est $\theta = l / (a(t) \sigma)$.

```

```{solution} exo:sphere-comobile
:label: exo:sphere-comobile-sol
:class: dropdown

1. La coordonnée comobile $\chi$ est explicitement l'angle polaire entre l'observateur et la galaxie. 
La distance propre est la longueur de l'arc qui est $d_p = a(t) \chi$ comme dans la géométrie habituelle. 
La coordonnée $\sigma$ est liée à la longueur $b$ de la corde à cet angle $\chi$ par :
\begin{equation}
\sigma = \sin \chi = \frac{b}{a(t)}
\end{equation}
Notons également que $b$ est le rayon du cercle de latitude $b = a(t) \sin \chi$. 

2. Avec la projection polaire, on voit que $\theta$ est l'angle délimitant un arc de taille $l$ et de rayon $b$, 
le rayon du cercle de latitude de $\chi$. Ainsi :
\begin{equation}
\theta = \frac{l}{b} = \frac{l}{a(t) \sin \chi} = \frac{l}{a(t) \sigma}
\end{equation}
Dans un espace plat, $\sigma$ est clairement la coordonnée radiale de rapprochement entre l'observateur et les galaxies. 
L'expression de $\theta$ dans le cas sphérique est cohérente avec celle dans le cas plat grâce au paramétrage $\sigma=f_k(\chi)$.

En utilisant la métrique FLRW, avec l'[](#exo:conformal-time) nous avons également :
\begin{equation}
l = \int_0^l \dd l' = \int_0^\theta \sqrt{g_{\theta\theta}} a(t)\dd\theta = a(t) \int_0^\theta f_k(\chi) \dd\theta = a(t) \theta \sin\chi = a(t) \theta \sigma
\end{equation}
Donc $\theta = l / a(t) \sigma$.

Il est facile de vérifier que nous avons les mêmes expressions dans le cas plat, et nous les admettrons dans la géométrie hyperbolique. 
La coordonnée $\sigma$ est donc utile pour faire des calculs et des dessins dans le cas plat et traduire ces résultats dans les cas courbes (ce qui n'est pas si facile avec $\chi$).


:::{figure} ../images/spherical_universe.svg
:width: 100%
:align: center
    
Géométrie dans un univers sphérique.
:::

```

### Temps cosmique et temps conforme

Le temps mérite une mention spéciale. Dans notre Univers idéal, sans surdensités ou sous-densités de matière, 
toutes les horloges qui suivent l'expansion (c'est-à-dire sans mouvement propre) battent la seconde à la même cadence. 
Avec un temps infini à notre disposition, nous pouvons proposer une convention commune pour synchroniser nos horloges : 
par exemple, lorsque la température du CMB atteint une valeur donnée. Il est donc possible de définir un temps cosmique, 
commun à tous les observateurs en chute libre {cite:p}`Weinberg1972` [p. 409]. 

```{exercise} Temps conforme
:label: exo:conformal-time

Transformer la partie spatiale de la métrique FLRW en coordonnées comobile $(\sigma,\theta,\phi)$ [](#eq:FLRW-metric-spherical)
au système de coordonnées comobile équivalent $(\chi,\theta,\phi )$ avec $\chi$ la distance comobile. 
Étendre cette transformation aux coordonnées temporelles et proposer une définition du temps conforme $\eta$ et l'écrire sous la forme :
\begin{equation}
\dd s^2 = a^2(t) \left[ -c^2 \dd\eta^2 + \dd\chi^2 + f_k^2(\chi)\dd\theta^2 + f_k^2(\chi)\sin^2\theta \dd\phi^2 \right]
\end{equation}
avec $f_k(\chi)$ une fonction de $k$ et $\chi$ à définir. 

```

```{solution} exo:conformal-time
:label: exo:conformal-time-sol
:class: dropdown

On commence par la définition de la métrique FLRW :
\begin{align}
\dd s^2 & = -c^2\dd t^2 + a^2(t) \left[ \frac{\dd\sigma^2}{1-k\sigma^2} + \sigma^2\dd\theta^2 + \sigma^2 \sin^2\theta \dd\phi^2 \right]  \\
& = -c^2\dd t^2 + a^2(t) \left[ \dd\chi^2 + r^2\dd\theta^2 +\sigma^2 \sin^2\theta \dd\phi^2 \right] \\
& = -c^2\dd t^2 + a^2(t) \left[ \dd\chi^2 + f_k^2(\chi)\dd\theta^2 +f_k^2(\chi) \sin^2\theta \dd\phi^2 \right]
\end{align}
avec $\dd\chi = \dd\sigma/\sqrt{1-k\sigma^2}$ et :
\begin{equation}
\sigma = f_k(\chi) = \left\lbrace\begin{array}{cl}
    \sin\chi & \text{ si } k=+1  \\
    \chi  & \text{ si } k=0 \\
    \sinh\chi & \text{ si } k=-1 
\end{array}
\right.
\end{equation}
On définit $\dd\eta =  \dd t / a(t)$ le temps conforme, et on aboutit à :
\begin{equation}
\dd s^2 = a^2(t) \left[ -c^2 \dd\eta^2 + \dd\chi^2 + f_k^2(\chi)\dd\theta^2 + f_k^2(\chi)\sin^2\theta \dd\phi^2 \right]
\end{equation}
Le temps conforme $\eta$ possède la dimension d'une durée. 

```


Géodésiques dans la métrique FLRW
---------------------------------

Quelle est la trajectoire d'une particule en chute libre dans une métrique FLRW ? D'après la Relativité Générale, 
nous savons qu'une telle particule se déplace le long d'une géodésique dont l'équation est la suivante :
\begin{equation}
{\dd^2 x^\mu \over \dd  s^2} +\Gamma^{\mu}_{\,\,\nu\kappa} {\dd x^\nu \over \dd  s}{\dd x^\kappa \over \dd  s}=0,
\label{geodesic}
\end{equation} 
où $s$ est un paramètre quelconque décrivant la position le long de la géodésique (le temps propre par exemple).
Une autre forme de l'équation des géodésiques va ici nous aider, obtenue à partir de l'équation [](#eq:dcov-cov) :
\begin{equation}
{\dd^2 x_\mu \over \dd  s^2} -\Gamma^{\nu}_{\,\,\mu\kappa} {\dd x_\nu \over \dd  s}{\dd x^\kappa \over \dd  s}=0.
\label{geodesic-cov}
\end{equation} 
Définissons le vecteur 4-impulsion comobile $P^\mu$ le long d'une ligne d'Univers par $^\mu = \dd x^\mu / \dd s$. Alors :
\begin{equation}
{\dd U_\mu \over \dd  s} = \Gamma^{\nu}_{\,\,\mu\kappa} U_\nu U^\kappa=  \frac{1}{2} \frac{\partial g_{\alpha\beta}}{\partial x^\mu} U^\alpha U^\beta.
\end{equation} 
A partir de cette forme de l'équation des géodésiques, calculons la forme que doit prendre le vecteur contravariant $U^\nu$ dans une métrique FLRW pour une particule en chute libre.

Commençons par le cas $\mu=3$ et utilisons les coordonnées sphériques $(\chi,\theta,\phi)$. Comme la métrique FLRW ne dépend pas de $\phi$, alors :
$${\dd U_3 \over \dd  s} = 0$$
donc $U_3$ est une constante du mouvement. Or, on a par ailleurs :
$$U_3 = g_{33} U^3 = a^2(t) f_k^2(\chi) \sin^2 \theta U^3 $$
dont l'expression s'annule à l'origine en $\chi=0$. Comme la composante $U_3$ est constante alors 
elle est identiquement nulle le long de la trajectoire. On en déduit :
$$U^3 = \frac{\dd \phi }{ \dd s} = 0 \Rightarrow \phi = \text{constante}$$

Passons au cas $\mu=2$. La seule composante de la métrique dépendant de $\theta$ est 
$g_{33}$ mais $U_3$ est identiquement nul donc :
$${\dd U_2 \over \dd  s} = \frac{1}{2} \frac{\partial g_{\alpha\beta}}{\partial x^2} U^\alpha U^\beta = \frac{1}{2} \frac{\partial g_{33}}{\partial x^2} U^3 U^3 = 0.$$
Or de même on a par ailleurs :
$$U_2 = g_{22} U^2 = a^2(t) f_k^2(\chi) U^2 $$
qui s'annule en $\chi=0$ donc $U^2$ est nul tout le long de la trajectoire. On en déduit :
$$U^2 = \frac{\dd \theta }{ \dd s} = 0 \Rightarrow \theta = \text{constante}$$

:::{important}
Les géodésiques passant par l'origine en coordonnées sphériques sont les trajectoires vérifiant :
$$\fbox{$\theta=\text{constante},\quad \phi=\text{constante}$}$$
:::


Le décalage spectral, ou redshift
----------------------------------


```{figure} ../images/distances2.svg
:name: fig:distances_croquis
:align: center
:width: 60%

Notations pour le calcul du redshift et des distances cosmologiques en coordonnées comobiles.
```

Pour mesurer la valeur des différents paramètres de densité dans notre
Univers, il faut avoir accès au paramètre d'échelle $a(t)$. Ceci est
possible par la mesure du décalage spectral de la lumière venant de
sources distantes. Dans la métrique FLRW, plaçons-nous par convention au
centre $r=0$ (ou $\sigma=0$), et considérons un objet situé aux coordonnées comobiles
$\left(\sigma_E,\theta_E,\phi_E\right)$, émettant un photon
à l'instant $t_E$ (voir [](#fig:distances_croquis)). Pour ce photon, voyageant à la vitesse
de la lumière, dans la métrique FLRW on a, à tout instant:
```{math}
:label: eq:ds2_lumiere

\dd s^2=0=-c^2 \dd t^2+\frac{a^2(t)}{1-k\sigma^2}\dd \sigma^2.
```
car le long de sa géodésique $\theta$ et $\phi$ sont constants.
Posons $t_0$ l'instant de la réception de cette onde en $\sigma=0$. Alors grâce à l'équation
précédente on a la relation : 
```{math}
:label: eq:comobile

\chi =  \int_{t_E}^{t_0} \frac{c\dd t}{a(t)} = \int_0^{\sigma_E}\frac{\dd\sigma}{\sqrt{1-k\sigma^2}} = \left\lbrace
\begin{array}{cl}
    \arcsin \sigma_E & \text{ si } k=+1 \\
    \sigma_E & \text{ si } k=0 \\
    \text{arcsh}\,\sigma_E & \text{ si } k=-1 
\end{array}
\right. .
``` 
Cette dernière intégrale est appelée distance comobile car
elle fait abstraction des effets de l'expansion de l'Univers dans le
calcul de la distance parcourue par la lumière. En effet, elle a la même
dimension que $\sigma$ donc est sans unité.

En utilisant le temps conforme $\eta$ défini par $\dd \eta = \dd t / a(t)$, pour un photon on obtient :
$$\chi = c \int_{\eta_E}^{\eta_0} \dd \eta = c (\eta_E - \eta_0)$$
donc on reconnait la relation traditionnelle entre distance et temps, mais dans l'espace comobile adimensionné 
par le facteur d'échelle $a(t)$.


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
\int_{t_E+T_E}^{t_0+T_0} \frac{c\dd t}{a(t)} & =\int_{t_E}^{t_0} \frac{c\dd t}{a(t)}  \\
\int_{t_E+T_E}^{t_E} \frac{c\dd t}{a(t)} & =\int_{t_0+T_0}^{t_0} \frac{c\dd t}{a(t)} \\
\Leftrightarrow \frac{cT_0}{a(t_0)} & = \frac{c T_E}{a(t_E)}  \\
\Leftrightarrow \frac{\lambda_0}{\lambda_E} & = \frac{a(t_0)}{a(t_E)}\label{eq:redshift2}
\end{aligned}
$$
Directement, si l'espace est en expansion alors $a(t_E) < a(t_0)$ et la
longueur d'onde reçue $\lambda_0$ est donc supérieure à la longueur
d'onde émise $\lambda_E$. On définit alors le décalage spectral,
communément appelé _redshift_ en raison du fait que la quasi-totalité
des spectres des galaxies observées sont décalées vers le rouge, par :
```{math}
:label: eq:redshift

 \fbox{$ \displaystyle{z = \frac{\lambda_0-\lambda_E}{\lambda_E} \Leftrightarrow 1+z = \frac{a_0}{a(t_E)}} $}.
```
Le décalage spectral est à la fois directement lié au paramètre
d'échelle $a(t)$, mais aussi à une grandeur expérimentale directement
mesurable sur le spectre d'émission des objets distants. En effet, en
regardant la position des raies d'absorption et d'émission des objets
lointains, on peut en déduire leurs décalages spectraux par rapport aux
mêmes éléments chimiques situés sur Terre, au repos. Cette donnée
expérimentale est donc souvent associée à la définition des distances en
cosmologie.


:::{exercise} Mesure du redshift
:label: exo:redshift

Calculer les décalages vers le rouge des deux galaxies dont les spectres sont représentés ci-dessous.
La raie $H\beta$ de l'hydrogène (de la série Balmer) est mesurée à $486.1\,$nm dans le cadre du repos de l'atome.

```{list-table}
:header-rows: 0
:name: fig:redshifts

* - ```{image} ../images/spectra_galaxy.png
    :alt: sphere
    :width: 95%
    :align: center
    ```
* - ```{image} ../images/spectra_galaxy2.png
    :alt: plan
    :width: 100%
    :align: center
    ```
```


:::


:::{solution} exo:redshift
:class: dropdown

Pour le premier spectre de galaxie, la raie $H\beta$ est mesurée à $\lambda-0\approx 5100\,$Å, le décalage vers le rouge de la galaxie est donc :
\begin{equation}
z = \frac{\lambda_0-\lambda_E}{\lambda_E} = \frac{5100-4861}{4861} = 0.049
\end{equation} 
 
Pour le second spectre de galaxie, la raie $H\beta$ est mesurée à $\lambda-0\approx 5000\,$Å donc le décalage vers le rouge de la galaxie est :
\begin{equation}
z = \frac{\lambda_0-\lambda_E}{\lambda_E} = \frac{5000-4861}{4861} = 0.028
\end{equation}
:::


[^gammat]: Rien ne l'interdit, puisque $\gamma_{ij}$ peut dépendre du temps
[^g00]: On peut introduire une nouvelle variable temps $t'$ telle que $\dd t' = \sqrt{g_{00}}\dd t$.

