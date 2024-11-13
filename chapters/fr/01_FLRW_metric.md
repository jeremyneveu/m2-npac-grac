---
short_title: Métrique FLRW
authors:
  - jneveu
keywords: FLRW, cosmological principle, comobile, coordinates
---


La métrique de Friedmann-Lemaître-Robertson-Walker
================================


Principe cosmologique
-----------------------



:::{iframe} https://www.youtube.com/embed/UTlYUxucEZA?si=WZpcAuL1ElZuyvf6
:name: fig:sdss
:align: center
:width: 60%

Galaxy distribution compiled by the eBOSS survey. Every dot in this "pie" diagram is a galaxy, color coded by type: green for nearby galaxies, magenta and red for old red galaxies, blue for young blue galaxies, yellow and white for quasars. Credit: A. Raichoor (EPFL) / A. Ross (Ohio State Univ.) / SDSS Collaboration
:::

:::{figure} ../../images/CMB_planck.jpg
:name: fig:cmb_planck
:align: center
:width: 70%

Carte de température du fond diffus cosmologique micro-onde (CMB) observée par le satellite Planck. L'écart relatif observé entre la  température des points chauds (rouges) ou froids (bleus) par rapport à la moyenne est de l'ordre de $\delta \theta / \theta \approx 10^{-5}$.
:::

Pour être en mesure de construire un modèle de l'Univers, c'est-à-dire une construction théorique capable de décrire le contenu de l'Univers et son évolution, il faut parvenir à résoudre l'équation d'Einstein de la Relativité Générale. Cependant, jusqu'à quel niveau de détail est-il nécessaire d'aller pour le décrire suffisamment bien aux grandes échelles ? On se doute que paramétrer l'équation d'Einstein jusqu'à inclure l'échelle du système solaire est à la fois illusoire et non nécessaire. Quelle est la structure de l'Univers aux plus grandes échelles ? Ici la nature nous fait un beau cadeau, qui va simplifier considérablement l'écriture d'un modèle cosmologique à partir des équations de la Relativité Générale.

:::{important} Principe cosmologique

À des échelles suffisamment grandes, l'univers est spatialement homogène et isotrope.
:::

1.  l'Univers est homogène : la métrique ne dépend donc pas de la position d'un observateur dans l'espace, donc aucune position n'est particulière dans l'Univers. Cette affirmation, issue du principe Copernicien, n'est que statistiquement vraie car localement on observe bien que la matière a formé des grumeaux (planètes, étoiles, galaxies,\...) au milieu de larges vides. Cependant l'observation de l'Univers à grande échelle montre que l'Univers est bien globalement homogène à des échelles plus grandes que $100\,$Mpc[^pc] (voir [](#fig:sdss) et par exemple {cite:t}`Scrimgeour2012` pour une mesure de l'homogénéité de l'Univers par comptage de galaxies).

2.  l'Univers est isotrope: aucune direction n'est privilégiée. Ainsi, des observations effectuées dans deux directions différentes du ciel sont équivalentes. Ceci est bien vérifié par l'observation du fond diffus cosmologique micro-onde (CMB) dont la température est mesurée identique  à $2.725\pm0.002\,$K dans toutes les directions de l'espace  {cite:p}`Mather1999`. Seules des fluctuations de température de l'ordre de $10^{-5}$\,K sont détectées sur cette image de l'Univers jeune (voir [](#fig:cmb_planck) et par exemple {cite:t}`ThePlanckCollaboration2013XIII` pour une vérification du principe d'isotropie utilisant l'effet Sunyaev-Zeldovich).

Ignorer complètement ce qui se passe à des échelles "insuffisamment" grandes est la première étape pour construire une solution cosmologique à la Relativité Générale. Muni de ces faits observationnels, nous imposerons l'homogénéité et l'isotropie à la métrique et à la distribution de la matière (c'est-à-dire au tenseur énergie-impulsion).

:::{note} A propos de l'homogénéité de l'Univers
:class: dropdown 

Avant de présenter cette solution cosmologique, il est intéressant de se demander pourquoi le principe cosmologique devrait s'appliquer. Alors que la gravité, la force dominante qui façonne les structures à grande échelle de l'univers, tend à détruire l'homogénéité (une région légèrement sur-dense dans un univers homogène attirera la matière et deviendra de plus en plus sur-dense), il faut plus de temps pour que la matière aux grandes échelles forment des grumeaux. Comme les grandes échelles semblent plus homogènes dans les observations, on peut supposer que l'univers était beaucoup plus homogène dans le passé à toutes les échelles et qu'il le devient de moins en moins sous l'action de la gravité. Mais pourquoi était-il homogène à l'origine ? Une réponse logique est qu'une interaction autre que la gravité y a contribué (comme, par exemple, la pression dans un gaz parfait). Cependant, la Relativité Générale stipule qu'aucune interaction ne peut se propager plus vite que la vitesse de la lumière. Nous verrons que dans une théorie où l'évolution de l'univers découle d'un Big Bang initial, cela crée une difficulté potentielle : l'homogénéisation ne devrait être possible que jusqu'à des échelles égales à la distance parcourue par un photon entre le Big Bang et aujourd'hui.
:::


Univers de symétrie maximale
------------------

Étant donné le principe cosmologique, on cherche à déterminer la forme que doit prendre la métrique d'un Univers de symétrie maximale, c'est-à-dire un Univers dont les propriétés sont invariantes par rotation et translation {cite:p}`Weinberg1972`[p. 379].


### Métrique d'un Univers isotrope

:::{figure} ../../images/foliation.svg

Le diagramme d'espace-temps d'un Univers homogène et isotrope possède un axe temporel orthogonal aux vecteurs de base spatiaux à cause de l'isotropie de l'Univers. Chaque hypersurface à un instant $t$ est alors un Univers de densité homogène.
:::


Tout d'abord, si l'univers est isotrope,  on peut vérifier que les composantes croisées $g_{i0}$ et $g_{i0}$ sont nulles. Si tel n'était pas le cas, on aurait une direction privilégiée dans le l'univers. On peut s'en convaincre en remarquant que ces composantes sont non nulles si on réalise une transformation de Lorentz [](#eq:lorentz)-[](#eq:lorentz2), justement lorsqu'on prend un référentiel en translation uniforme par rapport à un autre, donc se déplaçant dans une direction choisie. 

Autre façon de se convaincre, prenons un espace-temps 2D. Si la métrique a la forme :
\begin{equation}
g=\begin{pmatrix} g_{00} & g_{01}  \\ g_{01} & g_{11} \end{pmatrix}
\end{equation}
alors l'équation des trajectoires de type lumière est :
$$
\dd s^2=0=g_{00}c^2\dd t^2+2g_{01}\,c\,\dd x\,\dd t+g_{11}\dd x^2.$$
On peut alors vérifier, en résolvant l'équation du second degré en $\dd t$ que si $g_{01} \neq 0$, deux $\dd x$ opposés donnent deux valeurs différentes de $\dd t$ positif. C'est-à-dire qu'un observateur recevra à des moments différents les impulsions lumineuses émises simultanément par deux sources situées à la même distance dans des directions opposées $\pm \dd x$. Cela rompt évidemment l'isotropie. Les termes $g_{0i}$ et $g_{i0}$ de la métrique sont donc nuls. Cela signifie que le vecteur temporel $\vec e_0$ est orthogonal aux vecteurs de base spatiaux $\vec e_i$.


De plus, si l'Univers est homogène alors la composante $g_{00}(t,\vec x)$ ne peut dépendre que du temps $t$, de sorte que le battement des horloges ne dépendent pas de la position dans l'espace. Donc $g_{00}(t,\vec x) = g_{00}(t)$ {cite:p}`Weinberg1972`[p. 403]. Si nous appelons le paramètre $t$ le temps, nous voyons que nous avons un temps universel en tout point de l'espace, appelé temps cosmologique. Comme l'univers est homogène, alors cela signifie qu'à chaque date on peut associer une densité de matière ou d'énergie identique pour tous les observateurs, donc qu'avec un densimètre on peut construire une horloge commune à tous les observateurs présents dans l'Univers. 

En combinant les deux résultats précédents, l'intervalle espace-temps peut être écrit sous la forme suivante :
\begin{equation}
\dd s^2= g_{00}(t) c^2 \dd t^2 + \dd \vec l^2
\end{equation}
où $\dd \vec l$ est un vecteur élémentaire spatial. Il est alors possible de fixer $g_{00}$ à $-1$ quitte à redéfinir la variable temps[^g00]. La métrique prend donc la forme :
\begin{equation}
g_{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\ 
0 & \gamma_{11} & \gamma_{12} & \gamma_{13} \\ 
0 &\gamma_{12} & \gamma_{22} & \gamma_{23} \\ 
0 &\gamma_{13} & \gamma_{23} & \gamma_{33} 
\end{pmatrix}
\end{equation}
où $\gamma_{ij}$ est la métrique spatiale, qui peut dépendre du temps et de la position, et comportant 6 composantes indépendantes inconnues (une métrique est un tenseur symétrique).

:::{attention} Convention de signature pour la métrique

Dans ce cours, comme dans beaucoup de cours de cosmologie, la [signature](https://en.wikipedia.org/wiki/Metric_signature) choisie pour la métrique est $(-,+,+,+)$. En effet, en cosmologie on manipule beaucoup des distances donc il est plus commode d'avoir des éléments de longueur positifs. En physique théorique des hautes énergies, la métrique $(+,-,-,-)$ est souvent préférée. Une compilation des différentes signatures utilisées est présentée [ici](https://en.wikipedia.org/wiki/Sign_convention).

:::


### Géométrie d'un Univers maximallement symétrique

Trouvons maintenant une forme explicite pour $\dd \vec l^2$. Un Univers de symétrie maximale (homogène et isotrope) doit posséder une courbure constante spatialement. Cela se comprend assez intuitivement mais aussi se démontre en Relativité Générale {cite:p}`Weinberg1972` [p. 381]. Notons $a$ le rayon de courbure associé, et soit $\vec \xi = (\xi^1, \xi^2, \xi^3)$ un vecteur position dans l'espace 3D :
\begin{equation}
\dd \vec l^2 = \gamma_{ij} \dd \xi^i \dd \xi^j, \quad \text{avec}\quad i=1,2,3
\end{equation}


Tout d'abord, si cet espace possède une courbure nulle, alors la distance élémentaire $\dd \vec l$ s'écrit simplement :
\begin{equation}
\dd \vec l^2 =   \delta_{ij}\dd \xi^i \dd \xi^j,\quad \gamma_{ij} = \delta_{ij}
\end{equation}

Travaillons maintenant sur le cas où la courbure est non nulle. Pour décrire la courbure d'une surface avec des notions de géométries habituelles, étudions-la dans un espace avec une dimension supplémentaire. Plaçons cet espace 3D non euclidien (courbé) dans un espace 4D de métrique $C_{AB}$ avec des coordonnées cartésiennes $(x, y, z, w)$. Posons $r^2 = x^2 + y^2 + z^2$ la distance euclidienne dans le sous-espace 3D. On a alors deux hyper-surfaces 3D possibles, de courbure de Gauss constante $1/a^2$ {cite:p}`Baumann` :
- une 3-sphère de rayon $a$ si elle est plongée dans un espace Euclidien 4D : 
\begin{equation}
\quad  C_{AB} = \mathrm{diag}(1,1,1,1), \quad r^2 + w^2= a^2,\quad  \dd \vec l^2 = \dd r^2 + \dd w^2
\end{equation}
- une 3-hyperboloïde de courbure $a$ si elle est plongée dans un espace Lorentzien 4D :
\begin{equation}
 \quad C_{AB} = \mathrm{diag}(1,1,1,-1),\quad r^2 - w^2= -a^2,\quad  \dd \vec l^2 = \dd r^2 - \dd w^2
\end{equation}

:::{figure} ../../images/sphere_euclid.svg

Espace sphérique 2D de rayon $a$ représenté dans un espace euclidien 3D $(x,y,w)$. À une coordonnée $\vec \xi = (\xi_1, \xi_2)$, on souhaite exprimé la longueur d'un vecteur élémentaire tangent à la sphère $\dd \vec l$ dans les deux espaces.
:::

Les deux derniers cas de courbures strictement positive ou négative sont donc définis par *l'équation de contrainte* :
:::{math}
:label: eq_hyp_sph
r^2 \pm w^2= \pm a^2(t) 
:::
où on autorise ici le rayon $a(t)$ à dépendre du temps, car a priori $\gamma_{ij}$ peut dépendre du temps.

:::{tip} Notion de courbure
:class: dropdown

Si ces raisonnements vous troublent, rappelez-vous que c'est comme décrire la courbure d'un cercle de rayon $R$. Un cercle est un objet à une dimension car il n'y a qu'une seule direction de déplacement sur cet objet, paramétré par un angle $\theta$ par exemple). Mais il peut aussi se décrire dans un plan 2D, avec deux coordonnées $x$ et $y$ liées par l'équation :
\begin{equation*}
x^2 + y^2 = R^2
\end{equation*}
De même, une sphère (objet à deux dimensions) peut être étudiée dans un espace avec une troisième dimension, donc trois coordonnées $(x,y,z)$ liées par l'équation :
\begin{equation*}
x^2 + y^2 + z^2 = R^2
\end{equation*}

La notion de courbure peut se calculer soit intrinsèquement, soit à l'aide d'une dimension supplémentaire. Intrinsèquement, un être vivant sur un cercle peut mesurer sa courbure en mesurant le chemin parcouru lors d'un tour : il en déduira que la courbure de son cercle est $1/R^2$ avec $R$ déduit du périmètre parcouru $l = 2\pi R$. S'il est capable de sortir du cercle et de voyager dans une seconde dimension, il pourra observer son cercle depuis l'extérieur et mesurer aussi la courbure de son Univers.

:::

La distance infinitésimale $\dd \vec l^2$ entre deux points de l'hypersurface définie dans l'espace 3D courbe de métrique $\gamma_{ij}$ doit être identique à celle mesurée dans l'espace 4D, donc :
\begin{equation}
\dd \vec l^2= \gamma_{ij} \dd \xi^i \dd \xi^j =  \dd r^2 \pm \dd w^2
\end{equation}
où le cas $+$ correspond à une géométrie sphérique, le cas $-$ à une géométrie hyperbolique {cite:p}`Weinberg1972` [p. 390-391].

Or, l'équation de contrainte [](#eq_hyp_sph) lie $r, w$ et $a$ donc on peut remplacer $\dd w$ par une expression fonction de $r$ et $a$ (donc sans la quatrième dimension). La différentiation de l'équation [](#eq_hyp_sph) donne la relation 
$$
(\vec r \cdot \dd \vec r) \pm w\dd w=0,$$
donc, en injectant de nouveau l'équation [](#eq_hyp_sph), on obtient :
\begin{equation}
(\vec r \cdot \dd \vec r)^2=(w\dd w)^2 \Rightarrow (\dd w)^2= \frac{(\vec r \cdot \dd \vec r)^2}{w^2} = \frac{(\vec r \cdot \dd \vec r)^2}{a^2(t) \mp r^2}
\end{equation}
La distance infinitésimale entre 2 points de l'espace 3D non euclidien de courbure non nulle constante $a^{-2}$ est alors :
\begin{equation}
\dd \vec l^2= \dd \vec r^2 \pm \frac{(\vec r \cdot \dd \vec r)^2}{a^2(t)\mp r^2} 
\end{equation}

A cette étape, nous pouvons maintenant combiner le résultat obtenu pour les deux courbures non nulles avec le cas euclidien en introduisant le *paramètre de courbure* $k$ :
\begin{equation}
\label{K-def}
k = \left\lbrace
\begin{array}{rl}
 +1 & \text{3-sphère} \\
 0 & \text{espace\ plat} \\
 -1 & \text{3-hyperboloïde} \\
\end{array}\right.
\end{equation}
On a ainsi pour les trois géométries possibles[^flat] d'un Univers maximallement symétrique :
\begin{equation}
\dd \vec l^2= \dd \vec r^2 + k\frac{ (\vec r \cdot \dd \vec r)^2}{a^2(t) - k r^2}
\end{equation}
où dans le cas d'un espace plat on aurait $\vec r = \vec \xi$.

Enfin, introduisons la variable rééchelonnée $\vec\sigma=\vec r/a(t)$, et nous obtenons une nouvelle expression :
\begin{equation}
\dd \vec{l}^2= a^2(t) \left(\dd \vec \sigma^2 + k\frac{(\vec{\sigma} \cdot \dd \vec{\sigma})^2}{1 - k \sigma^2} \right)
\end{equation}

La métrique de Friedmann-Lemaître-Robertson-Walker décrivant un Univers homogène et isotrope s'écrit finalement :
\begin{equation}
\label{FLRW-metric}
\dd s^2=-c^2\dd t^2 + a^2(t) \left(\dd \vec \sigma^2 + k\frac{(\vec \sigma \cdot \dd \vec \sigma)^2}{1 - k \sigma^2} \right)
\end{equation}

La métrique de Friedmann-Lemaître-Robertson-Walker (FLRW) constitue le cadre de base du modèle cosmologique standard. Les hypothèses d'homogénéité et d'isotropie ont directement conduit à une métrique décrivant un univers avec seulement trois géométries possibles (plat, 3-sphère, 3-hyperboloid) et un facteur d'échelle $a(t)$ affectant les distances. Notez que, grâce à l'imposition des symétries d'homogénéité et d'isotropie, nous avons réduit l'écriture de la métrique $g_{\mu\nu}$ (qui est un tenseur symétrique) constituée a priori de 10 composantes indépendantes inconnues à un tenseur possédant une seule fonction inconnue $a(t)$.


:::{important} Où sont les unités ?
L'élément de distance $\dd s$ possède la dimension d'une longueur, par conséquent tous les termes de l'équation [](#FLRW-metric) aussi. 

Certains ouvrages proposent que le facteur d'échelle soit une fonction du temps sans dimension, et que $\sigma$ garde la dimension d'une longueur, normalisée par $a(t)$. Ceci permet de tout définir en particulier en posant qu'aujourd'hui le facteur d'échelle vaut $a_0=1$, mais alors il faut redéfinir $k$ et lui donner l'unité d'une courbure (inverse d'une distance au carré).

Dans ce cours, nous allons abondamment traiter des distances en cosmologie, et dans ce cas il est plus commode de penser que le facteur d'échelle est homogène à une longueur, et que les coordonnées spatiales $\vec \sigma$ forment un vecteur sans dimension. Le paramètre de courbure $k$ est alors un entier sans dimension également.

:::

Il est important de comprendre la signification physique du facteur d'expansion $a(t)$. Tout d'abord, d'après l'équation [](#FLRW-metric), ce facteur relie la distance physique $\vec r$ et la distance de coordonnées $\sigma$ par $\vec r=a(t)\vec \sigma$. Une particule dont les coordonnées spatiales $\vec \sigma$ sont fixes verra sa distance physique avec un observateur en $\vec \sigma=\vec 0$ augmenter (ou diminuer) avec le temps. Cette variation de la distance se réalise à la vitesse apparente :
$$
\frac{\dd \vec r}{\dd t} = \frac{\dd a(t)\vec \sigma}{\dd t} = \dot a \vec \sigma + a \dot{\vec \sigma} = \frac{\dot a}{a} \vec r
$$
car $\dot{\vec \sigma} = \vec 0$ si la particule n'a pas de mouvement propre, avec le point $\;\dot{}\;$ exprimant une dérivée par rapport au temps $t$. On obtient donc une relation directe entre la distance à un observateur central et la vitesse apparente : c'est la *loi de Hubble*. Le taux d'éloignement est donné par le paramètre de Hubble, qui quantifie la vitesse de variation du facteur d'échelle : 
\begin{equation}
\label{eq:H-def}
\boxed{\displaystyle H(t) = \frac{\dot a(t)}{a(t)}}
\end{equation}

Pour un univers sphérique, le facteur d'échelle $a(t)$ représente également son rayon de courbure. Un univers sphérique dynamique correspond donc à un univers possédant un rayon de courbure variable dans le temps. Un espace plat ne possède pas d'échelle caractéristique, la valeur de $a(t)$ n'est donc pas une observable physique. La quantité ayant un sens physique pour un tel univers est le paramètre de Hubble $H(t)$.

Dans le but d'alléger les notations, la dépendance temporelle des paramètres ne sera pas toujours explicitée, de sorte que $a(t)=a$. On désignera les paramètres évalués au temps présent $t_0$ par l'indice ou l'exposant 0 si bien que $a(t_0)=a_0$. Dans la suite, nous travaillerons dans le système où $a_0$ *n'est pas fixé* à 1. 

:::{list-table} Représentation des équivalents à deux dimensions des trois espaces solution des principes cosmologiques: la 2-sphère, le plan, le 2-hyperboloïde.
:header-rows: 0
:name: fig:espaces

* - :::{image} ../../images/sphere.jpeg
    :alt: sphere
    :width: 95%
    :align: center
    :::
  - :::{image} ../../images/plan.jpeg
    :alt: plan
    :width: 100%
    :align: center
    :::
  - :::{image} ../../images/hyperboloid.jpeg
    :alt: hyperboloid
    :width: 90%
    :align: center
    :::
:::

:::{note} Que signifie vivre dans un espace courbé ?

La [](#fig:espaces) représente des surfaces 2D plongées dans des espaces 3D. Mais comment se représenter que nous vivrions dans une 3-sphère ? Et qu'est-ce que cela implique ? Vivre dans un espace courbé implique que la somme des angles d'un triangle n'est pas égale à 180°: elle est supérieure pour une 3-sphère et inférieure pour un 3-hyperboloid. C'est ainsi que les deux triangles bleus [](#fig:triangles_on_sphere) ont une somme de leurs angles supérieures à 180°. Dans une 3-sphère nous pouvons avoir l'impression que deux objets sont éloignés angulairement, alors qu'en en fait leur distance qui les sépare est plus petite que ce qu'elle serait dans un espace plat. Et ceci dans toutes les directions de l'espace. 

En résumé, vivre dans un espace courbé signifie que la relation entre angles et longueurs est déformée par rapport à notre intuition euclidienne, en tous cas sur des distance cosmologiques.


```{figure} ../../images/triangles_on_sphere.svg
:name: fig:triangles_on_sphere 
:align: center

Prenons deux galaxies: elles forment un triangle avec la Terre, qui, dans une 3-sphère, possède trois angles dont la somme est supérieure à 180°. 
```

:::

Coordonnées comobiles
---------------------

Il est important de noter que tous les observateurs ne voient pas l'Univers comme isotrope, mais seulement les observateurs dits *comobiles*, qui sont localement au repos avec l'essentiel de la matière dans leur voisinage. Nous, par exemple, ne sommes pas des observateurs mobiles : lorsque nous observons la température du CMB, la première caractéristique que nous voyons est un grand dipôle de température (plus chaud d'un côté, plus froid du côté opposé), qui est le résultat du mouvement particulier de notre système solaire dans la galaxie, et de notre galaxie dans l'Univers (et de notre groupe de galaxies). Si on retranche ce mouvement propre par rapport au référentiel du CMB, alors cela ferait de nous des observateurs comobiles. Ainsi, on peut définir un système de coordonnées associés à des observateurs sans mouvements propres, dont les distances propres relatives n'augmentent qu'avec le facteur d'échelle $a(t)$ {cite:p}`Weinberg1972`[p. 409].

Dans la métrique FLRW où l'expansion de l'Univers est factorisée par un facteur d'échelle $a(t)$, les coordonnées spatiales $\vec \sigma$ sont appelées *coordonnées comobiles*. Il existe une grande liberté dans le choix des coordonnées comobiles. 

### Coordonnées sphériques

On privilégie souvent les coordonnées sphériques $(ct, \sigma, \theta, \phi)$ avec l'observateur (nous-mêmes) à l'origine, telles que :
\begin{equation}
\begin{aligned}
\sigma_1 &= \sigma \sin \theta \cos \phi \\
\sigma_2 &= \sigma \sin \theta \sin \phi \\
\sigma_3 &= \sigma \cos \theta
\end{aligned}
\end{equation}
Après des calculs simples mais longs (voir notebook et [ici](`https://en.wikipedia.org/wiki/Spherical_coordinate_system#Integration_and_differentiation_in_spherical_coordinates`)), dans les trois cas de courbures la métrique FLRW s'écrit :
\begin{equation}
\label{eq:FLRW-metric-spherical}
\dd s^2=-c^2\dd t^2 + a^2(t) \left( {1 \over 1-k\sigma^2}\dd \sigma^2 + \sigma^2 \dd \theta^2 + \sigma^2 \sin^2 \theta \dd \phi^2\right)
\end{equation}

:::{note} Courbure et finitude de l'Univers
:class: dropdown

Pour la 3-sphère, 3-hyperboloïde et le plan, la courbure de ces surfaces est {cite:p}`Weinberg1972`[p. 412]:
$$ K(t) = \frac{k}{a^2(t)}$$
La 3-hyperboloïde et le plan sont d'extension infinie. En revanche, la 3-sphère est d'extension finie mais reste non bornée : une particule ne rencontrera jamais 
de bord mais on peut définir un volume :
$$V(t) = 2 \pi^2 a^3(t)$$
et un périmètre (longueur d'un méridien) :
$$L(t) = 2 \pi a(t)$$
:::


### Coordonnées cartésiennes

Le cas de l'univers plat simplifie beaucoup les calculs qui suivront. Étant donné que l'hypothèse d'une courbure nulle est compatible avec les contraintes de plus en plus fortes des observations cosmologiques, nous concentrerons désormais nos développements analytiques sur l'univers plat, en mentionnant des résultats pour le cas général lorsque cela est nécessaire. Dans le cas de courbure nulle, il peut être pratique d'utiliser les coordonnées comobiles cartésiennes $(ct, x, y, z)$, telles que :
\begin{equation}
\sigma_1  = x,\quad \sigma_2  = y,\quad\sigma_3  = z,\quad\sigma^2  = x^2 + y^2 + z^2
\end{equation}
La métrique FLRW s'écrit dans un univers plat :
\begin{equation}
g_{\mu\nu} = 
\begin{pmatrix}
-1 & 0 & 0 & 0 \\ 
0 & a^2(t) & 0 & 0 \\ 
0 & 0 & a^2(t) & 0 \\ 
0 & 0 & 0 & a^2(t)
\end{pmatrix}
\end{equation}


Géodésiques dans la métrique FLRW
---------------------------------

Quelle est la trajectoire d'une particule en chute libre dans une métrique FLRW ? D'après la Relativité Générale, nous savons qu'une telle particule se déplace le long d'une géodésique $x^\mu(s)$ dont l'équation est la suivante :
\begin{equation}
\label{geodesic}
{\dd^2 x^\mu \over \dd  s^2} +\Gamma^{\mu}_{\,\,\nu\kappa} {\dd x^\nu \over \dd  s}{\dd x^\kappa \over \dd  s}=0,
\end{equation} 
où $s$ est un paramètre quelconque décrivant la position le long de la géodésique (le temps propre par exemple). Une autre forme de l'équation des géodésiques va ici nous aider, obtenue à partir de la définition de la dérivée covariante [](#eq:dcov-cov) :
\begin{equation}
\label{geodesic-cov}
{\dd^2 x_\mu \over \dd  s^2} -\Gamma^{\nu}_{\,\,\mu\kappa} {\dd x_\nu \over \dd  s}{\dd x^\kappa \over \dd  s}=0.
\end{equation} 
Définissons la quadri-vitesse $U^\mu$ le long d'une ligne d'Univers par $U^\mu = \dd x^\mu / \dd s$. Alors :
\begin{equation}
{\dd U_\mu \over \dd  s} = \Gamma^{\nu}_{\,\,\mu\kappa} U_\nu U^\kappa=  \frac{1}{2} \frac{\partial g_{\alpha\beta}}{\partial x^\mu} U^\alpha U^\beta.
\end{equation} 

:::{note} Démonstration
:class: dropdown

L'égalité précédente est démontrée dans {cite:t}`hobson2006general`[p. 81]. En voici l'essentiel :
\begin{align*}
\Gamma^{\nu}_{\,\,\mu\kappa} U_\nu U^\kappa
& = \frac{1}{2}g^{\lambda\nu}\left( \frac{\partial g_{\lambda\kappa}}{\partial x^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x^\kappa}  - \frac{\partial g_{\mu\kappa}}{\partial x^\lambda} \right) U_\nu U^\kappa \\
& = \frac{1}{2}\left( \frac{\partial g_{\lambda\kappa}}{\partial x^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x^\kappa}  - \frac{\partial g_{\mu\kappa}}{\partial x^\lambda} \right) U^\lambda U^\kappa  
= \frac{1}{2} \frac{\partial g_{\lambda\kappa}}{\partial x^\mu} U^\lambda U^\kappa
\end{align*}
car la métrique est un tenseur symétrique donc ${\partial_\kappa g_{\mu\lambda}} - {\partial_\lambda g_{\mu\kappa}} = 0$.
:::

A partir de cette forme de l'équation des géodésiques (voir {cite:p}`hobson2006general`[p. 81] pour une démonstration), calculons la forme que doit prendre le vecteur contravariant $U^\nu$ dans une métrique FLRW pour une particule en chute libre.

Commençons par le cas $\mu=3$ et utilisons les coordonnées sphériques $(\sigma,\theta,\phi)$. Comme la métrique FLRW ne dépend pas de $\phi$, alors :
$$
\frac{\dd U_3}{\dd s} = 0
$$
donc $U_3$ est une constante du mouvement. Or, on a par ailleurs :
$$
U_3 = g_{33} U^3 = a^2(t) (\sigma \sin \theta)^2 U^3 $$
dont l'expression s'annule à l'origine en $\sigma=0$, là nous observons. Comme la composante $U_3$ est constante alors elle est identiquement nulle le long de la trajectoire. On en déduit :
$$U^3 = \frac{\dd \phi }{ \dd s} = 0 \Rightarrow \phi = \text{constante}$$

Passons au cas $\mu=2$. La seule composante de la métrique dépendant de $\theta$ est 
$g_{33}$ mais $U_3$ est identiquement nul donc :
$$\frac{\dd U_2}{\dd s} = \frac{1}{2} \frac{\partial g_{\alpha\beta}}{\partial x^2} U^\alpha U^\beta = \frac{1}{2} \frac{\partial g_{33}}{\partial x^2} U^3 U^3 = 0.$$
Or de même on a par ailleurs :
$$U_2 = g_{22} U^2 = a^2(t) \sigma^2 U^2 $$
qui s'annule en $\sigma=0$ donc $U^2$ est nul tout le long de la trajectoire. On en déduit :
$$U^2 = \frac{\dd \theta }{ \dd s} = 0 \Rightarrow \theta = \text{constante}$$

:::{important}
En coordonnées sphériques, les géodésiques passant par l'origine sont les trajectoires vérifiant :
$$
\boxed{\theta=\text{constante},\quad \phi=\text{constante}}
$$
:::


Le décalage spectral, ou redshift
----------------------------------


:::{figure} ../../images/distances2.svg
:name: fig:distances_croquis
:align: center
:width: 60%

Notations pour le calcul du redshift et des distances cosmologiques en coordonnées comobiles.
:::

Pour mesurer l'histoire de l'expansion de l'Univers, il faut avoir accès au paramètre d'échelle $a(t)$. Ceci est possible par la mesure du décalage spectral de la lumière venant de sources distantes. Dans la métrique FLRW, plaçons-nous par convention au centre ($\sigma=0$), et considérons un objet situé aux coordonnées comobiles $\left(\sigma_E,\theta_E,\phi_E\right)$, émettant un photon à l'instant $t_E$ (voir [](#fig:distances_croquis)). Pour ce photon, voyageant à la vitesse de la lumière, dans la métrique FLRW on a, à tout instant:
:::{math}
:label: eq:ds2_lumiere

\dd s^2=0=-c^2 \dd t^2+\frac{a^2(t)}{1-k\sigma^2}\dd \sigma^2.
:::
car le long de sa géodésique $\theta$ et $\phi$ sont constants ($\dd \theta = \dd \phi=0$). Posons $t_0$ l'instant de la réception de cette onde en $\sigma=0$. Alors grâce à l'équation précédente on a la relation : 
:::{math}
:label: eq:comobile

\int_{t_E}^{t_0} \frac{c\dd t}{a(t)} =  -\int_{t_0}^{t_E} \frac{c\dd t}{a(t)} 
= \int_0^{\sigma_E}\frac{\dd\sigma}{\sqrt{1-k\sigma^2}}
= \left\lbrace
\begin{array}{cl}
    \arcsin \sigma_E & \text{ si } k=+1 \\
    \sigma_E & \text{ si } k=0 \\
    \text{arcsh}\,\sigma_E & \text{ si } k=-1 
\end{array}
\right. .
::: 
avec $\dd \sigma < 0$ pour $\dd t > 0$ en considérant un photon allant de la source vers l'observateur en 0.


Pour une onde électromagnétique de période $T$, l'expression [](#eq:ds2_lumiere) étant valable à tout instant, on peut calculer la même intégrale pour l'onde émise à l'instant $t_E+T_E$ et reçue à l'instant $t_0+T_0$ (on suppose donc que la période $T$ va varier au cours du temps): 
$$
\label{eq:comobileT}
\int_{t_E+T_E}^{t_0+T_0} \frac{c \dd t}{a(t)}= \int_0^{\sigma_E}\frac{\dd \sigma}{1-k\sigma^2}.
$$
Par égalité des expressions [](#eq:comobile) et [](#eq:comobileT), comme la période $T$ est petite devant les variations du facteur d'échelle $a(t)$ pour les ondes électromagnétiques usuelles, on obtient: 
$$
\begin{aligned}
\int_{t_E+T_E}^{t_0+T_0} \frac{c\dd t}{a(t)} & =\int_{t_E}^{t_0} \frac{c\dd t}{a(t)}  
\Leftrightarrow \int_{t_E+T_E}^{t_E} \frac{c\dd t}{a(t)}  =\int_{t_0+T_0}^{t_0} \frac{c\dd t}{a(t)} \\
\Leftrightarrow \frac{cT_0}{a(t_0)} & = \frac{c T_E}{a(t_E)}  
\Leftrightarrow \frac{\lambda_0}{\lambda_E}  = \frac{a(t_0)}{a(t_E)}\label{eq:redshift2}
\end{aligned}
$$
Directement, si l'espace est en expansion alors $a(t_E) < a(t_0)$ et la longueur d'onde reçue $\lambda_0$ est donc supérieure à la longueur d'onde émise $\lambda_E$. On définit alors le décalage spectral, communément appelé _redshift_ en raison du fait que la quasi-totalité des spectres des galaxies observées sont décalées vers le rouge, par :
:::{math}
:label: eq:redshift

 \boxed{ \displaystyle{z = \frac{\lambda_0-\lambda_E}{\lambda_E} \Leftrightarrow 1+z = \frac{a_0}{a(t_E)} }}
:::
Le décalage spectral est à la fois directement lié au paramètre d'échelle $a(t)$, mais aussi à une grandeur expérimentale directement mesurable sur le spectre d'émission des objets distants. En effet, en regardant la position des raies d'absorption et d'émission des objets lointains, on peut en déduire leurs décalages spectraux par rapport aux mêmes éléments chimiques situés sur Terre, au repos. Cette donnée expérimentale est donc souvent associée à la définition des distances en cosmologie.


:::{exercise} Mesure du redshift
:label: exo:redshift

Calculer les décalages vers le rouge des deux galaxies dont les spectres sont représentés ci-dessous.
La raie $H\beta$ de l'hydrogène (de la série Balmer) est mesurée à $486.1\,$nm dans le cadre du repos de l'atome.

```{list-table}
:header-rows: 0
:name: fig:redshifts

* - :::{image} ../../images/spectra_galaxy.png
    :alt: sphere
    :width: 95%
    :align: center
    :::
* - :::{image} ../../images/spectra_galaxy2.png
    :alt: plan
    :width: 100%
    :align: center
    :::
```

:::


:::{solution} exo:redshift
:class: dropdown

Pour le premier spectre de galaxie, la raie $H\beta$ est émise à $\lambda_E = 4861\,$Å et mesurée à $\lambda_0\approx 5100\,$Å, le décalage vers le rouge de la galaxie est donc :
\begin{equation}
z = \frac{\lambda_0-\lambda_E}{\lambda_E} = \frac{5100-4861}{4861} = 0.049
\end{equation} 
 
Pour le second spectre de galaxie, la raie $H\beta$ est mesurée à $\lambda_0\approx 5000\,$Å donc le décalage vers le rouge de la galaxie est :
\begin{equation}
z = \frac{\lambda_0-\lambda_E}{\lambda_E} = \frac{5000-4861}{4861} = 0.028
\end{equation}

:::




Distance propre et distance comobile
------------

La *distance propre* définit la distance physique entre deux objets à un instant $t$. Soit un objet émetteur situé aux coordonnées comobiles $(\sigma_E, \theta_E, \phi_E)$. Par définition, la distance propre entre cet objet et un observateur situé à l'origine est le long d'une courbe à $\theta$ et $\phi$ constants et vaut :
:::{math}
:label: eq:dist-prop

D_p(\sigma_E, t) = \int_0^{\sigma_E} 
\sqrt{g_{\sigma\sigma}}\dd\sigma' 
= \int_0^{\sigma_E}\frac{a(t)\dd\sigma'}{\sqrt{1-k\sigma'^2}} = a(t) \chi(\sigma_E)
:::
où on fait apparaître $\chi(\sigma_E)$ la _distance comobile_ entre cet objet et l'observateur :
:::{math}
:label: eq:dist-comobile

\chi(\sigma_E) = \int_0^{\sigma_E}\frac{\dd\sigma'}{\sqrt{1-k\sigma'^2}}
= \left\lbrace
\begin{array}{cl}
    \arcsin\sigma_E & \text{ si } k=+1  \\
    \sigma_E  & \text{ si } k=0 \\
    \text{arcsh}\,\sigma_E & \text{ si } k=-1 
\end{array}
\right.
:::
On voit que la distance propre $D_p$ possède bien l'unité d'une longueur alors que la distance comobile est sans dimension. Cette dernière représente la distance dans l'espace des coordonnées et est indépendante de l'expansion de l'Univers. En revanche la distance propre évolue dans le temps avec le facteur d'échelle.

Réciproquement, on définit $f_k(\chi)$ ainsi :
\begin{equation}
\sigma = f_k(\chi) = 
\left\lbrace
\begin{array}{cl}
    \sin\chi & \text{ si } k=+1  \\
    \chi  & \text{ si } k=0 \\
    \sinh\chi & \text{ si } k=-1 
\end{array}
\right.
\end{equation}

Imaginons maintenant que cette distance puisse être perçue par le voyage d'un photon. La lumière voyage en suivant une géodésique, donc dans la métrique FLRW on a bien $\dd \theta=\dd \phi=0$ et :
\begin{equation}
\dd s^2=0=-c^2 \dd t^2+\frac{a^2(t)}{1-k\sigma^2}\dd\sigma^2.
 \end{equation} 
Donc :
$$
\frac{\dd\sigma}{\sqrt{1-k\sigma^2}} = - \frac{c \dd t}{a(t)}
$$ 
avec le photon voyageant le long de la direction $\dd \sigma<0$ pour $\dd t > 0$. La distance comobile se réécrit :
\begin{equation}
\chi(\sigma_E) =  \int_0^{\sigma_E}\frac{\dd\sigma}{\sqrt{1-k\sigma^2}} = \int_{t_0}^{t_E} -\frac{c\dd t'}{a(t')}= \int_{t_E}^{t_0} \frac{c\dd t'}{a(t')} = \chi(t_E)
\end{equation}
Exprimons cette distance en fonction du redshift $z$, qui, on le rappelle, est une observable expérimentale. Les intégrales peuvent se transformer entre les variables $t$, $a$ grâce à la définition du taux d'expansion $H(t)$, et entre les variables $a$ et $z$ grâce à la définition du redshift :
\begin{equation}
H= \frac{1}{a}\frac{\dd a}{\dd t} \Rightarrow \dd t = \frac{1}{aH} \dd a
\end{equation}
\begin{equation}
a = \frac{a_0}{1+z} \Rightarrow \dd a = -a_0 \frac{\dd z}{(1+z)^2}\Rightarrow \frac{\dd a}{a} = -\frac{\dd z}{1+z}
\end{equation}
D'où la distance comobile en terme de temps $t$, facteur d'échelle $a$ et redshift $z$ :
\begin{align}
\chi(\sigma_E) & = \chi(t_E) = \int_{t_E}^{t_0} \frac{c\dd t'}{a(t')} = \int_{a_E}^{a_0} \frac{c\dd a}{a^2 H(a)} \\
& = -\int_z^0 \frac{1+z}{a_0}\frac{-c\dd z}{(1+z)H(z)} = \frac{1}{a_0}\int_0^z\frac{c\dd z}{H(z)} = \chi(z)
\end{align}
On résume dans le tableau [](#tab:atz) comment se convertissent les paramètres $a$, $t$ et $z$ à différents moments dans la chronologie de l'Univers.

:::{table} Conversion des paramètres $a$, $t$ et $z$. On note $t_U$ l'âge de l'Univers aujourd'hui.
:align: center
:label: tab:atz

|  | a | t | z |
| --- | --- | --- | --- | 
| réception (aujourd'hui) | $a_0$ | $t_U$ | 0 |
| émission (passé) | $a_E$ | $t_E$ | $z$ |
| début de l'Univers | $0$ | $0$ | $+\infty$ |
| fin des temps | $+\infty$ | $+\infty$ | -1 |

:::

La distance propre est la distance que l'on pourrait mesurer effectivement à un instant $t$ entre deux objets. Si on choisit un objet situé à la coordonné comobile $\sigma_E$ et un observateur comobile en 0, la distance propre aujourd'hui à $t_0$ s'écrit alors simplement pour les trois cas de courbure :
$$D_p(z) = a_0 \chi(z) =\int_0^z\frac{c \dd z}{H(z)} $$
et s'exprime bien en unités de longueur. La notion de distance propre est illustrée [](#fig:distances).


:::{figure} ../../images/distances.svg
:name: fig:distances
:align: center
:width: 100%

Distance propre entre la Terre et une galaxie lointaine sans vitesse propre apparente. (a) Aujourd'hui, la distance mesurée entre la Terre et cette galaxie est de $a_0 \sigma$ années-lumière dans un espace plat. (b) A une autre date $t$, cette distance évolue et vaut $a(t) \sigma$. (c) Distance propre dans un espace sphérique.

:::


:::{exercise} Coordonnées comobiles sur la sphère
:label: exo:sphere-comobile

Pour se créer une intuition sur la géométrie courbe et les coordonnées comobiles, nous allons étudier une sphère 2D de rayon $a(t)$. Sur cette sphère, les coordonnées sont données par l'angle polaire $\chi$ et la longitude $\theta$ (la coordonnée $\phi$ est donc omise par rapport au cas FLRW). Considérons qu'un observateur est situé en $(\chi,\theta)=(0, 0)$ et une galaxie en $(\chi, 0)$. 

1. Représenter une sphère et tracer le méridien $\theta = 0$. Placer les quantités suivantes : l'observateur, la galaxie, $a(t)$, $\chi$, la distance propre entre l'observateur et la galaxie $D_p$. Relier ces quantités à la coordonnée $\sigma$ et à l'expression de $D_p$.


2. Considérons maintenant deux galaxies à la même coordonnées $\chi$, séparées par la distance physique $l$. Montrer que l'angle $\theta$ sous lequel elles sont observées sur la sphère est $\theta = l / (a(t) \sigma)$  si $\theta \ll 1$.

:::

:::{solution} exo:sphere-comobile
:label: exo:sphere-comobile-sol
:class: dropdown

1. La coordonnée comobile $\chi$ est explicitement l'angle polaire entre l'observateur et la galaxie. La distance propre est la longueur de l'arc qui est $D_p = a(t) \chi$ comme dans la géométrie habituelle. La coordonnée $\sigma$ est liée à la longueur $b$ de la corde à cet angle $\chi$ par :
\begin{equation}
\sigma = \sin \chi = \frac{b}{a(t)}
\end{equation}
Notons également que $b$ est le rayon du cercle de colatitude $\chi$ : $b = a(t) \sin \chi$. 

2. Avec la projection polaire [](#fig:projection_polaire), on voit que $\theta$ est l'angle délimitant un arc de taille $l$ et de rayon $b$, le rayon du cercle de latitude de $\chi$. Ainsi :
\begin{equation}
\theta = \frac{l}{b} = \frac{l}{a(t) \sin \chi} = \frac{l}{a(t) \sigma}
\end{equation}
Grâce au paramétrage $\sigma=f_k(\chi)$, on voit que cette égalité fonctionne en espace plat et en espace courbe.

Si on préfère un raisonnement mathématique plutôt que graphique, en utilisant la métrique FLRW, nous pouvons démontrer également :
\begin{equation}
l = \int_0^d \dd l' = \int_0^\theta \sqrt{g_{\theta\theta}} a(t)\dd\theta' = a(t) \int_0^\theta f_k(\chi) \dd\theta' = a(t) \theta \sin\chi = a(t) \theta \sigma
\end{equation}
Donc on obtient de nouveau $\theta = l / a(t) \sigma$.

Il est facile de vérifier que nous avons les mêmes expressions dans le cas plat, et nous les admettrons dans la géométrie hyperbolique. La coordonnée $\sigma$ est donc utile pour faire des calculs et des dessins dans le cas plat et traduire ces résultats dans les cas courbes (ce qui n'est pas si facile avec $\chi$).


```{figure} ../../images/spherical_universe.svg
:width: 100%
:align: center
:label: fig:projection_polaire
    
Géométrie dans un univers sphérique.
```

:::



:::{warning}

Ni la distance propre ni la distance comobile ne sont mesurables car elles supposent de pouvoir s'affranchir de l'expansion de l'Univers. Or, en cosmologie, on veut mesurer des distances et leur évolution pour en déduire le comportement de $a(t)$ et donc le comportement du contenu de l'Univers. Traditionnellement, la cosmologie utilise les photons comme messagers venant des galaxies les plus lointaines. L'observation des astres lumineux peut nous conduire à déterminer des distances selon au moins deux de leurs aspects: leur luminosité et leur taille apparente. On peut ainsi définir deux distances basées sur l'observation des flux lumineux $\Phi$ et des tailles angulaires $\delta$ :
$$
\Phi = \frac{L}{4\pi D_L^2}, \qquad \delta = \frac{l}{D_A}
$$
où $L$ est la luminosité intrinsèque d'un objet (en watts) et $l$ une taille physique (en mètres).

:::


Temps cosmique et temps conforme
--------------------------------

Le temps mérite une mention spéciale. Dans notre Univers idéal, sans surdensités ou sous-densités de matière, toutes les horloges qui suivent l'expansion (c'est-à-dire sans mouvement propre) battent la seconde à la même cadence. Avec un temps infini à notre disposition pour mettre à l'heure toutes les horloges de l'Univers, nous pouvons proposer une convention universelle pour synchroniser nos horloges. Par exemple, lorsque la température du CMB atteint une valeur donnée, toutes les civilisations de l'Univers peuvent décider que cela correspond à une certaine date. Il est donc possible de définir un temps cosmique, commun à tous les observateurs comobiles {cite:p}`Weinberg1972` [p. 409]. 




% :::{exercise} Temps conforme
% :label: exo:conformal-time

% Transformer la partie spatiale de la métrique FLRW dy système de coordonnées comobiles $(\sigma,\theta,\phi)$ [](#eq:FLRW-metric-spherical) au système de coordonnées comobiles équivalent $(\chi,\theta,\phi )$ avec $\chi$ la distance comobile. Étendre cette transformation aux coordonnées temporelles et proposer une définition du temps conforme $\eta$ et l'écrire sous la forme :
% \begin{equation}
% \dd s^2 = a^2(t) \left[ -c^2 \dd\eta^2 + \dd\chi^2 + f_k^2(\chi)\dd\theta^2 + f_k^2(\chi)\sin^2\theta \dd\phi^2 \right]
% \end{equation}
% avec $f_k(\chi)$ une fonction de $k$ et $\chi$ à définir. 

% :::

% :::{solution} exo:conformal-time
% :label: exo:conformal-time-sol
% :class: dropdown

% On commence par la définition de la métrique FLRW :
% \begin{align}
% \dd s^2 & = -c^2\dd t^2 + a^2(t) \left[ \frac{\dd\sigma^2}{1-k\sigma^2} + \sigma^2\dd\theta^2 + \sigma^2 \sin^2\theta \dd\phi^2 \right]  \\
% & = -c^2\dd t^2 + a^2(t) \left[ \dd\chi^2 + \sigma^2\dd\theta^2 + \sigma^2 \sin^2\theta \dd\phi^2 \right] \\
% & = -c^2\dd t^2 + a^2(t) \left[ \dd\chi^2 + f_k^2(\chi)\dd\theta^2 +f_k^2(\chi) \sin^2\theta \dd\phi^2 \right]
% \end{align}
% avec $\dd\chi = \dd\sigma/\sqrt{1-k\sigma^2}$ et :
% \begin{equation}
% \sigma = f_k(\chi) = \left\lbrace\begin{array}{cl}
%     \sin\chi & \text{ si } k=+1  \\
%     \chi  & \text{ si } k=0 \\
%     \sinh\chi & \text{ si } k=-1 
% \end{array}
% \right.
% \end{equation}
% On définit $\dd\eta =  \dd t / a(t)$ le temps conforme, et on aboutit à :
% \begin{equation}
% \dd s^2 = a^2(t) \left[ -c^2 \dd\eta^2 + \dd\chi^2 + f_k^2(\chi)\dd\theta^2 + f_k^2(\chi)\sin^2\theta \dd\phi^2 \right]
% \end{equation}
% Le temps conforme $\eta$ possède la dimension d'une durée. 

% :::

% D'ailleurs, en utilisant le temps conforme $\eta$ défini par $\dd \eta = \dd t / a(t)$, pour un photon on obtient :
% $$
% \chi = c \int_{\eta_E}^{\eta_0} \dd \eta = c (\eta_0 - \eta_E)$$
% donc on reconnait la relation traditionnelle entre distance et temps, mais dans l'espace comobile sans dimension.


[^gammat]: Rien ne l'interdit, puisque $\gamma_{ij}$ peut dépendre du temps

[^g00]: On peut introduire une nouvelle variable temps $t'$ telle que $\dd t' = \sqrt{\vert g_{00}\vert }\dd t$.

[^pc]: 1 parsec (pc) $= 3.262$ années-lumière $= 3.086\times 10^{16}\,$m. $100\,\text{Mpc}\approx 3\times 10^8\;$ années-lumière.
