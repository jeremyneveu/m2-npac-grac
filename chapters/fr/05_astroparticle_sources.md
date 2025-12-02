---
short_title: Sources d'astroparticules avec et sans jets
authors:
  - jbiteau
keywords: jet
---

Sources d'astroparticules avec et sans jets dans l'univers
=============================================


Émissions électromagnétiques à l'échelle cosmique
--------------------------------

### Densité d'énergie, brillance de surface, densité de flux et luminosité

Une observable directement liée à la densité d'énergie d'un champ isotrope de particules relativistes est la brillance de surface du ciel. Suivant la notation de {cite}`1986rpa..book.....R`, la brillance de surface bolométrique ou intensité bolométrique, $I$, est définie comme l'énergie passant à travers une surface $\dd A$ pendant un temps $\dd t$ et provenant d'un angle solide $\dd \Omega$ :
$$
\dd E = I \dd A \dd t \dd \Omega,
$$
avec $[I] = \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}$.

La densité d'énergie du champ de particules relativistes, $\varepsilon$, dans un volume $\dd V = c \dd t \dd A$ est 
telle que $dE = \varepsilon \dd V$, de sorte que l'intensité moyenne intégrée sur la sphère est
$$
I = \frac{c}{4\pi} \varepsilon
$$ 

:::{important}
L'intensité spécifique, $I_\nu$, est la dérivée de l'intensité bolométrique, $I$ :

$$
I = \int \dd \nu\ I_{\nu}, \quad \mathrm{avec\ } [I_{\nu}] =  \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{Hz}^{-1}
$$

L'intensité spécifique est souvent représentée sous la forme $\nu I_\nu$ en fonction de $\ln \nu$, puisque l'intégrale sous 
la courbe donne alors l'intensité bolométrique :
$$\int \dd \ln \nu\ \nu I_{\nu} = \int \dd \nu\ I_{\nu} = I$$

Les astronomes radio-optiques tracent souvent $\nu I_\nu$, tandis que les astronomes X et à plus haute énergie considèrent souvent 
$E^2 J(E) = \nu I_\nu$, où les deux quantités sont en unités de puissance par unité de surface par unité d'angle solide. L'intensité différentielle de particules, $J(E)$, où "différentielle" signifie "par unité d'énergie", est donc en unités de
$\#\, \mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{s}^{-1}\,\mathrm{eV}^{-1}$ avec $\#$ indiquant un nombre de particules.

De même, la densité de flux spécifique d'une source ponctuelle, notée $S_\nu$ ou $F_\nu$ avec
$[F_\nu] = \mathrm{W}\,\mathrm{m}^{-2}$, est représentée comme $\nu F_\nu = E^2 \frac{\dd N}{\dd E}$, où
$\frac{\dd N}{\dd E}$ est le flux différentiel de particules en unités de
$\mathrm{m}^{-2}\,\mathrm{s}^{-1}\,\mathrm{eV}^{-1}$. Notez que $\frac{\dd N}{\dd E}$ devrait formellement être écrit comme
$\frac{\dd N}{\dd E \dd A \dd t}$. En pratique, la différentiation de surface et de temps sont omises dans la notation standard
$\frac{\dd N}{\dd E}$ trouvée dans la littérature. 

Les luminosités spécifique et bolométrique sont estimées à partir du flux, $F_\nu$, et de la distance de luminosité, $D_L$ comme 
$L_\nu = 4\pi D_L^2 F_\nu$ et $L = 4\pi D_L^2 F$.

Le flux net émis par une région sur un angle solide $\dd \Omega$ à un angle zénithal $\theta$ peut être calculé à partir 
de la brillance de surface de cette région comme
$$
F = \int \dd\Omega\ I \cos \theta 
$$ 

Notez que si $I$ est isotrope, le flux net total est nul car l'énergie traversant la surface $\dd A$ dans la direction $+\vec{n}$ 
est l'opposé de celle provenant de la direction $-\vec{n}$.


:::

:::{note}
La littérature utilise parfois la notation $I_{\mathrm{dex}}$ avec
$[I_{\mathrm{dex}}] = \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{dex}^{-1}$. Avec cette notation, 
$$\int \dd \log_{10}(\nu)\ I_{\mathrm{dex}} = \int \dd \nu\ I_{\nu} = I$$
Comme $\log_{10}(x) = \ln(x)/\ln(10)$, on peut noter que $I_\mathrm{dex}$ diffère d'un facteur $\nu \ln 10$ de $I_{\nu}$
:::

Suivant à nouveau {cite}`1986rpa..book.....R`, la densité d'énergie d'un champ de particules avec une impulsion entre $p$ et 
$p + \dd p$ dépend du nombre de particules par volume de phase, $\dd \mathcal{N}/\dd^3 x \dd^3 p$ comme

$$
\varepsilon_\nu \dd \nu = h\nu  \frac{\dd \mathcal{N}}{\dd^3 x \dd^3 p} 4\pi p^2 \dd p
$$

$\dd \mathcal{N}/\dd^3 x \dd^3 p$ est invariant sous une transformation de Lorentz. En effet, $\dd \mathcal{N}$ est dénombrable 
et donc invariant. Sous un boost $(\beta, \gamma)$ le long de l'axe x du référentiel de 
l'observateur (K) vers le référentiel comobile (K'), on trouve $\dd x = \gamma^{-1} \dd x'$ (contraction des longueurs) 
et $\dd p_x = \gamma (\dd p_{x'} - \beta \dd E') = \gamma \dd p_{x}'$ pour des particules à énergie fixée (impulsion totale fixée entre $p$ et $p + \dd p$). Ainsi $\dd^3 x \dd^3 p$ est invariant, *quod erat demonstrandum*.
 
 
On trouve
$$
I_\nu \dd \nu = hc \times (\frac{h\nu}{c})^3 \times  \frac{\dd \mathcal{N}}{\dd^3 x \dd^3 p} \dd \nu
$$

de sorte que 

$$
I_\nu / \nu^3 \equiv \mathrm{invariant\ de\ Lorentz}
$$


### Le spectre multi-longueurs d'onde de l'univers


:::{figure}  ../../images/The_Fitted_MWL_EGAL_Background_2025.jpg
:name: fig:mm_spectrum
:align: center
:width: 100%

Le spectre extragalactique multi-longueurs d'onde. Adapté de cette [page](https://zenodo.org/records/7842239).
:::

L'émission à large bande de toutes les populations de galaxies (et des sources au sein de ces galaxies) est responsable du 
spectre de l'univers montré dans [](#fig:mm_spectrum). En particulier, les rayonnements électromagnétiques incluent le fond radio cosmique (CRB) provenant à la fois des galaxies actives et à formation stellaire, les fonds infrarouge et optique cosmiques (CIB et COB) provenant principalement de la nucléosynthèse et de l'émission de poussière dans les galaxies à formation stellaire, le fond X cosmique (CXB) provenant des 
galaxies actives et 
le fond gamma cosmique (CGB) provenant des galaxies actives avec jets. Les mesures différentielles de ces fonds cosmiques sont d'une valeur fondamentale : elles reflètent notre connaissance de la distribution de la lumière émise par la formation stellaire, l'accrétion et l'éjection intégrées depuis la formation des premières sources astrophysiques. Bien que ces 
émissions ne soient qu'une partie négligeable de l'inventaire énergétique cosmique, elles nous fournissent un test de cohérence cosmologique essentiel pour comprendre le contenu et l'évolution de l'univers post-recombinaison {cite:p}`2004ApJ...616..643F`. 

Les valeurs indiquées par le texte vertical dans [](#fig:mm_spectrum) correspondent à la densité d'énergie de chaque composante, c'est-à-dire
l'intégrale de l'intensité spécifique multipliée par $4\pi/c$. En particulier, on peut vérifier que la 
densité d'énergie attendue des processus de nucléosynthèse et d'accrétion calculée dans le chapitre précédent, c'est-à-dire
${\sim}\,(13+1.5) \times 10^3\,\mathrm{eV}\,\mathrm{m^{-3}}$, se retrouve presque dans son intégralité dans le COB et le CIB. La 
densité d'énergie des processus d'éjection autour des trous noirs supermassifs, attendue à
${\sim}\,3 \,\mathrm{eV}\,\mathrm{m^{-3}}$, se trouve dans le CGB.

Les mesures montrées dans [](#fig:mm_spectrum) quantifient également le degré d'obscurité du ciel nocturne une fois les 
avant-plans soustraits. C'est l'histoire de leur émission qui fournit la solution au paradoxe d'Olbers. 
L'intensité actuelle de ces fonds détermine l'obscurité (ou plutôt la grisaille) du ciel nocturne, une fois tous les 
avant-plans (Système solaire, Voie lactée) enlevés. Nous pouvons comprendre les fonds extragalactiques à toutes les 
longueurs d'onde électromagnétiques, la soi-disant lumière de fond extragalactique, en utilisant des modèles synthétiques de populations de galaxies.
Certaines inconnues dans la lumière de fond extragalactique, y compris des tensions entre les mesures, sont néanmoins encore 
le sujet de recherches actives {cite:p}`2025arXiv250917954B`.

L'émission de lumière est fondamentalement le résultat du chauffage, de l'accélération et de la désintégration de la matière. Nous explorerons dans la prochaine 
section les connaissances établies avec les photons, en particulier à travers les observations multi-longueurs d'onde des sources gamma. Nous explorerons également dans les leçons suivantes dans quelle mesure cette connaissance multi-longueurs d'onde nous permet 
de comprendre les fonds extragalactiques observés aujourd'hui avec d'autres messagers, en particulier le fond de neutrinos extragalactique (ENB) entre $30\,$TeV et $3\,$PeV et le fond de rayons cosmiques extragalactique (ECRB) entre 
$200\,$PeV et $200\,$EeV.



Émission électromagnétique des sources non thermiques
----------------------------------
### Astronomie multi-longueurs d'onde

Le développement de la radioastronomie autour de la Seconde Guerre mondiale a conduit à l'émergence de l'astronomie multi-longueurs d'onde comme 
un outil puissant pour comprendre la Voie lactée et les sources extragalactiques. Karl Jansky a d'abord utilisé cette approche pour 
les observations galactiques dans les années 1930, et à partir des années 1960, Martin Schmidt et d'autres l'ont employée pour étudier les 
premiers noyaux actifs de galaxies, connus à l'époque sous le nom de quasars. L'émergence ultérieure de 
l'astronomie X et gamma dans les années 1970 et 1990, respectivement, a conduit à notre compréhension actuelle des émetteurs non thermiques — 
des sources astrophysiques qui émettent des rayonnements au-delà du spectre optique et infrarouge.

[](#fig:MWL_SkyMap) fournit une vue multi-longueurs d'onde de l'ensemble du ciel en coordonnées galactiques. Dans ce système de coordonnées 
sphériques, le centre galactique est au milieu de la carte et le plan galactique 
sépare les hémisphères galactiques nord et sud. Notez que les cartes du ciel sont montrées en fonction de la 
longitude galactique décroissante, allant de $+180^\circ$ à gauche à $-180^\circ$ à droite. C'est l'opposé de la façon dont 
nous représentons la Terre (c'est-à-dire avec la longitude croissante de gauche à droite), car nous observons la sphère depuis 
l'intérieur quand nous regardons le ciel.

:::{figure}  ../../images/multiwavelength_sky.jpg
:name: fig:MWL_SkyMap
:align: center
:width: 50%

Vue multi-longueurs d'onde du ciel en coordonnées galactiques. De cette [page](https://imagine.gsfc.nasa.gov/science/toolbox/multiwavelength1.html).

:::

Une grande partie de l'émission radio montrée dans [](#fig:MWL_SkyMap) provient des électrons et positrons de haute énergie rayonnant 
dans le champ magnétique 
de la Voie lactée. Les ondes de choc dans les restes de supernovae produisent également des émissions radio intenses près de ces sources. 
La majeure partie de l'émission infrarouge provient d'étoiles relativement froides situées dans le disque et le bulbe de la Voie lactée. 
La poussière interstellaire est relativement transparente à ces longueurs d'onde. Aux longueurs d'onde visibles (entre 0.4 et 0.6 
microns), une forte absorption par les nuages de gaz et de poussière limite la profondeur des observations. En conséquence, la lumière visible le long du plan galactique provient principalement d'étoiles situées à quelques kiloparsecs du Soleil. L'image composite 
X est reconstruite à partir de bandes centrées à 0.25, 0.75 et 1.5 keV (rouge, vert et bleu, respectivement). Le 
gaz chaud et choqué dans la Voie lactée émet des rayons X de basse énergie (également appelés "rayons X mous"). Le milieu interstellaire 
absorbe fortement les rayons X mous, nous permettant de percevoir les nuages froids de gaz interstellaire comme des ombres contre le fond d'émission X. Les zones noires indiquent des lacunes dans le relevé. 

L'image gamma inclut tous les photons avec des énergies supérieures à 1 GeV. À ces hautes énergies, une grande partie de l'émission gamma 
le long du plan galactique provient d'interactions de rayons cosmiques avec les noyaux d'hydrogène et d'hélium dans 
le milieu interstellaire. Des sources brillantes et ponctuelles sont observées le long du plan galactique, telles que les pulsars Vela, 
Geminga et Crabe, qui sont situés à des longitudes d'environ $-95^\circ$, $-165^\circ$ et $-175^\circ$, 
respectivement. Des sources ponctuelles se trouvent également en dehors du plan galactique, principalement sous la forme de noyaux actifs de 
galaxies avec jets. Une introduction plus détaillée aux observations dans chaque bande, dont les deux 
paragraphes précédents sont adaptés, peut être trouvée sur cette [page](https://asd.gsfc.nasa.gov/archive/mwmw/mmw_images.html).


En zoomant sur un carré mesurant environ 0.1° centré sur les coordonnées galactiques de l = -175.44° et b = -5.78°, 
on révèle dans [](#fig:MWL_Crab) l'émission entourant le pulsar du Crabe. Cette émission étendue est connue sous le nom de Nébuleuse du Crabe. La Nébuleuse du Crabe est le résultat d'une supernova à effondrement de cœur qui a explosé en 1054 ap. J.-C. Le pulsar au 
cœur de la nébuleuse a une période d'environ 33 millisecondes. La rotation de l'étoile à neutrons alimente le rayonnement 
observé dans la nébuleuse du vent de pulsar.

:::{figure}  ../../images/Crab_Nebula_in_Multiple_Wavelengths_2.jpg
:name: fig:MWL_Crab
:align: center
:width: 80%

Vue multi-longueurs d'onde de la Nébuleuse du Crabe. De cette [page](https://commons.wikimedia.org/wiki/File:Crab_Nebula_in_Multiple_Wavelengths_2.png).

:::

Dans [](#fig:MWL_Crab), les observations radio dépeignent la nébuleuse du vent de pulsar en rouge et l'émission d'électrons libres en 
vert. La région bleu-blanc dans l'image infrarouge correspond aux électrons piégés dans le champ magnétique, 
tandis que les filaments rouges révèlent le reste des couches externes originales de l'étoile. Le réseau de filaments est 
clairement visible dans l'image optique, entourant le noyau bleuâtre de la nébuleuse du vent de pulsar. La Nébuleuse du Crabe s'étend 
légèrement plus loin dans l'ultraviolet que dans les rayons X. Cela est dû au fait que les électrons responsables de l'émission UV perdent 
leur énergie plus lentement que ceux émettant à des énergies plus élevées. L'image X révèle des structures impressionnantes qui 
tracent le champ magnétique entourant le pulsar, y compris un objet compact, deux tores concentriques et des jets de chaque 
côté. Une introduction plus détaillée à la Nébuleuse du Crabe peut être trouvée sur cette
[page](https://chandra.harvard.edu/graphics/resources/handouts/lithos/crab_litho.pdf) et cette
[page](https://imagine.gsfc.nasa.gov/science/toolbox/multiwavelength2.html).

La résolution angulaire des observatoires gamma est à peine suffisante pour résoudre la nébuleuse du vent de pulsar du Crabe, qui 
apparaît donc presque comme une source ponctuelle. Fait intéressant, une légère extension peut néanmoins être mesurée 
au-delà de l'étendue de la fonction de réponse ponctuelle, allant de 0.035° ± 0.003° au-dessus de 1 GeV à 0.014° ± 0.005° au-dessus de 10 
TeV {cite:p}`2024A&A...686A.308A`. La nébuleuse du vent de pulsar du Crabe présente donc une morphologie complexe qui dépend 
de l'énergie, traçant la structure du champ magnétique et l'injection de leptons dans l'environnement du pulsar.

### Sources non thermiques

#### Bestiaire de sources

Les photons détectés dans la gamme radio à PeV offrent un avantage significatif par rapport aux autres astroparticules, telles que 
les neutrinos et les rayons cosmiques chargés. Leurs sections efficaces d'interaction plus grandes les rendent plus faciles à détecter que les neutrinos.
De plus, comme les neutrinos, les photons se propagent le long de géodésiques (c'est-à-dire en ligne droite, en première approximation), 
alors que les rayons cosmiques chargés sont déviés par les champs magnétiques qu'ils traversent.

De tous les relevés gamma effectués à ce jour, le plus complet est celui obtenu par le satellite Fermi-LAT dans la 
gamme d'énergie GeV. Cette carte est montrée en coordonnées galactiques dans [](fig:lat_skymap).

:::{figure}  ../../images/Fermi_5_year_scaled.jpg
:name: fig:lat_skymap
:align: center
:width: 100%

Carte du ciel en coordonnées galactiques de l'excès de rayons gamma avec des énergies supérieures à $1\,$GeV provenant de 5 ans d'observations avec Fermi-LAT. De cette [page](https://svs.gsfc.nasa.gov/11342).
:::

La plupart des ${\sim}\,7000$ sources observées aux énergies GeV sont situées en dehors du plan galactique. Ce sont principalement 
des noyaux actifs de 
galaxies avec jets, les plus brillants étant les "blazars", dont l'axe d'émission est aligné avec la ligne de visée. 
D'autres noyaux actifs de galaxies avec jets avec un jet "désaligné" sont appelés radiogalaxies. Environ une douzaine 
de galaxies à flambée d'étoiles ont également été détectées dans l'univers extragalactique observé en rayons gamma. Ces galaxies 
présentent un taux de formation stellaire par unité de masse stellaire plus élevé que notre propre galaxie. Par rapport à la Voie lactée, 
les galaxies à flambée d'étoiles produisent 
plus d'étoiles massives à courte durée de vie qui terminent leur vie en supernovae. Plusieurs centaines de sursauts gamma ont également été 
détectés dans le ciel gamma extragalactique, principalement des sursauts gamma longs résultant des explosions d'étoiles massives 
jusqu'à un décalage vers le rouge de $z > 4$. 

Les émissions diffuses de notre galaxie peuvent être vues d'abord le long du plan galactique et deuxièmement comme des 
émissions plus faibles en forme de cacahuète de chaque côté du centre galactique : les bulles de Fermi. Ces bulles ont une morphologie similaire à celles 
observées en micro-ondes par les satellites WMAP et Planck et en rayons X par le satellite eROSITA. L'explication dominante pour les bulles de Fermi est l'accélération passée de rayons cosmiques dans les régions internes de la Voie lactée, 
suivie de la diffusion de ces particules chargées dans le champ magnétique galactique.

Enfin, notre galaxie est peuplée d'une myriade de sources de taille stellaire. Les coquilles creuses sont les restes de supernovae 
(dont il existe deux types : à effondrement de cœur et thermonucléaires, également connues sous le nom de SN1a). Les supernovae à effondrement de cœur peuvent 
laisser une étoile à neutrons hautement magnétisée dans leur cœur après leur explosion, qui est connue sous le nom de pulsar. Les vents 
de ces pulsars, connus sous le nom de nébuleuses de vent de pulsar, remplissent l'espace laissé par l'explosion de supernova et accélèrent 
les électrons et positrons, qui ré-émettent des rayons gamma. Dans des stades plus avancés de leur vie, la diffusion de 
particules autour du pulsar peut même conduire à une émission étendue sur plusieurs degrés, connue sous le nom de halos TeV. Notre 
galaxie contient également de nombreuses sources gamma provenant de systèmes binaires : novae, binaires X et 
même microquasars, qui sont les analogues à échelle stellaire des noyaux actifs de galaxies avec jets.

Les images statiques, telles que celles présentées dans [](#fig:MWL_SkyMap) et [](#fig:MWL_Crab), sont particulièrement utiles pour 
les sources astronomiques qui sont périodiques ou constantes à l'échelle de temps humaine. Pour de telles sources, les observations à 
différentes longueurs d'onde faites à différents moments peuvent être combinées a posteriori sans altérer l'image physique. 
Cependant, cela ne s'applique pas aux sources variables persistantes, telles qu'un noyau actif de galaxie avec jets, dont le 
flux varie de manière erratique sur des échelles de temps allant de décennies à minutes, ni aux sources transitoires, telles que les sursauts gamma et les novae, qui apparaissent et disparaissent en quelques secondes à quelques jours après les explosions. 

Heureusement, depuis le début des années 
2020, nous avons accès à un réseau d'observatoires multi-longueurs d'onde couvrant près de 22 ordres de grandeur en 
énergie, de quelques dizaines de MHz à des énergies de l'ordre du PeV, y compris certains avec des capacités spectroscopiques ou polarimétriques. Des campagnes d'observation simultanées sont programmées et 
les sursauts peuvent être suivis grâce à des alertes transmises dans le monde entier en quelques minutes. Ces alertes sont également émises par 
des installations multi-messagers, qui ont été cruciales depuis le milieu des années 2010, comme nous le discuterons dans la prochaine leçon.


#### Faisceau relativiste 

Les sources les plus variables connues à ce jour présentent souvent (ou sont supposées héberger) des jets de plasma.

L'existence de zones d'émission avec une vitesse globale (par rapport à l'objet compact central) approchant la vitesse 
de la lumière peut être illustrée par le mouvement apparent de régions de plasma (souvent appelées "blobs") dans ces 
jets astrophysiques. La vitesse apparente de ces blobs de plasma peut dépasser la vitesse de la lumière, un effet qui 
peut être expliqué par des arguments purement géométriques basés sur la physique classique, comme [](#exo:superluminal) l'illustre.

:::{exercise} Mouvement superluminique
:label: exo:superluminal

Le blob de plasma imagé en ondes radio, le plus à droite dans [](#fig:superluminal), semble parcourir une distance 
de ${\sim}\,30\,$ années-lumière sur une période de ${\sim}\,7\,$ ans.

1. Donnez une expression de la vitesse apparente en fonction de la vitesse physique du blob de plasma le long du jet dans le référentiel de l'observateur et de l'angle entre le jet et la ligne de visée.

2. Déduisez une contrainte sur le facteur de Lorentz du blob de plasma dans le référentiel de l'observateur.


:::{figure}  ../../images/3c279_320.jpg
:name: fig:superluminal
:align: center
:width: 60%

Émission radio du jet du noyau actif de galaxie 3C 279. De cette [page](http://user.astro.columbia.edu/~jules/UN2002/superluminal.html).

:::


:::{solution} exo:superluminal
:class: dropdown

1. Suivant les notations dans [la figure %s](#fig:superluminal_sol), la vitesse apparente, $v_\mathrm{app}$, du 
   blob de plasma est donnée par

$$
\begin{align}
v_\mathrm{app} &= \frac{L}{t_2-t_1} \\
			 &= \frac{L}{t_{i,2}-t_{i,1} - \frac{d_1-d_2}{c}} \\
 			 &= \frac{H\sin\theta}{H/v - H\cos\theta/c} \\
 			 &= \frac{v\sin\theta}{1 - \frac{v}{c}\cos\theta},
\end{align}
$$
où $v$ est la vitesse physique du blob de plasma le long du jet dans le référentiel de l'observateur.

2. En utilisant $\beta = \frac{v}{c}$ et $t = \tan(\theta/2)$, ainsi que la trigonométrie standard, on obtient :
$$
v_\mathrm{app} = \frac{2t\beta }{1+t^2 - (1-t^2)\beta}
$$
De sorte qu'après un peu d'algèbre, une vitesse apparente égale à une fraction $k$ de la vitesse de la lumière s'écrit
$$
v_\mathrm{app} = kc  \Leftrightarrow \Big[(1+\beta)t - \beta/k\Big]^2 = (\beta/k - 1/\Gamma) \times (\beta/k + 1/\Gamma),
$$
où $\Gamma = 1/\sqrt{1-\beta^2}$ est le facteur de Lorentz du blob de plasma.

Le membre de droite de l'équation a une solution si et seulement si $\beta/k - 1/\Gamma \geq 0$ c'est-à-dire $k \leq \Gamma\beta$. Comme 
$k = v_\mathrm{app}/c$ et $\beta < 1$, on obtient $\Gamma > v_\mathrm{app}/c$ c'est-à-dire un facteur de Lorentz supérieur à $4$ 
pour le jet du noyau actif de galaxie 3C 279.

:::{figure}  ../../images/superluminal_calc.jpg
:name: fig:superluminal_sol
:align: center
:width: 30%

Modélisation schématique du nœud radio.
:::

Le mouvement relativiste des blobs de plasma dans les sources astrophysiques avec jets résulte en une émission anisotrope. Le 
mouvement augmente également l'énergie des photons et l'intensité du rayonnement lorsque la région se déplace vers l'observateur. 
La dérivation standard de cet effet Doppler relativiste est basée sur les transformations de vitesse. Alternativement, nous 
utilisons ici une approche plus directe basée sur la transformation de l'énergie d'un photon émis. 

Supposons une émission isotrope d'énergie $E'$ dans le référentiel comobile avec la région émettrice, avec 
quadri-impulsion correspondante $[E' , p_x'c, p_y'c, p_z'c]$. L'observateur reçoit des photons d'énergie $E$ dans le référentiel du laboratoire le long de la direction $x$, donc la quadri-impulsion observée est $[E, p_xc = E, p_yc = 0, p_zc = 0]$. Nous pouvons passer d'un référentiel à l'autre via un boost de Lorentz $(\Gamma, \Gamma \vec{\beta})$ de la région émettrice et une rotation d'un 
angle $\theta$ par rapport à la direction du mouvement, c'est-à-dire

$$
 \begin{bmatrix} E' \\ p_x'c \\ p_y'c \\ p_z'c \end{bmatrix}
 =
  \begin{bmatrix}
   \Gamma & - \Gamma \beta & & \\
   - \Gamma \beta & \Gamma & & \\
    & & 1 & \\
    & &   & 1 \\
   \end{bmatrix}
 \begin{bmatrix}
   1 & & & \\
     & \cos \theta & -\sin \theta & \\
     & \sin \theta & \cos \theta &  \\
    & &   & 1 \\
   \end{bmatrix}   
   \begin{bmatrix} E \\ E \\ 0 \\ 0 \end{bmatrix}
$$

La première composante de type espace s'écrit $p_x'c = \Gamma E(\cos\theta-\beta)$. Les photons émis dans la direction avant 
$p_x'>0$ atteignent donc l'observateur dans un cône défini par $\cos\theta > \beta$. Dans la limite ultra-relativiste, 
cette inégalité s'écrit $1-\theta^2/2 > 1 - 1/(2\Gamma^2)$, ce qui définit un cône de demi-angle d'ouverture
$\theta < 1 /\Gamma$. Cela correspond à un demi-angle d'ouverture
$\theta_\mathrm{max} = \frac{1}{\Gamma} \approx 6^\circ \times \big( \frac{\Gamma}{10} \big)^{-1}$.

L'équation de la composante temporelle s'écrit $E' = \Gamma E (1-\beta\cos\theta)$. Ainsi, dans le référentiel de l'observateur, 
l'énergie est augmentée par un facteur Doppler $\delta = E / E'$ c'est-à-dire
$$
\delta = \frac{1}{\Gamma(1-\beta\cos\theta)}.
$$
Cette augmentation d'énergie $E=h\nu$ correspond à une augmentation de fréquence et donc à un raccourcissement des 
échelles de temps observées d'un facteur $\delta$. Dans la limite ultra-relativiste et pour un jet presque aligné avec la 
ligne de visée (source de type blazar), cela correspond à une amplification d'énergie ou à un raccourcissement de temps d'un facteur
$\delta \approx \frac{1}{\Gamma\big(1-[1-1/(2\Gamma^2)]\big)} \approx 2 \Gamma$ c'est-à-dire $\delta \approx 10 \times \big( \frac{\Gamma}{5} \big)$.

L'intensité spécifique de la source, c'est-à-dire sa brillance, est également amplifiée. Comme $I_\nu/\nu^3$ est un invariant de Lorentz, 
l'intensité spécifique est amplifiée d'un facteur $\delta^3$ et l'intensité bolométrique,
$I = \int_0^{+\infty} I_\nu \dd \nu$, est amplifiée d'un facteur $\delta^4 \approx 10,000 \times \big( \frac{\Gamma}{5} \big)^4$.


:::{exercise} Opacité des jets de GRB
:label: exo:grb_opacity

Deux coquilles sont émises par le moteur central avec un délai temporel $\Delta t_\mathrm{var}$ dans le référentiel de l'observateur. 
Pour simplifier, nous supposons que la première coquille se déplace à $v_1 = \beta c$ et la seconde à $v_2 = c$.

1. Donnez une expression de la distance $r$ depuis le moteur central (référentiel de l'observateur) à laquelle les coquilles entrent en collision en 
   fonction de $\Delta t_\mathrm{var}$ et du facteur de Lorentz de la première coquille.

Dans le référentiel se déplaçant à quatre-vitesse $(\Gamma, \Gamma\vec{\beta})$ vers l'observateur, la région d'émission est 
modélisée comme une région sphérique de luminosité $L'$ et de taille $\Delta r' = c \Delta t_\mathrm{var}'$ remplie (pour 
simplifier) d'un champ de photons monochromatique à $h\nu' = m_e c^2 \approx 511\,$keV.

Le mécanisme de production de paires résulte en une profondeur optique du milieu, $\tau$, pour les photons. Une profondeur optique est le 
produit d'une distance, d'une densité de cibles et d'une section efficace. 

2. Donnez une expression de la profondeur optique pour la production de paires en fonction de la luminosité observée $L$ et 
   de l'échelle de temps de variabilité $\Delta t_\mathrm{var}$, en supposant une section efficace $\sigma_{\gamma\gamma} \approx \sigma_T/5 \approx 0.1\,$barn.

La fraction de photons qui échappent aux interactions est $\exp(-\tau)$. Par conséquent, pour que les photons s'échappent, la profondeur optique 
ne devrait pas être trop grande ($\tau<1$, correspondant à un milieu "optiquement mince").

L'émission prompte d'un GRB court montre une luminosité observée $L = 10^{44}\,$W et une durée $\Delta t_\mathrm{var} = 10\,$ms.

3. Donnez une contrainte (expression et valeur numérique) sur le facteur de Lorentz de la première coquille et sur la distance 
   depuis le moteur central à laquelle le choc interne entre les deux coquilles se produit.

:::{figure}  ../../images/GRB_scenario_DESY.jpg
:name: fig:grb_desy
:align: center
:width: 80%

Vue schématique des chocs entre coquilles internes au jet d'un sursaut gamma. De cette [page](https://www.desy.de/news/news_search/index_eng.html?openDirectAnchor=760&two_columns=1&printversion=1). Exercice adapté de la leçon de F. Rieger à cette [page](https://www.mpi-hd.mpg.de/personalhomes/frieger/HEA4.pdf).

:::

:::{solution} exo:grb_opacity
:class: dropdown

1. Chaque coquille atteint un rayon $r_i = v_i(t-t_i)$, avec $i=1,2$ et $t_2-t_1 = \Delta t_\mathrm{var}$. Le choc interne 
   se produit à une distance $r=r_1=r_2$ et au temps $t = t_1 + r/v_1 = t_2 + r/v_2$. Alors, $\Delta t_\mathrm{var} = r\times(1/v_1 - 1/v_2)$, c'est-à-dire
\begin{align}
r &= \Delta t_\mathrm{var} \frac{v_1v_2}{v_2-v_1}\\
  &= c\Delta t_\mathrm{var}\frac{\beta}{1-\beta}\\
  &\approx 2\Gamma^2 c\Delta t_\mathrm{var} \mathrm{\ pour\ } \Gamma\gg 1.
\end{align} 

2. La profondeur optique est le produit d'une distance, d'une densité de cibles et d'une section efficace. Ce nombre pur qui 
   quantifie la probabilité d'interaction est un invariant de Lorentz. Nous pouvons calculer sa valeur dans le référentiel d'émission isotrope : $\tau_{\gamma\gamma} = \tau_{\gamma\gamma}' = n' \Delta r' \sigma_{\gamma\gamma}$, où la 
   distance est $\Delta r'= c \Delta t_\mathrm{var}'$ (argument de causalité) et où la densité de photons cibles est $n' = \frac{\varepsilon}{h\nu'} = \frac{1}{h\nu'} \frac{4\pi}{c}I' = \frac{1}{h\nu'} \frac{4\pi}{c} \frac{L'}{4\pi (\Delta r')^2}$. Cela donne une profondeur optique :
\begin{align}
\tau_{\gamma\gamma} &= \frac{L'\sigma_{\gamma\gamma}}{h\nu' c^2 \Delta t_\mathrm{var}'}\\
 										&= \frac{L\sigma_{\gamma\gamma}/c^2}{\delta^5 m_e c^2 \Delta t_\mathrm{var}}, \mathrm{\ où\ }\delta \approx 2\Gamma \mathrm{\ est\ le\ facteur\ Doppler}
\end{align}

3. La région est partiellement transparente aux photons pour $\tau_{\gamma\gamma} < 1$, c'est-à-dire pour
\begin{align}
\delta &> \Big( \frac{L\sigma_{\gamma\gamma}/c^2}{m_e c^2 \Delta t_\mathrm{var}} \Big)^\frac{1}{5}\\
&> \Big( \frac{10^{44}\times 0.1\times 10^{-28}/(3\times 10^8))^2}{0.5 \times 10^6 \times 1.6 \times 10^{-19} \times 10^{-2}} \Big)^\frac{1}{5}\\
&\gtrsim 400, 
\end{align}
ce qui correspond à $\Gamma \gtrsim 200$ dans la limite ultra-relativiste.

En injectant cette borne inférieure sur le facteur de Lorentz dans la solution de la question 1, on obtient $r \gtrsim 2 \times 10^{11}\,$m c'est-à-dire environ 1 U.A.

:::


:::{tip}
**Notions de ce chapitre**

_Sources galactiques et extragalactiques_
- Puis-je citer une classe de sources galactiques de rayons gamma ?
- Puis-je citer une classe de sources extragalactiques de rayons gamma ?
:::


:::{tip}
**Calculs / démonstrations**

_Intensité et densité d'énergie_
- Quelle est la relation entre ces deux quantités ?

_Facteur Doppler : $\delta = \frac{1}{\Gamma(1-\beta\cos\theta)}$_
- Que sont $\delta$, $\Gamma$, $\beta$ et $\theta$ ?
- Comment l'énergie d'un photon, le temps entre l'arrivée de deux photons et l'intensité (ou luminosité) d'un champ de photons sont-ils affectés par l'amplification Doppler ?

_Profondeur optique : $\tau = n \sigma r$_
- Que sont $\tau$, $n$, $\sigma$, $r$ et leurs unités ? 
- Que signifient $\tau \ll 1$ et $\tau \gg 1$ ? 

:::
