Les observables cosmologiques
=============================

Le modèle du Galiléon est-il en accord avec les données
cosmologiques actuelles? Avant d'exposer les résultats de cette
confrontation entre théorie et expérience, je vais décrire dans ce
chapitre les données cosmologiques que j'ai utilisées pour contraindre
les paramètres du modèle du Galiléon. Le calcul des observables
correspondantes dans le modèle sera détaillé au chapitre suivant. Le
point crucial pour choisir ces données a été de ne retenir que des
mesures indépendantes de la cosmologie, afin qu'elles soient aussi
vraies dans le contexte d'un modèle Galiléon que dans celui d'un modèle
$\Lambda$CDM.

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
sachant qu'elle n'a pas dû évoluer on peut en connaître sa distance.
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


Supernovæ de type Ia
--------------------

### Principe

Les supernovæ de type Ia (SNe Ia) sont les premières sondes
cosmologiques qui ont permis de mesurer l'expansion de l'Univers, et
découvrir son expansion accélérée {cite:p}`Riess1998; Perlmutter1999`. Le
principe de la mesure a été résumé en introduction de ce chapitre: s'il
existe un objet astrophysique de luminosité intrinsèque reproductible,
suffisamment brillant pour être visible sur des distances cosmologiques,
alors la mesure du flux lumineux reçu renseigne automatiquement sur sa
distance.

#### Les supernovæ

L'objet astrophysique en question est bien entendu la supernova de type
Ia. Tout d'abord, les supernovæ sont des événements extrêmement
brillants, dont la luminosité égale ou dépasse celle de la galaxie hôte
(voir photographie [](#fig:sn)). Ce sont donc des objets a priori visibles à des
distances cosmologiques, cependant ce sont aussi des événements
transitoires: la durée d'une supernova est de quelques dizaines de
jours. Pour la capter, il faut donc regarder le ciel au bon endroit au
bon moment.

```{figure} ../images/SN1994D.jpg
:name: fig:sn
:align: center
:width: 40%

La supernova SN 1994D (le point blanc brillant en bas à gauche de
l'image), dans la galaxie spirale NGC
4526.
```

Les supernovæ sont classées en deux types: gravitationnelles ou
thermonucléaires. Les premières sont les plus connues: elles
correspondent à l'explosion d'une étoile massive (plus de 8 fois la
masse du Soleil) en fin de vie, laissant un cœur stellaire dense et
froid: une étoile à neutrons, voire un trou noir dans les cas extrêmes.
Pour les secondes, les étoiles de masse inférieure à $8\,M_\odot$, leur
vie se termine en naine blanche, le cœur de l'étoile dont l'effondrement
est stoppé par la pression de dégénérescence des électrons (et non des
neutrons comme dans le premier cas). Le rayon typique d'un tel objet est
de 3 km.

D'après une étude du Very Large Telescope, environ 75% des étoiles
massives sont des systèmes binaires {cite:p}`Sana2012`. Dans certains cas, une
naine blanche peut donc être liée gravitationnellement à une autre
étoile qui, si elle est suffisamment proche, peut voir ses couches
externes aspirées par la gravité de la naine blanche. Lorsque cette
dernière accumule trop de matière venant de son voisin et approche la
masse de Chandrasekhar[^1] ($1.4\,M_\odot$), elle s'effondre à nouveau
ce qui provoque des réactions en chaîne qui conduisent à son explosion.
Cette explosion particulière correspond à une supernova de type Ia.
\"I\" car dans leur spectre aucune raie caractéristique de l'atome
d'hydrogène n'est visible[^2], et \"a\" car des raies du silicium ionisé
sont visibles (SiII). Ce scénario d'explosion ne reste toutefois qu'une
hypothèse dans la mesure où aucune preuve n'existe. D'autres scénarios
existent comme la fusion de deux naines blanches {cite:p}`Nomoto2013`. Des
exemples de spectres de supernovæ de différents types sont présentés
[](#fig:spectresIa).


```{figure} ../images/spectresIa.png
:name: fig:spectresIa
:align: center
:width: 70%

Échantillon de spectres de supernovæ au maximum de luminosité, en
échelle logarithmique et avec des décalages arbitraires. Les ions
formant les principales raies d'absorption sont indiqués, ainsi que les
bandes d'absorption atmosphérique (par $O_2$ et $H_2 O$, marquées
$\oplus$) apparentes [@Baumont2007]. On observe que les supernovæ de
type Ia représentées ont des spectres identiques, et différents des
spectres des autres supernovæ de type Ic, 1b ou IIp.
```


```{figure} ../images/SN2014J.jpg
:name: fig:SN2014J
:align: center
:width: 70%

Gauche: la détection de SN2014J est présentée en haut à gauche, ainsi
que l'image de référence de la galaxie M82 à sa droite. La soustraction
des deux images fait clairement apparaître la supernova. En dessous,
l'image optique du HST centrée sur la position de l'explosion avant
qu'elle n'intervienne. En bas, le spectre de SN2014J mesuré quelques
heures après sa détection, comparé à celui de SN2011fe en ligne grisée.
Droite: Évolution du spectre de SN2014J au cours du temps, comparé à
celui de SN2011fe en ligne
grisée.
```


```{figure} ../images/SN2014J_spectra.jpg
:name: fig:SN2014J_spectra
:align: center
:width: 70%

Gauche: la détection de SN2014J est présentée en haut à gauche, ainsi
que l'image de référence de la galaxie M82 à sa droite. La soustraction
des deux images fait clairement apparaître la supernova. En dessous,
l'image optique du HST centrée sur la position de l'explosion avant
qu'elle n'intervienne. En bas, le spectre de SN2014J mesuré quelques
heures après sa détection, comparé à celui de SN2011fe en ligne grisée.
Droite: Évolution du spectre de SN2014J au cours du temps, comparé à
celui de SN2011fe en ligne
grisée.
```

Un superbe exemple récent de SNIa est SN2014J, survenue dans une galaxie
très proche de nous (M82) et détectée très tôt {cite:p}`Goobar2014`. Sa
détection dans les images optiques et le suivi de son spectre au cours
du temps sont présentés
[](#fig:SN2014J). Cette supernova était si brillante qu'elle a
pu être observée avec des instruments d'astronomie amateur.

Les supernovæ sont donc des objets astrophysiques dont les spectres et
courbes de lumière sont très similaires. Ce sont des candidats idéaux à
utiliser comme chandelles standard.

La magnitude $m$ d'un objet est définie par:
$$
m = -2.5 \log_{10}\left( \frac{F}{F_{ref}} \right) = -2.5 \log_{10} \left[L\left(\frac{10}{d_L}\right)^2\right] + C,
$$
où $F$ est le flux lumineux mesuré de l'objet et $F_{ref}$ un flux de
référence. Plus un objet est lumineux, plus sa magnitude est petite. La
magnitude est exprimable en fonction de la luminosité intrinsèque de
l'objet $L$ et de sa distance de luminosité $d_L$ (exprimée en parsecs
et comparée par convention à une distance de 10 parsecs). Le flux de
référence repose sur celui d'une étoile étalon, par exemple l'étoile
Véga de la constellation de la Lyre ($\alpha$ Lyr) dont le flux a été
mesuré à 555.6 m à 3.52e-23 W/m\^2/Hz pour une magnitude de 0.048. Le
flux $F$ dépend de nombreux paramètres liés à l'instrument (transmission
des optiques, des filtres, intégration sur la bande passante), et à
l'environnement (présence de la Lune, halo galactique, environnement en
poussières proche de l'objet,\...). L'indice de couleur d'une étoile
désigne la différence de magnitudes mesurées dans deux bandes spectrales
différentes. Par exemple, l'indice $B-V$ est défini par:
$$
B-V\equiv m_{B}-m_{V}=2.5\log_{10} \left({\frac {L_{V} F_{B,ref}}{L_{B} F_{V,ref}}}\right) .
$$
Les bandes spectrales sont ici décrites dans le système UBVRI:

-   U (Ultraviolet):
    $\lambda_{\mathrm{eff}} = 360$ nm, $\Delta\lambda = 50$ nm;

-   B (Bleu):
    $\lambda_{\mathrm{eff}} = 430$ nm, $\Delta\lambda = 72$ nm;

-   V (Vert):
    $\lambda_{\mathrm{eff}} = 550$ nm, $\Delta\lambda = 86$ nm;

-   R (Rouge):
    $\lambda_{\mathrm{eff}} = 650$ nm, $\Delta\lambda = 133$ nm;

-   I (Infrarouge):
    $\lambda_{\mathrm{eff}} = 820$ nm, $\Delta\lambda = 140$ nm;

Dans une expérience donnée, les filtres disposés devant la caméra ont
cependant leurs propres bandes passantes (le relevé SNLS utilise par
exemple un système $u,g,r,i,z$). Pour obtenir un indice de couleur, il
faut donc connaître la réponse de l'instrument et des filtres, la
retirer, et la remplacer par la définition des bandes UBVRI. On peut
toutefois aussi définir des indices de couleur directement avec les
filtres utilisés.

#### Courbes de lumière

Une supernova de type Ia est un événement transitoire observable 60
jours en moyenne. Le flux lumineux en provenance de la supernova
enregistré au cours du temps est appelé courbe de lumière. Plusieurs
exemples de courbes de lumière issues de SNe Ia en bande $V$ sont
présentés [](#fig:courbes_de_lumiere). On remarque que les 29 SNe Ia
détectées par le relevé Calán/Tololo {cite:p}`Hamuy1996` ont des courbes de
lumière de forme identique, mais une dispersion intrinsèque existe sur
la magnitude au maximum, avec une déviation standard de $0.4\,$mag (pour
plus de détails sur les magnitudes et les couleurs, voir encadré). Les
SNe Ia ne seraient-elles pas si standard? Cette dispersion peut être
empiriquement corrigée. En effet, on observe que plus la courbe de
lumière dure dans le temps, plus elle est brillante à son maximum (règle
du *brighter-slower*). Outre la dispersion représentée, il en existe une
autre liée à la couleur $B-V$: les SNIa les plus bleues sont aussi les
plus brillantes (règle du *brighter-bluer*). Il y a aussi un effet
d'environnement qui lie la brillance de la supernova et les propriétés
de l'hôte.




```{figure} ../images/courbes_de_lumiere.png
:name: fig:courbes_de_lumiere
:align: center
:width: 60%

Dispersion des 29 courbes de lumière de SNe Ia proches observées en
bande $V$, issus du lot historique utilisé pour la première tentative de
standardisation [@Hamuy1996]. Il semble qu'il y ait une relation simple
entre le maximum de luminosité et la durée de la supernova. Après une
correction empirique de cet effet (voir
section [1.1.3](#sec:sn_mesures){reference-type="ref"
reference="sec:sn_mesures"}), la dispersion est beaucoup plus faible
(figure du bas).
```


Le flux de lumière est lié à la production et à la décroissance de
nickel $^{56}$Ni. Les deux relations présentées ci-dessus peuvent ainsi
être expliquées qualitativement: plus la SNIa produit de $^{56}$Ni, plus
elle sera brillante et contiendra d'émetteurs FeII/CoII (produits de la
désintégration de $^{56}$Ni, émettant dans le bleu), et plus elle sera
opaque (donc l'émission des photons par diffusion sera retardé, donc la
SNIa brillera plus longtemps) {cite:p}$`Kasen2007`.

Les SNe Ia ne sont donc pas si standard, car leur courbe de lumière
dépend de la quantité de $^{56}$Ni produit à l'origine. Néanmoins sans
corriger cette dispersion intrinsèque les équipes du Supernova Cosmology
Project (SCP) mené par Saul Perlmutter et du High-z Supernova Search
Team mené par Brian Schmidt ont pu démontrer l'existence d'une expansion
accélérée {cite:p}`Riess1998; Perlmutter1999`. Cette dispersion est gênante
pour améliorer les mesures d'expansion de l'Univers. Néanmoins, elle se
décrit qualitativement par les trois règles mentionnées plus haut, ce
qui permet de la corriger empiriquement par l'ajout de paramètres de
nuisance (voir section [1.1.3](#sec:sn_mesures)).

### Le Supernova Legacy Survey

#### Les instruments de mesure

Le but du SuperNova Legacy Survey (SNLS) est d'affiner la valeur mesurée
des paramètres cosmologiques en fournissant un catalogue étoffé de
SNe Ia mesurées le plus précisément possible.

Le relevé des SNe Ia a été effectué entre 2003 et 2008 par le télescope
Canada-France-Hawaï (CFHT) situé au sommet du volcan Mauna Kea à Hawaï,
où les conditions d'observation sont excellentes. Le télescope possède
un miroir de 3.60 m de diamètre, un des plus grands au monde avant
l'arrivée des télescopes géants (Keck I et II 10 m, VLT 8 m,\...).

Il est équipé à son foyer primaire de la caméra Megacam {cite:p}`Boulade2003`,
construite par le CEA/IRFU, la plus grande caméra CCD au monde en 2003
(340 millions de pixel). Le gigantisme de cette caméra a pour but de
photographier en une prise le plus grand champ possible
(0.96$\times$0.96 degrés carrés), et donc d'augmenter les chances de
capter une SNIa. La caméra est refroidie à $-120\celsius$ pour diminuer
le bruit électronique thermique. Elle est équipée de cinq filtres
$u,g,r,i,z$ ([](#fig:filtres)), très similaires à ceux utilisés par le Sloan
Digital Spectroscopic Survey (SDSS). Ce choix permet aujourd'hui de
mieux étalonner les flux lumineux reçus, car il existe une zone de
recouvrement entre les champs observés par le SDSS et ceux du CFHT.


```{figure} ../images/filters.pdf
:name: fig:filtres
:align: center
:width: 60%

Bandes passantes des filtres utilisés avec la caméra Megacam. La
mesure dite REOSC a été effectuée en 2002, tandis que les mesures au
CFHT ont eu lieu en 2006: ces dernières mesurent un élargissement des
bandes passantes de filtres $r$ et $i$. Cet élargissement a été confirmé
par une mesure récente (REOSC altered,
2008).
```


#### Stratégie d'observation

Le SNLS couvre quatre champs de 1 deg$^2$, répartis de sorte que deux
champs soient toujours observables simultanément tout au long de
l'année. Les prises de vue ont lieu sur une période de 15 à 18 jours
autour de la nouvelle lune afin de s'affranchir au maximum du bruit de
fond créé par la lumière lunaire. De 2003 à 2008, dans les périodes
d'observation le télescope pointe tous les 3 ou 4 jours le même champ,
de façon à détecter tôt l'apparition d'une SNIa et ensuite d'avoir un
bon échantillonnage temporel de sa courbe de lumière.

Détecter la SNIa dans la partie montante de sa courbe de lumière permet
ensuite aux télescopes partenaires de très grand diamètre d'en effectuer
le spectre près du maximum de luminosité (VLT, Gemini Nord, Magellan,
Keck I et II). Le spectre permet alors de confirmer s'il s'agit bien
d'une SNIa et de mesurer son décalage spectral avec une très grande
précision (de 1% à 0.1%). Le SNLS a bénéficié finalement de plus de
temps d'observation spectroscopique que photométrique.

La détection des SNe Ia est effectuée par soustraction à une image brute
d'une image de référence. L'image de référence est issue d'un alignement
et d'une moyenne par médiane[^3] d'une vingtaine d'images de haute
qualité (prises dans les meilleures conditions d'observations). Par
soustraction de l'image de référence, l'apparition d'un flux important
venant d'un objet ponctuel tel qu'une supernova est détectable (voir
[](#fig:snIa_raw)).

\centering
![Observation d'une supernova de type Ia dans les images brutes du SNLS
avant (gauche) et après (droite)
explosion.](../images/snIa_raw_before.png "fig:"){width="30%"}
![Observation d'une supernova de type Ia dans les images brutes du SNLS
avant (gauche) et après (droite)
explosion.](../images/snIa_raw_after.png "fig:"){width="29%"}

[\[fig:snIa\_raw\]]{#fig:snIa_raw label="fig:snIa_raw"}

(sec:mesures)=
### Mesures

#### Données

Pour chaque supernova détectée, un outil de caractérisation
photométrique (SALT2 {cite:t}`Guy2007`, ou SiFTO {cite:t}`Conley2008`) extrait des
informations sur les propriétés intrinsèques de la supernova à partir de
la courbe de lumière. L'outil est calibré sur un ensemble de centaines
de spectres et de courbes de lumières, qui modélise l'évolution du
spectre d'une SNIa au cours du temps. A partir de ce modèle et de la
donnée du redshift mesuré par spectroscopie (à $<1\%$ près), le logiciel
fournit pour chaque supernova:

-   sa magnitude *déredshiftée* (voir ci-après) au maximum de luminosité
    dans la bande $B$ {cite:p}`Astier2006; Hogg1999`, $m_B^*$;

-   sa date du maximum de luminosité, $t_B$;

-   sa couleur $c$ (qui représente la différence entre la couleur $B-V$
    et la couleur moyenne $\overline{B-V}$ des SNe Ia);

-   le facteur d'élargissement temporel ou *stretch* ($s$ pour SiFTO,
    $x_1$ pour SALT2 avec $x_1=10(s-1)$).

Les incertitudes et corrélations entre ces paramètres sont aussi
fournies.

Revenons sur ce que représente la magnitude *déredshiftée* $m_B^*$. Deux
effets se cumulent dans le spectre d'une supernova suite à son
éloignement. L'amplitude du spectre est diminuée par la distance et le
spectre est décalé en longueur d'onde (voir
[](#fig:snls_calib) par exemple). Pour être utilisable et tirer
partie du fait que les SNe Ia sont des chandelles standard, la magnitude
apparente $m_B$ doit être calculée en utilisant des portions identiques
des spectres des supernovæ. Or les spectres étant décalés par le
redshift, on retire cet effet. On définit alors une magnitude apparente
*déredshiftée* $m_B^*$ comme l'intégrale dans la bande $B$ du spectre
*déredshiftée*. Il ne subsiste alors que l'effet d'atténuation du
spectre. Une autre façon de voir les choses est de s'imaginer que la
bande passante du filtre $B$ est décalée vers le rouge comme si nous
observions le spectre de la supernova juste à côté d'elle, à \"$z=0$\",
en gardant toutefois la même amplitude de spectre. Les magnitudes
$m_B^*$, alors comparables entre supernovæ car elles viennent d'objets
standardisés, sont mesurées sur les mêmes parties des spectres, et seule
la distance les différencie par l'atténuation des flux reçus.

Le catalogue fourni par le SNLS regroupe des données venant de quatre
sources: SNLS, les supernovæ à bas redshift (Low-$z$), le Hubble Space
Telescope (HST) et le SDSS. Le catalogue de données SNLS 3 ans (SNLS3)
fournit 472 SNe Ia précisément identifiées et mesurées (dont 242 venant
du SNLS {cite:p}`Guy2010`), munies de leur redshift spectroscopique, de leurs
incertitudes systématiques et de leurs corrélations {cite:p}`Conley2011`. Ce
jeu de données sera dénommé SNLS3 dans la suite. Plus récemment, en
janvier 2014 SNLS et SDSS ont publié conjointement un nouveau catalogue
de 740 SNe Ia, dont les erreurs systématiques ont été réévaluées et
réduites par des calibrations croisées entre les deux expériences et une
révision de la transmission des filtres
([](#fig:filtres)). Ce jeu de données sera dénommé JLA par la
suite, pour Joint Light-curve Analysis. La publication des données
complètes du SNLS 5 ans est prévue pour 2015.


```{figure} ../images/lightcurve_white.png
:name: fig:lightcurve
:align: center
:width: 60%

Schéma d'une courbe de lumière d'une supernova dans la bande B
définissant les paramètres caractéristiques.
```

#### Diagrammes de Hubble et paramètres de nuisance {#sec:snls_hubble}

\centering
![Diagrammes de Hubble des supernovæ des catalogues SNLS3 (à gauche,
paramétrisation SiFTO) et JLA (à droite, paramétrisation SALT2). Pour
les données JLA, une échelle logarithmique est utilisée en $z$ pour
montrer l'abondance des mesures rajoutées par le SDSS. La courbe noire
représente un modèle $\Lambda$CDM ajusté aux données. Un modèle sans
énergie noire apparaîtrait significativement en dessous de la courbe
décrite par les données ($-0.6\,$mag à
$z=1$).[]{label="fig:HD"}](../images/HD_snls3.jpg "fig:"){width="49%"}
![Diagrammes de Hubble des supernovæ des catalogues SNLS3 (à gauche,
paramétrisation SiFTO) et JLA (à droite, paramétrisation SALT2). Pour
les données JLA, une échelle logarithmique est utilisée en $z$ pour
montrer l'abondance des mesures rajoutées par le SDSS. La courbe noire
représente un modèle $\Lambda$CDM ajusté aux données. Un modèle sans
énergie noire apparaîtrait significativement en dessous de la courbe
décrite par les données ($-0.6\,$mag à
$z=1$).[]{label="fig:HD"}](../images/HD_jla.pdf "fig:"){width="49%"}

Le diagramme de Hubble rapporte la magnitude apparente de la supernova
en fonction de son redshift. Dans un modèle cosmologique donné, la
magnitude $m_B^*$ est reliée à la distance de luminosité par:
$$\fbox{$\displaystyle m_B^*(z)=-2.5 \log_{10} \left[ L \left(\frac{10 \text{pc}}{d_L}\right)^2 \right] + C = 5 \log_{10}\frac{d_L(z)}{10\text{pc}} + M_B$}$$
avec $M_B$ la magnitude absolue de la supernova et $d_L$ la distance de
luminosité définie
section [\[sec:distances\]](#sec:distances){reference-type="ref"
reference="sec:distances"}. Pour un univers en expansion à vitesse
constante, on aurait $H(z)=H_0$ et: $$\label{eq:vitesse-constante}
m_B^*(z)= 5 \log_{10} \frac{cz(1+z)}{H_0} + M_B$$ Or il se trouve que
les mesures $m_{B,mes}^*$ sont en moyenne plus grandes que ne le prévoit
l'équation [](#eq:vitesse-constante) (donc les luminosités des SNe Ia
apparaissent plus faibles). Cela revient à dire que les supernovæ sont
plus lointaines que prévu, par conséquent l'expansion de l'Univers ne
s'effectue pas à vitesse constante (loi de Hubble) mais s'accélère.

A priori, $m_B^*(z)$ ne dépend que de la distance de la supernova car
toutes les supernovæ sont censées être identiques. Or, nous avons vu
qu'une dispersion intrinsèque existe parmi les SNe Ia, qu'il convient de
corriger. On définit le module de distance $\mu_B$ en corrigeant la
magnitude mesurée $m_{B,mes}^*$ par une modélisation empirique des deux
règles *brighter-slower* et *brighter-bluer*:
$$
\fbox{$\displaystyle \mu_B = m_{B,mes}^* - (M_B - \alpha (s-1) + \beta c)$}
$$
où $\alpha$, $\beta$ et $M_B$ sont des paramètres de nuisance supposés
communs à toutes les SNIa. La quantité $M_B$ est la magnitude absolue
des supernova, à laquelle on apporte une correction supplémentaire en
fonction de la masse de la galaxie hôte $m_{\text{hôte}}$:
$$M_B = \begin{cases}
    M_1 &\text{si } m_{\text{hôte}}<10^{10}\ M_{\odot} \\
    M_2 &\text{si } m_{\text{hôte}}>10^{10}\ M_{\odot}
  \end{cases}.$$ 
En effet, il semble que les galaxies massives
contiennent beaucoup plus de métaux et que les supernovæ peuvent y
apparaissent plus brillantes que dans les galaxies légères (voir la
discussion section 5.5 de la référence {cite:p}`Sullivan2010`). Comme suggéré
par la référence {cite:p}`Sullivan2010`, on divise les données en deux lots
selon la masse de la galaxie hôte. Au final, le tracé des mesures de
$\mu_B$ pour toutes les SNe Ia détectées en fonction de leur redshift
constitue un diagramme de Hubble corrigé des effets mentionnés plus haut
(voir [](#fig:HD)).

#### Étalonnages

\centering
![Stratégies pour étalonner la mesure du flux lumineux des étoiles
tertiaires (les étoiles secondaires ne sont pas représentées). A gauche:
la stratégie standard utilisant Véga. A droite, d'autres stratégies
utilisant l'étoile BD+174708 observée par le HST et des étoiles du
catalogue CALSPEC P041C et P177D. La bande $B$ redshiftée est
représentée en bleu sur les spectres des SNe Ia. L'utilisation de naines
blanches présentes dans les champs du SNLS serait aussi possible dans
les expériences futures
[@Lidman2012].](../images/strategy1.png "fig:"){width="49%"}
![Stratégies pour étalonner la mesure du flux lumineux des étoiles
tertiaires (les étoiles secondaires ne sont pas représentées). A gauche:
la stratégie standard utilisant Véga. A droite, d'autres stratégies
utilisant l'étoile BD+174708 observée par le HST et des étoiles du
catalogue CALSPEC P041C et P177D. La bande $B$ redshiftée est
représentée en bleu sur les spectres des SNe Ia. L'utilisation de naines
blanches présentes dans les champs du SNLS serait aussi possible dans
les expériences futures
[@Lidman2012].](../images/strategy2.png "fig:"){width="49%"}

[\[fig:snls\_calib\]]{#fig:snls_calib label="fig:snls_calib"}

Pour mesurer le flux reçu d'une supernova, il faut le comparer à une
étoile de référence. L'étoile Véga a été utilisée au début de la
collaboration SNLS bien que celle-ci ne soit pas présente dans les
champs observés par le SNLS: l'étalonnage des flux reçus est donc
dépendant de données extérieures, obtenues avec un instrument différent.
Ce système d'étalonnage est pourtant celui utilisé faute de mieux au
début par le SNLS. Des étoiles de référence du catalogue dit de Landolt,
étalonnées sur le flux de l'étoile Véga, sont observées par le SNLS dans
des champs d'observation d'étalonnage (différents des champs où sont
recherchés les supernovæ). La photométrie est alors étalonnée sur ces
références (étoiles dites secondaires, l'étoile Véga étant l'étoile
primaire) et propagée aux étoiles présentes dans les champs de science
(étoiles tertiaires). Le flux des supernovæ est alors connue par
comparaison avec le flux reçu par les étoiles tertiaires présentes dans
le champ observé.

Pour réduire les erreurs systématiques liées à l'étalonnage, l'idéal est
donc de bénéficier d'étoiles primaires mesurées plus précisément et plus
adaptées à nos besoins. En 2008, le catalogue d'étoiles de référence
CALSPEC {cite:p}`Bohlin2008` fourni par le HST a été étendu à des étoiles
rouges et faibles, plus fiables que l'étoile Véga (l'une est de couleur
plus proche de celle des étoiles secondaires utilisées par SNLS, trois
autres sont observables directement par SNLS). L'étalonnage sur ces
étoiles primaires permet d'établir plus précisément les magnitudes des
étoiles tertiaires et la cas échéant de la supernova. De plus, plusieurs
champs d'observation du SDSS se recoupent avec ceux du SNLS, ce qui
permet aussi un étalonnage croisé entre les étoiles tertiaires des deux
expériences. Ce sont donc trois méthodes qui sont disponibles pour
étalonner la photométrie de SNLS et SDSS. La combinaison de ces méthodes
a permis de réduire les incertitudes systématiques liées à la
calibration dans le catalogue JLA {cite:p}`Betoule2013`.

#### Incertitudes systématiques

Le SNLS a été le premier relevé de supernovæ à identifier et à prendre
en compte les erreurs systématiques liées à la mesure des supernovæ,
corrélations comprises. Aujourd'hui, pour les supernovæ l'erreur
statistique sur les paramètres cosmologiques est du même ordre de
grandeur que la contribution des incertitudes systématiques (cf
{cite:t}`Guy2010`). Ces dernières ne sont donc pas à négliger et doivent être
traitées correctement.

Comme $s$ et $c$ sont liés à $\alpha$ et $\beta$, l'incertitude
statistique $\sigma_{SN}$ sur le module de distance est une fonction de
$\alpha$ et $\beta$:
$$\sigma_{SN}(\alpha,\beta)=\sigma_{m_B^*}^2 + \alpha^2 \sigma_s^2 + \beta^2 \sigma_c^2 + \sigma_{\text{hôte}}^2 + \left(\frac{5(1+z)}{z(1+z/2)\ln 10}\right)\sigma_z^2 + \sigma_{int}^2 = \bold{D}_{stat,ii}$$

-   $\sigma_{m_B^*}$: erreur sur $m_B^*$ (erreur diagonale seulement);

-   $\sigma_s$: erreur sur s;

-   $\sigma_c$: erreur sur c;

-   $\sigma_{\text{hôte}}$: erreur sur la masse de l'hôte;

-   $\sigma_z$: erreur sur z;

-   $\sigma_{int}$: terme d'erreur rajouté pour avoir au final
    $\chi^2_{min} = 1$ par degré de liberté (obsolète dans le catalogue
    JLA);

-   $\bold{D}_{stat,ii}$: matrice diagonale des erreurs statistiques.

Les erreurs statistiques, systématiques et leurs corrélations sont
regroupées dans la matrice de covariance : $$\label{eq:snls_cov}
 \bold{C}(\alpha,\beta) = \bold{D}_{stat} + \bold{C}_{stat}(\alpha,\beta) + \bold{C}_{syst}$$
La matrice $\bold{C}_{stat}(\alpha,\beta)$ regroupe les corrélations
entre les incertitudes statistiques des supernova. La matrice
$\bold{C}_{syst}$ regroupe les incertitudes systématiques liées
{cite:p}`Conley2011`:

-   à l'étalonnage des flux;

-   à l'utilisation des outils de caractérisation photométrique SALT2
    et/ou SiFTO;

-   aux vitesses particulières des objets (importants à bas $z$),

-   au biais de Malmquist (seuls les objets les plus brillants sont
    visibles aux redshifts lointains, ce qui biaise le catalogue);

-   à la contamination possible du catalogue par des supernovæ de type
    non Ia;

-   à la modélisation de la magnitude en fonction de la masse de l'hôte;

-   au modèle d'absorption du flux lumineux par les poussières proches
    du plan galactique;

-   à l'évolution possible de $\beta$ en fonction du redshift.

L'incertitude liée à l'étalonnage photométrique est de loin
l'incertitude dominante (79% de l'incertitude mesurée sur $w$ dans un
modèle FWCDM d'après la référence {cite:t}`Conley2011` Table 7). Ces
incertitudes systématiques, nombreuses, ont été précisément étudiées et
doivent être prises en compte lors d'une utilisation rigoureuse des
SNe Ia pour dériver des contraintes expérimentales sur des paramètres
cosmologiques.

(sec:cmb)=
Fond diffus cosmologique
------------------------

Le fond diffus cosmologique (CMB dans la suite) fournit des mesures
précises de l'état de l'Univers ans seulement après le Big Bang
($z\approx 1090$), ce qui permet de disposer d'un jalon précis dans le
passé de l'Univers pour contraindre son histoire. Un modèle cosmologique
doit donc à la fois être en accord avec des mesures relativement proches
en redshift ($z\lesssim 1$) et avec celles du CMB, ce qui encadre
fortement son évolution. Cette sonde fournit un jalon très contraignant
pour le modèle Galiléon comme nous allons le voir au
chapitre [](#chap:contraintes_galileon).

### Le spectre de puissance angulaire du CMB

#### Propagation des fluctuations de densité dans le plasma primordial

Au commencement (i.e. juste après la phase d'inflation), l'Univers est
un plasma de particules extrêmement chaud, qui se refroidit sous l'effet
de son expansion (voir l'encadré sur la thermodynamique d'un Univers en
expansion). Cependant, il n'est pas complètement homogène: il contient
de petites fluctuations de densité, de vitesse, etc\... dites
primordiales (les modèles d'inflation les décrivent comme provenant des
fluctuations quantiques pré-inflation). Ces fluctuations primordiales
grandissent au cours du temps en agglomérant de la matière par
gravitation. Elles sont les germes des futures grandes structures de
l'Univers (galaxies, amas de galaxies).

Par des considérations thermodynamiques liées à la conservation de
l'énergie, on peut montrer que l'évolution de l'Univers s'effectue à
entropie $S$ constante: $dS=0$. Si on s'intéresse à un cube d'Univers de
côté $a$, alors si $s$ est la densité d'entropie volumique on a
$S= \frac{\rho + p}{T} a^3 = s a^3 = \text{constante}$.

Dans l'Univers primordial, la matière relativiste domine donc
globalement on a $p=\rho/3$ et $\rho \propto T^4$. On en déduit
$s\propto T^3$ donc $T \propto a^{-1}$: un Univers en expansion se
refroidit.

Les fluctuations peuvent être décrites mathématiquement par des
perturbations des équations régissant le plasma. Les perturbations
possibles peuvent être scalaires, vectorielles ou tensorielles.
Concentrons-nous ici sur les perturbations scalaires, qui sont à
l'origine du spectre de puissance angulaire du CMB et des oscillations
acoustiques de baryons. On considère des fluctuations de densité
d'énergie adiabatiques [^4]:
$$\delta(x^\mu) = \frac{\delta \rho(x^\mu)}{\bar \rho(x^\mu)}=\frac{\rho(x^\mu) - \bar \rho(x^\mu)}{\bar \rho(x^\mu)}.$$

Avant la recombinaison, l'Univers est constitué d'un plasma de baryons,
d'électrons, de photons, de neutrinos et de matière noire. Dans ce
milieu, les fluctuations de densité du plasma ne peuvent croître sans
fin sous l'effet de la gravitation car la forte pression de radiation
des photons s'y oppose. Du combat entre ces deux forces naît une onde de
propagation acoustique dans le plasma, se propageant à une vitesse $c_s$
(vitesse du son dans le plasma). En revanche, les fluctuations de
densité de la matière noire, non couplée aux photons, ne subissent pas
cette pression de radiation et donc croissent sans osciller.

A quelle vitesse se propagent les ondes acoustiques dans le plasma de
baryons? En thermodynamique, la vitesse du son dans un fluide parfait
est déterminée par: $$c_s^2 = \frac{d p_p}{d \rho_p},$$ où l'indice $p$
désigne le plasma. Or la densité $\rho_p$ et la pression $p_p$
s'écrivent:
$$\rho_p = \rho_\gamma + \rho_b,\qquad p_p = p_\gamma + p_b.$$ De plus,
on a vu que $p_\gamma/\rho_\gamma=1/3$ et $p_b$=0, donc on obtient:
$$c_s^2 =  \frac{d p_\gamma}{d \rho_p} = \frac{1}{3\left(1+\frac{d\rho_b}{d\rho_\gamma}\right)}.$$
Avec les équations de conservation de l'énergie pour la
matière [](#eq:conservation_energie_matiere) et le
rayonnement [](#eq:conservation_energie_radiation) que l'on rappelle:
$$\frac{d \rho_b}{dt} = -3 H \rho_b,\qquad \frac{d \rho_\gamma}{dt} = -4 H \rho_\gamma,$$
on obtient:
$$c_s^2 = \frac{1}{3\left(1+\frac{3\rho_b}{4\rho_\gamma}\right)}.$$ De
plus, avec ces mêmes équations de conservation de l'énergie on a
$\rho_b / \rho_c = \Omega_b^0 a^{-3}$ et
$\rho_\gamma / \rho_c = \Omega_\gamma^0 a^{-4}$ donc en terme de
paramètre de densité on obtient finalement:
$$c_s = \frac{1}{\sqrt{3}}\frac{1}{\sqrt{1+a\frac{3\Omega_b^0}{4\Omega_\gamma^0}}}.$$
On voit donc que $c_s$ dépend de l'expansion de l'Univers à travers $a$,
et des paramètres de densité $\Omega_b^0$ et $\Omega_\gamma^0$, mais
vaut en première approximation[^5] $c/\sqrt{3}$ (voir
[](#fig:cs2_classic)). La vitesse de propagation est donc relativiste.


```{figure} ../images/cs2_classic.pdf
:name: fig:cs2_classic
:align: center
:width: 60%

Évolution de la vitesse du son $c_s^2(z)$ dans le plasma primordial,
de $z=1100$ à $z=10^6$ (moins d'un an après le Big Bang). La vitesse
tend vers $c/\sqrt{3}$ aux premiers instants de l'Univers.
```


Durant ans, les fluctuations de densité oscillent et des ondes de
densité se propagent à des vitesses relativistes dans le milieu. Mais à
la recombinaison, les photons se découplent du plasma, figeant ainsi
soudainement les fluctuations de densité. Observer les photons du CMB
permet d'obtenir une photographie de la répartition et de la taille de
ces fluctuations de densité à la recombinaison (carte de la
collaboration Planck {cite:p}`PlanckCollaboration2013XVI` représentée
[](#fig:cmb_planck)).

Le décalage spectral marquant le découplage des photons, noté $z_*$, est
défini comme le moment où les photons ne subiront en moyenne qu'une
seule interaction jusqu'à notre époque {cite:p}`Hu1996`. A $z=z_*$ les
fluctuations sur le spectre en photon sont figées. Cet instant est
appelé découplage. Ceci ne correspond pas à l'arrêt des fluctuations des
baryons, qui a lieu à $z=z_d$, moment où les baryons ne subissent en
moyenne qu'une seule interaction Compton avec les photons jusqu'à notre
époque[^6] {cite:p}`Hu1996; Eisenstein1998`. La collaboration Planck a
contraint $z_* = 1090.43\pm0.54$ et $z_d=1059.25\pm0.58$ dans le cadre
d'un modèle $\Lambda$CDM {cite:p}`PlanckCollaboration2013XVI`. La physique très
fine et très riche qui décrit les oscillations dans le plasma primordial
est abondamment décrite dans {cite:t}`Hu1996; Eisenstein1998`. Les
oscillations peuvent être décrites très précisément et beaucoup
d'observables construites.

(sec:angular_power_spectrum)=
#### Construction du spectre de puissance angulaire

Le fond diffus cosmologique est un rayonnement de corps noir
quasi-parfait de température $T_{\mathrm{CMB}}$
([](#fig:cmb_cn)). L'intensité $I(\nu,T_{\mathrm{CMB}})$ du
rayonnement reçu à une fréquence $\nu$ suit donc la loi de Planck:
$$
I(\nu,T_{\mathrm{CMB}}) = \frac{2 h \nu^3}{c^2}\frac{1}{e^{h\nu/k_B T_{\mathrm{CMB}}}-1}
$$
avec $k_B$ la constante de Boltzmann. La carte de rayonnement contient
toutefois de petits écarts à la loi de Planck, de l'ordre de
$\Delta T_{\mathrm{CMB}} / T_{\mathrm{CMB}} \approx 10^{-5}$, dus à la
présence des fluctuations dans le plasma primordial. La température
$T_{\mathrm{CMB}}$ mesurée en un point du ciel est reliée à la
température $T_p$ du plasma par la conjugaison de trois effets
physiques:

-   un changement intrinsèque de température dû aux fluctuations de
    densité (une compression entraîne un réchauffement),

-   un décalage Doppler qui modifie la fréquence des photons $\nu$ et
    donc $T_{\mathrm{CMB}}$ induit par une perturbation de vitesse sur
    la surface de dernière diffusion,

-   un décalage gravitationnel si la fluctuation n'est pas au même
    potentiel que l'observateur (effet Sachs-Wolfe) ou si la lumière
    traverse des potentiels variables au cours du temps (effet
    Sachs-Wolfe intégré ou ISW).

Ces trois mécanismes sont achromatiques (ne dépendent pas de la
fréquence) et donc ne modifient pas le spectre de corps noir. Les
fluctuations observées sur la carte de température du CMB traduisent
donc directement les fluctuations de densité de matière au moment du
découplage. Le processus dominant est l'effet Sachs-Wolfe {cite:p}`Sachs1967`:
les points froids sur la carte de température proviennent donc des
sur-densités du plasma (donc de température plus chaudes que la moyenne)
car les photons ont en moyenne perdu de l'énergie pour échapper au puits
gravitationnel formé par la sur-densité.

Pour étudier les fluctuations de densité, il est possible de décomposer
la carte de température $T(\theta,\phi)$ en harmoniques sphériques[^7]:
$$\label{eq:cmb_angular}
\frac{\Delta T(\theta,\phi)}{ T_{\mathrm{CMB}}} =\frac{T(\theta,\phi)-T_{\mathrm{CMB}}}{ T_{\mathrm{CMB}}}= \sum_{l=0}^\infty \sum_{m=-l}^l a_{lm} Y_{lm}(\theta,\phi),$$
où $(\theta,\phi)$ correspondent aux coordonnées galactiques sur le
ciel, et $a_{lm}$ donne la puissance associée à l'harmonique sphérique
$Y_{lm}$:
$$a_{lm} = \int_{4\pi} \frac{\Delta T(\theta,\phi)}{ T_{\mathrm{CMB}}} Y_{lm}^*(\theta,\phi) d\Omega$$
Une illustration de cette décomposition en harmoniques sphériques est
donnée [](#fig:cmb_sphere). Le coefficient $a_{lm}$ quantifie
l'intensité en température aux échelles angulaires
$\Delta \theta \equiv \pi / l$. Par exemple, l'harmonique $Y_{00}$ est
une constante correspondant à la température moyenne du CMB mesurée à
$T_{\mathrm{CMB}} = \SI{2.7255}{\kelvin}$ {cite:p}`Fixsen2009`, d'où
$a_{00} = 0$. Le paramètre $a_{10}$ donne la température du dipôle
($l=1$) engendré par la vitesse de déplacement du système solaire par
rapport au CMB. Il est de l'ordre de $10^{-3}$. On ne peut séparer ce
dernier du dipôle cosmologique véritable engendré par les fluctuations
de températures aux très larges échelles, c'est pourquoi on ne
s'intéressera finalement qu'aux indices $l\geq 2$ par la suite, d'ordre
encore plus faibles ($<10^{-5}$).

```{figure} ../images/cmb_sphere.png
:name: fig:cmb_sphere
:align: center
:width: 100%

Décomposition de la carte de température du CMB à des harmoniques
sphériques caractéristiques ($l=2,18,220,440$). Une zone de
$\SI{2}{\degree}\times\SI{2}{\degree}$ est agrandie en haut à droite, et
la position $l$ dans le spectre de puissance angulaire est donné en haut
à gauche. *Source:
<http://www.apc.univ-paris7.fr/blog/content/le-fond-diffus-cosmologique-cmb>*.
```

Toute l'information concernant les anisotropies du CMB étant contenue
dans les coefficients $a_{lm}$ (voir
équation [](#eq:cmb_angular)), une mesure du fond diffus cosmologique
consiste à déterminer ces derniers. Si les fluctuations de température
$\Delta T$ du CMB suivent une distribution gaussienne de moyenne nulle,
alors chaque coefficient $a_{lm}$ est une variable aléatoire gaussienne
de moyenne statistique nulle[^8]: 
$$\overline{a_{lm}} = 0.$$ 
La quantité intéressante à rechercher est donc une estimation de la variance
$\overline{ \vert a_{lm} \vert^2 }$ pour avoir une prédiction de la
taille typique des coefficients $a_{lm}$. La nature isotrope de
l'Univers impose que cette moyenne ne dépendent que de l'indice[^9] $l$
et non de $m$. On définit le spectre de puissance angulaire du CMB par
une fonction $C_l$ dépendante de l'indice $l$ uniquement:
$$\overline{a_{lm}a_{l'm'}^* } = \delta_{ll'} \delta_{mm'} C_l.$$ Le
spectre de puissance angulaire $C_l$ du CMB est relié à la contribution
du multipôle $l$ à la variance statistique des fluctuations de
température[^10]:
$$
\overline{\left( \frac{\Delta T}{T_{\mathrm{CMB}}} \right)^2 } = \sum_{ll'\geq 2} \sum_{mm'} Y_{lm}(\theta,\phi) Y_{l'm'}^*(\theta,\phi) \overline{ a_{lm}a_{l'm'}^*} =  \frac{1}{4\pi} \sum_{l=2}^\infty (2l+1) C_l.
$$
Toutefois, la moyenne statistique est réalisée ici sur un ensemble de
réalisations de la variable $a_{lm}$, liées au processus aléatoire
engendrant les perturbations primordiales. Pour pouvoir réaliser une
telle moyenne d'ensemble, il faudrait donc pouvoir disposer de plusieurs
réalisations d'univers[^11]. Cela étant impossible, nous ne pouvons
observer qu'un exemplaire de cette variable $a_{lm}$, celui engendré par
les conditions initiales de notre propre Univers. A défaut, on définit
alors le spectre de puissance angulaire observé $\hat{C}_l$ par:
$$
\hat{C}_l = \frac{1}{2l+1}\sum_{m=-l}^l \vert a_{lm}^2 \vert,
$$ qui
est lui relié à la variance sur la sphère céleste des anisotropies de
températures observées[^12]: 
$$\begin{aligned}
\left\langle \left( \frac{\Delta T}{T_{\mathrm{CMB}}} \right)^2 \right\rangle &= \frac{1}{4\pi}\int\left( \frac{\Delta T}{T_{\mathrm{CMB}}} \right)^2  d\Omega  \notag \\
&= \frac{1}{4\pi}\sum_{ll'\geq 2} \sum_{mm'}  a_{lm}a_{l'm'}^* \int  Y_{lm}(\theta,\phi)Y_{l'm'}^*(\theta,\phi) d\Omega\notag \\
 &=   \frac{1}{4\pi} \sum_{l=2}^\infty \sum_{m=-l}^l \vert a_{ml}\vert^2 =   \frac{1}{4\pi} \sum_{l=2}^\infty (2l+1)\hat{C}_l.\end{aligned}$$
On peut approximer la somme par l'intégrale {cite:p}`Gangui2001`:
$$\left\langle  \left( \frac{\Delta T}{T_{\mathrm{CMB}}}\right)^2 \right\rangle  \approx \frac{1}{4\pi} \int_{2}^\infty l (2l +1 ) \hat{C}_l \frac{dl}{l} = \frac{1}{4\pi} \int_{2}^\infty  l (2l +1 ) \hat{C}_l d\ln l,$$
donc la fonction $\Delta_T^2(l)=(2l+1)\hat{C}_l / 4\pi$ représente
directement la distribution de puissance des fluctuations de température
par unité de $\ln l$. Il est cependant usuel de représenter ce spectre
de puissance angulaire par la quantité
$\Delta_T^2(l)=l(l + 1)\hat{C}_l /2\pi$, qui pour des grandes valeurs de
$l$ rejoint la proposition précédente, mais pour des petites valeurs de
$l$ a la remarquable propriété d'être en première approximation
constante (plateau de Sachs-Wolfe, voir
[](#fig:power_spectrum)).

La valeur attendue pour un grand nombre de réalisations d'univers de
l'estimateur $\hat{C}_l$ de $C_l$ est bien égale à $C_l$:
$$
\overline{\hat{C}_l}=C_l \Rightarrow \overline{\hat{C}_l-C_l} = 0,
$$
donc cet estimateur n'est pas biaisé. Cependant, la valeur actuelle des
$\hat{C}_l$ est nécessairement différente du spectre de puissance
angulaire théorique $C_l$, bien que statistiquement proche. On appelle
variance cosmique la différence au carré entre l'estimateur $\hat{C}_l$
et la valeur attendue $C_l$:
$$
\overline{\left(\frac{\hat{C}_l-C_l}{C_l}\right)^2} = \frac{2}{2l+1}.
$$
Cette moyenne statistique ne s'effectuant que sur $(2l+1)$ valeurs, la
variance statistique pour les $\hat{C}_l$ devient logiquement importante
pour les valeurs de $l$ proche de l'unité. La variance cosmique limite
donc la précision des comparaisons aux grandes échelles cosmologiques
entre les mesures du CMB et la théorie.

### Contraindre les paramètres cosmologiques

Des prédictions théoriques du spectre de puissance peuvent être obtenues
dans différents modèles cosmologiques. Dans un modèle $\Lambda$CDM
standard, ce spectre de puissance est composé de quatre parties
([](#fig:power_spectrum)), sensibles aux différents paramètres de
densité $\Omega_i^0$:

-   $l \lesssim 10$: on constate une montée aux plus grandes échelles du
    spectre de puissance angulaire à cause de l'effet Sachs-Wolfe
    intégré (ISW). Cette montée est en partie due à l'expansion de
    l'Univers, qui aplatit les puits gravitationnels aux échelles
    cosmologiques et permet aux photons qui les traversent de ressortir
    avec plus d'énergie que lors de leur entrée (d'où plus de puissance
    à ces échelles dans le spectre). Cette partie du spectre de
    puissance est donc sensible à l'énergie noire $\Omega_\Lambda^0$;

-   $10 \lesssim l \lesssim 100$: c'est le plateau de Sachs-Wolfe,
    constant en $l$. Il est essentiellement sensible à la courbure de
    l'Univers $\Omega_k^0$;

-   $100 \lesssim l \lesssim 1000$: cette partie du spectre de puissance
    est dominée par les pics acoustiques engendrés par les oscillations
    du plasma primordial. Le premier pic, le plus puissant, correspond
    aux sur-densités qui ont atteint leur compression maximale. Les pics
    suivants correspondent ensuite successivement à des compressions
    minimales et maximales, amorties. Ils fournissent beaucoup
    d'informations sur les paramètres cosmologiques (voir
    [](#fig:power_spectrum)):

    -   la position globale des pics renseigne sur $\Omega_\Lambda^0$ et
        $\Omega_k^0$

    -   la hauteur et la largeur des pics contraignent $\Omega_m^0h^2$

    -   l'importance relative des pics permet de contraindre
        $\Omega_b^0h^2$

-   $l \gtrsim 1000$: le spectre de puissance angulaire s'amortit aux
    petites échelles à cause de la non-instantanéité de la
    recombinaison. Ceci a pour effet de gommer les anisotropies les plus
    petites, et donne une sensibilité à $\Omega_b^0h^2$ et $\Omega_m^0$
    (voir [](#fig:power_spectrum)).

\centering
![Gauche: allure du spectre de puissance angulaire $C_l$ pour un modèle
$\Lambda$CDM (*Source:
<http://ned.ipac.caltech.edu/level5/March05/Scott/Scott4.html>*).
Droite: variation du spectre de puissance angulaire théorique en
fonction de la variation des paramètres $\Omega_i^0$
[@Hu2001].](../images/power_spectrum.jpg "fig:"){width="45%"}
![Gauche: allure du spectre de puissance angulaire $C_l$ pour un modèle
$\Lambda$CDM (*Source:
<http://ned.ipac.caltech.edu/level5/March05/Scott/Scott4.html>*).
Droite: variation du spectre de puissance angulaire théorique en
fonction de la variation des paramètres $\Omega_i^0$
[@Hu2001].](../images/cmb_omegas.eps "fig:"){width="54%"}

[\[fig:power\_spectrum\]]{#fig:power_spectrum
label="fig:power_spectrum"}

Nous avons vu que le premier pic est particulièrement sensible aux
paramètres cosmologiques. Sa position dans le spectre de puissance
angulaire est liée à la taille de l'horizon acoustique au découplage
$r_s(z_*)$ défini par: 
$$\label{eq:rs}
r_s(z_*) = \frac{c}{H_0}\int_{z_*}^\infty \frac{c_s(z')}{\bar{h}(z')}dz'
$$
C'est la distance propre maximum sur laquelle a pu se propager une onde
acoustique créée par une fluctuation de densité, des débuts de l'Univers
jusqu'au découplage. Le redshift du découplage $z_*$ peut être estimé à
partir des paramètres cosmologiques grâce à la formule de Hu et Sugiyama
{cite:p}`Hu1996`: 
$$\label{eq:zstar}
z_*=1048\left[1+0.00124(\Omega_b^0h^2)^{-0.738}\right]
\left[1+g_1(\Omega_m^0h^2)^{g_2}\right]
$$ 
$$
\begin{aligned}
g_1=\frac{0.0783(\Omega_b^0h^2)^{-0.238}}{1+39.5(\Omega_b^0h^2)^{0.763}}\\
g_2=\frac{0.560}{1+21.1(\Omega_b^0h^2)^{1.81}}.\end{aligned}
$$
Cette formule a été élaborée à partir de la simulation d'un grand nombre de
modèles cosmologiques. Elle est estimée fiable à quelques pour-cents
près pour un grand nombre de scénarios cosmologiques {cite:p}`Hu1996`. 

En combinant $r_s (z_*)$ et la distance angulaire comobile au découplage
$d_A (z_*)$ (définie section [](#sec:distances)), on peut en déduire la taille angulaire
comobile de l'horizon acoustique sur la carte de température:
$$\theta_a =  \frac{r_s(z_*)}{d_A(z_*)},$$ qui traduite en échelle $l$
donne l'échelle acoustique $l_a$:
$$\fbox{$\displaystyle l_a = \frac{\pi}{\theta_a} = \frac{\pi d_A(z_*)}{r_s(z_*)}=(1+z_*)\frac{\pi D_A(z_*)}{r_s(z_*)}$}$$
échelle à laquelle est mesurée la position du premier pic, avec $D_A$ la
distance angulaire définie
section [](#sec:distances). On verra par la suite que l'on mesure
$l_a\approx 300$ alors que la position du premier pic sur les spectres
de puissance mesurés est à $l\approx 220$ (angle de 1). La différence
vient de l'effet Sachs-Wolfe intégré survenant juste après le
découplage. A ce moment de l'histoire de l'Univers, celui-ci est encore
dominé par le rayonnement, qui a pour effet d'aplanir les puits
gravitationnels. Ce lissage du paysage gravitationnel a pour effet de
décaler l'ensemble des pics acoustiques de $\Delta l \approx -80$
{cite:p}`Hu2001b`.

(mesures)=
### Mesure

\centering
![Gauche: spectre de puissance angulaire des anisotropies de température
$\hat{C}_l$ du CMB observé par WMAP9 (mission WMAP après 9 ans de prises
de données) en noir, SPT en bleu et ACT en jaune, comparé à un modèle de
spectre de puissance angulaire $C_l$ issu du modèle $\Lambda$CDM ajusté
aux données (ligne grise) [@Hinshaw2013]. Droite: spectre de puissance
des anisotropies de température du CMB $\hat{C}_l$ mesuré par Planck
(bleu), comparé au modèle $\Lambda$CDM ajusté aux données (rouge)
[@PlanckCollaboration2013XVI].](../images/WMAP9_power_spectrum.jpg "fig:"){width="47%"}
![Gauche: spectre de puissance angulaire des anisotropies de température
$\hat{C}_l$ du CMB observé par WMAP9 (mission WMAP après 9 ans de prises
de données) en noir, SPT en bleu et ACT en jaune, comparé à un modèle de
spectre de puissance angulaire $C_l$ issu du modèle $\Lambda$CDM ajusté
aux données (ligne grise) [@Hinshaw2013]. Droite: spectre de puissance
des anisotropies de température du CMB $\hat{C}_l$ mesuré par Planck
(bleu), comparé au modèle $\Lambda$CDM ajusté aux données (rouge)
[@PlanckCollaboration2013XVI].](../images/Planck_power_spectrum.jpg "fig:"){width="52%"}

[\[fig:power\_spectrum\_mesure\]]{#fig:power_spectrum_mesure
label="fig:power_spectrum_mesure"}

Le spectre de puissance angulaire a été mesuré récemment par les
satellites WMAP et Planck, ainsi que par des expériences au sol (ACT et
SPT, sensibles à partir de $l\gtrsim 500$). La mesure du spectre de
puissance consiste à capter les photons sur plusieurs bandes de
fréquence autour de 200 (maximum d'émission du CMB) et au delà pour
pouvoir capter l'émission venant des avant-plans (émission des
poussières galactiques à environ 18, amas, etc\...). Une carte précise
de la température du CMB peut alors être construite, avec des
incertitudes maîtrisées, de laquelle on tire le spectre de puissance
angulaire (voir les mesures de WMAP9 et Planck [](#fig:power_spectrum_mesure)).

Pour confronter les spectres de puissance angulaires à des modèles
cosmologiques, il faut être capable de prédire dans ces derniers la
forme du spectre. Pour des modèles cosmologiques standard ($\Lambda$CDM,
FWCDM,\...) cette prédiction est connue
([](#fig:power_spectrum) par exemple). En revanche, pour des
modèles plus complexes, il peut être très difficile à calculer. Dans le
cas du modèle Galiléon, une telle prédiction n'existait pas au début de
ma thèse en 2011. Mais en août 2012 les équations permettant la
prédiction d'un spectre de puissance angulaire dans le cadre d'un modèle
Galiléon ont été publiées {cite:p}`Barreira2012` puis confrontées aux données
en 2013 {cite:p}`Barreira2013`.

A partir du spectre des fluctuations de température, il est cependant
possible d'extraire un certain nombre de paramètres qui soient
indépendants du choix de la cosmologie. Les références
{cite:t}`Wang2006; Wang2007; Elgaroy2007` montrent qu'il existe deux
paramètres, liés au premier pic acoustique, dérivables du spectre de
puissance et indépendants de la cosmologie. Ces deux paramètres sont
l'échelle acoustique $l_a$ déjà introduite et le paramètre de shift $R$
défini par:
$$\fbox{$\displaystyle R = \frac{\sqrt{\Omega_m^0H_0^2}}{c}(1+z_*)D_A(z_*)=\sqrt{\Omega_m^0}\int_0^{z_*}\frac{dz'}{\bar H(z')}$}$$
Plus précisément, ces paramètres peuvent être déduits des spectres de
puissance dans différentes cosmologies et les auteurs montrent que les
valeurs centrales et les incertitudes sont quasi-identiques dans toutes
ces configurations (voir
[](#fig:la_R)).

\centering
![Densités de probabilité obtenues pour les paramètres $R$ (gauche) et
$l_a$ (droite) à partir du spectre de puissance WMAP3 pour différents
modèles cosmologiques, tirées de la référence
[@Wang2007].](../images/R.eps "fig:"){width="48%"} ![Densités de
probabilité obtenues pour les paramètres $R$ (gauche) et $l_a$ (droite)
à partir du spectre de puissance WMAP3 pour différents modèles
cosmologiques, tirées de la référence
[@Wang2007].](../images/la.eps "fig:"){width="48%"}

[\[fig:la\_R\]]{#fig:la_R label="fig:la_R"}

|        | WMAP7                                                                                                                                 | WMAP9  |
|--------|---------------------------------------------------------------------------------------------------------------------------------------|--------|
|  $l_a$ | $302.09\pm0.76$                                                                                                                       | $302.40\pm0.69$ |
| $R$ | $1.725\pm0.018$                                                                                                                       | $1.725\pm0.018$ |
| $z_*$ | $1091.3\pm0.91$                                                                                                                       | $1090.88\pm1.00$ | 
| $\mathbf{C}^{-1}_{CMB}$ | $\left( \begin{array}{ccc} 2.305 & 29.698 & -1.333 \\ 29.698 & 6825.270 & -113.180 \\ -1.333 & -113.180 & 3.414 \end{array} \right)$  | $\left( \begin{array}{ccc} 3.182 & 18.253 & -1.429 \\ 18.253 & 11887.879 & -193.808 \\ -1.429 & -193.808 & 4.556 \end{array} \right)$ |

La collaboration WMAP a publié les mesures de ces paramètres à partir de
leur spectre de puissance angulaire, accompagnées de leur matrice de
covariance. En revanche, la collaboration Planck
{cite:p}`PlanckCollaboration2013XVI` ne les fournit pas. Un groupe indépendant
les a dérivés à partir du spectre de puissance angulaire de Planck
{cite:p}`Wang2013`, mais ceux-ci ne sont peut-être pas indépendants de toute
hypothèse cosmologique à cause de l'inclusion des effets de lentille
gravitationnelle dans le spectre de puissance observé par le satellite
Planck.

La référence {cite:t}`Komatsu2009` signale cependant que les valeurs mesurées
des paramètres $l_a$, $R$ et $z_*$ ne peuvent être utilisées que pour
contraindre des modèles cosmologiques satisfaisant un certain nombre
d'hypothèses (utiliser une métrique FLRW, utiliser
$N_{\mathrm{eff}}=3.04$, avoir des conditions initiales
identiques,\...). Le modèle du Galiléon remplit bien toutes ces
conditions {cite:p}`Nesseris2010`.

Oscillations acoustiques de baryons
-----------------------------------

Les oscillations acoustiques de baryons (BAO) sont intimement liées à la
physique du fond diffus cosmologique. Elles correspondent à la trace
laissée dans le spectre de la matière par les oscillations acoustiques
qui ont eu lieu avant le découplage et ont été figées à $z=z_d$. On a vu
que le premier pic acoustique possède une taille angulaire
$\theta \approx \SI{1}{\degree}$, ce qui correspond à une distance
comobile transverse de 150. Cette distance caractéristique séparant les
fluctuations de température du CMB se retrouve ensuite dans le spectre
de la matière, car les sur-densités de baryons au découplage sont les
germes des futures grandes structures de l'Univers. Une distance
transverse comobile caractéristique de 150 est donc attendue entre les
galaxies: c'est une règle standard. Une description complète et
pédagogique de la mesure des BAOs est donnée dans la référence
{cite:t}`Percival2013`.

### Spectre de puissance de la matière

Au moment du découplage entre les photons et les baryons, l'image de la
carte des fluctuations $\delta(t,\vec r)$ est donnée par la carte des
fluctuations de température. On construit un spectre de puissance défini
par
$\left\langle \left( \Delta T/ T_{\mathrm{CMB}} \right)^2 \right\rangle$
représenté en fonction d'une échelle $l$. Nous allons faire de même pour
le spectre de puissance de la matière. La matière étant constituée
essentiellement de matière sombre non visible, il est supposé que les
baryons suivent bien la distribution totale de la matière. Les galaxies
sont alors supposées être un bon traceur de la distribution de la
matière. Toutefois, les fluctuations de densité des galaxies ne sont
probablement pas égales aux fluctuations de densité de la matière. Ce
désaccord est modélisé par un biais $b$: $$\label{eq:biais}
\delta_g = \frac{\delta n_{g}}{n_{g}} = b \frac{\delta \rho_m}{\rho_m} = b \delta_m,$$
qui aura beaucoup d'importance pour les mesures de croissance des
structures (voir section [1.4](#sec:gof){reference-type="ref"
reference="sec:gof"}). On le suppose ici indépendant de $z$ et de
l'échelle $k$.

La stratégie pour mesurer le spectre de puissance de la matière consiste
à relever la position d'un grand nombre de galaxies. Cette position
inclut la donnée de la position angulaire sur la carte du ciel, mais
aussi du décalage spectral $z$, qui doit être mesuré précisément pour
chaque galaxie par spectroscopie. La carte des fluctuations de galaxies
s'exprime dans l'espace de Fourier:
$$\delta_g(\vec r, t) = \frac{1}{(2\pi)^3}\int \delta_g(\vec k,t) e^{-i \vec k \cdot \vec r} d^3 \vec k$$
où $\vec r$ et donc $\vec k$ sont en coordonnées comobiles (on se place
ici dans un espace plat cartésien). Par analogie avec le fond diffus
cosmologique, on définit le spectre de puissance des fluctuations de
matière $\delta_g(\vec k,t)$ par:
$$P(k) = \left\langle \vert \delta_g(\vec k,t) \vert^2 \right\rangle$$
où la moyenne est effectuée sur tous les modes $\vec k$ tels que
$\Vert \vec k \Vert = k$[^13]. La variance
$\left\langle \delta_g^2(\vec r,t) \right\rangle$ est reliée au spectre
de puissance par la relation:
$$\left\langle \delta_g^2(\vec r,t) \right\rangle = \frac{1}{(2\pi)^3} \int d\vec{k} \vert \delta_g(\vec k,t) \vert^2 = \frac{1}{2\pi^2} \int_0^\infty  k^2 dk P(k).$$
On s'attend à retrouver dans le spectre de puissance de la matière
l'empreinte des oscillations primordiales des baryons. Ce sera chose
faite en 2005 avec la première détection du pic acoustique principal
dans le spectre de puissance de la matière par les collaborations SDSS
[@Eisenstein2005] et 2dFGRS [@Cole2005]. Aujourd'hui, dans les
expériences récentes comme celle menée par le Baryonic Oscillation
Spectroscopic Survey (BOSS), plusieurs oscillations baryoniques sont
même visibles (voir figure [\[fig:bao\]](#fig:bao){reference-type="ref"
reference="fig:bao"}, [@Anderson2013]).

### Fonction de corrélation

La fonction de corrélation à deux points permet de mettre en évidence
l'échelle caractéristique de 150. Elle est définie par:
$$\xi(r) = \left\langle \delta_g(\vec r_1) \delta_g(\vec r_2) \right\rangle_r$$
où la moyenne est effectuée sur tous les points $\vec r_1$ et $\vec r_2$
vérifiant $r=\Vert \vec r_2 - \vec r_1 \Vert$. Avec les notations de la
section précédente, on obtient:
$$\xi(r) = \frac{1}{(2\pi)^3}\int d^3 \vec k \vert \delta_g(\vec k,t) \vert^2 e^{-i \vec k \cdot \vec r} = \frac{1}{2\pi^2} \int_0^\infty k^2 dk P(k) \frac{\sin(kr)}{kr}.$$
La fonction de corrélation $\xi(r)$ est donc liée directement au spectre
de puissance de la matière $P(k)$ par une relation de transformée de
Fourier: $$P(k) = \int_0^\infty  r^2 dr \xi(r) \frac{\sin(kr)}{kr}.$$
Les deux quantités $P(k)$ et $\xi(r)$ contiennent donc la même
information sur la répartition de la matière dans l'Univers. Si une
oscillation régulière est présente dans l'espace de Fourier $k$ dues aux
différents modes d'oscillation des fluctuations de baryons, un pic est
attendu en revenant dans l'espace réel $r$. La mesure de la fonction de
corrélation à deux points $\xi(r)$ à partir du relevé de galaxies fait
apparaître clairement ce pic à $r=\SI{150}{\mega\parsec}$ (voir par
exemple figure [\[fig:bao\]](#fig:bao){reference-type="ref"
reference="fig:bao"}).

\centering
![Gauche: spectre de puissance des galaxies $P(k)$. Droite: Fonction de
corrélation des galaxies $\xi(r)$ de l'échantillon. Ces mesures ont été
fournies par la collaboration BOSS (détection du pic à 6.7$\sigma$)
[@Anderson2013].[]{label="fig:bao"}](../images/matter_power_spectrum.jpg "fig:"){width="49%"}
![Gauche: spectre de puissance des galaxies $P(k)$. Droite: Fonction de
corrélation des galaxies $\xi(r)$ de l'échantillon. Ces mesures ont été
fournies par la collaboration BOSS (détection du pic à 6.7$\sigma$)
[@Anderson2013].[]{label="fig:bao"}](../images/bao.jpg "fig:"){width="49%"}

### Mesures {#mesures-1}

La fonction de corrélation peut être calculée pour différents lots de
galaxies[^14] à des intervalles en décalage spectral différents, ce qui
permet de mesurer cette règle standard à différents moments de
l'évolution de l'Univers. La position du pic BAO peut être ajustée pour
un modèle cosmologique donné à partir de simulations à N-corps. Elle est
sensible à une distance dite volumique[^15] {cite:p}`Eisenstein2005`:
$$D_V(z)=\left[(1+z)^2D_A^2(z)\frac{cz}{H(z)}\right]^{1/3},$$ et bien
entendu à la taille de l'horizon sonique au découplage des baryons
$r_s(z_d)$. Les mesures BAO sont données sous la forme:
$$\fbox{$\displaystyle y_s(z)=r_s(z_d)/D_V(z)$}$$ Le redshift $z_d$ de
découplage des baryons est calculé en utilisant la formule
{cite:p}`Eisenstein1998`:
$$z_d=\frac{1291(\Omega_m^0h^2)^{0.251}}{1+0.659(\Omega_m^0h^2)^{0.828}}
\left[1+b_1(\Omega_b^0h^2)^{b_2}\right]$$ $$\begin{aligned}
b_1 &= 0.313(\Omega_m^0h^2)^{-0.419}
\left[1+0.607(\Omega_m^0h^2)^{0.674}\right] \\
b_2 &= 0.238(\Omega_m^0h^2)^{0.223} .\end{aligned}$$

D'autres méthodes pour dériver la position du pic sont possibles, en
utilisant le test géométrique d'Alcock-Paczynski [@Reid2012] (qui permet
d'obtenir une mesure orthogonale et le long de la ligne de visée, et
sera expliqué section [1.4.2](#sec:ap){reference-type="ref"
reference="sec:ap"}) ou bien en comparant directement le spectre $P(k)$
mesuré aux simulations [@Anderson2013].

Dans cette thèse, j'ai sélectionné les mêmes trois mesures BAO que
celles utilisées dans l'analyse cosmologique de BOSS
[@Anderson2013; @Sanchez2012]. Ces mesures ont été sélectionnées de
sorte que les lots de galaxies en jeu ne se recoupent pas et donc qu'il
n'y ait pas de corrélations cachées entre les mesures. Les mesures des
trois collaborations sont présentées dans la
table [\[tab:bao\]](#tab:bao){reference-type="ref"
reference="tab:bao"}[^16].

  ----------------- --------------------- ------------ --------------------
                                                       
    \[-1.ex\] $z$      $y_s^{mes}(z)$      Expérience       Référence
       \[1ex\]                                         
   \[-1.ex\] 0.106    $0.336 \pm 0.015$      6dFGRS       [@Beutler2011]
        0.35         $0.1126 \pm 0.0022$    SDSS LRG    [@Padmanabhan2012]
        0.57         $0.0732 \pm 0.0012$   BOSS CMASS    [@Anderson2013]
       \[1ex\]                                         
  ----------------- --------------------- ------------ --------------------

D'autres méthodes sont possibles pour mesurer la règle standard au cours
de l'histoire de l'Univers. En particulier, en 2012 cette distance
caractéristique a été détectée pour la première fois dans les
forêts[^17] Lyman-$\alpha$, à un redshift lointain $z=2.3$ [@Busca2013].
Une mesure à un redshift si lointain pourrait être contraignante pour le
modèle du Galiléon. Cependant, son incertitude était telle qu'aucune
distance exploitable n'a pu être extraite de la fonction de corrélation.

Pour le moment, les incertitudes invoquées sont dominées par la taille
du volume d'Univers sur lequel s'effectue le relevé de galaxies et la
méthode d'extraction de la mesure. Dans le futur, des relevés de taille
importante, en surface sur le ciel et en profondeur, tels que eBOSS ou
DESI fourniront des mesures plus précises et surtout plus lointaines en
redshift.

Croissance des structures {#sec:gof}
-------------------------

La Galiléon étant une théorie de gravité modifiée, la façon dont les
structures se forment dans une gravité Galiléon est une observable
importante pour distinguer ce modèle du modèle $\Lambda$CDM. Une
observable importante dérivée des modèles de croissance des structures
est fournie par les distorsions dans l'espace des redshifts. Une
introduction est présentée dans la référence [@Percival2009].

### Distorsions dans l'espace des redshifts (RSD)

Pour mesurer la position des galaxies, on relève leur position angulaire
sur le ciel et leur décalage spectral. Afin d'en extraire le signal BAO,
on suppose que ce décalage spectral est uniquement dû à l'expansion de
l'Univers ($z=1/a -1$). Or, si la galaxie a une vitesse particulière
propre le long de la ligne de visée, le redshift mesuré par
spectroscopie sera la somme de deux effets: le redshift cosmologique et
le décalage spectral dû à l'effet Doppler. Ce dernier correspond à une
correction du second ordre dans le calcul du spectre de la matière et
n'est donc pas pris en compte dans le calcul du signal BAO. Cependant,
il contient des informations intéressantes à exploiter pour mesurer la
croissance des structures dans l'Univers.

Considérons une galaxie comme une particule ponctuelle, située au bord
d'un puits de potentiel profond créé par un amas. Cette galaxie va alors
tomber dans le puits et acquérir une vitesse particulière avec une
composante pointant vers le centre du puits. Si cette galaxie se situe
entre nous et l'amas, le redshift mesuré est alors plus grand par effet
Doppler, car elle s'éloigne encore plus vite de nous du fait de
l'expansion de l'Univers. Si elle se situe derrière l'amas, c'est
l'effet inverse. Dans tous les cas, dans un référentiel comobile centré
sur l'observateur, la position mesurée par le redshift $\vec s$ le long
de la ligne de visée sera biaisée et ne reflétera pas la position réelle
$\vec r$ de la galaxie. Plus précisément, on aura: $$\label{eq:rsd}
 \vec s(\vec r) = \vec r + \vec u_z \cdot \vec v(\vec r)$$ avec
$\vec u_z$ un vecteur unitaire parallèle à la ligne de visée et
$\vec v ( \vec r)$ la vitesse particulière de la galaxie (voir
illustration figure [\[fig:rsd\]](#fig:rsd){reference-type="ref"
reference="fig:rsd"}). Cette distorsion de l'espace réel est observable
et renseigne sur la gravité engendrée par la masse centrale.

\centering
![Illustration de la distorsion observée entre positions réelles et
positions déduites du redshift, pour deux galaxies 1 et 2 tombant sur un
objet massif. La distorsion observée dans l'espace des redshifts est due
à la vitesse particulière des
galaxies.[]{label="fig:rsd"}](../images/rsd.jpg){width="90%"}

Dans l'hypothèse où le champ de vitesse est issu d'une théorie linéaire
de la croissance des structures et est irrotationnel, par conservation
de l'énergie en coordonnées comobiles on a:
$$\dot{\delta}_m + \frac{1}{a}\mathrm{div} \vec v = 0,$$ d'où[^18]:
$$\delta_m \frac{d \ln \delta_m}{d \ln a} H +  \frac{1}{a}\mathrm{div} \vec v = 0 \Leftrightarrow f \delta_m = - \frac{1}{Ha}\mathrm{div} \vec v$$
On définit ainsi le champ de vitesse
$\theta  = - \frac{1}{Ha}\mathrm{div} \vec v$ et le taux de croissance
des structures $f$ par:
$$\fbox{$\displaystyle f=\frac{d \ln D(a)}{d \ln a}$}$$ où la fonction
$D(a) = \delta_m(a) / \delta_m(1)$ code la croissance des structures au
cours du temps.

De plus, si on réécrit
l'équation [\[eq:rsd\]](#eq:rsd){reference-type="ref"
reference="eq:rsd"} dans l'espace de Fourier, la position observée de la
galaxie $\delta^s_g(k)$ est liée à sa position réelle $\delta^r_g(k)$
par: $$\delta^s_g(k,\mu) = \delta^r_g(k) - \mu^2 \theta(k) + ...$$ avec
$\mu^2 = \cos^2 \alpha$ (où $\alpha$ est l'angle entre la ligne de visée
et le mode $\vec k$). Le spectre de puissance des galaxies observé
s'écrit alors: $$\label{eq:kaiser1}
P_g^s(k,\mu) = \left\langle \vert \delta_g^s(k,\mu) \vert^2 \right\rangle = P_{gg}(k) -2\mu^2 P_{ g \theta} + \mu^4 P_{\theta\theta}(k),$$
avec
$P_{gg}(k) = \left\langle \vert \delta_g^r(\vec k) \vert^2 \right\rangle$
(spectre des galaxies au premier ordre duquel on déduit la mesure du pic
BAO),
$P_{g\theta}(k) = \left\langle  \delta_g^r(\vec k) \theta(\vec k) \right\rangle$
et
$P_{\theta\theta}(k) = \left\langle \vert \theta(\vec k) \vert^2 \right\rangle$.

Or le champ de vitesse $\theta$ est relié à la croissance des structures
par le paramètre $f$: $\theta (k ) = -f \delta_m(k)$. On peut alors
directement lier le spectre mesuré $P_g^s(k,\mu)$ au spectre de
puissance de la matière (si $\delta_g,b\delta_g\ll 1$) par:
$$\label{eq:kaiser2}
P_g^s(k,\mu) = P_m (k) (b^2 + 2 \mu^2 fb + \mu^4 f^2) = P_{gg}(k)(1 + 2 \mu^2 \beta + \mu^4 \beta^2) ,$$
avec le biais $b$ introduit
équation [\[eq:biais\]](#eq:biais){reference-type="ref"
reference="eq:biais"} avec $\delta_g = b \delta_m$ et $\beta = f/b$. Le
spectre mesuré $P_g^s(k,\mu)$ est donc directement relié au spectre réel
des galaxies $P_{gg}(k)$ comme pour les BAO, mais avec des corrections
dépendant de $\mu,f$ et $b$. C'est la formule dite de Kaiser
[@Kaiser1987].

La normalisation du spectre est usuellement définie par l'amplitude de
l'écart type des fluctuations dans une sphère de rayon 8 Mpc/h:
$$\fbox{$\displaystyle \sigma_{8,g}^2(\mu) = \frac{1}{2\pi^2} \int_0^\infty k^2 dk W_8^2(k)P_g^s(k)$}$$
où $W_8(k)$ correspond à la transformée de Fourier d'une fonction de
fenêtrage de largeur 8 Mpc/h. A partir de
l'équation [\[eq:kaiser1\]](#eq:kaiser1){reference-type="ref"
reference="eq:kaiser1"}, en utilisant le fait que les spectres $P_{gg}$,
$P_{\theta g}$ et $P_{\theta\theta}$ sont isotropes, on obtient:
$$\sigma_{8,g}^2(\mu) = (b\sigma_{8,m})^2 + 2\mu^2 (b r \sigma_{8,m})(f \sigma_{8,m}) + \mu^4(f \sigma_{8,m})^2,$$
où $r$ est le coefficient de corrélation entre les distributions de
masse et de galaxies [@Percival2009]. Grâce à la dépendance en $\mu$, on
peut mesurer directement à partir du spectre $P_g^s(k,\mu)$ les
paramètres $f \sigma_{8,m}$, $b r \sigma_{8,m}$ et $b\sigma_{8,m}$.
C'est la mesure de $f \sigma_{8,m}$ qui sera l'observable utilisée pour
tester la croissance des structures dans le modèle Galiléon, car le
biais n'est pas modélisable.

### Test d'Alcock-Paczynski {#sec:ap}

Il est important de noter ici que pour extraire une mesure du taux de
croissance des structures $f$ du spectre de puissance de la matière, il
faut avant toute chose faire l'hypothèse d'un modèle cosmologique. En
effet, les observations sont effectuées en angles et redshifts dans
l'espace réel. Pour aboutir à un mode $k$ et à un angle $\mu$ dans
l'espace comobile, il faut faire l'hypothèse d'une géométrie d'Univers
donc choisir un modèle cosmologique. Les mesures tirées du spectre
$P_g^s(k,\mu)$ ne sont donc a priori valables que pour un modèle
cosmologique muni d'un jeu de paramètres. Cependant, il existe une
manière de s'affranchir du choix d'une cosmologie en faisant une
hypothèse sur la géométrie des objets observés.

Le test d'Alcock-Paczynski [@Alcock1979] est une mesure de la géométrie
basée sur la comparaison des dimensions tangentielles et radiales
d'objets, qui sont supposés isotropes dans le bon choix de modèle
cosmologique [@Blake2011]. Prenons un objet sphérique. Dans une
cosmologie donnée, celui-ci peut apparaître ellipsoïdal pour un
observateur. Si on sait que dans un espace comobile celui-ci est censé
apparaître sphérique, alors on peut retrouver la cosmologie qui le fait
apparaître ainsi distordu. Ce test géométrique peut donc tout à fait
s'appliquer à la fonction de corrélation à deux points des galaxies que
l'on suppose isotrope.

Plus formellement, considérons un objet sphérique de diamètre $L_0$
(voir figure [\[fig:ap\]](#fig:ap){reference-type="ref"
reference="fig:ap"}). Alors sa taille angulaire comobile observée est:
$$\Delta \theta = \frac{L_0}{(1+z)D_A(z)}.$$ De même, sa dimension
radiale est reliée au redshift à travers la distance propre par:
$$L_0 = \int_0^{z+\Delta z} \frac{cdz}{H(z)} -\int_0^{z} \frac{cdz}{H(z)} = \frac{c\Delta z}{H(z)}.$$
On construit alors le paramètre d'Alcock-Paczynski pour un objet
isotrope par:
$$\fbox{$\displaystyle F(z) = \frac{\Delta z}{\Delta \theta} = (1+z) \frac{D_A(z)H(z)}{c}$}$$

![Illustration de la construction du paramètre
d'Alcock-Paczynski.[]{label="fig:ap"}](../images/ap.png){width="100%"}

Dans le spectre de puissance, on n'a aucune distance caractéristique
$L_0$ à laquelle se rattacher a priori. En revanche, le paramètre
d'Alcock-Paczynski peut être ajusté sur le spectre avec les autres
grandeurs telles que $f\sigma_{8,m}$ de sorte qu'aucune cosmologie ne
doit alors être supposée. En effet, en pratique, il faut toujours
supposer une cosmologie pour convertir les angles et redshifts en modes
$\vec k$. Cependant, on paramètre l'écart entre la cosmologie réelle et
la cosmologie adoptée par deux facteurs d'échelle
$f_\perp = D_A(z)/D_{A,fid}(z)$ et $f_\parallel = H_{fid}(z)/H(z)$, qui
relient les valeurs observées des modes $(k'_\perp,k'_\parallel)$ à
leurs véritables valeurs $(k_\perp,k_\parallel)$ par
$k'_\perp = f_\perp k_\perp$ et $k'_\parallel = f_\parallel k_\parallel$
($\parallel$ et $\perp$ sont définis par rapport à la ligne de visée).
Dans le cadre du test d'Alcock-Paczynski, ces deux paramètres sont liés
au seul paramètre $F(z)$ par:
$$\frac{f_\parallel}{f_\perp} = \frac{D_A(z)H(z)}{D_{A,fid}(z)H_{fid}(z)} = \frac{F(z)}{F_{fid}(z)}.$$
On peut alors choisir de fixer $f_\parallel = 1$ et ne s'intéresser qu'à
$f_\perp = F(z)/F_{fid}(z)$. Avec
$\mu' = k'_\parallel/k = \cos^2 \alpha'$,
l'équation [\[eq:kaiser2\]](#eq:kaiser2){reference-type="ref"
reference="eq:kaiser2"} devient alors [@Blake2011]:
$$P_g^s(k',\mu') = \frac{b^2}{(F/F_{fid})^2} \left[ \frac{1 + \mu'^2\left(\frac{1+\beta}{(F/F_{fid})^2}-1 \right)}{1 + \mu'^2\left(\frac{F_{fid}^2}{F^2}-1 \right)}\right]^2 P_m\left(k'\frac{F}{F_{fid}}\sqrt{ 1 + \mu'^2\left(\frac{F_{fid}^2}{F^2} -1\right) } \right)$$
Comme précédemment, on peut alors tirer du spectre de puissance
l'observable $f\sigma_{8,m}$, mais cette fois-ci accompagnée de la
mesure du paramètre $F(z)$. Le paramètre $f\sigma_{8,m}$ est alors
indépendant du modèle cosmologique car la cosmologie sous-jacente a été
déduite du spectre à travers la recherche de $F(z)$. Cependant, pour
réaliser la mesure il est nécessaire de connaître la forme du spectre de
puissance de la matière $P_m$ [@Blake2011]. Ce dernier peut être obtenu
par des simulations mais limite la solidité de la méthode de mesure.

  ---------------- ------------------ ----------------- ------- -------------- ------------------
                                                                               
    \[-1ex\] $z$     $f\sigma_8(z)$        $F(z)$         $r$     Expérience       Référence
      \[1ex\]                                                                  
   \[-1ex\] 0.067   $0.423\pm 0.055$         \-           \-      6dFGRS (a)     [@Beutler2012]
    \[1ex\] 0.17     $0.51\pm 0.06$          \-           \-      2dFGRS (a)    [@Percival2004]
    \[1ex\] 0.22     $0.53\pm 0.14$     $0.28\pm0.04$    0.83      WiggleZ        [@Blake2011]
    \[1ex\] 0.25    $0.351\pm 0.058$         \-           \-     SDSS LRG (b)   [@Samushia2012a]
    \[1ex\] 0.37    $0.460\pm 0.038$         \-           \-     SDSS LRG (b)   [@Samushia2012b]
    \[1ex\] 0.41     $0.40\pm 0.13$     $0.44\pm0.07$    0.94      WiggleZ        [@Blake2011]
    \[1ex\] 0.57    $0.430\pm 0.067$   $0.677\pm0.042$   0.871    BOSS CMASS      [@Reid2012]
    \[1ex\] 0.6      $0.37\pm 0.08$     $0.68\pm0.06$    0.89      WiggleZ        [@Blake2011]
    \[1ex\] 0.78     $0.49\pm 0.12$     $0.49\pm0.12$    0.84      WiggleZ        [@Blake2011]
      \[1ex\]                                                                  
      \[-1ex\]                                                                 
  ---------------- ------------------ ----------------- ------- -------------- ------------------

  : Mesures de croissance des structures. $r$ est le coefficient de
  corrélation entre les paramètres $f\sigma_{8,m}$ et $F(z)$. (a)
  L'effet Alcock-Paczynski est argumenté comme étant négligeable à bas
  redshift. (b) L'effet Alcock-Paczynski est pris en compte dans la
  mesure de $f\sigma_8$ mais aucune mesure de $F(z)$ n'est fournie.
  []{label="tab:gof"}

### Mesures {#mesures-2}

Parmi les mesures disponibles de $f\sigma_{8,m}$, j'ai pris soin de ne
choisir que celles indépendantes du choix d'un modèle cosmologique. En
effet, un certain nombre d'entre elles ont été dérivées dans le cadre
d'un modèle $\Lambda$CDM, et ne sont donc pas appropriées pour l'étude
du modèle Galiléon. Les mesures choisies sont rassemblées dans le
tableau [\[tab:gof\]](#tab:gof){reference-type="ref"
reference="tab:gof"}. Certaines mesures n'ont pas été dérivées avec un
paramètre d'Alcock-Paczynski, car les auteurs ont justifié que l'impact
du test d'Alcock-Paczynski est faible à bas redshifts[^19].

Comme les paramètres $f\sigma_{8,m}$ et $F(z)$ sont dérivés
conjointement, la corrélation (forte) entre les deux paramètres est
prise en compte. Les incertitudes invoquées ici sont en général dominées
par des incertitudes systématiques liées au choix du modèle pour $P(k)$.
En effet, la formule [\[eq:kaiser2\]](#eq:kaiser2){reference-type="ref"
reference="eq:kaiser2"} a été dérivée à partir d'hypothèses de
linéarité, mais peut être modifiée pour prendre en compte des effets
non-linéaires tels que des frottements. Plusieurs choix de modélisation
sont alors possibles, et n'en retenir qu'une serait un choix arbitraire
non nécessairement motivé. Les mesures de la référence [@Blake2011] sont
par exemple pourvues d'une grande erreur systématique liée au fait que
plusieurs modélisations sont retenues. On reviendra sur l'impact des
non-linéarités
section [\[sec:growth\_disc\]](#sec:growth_disc){reference-type="ref"
reference="sec:growth_disc"}.

Résumé
------

En résumé, au chapitre suivant je vais utiliser les observables
suivantes et détailler comment elles sont calculées dans les modèles
$\Lambda$CDM, FWCDM et Galiléon:

-   supernovæ de type Ia: $m_B^*(z)$;

-   fond diffus cosmologique: $l_a$, $R$, $z_*$;

-   oscillations baryoniques acoustiques: $y_s(z)$;

-   croissance des structures: $f\sigma_8(z)$, $F(z)$.

\bibliographystyle{StyleTheseWithEtAl}

[^1]: Proche de la masse de Chandrasekhar, la pression mécanique exercée
    par les couches externes sur le cœur dépassent la pression répulsive
    de dégénérescence électronique.

[^2]: Il n'y a pas d'hydrogène dans une naine blanche, essentiellement
    du carbone et de l'oxygène.

[^3]: La valeur d'un pixel de l'image de référence est la valeur médiane
    des 20 pixels issus des 20 images de références. Le signal sur bruit
    augmente alors d'un facteur $\sqrt{20}$ et limite la contamination
    de l'image de référence par des événements transitoires.

[^4]: La propriété d'adiabadicité est justifiée par les observations
    actuelles du CMB et la prédiction des modèles d'inflation.

[^5]: La dernière mesure de la collaboration Planck
    [@PlanckCollaboration2013XVI] donne
    $\Omega_b^0h^2 = 0.02205\pm0.00028$ et on calcule
    $\Omega_\gamma^0 h^2 = 2.469\times10^{-5}$ pour
    $T_{\mathrm{CMB}}=\SI{2.725}{\kelvin}$, cependant avant la
    recombinaison on a $a<10^{-3}$. Le rapport
    $a\frac{3\Omega_b^0}{4\Omega_\gamma^0}$ est donc bien petit devant
    1.

[^6]: Ces deux définitions ne tiennent pas compte de la période de
    réionisation, qui a lieu après la recombinaison lorsque les
    premières étoiles se forment et ionisent leur environnement gazeux.

[^7]: Ceci correspond à une transformée de Fourier sur une sphère.

[^8]: Au premier ordre, la théorie des perturbations décrivant les
    fluctuations de température du CMB est linéaire ce qui lie
    linéairement $\Delta T$ aux coefficients $a_{lm}$

[^9]: L'indice $l$ est lié à la taille angulaire typique des
    fluctuations alors que $m$ traduit son orientation sur la voûte
    céleste.

[^10]: Pour un indice $l$ donné, on a la relation de fermeture
    $\sum_m \vert Y_{lm}(\theta,\phi) \vert^2 = (2l+1)/4\pi$.

[^11]: Ou bien, il faudrait pouvoir observer le CMB depuis d'autres
    points de vue que la Terre, autrement dit pouvoir se trouver au
    centre d'une autre sphère de dernière diffusion.

[^12]: On a la relation d'orthogonalité
    $\int d\Omega Y_{lm}(\theta,\phi) Y_{l'm'}^*(\theta,\phi) = \delta_{ll'}\delta_{mm'}$.

[^13]: Ceci est équivalent à la moyenne effectuée sur les indices $m$
    dans la cadre du CMB, et à s'intéresser aux modes $l$ seulement.

[^14]: Par exemple avec des *Luminous Red Galaxies* (LRG): vieilles
    galaxies très lumineuses de couleur plutôt rouge, ou des Emission
    Line Galaxies ELG: jeunes galaxies bleues lointaines présentant un
    doublet marqué de raies d'émission de l'oxygène.

[^15]: Cette distance correspond à la longueur du côté d'un cube de
    volume $\propto d_A(z)^2 / H(z)$. Son introduction permet de gagner
    en sensibilité dans la mesure du pic BAO, notamment en prenant en
    compte les effets d'expansion d'Univers le long de la ligne de visée
    à travers $1/H(z)$ [@Eisenstein2005].

[^16]: A noter qu'une amélioration de la mesure à $z=0.35$
    [@Padmanabhan2012] a été publiée dans la référence [@Anderson2014].
    Cette dernière bénéficie de plus de galaxies, ce qui a permis de
    décroître les incertitudes.

[^17]: Les quasars, des astres très brillants et très lointains,
    présentent une raie d'émission de l'hydrogène Lyman-$\alpha$ très
    marquée dans leur spectre
    ($\lambda_{\text{Ly-}\alpha}^0=\SI{121.5}{nm}$). Leur lumière se
    propageant dans le milieu interstellaire, leur spectre se décale
    vers le rouge du fait de l'expansion de l'Univers et en traversant
    des nuages d'hydrogène des raies d'absorption associées à cette raie
    apparaissent dans le spectre. Sur Terre, on mesure alors un spectre
    présentant une forte raie d'émission en
    $\lambda_{\text{Ly-}\alpha}^{z_{\text{quasar}}} = \lambda_{\text{Ly-}\alpha}^0 (1+z_{\text{quasar}})$
    suivie d'une succession dense de raies d'absorption en
    $\lambda_{\text{Ly-}\alpha}^{z_{H}} < \lambda_{\text{Ly-}\alpha}^{z_{\text{quasar}}}$
    dues aux nuages d'hydrogène situés aux redshifts
    $z_H < z_{\text{quasar}}$. Cet ensemble de raies d'absorption est
    appelé forêt Lyman-$\alpha$.

[^18]: On a la relation
    $H=\frac{1}{a}\frac{da}{dt} = \frac{d\ln a}{dt}$.

[^19]: A bas décalage spectral, on a environ $F(z)\approx z$ donc $f/b$
    peut être mesuré indépendamment de la cosmologie.
