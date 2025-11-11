---
short_title: Supernovae type Ia
authors:
  - jneveu
keywords: supernovae, Hubble diagram, $H_0$
---

Supernovæ de type Ia
===================

On distingue deux types de mesures cosmologiques: les mesures de distance qui cartographient l'histoire de l'expansion de l'Univers, et les mesures de croissance des structures qui décrivent l'évolution des grandes structures de l'Univers. Les premières sont des données simples qui in fine reviennent à mesurer l'évolution du paramètre de Hubble $H(z)$. Deux méthodes sont utilisées. La première méthode historiquement mise en œuvre utilise des chandelles standard, via des supernovæ de type Ia. Si on sait d'une catégorie d'objets astrophysiques qu'ils ont tous la même luminosité intrinsèque, alors si cet objet apparaît faible, c'est qu'il est situé loin et on peut en déduire sa distance à partir de sa luminosité apparente. La seconde méthode utilise une règle standard, à comprendre une longueur caractéristique invariante que l'on peut mesurer tout le long de l'histoire de l'Univers. Si cette longueur apparaît plus petite qu'aujourd'hui à un certain redshift $z$, alors sachant qu'elle n'a pas dû évoluer (ou sachant comment elle a évolué), on peut en connaître sa distance. Cette méthode est utilisée dans les oscillations baryoniques acoustiques et la mesure du spectre de puissance angulaire du fond diffus cosmologique. Le principe de ces deux méthodes est illustré [](#fig:chandelles).

:::{figure} ../../images/chandelles.jpg
:name: fig:chandelles
:align: center
:width: 80%

Principe de la mesure de l'expansion de l'Univers par l'utilisation de chandelles standard (les supernovæ de type Ia) et d'une règle standard (distance moyenne entre galaxies, issue de la distance moyenne entre sur-densités du fond diffus cosmologique).
:::


Principe de la méthode des chandelles standard
-----------------------------------

La méthode des chandelles standard s'appuie sur la mesure des flux lumineux venant d'astres de luminosités intrinsèques identiques. Pour mesurer la vitesse d'expansion de l'Univers, il faut disposer de distances de luminosité associées à des redshifts et ainsi construire un diagramme de Hubble-Lemaître. 

La <wiki:Apparent_magnitude> $m$ est une échelle logarithmique qui mesure la luminosité d'un objet observé depuis la Terre. Elle repose sur la mesure d'un flux lumineux $\Phi_{0}$ acquis avec un télescope équipé d'un capteur photosensible ($\gamma$/s/m$^2$) ou un bolomètre (W/m$^2$), comparé à un flux de référence $\Phi_{\rm ref}$ qui fixe l'échelle. Historiquement, ce flux de référence s'appuie sur une étoile étalon, Véga dans la constellation de la Lyre. Pour se raccorder aux 6 catégories de magnitudes définies dans l'Antiquité, la magnitude apparente d'un astre est définie par :
\begin{equation}
m = -2.5\log_{10} \left[\frac{\Phi_{0}}{\Phi_{\rm ref}} \right] 
\end{equation}
La magnitude absolue $M$ est le flux qu'on recevrait de cette source de luminosité $L$ observée à une distance de $10\,\parsec$ :
\begin{equation}
M = -2.5\log_{10} \left[\frac{L}{4\pi (10\,\parsec)^2\Phi_{\rm ref}} \right] 
\end{equation}

:::{note} Magnitudes

Le classement de la brillance des étoiles en magnitude vient de l'Antiquité, donc de l'observation visuelle. Entre les étoiles de magnitude 0 et 5, il se trouve qu'il y a un rapport cent en flux lumineux, les étoiles de magnitude faible étant les plus brillantes. Le flux est donc divisé par un facteur 2.5 entre chaque magnitude.
:::

Dans un monde idéal, il suffirait de mesurer les flux $\Phi_{0}^{(i)}$ d'une collection de $N$ chandelles standard à des redshifts $z_i$ et de les comparer entre eux pour obtenir une relation entre distance de luminosité et redshift. En effet, la magnitude apparent $m_i$ d'une chandelle standard de redshift $z_i$ est liée au taux d'expansion $H(z)$ via la distance de luminosité:
\begin{align*}\label{eq:utopie}
m_i & = -2.5\log_{10} \left[\frac{ \Phi_{0}^{(i)}}{\Phi_{\rm ref}}\right] \\
& = -2.5 \log_{10}\left[ \frac{L}{4\pi D_L^2(z_i) \Phi_{\rm ref}}\right]  \\
& = 5 \log_{10}\left[ \frac{D_L(z_i)}{10\,\parsec}\right] + M
\end{align*}
On appelle module de distance $\mu(z)$ la quantité :
\begin{equation}
\mu(z) = 5 \log_{10}\left[ \frac{D_L(z)}{10\,\parsec}\right] = 5 \log_{10} \left[\frac{(1+z)}{10\,\parsec} \int_0^z \frac{\dd z}{H(z)}   \right]  \text{ si } k=0
\end{equation}
C'est la baisse de luminosité en magnitude liée à la distance de l'astre. Si une chandelle standard est 2 fois plus loin alors elle apparait 4 fois moins brillante et son module de distance augmente de 1.5 magnitude. Par la mesure des flux, on peut ainsi estimer les distances relatives entre les chandelles standard.

Le point le plus important à remarquer dans cette formule est que la vitesse d'expansion cosmologique $H(z)$ est inscrit dans la forme de la courbe $\mu(z)$, et non dans sa normalisation. La normalisation de la courbe dépend notamment de $L$ et $H_0$. La méthode des chandelles standard permet donc de mesurer l'évolution de l'expansion de l'Univers, sans avoir besoin de connaître leur luminosité absolue $L$! En revanche, si on connaît leur luminosité absolue $L$, alors on peut établir une échelle de distances absolues et la normalisation du diagramme de Hubble donne accès à la valeur de $H_0$ ([](#fig:distmod)).

:::{figure} #distmod
:name: fig:distmod
:align: center
:width: 70%

Module de distance en fonction du redshift pour trois modèles cosmologiques. Un changement des paramètres $\Omega_i^0$ modifie la forme de la courbe alors que le paramètre $H_0$ modifie sa normalisation.
:::


Diagramme de Hubble des supernovae
-----------------------------------

Pour établir un diagramme de Hubble sur des distances cosmologiques, il faut disposer de sources de luminosités identiques et visibles sur de très grandes distances. Les galaxies sont de tailles donc de luminosité intrinsèque trop variables pour jouer ce rôle. Cependant, les supernovae de type Ia sont des explosions stellaires dont la luminosité est commensurable à celle d'une galaxie. Elles peuvent donc être visibles de loin mais seulement pendant un certain temps.

### Les supernovæ de type Ia

Les supernovæ sont classées en deux types: gravitationnelles ou thermonucléaires. Les premières sont les plus connues: elles correspondent à l'explosion d'une étoile massive (plus de 8 fois la masse du Soleil) en fin de vie, laissant un cœur stellaire dense et froid: une étoile à neutrons, voire un trou noir dans les cas extrêmes. Les supernovae de type I sont celles ne présentant pas de raies de l'hydrogène dans leur spectre, alors que les supernovae de type II en contiennent. Parmi les supernovae de type I, celles contenant du silicium sont de type Ia, puis les autres Ib ou Ic.

Les étoiles de masse inférieure à $8\,M_\odot$ terminent leur vie sous forme de géante rouge. A la fin de la combustion de l'hélium, les couches externes sont dispersées dans le milieu interstellaire sous forme de nébuleuse planétaire (sans forcément produire une explosion intense), laissant le coeur stellaire nu. L'effondrement du coeur est stoppé à cause de la pression de dégénérescence des électrons (et non des neutrons comme dans pour les étoiles à neutrons) et de sa faible masse (typiquement $0.5\,M_\odot$). Sa température de surface reste longtemps très élevée (environ $10\,000\,\kelvin$), d'où son nom de naine blanche. Il est essentiellement composé de carbone et d'oxygène, l'hélium et l'hydrogène ayant été expulsé dans l'espace. Le rayon typique d'un tel objet est de quelques milliers de kilomètres (comme une planète tellurique). 
 
:::{figure} ../../images/Type_Ia_Supernova_When_a_White_Dwarf_Steals_Material_from_Companion.mp4

Cette animation montre l'explosion d'une naine blanche, vestige extrêmement dense d'une étoile qui ne peut plus brûler de combustible nucléaire en son cœur. Dans cette supernova de type Ia, la gravité de la naine blanche dérobe de la matière à un compagnon stellaire proche. Lorsque la naine blanche atteint une masse estimée à 1.4 fois la masse actuelle du Soleil, elle ne peut plus supporter son propre poids et explose. Credit: NASA/JPL-Caltech
:::


D'après une étude du Very Large Telescope, environ 75% des étoiles massives vivent dans des systèmes binaires {cite:p}`Sana2012`. Dans certains cas, une naine blanche peut donc être liée gravitationnellement à une autre étoile qui, si elle est suffisamment proche, peut voir ses couches externes aspirées par la gravité de la naine blanche. Lorsque la naine blanche a accumulé trop de matière venant de son voisin et approche la masse de Chandrasekhar ($1.4\,M_\odot$), elle devient instable. Les conditions de pression et de température au c\oeur de la naine blanche permettent le réallumage de la fusion du carbone. La naine blanche ne peut se dilater et se refroidir à cause de la pression de dégénérescence des électrons, indépendantes de la température (effet quantique). La réaction s'emballe en une flamme thermonucléaire qui vaporise l'astre en quelques secondes. L'explosion enrichit le milieu interstellaire en éléments de masse intermédiaire (oxygène, calcium, magnésium, silicium, soufre) et de la famille du fer (nickel, cobalt). Ce scénario d'explosion ne reste toutefois qu'une hypothèse dans la mesure où aucune preuve n'existe encore. D'autres scénarios existent comme la fusion de deux naines blanches {cite:p}`Nomoto2013`.

Les SNe Ia puisent leur énergie de la désintégration des éléments du groupe du fer qui ont été produits lors de l’explosion <doi:10.1086/150102>. Le principal élément radioactif formé est le $^{56}_{28}\text{Ni}$ :
\begin{equation}
2\ ^{12}_{\ 6}\mathrm{C} + 2\ ^{16}_{\ 8}\mathrm{O} \rightarrow ^{56}_{28}\mathrm{Ni}
\end{equation}
puisqu'il est une combinaison stoechiométrique simple d'atomes de carbone et d'oxygène, les atomes les plus abondants d'une naine blanche. L'isotope du nickel $^{56}_{28}\text{Ni}$ se désintègre ensuite en $^{56}_{27}\text{Co}$ avec une demi-vie de 6.1 jours, qui lui même se désintègre en fer stable $^{56}_{26}\text{Fe}$ avec une demie-vie de 77.3 jours : 
\begin{equation}
^{56}_{28}\mathrm{Ni} \rightarrow ^{56}_{27}\mathrm{Co} \rightarrow ^{56}_{26}\mathrm{Fe}
\end{equation}
La luminosité totale est estimée à $10^{10}\,L_\odot$ soit environ celle d'une galaxie (voir photographies [](#fig:sn) et [](#fig:sn2)). Ce sont donc des objets a priori visibles à des distances cosmologiques. Comme l'explosion se produit systématiquement à la même masse stellaire, à peu près la même quantité de matériaux est rejetée dans l'espace et émet la même quantité de lumière. De plus, la composition des naines blanches étant très standard, la composition de la matière émettrice est la même. Elles ont donc toutes à peu près la même luminosité totale intrinsèque. Cependant ce sont aussi des événements transitoires: la durée d'une supernova est de quelques dizaines de jours. Pour la capter, il faut donc regarder le ciel au bon endroit et au bon moment.


Les supernovæ de type Ia (SNe Ia) sont les premières sondes cosmologiques qui ont permis de mesurer l'expansion de l'Univers sur des distances cosmologiques, et découvrir son expansion accélérée {cite:p}`Riess1998; Perlmutter1999`. Le prix Nobel de physique a été décerné en 2011 à Saul Perlmutter, Brian Schmidt et Adam Riess pour cette découverte majeure. 

:::{figure} ../../images/SN1994D.jpg
:name: fig:sn
:align: center
:width: 60%

La supernova SN 1994D (le point blanc brillant en bas à gauche de l'image), dans la galaxie spirale NGC4526.
:::

:::{figure} ../../images/sn2023_ixf_ugri_gimp_leg.png
:name: fig:sn2
:align: center
:width: 60%

La supernova sn2023ixf découverte par le relevé ZTF et photographiée par le télescope StarDICE (Newton, diamètre $40\,$cm) dans 4 filtres $ugri$ le 25 mai 2023.
:::




### Séquences spectrales et courbes de lumière



Une supernova de type Ia reste visible environ 40 jours dans le ciel dans le visible. Pour reconnaître son type, il faut l'observer sous plusieurs couleurs et si possible acquérir son spectre. Une séquence de spectres acquises sur une supernovæ de type Ia est présentée [](#fig:spectresIa).


:::{iframe} https://www.youtube.com/embed/350HR7Z8OYw?si=luHEY7x1g1TQDKvd
:width: 100%

Série d'images de l'explosion d'une supernova de type Ia. La supernova, SN 2015F, s'est produite dans la galaxie NGC 2442 au début du mois de mars 2015, à une distance d'environ 80 millions d'années-lumière de la Terre. Des images quotidiennes de février 2015 à octobre 2015 ont été combinées pour créer ce film. Les images ont été prises avec un télescope robotique de 17 pouces en Australie. 
:::

:::{figure} ../../images/timeseries.png
:name: fig:spectresIa
:align: center
:width: 70%

Série spectro-temporelle de SN2011fe mesurée par le relevé SNfactory {cite:p}`Pereira2013`. Les noms des principales composantes du spectre sont indiqués dans la partie supérieure de la figure.
:::


:::{figure} ../../images/lc.png
:name: fig:courbeslumiere
:align: center
:width: 70%

Courbes de lumière synthétisées SN2011fe en utilisant le jeu de filtres UBVRI$_\mathrm{SNf}$ {cite:p}`Pereira2013`. Les symboles remplis et ouverts correspondent respectivement aux nuits photométriques et non photométriques. Les résultats d'un ajustement simultané SALT2 de UBVR$_\mathrm{SNf}$ dans la plage de dans l'intervalle de phase $-\,16 < t < +\,25$ jours sont représentés par des lignes pleines, avec les résidus correspondants (SALT2 - SNf) sur le panneau inférieur. Les zones ombrées représentent l'erreur du modèle SALT2. La rupture dans l'axe du temps correspond à l'écart de $\sim 50$ jours dans le suivi pendant lequel SN2011fe n'était pas visible pendant la nuit depuis Hawaii. Notez le changement d'échelle de l'axe temporel étendu couvrant les observations tardives.
:::

En pratique, nous ne possédons pas de séquences spectrales aussi précises que celle présentée [](#fig:spectresIa) pour chaque supernova détectée, car cela coûte trop de temps d'observation sur les plus grands télescopes au monde équipés de spectrographe. Seul le relevé SNFactory a dédié un spectrographe à l'étude spectrale systématique des supernovae. En règle générale, si possible, un seul spectre de la supernova est acquis autour de son maximum de luminosité (car c'est plus aisé) afin de vérifier que c'est bien une type Ia (spectre d'identification), avec un spectrographe qui n'a pas besoin d'avoir une grande résolution pour identifier les raies principales de l'explosion thermonucléaire. Plus tard, un spectre de la galaxie hôte est pris pour mesurer son redshift précisément s'il n'est pas déjà connu, avec un spectrographe à plus haute résolution (spectre de redshift).

La principale information disponible sur une supernova de type Ia est donc sa courbe de lumière, c'est-à-dire la séquence temporelle des flux lumineux, mesurée par un télescope avec différents filtres passe-bande équipant la caméra du télescope [](#fig:courbeslumiere). 


Il faut donc définir un instant où comparer la brillance des chandelles standard et un filtre de référence. Pour des raisons pratiques, on utilise comme référence les magnitudes au maximum de l'émission. Pour des raisons historiques, on utilise la bande Johnson B comme filtre de référence. La magnitude du maximum de luminosité d'une supernova de type Ia observée en bande B est donc utilisée comme chandelle standard, ou du moins standardisable.


:::{note} Systèmes photométriques
:class: dropdown

```{figure} ../../images/photometric_systems.png
:name: fig:photsyst
:align: center
:width: 70%

Filtres passe-bande pour différents systèmes photométriques {cite:p}`Bessell2005`.

```

Les relevés astrophysiques et cosmologiques en photométrie sont intéressés par mesurer la couleur des objets pour accéder à leurs propriétés physiques. Pour cela, les télescopes sont équipés de filtres passe-bande, dont les formes et positions dépendent des technologies utilisées et des besoins du relevé.

Un système photométrique standard est défini par une liste de magnitudes et de couleurs standard mesurées à des bandes passantes spécifiques pour un ensemble d'étoiles bien réparties dans le ciel. Les magnitudes observées sont corrigées pour tenir compte de l'atténuation de l'atmosphère terrestre loin du zénith, et les données sont ensuite normalement extrapolées à une masse d'air nulle (en dehors de l'atmosphère). 

Le système UBV est l'un des systèmes photométriques photoélectriques standard les plus anciens et les plus utilisés <doi:10.1086/145697>. La bande B a été conçue pour se rapprocher de la magnitude photographique brute (moins les UV), tandis que la bande V a été conçue pour se rapprocher du système de magnitude visuelle. Les systèmes photométriques des relevés modernes SDSS et LSST utilisent plutôt des filtres interférentiels nommés ugrizy dans le visible et proche infrarouge.

:::


### Magnitude dans le référentiel au repos

Les flux lumineux $\Phi$ exprimés en ($\gamma$/s/m$^2$) ou (W/m$^2$) sont dits bolométriques[^bolo] car intégrés sur tout le spectre. Malheureusement la capacité à mesurer cette quantité dépend du capteur utilisé. Dans le visible et l'infrarouge, les capteurs sont basés sur l'effet photoélectrique donc ils sont transparents au-dessus d'une certaine longueur d'onde. Dans le visible et l'infrarouge, les flux mesurés ne peuvent être bolométriques. 

De plus, beaucoup d'information peut être tirée de la mesure de la couleur d'un objet, comme le type de la supernova : pour cela il faut l'observer à travers différents filtres passe-bande et comparer les flux. 

On introduit la densité spectrale d'énergie d'un astre $S_\lambda(\lambda)$ exprimée[^Sfreq] en W/m$^2$/nm. Notons $T_f(\lambda)$ la transmission de l'instrument équipé d'un filtre $f$. Le flux mesuré est alors :
\begin{equation}
\Phi_{0,f} = \int \frac{\dd \lambda}{hc/\lambda} S_\lambda(\lambda) T_f(\lambda) \text{\ \ \   en $\gamma$/m$^2$/s}
\end{equation}
où $\lambda$ est la longueur d'onde des photons incidents. Alors la définition de la magnitude apparente pour un filtre $f$ devient :
\begin{equation}
m_f = -2.5 \log_{10} \left[ \frac{ \int \lambda \dd \lambda S_\lambda(\lambda) T_f(\lambda) }{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_f(\lambda)}\right]
\end{equation}
avec $S_{\mathrm{ref}}(\lambda)$ la densité spectrale de flux de la source de référence (Véga par exemple). La magnitude absolue en filtre $f$ est la magnitude de l'astre en filtre $f$ si on l'observait dans son référentiel au repos à $10\,\parsec$ :
\begin{equation}
M_f = -2.5\log_{10} \left[\frac{1}{4\pi (10\,\parsec)^2} \frac{ \int \lambda \dd \lambda L_\lambda(\lambda) T_f(\lambda)}{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda)T_f(\lambda) } \right] 
\end{equation}
avec $L_\lambda$ la luminosité spectrale (en W/nm). 

On note $B(\lambda)$ la transmission du filtre B dans le système photométrique de Johnson UBV (voir encadré). Alors on pose:
\begin{equation}
m_B^* = -2.5 \log_{10} \left[ \frac{ \int \lambda \dd \lambda S^{\rm max}_\lambda(\lambda) B(\lambda) }{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) B(\lambda)}\right]
\end{equation}
La magnitude absolue dans la bande $B$ est :
\begin{equation}
M_B = -2.5\log_{10} \left[\frac{1}{4\pi (10\,\parsec)^2} \frac{ \int \lambda \dd \lambda L_\lambda(\lambda) B(\lambda)}{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) B(\lambda)}   \right] 
\end{equation}
 
Cependant, les télescopes ne sont pas tous équipés d'un filtre B. De plus, et c'est la raison principale, le maximum d'émission se déplace en longueur d'onde avec le décalage vers le rouge donc il faudrait pouvoir décaler vers le rouge le filtre B pour capter la même portion de spectre ([](#fig:snIaB)). Comme nous voulons comparer l'effet de la distance uniquement pour cartographier $D_L(z)$, ces effets de décalage en longueur d'onde doivent pourtant être supprimés pour standardiser et comparer le flux observé au maximum d'émission. Historiquement, pour les supernovæ de type Ia, les cosmologistes établissent les magnitudes apparentes en bande B _dans le référentiel au repos de la supernova_. La magnitude $m_B^*$ est donc la magnitude apparente dans le référentiel au repos en bande B, _comme s'il n'y avait pas d'expansion mais seulement un effet de distance_.

**La chandelle standard est le maximum d'émission des supernovæ de type Ia dans la bande $B$ comme si elle était observée dans son référentiel au repos.**


:::{figure} ../../images/snIa_restframeB.png
:name: fig:snIaB
:align: center
:width: 100%

Magnitudes apparentes en bande $B$ pour des supernovæ à différents redshifts: elles correspondent à l'intégrale de la densité spectrale de la supernova à son maximum dans la bande $B$ redshiftée.
:::

Comme ce n'est pas possible de réaliser une observation dans le référentiel au repos de la supernova, cette magnitude $m_B^*$ doit être calculée à partir des observations dans des filtres $f$ quelconques et d'un modèle _spectrophotométrique_ de la supernova.


### Modèle spectrophotométrique

Le modèle spectrophotométrique va être la donnée de la densité spectrale en fonction du temps $S_\lambda(\lambda, t)$, déterminée sur les données (la collection des courbes de lumière et des spectres disponibles). Supposons qu'on est capable de l'obtenir, après un entrainement sur les données, comme avec le modèle SALT2 {cite:p}`Guy2007`. Comment pouvons-nous transformer les magnitudes apparentes observées $m_f$ en magnitudes en bande B dans le référentiel au repos $m_B^*$?

Tout d'abord, il faut étudier l'effet du redshift sur les densités spectrales.
Le flux $\Phi_{0}$ et la luminosité intrinsèque $L$ (en W) d'un astre situé au redshift $z$ sont reliés par :
\begin{equation}\label{eq:boloPhiL}
\Phi_{0} = \frac{L}{4\pi D_L^2(z)}
\end{equation}
avec $D_L(z)$ la distance de luminosité. Tous les photons reçus dans une étroite gamme de fréquences logarithmiques centrée sur la longueur d'onde observée $\lambda_0$ ont été émis dans une gamme de longueur d'onde centrée également étroite centrée sur $\lambda_E = \lambda_0 / (1+z)$. L'équation [](#eq:boloPhiL) relie donc ainsi les densités spectrales de flux aux luminosités spectrales en présence d'un redshift $z$ {cite:p}`Condon2018`:
\begin{align}
\dd \lambda_0 S_\lambda(\lambda_0) & =  \frac{\dd \lambda_E L_\lambda(\lambda_E)}{4 \pi D_L^2 (z)} =  \frac{\dd \lambda_0}{1+z}\frac{ L_\lambda(\lambda_0/(1+z))}{4 \pi D_L^2 (z)} \notag \\ 
& \Rightarrow S_\lambda(\lambda_0) =\frac{L_\lambda(\lambda_0/(1+z))}{4 \pi (1+z) D_L^2 (z)} 
\end{align}
Cette relation donne le lien entre la densité spectrale de flux observée à $\lambda_0$ et la densité spectrale de luminosité émise à $\lambda_E$.

Maintenant, recherchons comment transformer les magnitudes observées $m_f$ en magnitudes $m_B^*$, à partir de la définition de la magnitude apparente en bande $f$ :
\begin{align*}
m_f & = -2.5 \log_{10} \left[ \frac{\int \lambda \dd \lambda S_\lambda(\lambda) T_f(\lambda) }{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_f(\lambda)}\right] \\
& = -2.5 \log_{10} \left[\frac{1}{4 \pi (1+z) D_L^2 (z)} \frac{\int \lambda \dd \lambda L_\lambda(\lambda/(1+z)) T_f(\lambda) }{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_f(\lambda)}\right]
\end{align*}
Posons $K_{fB}$ la _$K$-correction_ en bandes $f$ et $B$ {cite:p}`hogg2002k` :
\begin{align*}
K_{fB} &  = -2.5\log_{10} \left[\frac{1}{(1+z)} \frac{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) B(\lambda)}{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_f(\lambda)}  \frac{\int \lambda \dd \lambda L_\lambda(\lambda/(1+z)) T_f(\lambda) }{\int \lambda \dd \lambda L_\lambda(\lambda) B(\lambda)}\right]
\end{align*}
Alors la magnitude apparente peut se décomposer en trois termes :
\begin{align*}
m_f &  = M_B + \mu(z) + K_{fB}(z) 
\end{align*}
et la magnitude $m_B^*$ se calcule à partir des observations $m_f$ et de la $K$-correction calculée :
$$ \boxed{m_B^* = m_f - K_{fB}}$$
La $K$-correction représente bien la correction en magnitude qu'il faut apporter si on observait l'astre dans son référentiel au repos et avec un autre filtre. Après l'application de la $K$-correction, le diagramme de Hubble se modélise simplement par :
\begin{equation}
\boxed{m_B^*(z) = m_f - K_{fB}(z) = M_B + \mu(z)}
\end{equation}
une équation très similaire à [](#eq:utopie). Le membre de gauche représente les magnitudes acquises par le télescope et transformées en bande $B$ au repos et au maximum. Le membre de droite représente le modèle cosmologique explicatif. Pour les SNe Ia, $M_B = -19.08 \pm 0.03$ {cite:p}`Betoule2014`. On voit donc que la dépendance en distance est entièrement contenue dans le module de distance $\mu(z)$, mais remarquons qu'il existe une dépendance en redshift supplémentaire dans la $K$-correction. Il faut donc savoir correctement modéliser $K_{fB}(z)$ pour ne pas introduire de biais en redshift dans le diagramme de Hubble. 

Malheureusement, la $K$-correction dépend d'un certain nombre d'ingrédients qu'il faut donc connaître au préalable pour la calculer :
- le redshift $z$, à inférer depuis un spectre;
- la densité spectrale $S_\lambda$ de la supernova, à construire par un modèle spectrophotométrique ajusté sur les séquences spectrales mesurées (comme dans la [](#fig:spectresIa)) comme SALT2 {cite:p}`Guy2007`;
- la densité spectrale de référence $S_{\mathrm{ref}}(\lambda)$, à établir par mesure (<doi:10.1086/153547>, <doi:10.48550/arXiv.2411.03256>)  ou modélisation d'atmosphère stellaire <doi:10.1086/677655>;
- la transmission des filtres du télescope $T_f$, voire de la transmission atmosphérique du lieu $T_{\mathrm{atm}}(\lambda)$.

Pour obtenir une mesure du paramètre d'état de l'énergie noire $w_{DE}$ au pourcent, il faut donc que chacun de ces ingrédients soit établi à mieux que le pourcent. Aujourd'hui, les incertitudes dominantes sur la mesure de $w_{DE}$ par les supernovae de type Ia sont les incertitudes systématiques de calibration photométrique, donc la connaissance de la bande passante des filtres des instruments ainsi que la connaissance des flux de références {cite:p}`Betoule2013,Scolnic2018` .

#### Standardisation

Après $K$-correction, on peut comparer les magnitudes $m_B^*$ à un modèle cosmologique. Avec les données JLA du SuperNova Legacy Survey, on obtient le diagramme de Hubble [](#fig:hubblemb).

:::{figure} #hubbleDiagramMb
:name: fig:hubblemb
:align: center
:width: 70%

Diagramme de Hubble des 740 SNeIa du relevé SNLS, comparé à un modèle $\Lambda$CDM avec $\Omega_m^0 = 0.3$ et $\Omega_\Lambda^0=0.7$.
:::

Autour du diagramme, on observe que les résidus au diagramme de Hubble ont une dispersion de $0.4\,$mag, supérieures aux erreurs de mesure. Si on trace ces résidus en fonction de la couleur $c=B-V$ ou de la durée normalisée $x_1$ de la supernova, on s'aperçoit qu'ils sont corrélés ([](#fig:hubbleRes)). 

:::{list-table} Résidus au diagramme de Hubble colorés en fonction de la durée normalisée $x_1$ (gauche) ou de la couleur $c=B-V$ (droite).
:header-rows: 0
:name: fig:hubbleRes

* - :::{image} #hubbleResX1
    :alt: x1
    :width: 95%
    :align: center
    :::
  - :::{image} #hubbleResC
    :alt: color
    :width: 100%
    :align: center
    :::
:::

Il y a donc une variabilité des supernovae qui n'a pas été prise en compte dans notre modèle spectrophotométrique jusqu'à présent.

On observe que plus la courbe de lumière dure dans le temps, plus elle est brillante à son maximum (règle du *brighter-slower*). De plus, plus les SNIa sont bleues, plus elles sont brillantes également (règle du *brighter-bluer*). Il y a aussi un effet d'environnement qui lie la brillance de la supernova et la masse de la galaxie hôte.

:::{figure} ../../images/courbes_de_lumiere_x1c.png
:name: fig:courbes_de_lumiere_x1c
:align: center
:width: 60%

Courbes de lumière de SNe Ia du lot de données JLA du relevé SNLS colorées en fonction de $x_1$ ou $c$ {cite:p}`nicola2022`.
:::


Le flux de lumière est lié à la production et à la décroissance de nickel $^{56}$Ni. Les deux relations présentées ci-dessus peuvent ainsi être expliquées qualitativement: plus la SNIa produit de $^{56}$Ni, plus elle sera brillante et plus elle contiendra d'ions FeII et CoII émettant dans le bleu, mais aussi plus elle sera opaque (donc l'émission des photons par diffusion sera retardée, donc la SNIa brillera plus longtemps) {cite:p}`Kasen2007`.

Les SNe Ia ne sont donc pas si standard, car leurs courbes de lumière dépendent de la quantité de $^{56}$Ni disponible à l'origine. Néanmoins sans corriger cette dispersion intrinsèque les équipes du Supernova Cosmology Project (SCP) mené par Saul Perlmutter et du High-z Supernova Search Team mené par Brian Schmidt ont pu démontrer l'existence d'une expansion accélérée {cite:p}`Riess1998; Perlmutter1999`. Cette dispersion est gênante pour améliorer les mesures d'expansion de l'Univers au niveau du pourcent. Néanmoins, elle se décrit empiriquement par deux relations linéaires pour $x_1$ et $c$ avec des coefficients $\alpha$ et $\beta$ respectivement. Pour la masse de l'hôte, on ajuste un paramètre $\Delta M_{host}$ augmentant la magnitude pour les supernovae se situant dans des galaxies de masse supérieure à $10^{10}\,M_\odot$.

Ces trois relations empiriques ajoutent trois paramètres supplémentaires $\alpha$, $\beta$ et $\Delta M_{host}$ à ajuster également sur les données <doi:10.1086/307883>:
\begin{equation}
\boxed{m_{B,corr}^* = M_B + \mu -\alpha x_1 + \beta c +  \Delta M_{host}}
\end{equation}
Après cette standardisation, la dispersion au diagramme de Hubble est réduite à $0.15\,$mag ce qui augmente la précision sur les paramètres cosmologiques.


:::{figure} ../../images/HD_jla.png
:name: fig:HD
:align: center
:width: 70%

Diagramme de Hubble des supernovæ du catalogue JLA. La courbe noire représente un modèle $\Lambda$CDM ajusté aux données. Un modèle sans énergie noire apparaîtrait significativement en dessous de la courbe décrite par les données ($-0.6\,$mag à $z=1$).
:::

:::{note} Origine de $\Delta M_{host}$

En effet, il semble que les galaxies massives contiennent beaucoup plus de métaux et que les supernovæ peuvent y apparaissent plus brillantes que dans les galaxies légères (voir la discussion section 5.5 de la référence {cite:p}`Sullivan2010`). Comme suggéré par la référence {cite:p}`Sullivan2010`, on divise les données en deux lots selon la masse de la galaxie hôte. 
:::




### Étalonnages

:::{figure} ../../images/strategy1.png
:name: fig:SNCalib
:align: center
:width: 70%

Stratégies pour étalonner la mesure du flux lumineux des étoiles tertiaires (les étoiles secondaires ne sont pas représentées). La bande $B$ redshiftée est représentée par un trait bleu épais sur les spectres des SNe Ia. 
:::

### State of the art





Mesure locale de $H_0$
------------------------

Le module de distance $\mu(z)$ permet de mesurer la distance relative entre les SNe Ia, ce qui fournit des informations cruciales sur l'énergie noire. Cependant, la distance absolue des SNe Ia ne peut pas être obtenue par cette méthode : il y a une dégénérescence entre la luminosité de la SNe Ia $L$ et $H_0$ lors de l'estimation. Pour briser cette dégénérescence, l'échelle des distances cosmiques est utilisée. Cette méthode implique une série de mesures de distances qui se chevauchent en utilisant divers objets et techniques astronomiques, comme l'illustre la figure 12 de {cite:t}`Riess2022`. En ancrant les distances des SNe Ia à des distances mesurées indépendamment par l'échelle des distances cosmiques, nous pouvons démêler la magnitude absolue des SNe Ia de celle de H0. Dans ce qui suit, nous allons discuter des différentes étapes de cette échelle de distance.

:::{figure} ../../images/distance_ladder.png
:name: fig:distance_ladder
:align: center
:width: 100%

Echelle des distances astrophysiques {cite:p}`Riess2022`. Les mesures des paramètres d'orbite dans le Système Solaire permettent de calibrer la mesure des distances des étoiles par la méthode de la parallaxe. La distance de certaines étoiles Céphéides est mesurée par parallaxe ce qui permet d'établir une relation entre le flux des céphéides, leur période de luminosité et leur distance (carré inférieur). La distance obtenue par la luminosité de Céphéides dans des galaxies proches permet de calibrer la luminosité intrinsèque de SNe Ia explosant dans une galaxie contenant des Céphéides (carré intermédiaire). Une fois la luminosité intrinsèque des SNe Ia connue, la mesure de la pente de la relation distance-redshift pour des supernovae lointaines (mais pas trop) permet d'accéder à $H_0$.
:::

### Mesure de la parallaxe

Lorsqu'une étoile de premier plan est observée à partir de deux positions opposées, A et B, sur l'orbite de la Terre autour du Soleil, elle semble se déplacer par rapport au champ d'étoiles d'arrière-plan vers des positions A' et B'. Ce décalage apparent est appelé parallaxe. La distance entre la Terre et le Soleil est définie comme une unité astronomique (UA), c'est-à-dire la moyenne entre les deux demi-axes de l'orbite elliptique de la Terre. Avec cette distance, et en mesurant le déplacement apparent de la position de l'étoile, on peut calculer par trigonométrie la distance entre l'observateur et l'étoile. Ce phénomène est connu sous le nom de parallaxe. Les mesures de parallaxe effectuées par Gaia atteignent une précision de 0.04 mas <doi:10.1051/0004-6361/201832964>. Cette méthode constitue le premier barreau de l'échelle des distances cosmiques.

###  Céphéides


Les Céphéides sont un type d'étoile qui pulse radialement, subissant des variations régulières de diamètre et de température. Ces pulsations se traduisent par des changements de luminosité avec une période et une amplitude bien définies et stables. Elles ont été découvertes par Henrietta Swan Leavitt {cite:p}`Leavitt1907`, qui a mis en évidence la corrélation entre le diamètre et la température de l'étoile.

:::{figure} ../../images/leavitt_cepheids.png
:name: fig:leavitt_cepheids
:align: center
:width: 70%

Relation entre la magnitude des minima (courbe basse) et des maxima (courbe haute) des courbes de lumière des Céphéides en fonction du logarithme de leur période de pulsation, d'après {cite:t}`Leavitt1912`.
:::

La magnitude des maxima ou minima de la courbe de lumière d'une Céphéide est proportionnelle au logarithme de sa période de pulsation. Cette loi est connue sous le nom de loi de Leavitt, et la figure 2 de {cite:t}`Leavitt1912`, illustre cette relation ([](#fig:leavitt_cepheids)).

En observant des Céphéides suffisamment proches pour utiliser la méthode de parallaxe pour l'estimation de la distance, nous pouvons calibrer la magnitude absolue des Céphéides, et donc leur relation période-luminosité intrinsèque. En raison de la stabilité de leur fonction période-luminosité, cette calibration peut ensuite être appliquée à toutes les Céphéides, ce qui nous permet de mesurer leur distance de luminosité dans d'autres galaxies où la méthode de la parallaxe n'est pas réalisable. Par conséquent, les Céphéides servent de première chandelle standard dans l'échelle des distances cosmiques, permettant de déterminer la distance d'autres galaxies, comme le montre le graphique central de la [](#fig:distance_ladder).




:::{note} NGC4258 maser

La galaxie NGC4258 contient des masers à molécules d'eau, l'équivalent de lasers mais avec des ondes micro-ondes, observables en radioastronomie. Les masers sont des nuages de gaz moléculaires répartis dans un disque d'accrétion en rotation et excités par le trou noir central de cette galaxie. Le suivi de la raie d'émission à $22\,$GHz sur plusieurs mois a permis de mesurer l'accélération dans le disque d'accrétion en fonction de la distance angulaire au centre {cite:p}`Greenhill1995`. Connaissant l'accélération, la vitesse et en faisant l'hypothèse que l'orbite est keplerienne, on en déduit la distance physique entre les masers et le centre de rotation. Associées à leurs distances angulaires apparentes, on en déduit finalement la distance de NGC4258 : $(7.60 \pm 0.17 \pm 0.15)\,$Mpc (<doi:10.1038/22972>,  <doi:10.1088/0004-637X/775/1/13>). L'observation de 443 Céphéides dans NGC4258 permet ensuite de raffiner la calibration de leur relation période-luminosité {cite:p}`Riess2022` et augmenter la précision sur $H_0$.

:::


### Supernovae de type Ia

Une fois que la fonction période-luminosité des Céphéides est calibrée, cette calibration est transférée aux SNe Ia. Pour estimer la distance d'une galaxie à l'aide d'une Céphéide, celle-ci doit être résolue par rapport aux autres sources lumineuses de la galaxie et sa photométrie doit être réalisée ([](#fig:cepheids_shoes)). En mesurant sa période de pulsation, on en déduit sa luminosité intrinsèque donc la distance de la galaxie hôte. 


:::{figure} ../../images/cepheids_shoes.png
:name: fig:cepheids_shoes
:align: center
:width: 70%

Identification de Céphéides (points rouges) dans 18 galaxies où ont été observées des SNe Ia ainsi que dans le maser NGC4258, par le relevé SHOES du Hubble Space Telescope (d'après {cite:t}`Riess2022`).
:::

Ensuite, l'observation d'une SN Ia dans la même galaxie permet de connaître sa luminosité intrinsèque puisque la distance est connue via la Céphéide. {cite:t}`Riess2022` rapporte l'observation de 42 SNe Ia dans 37 hôtes calibrés. Ces SNe Ia sont représentées dans le carré central de [](#fig:distance_ladder), ce qui permet de calibrer la magnitude absolue des SNe Ia. Enfin, le carré supérieur trace un diagramme de Hubble des SNe Ia, qui est directement lié à l'estimation de la distance géométrique par la méthode de la parallaxe. 

Avec cet échantillon,  {cite:t}`Riess2022` rapporte une mesure de $H_0$ de $73.04 \pm 1.04\,$km/s/Mpc, en tension à plus de $5\sigma$ avec l'extrapolation des mesures de {cite:t}`Planck2018`. Il y a donc un désaccord entre les mesures réalisées sur le CMB (univers jeune, lointain) et les mesures réalisées avec les SNe Ia (univers récent, local). De multiples sources d'erreurs systématiques ont été investiguées mais pour le moment aucune d'elles ne semblent résoudre la tension. Des méthodes de mesure alternatives indépendantes sont aussi mises en oeuvre pour départager les tenants des SNe Ia des tenants du CMB, comme par exemple l'utilisation des fusions d'étoiles à neutrons observées en optique et par ondes gravitationnelles. Aussi, des modèles de nouvelle physique sont en compétition pour réconcilier l'univers jeune et l'univers récent($H_0$-Olympics : <doi:10.1016/j.physrep.2022.07.001>). 




:::{important} A retenir

- Les supernovae de type Ia sont des explosions stellaires thermonucléaires ayant des luminosités intrinsèques très similaires, aussi importantes qu'une galaxie entière. En revanche, elles ne durent qu'une quarantaine de jours.

- La magnitude apparente en bande $B$ calculée dans le référentiel au repos de la supernova est le flux standard permettant de comparer les supernovae de type Ia entre elles et d'établir une relation distance-redshift (diagramme de Hubble-Lemaître).

- Le calcul implique de bien connaître les bandes passantes de l'instrument d'observation afin de ne pas introduire de biais sur la mesure des distances.

- Les SNe Ia sont standardisables par trois relations empiriques impliquant leur couleur, leur durée et la masse de la galaxie hôte.

- La mesure de $H_0$ par les SNe Ia est calibrée sur des mesures de distance locales, en particulier sur la relation période-luminosité des Céphéides.

::: 


:::{seealso}  Pour approfondir

- Effet du redshift sur les mesures astrophysiques : {cite:t}`Condon2018`

- Sur l'histoire du premier diagramme de Hubble : https://arxiv.org/abs/2311.07552

- Sur la tension $H_0$ :  {cite:t}`Riess2022` et <doi:10.1016/j.physrep.2022.07.001>

:::




[^bolo]: Un capteur bolométrique est capable d'absorber des photons et de mesurer leur énergie peu importe leur longueur d'onde (par exemple en mesurant l'échauffement d'un matériau). A contrario, un capteur photonique basé sur l'effet photoélectrique devient transparent dans les grandes longueurs d'ondes, lorsque l'énergie du photon passe sous le seuil d'émission d'un électron.

[^Sfreq]: Ou en fréquence $S_\nu(\nu)$ exprimée en W/m$^2$/Hz.