---
short_title: Émissions astrophysiques
authors:
  - jbiteau
keywords: émissions astrophysiques
---


Émissions astrophysiques à l'échelle cosmique
=============================================

Un univers homogène et isotrope ?
--------------------------------

Les modèles cosmologiques que nous avons discutés postulent que l'univers est homogène et isotrope aux grandes 
échelles, c'est-à-dire à des distances typiquement supérieures à 100 Mpc. En dessous de cette échelle caractéristique, les galaxies observées dans les relevés optiques à grand champ sont distribuées le long de la toile cosmique. Les grandes structures qui tissent cette toile se sont formées suite à la croissance des fluctuations du CMB. En raison des propriétés de la gravitation, une surdensité initialement ellipsoïdale s'effondre préférentiellement le long de son axe le plus petit, résultant en une feuille (appelée crêpe de Zel'dovich). Ces feuilles peuvent s'effondrer sous forme de filaments, qui eux-mêmes convergent vers des amas de galaxies. Les zones non peuplées par la toile cosmique constituent les vides cosmiques, qui occupent la majeure partie de l'espace.

### Distance des grandes structures locales

Les structures qui forment la toile cosmique s'organisent en un réseau ressemblant à celui de bulles de savon
(voir [](#fig:bubble_network), gauche). Une représentation cristallographique simplifiée est donnée ci-dessous (voir [](#fig:bubble_network), droite), avec $l$ la taille caractéristique de cellule et $w$ le diamètre typique des amas, ou 
la section transversale des filaments. Les feuilles, également appelées murs pour les plus grandes, ont une épaisseur $w$ et une
aire $l^2$. Les simulations cosmologiques suggèrent un taux d'occupation des vides de l'ordre de $(1-w/l)³ =75\%$ (voir exercice 
ci-dessous). Sachant que le rayon caractéristique des amas que nous observons est $w \approx 1\,$Mpc,
nous en déduisons une taille de cellule typique de l'ordre de $l \approx 10\,$Mpc.


:::{figure} ../../images/bubble_network_2019GReGr..51....9F_ 2022A&A...662A..87O.jpg
:name: fig:bubble_network
:align: center
:width: 100%

Réseau de bulles de savon et modèle cubique illustrant la structure de la toile cosmique. Sur la partie droite, les nœuds en orange correspondent aux amas, les feuilles et filaments sont en bleu ciel et les vides en bleu foncé. Images tirées de {cite}`2019GReGr..51....9F` et {cite}`2022A&A...662A..87O`.
:::

:::{exercise} Facteur de remplissage volumique des grandes structures
:label: exo:volume_filling

Estimez l'occupation volumique relative des amas, filaments et feuilles en utilisant une approche cristallographique comme présentée ci-dessus.
:::

:::{solution} exo:volume_filling
:class: dropdown

Dans l'approche cristallographique présentée ci-dessus, les facteurs de remplissage volumique des amas, $\mathrm{VFF}_\mathrm{c}$, filaments, $\mathrm{VFF}_\mathrm{f}$, feuilles, $\mathrm{VFF}_\mathrm{s}$ et vides, $\mathrm{VFF}_\mathrm{v}$ sont

$$
\begin{aligned}
\mathrm{VFF}_\mathrm{c} &= \left(\frac{w}{l}\right)^3 \nonumber \\
\mathrm{VFF}_\mathrm{f} &= 3\left(\frac{w}{l}\right)^2 \left(1 - \frac{w}{l}\right) \nonumber \\
\mathrm{VFF}_\mathrm{s} &= 3\frac{w}{l} \left(1-\frac{w}{l}\right)^2 \nonumber \\
\mathrm{VFF}_\mathrm{v} &= \left(1-\frac{w}{l}\right)^3
\end{aligned}
$$

Notez que la somme est égale à 1 en raison de l'identité binomiale $\left(\frac{w}{l} + \left(1-\frac{w}{l}\right)\right)^3 = 1$.


Le tableau suivant, adapté de {cite}`2022A&A...662A..87O`, fournit une comparaison entre notre estimation simple et les valeurs déduites d'un ensemble typique de simulations cosmologiques.

| Type de structure | Cellule cubique $w/l = 0.1$ | Résultats de simulations cosmiques |
| :---------------- | :--------------------------: | :---------------------------------: |
| Vides             | 72.9%                        | 76%                                 |
| Feuilles          | 24.3%                        | 18%                                 |
| Filaments         |  2.7%                        |  5%                                 |
| Amas              |  0.1%                        |0.5%                                 |

Note : Les simulations cosmologiques à grande échelle indiquent qu'à $z=0$, les amas et filaments englobent respectivement ${\sim}\,50\%$ et $
{\sim}\,45\%$ de la matière noire. En tenant compte de la rétroaction des vents galactiques et des jets, on suggère une distribution baryonique plus diffuse : ${\sim}\,25\%$ des baryons se trouveraient dans les amas, ${\sim}\,45\%$ dans les filaments et feuilles, ${\sim}\,30\%$ dans les vides {cite:p}`2016MNRAS.457.3024H`.
:::

Les quatre types de structures (vides, feuilles ou murs, filaments, amas) sont visibles dans la distribution des 
galaxies proches. Notre galaxie, sa voisine Andromède à $0.75\,$Mpc et leurs satellites, tels que le Grand Nuage de Magellan à $50\,$kpc, forment le Groupe Local. Comme illustré dans [](#fig:council-giants), le Groupe Local se trouve au cœur 
de la Feuille Locale. Cette feuille est une structure planaire d'un diamètre de ${\sim}\,10\,$Mpc, délimitant un côté du Vide Local.


:::{figure}  ../../images/mccall_fig3.jpeg
:name: fig:council-giants
:align: center
:width: 70%

Galaxies de la Feuille Locale ($R \approx 5\,$Mpc) entourant le groupe local ($R \approx 1\,$Mpc). D'après {cite}`2014MNRAS.440..405M`.
:::

À l'opposé de la galaxie NGC 253, à environ $16\,$Mpc de la Voie Lactée, se trouve l'amas de galaxies de la Vierge, qui présente une structure en forme de ballon de rugby, comme on peut le voir ci-dessous. Les amas de galaxies peuvent contenir plusieurs milliers de galaxies.

:::{figure}  ../../images/virgo_2007ApJ...655..144M.jpg
:name: fig:virgo
:align: center
:width: 70%

Distribution spatiale des galaxies dans l'amas de la Vierge avec des distances bien contraintes en coordonnées supergalactiques (le plan supergalactique est une structure historique presque identique à la Feuille Locale, avec une inclinaison de 8°). Les galaxies les plus brillantes sont représentées en rouge. D'après {cite}`2007ApJ...655..144M`.
:::

Les amas de galaxies tels que la Vierge sont connectés à la toile cosmique par des filaments de galaxies, dont la position dans le plan céleste et la projection de vitesse radiale peuvent être déduites par spectroscopie, comme illustré ci-dessous.

:::{figure}  ../../images/virgo_filaments_2022ApJS..259...43C
:name: fig:filaments
:align: center
:width: 100%

Les filaments autour de l'amas de la Vierge. La distribution des galaxies dans le ciel est représentée en coordonnées équatoriales (ascension droite, R.A., et déclinaison, Dec, en degrés). D'après {cite}`2022ApJS..259...43C`.
:::

À une échelle encore plus grande, typiquement $100\,$Mpc, les amas sont regroupés en superamas tels que Laniakea, qui nous héberge.

:::{figure}  ../../images/laniakea_2014Natur.513...71T.jpg
:name: fig:supercluster
:align: center
:width: 100%

Les superamas locaux. Les lignes de flux de vitesse de notre superamas, Laniakea, sont représentées en blanc. D'après {cite}`2014Natur.513...71T`.
:::

### Masse des grandes structures locales

Non seulement les astronomes peuvent mesurer la position des galaxies dans le ciel, mais ils peuvent également mesurer la composante radiale de 
leur vitesse ainsi que leur distance en utilisant les étoiles qui calibrent l'échelle de distance cosmique. Le champ de vitesse des galaxies peut ainsi être utilisé pour contraindre le champ gravitationnel de Laniakea ou de son superamas compagnon 
Persée-Poissons. La masse du superamas Laniakea est estimée à ${\sim}\,10^{17}\, M_\odot$ {cite:p}`2014Natur.513...71T`. [^a] 
À plus petite échelle, la masse de l'amas de la Vierge est estimée à ${\sim}\,10^{15}\, M_\odot$ {cite:p}`2016A&A...596A.101P`. De tels arguments dynamiques donnent également une estimation de la masse du Groupe Local de galaxies à ${\sim}\,3 \times 10^{12}\, M_\odot$. La masse dynamique du Groupe Local est dominée par celle de la Voie Lactée, $(1. 2 \pm 0.2)  \times 10^{12}\, M_\odot$ et d'Andromède, $(1.8 \pm 0.5) \times 10^{12}\, M_\odot$ {cite:p}`2022ApJ...928L...5B`.


[^a]: Le soleil a une masse mesurée avec une précision meilleure que $10^{-4}$ à $M_\odot = 1.9885 \times 10^{30}\,$kg.


Ces masses sont déduites en utilisant des arguments dynamiques tels que le théorème du viriel (|énergie cinétique| = |énergie potentielle|/2 pour un système à l'équilibre) ou en utilisant les trajectoires projetées des traceurs. En utilisant les étoiles comme traceurs, 
les astronomes estiment la masse du trou noir central de la Voie Lactée, Sgr A*, à $(4.15 \pm 0.01) \times 10^{6}\, M_\odot$ {cite:p}`2019A&A...625L..10G` (voir [](#fig:S2-trajectory)). Ce dernier a une faible contribution à la masse de notre galaxie par rapport aux étoiles qui la composent $(6 \pm 1)  \times 10^{10}\, M_\odot$ {cite:p}`2015ApJ...806...96L`.
La masse de la Voie Lactée contenue dans les baryons (étoiles et poussière) est elle-même environ 20 fois inférieure à sa masse dynamique.


:::{figure}  ../../images/S2_orbit.jpg
:name: fig:S2-trajectory
:align: center
:width: 100%

L'orbite de 16 ans de l'étoile S2 autour du trou noir massif Sgr A*, qui a également été suivie spectroscopiquement pendant 27 ans. D'après {cite}`2019A&A...625L..10G`.
:::

Le déficit de masse (masse dynamique moins masse baryonique) observé dans la Voie Lactée est également déduit au niveau des 
populations de galaxies. La masse stellaire de chaque galaxie peut être estimée en utilisant des observations dans le proche infrarouge. À ces longueurs 
d'onde (autour de $1-3\,$µm), l'émission des étoiles de taille moyenne comme le Soleil est élevée par rapport à celle de la poussière, qui 
émet principalement à des longueurs d'onde supérieures à $5\,$µm, et à celle des étoiles plus massives et plus jeunes, qui émettent 
principalement dans l'UV et la bande bleue.


:::{exercise} Masse stellaire dans les galaxies
:label: exo:stellar_mass

En supposant que la masse (ou la luminosité associée) suit une loi de distribution selon une fonction de Schechter, 
$$f(M_\star) \dd M_\star= n_\star \left(\frac{M_\star}{M_0} \right)^{-\alpha} \exp\left(-\frac{M_\star}{M_0} \right) \dd M_\star,
$$
calculez la densité d'énergie de masse stellaire en utilisant [](#fig:stellar_mass).

```{figure}  ../../images/stellar_mass_fun_2022MNRAS.513..439D.jpg
:name: fig:stellar_mass
:align: center
:width: 100%

La fonction de masse stellaire des galaxies dans l'Univers local ($z<0.1$). D'après {cite}`2022MNRAS.513..439D`.
```

Astuce mathématique utile : la [fonction Gamma](https://fr.wikipedia.org/wiki/Fonction_gamma) est définie comme $\Gamma(x) = 
\int_0^\infty\dd t\, t^{x-1} \exp(-t)$, avec $\Gamma(\frac{1}{2}) = \sqrt{\pi}$.

:::


:::{solution} exo:stellar_mass
:class: dropdown

Le premier panneau représente la fonction $g(M_\star)$ telle que $\int g(M_\star) \dd \log_{10}M_\star = 1/V$,
où $V$ est le volume considéré et où $\log_{10}(x) = \frac{\ln(x)}{\ln(10)}$. 
Comme $f(M_\star)\dd M_\star = g(M_\star) \dd \log_{10} M_\star$, nous trouvons $f(M_\star) = g(M_\star)/(\ln(10)M_\star)$.

D'après le premier panneau, nous estimons à l'œil un seuil à $M_0 \approx 1 \times 10^{11}
\,M_\odot$ où la densité est
$g(M_0) = \ln(10) M_0 n_{\star}/e \approx 2  \times  10^{-3}\,\mathrm{Mpc}^{-3}\,\mathrm{dex}^{-1}$.
Nous trouvons $n_{\star} M_0 \approx 2 \times 10^{-3} \,\mathrm{Mpc}^{-3}$. L'indice est similairement estimé à $\alpha=1.5$.

La densité d'énergie de masse stellaire est alors

$$
\begin{align}
\int f(M_\star) M_\star c^2 \dd M_\star &= n_\star M_0 \times M_0  c^2 \int \dd x \, x^{1-\alpha} \exp(-x) dx \nonumber\\
							&=\Gamma(2-\alpha) \times n_\star M_0 \times M_0  c^2 \nonumber\\					
							&\approx \sqrt{\pi} \times 2 \cdot 10^{-3} \times 10^{11} \times  1.1 \cdot 10^{66}/(3.1 \cdot 10^{22})^3\,\mathrm{eV\,m}^{-3} \nonumber\\
														&\approx 13 \times 10^{6}\,\mathrm{eV\,m}^{-3}.
\end{align}
$$

L'estimation utilisant la forme exacte de la fonction de distribution de masse donne une densité de matière stellaire jusqu'à $z < 0. 1$ ou $D_L < 500\,$Mpc de $\rho_{\star, 0}= (2.97 \pm 0.04) \times 10^8 \,h_{70}\, M_\odot \, \mathrm{Mpc}^{-3}$, où $h_{70} = H_0 / (70\,\mathrm{km}\,\mathrm{s}^{-1}\,\mathrm{Mpc}^{-1})$. Cela correspond à une densité d'énergie comparable à notre estimation grossière, à savoir $\varepsilon_{\star, 0} \approx (11.0 \pm 0.1) \, h_{70} \times 10^{6}\,\mathrm{eV\,m}^{-3}$
:::


:::{note} $M_\odot$ par Mpc$^{3}$ et eV par m$^3$
L'énergie de masse au repos du soleil est $M_\odot c^2 \approx 1.8\times 10^{47} \, \mathrm{J} \approx 1.1\times 10^{66}\,\mathrm{eV}$. La distance typique entre galaxies voisines est $1\, \mathrm{Mpc} \approx 3.1 \times 10^{22}\, \mathrm{m}$. La bonne correspondance entre les puissances de dix ($66 = 22 \times 3$) rend assez facile la conversion de la densité de masse stellaire en densité d'énergie.
:::

### Inventaire énergétique cosmique

Pour une densité d'énergie aujourd'hui égale à la densité critique 
$\rho_{c,0} = \frac{3 H_0^2  c^2}{8\pi G} = 1.36 \times 10^{11}\, h_{70}^2\, M_\odot\,\mathrm{Mpc}^{-3}$, 
c'est-à-dire $\varepsilon_{c,0} \approx 5.1\, h_{70}^2\,$GeV$\,$m$^{-3}$, 
où $h_{70} = H_0 / 70 \,\mathrm{km}\,\mathrm{s}^{-1}\,\mathrm{Mpc}^{-1}$, 
la solution de [](#exo:stellar_mass) montre que seulement deux millièmes du budget énergétique de l'univers sont constitués d'étoiles. Une répartition détaillée des différents budgets énergétiques de l'univers est présentée ci-dessous.

:::{figure}  ../../images/cosmic_inventory.png
:name: fig:cosmic_inventory
:align: center
:width: 100%

L'inventaire énergétique cosmique de {cite}`2004ApJ...616..643F`. Adapté de cette [page](https://www2.mpia-hd.mpg.de/home/poessel/UT2012/).
:::


:::{note}
La majeure partie de ce que nous savons sur l'univers provient de quatre messagers : les photons, les neutrinos, les rayons cosmiques et les ondes gravitationnelles. Comme le montre [](#fig:cosmic_inventory), la densité d'énergie associée à ces traceurs n'est que de quelques parties par million. Malgré cela, les estimations de la quantité de matière baryonique à partir du rayonnement sont de plus en plus précises. On note en particulier la résolution potentielle d'un problème de longue date, la localisation de la moitié manquante des baryons de l'univers, qui pourrait se trouver dans le plasma intergalactique chaud/tiède qui constitue la toile cosmique (voir {cite}`2021NatAs...5..852D`).
:::



Moteurs cosmiques derrière les émissions astrophysiques
--------------------------------

Les processus responsables de la plupart des émissions astrophysiques sont la formation d'étoiles, l'accrétion de matière baryonique et 
l'éjection de jets de plasma par les trous noirs, en particulier les trous noirs supermassifs
(de masses $M_\bullet \approx 10^6 - 10^{10} M_\odot$).

### Formation stellaire

L'évolution de la matière baryonique et l'émission de lumière suivent l'histoire cosmique de formation des étoiles. Leur taux de 
formation par unité de volume comobile est illustré dans [](#fig:csfh).

:::{figure}  ../../images/SFRD_2014ARA&A..52..415M.png
:name: fig:csfh
:align: center
:width: 80%

L'histoire cosmique du taux de formation stellaire. D'après {cite:p}`2014ARA&A..52..415M`.
:::

Dans cette figure, le décalage vers le rouge, qui est défini par la relation $1+z = \frac{a_0}{a}$ avec $a$ le facteur d'échelle et 
$a_0=1$, est converti en âge cosmologique en utilisant une cosmologie $\Lambda$CDM plate, avec constante de Hubble $H_0 = 70\,\mathrm{km}\,\mathrm{s}^{-1}\,\mathrm{Mpc}^{-1}$ et densité d'énergie noire $\Omega_\Lambda = 0.7$, c'est-à-dire avec $\Omega_\mathrm{m} = 0.3$. Le temps de regard en arrière est la contrepartie de l'âge cosmique, c'est-à-dire $t_{L}(z) = \int_0^z \dd z' \left|\frac{\dd t}{\dd z'} \right|$, où 


$$
\begin{align}
\frac{\dd t}{\dd z} &= \left[\frac{\dd z}{\dd t}\right]^{-1} \nonumber \\
					&= -\left[\frac{1}{a^2} \frac{\dd a}{\dd t}\right]^{-1} \nonumber \\
					&= -\left[(1+z)H(z)\right]^{-1} 
\end{align}
$$
C'est-à-dire, dans un modèle $\Lambda$CDM plat avec $H(z) = H_0\sqrt{\Omega_\Lambda + \Omega_\mathrm{m}  (1+z)^3}$ (rayonnement 
négligé) :

$$			
\left|\frac{\dd t}{\dd z}\right| =  \frac{1}{H_0} \frac{1}{(1+z)\sqrt{\Omega_\Lambda + \Omega_\mathrm{m}  (1+z)^3}},
$$

avec une contribution négligeable de la densité d'énergie associée au rayonnement, $\Omega_\mathrm{r}$. 

L'évolution du taux de formation stellaire, $\Psi$, détermine l'évolution de la fraction de la masse baryonique 
contenue dans les étoiles et le gaz, ainsi que l'enrichissement du milieu interstellaire dans les galaxies. Par exemple, la densité de masse 
contenue dans les étoiles, $\rho_\star$ montrée dans [](#fig:csmh), peut être calculée à partir de l'équation de conservation suivante :
$$
\frac{\dd \rho_\star}{\dd t} = (1-R) \Psi
$$

Ici $R$ est la "fraction de retour", c'est-à-dire la proportion de matière réinjectée dans le milieu interstellaire par les vents stellaires et les explosions. La valeur de $R$ est estimée à $30-40\%$, selon la distribution initiale de masse stellaire dans une galaxie typique, qui est appelée la fonction de masse initiale.

:::{figure}  ../../images/smd_2014ARA&A..52..415M.png
:name: fig:csmh
:align: center
:width: 80%

Évolution cosmique de la densité de masse stellaire. D'après {cite:p}`2014ARA&A..52..415M`.
:::

L'évolution de la formation stellaire dans l'univers, qui est montrée dans [](#fig:csfh) a conduit à un enrichissement des 
milieux interstellaires en atomes plus lourds que le carbone, appelés métaux en astrophysique thermique. Cet enrichissement est dû à 
la nucléosynthèse dans les premières étoiles à partir de l'hydrogène et de l'hélium primordiaux (voir [chaîne pp](wiki:Proton–proton_chain) et 
[cycle CNO](wiki:CNO_cycle)). Ces premières étoiles, connues sous le nom d'étoiles de Population III, ont contribué à la réionisation de 
leur environnement durant leur courte durée de vie de quelques millions d'années. Les étoiles les plus massives (${>}\,8\,M_\odot$) 
ont explosé en supernovae et ont éjecté des métaux qui ont alimenté les générations suivantes d'étoiles, et ainsi de suite jusqu'au Soleil, 
qui appartient à la Population I. Le gaz, les molécules - comme les plus abondantes H$_2$ et CO - et la poussière - sous forme de 
grains carbonés et de silicates amorphes - ont continué à s'accumuler dans le milieu interstellaire tout au long des trois premiers milliards d'années de l'univers jusqu'au pic cosmique de formation stellaire autour d'un décalage vers le rouge $z \sim 2$. Cette période 
d'activité accrue de formation stellaire est connue sous le nom de "midi cosmique". Depuis lors, l'univers a été peuplé principalement par 
des étoiles de Population I à longue durée de vie, typiquement $t_\odot \approx 10\,$Gyr pour le Soleil. Leur taux moyen de formation a 
diminué à mesure que le réservoir de gaz disponible dans le milieu interstellaire s'est épuisé jusqu'à aujourd'hui.


Comme pour la masse de matière contenue dans les étoiles aujourd'hui, l'émission cumulée des processus de nucléosynthèse est proportionnelle à l'intégrale du taux de formation stellaire cosmique.


:::{exercise} Densité d'énergie cosmique de photons produits par la nucléosynthèse
:label: exo:photons_nucl

1. Estimez l'efficacité de conversion de la matière en lumière, $\eta_\odot$, au sein d'étoiles similaires au Soleil. Sa luminosité bolométrique est $L_\odot = 3.8 \times 10^{26}\,$W.

2. Discutez l'efficacité de cette production de lumière par rapport à celle de la chaîne pp ($4 p + 2 e^- \rightarrow\ ^{4}\mathrm{He}^{2+} + 2 \nu_e$), qui libère $26.1\,$MeV d'énergie sous forme de photons (et $0.6\,$MeV sous forme d'énergie cinétique de neutrinos).

3. À partir de l'efficacité de conversion lumière-matière dans le soleil et de la densité de taux de formation stellaire, calculez la densité d'énergie dans le champ de photons émis par toutes les étoiles de l'univers.
:::

:::{solution} exo:photons_nucl
:class: dropdown

1. $$\begin{align}
\eta_\odot &= \frac{L_\odot t_\odot}{M_\odot c^2} \nonumber \\
& \approx 7 \times 10^{-4}
\end{align}$$

2. $$\eta_\mathrm{pp} \approx \frac{26.1}{4\times 938} \approx 7 \times 10^{-3}$$

L'efficacité de la conversion matière-lumière dans le Soleil n'est donc qu'un dixième de l'efficacité théorique maximale. Il convient de noter que bien que la chaîne pp soit dominante au sein du Soleil, cela ne signifie pas que tous ses protons sont impliqués dans les processus de fusion.

3. $$\begin{align}
\varepsilon_{\gamma, \mathrm{nucl}} &= \eta_\odot c^2 \int \dd t \Psi(t) \nonumber \\
& \approx 7 \cdot 10^{-4} \times 10^{10} \times 0.05 M_\odot c^2 \,\mathrm{Mpc}^{-3}  \nonumber\\
& \approx 3.5\cdot 10^{5} \times 1.1\cdot 10^{66}/(3.1\cdot 10^{22})^3 \mathrm{\,eV\,m}^{-3}  \\
& \approx 13 \times 10^{3}\mathrm{\,eV\,m}^{-3}
\end{align}$$

À titre de comparaison, la densité d'énergie contenue dans le CMB est vingt fois plus grande, c'est-à-dire $\varepsilon_{\gamma, \mathrm{CMB}} = 260 \times 10^3\mathrm{\,eV\,m}^{-3}$ (ou $0.26\mathrm{\,eV\,cm}^{-3}$).
:::

### Accrétion

Les galaxies se sont formées de manière hiérarchique, d'abord par la concentration de matière baryonique dans leurs halos de faible masse, 
puis par fusion avec d'autres galaxies dans la toile cosmique. L'évolution des galaxies s'accompagne de la croissance de 
leur trou noir massif central. La masse de ces trous noirs, $M_\bullet \approx 10^6 - 10^{10} M_\odot$, représente 
environ deux millièmes de la masse stellaire du bulbe de la galaxie hôte {cite:p}`2020ApJ...888...37D`. Cette 
relation illustre la co-évolution des trous noirs centraux et de leurs galaxies hôtes. De nombreuses autres corrélations 
entre observables soutiennent ce lien : par exemple la relation $M_\bullet - \sigma_\star$ entre la masse du trou noir et la dispersion des vitesses stellaires au sein des sphéroïdes (galaxie elliptique ou bulbe central pour une galaxie 
spirale). Le taux d'accrétion de matière par les trous noirs massifs suit ainsi une évolution, $\Psi_\mathrm{accr}$, 
comparable à celle du taux de formation stellaire, avec une densité $2000-3000$ fois inférieure comme le montre [](#fig:csmh).

:::{figure}  ../../images/accr_2014ARA&A..52..415M.png
:name: fig:csmh
:align: center
:width: 80%

L'évolution du taux de formation stellaire (courbe noire) et du taux d'accrétion des trous noirs massifs (courbes et bandes colorées). Les estimations du taux d'accrétion sont multipliées par un facteur de ${\sim}\,3000$ pour les ramener à l'échelle du taux de formation stellaire. D'après {cite:p}`2014ARA&A..52..415M`.
:::

L'accrétion de matière autour des trous noirs supermassifs est la deuxième source d'énergie la plus importante pour l'émission de lumière après 
la formation stellaire. Ces processus d'accrétion laissent une signature particulièrement prononcée dans les galaxies à noyaux actifs 
(environ 1% de toutes les galaxies). Ces processus d'accrétion peuvent être observés le plus clairement dans les galaxies à noyaux actifs, qui représentent environ 1% de toutes les galaxies. De tels noyaux actifs de galaxies, constitués d'un trou noir supermassif et d'un disque d'accrétion, peuvent dépasser la luminosité combinée de toutes les étoiles de la galaxie hôte.

L'énergie libérée par l'accrétion sous forme de photons peut être estimée en utilisant l'argument de Soltan
{cite:p}`1982MNRAS.200..115S`. L'énergie d'une particule test accrétée par un trou noir depuis la dernière orbite marginalement 
stable n'est qu'une fraction de l'énergie de masse au repos. Le reste peut être libéré sous forme de rayonnement. L'efficacité radiative du processus d'accrétion, $\eta_\mathrm{accr}$, est définie comme le rapport de la puissance rayonnée au taux de dépôt d'énergie-masse dans le disque, mesuré par un observateur à l'infini. En tenant compte de la décélération de la rotation du trou noir par les photons accrétés, Thorne calcule une efficacité radiative de $5.7\% < \eta_\mathrm{accr} < 30.8\%$ {cite:p}`1974ApJ...191..507T`.[^b]

[^b]: La borne supérieure de cette plage est inférieure aux 42% attendus pour un trou noir de Kerr en rotation maximale. La différence avec la valeur estimée par Thorne est due à la capture de photons.

### Éjection

Environ 10% des noyaux actifs de galaxies développent un jet de part et d'autre du disque d'accrétion {cite:p}`2019ARA&A..57..467B`.
La présence de jets est déduite ou observée dans de nombreux systèmes astrophysiques. C'est le cas pour les AGN avec jets, mais aussi 
pour les sursauts gamma longs qui résultent de l'effondrement d'étoiles massives, pour les sursauts gamma courts qui résultent 
des fusions de deux objets compacts (trous noirs de taille stellaire ou étoiles à neutrons), et pour les micro-quasars constitués d'un objet compact accrétant de la matière d'une étoile compagnon. 

L'éjection de plasma dans de tels jets résulte de la conversion de l'énergie électromagnétique à leur base en énergie cinétique 
à leur terminaison. L'énergie cinétique des jets peut être estimée pour certains noyaux actifs de galaxies par la taille des 
cavités radio qu'ils forment dans le milieu intra-amas {cite:p}`2012ARA&A..50..455F`. Les modèles d'évolution synthétiques 
qui tentent de reproduire ces observations estiment qu'environ ${\sim}\,0.5\%$ de l'énergie de masse associée à 
l'accrétion est injectée dans les jets des noyaux actifs de galaxies {cite:p}`2008MNRAS.388.1011M`. Cependant, les 
incertitudes entourant les mécanismes de formation des jets et les différents régimes d'accrétion signifient que ce rapport 
n'est qu'une estimation grossière de l'équilibre entre l'énergie cinétique et l'énergie accrétée.

La conversion du flux de Poynting (énergie électromagnétique) en mouvement global du plasma (énergie cinétique) est 
accompagnée par l'accélération de particules chargées, par exemple par des ondes de choc dans les jets ou à sa frontière 
(cisaillement), ou par reconnexion magnétique. Les particules accélérées perdent de l'énergie par des processus radiatifs : synchrotron et 
Compton inverse pour les électrons et positrons, ainsi que production de paires et de pions pour les protons et noyaux. Ces 
pertes radiatives produisent l'émission des jets des ondes radio aux rayons gamma. L'efficacité de conversion de l'énergie cinétique en rayonnement est estimée à $10\%$ pour les jets des noyaux actifs de galaxies, les sursauts gamma et les microquasars.



:::{exercise} Densité d'énergie cosmique de photons issus de l'accrétion et des jets
:label: exo:photons_accr

1. Quelle est la fraction d'énergie de masse qui peut être convertie en rayonnement pour un trou noir accrétant au taux $\dot M$ avec une efficacité radiative $\eta_\mathrm{accr}$ ?

2. Estimez la densité d'énergie des photons issus de la matière accrétée par les trous noirs massifs.

3. Estimez la densité d'énergie des photons issus des jets émis au voisinage des trous noirs massifs.
:::

:::{solution} exo:photons_accr
:class: dropdown
1. Considérons pour l'exercice $\eta_\mathrm{accr} \approx 20\%$. La fraction de masse effectivement accrétée par le 
   trou noir est $1-\eta_\mathrm{accr}$. L'énergie de masse qui peut être convertie en rayonnement est donc $\frac{\eta_\mathrm{accr}}{1-\eta_\mathrm{accr}} \dot M$.

2. Pour $\psi_\mathrm{accr}(t) = f_\mathrm{accr} \psi(t)$ avec $f_\mathrm{accr} = 1/3000$, la densité d'énergie du champ de photons émis par les processus d'accrétion est
$$\begin{align}
\varepsilon_{\gamma, \mathrm{accr}} &= \frac{\eta_\mathrm{accr}}{1-\eta_\mathrm{accr}} c^2 \int \dd t \Psi_\mathrm{accr}(t) \nonumber \\
	&=  f_\mathrm{accr} \frac{\eta_\mathrm{accr}/\eta_\odot}{1-\eta_\mathrm{accr}} \varepsilon_{\gamma, \mathrm{nucl}} \nonumber \\
& \approx 1.5 \times 10^{3}\mathrm{\,eV\,m}^{-3}
\end{align}$$

3. En utilisant le rapport de l'énergie cinétique du jet à l'énergie de masse accrétée de $0.5\%$ et en supposant que 10% de l'énergie cinétique va au rayonnement, nous obtenons un facteur de conversion d'énergie entre masse accrétée et émission de photons par les jets $\eta_\mathrm{jet} \approx 0.05\%$ à l'échelle cosmique. La densité d'énergie des photons rayonnés par les jets devrait alors être de l'ordre de

$$\begin{align}
\varepsilon_{\gamma, \mathrm{accr}} &=\eta_\mathrm{jet} c^2 \int \dd t \Psi_\mathrm{accr}(t) \nonumber \\
	&=  f_\mathrm{accr} \frac{\eta_\mathrm{jet}(1-\eta_\mathrm{accr})}{\eta_\mathrm{accr}} \varepsilon_{\gamma, \mathrm{accr}} 
\nonumber \\
& \approx 3 \mathrm{\,eV\,m}^{-3}
\end{align}$$

L'émission produite par l'accrétion n'est pas négligeable, surtout si l'on réalise que seulement 1% des galaxies ont un noyau actif {cite:p}`2010ApJ...723.1447H`.
:::
 
Maintenant que nous avons estimé les densités d'énergie associées aux champs de photons émis par les trois processus 
astrophysiques majeurs, nous pouvons les comparer avec les observations, comme couvert dans le prochain cours.


:::{tip}
**Notions de ce chapitre**

_Échelles de distance et de masse_
- Quel est le rayon typique du Groupe Local et de la Feuille Locale ? Quelle est la distance à l'amas de la Vierge ? Quelle est la taille de Laniakea ?
- Quelle est la masse typique d'un trou noir supermassif ? Comment se compare-t-elle à la masse stellaire et dynamique d'une galaxie telle que la Voie Lactée ?

_Formation stellaire / Accrétion / Éjection_
- Puis-je définir en quelques lignes ces notions ?
- Puis-je donner des exemples de classes de sources astrophysiques alimentées par ces processus ? 

:::
