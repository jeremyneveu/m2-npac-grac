---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
  '\parsec': '\mathrm{parsec}'
---

Supernovæ de type Ia
===================

### Préambule

On distingue deux types de mesures cosmologiques: les mesures de
distance qui cartographient l'histoire de l'expansion de l'Univers, et
les mesures de croissance des structures qui décrivent l'évolution des
grandes structures de l'Univers. Les premières sont des données simples
qui in fine reviennent à mesurer l'évolution du paramètre de Hubble
$H(z)$. Deux méthodes sont utilisées. La première méthode historiquement
mise en œuvre utilise des chandelles standard, via des supernovæ de type
Ia. Si on sait d'une catégorie d'objets astrophysiques qu'ils ont tous
la même luminosité intrinsèque, alors si cet objet apparaît faible,
c'est qu'il est situé loin et on peut en déduire sa distance à partir de
sa luminosité apparente. La seconde méthode utilise une règle standard,
à comprendre une longueur caractéristique invariante que l'on peut
mesurer tout le long de l'histoire de l'Univers. Si cette longueur
apparaît plus petite qu'aujourd'hui à un certain redshift $z$, alors
sachant qu'elle n'a pas dû évoluer (ou sachant comment elle a évolué),
on peut en connaître sa distance.
Cette méthode est utilisée dans les oscillations baryoniques acoustiques
et la mesure du spectre de puissance angulaire du fond diffus
cosmologique. Le principe de ces deux méthodes est illustré
[](#fig:chandelles).


```{figure} ../images/chandelles.jpg
:name: fig:chandelles
:align: center
:width: 80%

Principe de la mesure de l'expansion de l'Univers par l'utilisation de
chandelles standard (les supernovæ de type Ia) et d'une règle standard
(distance moyenne entre galaxies, issue de la distance moyenne entre
sur-densités du fond diffus
cosmologique).
```


Diagramme de Hubble des supernovae
-----------------------------------


### Principe

Les supernovæ de type Ia (SNe Ia) sont les premières sondes cosmologiques qui ont permis de mesurer l'expansion de l'Univers sur de lointaines distances, et découvrir son expansion accélérée {cite:p}`Riess1998; Perlmutter1999`. Le prix Nobel de physique a été décerné en 2011 à Saul Perlmutter, Brian Schmidt et Adam Riess pour cette découverte majeure. 

Le principe de la mesure a été résumé en introduction de ce chapitre: s'il existe un objet astrophysique de luminosité intrinsèque reproductible,  suffisamment brillant pour être visible sur des distances cosmologiques, alors la mesure du flux lumineux reçu renseigne directement sur sa
distance. L'objet astrophysique en question est bien entendu la supernova de type Ia, dont la luminosité égale ou dépasse celle de la galaxie hôte (voir photographies [](#fig:sn) et [](#fig:sn2)). Ce sont donc des objets a priori visibles à des distances cosmologiques, cependant ce sont aussi des événements transitoires: la durée d'une supernova est de quelques dizaines de jours. Pour la capter, il faut donc regarder le ciel au bon endroit au bon moment.


```{figure} ../images/SN1994D.jpg
:name: fig:sn
:align: center
:width: 40%

La supernova SN 1994D (le point blanc brillant en bas à gauche de
l'image), dans la galaxie spirale NGC
4526.
```

```{figure} ../images/sn2023_ixf_ugri_gimp_leg.png
:name: fig:sn2
:align: center
:width: 40%

La supernova sn2023ixf découverte par le relevé ZTF et photographiée par le télescope StarDICE (Newton, diamètre $40\,$cm) dans 4 filtres $ugri$ le 25 mai 2023.
```

### Les supernovæ

Les supernovæ sont classées en deux types: gravitationnelles ou thermonucléaires. Les premières sont les plus connues: elles correspondent à l'explosion d'une étoile massive (plus de 8 fois la masse du Soleil) en fin de vie, laissant un cœur stellaire dense et froid: une étoile à neutrons, voire un trou noir dans les cas extrêmes. Les supernovae de type I sont celles ne présentant pas de raies de l'hydrogène dans leur spectre, alors que les supernovae de type II en contiennent. Parmi les supernovae de type I, celles contenant du silicium sont de type Ia, puis les autres Ib ou Ic.

Les étoiles de masse inférieure à $8\,M_\odot$ terminent leur vie sous forme de géante rouge. A la fin de la combustion de l'hélium, les couches externes sont dispersées dans le milieu interstellaire sous forme de nébuleuse planétaire (sans forcément produire une explosion intense), laissant le coeur stellaire nu. L'effondrement du coeur est stoppé à cause de la pression de dégénérescence des électrons (et non des neutrons comme dans pour les étoiles à neutrons) et de sa faible masse (typiquement $0.5\,M_\odot$. Sa température de surface reste longtemps très élevée (environ $10\,000\,$K), d'où son nom de naine blanche. Il est essentiellement composé de carbone et d'oxygène, l'hélium et l'hydrogène ayant été expulsé dans l'espace. Le rayon typique d'un tel objet est de quelques milliers de kilomètres (comme une planète telluriques). 
 
:::{figure} ../images/Type_Ia_Supernova_When_a_White_Dwarf_Steals_Material_from_Companion.mp4

Cette animation montre l'explosion d'une naine blanche, vestige extrêmement dense d'une étoile qui ne peut plus brûler de combustible nucléaire en son cœur. Dans cette supernova de type Ia, la gravité de la naine blanche dérobe de la matière à un compagnon stellaire proche. Lorsque la naine blanche atteint une masse estimée à 1.4 fois la masse actuelle du Soleil, elle ne peut plus supporter son propre poids et explose. Credit: NASA/JPL-Caltech
:::


D'après une étude du Very Large Telescope, environ 75% des étoiles massives sont des systèmes binaires {cite:p}`Sana2012`. Dans certains cas, une naine blanche peut donc être liée gravitationnellement à une autre étoile qui, si elle est suffisamment proche, peut voir ses couches externes aspirées par la gravité de la naine blanche. Lorsque la naine blanche a accumulé trop de matière venant de son voisin et approche la masse de Chandrasekhar[^1] ($1.4\,M_\odot$), elle devient instable. Les conditions de pression et de température au c\oeur de la naine blanche permettent le réallumage de la fusion du Carbone. La naine blanche ne pouvant se dilater à cause de la pression de dégénérescence et ainsi se refroidir, la réaction s'emballe en une flamme thermonucléaire qui vaporise l'astre en quelques secondes, et enrichit le milieu interstellaire en éléments de masse intermédiaire (Oxygène, Calcium, Magnésium, Silicium, Soufre) et de la famille du Fer (Nickel, Cobalt). 

Les SNe Ia puisent leur énergie de la désintégration des éléments du groupe
du Fer qui ont été produits lors de l’explosion [Colgate & McKee (1969)]. Le principal élément
radioactif formé est le $^{56}_{28}$Ni :
\begin{equation}
2\ ^{12}_{\ 6}\mathrm{C} + 2\ ^{16}_{\ 8}\mathrm{O} \rightarrow ^{56}_{28}\mathrm{Ni}
\end{equation}
L'isotope du nickel $^{56}_{28}$Ni se désintègre ensuite en $^{56}_{27}$Co avec une demi-vie de 6.1 jours, qui lui
même se désintègre en fer stable $^{56}_{26}$Fe avec une demie-vie de 77.3 jours : 
\begin{equation}
^{56}_{28}\mathrm{Ni} \rightarrow ^{56}_{27}\mathrm{Co} \rightarrow ^{56}_{26}\mathrm{Fe}
\end{equation}
La luminosité totale est estimé à $10^{10}\,L_\odot$ soit environ celle d'une galaxie.

Ce scénario d'explosion ne reste toutefois qu'une hypothèse dans la mesure où aucune preuve n'existe encore. D'autres scénarios existent comme la fusion de deux naines blanches {cite:p}`Nomoto2013`.

### Courbes de lumières et séquences spectrales

Une supernovae de type Ia dure reste visible environ 40 jours dans le ciel dans le visible. Pour reconnaître son type, il faut l'observer sous plusieurs couleurs et si possible acquérir son spectre. La séquence temporelle de sa brillance au cours du temps est appelée courbe de lumière, souvent acquise avec différents filtres passe-bande équipant la caméra du télescope  [](#fig:courbeslumiere).

:::{iframe} https://www.youtube.com/embed/350HR7Z8OYw?si=luHEY7x1g1TQDKvd
:width: 100%

This is a real footage of the type Ia supernova explosion. The supernova, SN 2015F, occurred in NGC 2442 galaxy in early March, 2015, at a distance about 80 million light years away from the earth. Daily cadence images from Feb. 2015 through Oct. 2015, were combined to create the movie. Images were taken with a robotic 17-inch telescope in Australia. Our analysis suggests that this explosion was possibly caused by the interaction between a white dwarf star and a main sequence star with a size of 0.1 - 1.0 times the sun.
:::


```{figure} ../images/lc.pdf
:name: fig:courbeslumiere
:align: center
:width: 70%

Courbes de lumière synthétisées SN~2011fe en utilisant le jeu de filtres UBVRI$_\mathrm{SNf}$ {cite:p}`Pereira2013`. Les symboles remplis et ouverts correspondent respectivement aux nuits photométriques et non photométriques respectivement. Les résultats d'un ajustement simultané SALT2 de UBVR$_\mathrm{SNf}$ dans la plage de dans l'intervalle de phase $-\,16 < t < +\,25$~d sont représentés par des lignes pleines, avec les résidus correspondants (SALT2 - \snifs) sur le panneau inférieur.panneau inférieur. Les zones ombrées représentent l'erreur du modèle SALT2. La rupture dans l'axe du temps correspond à l'écart de $\sim50$ jours dans le suivi pendant lequel SN~2011fe n'était pas visible pendant la nuit depuis Hawaii. Notez le changement d'échelle de l'axe temporel étendu couvrant les observations tardives.
```

Une séquence de spectres acquises sur une supernovæ de de type Ia est présentée [](#fig:spectresIa).

```{figure} ../images/timeseries.pdf
:name: fig:spectresIa
:align: center
:width: 70%

Série spectro-temporelle de SN2011fe mesurée par le relevé SNfactory {cite:p}`Pereira2013`. Les noms des principales composantes du spectre sont indiqués dans la partie supérieure de la figure.
```

En pratique, nous ne possédons pas de séquences spectrales aussi précises que celle présentée [](#fig:spectresIa) pour chaque des supernovae détectée, car cela coute trop de temps d'observation sur les plus grands télescopes au monde équipés de spectrographe. Seul le relevé SNFactory a dédié un spectrographe à l'étude spectrale systématique des supernovae. En règle générale, si possible, un spectre de la supernova est acquis à son maximum de luminosité (car c'est plus aisé) afin de vérifier que c'est bien une type Ia (spectre d'identification), avec un spectrographe qui n'a pas besoin d'avoir une grande résolution pour identifier les raies principales de l'explosion thermonucléaire. Plus tard, un spectre de la galaxie hôte est pris pour mesurer son redshift précisément s'il n'est pas déjà connu, avec un spectrographe à plus haute résolution (spectre de redshift). 

La seule information typiquement disponible sur une supernovae de type Ia est donc sa courbe de lumière, c'est-à-dire la séquence temporelle des flux lumineux mesurées par un télescope dans ses différents filtres.

Comme l'explosion se produit systématiquement à la même masse stellaire, à peu près la même quantité de matériaux est rejetée dans l'espace et émet la même quantité de lumière. De plus, la composition des étoiles à neutrons étant très standard, la composition de la matière émettrice est la même. Elles ont donc toutes à peu près la même luminosité totale intrinsèque, et les courbes de lumière sont très similaires. Ce sont des astres transitoires qui brillent environ 40 jours dans le visible : il faut donc définir un instant où comparer la brillance des chandelles standard. Pour des raisons pratiques, dans un diagramme de Hubble on utilise les magnitudes au maximum de l'émission. La magnitude du maximum de luminosité d'une supernovae de type Ia est donc idéale à utiliser comme chandelle standard, ou du moins standardisable.

### Interprétation des courbes de lumière

La <wiki:Apparent_magnitude> est une échelle logarithmique qui mesure la luminosité d'un objet observé depuis la Terre. Elle repose sur la mesure d'un flux lumineux $F_{\rm obs}$ acquis avec un télescope équipé d'un capteur photosensible ($\gamma$/s/m$^2$) ou un bolomètre (W/m$^2$), comparé à un flux de référence $F_{\rm ref}$ qui fixe l'échelle. Historiquement, cette dernière s'appuie sur une étoile étalon, Véga dans la constellation de la Lyre. Pour se raccorder aux 6 catégories de magnitudes définies dans l'Antiquité, la magnitude apparente d'un astre est définie par :
\begin{equation}
m = -2.5\log_{10} \left[\frac{F_{\rm obs}}{F_{\rm ref}} \right] 
\end{equation}
La magnitude absolue est le flux qu'on recevrait de cette source à une distance de $10\,\parsec$ :
\begin{equation}
M = -2.5\log_{10} \left[\frac{L}{4\pi (10\,\parsec)^2F_{\rm ref}} \right] 
\end{equation}

:::{note} Magnitudes

Le classement de la brillance des étoiles en magnitude vient de l'Antiquité, donc de l'observation visuelle. Entre les étoiles de magnitude 0 et 5, il se trouve qu'il y a un rapport cent en flux lumineux, les étoiles de magnitude faible étant les plus brillantes. Le flux est donc divisé par un facteur 2.5 entre chaque magnitude.
:::


#### Utopie des supernovistes

Dans un monde idéal, il suffirait de mesurer les flux $F_{\rm obs}^{(i)}$ d'une collection de $N$ supernovae de type Ia à des redshifts $z_i$ et de les comparer entre eux pour obtenir une relation entre distance de luminosité et redshift. En effet, la magnitude apparent $m_i$ d'une chandelle standard de redshift $z_i$ est liée au taux d'expansion $H(z)$ via la distance de luminosité:
\begin{align*}\label{eq:utopie}
m_i & = -2.5\log_{10} \left[\frac{ F_{\rm obs}^{(i)}}{F_{\rm ref}}\right] \\
& = -2.5 \log_{10} \frac{L}{4\pi D_L^2(z_i) F_{\rm ref}}  \\
& = 5 \log_{10}\left[ \frac{D_L(z_i)}{10\,\parsec}\right] + M
\end{align*}
On appelle module de distance la quantité :
\begin{equation}
\mu = 5 \log_{10}\left[ \frac{D_L(z_i)}{10\,\parsec}\right] = 5 \log_{10} \left[\frac{(1+z)}{10\,\parsec} \int_0^z \frac{\dd z}{H(z)}   \right]  \text{ si } k=0
\end{equation}
C'est la baisse de luminosité en magnitude liée à la distance de l'astre. Ainsi, l'ajustement d'un modèle cosmologique avec les paramètres $\Lambda$CDM sur les magnitudes $m_i$ (mesurées par comparaison à une même référence) permettrait de remonter aux paramètres cosmologiques de l'Univers. Le point le plus important à remarquer dans cette formule est que le signal cosmologique est inscrit dans la forme de la courbe, et non dans sa magnitude absolue donc sa normalisation (qui peut donc être un paramètre libre du modèle). Les chandelles standards permettent de mesurer les propriétés de l'expansion de l'Univers, mais il n'est pas nécessaire d'en connaître leur luminosité absolue $L$ !

La réalité est beaucoup moins simple :
- les flux lumineux sont observés à travers une certaine bande passante;
- les supernovae ont des spectres décalés vers le rouge, donc selon le redshift la luminosité apparente d'une supernova varie parce qu'elle est plus distant mais aussi parce qu'on en observe pas la même portion de spectre;
- l'atmosphère terrestre absorbe plus dans le bleu (diffusion Rayleigh en $\lambda^{-4}$) donc plus une supernovae est basse sur l'horizon plus elle est rougie et atténuée par rapport à une supernova au zénith (moins d'atmosphère à traverser pour la lumière);
- la poussière interstellaire de la Voie Lactée rougit et atténue aussi le spectre des objets extra-galactiques selon qu'ils sont proches du plan galactique ou aux pôles galactiques. 

Comme les supernovae de type Ia sont des chandelles standards, elles ont à peu près toute la même magnitude absolue dans une bande donnée. Historiquement, pour les supernovae de type Ia, les cosmologistes établissent les magnitudes en bande B (dans le système photométrique de Johnson UBV) dans le référentiel au repos. 
Le maximum d'émission se déplace en longueur d'onde avec le décalage vers le rouge, et sa puissance diminue avec la distance. Comme nous voulons comparer l'effet de la distance uniquement pour cartographier $D_L(z)$ et que nous n'avons pas de flux de référence bolométrique pur, ces effets de décalage doivent être supprimés pour standardiser et comparer le flux observé au maximum d'émission.

_La chandelle standard est donc le maximum d'émission des supernovae de type Ia dans la bande $B$ vu dans le référentiel au repos._


Dans ce cours, nous allons seulement aborder la complexité venant des deux premiers points énumérés ci-dessus.


### Modèle spectrophotométrique

#### Rest-frame magnitude

Les flux lumineux $F$ exprimés en ($\gamma$/s/m$^2$) ou (W/m$^2$) sont dits bolométriques[^bolo] car intégrés sur tout le spectre. Malheureusement la capacité à mesurer cette quantité dépend du capteur utilisé. Dans le visible et l'infrarouge, les capteurs sont basés sur l'effet photoélectrique donc ils sont transparents au-dessus d'une certaine longueur d'onde, donc les flux mesurés ne peuvent être bolométriques. 

De plus, beaucoup d'information peut être tirée de la mesure de la couleur d'un objet, comme le type de la supernova : pour cela il faut l'observer à travers différents filtres et comparer les flux. 

On introduit la densité spectrale d'énergie d'un astre $F_\lambda(\lambda)$ exprimée[^Sfreq] en W/m$^2$/nm. Les flux lumineux sont observés à travers par des télescopes équipés de filtres, ayant différentes bandes passantes. Notons $T_b(\lambda)$ la transmission de l'instrument dans la bande $b$. Le flux mesuré est alors :
\begin{equation}
F_{\rm obs,b} = \int \frac{\dd \lambda}{hc/\lambda} F_\lambda(\lambda) T_b(\lambda) \text{ en $\gamma$/m$^2$/s}
\end{equation}
où $\lambda$ est la longueur d'onde observée.
Alors la définition de la magnitude apparente en bande $b$ devient :
\begin{equation}
m_b = -2.5 \log_{10} \left[ \frac{\int \lambda \dd \lambda F_\lambda(\lambda) T_b(\lambda) }{\int \lambda \dd \lambda F_{\mathrm{ref}}(\lambda) T_b(\lambda)}\right]
\end{equation}
avec $F_{\mathrm{ref}}$ la densité spectrale de flux de la source de référence (Véga par exemple). La magnitude absolue en bande $b$ est la magnitude de l'astre en bande $b$ si on l'observait dans son référentiel au repos à $10\,\parsec$ :
\begin{equation}
M_b = -2.5\log_{10} \left[\frac{1}{4\pi (10\,\parsec)^2} \frac{\int \lambda \dd \lambda L_\lambda(\lambda) T_b(\lambda)}{\int \lambda \dd \lambda F_{\mathrm{ref}}(\lambda)T_b(\lambda) } \right] 
\end{equation}
avec $L_\lambda$ la luminosité spectrale (en W/nm). Pour les SNe Ia, $M_B = -19.08 \pm 0.03$ {cite:p}`Betoule2014`.

Le flux $F_{\rm obs}$ et la luminosité intrinsèque $L$ (en W) d'un astre situé au redshift $z$ s'écrit :
\begin{equation}\label{eq:boloPhiL}
F_{\rm obs} = \frac{L}{4\pi D_L^2(z)}
\end{equation}
avec $D_L(z)$ la distance de luminosité. Tous les photons reçus dans une étroite gamme de fréquences logarithmiques centrée sur la longueur d'onde observée $\lambda$ ont été émis dans une gamme de longueur d'onde centrée également étroite centrée sur $\lambda_E = \lambda / (1+z)$. L'équation [](#eq:boloPhiL) relie donc ainsi les densités spectrales de flux aux luminosités spectrales en présence d'un redshift $z$ {cite:p}`Condon2018`:
\begin{align}
\dd \lambda F_\lambda(\lambda) & =  \frac{\dd \lambda_E L_\lambda(\lambda_E)}{4 \pi D_L^2 (z)} =  \frac{\dd \lambda}{1+z}\frac{ L_\lambda(\lambda/(1+z))}{4 \pi D_L^2 (z)} \notag \\ 
& \Rightarrow F_\lambda(\lambda) =\frac{L_\lambda(\lambda/(1+z))}{4 \pi (1+z) D_L^2 (z)} 
\end{align}

Revenons au lien entre les flux observés et la distance de luminosité. Dans une bande $b$, la magnitude apparente est liée à la distance de luminosité par :
\begin{align*}
m_b & = -2.5 \log_{10} \left[ \frac{\int \lambda \dd \lambda F_\lambda(\lambda) T_b(\lambda) }{\int \lambda \dd \lambda F_{\mathrm{ref}}(\lambda) T_b(\lambda)}\right] \\
& = -2.5 \log_{10} \left[\frac{1}{4 \pi (1+z) D_L^2 (z)} \frac{\int \lambda \dd \lambda L_\lambda(\lambda/(1+z)) T_b(\lambda) }{\int \lambda \dd \lambda F_{\mathrm{ref}}(\lambda) T_b(\lambda)}\right] \\
& = M_B + \mu + K_{bB} 
\end{align*}
avec la magnitude absolue en bande $B$ :
\begin{equation}
M_B = -2.5\log_{10} \left[\frac{1}{4\pi (10\,\parsec)^2} \frac{\int \lambda \dd \lambda L_\lambda(\lambda) B(\lambda)}{\int \lambda \dd \lambda F_{\mathrm{ref}}(\lambda) B(\lambda)}   \right] 
\end{equation}
avec $B(\lambda)$ la transmission de la bande B et la _$K$-correction_ en bandes $b$ et $B$ {cite:p}`hogg2002k` :
\begin{align*}
K_{bB} &  = -2.5\log_{10} \left[\frac{1}{(1+z)} \frac{\int \lambda \dd \lambda F_{\mathrm{ref}}(\lambda) B(\lambda)}{\int \lambda \dd \lambda F_{\mathrm{ref}}(\lambda) T_b(\lambda)}  \frac{\int \lambda \dd \lambda L_\lambda(\lambda/(1+z)) T_b(\lambda) }{\int \lambda \dd \lambda L_\lambda(\lambda) B(\lambda)}\right]
\end{align*}
On voit donc que la dépendance en distance reste entièrement contenue dans le module de distance $\mu$, mais il existe une dépendance en redshift supplémentaire dans la $K$-correction qu'il faut modéliser. Cette dernière représente la correction en magnitude qu'il faut apporter si on observait l'astre dans son référentiel au repos. On note $m_B^* = m_b - K_{bB}$ la magnitude apparente dans le référentiel au repos en bande B, _comme s'il n'y avait pas d'expansion mais seulement un effet de distance_. Après l'application de la $K$-correction, le diagramme de Hubble se modélise simplement par :
\begin{equation}
\boxed{m_B^* = m_b - K_{bB} = M_B + \mu}
\end{equation}
une équation très similaire à [](#eq:utopie).  Malheureusement, la $K$-correction dépend d'un certain nombre d'ingrédients qu'il faut donc connaître pour la calculer :
- le redshift $z$, à inférer depuis un spectre;
- la densité spectrale $F_\lambda$ de la supernova, à construire par un modèle spectrophotométrique ajusté sur les séquences spectrales mesurées (comme dans la [](#fig:spectresIa)) comme SALT2 {cite:p}`Guy2007`;
- la densité spectrale de référence $F_{\mathrm{ref}}(\lambda)$, à établir par mesure (cite) ou modélisation d'atmosphère stellaire (cite);
- la transmission des filtres du télescope $T_b$, voire de la transmission atmosphérique du lieu $T_{\mathrm{atm}}(\lambda)$.

Pour obtenir une mesure du paramètre d'état de l'énergie noire $w_{DE}$ au pourcent, il faut donc que chacun de ces ingrédients soit établi à mieux que le pourcent. Aujourd'hui, les incertitudes dominantes sur la mesure de $w_{DE}$ par les supernovae de type Ia sont les incertitudes systématiques de calibration photométrique, donc la connaissance de la bande passante des filtres des instruments ainsi que la connaissance des flux de références {cite:p}`Betoule2013` (+ citer PANSTARS).


#### Standardisation

Après $K$-correction, on peut comparer les magnitudes $m_B^*$ à un modèle cosmologique. Avec les données JLA du SuperNova Legacy Survey, on obtient le diagramme de Hubble [](#fig:hubblemb).

```{figure} #hubbleDiagaramMb
:name: fig:hubblemb
:align: center
:width: 70%

Diagramme de Hubble des 740 SNeIa du relevé SNLS, comparé à un modèle $\Lambda$CDM avec $\Omega_m^0 = 0.3$ et $\Omega_\Lambda^0=0.7$.
```

Autour du diagramme, on observe que les résidus au diagramme de Hubble ont une dispersion de $0.4\,$mag, supérieures aux erreurs de mesure. Si on trace ces résidus en fonction de la couleur $c=B-V$ ou de la durée normalisée $x_1$ de la supernova, on s'aperçoit qu'ils sont corrélés ([](#fig:hubbleRes)). 

```{list-table} Résidus au diagramme de Hubble colorés en fonction de la durée normalisée $x_1$ (gauche) ou de la couleur $c=B-V$ (droite).
:header-rows: 0
:name: fig:hubbleRes

* - ```{image} #hubbleResX1
    :alt: x1
    :width: 95%
    :align: center
    ```
  - ```{image} #hubbleResC
    :alt: color
    :width: 100%
    :align: center
    ```
```

Il y a donc une variabilité des supernovae qui n'a pas été prise en compte dans notre modèle spectrophotométrique jusqu'à présent.



On observe que plus la courbe de lumière dure dans le temps, plus elle est brillante à son maximum (règle
du *brighter-slower*). De plus, plus les SNIa sont bleues, plus elles sont brillantes également (règle du *brighter-bluer*). 
Il y a aussi un effet d'environnement qui lie la brillance de la supernova et la masse de la galaxie hôte.




```{figure} ../images/courbes_de_lumiere_x1c.png
:name: fig:courbes_de_lumiere_x1c
:align: center
:width: 60%

Courbes de lumière de SNe Ia du lot de données JLA du relevé SNLS colorées en fonction de $x_1$ ou $c$ {cite:p}`nicola2022`.
```


Le flux de lumière est lié à la production et à la décroissance de
nickel $^{56}$Ni. Les deux relations présentées ci-dessus peuvent ainsi
être expliquées qualitativement: plus la SNIa produit de $^{56}$Ni, plus
elle sera brillante et contiendra d'émetteurs FeII/CoII (produits de la
désintégration de $^{56}$Ni, émettant dans le bleu), et plus elle sera
opaque (donc l'émission des photons par diffusion sera retardé, donc la
SNIa brillera plus longtemps) {cite:p}$`Kasen2007`.

Les SNe Ia ne sont donc pas si standard, car leur courbe de lumière dépend de la quantité de $^{56}$Ni produit à l'origine. Néanmoins sans corriger cette dispersion intrinsèque les équipes du Supernova Cosmology Project (SCP) mené par Saul Perlmutter et du High-z Supernova Search Team mené par Brian Schmidt ont pu démontrer l'existence d'une expansion accélérée {cite:p}`Riess1998; Perlmutter1999`. Cette dispersion est gênante pour améliorer les mesures d'expansion de l'Univers au niveau du pourcent. Néanmoins, elle se décrit empiriquement par deux relations linéaires pour $x_1$ et $c$ avec des coefficients $\alpha$ et $\beta$ respectivement (voir []()). Pour la masse de l'hôte, on ajuste un paramètre $\Delta M_{host}$ augmentant la magnitude pour les supernovae des se situant dans des galaxies de masse supérieure à $10^{10}\,M_\odot$.

Ces trois relations empiriques ajoutent trois paramètres supplémentaires $\alpha$, $\beta$ et $\Delta M_{host}$ à ajuster également sur les données :
\begin{equation}
\boxed{m_{B,corr}^* = M_B + \mu -\alpha x_1 + \beta c +  \Delta M_{host}}
\end{equation}
mais après cela la dispersion au diagramme de Hubble est réduite à $0.15\,$mag ce qui augmente la précision sur les contraintes de l'expansion de l'Univers.


```{figure} ../images/HD_jla.pdf
:name: fig:HD
:align: center
:width: 70%

Diagramme de Hubble des supernovæ du catalogue JLA. La courbe noire
représente un modèle $\Lambda$CDM ajusté aux données. Un modèle sans
énergie noire apparaîtrait significativement en dessous de la courbe
décrite par les données ($-0.6\,$mag à $z=1$).
```

:::{note} Origine de $\Delta M_{host}$

En effet, il semble que les galaxies massives contiennent beaucoup plus de métaux et que les supernovæ peuvent y apparaissent plus brillantes que dans les galaxies légères (voir la discussion section 5.5 de la référence {cite:p}`Sullivan2010`). Comme suggéré par la référence {cite:p}`Sullivan2010`, on divise les données en deux lots selon la masse de la galaxie hôte. 
:::




### Étalonnages

```{figure} ../images/strategy1.png
:name: fig:SNCalib
:align: center
:width: 70%

Stratégies pour étalonner la mesure du flux lumineux des étoiles tertiaires (les étoiles secondaires ne sont pas représentées). La bande $B$ redshiftée est représentée par un trait bleu épais sur les spectres des SNe Ia. 
```

### State of the art





Mesure locale de $H_0$
------------------------

Montrer que dans la diagramme précédent on ne peut pas mesurer H_0 car dégénéré



[^bolo]: Un capteur bolométrique est capable d'absorber des photons et de mesurer leur énergie peu importe leur longueur d'onde (par exemple en mesurant l'échauffement d'un matériau). A contrario, un capteur photonique basé sur l'effet photoélectrique devient transparent dans les grandes longueurs d'ondes, lorsque l'énergie du photon passe sous le seuil d'émission d'un électron.

[^Sfreq]: Ou en fréquence $S_\nu(\nu)$ exprimée en W/m$^2$/Hz.