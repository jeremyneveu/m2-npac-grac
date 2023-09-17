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



```{figure} ../images/sdss_pie2.jpg
:name: fig:sdss
:align: center
:width: 60%

Répartition des galaxies détectées par l'expérience Sloan Digital Sky
Survey (SDSS), en fonction du redshift $z$ (cette notion sera définie
plus loin, mais peut être liée à une notion de distance, $z=0$ étant
notre position).
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

En combinant les deux résultats précédents, la métrique peut être écrite sous la forme suivante :
\begin{equation}
\dd s^2= -g_{00}(t) c^2 \dd t^2 + \dd l^2
\end{equation}
où $\dd l$ est l'élément de ligne pour la surface spatiale 3D. Trouvons maintenant une forme explicite pour $\dd l^2$.

:::{attention} Convention de signature pour la métrique
Dans ce cours, comme dans beaucoup de cours de cosmologie, la [signature](https://en.wikipedia.org/wiki/Metric_signature) choisie pour la métrique est $(-,+,+,+)$. 
En effet, en cosmologie on manipule beaucoup des distances donc il est plus commode d'avoir des éléments de longueur positifs. En physique théorique
des hautes énergies, la métrique $(+,-,-,-)$ est souvent préférée. Une compilation des différentes signatures utilisées est présentée
[ici](https://en.wikipedia.org/wiki/Sign_convention)

:::


### Géométrie d'un Univers maximallement symétrique

Dans un espace 3D non euclidien homogène et isotrope, la courbure de toute géodésique, en tout point le long de la géodésique, doit être la même {cite:p}`Weinberg1972`. Notons $a$ le rayon de courbure associé.

Tout d'abord, si cet espace possède une courbure nulle, alors l'élément de métrique $\dd l$ s'écrit simplement avec des coordonnées cartésiennes :
\begin{equation}
\dd l^2 = \dd x^2 + \dd y^2 + \dd z^2
\end{equation}

Travaillons maintenant sur le cas où la courbure est non nulle. Pour décrire la courbure d'une surface avec des notions de géométries habituelles, étudions-la dans un espace avec une dimension supplémentaire.
Si nous plaçons cet espace 3D non euclidien dans un espace 4D euclidien avec des coordonnées euclidiennes $(x,y,z,w)$, 
l'hyper-surface 3D non euclidienne de courbure gaussienne positive constante $a^{-3}$ peut être décrite par l'équation suivante :
- pour une 3-sphère de rayon $a$ : 
\begin{equation}
x^2+y^2+z^2+w^2= a^2
\end{equation}
- pour un 3-hyperboloïde de courbure $a$ :
\begin{equation}
x^2+y^2+z^2-w^2= a^2
\end{equation}

Utilisons les coordonnées sphériques $(r,\theta,\phi)$ telle que $r^2=x^2+y^2+z^2$. Alors ces deux derniers cas sont définis par l'équation de contrainte :
```{math}
:label: eq_hyp_sph
r^2 \pm w^2= a^2
```

:::{tip} Notion de courbure
:class: dropdown

Si ces raisonnements vous troublent, rappelez-vous que c'est comme décrire la courbure $R$ d'un cercle 
(objet à une dimension car il n'y a qu'une seule direction de déplacement sur cet objet)
dans un espace à deux dimensions par :

$$x^2 + y^2 = R^2$$ 
ou celle d'une sphère (deux dimensions) dans un espace à trois dimensions.
:::

La distance infinitésimale entre deux points dans l'espace 4D euclidien peut être écrite :
\begin{equation}
\dd l^2=\dd x^2+\dd y^2+\dd z^2 \pm \dd w^2=\dd r^2+r^2(\dd \theta^2+\sin^2\theta \,\, \dd \phi^2) \pm dw^2
\end{equation}

Si ces deux points sont contraints d'être sur notre espace 3D non euclidien, la différentiation de l'équation
eq. [](#eq_hyp_sph) donne la relation $r\dd r \pm w\dd w=0$, donc, en injectant de nouveau l'équation [](#eq_hyp_sph), on obtient :
\begin{equation}
r^2 \dd r^2=w^2\dd w^2 \Leftrightarrow \dd w^2= \frac{r^2 \dd r^2}{w^2} \dd w^2= \frac{r^2 \dd r^2}{a^2 \mp r^2}
\end{equation}
La distance infinitésimale entre 2 points de l'espace 3D non euclidien de courbure positive constante $a^{-3}$ est alors :
\begin{equation}
\dd l^2= \dd r^2 \pm \frac{r^2}{a^2\mp r^2} \dd r^2+r^2(\dd \theta^2+\sin^2\theta \,\, \dd \phi^2)
\end{equation}


Enfin, notons que le rayon de courbure peut en fait être une fonction du temps. On introduit la variable rééchelonnée $\sigma=r/a(t)$, et nous obtenons une nouvelle expression :
\begin{equation}
\dd l^2= a^2(t) \left( \frac{1}{1\mp \sigma^2}\dd \sigma^2+\sigma^2(\dd \theta^2+\sin^2\theta \,\, \dd \phi^2)\right)
\end{equation}

Il est alors possible de fixer $g_{00}$ à 1 en redéfinissant la variable temps. La métrique de Friedmann-Lemaître-Robertson-Walker décrivant un Univers homogène 
et isotrope s'écrit finalement :
```{math}
:label: FLRW-metric

\dd s^2=-c^2\dd t^2 + a^2(t) \left( {1 \over 1-K\sigma^2}\dd \sigma^2+\sigma^2(\dd \theta^2+\sin^2\theta \,\, \dd \phi^2)\right)
```
avec
```{math}
:label: K-def

K = \left\lbrace
\begin{array}{rl}
 +1 & \text{3-sphère} \\
 0 & \text{espace\ plat} \\
 -1 & \text{3-hyperboloïde} \\
\end{array}\right.
```

La métrique de Friedmann-Lemaître-Robertson-Walker (FLRW) constitue le cadre de base du modèle cosmologique standard. Les hypothèses d'homogénéité
et d'isotropie ont directement conduit à une métrique décrivant un univers avec seulement trois géométries possibles (plat, 3-sphère, 3-hyperboloid) avec 
un facteur d'échelle $a(t)$ affectant les distances.

Le cas de l'univers plat simplifie beaucoup les calculs qui suivront. Étant donné qu'une courbure nulle est toujours compatible avec les contraintes de plus en plus fortes des observations cosmologiques
nous concentrerons désormais nos développements analytiques sur l'univers plat, en mentionnant des résultats pour le cas général lorsque cela est nécessaire. La métrique
FLRW s'écrit dans un univers plat :
\begin{equation}
g_{\mu\nu}=\begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & a^2(t) & 0 & 0 \\ 0&0& a^2(t)&0 \\ 0&0&0&a^2(t) \end{pmatrix}
\end{equation}


:::{important} Où sont les unités ?
L'élément de distance $\dd s$ possède la dimension d'une longueur, par conséquent tous les terms de l'équation [](#FLRW-metric) aussi. 

Certains ouvrages proposent que le facteur d'échelle soit une fonction du temps sans dimension, et que $\sigma$ garde la dimension d'une longueur, 
normalisée par $a(t)$. Ceci permet de tout définir en particulier en posant qu'aujourd'hui le facteur d'échelle vaut $a_0=1$, mais alors il faut redéfinir
$K$ (avec $w$) et lui donner l'unité d'une courbure.

Dans ce cours, nous allons abondamment traiter des distances en cosmologie, et dans ce cas il est plus commode de penser que le facteur d'échelle est 
homogène à une longueur, et que les coordonnées spatiales $(\sigma, \theta, \phi)$ forment un vecteur sans dimension. 
Le paramètre de courbure $K$ est alors sans dimension également.

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

\fbox{$\displaystyle H = \frac{\dot a}{a} $}
```
avec le point $\dot{}$ exprimant une dérivée par rapport au temps $t$.
Dans le but d'alléger les notations, la dépendance temporelle des
paramètres ne sera pas toujours explicitée, de sorte que $a(t)=a$. On
désignera les paramètres évalués au temps présent $t_0$ par l'indice ou
l'exposant 0 si bien que $a(t_0)=a_0$. 
Dans la suite, nous travaillerons dans le système où $a_0$ n'est pas fixé à 1. 

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

:::{note} Que signifie vivre dans un espace courbé ?
La [](#fig:espaces) représente des surfaces 2D plongées dans des espaces 3D. Mais comment se représenter que nous vivrions dans une 3-sphère ? Et qu'est-ce 
que cela implique ? Vivre dans un espace courbé implique que la somme des angles d'un triangle n'est pas égale à 180°: elle est supérieure pour une 3-sphère et inférieure pour
un 3-hyperboloid. C'est ainsi que les deux triangles bleus [](#fig:triangles_on_sphere)
ont une somme de leurs angles supérieures à 180°. Dans une 3-sphère nous pouvons avoir l'impression que deux objets sont éloignés angulairement, alors qu'en en fait leur distance qui les sépare
est plus petite que ce qu'elle serait dans un espace plat. Et ceci dans toutes les directions de l'espace. 


En résumé, vivre dans un espace courbé signifie que la relation entre angles et longueurs est déformée par rapport à notre intuition euclidienne, en 
tous cas sur des distance cosmologiques.


:::


:::{figure} ../images/triangles_on_sphere.svg
:name: fig:triangles_on_sphere 
:align: center

Prenons deux galaxies: elles forment un triangle avec la Terre, qui, dans une 3-sphère, possède trois angles dont la somme est supérieure à 180°. Il repose
sur une 2-sphère, hyperplan de la 3-sphère (surface $w=cste$), dont les méridiens définissent les géodésiques par lesquelles la lumière nous parvient. 
Pour toute paire de points, on peut ainsi définir un tel triangle reposant sur une 2-sphère (bleu et cyan par exemple).
:::


Coordonnées comobiles
---------------------




Le décalage spectral, ou redshift
----------------------------------

Pour mesurer la valeur des différents paramètres de densité dans notre
Univers, il faut avoir accès au paramètre d'échelle $a(t)$. Ceci est
possible par la mesure du décalage spectral de la lumière venant de
sources distantes. Dans la métrique FLRW, plaçons-nous par convention au
centre $r=0$ (ou $\sigma=0$), et considérons un objet situé aux coordonnées comobiles
$\left(\sigma_E,\theta_E,\phi_E\right)$, émettant une onde électromagnétique
à l'instant $t_E$ (voir [](#fig:distances_croquis)). Le front d'onde est paramétré par
la coordonnée comobile $\sigma(t)$. Pour cette onde, voyageant à la vitesse
de la lumière, dans la métrique FLRW on a, à tout instant:
```{math}
:label: eq:ds2_lumiere

\dd\tau^2=0=-c^2 \dd t^2+\frac{a^2(t)}{1-K\sigma^2}\dd r^2.
```
Posons $t_0$ l'instant de la réception de cette onde en $\sigma=0$, alors grâce à l'équation
précédente on a la relation: 
```{math}
:label: eq:comobile

\chi(t_0)\equiv \int_{t_E}^{t_0} \frac{cdt}{a(t)} = \int_0^{r_E}\frac{\dd\sigma}{\sqrt{1-K\sigma^2}} = \left\lbrace
\begin{array}{cl}
    \arcsin \sigma_E & \text{ si } K=+1 \\
    \sigma_E & \text{ si } K=0 \\
    \text{arcsh } \sigma_E & \text{ si } K=-1 
\end{array}
\right. .
``` 
Cette dernière intégrale est appelée distance comobile car
elle fait abstraction des effets de l'expansion de l'Univers dans le
calcul de la longueur parcourue par la lumière. En effet, elle a la même
dimension que $\sigma$ donc est sans unité.

```{figure} ../images/distances2.svg
:name: fig:distances_croquis
:align: center
:width: 100%

Notations pour le calcul du redshift et des distances cosmologiques en coordonnées comobiles.
```


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

:::{note}
Peut-on caractériser le mouvement d'une simple particule en chute libre dans une métrique FLRW ? D'après la GR, nous savons qu'une telle particule se déplace le long d'une géodésique dont l'équation est la suivante :


\begin{equation}
{d^2 x^\mu \over du^2} +\Gamma^{\mu}_{\,\,\nu\kappa} {d x^\nu \over du}{d x^\kappa \over du}=0,
\label{geodesic}
\end{equation} 
où $u$ est un paramètre quelconque décrivant la position le long de la géodésique (le temps propre par exemple).
Rappelons que les connexions métriques peuvent être dérivées du tenseur métrique à l'aide de la relation :

\begin{equation}
\Gamma^{\mu}_{\,\,\nu\kappa}={1 \over 2}g^{\mu\lambda}\left[g_{\nu\lambda ,\kappa}+g_{\lambda\kappa ,\nu}-g_{\nu\kappa ,\lambda}\right],
\end{equation}
où les virgules désignent une dérivée partielle par rapport à la variable spatio-temporelle correspondant à l'indice suivant la virgule. La métrique FLRW étant homogène, seules les dérivées temporelles produiront des résultats non nuls dans la formule ci-dessus. De plus, $g$ étant diagonal, la dérivée par rapport à la variable d'espace-temps
puisque $g$ est diagonal, les deux autres indices des coefficients de connexion non nuls doivent être égaux. Il suffit donc de
 Il est trivial de vérifier que $\Gamma^{0}_{\N- \N- 00}=0$. En utilisant la convention habituelle selon laquelle les indices latins ne s'étendent que sur les coordonnées spatiales, nous obtenons :

\begin{equation*}
 \Gamma^{0}_{\,\,ii}=  {\dot{a}a \over c }
\end{equation*}
\begin{equation*}
\Gamma^{i}_{\,\,0i}= {\dot{a}\over c a}
\end{equation*}
En injectant ces coefficients de connexion dans la composante spatiale de l'équation géodésique, nous obtenons :

\begin{equation}
{d^2 x^i \over du^2} + \Gamma^i_{0i}{c dt \over du}{d x^i \over du} + \Gamma^i_{i0}{d x^i \over du}{c dt \over du}=0
\end{equation}
Nous choisissons maintenant $u$ comme temps propre.
\begin{equation}
{d^2 x^i \over d\tau^2} = - 2 {\dot{a} \over a} {dt \over d\tau}{ dx^i \over d\tau}
\end{equation}
Il est facile de l'intégrer pour montrer que ${d x^i \over d \tau} = {cst \over a^2}$. Les ${d x^i \over d \tau}$ sont les composantes spatiales de la vitesse 4 en mouvement. Alors les _composantes de l'espace du mouvement_ 4-momentum sont $ m {d x^i \over d \tau}$.
Il s'ensuit que les composantes spatiales du _moment physique_ évoluent comme suit :

\begin{equation}
p\propto a^{-1}
\end{equation}

Une fois encore, à un niveau superficiel, la conservation de la quantité de mouvement semble être rompue si $a$ n'est pas constant. Cependant, la mécanique classique n'est pas en mesure de décrire la gravitation provenant d'un espace uniforme, infini et non vide (l'équation de Poisson ne s'applique pas).
:::