---
short_title: Histoire thermique
authors:
  - jneveu
keywords: fonds diffus cosmologique, CMB, neutrinos, nucléosynthèse
---

Histoire thermique de l'Univers
===============================

L'expansion de l'Univers est aujourd'hui bien décrite par le modèle $\Lambda$CDM plat ($\Omega_k^0=0$). Les proportions de chacune de ces composantes sont aujourd'hui évaluées à {cite}`Planck2018`:
$$ \Omega_\Lambda^0 = 0.685,\quad \Omega_m^0=0.315$$

Dans ce chapitre, nous allons étudier l'histoire thermique de l'Univers ainsi que l'évolution de sa composition. Jusqu'à maintenant dans ce cours, la matière non-relativiste était traitée comme une seule entité, ralentissant l'expansion de l'Univers par son interaction gravitationnelle. Mais pour étudier son évolution avec la température et ses interactions avec les autres composantes, il faut séparer celles-ci en deux contributions: la matière sombre $\Omega_{c}^0$ et la matière baryonique[^baryons] $\Omega_b^0$. En effet, en 1933, en étudiant l'amas de Coma, l'astrophysicien Fred Zwicky montre que la masse déduite du mouvement des sept galaxies qui le composent est 400 fois plus grande que la masse déduite du comptage des objets lumineux. Cette mesure est répétée en 1936 sur l'amas de la Vierge et donne cette fois un facteur 200. Ces mesures toutefois un peu imprécises tombent dans l'oubli jusque dans les années 1970, lorsque l'astronome Vera Rubin constate que la vitesse de rotation des étoiles de la Galaxie d'Andromède est bien plus élevée que ne le suggère sa masse lumineuse observée {cite:p}`Rubin1970`. Le constat est vite répété sur de nombreuses galaxies: une partie de la matière constituant la galaxie est donc une matière sombre, échappant alors à toute détection, représentant souvent la majorité de la masse totale des galaxies. La présence de matière sombre abondante est même visible dans l'amplitude des anisotropies de températures du fond diffus cosmologique (voir fin de chapitre). Aujourd'hui, on estime que la proportion de ces deux formes de matière froide est {cite}`Planck2018`:
$$ \Omega_{c}^0=0.264,\quad \Omega_b^0=0.049$$

Description de l'Univers primordial
--------------------------

### Le fond diffus cosmologique

Si l'Univers est aujourd'hui en expansion, alors il était plus petit dans le passé. L'expansion cosmique réduit la quantité de mouvement des particules d'un facteur $\propto a^{-1}$ et la densité des particules d'un autre $a^{-3}$. Dans les premiers temps, l'Univers était donc un état chaud et dense. Il doit donc il y avoir eu un moment où l'Univers était suffisamment chaud pour que les atomes soient ionisés, et donc dans un état de plasma où les photons interagissent avec les électrons libres. Par ces interactions fréquentes, si l'équilibre thermodynamique est atteint le rayonnement suit un spectre de corps noir défini par la température du milieu (<wiki:Planck's_law>). Lors de la transition de l'état plasma à l'état neutre, vers $3\,000\,\kelvin$ pour un gaz d'hydrogène, l'Univers devient subitement transparent et les photons se propagent librement. Ce rayonnement de corps noir à haute température libéré à cet instant. Ce rayonnement dit fossile a été refroidi par l’expansion de l'Universe. Ce fond diffus cosmologique micro-onde a été prédit en 1948 par Ralph Alpher, Robert Herman {cite:p}`Alpher1948` et George Gamow {cite:p}`Gamow1948` autour de $5\,\kelvin$, et découvert fortuitement par Arno Penzias et Robert Wilson en 1964 {cite:p}`Penzias1965a,Penzias1965b` à un température de $3.5\,\kelvin$ ([](#fig:cmb_antenna)). 

:::{figure} ../../images/Horn_Antenna.jpg
:name: fig:cmb_antenna
:align: center
:width: 80%

L'antenne cornet Holmdel de 15 mètres des Bell Telephone Laboratories à Holmdel, avec Arno Penzias et Robert Wilson, qui a permis la découverte du CMB. Elle a été construite en 1959 dans le cadre d'un travail sur les satellites de communication pour la NASA ECHO I (By NASA, restored by Bammesk).
:::

Le spectre du fond diffus cosmologique a été caractérisé grâce au satellite COBE, et sa température est aujourd'hui établie à (<doi:10.1088/0004-637X/707/2/916>):
$$T_0 = 2.72548 \pm 0.00057 \,\kelvin$$
en modélisant ses données par la loi de rayonnement de Planck :
\begin{equation}
  I_\nu(\nu, T_0) = \frac{2 h \nu^3}{c^2}\frac{1}{\exp(h\nu/k_B T_0) - 1}
\end{equation}
C’est le meilleur rayonnement de corps noir jamais détecté ([](#fig:cmb_cn)). Le rayonnement de fonds diffus cosmologique (CMB) est probablement la preuve la plus directe que l'Univers a bien été sous forme d'un plasma chaud et dense à l'équilibre dans un passé lointain.

:::{figure} ../../images/cmb_cn.jpg
:name: fig:cmb_cn
:align: center
:width: 60%

Ajustement d'un modèle de corps noir sur les diverses données mesurant le flux venant du fond diffus cosmologique {cite:p}`Mather1999`.
:::


### Ordres de grandeurs

Remontons bien au-delà du redshift de la dernière surface de diffusion, et considérons l'Univers à, disons, $z \sim 10\,000$. Que pouvons-nous en dire ?


#### Température

Pour un gaz de photons, nous savons que :
\begin{equation}
\epsilon_\gamma \propto a^{-4}
\end{equation}
Or, à l'équilibre thermique, la densité d'énergie d'un gaz de photons est l'intégrale de la loi de Planck :
\begin{equation}
\epsilon_\gamma = \frac{2 \pi^2 (k_B T)^4}{15 h^3 c^3}
\end{equation}
La température d'équilibre des photons $T_\gamma$ évolue donc comme suit :
\begin{equation}
T_\gamma \propto a^{-1}
\end{equation}
La température des photons $T_\gamma$ peut donc être utilisée comme paramètre temporel comme $a$ ou $z$ si $T$ est isotrope.

:::{exercise} Redshift du CMB
:label: exo:Tdec

Les photons se sont découplés de la matière lorsque l'Univers est passé de l'état plasma à l'état neutre, à $z_{\mathrm{dec}} \approx 1090$. Ils forment maintenant ce que l'on appelle le fond diffus cosmologique. Quelle était la température $T_{\mathrm{dec}}$ des photons au moment du découplage ?

:::

:::{solution} exo:Tdec
:class: dropdown

\begin{equation}
a_{\mathrm{dec}} T_{\mathrm{dec}} = a_0 T_0 \Rightarrow T_{\mathrm{dec}} = (1+z_{\mathrm{dec}}) T_0 = 2972\,\kelvin
\end{equation}

:::

:::{note} Évolution de $T_\gamma$ avec le redshift
:class: dropdown

Grâce aux interactions entre les photons du CMB et la matière à différent redshifts, les cosmologistes sont capables de mesurer l'évolution de la température de ce bain de photons ambiant avec l'expansion. Par exemple, on peut regarder l'interaction Compton des photons du CMB avec le plasma d'électrons chauds ($\approx 10^8\,\kelvin$) situé dans les amas de galaxies (effet Sunyaev-Zeldovich thermique <wiki:Sunyaev–Zeldovich_effect>). On peut également mesuré le chauffage des molécules CO ou CN du gaz interstellaire par les photons du CMB à différents redshifts. Une des meilleures mesures de la décroissance de la température des photons avec l'expansion est  $T_\gamma(z) = (2.726 ± 0.001) × (1 + z)^{1−β}\,\kelvin$ avec $β = 0.006 ± 0.013$ (<doi:10.1051/0004-6361/201322632>, voir aussi <doi:10.1051/0004-6361/201016140>).

```{figure} ../../images/TCMBz.eps
:name: fig:TCMBz
:align: center
:width: 80%

Evolution de la température des photons du CMB en fonction du redshift, tiré de <doi:10.1051/0004-6361/201322632>.
```


:::

#### Densités

Nous pouvons maintenant calculer la contribution actuelle des photons du CMB à la densité critique de l'univers en utilisant la température du corps noir :
\begin{equation}
\Omega_{\gamma}^0= {\epsilon_\gamma^0 \over c^2 \rho^0_c}= {4 \sigma_S T_0^4 \over c^3}{8 \pi \GN \over 3 H_0^2} \sim 5 \times 10^{-5}
\end{equation}
C'est donc une densité d'énergie négligeable comparée à la matière froide et à l'énergie sombre.
Certes, d'autres particules ultra relativistes telles que les neutrinos contribuent à la partie restante de $\Omega_r^0$. Mais avec 3 neutrinos sans masse, on aboutirait seulement à $\Omega_r^0 \sim 9 \times 10^{-5}$ comme on pourra le voir en fin de chapitre.

On définit  _l'équivalence_ le moment où matière relativiste et non relativiste sont en proportion égale.
Calculons le redshift $z_{\rm eq}$ au moment où les proportions de matière et de rayonnement sont égales :
\begin{equation}
 \rho_r(z)= \rho_r^0 (1+z)^4\text{ et } \rho_m(z) = \rho_m^0(1+z)^3
 \end{equation} 
On en déduit que :
\begin{equation}
\frac{\rho_r(z)}{\rho_m(z)} = \frac{\rho_r^0}{\rho_m^0}(1+z) = \frac{\Omega_r^0}{\Omega_m^0}(1+z)
\end{equation}
\begin{equation}
\frac{\rho_r}{\rho_m} = 1 = \frac{\Omega_r^0}{\Omega_m^0}(1+z_{\rm eq}) \Rightarrow z_{\rm eq} = \frac{\Omega_m^0}{\Omega_r^0}-1 \approx \frac{0.3}{9\times 10^{-5}}-1 \approx 3332
\end{equation}
Donc à $z> z_{\mathrm{eq}}$, le contenu de l'Univers est dominé par la matière relativiste.


#### Photons

Concentrons-nous maintenant sur les propriétés des photons. Nous savons que $T_\gamma \propto a^{-1}$, donc à $z=10^4$ leur température est :
\begin{equation}
  T_\gamma(z=10\,000) = (1+z)T_0 \approx 2.726\times 10^{4}\,\kelvin
\end{equation}
L'énergie moyenne des photons à $z=10^4$ est :
\begin{equation}
  k_B T_\gamma(z) = (1+z)k_B T_0  \approx 2.34\,\mathrm{eV}
\end{equation}
Par analyze dimensionnelle, la densité des photons à un redshift z vaut, à des facteurs numériques près que nous verrons plus loin :
\begin{equation}
  n_\gamma(z) \sim \epsilon_\gamma(z)/ (k_B T_\gamma(z)) \sim \frac{\left[(1+z)k_B T_0\right]^3}{c^3 \hbar^3}\sim 
\left\lbrace
\begin{array}{ll}
10^{21}\ \gamma / \mathrm{m^3} & \text{à}\ z=10^4 \\
10^{9}\ \gamma / \mathrm{m^3} & \text{à}\ z=0 \\
\end{array}
\right.
\end{equation}

#### Baryons

Évaluons maintenant la densité de baryons (particules avec 3 quarks comme les protons et neutrons) à $z \sim 10\,000$. La densité de baryons est aujourd'hui $\Omega_b^0 = 0.049$. Avec une densité critique de $\rho_c^0 \sim 6\,m_p / m^{3}$,  cela donne environ $n_b^0 \approx 0.3\,\mathrm{baryons / m^{3}}$ aujourd'hui, puis à $z \sim 10\,000$ :
\begin{equation}
  n_b(z) \approx \Omega_b^0 \rho_c^0 (1+z)^3/m_p \approx 3\times 10^{11} \ \mathrm{baryons} /  \mathrm{m^3}
\end{equation}
L'univers est donc largement dominé par les photons en terme de densité de particules, et cette proportion reste constante tout le long de l'histoire de l'Univers :
\begin{equation}\label{eq:eta}
\boxed{\eta= \frac{n_b(z)}{n_\gamma(z)} \sim \frac{\Omega_b^0 \rho_c^0 c^3 \hbar^3}{(k_B T_0)^3} \sim 10^{-9}}
\end{equation}


#### Taux d'expansion

La valeur du taux d'expansion de Hubble peut être déduite de l'équation de Friedmann :
\begin{equation}
  H(z) = H_0 \left( \Omega_m^0(1+z)^3 + \Omega_r^0 (1+z)^4 + \Omega_\Lambda^0\right)^{1/2}
\end{equation}
Prenons les valeurs canoniques $\Omega_m^0 = 0.315$, $\Omega_\Lambda^0 = 0.685$ et $\Omega_r^0 \sim 9 \times 10^{-5}$ pour la densité de matière relativiste (photons et neutrinos). A $z \sim 10\,000$, cela donne  :
\begin{equation}
  H(z) \approx 10^6 \times H_0
\end{equation}
L'expansion de l'Univers était beaucoup plus rapide qu'aujourd'hui !

(lpm_photons)=
#### Libre parcours moyen des photons

Enfin, on peut s'interroger sur le libre parcours moyen des photons. Les photons interagissent préférentiellement avec les électrons par diffusion Thomson $e^- + \gamma \rightarrow e^- + \gamma$ et une bonne approximation du libre parcours moyen des photons est donnée par :
\begin{equation}\label{eq:lpm_thomson}
 l_{T} =\frac{1}{\sigma_T n_e}
\end{equation}
où $\sigma_T$ est la section efficace de diffusion de Thomson ($6.6529\times 10^{-29}\ \mathrm{m^2}$). Pour la densité électronique, considérons que l'Univers étant neutre, il y a un électron pour chaque proton donc $n_e = n_p \approx 0.3\,e^-/\mathrm{m^{3}}$. Le temps typique entre deux interactions $\tau_T$ est alors :
\begin{equation}
 \tau_T = \frac{l_T}{c} = \frac{1}{\sigma_T n_e c} \approx 5\times 10^{12}\,\mathrm{yr} \gg t_H = \frac{1}{H_0}
\end{equation}
aujourd'hui si la matière est dans un état ionisé, et à l'époque :
\begin{equation}
\tau_T=  \frac{1}{\sigma_T n_e(1+z)^3 c} \approx 5\,\mathrm{yr} \ll \frac{1}{H(z)} \sim 10^{-6} t_H \sim 10\,000\,\mathrm{yr}
\end{equation}

On voit donc que dans le passé les interactions entre matière et photons étaient suffisamment fréquentes pour atteindre l'équilibre thermique en un temps court devant l'expansion de l'Univers. Mais aujourd'hui, même si toute la matière était ionisée, ces photons n'interagissent plus avec elle. Les photons du CMB ne sont donc _pas_ en équilibre thermique avec quoi que ce soit d'autres aujourd'hui. L'immense majorité des photons du CMB n'ont jamais été en contact avec des particules depuis leur émission. 
Cependant, cette absence d'interactions a préservé la forme originale du spectre du CMB, qui n'a été affecté que par le décalage vers le rouge. Un photon détecté à la fréquence $\nu$ a été émis à l'origine à la fréquence $(1+z)\nu$. En d'autres termes, le spectre d'origine était le suivant {cite:p}`Condon2018` :
\begin{equation}
I_\nu(\nu, T_0, z) = \frac{2 h \nu^3}{c^2}\frac{1}{\exp(h\nu/(1+z)k_B T_0) - 1}
\end{equation}
c'est-à-dire toujours un rayonnement de corps noir, mais avec une température $(1+z) T_0$.


### Scénario du Big Bang

L'Univers à $z \approx 10\,000$ était beaucoup plus chaud et plus dense. A cette température, les atomes sont ionisés et on a donc un plasma.
Tout comme aujourd'hui, la densité du nombre de photons était significativement plus grande que celle des baryons.
Enfin, les interactions entre photons et particules chargées étaient beaucoup plus fréquentes (plusieurs par temps de Hubble), il est donc tout à fait logique de considérer l'Univers comme un plasma en équilibre thermique.

A partir de cette description, nous pouvons esquisser un scénario d'évolution du plasma primordial en cataloguant les différents phénomènes physiques qui peuvent se produire lorsque celui-ci se refroidit. En voici un résumé non exhaustif.

Tout d'abord, au sortir de l'inflation (environ $10^{-34}\,$s après le Big Bang), il y a dû y avoir une phase dite de _baryogénèse_, où l'ensemble des particules et antiparticules sont créées avec un léger avantage pour la matière face à l'antimatière menant à $\eta \sim 10^{-9}$. En dessous d'une température de $100\,\GeV$ environ ($t \sim 20\,$ps), la transition de phase électrofaible a lieu, donnant la masse aux particules et faisant apparaître les bosons de jauge Z, W$^\pm$. Sous $150\,\MeV$ ($t\sim 20\,\mathrm{\mu s}$, c'est la transition de phase QCD :  l'interaction forte prend le dessus sur les effets thermiques. Les quarks et gluons coagulent pour former des baryons (trois quarks) et des mésons (deux quarks). Puis, $6\,\mathrm{s}$ plus tard, électrons et positrons s'annihilent car la température du bain de photons passe sous la masse de l'électron $T < m_e=511\,\keV$. Pendant les trois premières minutes de l'Univers ($T > 100\,\keV$), les noyaux atomiques des éléments légers sont formés. Au bout de $380\,000\,$ans, les électrons se lient aux noyaux atomiques ($e^- + p \rightarrow \mathrm{H} + \gamma$), c'est la _recombinaison_, et les photons se découplent de la matière ($\tau_T \ll 1/H)$. Libre de se propager, ces photons forment le fond diffus cosmologique et fournissent une photographie du plasma primordial à la fin de la recombinaison.


Thermodynamique statistique à l'équilibre
-------------------------------

Nous allons maintenant aborder une description plus fine de ce qu'il s'est passé dans l'Univers primordial en utilisant la physique statistique. 

### Description statistique

Modélisons le contenu de l'Univers comme un gaz de particules interagissant faiblement. Nous pouvons alors utiliser le formalisme de la physique statistique et décrire le gaz par les positions et les impulsions de toutes ses particules, définies sur l'espace $\{\vec{x}, \vec{p}\}$. 

Dans un gaz de particules _à l'équilibre thermodynamique_, le nombre de particules pouvant occuper un état d'énergie $(\vec{x}, \vec{p})$ suit une fonction de distribution statistique $f(\vec{x}, \vec{p}, t)$. En cosmologie, en raison de l'homogénéité de l'Univers, $f$ ne peut pas dépendre de la position $\vec{x}$. De plus, en raison de l'isotropie, $f$ ne peut dépendre que de la norme de la quantité de mouvement $p \equiv \Vert \vec{p}\Vert$ et non de sa direction.

Muni des fonctions de distribution, nous pouvons en déduire des propriétés macroscopiques du gaz en évaluant la probabilité d'occupation des états du système. Mais qu'elles sont-elles? Tout d'abord, la mécanique quantique nous impose que la densité des états dans l'espace des phases est finie. En effet, considérons une boîte de taille $L$, avec des conditions périodiques et résolvons l'équation de Schrodinger, nous obtenons que les valeurs possibles de la quantité de mouvement sont :
\begin{equation}
  \vec{p} = \frac{h}{L}\left(n_x \vec{e}_x + n_y \vec{e}_y + n_z \vec{e}_z\right), \ \ \ n_i = 0, \pm 1, \pm 2, \ldots
\end{equation}
où $\vec{e}_x, \vec{e}_y$ et $\vec{e}_z$ sont les vecteurs unitaires et $h$ est la constante de Planck. En conséquence, dans l'espace des quantités de mouvement, il y un état par cube élémentaire de volume $h^3/L^3$. La densité d'état dans l'espace des quantités de mouvement est donc $L^3/h^3$ :
Ensuite, il n'y a qu'une particule dans la boite quantique donc un seul état de position : dans l'espace des positions la densité d'état est de $1/L^3$. Au total, si la particule possède $g$ degrés de liberté internes, la densité d'état dans l'espace des phases est :
\begin{equation}
 g \times  \frac{L^3}{h^3} \times \frac{1}{L^3} = \frac{g}{h^3} = \frac{g}{(2\pi\hbar)^3}
\end{equation}
 La densité d'état est donc indépendante du volume $L^3$. Elle reste la même pour un système arbitrairement grand. 

Les propriétés macroscopiques (densité de nombre, densité d'énergie, pression) se déduisent de la probabilité d'occupation des états $f(\vec{x}, \vec{p}, t)$ et de la densité d'état de l'espace des phases. La densité volumique de particules d'impulsion comprise entre $p$  et $p+\dd p$ est par exemple donné par :
\begin{equation}\label{eqn:fweights}
 n(p) = \frac{g}{(2\pi\hbar)^3} f(p) \dd^3\mathbf{p}
\end{equation}

La densité volumique particulaire moyenne du gaz est:
\begin{equation}\label{eqn:number_density_general}
  \boxed{n = \frac{g}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p,t)}
\end{equation}

Pour la densité d'énergie moyenne, puisqu'on considère que les particules interagissent faiblement et ne sont pas confinées, alors les niveaux d'énergie $E(p)$ sont ceux d'une particule libre $E(p)=\sqrt{p^2c^2 + m^2 c^4}$. Pour obtenir la densité d'énergie du gaz, il suffit de faire la somme des niveaux d'énergie pondérés par leur probabilité d'occupation : 
\begin{equation}\label{eqn:energy_density_general}  
  \boxed{\epsilon = \rho c^2 = \frac{g}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p,t) E(p) = \frac{g}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p,t) \sqrt{p^2c^2 + m^2 c^4}}
\end{equation}

Nous pouvons obtenir de la même manière la pression du gaz : 
\begin{equation}\label{eqn:pression_generale}
  \boxed{P = \frac{g}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p,t) \frac{p^2}{3E}}
\end{equation}

Au final, le tenseur énergie-impulsion pour un ensemble de particules quantiques peut s'écrire :
\begin{equation}
\boxed{T^{\mu\nu}=\frac{g}{(2\pi\hbar)^3}\int{\dd^3\mathbf{p} f(p,t) \frac{p^\mu p^\nu}{p^0}}}
\end{equation}
Remarquons que cette formule est la version quantique en limite continue de la formule [](#eq:TmunuGaz) obtenu pour un gaz parfait classique.

:::{note} Pourquoi $p^2/3E$ ?

Considérons un élément de surface $\delta A$. Nous notons $\hat{n}$ son vecteur unitaire. Les particules de vitesse $v$ qui frappent $\delta A$ entre $t$ et $t + \delta t$ sont situées dans une coque sphérique autour de $\delta$, entre les rayons $vt$ et $v(t + \delta t)$ :
\begin{equation}
  \dd N = \frac{g}{(2\pi\hbar)^3} f(E) R^2 v \dd t \dd\Omega 
\end{equation}

Toutes ces particules n'atteignent pas la surface. Seules celles dont la vitesse sont dirigées vers $\delta A$, c'est-à-dire celles dont le vecteur vitesse est dans l'angle solide sous-tendu par $\delta A$.
angle solide sous-tendu par $\delta A$. Donc :
\begin{equation}
  \begin{split}
    \dd N_{hit} & = \dd N \times \frac{|\hat{v}\cdot\hat{n}|}{4\pi R^2} \\
            & = \frac{g}{(2\pi\hbar)^3} f(E) \frac{\hat{v}\cdot\hat{n}}{4\pi}\ \dd A\ \dd t\ \dd\Omega
  \end{split}
\end{equation}  
Supposons que les interactions soient élastiques et que chaque particule  transfère une quantité de mouvement $2|\vec{p}\vec{n}|$ à la surface. La pression  pression résultante est :
\begin{equation}
  \begin{split}
    \dd P(v) & = \int \frac{2|\vec{p}\cdot\vec{n}|}{\dd A\ \dd t} \dd N_A \\ & = \frac{2|\vec{p}\cdot\vec{n}|}{\dd A\ \dd t} \dd N_A \\
    & = \frac{g}{(2\pi\hbar)^3} f(E) \frac{p^2}{2\pi E} \int \cos^2\theta \sin\theta \dd\theta \dd\phi \\ & = \frac{g}{(2\pi\hbar)^3} f(E) \\
    & = \frac{g}{(2\pi\hbar)^3} f(E) \frac{p^2}{3E}
  \end{split}  
\end{equation}

:::

#### L'équilibre cinétique

Lorsque les particules peuvent échanger souvent de l'énergie et de la quantité de mouvement par des collisions élastiques, le gaz atteint un état d'entropie maximale, appelé équilibre cinétique. Les fonctions de distribution $f(p,t)$ peuvent être obtenues en évaluant l'entropie du gaz ($S = k_B \ln \Omega$) et en la maximisant, pour une énergie totale donnée et un nombre total de particules donné.

Selon la nature fermionique ou bosonique des particules du gaz, la combinatoire donnant les probabilités d'occupation de l'ensemble des micro-états $\Omega$ est différente à cause du principe d'exclusion de Pauli. A énergie totale et nombre total de particules fixés, après usage des multiplicateurs de Lagrange, ces contraintes imposent que les fonctions de distribution à l'équilibre thermodynamique sont :
\begin{equation}
  \boxed{\text{Fermi-Dirac:\ } f(p) = \frac{g}{\exp\left({\dfrac{E(p) - \mu}{k_B T}}\right) + 1}}
\end{equation}
\begin{equation}
  \boxed{\text{Bose-Einstein:\ } f(p) = \frac{g}{\exp\left({\dfrac{E(p) - \mu}{k_B T}}\right) - 1}}
\end{equation}
avec  $T$ la température du gaz, $\mu$ le potentiel chimique de l'espèce et $g$ son nombre de degrés de libertés interne (par exemple le nombre d'état de spin). Elles donnent le nombre de particules pouvant occuper un état d'énergie $E$ selon que ce sont des bosons ou des fermions, à l'équilibre thermodynamique.

A haute température, on retrouve la distribution de Maxwell-Boltzmann :
\begin{equation}
  \boxed{\text{Maxwell-Boltzmann:\ }f(p) = g\exp\left(-{\frac{E(p) - \mu}{k_B T}}\right)}
\end{equation}
valable pour les fermions et les bosons.

Les fonctions de distribution de Fermi-Dirac et de Bose-Einstein dépendent de deux paramètres : la température du gaz, $T$, et le potentiel chimique de l'espèce $\mu$, qui caractérise la variation d'entropie ou d'énergie lorsque le nombre de particules varie (voir l'encadré ci-dessous).

Si le gaz contient plusieurs espèces en interaction, chaque espèce $i$ est décrite par sa propre fonction de distribution, son propre potentiel chimique $\mu_i$. chimique $\mu_i$, et éventuellement (si elle est découplée) sa propre température $T_i$.  Nous pouvons en déduire la densité de nombre, la densité d'énergie et la température de chaque espèce. 

Si toutes les espèces sont en équilibre cinétique et partagent la même température : $T_i = T$, le système a atteint _l'équilibre thermique_.


#### L'équilibre chimique

:::{note} Potentiel chimique

Les variations d'énergie d'un système peuvent être exprimées en fonction de de son entropie, de son volume et de sa température :
\begin{equation}
\dd U = T \dd S - P \dd V + \mu \dd N
\end{equation}
ou encore :
\begin{equation}
\dd S = \frac{\dd U}{T} + \frac{P}{T} \dd V - \frac{\mu}{T} \dd N
\end{equation}

Considérons deux systèmes $\mathcal{S}_1$ et $\mathcal{S}_2$ à des températures $T_1$ et $T_2$ mis en contact.  Si les deux systèmes sont isolés :
1. l'énergie l'énergie totale de ($S_1+S_2$) est constante 
$$\dd U = \dd U_1 + \dd U_2 = 0 \Rightarrow \dd U_1 = -\dd U_2$$
2. l'entropie de ($S_1 + S_2$) atteint un maximum 
$$\dd S = \dd S_1 + \dd S_2 = 0 \Rightarrow \dd U_1/T_1 + \dd U_2/T_2 = 0$$
ce qui donne $T_1 = T_2$ à l'équilibre.

Considérons maintenant que $\mathcal{S}_1$ et $\mathcal{S}_2$ peuvent échanger des particules (en gardant le nombre total de particules constant). Nous avons :
1. $\dd N = \dd N_1 + \dd N_2 = 0 \Rightarrow \dd N_1 = - \dd N_2$ 
2. et l'entropie de $(\mathcal{S}_1 + \mathcal{S}_2)$ atteint un maximum, ce qui donne :
$$-\frac{\mu_1}{T} \dd N_1 - \frac{\mu_2}{T} \dd N_2 = 0$$
d'où $\mu_1 = \mu_2$. À l'équilibre, les deux potentiels chimiques sont égaux.

Considérons maintenant le cas d'une réaction chimique : 
$$1 + 2 \rightleftharpoons 3 + 4$$
c'est-à-dire le cas de quatre systèmes $S_1$, $S_2$, $S_3$ et $S_4$ mis en contact. En suivant le même même raisonnement, on peut montrer que :
1. ils atteignent une même température d'équilibre température $T$ 
2. et qu'à l'équilibre, on a :
$$\mu_1 + \mu_2 = \mu_3 + \mu_4$$

:::

Nous avons vu dans l'encadré ci-dessus que si plusieurs espèces interagissent par le biais d'une réaction, par exemple :
\begin{equation}
  \nu_1 X_1 + \nu_2 X_2 + \ldots \rightleftharpoons \nu'_1 Y_1 + \nu'_2 Y_2 + \ldots
\end{equation}
et atteignent l'équilibre chimique (c'est-à-dire l'état d'entropie maximale), les potentiels chimiques satisfont : 
\begin{equation}
  \sum_i \nu_i \mu_i = \sum_j \nu'_j \mu_j 
\end{equation}
plus toute équation de conservation imposée par une charge conservée (nombre de particules, charge électrique, charge baryonique, etc.)

Pour les photons, il n'y a pas de charge conservée. Même le nombre de photons n'est pas conservé.  Par exemple, nous avons une double diffusion Compton $e^- + \gamma \rightarrow e^- + \gamma + \gamma$ ou Bremstrahlung  $e^- + p \rightarrow e^- + p + \gamma$. D'où :
\begin{equation}
  \mu_\gamma = 0
\end{equation}

Les particules et les antiparticules sont de charges opposées, d'où, _à l'équilibre_ :
\begin{equation}
  \mu_X = -\mu_{\bar{X}}
\end{equation}
On peut aussi utiliser la réaction $X + \bar{X} \rightleftharpoons \gamma + \gamma$ pour arriver à la même conclusion.

En résumé: 
- Un système composés de différentes espèces a atteint l'équilibre cinétique s'il a atteint un état d'entropie maximale décrit par une fonction de distribution de Fermi-Dirac ou de Bose-Einstein. 
- Un système composé de plusieurs espèces interagissant via une ou plusieurs réactions chimiques a atteint l'équilibre chimique s'il a atteint un état d'entropie maximale, où la somme des potentiels chimiques des réactifs est égale à la somme des potentiels chimiques des produits. 
- Un système a atteint l'équilibre thermodynamique s'il a atteint l'équilibre chimique et si toutes les espèces partagent la même température $T$, la _température de l'Univers_.

### Densité et pression des fermions et bosons

Nous avons maintenant tout ce qu'il faut pour calculer la densité particulaire, la densité d'énergie et la pression des constituants de l'Univers. Les potentiels chimiques peuvent être négligés à haute température ($\mu \ll T$), et les équations [](#eqn:number_density_general), [](#eqn:energy_density_general) et [](#eqn:pression_generale) peuvent être réécrites :
\begin{equation}
  \begin{split}
    n &= \frac{g}{2\pi^2\hbar^3} \int \dd p \frac{p^2}{\exp\left(\sqrt{p^2c^2 + m^2 c^4}/k_B T\right) \pm 1} \\
    \epsilon &= \frac{g}{2\pi^2\hbar^3} \int \dd p \frac{p^2 \sqrt{p^2c^2 + m^2 c^4}}{\exp\left(\sqrt{p^2c^2 + m^2 c^4}/k_BT\right) \pm 1} \\
    P &= \frac{g}{2\pi^2\hbar^3} \frac{1}{3} \int \dd p \frac{p^4}{\sqrt{p^2c^2 + m^2 c^4} \left[\exp\left(\sqrt{p^2c^2 + m^2c^4}/k_B T\right) \pm 1\right]}\\    
  \end{split}
\end{equation}
avec le signe $+$ pour les fermions et le signe $-$ pour les bosons.

Dans le cas général, les intégrales ci-dessus doivent être calculées numériquement. Il existe cependant deux limites intéressantes, qui permettent de comprendre les processus physiques en cours : le cas où les particules sont relativiste ($k_B T \gg m c^2$) et le cas opposé d'espèces non relativistes ($k_B T \ll m c^2$). 

Avant de poursuivre, définissons : $x \equiv m c^2/k_B T$ et $\xi \equiv pc/k_B T$. Nous pouvons alors réécrire $n$ et $\rho$ ci-dessus comme :
\begin{equation}
  \begin{split}
    n &= \frac{g(k_BT)^3}{2\pi^2\hbar^3 c^3}  I_\pm(x) \ \ \ \mathrm{with} \ \ I_\pm(x) = \int_0^\infty \dd \xi \frac{\xi^2}{\exp\left(\sqrt{\xi^2 + x^2}\right) \pm 1} \\
    \epsilon &= \frac{g(k_BT)^4}{2\pi^2\hbar^3 c^3}  J_\pm(x) \ \ \ \mathrm{with}\ \ J_\pm(x) = \int_0^\infty \dd \xi \frac{\xi^2 \sqrt{\xi^2 + x^2}}{\exp\left(\sqrt{\xi^2 + x^2}\right) \pm 1} \\
  \end{split}
\end{equation}

#### Limite relativiste

Dans la limite relativiste, nous avons $x\ll 1$ et les intégrales $I_\pm(0)$ et $J_\pm(0)$ peuvent être calculées exactement :
$$
J_-(0) = \frac{\pi^4}{15},\quad J_+(0) = \frac{7}{8}\frac{\pi^4}{15},\quad I_-(0) = 2 \zeta(3),\quad I_+(0) = \frac{3}{2}\zeta(3)
$$
avec $\zeta$ la fonction de Riemann.



Nous trouvons :
\begin{equation}
  \boxed{\begin{aligned}
           &        \mathrm{Bosons}                       &  \mathrm{Fermions} \\
    n = & \frac{g \zeta(3)(k_BT)^3}{\pi^2\hbar^3 c^3}   & n =\frac{3}{4} \frac{g \zeta(3)(k_BT)^3}{\pi^2\hbar^3 c^3}  \\
    \epsilon = & \frac{g\pi^2(k_BT)^4}{30\hbar^3 c^3}        & \epsilon =\frac{7}{8}\frac{g \pi^2(k_BT)^4}{30\hbar^3 c^3} \\
  \end{aligned}}
  \label{eqn:n_rho_relativistic_limit}
\end{equation}
On voit que les densités particulaires et d'énergie sont identiques pour les bosons et fermions relativistes à un facteur numérique près. De plus, les photons sont des bosons avec $g_\gamma=2$ polarisations possibles, donc on a ici redémontré la loi de Stefan-Boltzmann.

Concernant le calcul de la pression, on a $p^2 / E \sim p$ pour les particules relativistes, donc :
\begin{equation}
  P = \frac{1}{3} \frac{g}{2\pi^2\hbar^3 c^3} (k_BT)^4 \int \dd \xi \frac{\xi^3}{\exp\xi \pm 1} = \frac{1}{3} \frac{g}{2\pi^2\hbar^3 c^3} (k_BT)^4 J_\pm(0) = \frac{\epsilon}{3}
  \label{eqn:P_relativistic_limit}
\end{equation}
On retrouve l'équation d'état déjà introduite précédemment. 


:::{exercise}

En utilisant $T_0 = 2,726 K$, calculez la densité de nombre de photons (aujourd'hui) et la densité d'énergie des photons (aujourd'hui). Montrez que :
\begin{equation*}
  \begin{split}
    n_\gamma & = 411\ \mathrm{cm}^{-3}\\
    \epsilon_\gamma &= 4.6 \times 10^{-34}\ \mathrm{g/cm^{3}} \\
    \end{split}
  \end{equation*}
:::


:::{note} Calculs de $I_\pm(0)$ et $J_\pm(0)$
:class: dropdown

To compute $I_{-}(0)$ it is useful to know the definition of the Riemann-zeta function:
$$
\zeta(s) = \sum_{i=1}^\infty \frac{1}{n^s} = \frac{1}{\Gamma(s)} \int_0^\infty \frac{x^s}{e^x - 1} \dd x
\ \ \text{où}\ \ \ \Gamma(s) = \int_0^\infty x^{s-1} e^{-x} \dd x
$$

Pour les bosons, nous obtenons immédiatement 
$$
I_-(0) = 2 \zeta(3) \approx 2.40411
$$
Pour les fermions, nous avons
\begin{equation}
  \begin{split}
    I_+(0) & = \int_0^\infty \xi^2 \left(\frac{1}{e^\xi - 1} - \frac{2}{e^{2\xi} - 1}\right) \dd \xi \\
    & = I_-(0) - 2 \int_0^\infty \frac{\xi^2}{e^{2\xi} - 1} \dd \xi \\
    & = \frac{3}{4} I_-(0) \\
  \end{split}
\end{equation}

$J_\pm(0)$ peut aussi être exprimé comme une fonction de $\zeta$. Pour les bosons, on obtient immédiatement
$$ J_-(0) = \underbrace{\Gamma(4)}_{3!}\ \underbrace{\zeta(4)}_{\pi^4/90} = \frac{\pi^4}{15}$$
Pour le fermion, nous utilisons la même astuce que ci-dessus, et nous obtenons :
$$
J_+(0) = \frac{7}{8} J_-(0)
$$
  
:::


#### Limite non relativiste

Dans la limite non relativiste, l'énergie des particules est égale à leur masse au repos ($m c ^2 \gg k_B T \Leftrightarrow x \gg 1$). Le potentiel chimique $\mu$ n'est plus forcément négligeable non plus. Les intégrales $I$ et $J$ définies ci-dessus sont les mêmes pour les fermions et les bosons et nous trouvons :

\begin{equation}
  \boxed{\begin{aligned}
    n    &\approx g \left(\frac{m k_B T}{2\pi \hbar^2}\right)^{3/2} \exp\left(-\frac{(mc^2 - \mu)}{k_B T}\right)\label{eq:n_nonrel} \\
    \rho &\approx n m + \frac{3}{2} \frac{nk_B T}{c^2} \\
    P    &= n k_B T \ll \epsilon = nmc^2 \\
  \end{aligned}}
\end{equation}
Lorsque la température descend en dessous de la masse au repos des particules, la densité du nombre de particules chute exponentiellement. La densité d'énergie et la pression sont (au premier ordre) proportionnelles à $n$ et diminuent en conséquence. Les espèces non relativistes se comportent donc comme un gaz sans pression (car $P \ll \epsilon$ i.e. $w_m=0$). C'est cette description de la matière non relativiste que nous avons utilisée pour calculer l'expansion de l'Univers dans le régime dit "dominé par la matière".

:::{note} Calcul de la densité particulaire dans le régime non relativiste
:class: dropdown

Avec les mêmes définitions que ci-dessus : $x\equiv m c^2 / k_B T$, $\xi \equiv p c /k_B T$ et avec $y = \mu/k_B T$ pour réintroduire le potentiel chimique, les intégrales $I_-$ et $I_+$ se réduisent à une seule expression si $x \gg 1$  :
\begin{equation}
  I_\pm(x\gg 1) = \int_0^\infty \frac{\xi^2 \dd \xi}{\exp(\sqrt(x^2 + \xi^2) - y)}
\end{equation}
$\xi \ll x$ et nous pouvons développer : $(x^2 + \xi^2)^{1/2} \approx x (1 + \frac{1}{2}\frac{\xi^2}{x^2})$, et nous pouvons approximer l'intégrale ci-dessus avec :
\begin{equation}
    I_\pm(x\gg 1) \approx e^{-(x-y)} \int_0^\infty \xi^2 e^{-\frac{\xi^2}{2 x}} \dd \xi \approx e^{-(x-y)} (2x)^{3/2} \frac{1}{2} \underbrace{\Gamma\left(\frac{3}{2}\right)}_{\sqrt{\pi}/2}
\end{equation}

:::

:::{note} Gaz moléculaire
:class: dropdown

Si la particule considérée est composée de plusieurs atomes, alors elles possèdent plus de degrés de libertés que les 3 translations dans l'espace. Suivant une statistique de Boltzmann, elle peut stocker de l'énergie dans des degrés de liberté de rotation ou de vibration si le milieu est assez chaud, chacun comptant pour $k_B T / 2$ dans son énergie interne. Si on note $g_m$ le nombre de degrés de liberté d'une molécule, alors la densité d'énergie s'écrit :
$$ \epsilon \approx n m c^2 + \frac{g_m}{2} nk_B T = n m c^2 + \frac{1}{\gamma -1} n k_B T $$
avec $\gamma=C_p/C_V$ l'indice adiabatique, que l'on retrouve dans la loi de Laplace $PV^\gamma = \cst$.
:::


:::{note} Ordre de grandeur des potentiels chimiques
:class: dropdown

Pour les fermions, montrons que leur potentiels chimiques sont négligeables. Comparons les densités particulaires avant et après l'annihilation de particules avec leurs antiparticules (voir {cite:p}`KolbTurner` p.89):

\begin{align*}
n_f - n_{\bar f} & = \frac{g}{2\pi^2\hbar^3} \int \dd p \left[ \frac{p^2}{\exp\left((\sqrt{p^2c^2 + m^2 c^4}-\mu)/k_B T\right) + 1} -  \frac{p^2}{\exp\left((\sqrt{p^2c^2 + m^2 c^4}+\mu)/k_B T\right) + 1}\right] \\
& = \frac{g}{6\pi^2\hbar^3}(k_B T)^3 \left[\pi^2 \left(\frac{\mu}{k_B T}\right) + \left(\frac{\mu}{k_B T}\right)^3 \right] \text{ si } mc^2 \ll k_B T \\
& = 2 g \left(\frac{m k_B T}{2\pi \hbar^2}\right)^{3/2} \sinh\left(\frac{\mu}{k_B T}\right) e^{-mc^2/(k_B T)} \text{ si } mc^2 \gg k_B T \\
\end{align*}


Or pour les baryons, aujourd'hui leur densité particulaire est $(n_b - n_{\bar b}) \approx  \eta n_\gamma \propto \eta (k_B T)^3$. Pour les cas relativistes et non relativistes, on a donc $\mu_b / k_B T \sim \eta \ll 1$ donc le potentiel chimique des baryons est bien négligeable. Pour les électrons, comme l'Univers est électriquement neutre[^neutrality] alors on a le même ordre de grandeur. Concernant les neutrinos, c'est plus ambigü car le fond diffus de neutrinos n'a pas encore été détecté, mais en première approximation on peut penser que là encore le potentiel chimique doit être négligeable ({cite}`Weinberg1989` p.531).

:::


### Nombre effectif d'espèces relativistes

#### Définition

Nous partons d'un plasma primordial en équilibre thermique et chimique, contenant des espèces $i$ à la température $T_i$.
Avant l'équivalence, le taux d'expansion est une fonction directe de la densité massique de matière relativiste :
\begin{equation}
  H^2 = \frac{8\pi G}{3} \rho_r(T)
\end{equation}
où $\rho_r(T)$ est la somme des densités de chaque espèce relativiste présente dans le fluide primordial :
\begin{equation}
  \rho_r(T) = \sum_i^{m_i \ll T} \rho_i(T)
\end{equation}
Nous avons vu dans la section précédente que $\rho_i \propto T_i^4$ tant que la particule reste relativiste, alors que la densité chute exponentiellement quand la température tombe en dessous de la masse de la particule. Plus précisément, nous pouvons écrire :
\begin{align*}
\rho_r & = \sum_{i=\mathrm{bosons}}^{m_i \ll T} \frac{g_i\pi^2}{30\hbar^3c^3}(k_BT_i)^4 +   \sum_{i=\mathrm{fermions}}^{m_i \ll T} \frac{7}{8}\frac{g_i\pi^2}{30\hbar^3c^3}(k_BT_i)^4 \\
& = (k_BT)^4 \left(\frac{\pi^2}{30\hbar^3c^3}\right) \sum_{i=\mathrm{bosons}} g_i \left(\frac{T_i}{T}\right)^4 +   \frac{7}{8} \sum_{i=\mathrm{fermions}} g_i \left(\frac{T_i}{T}\right)^4 
\end{align*}
On définit $g_\star(T)$ le nombre effectif de degrés de liberté _relativistes_ du plasma à la température $T$ : 
\begin{equation}
\rho_r(T) = g_\star(T) \left(\frac{\pi^2}{30\hbar^3 c^5}\right) (k_BT)^4
\end{equation}
\begin{equation}
g_\star(T) = \sum_{i=\mathrm{bosons}}^{m_i \ll T} g_i \left(\frac{T_i}{T}\right)^4 +   \frac{7}{8} \sum_{i=\mathrm{fermions}}^{m_i \ll T}  g_i \left(\frac{T_i}{T}\right)^4
\end{equation}
Lorsque l'espèce $i$ est encore à l'équilibre thermique avec les photons, alors $T_i=T$. Lorsque la température descend en dessous de la masse $m_i$ de l'une des espèces, elle devient relativiste et disparaît de la somme ci-dessus. Si elle se découple des photons avec une température $T_i$ différente des photons, tout en restant relativiste, alors elle reste présente dans $g_*(T)$ avec un poids $(T_i/T)^4$.


#### Évolution de $g_\star(T)$


:::{figure} #gtable
:name: tab:gtable

Caractéristiques des particules du modèle standard pour calculer $g_*(T)$. En l'absence de neutrinos droits, on ne compte qu'un état de spin pour les neutrinos. Les gluons pouvant porter 2 charges de couleurs de l'interaction forte parmi $\lbrace r, g, b\rbrace$, cela fait 9 états possibles mais la combinaison linéaire de couleur blanche  $r\bar r + g \bar g + b \bar b=0$ retire un degré de liberté à l'interaction forte donc il n'y a finalement que 8 états indépendants (<wiki:Gluon>).

:::

Etudions maintenant l'évolution de $g_\star(T)$, qui raconte simplement l'évolution de la matière relativiste du plasma primordial au fur et à mesure qu'il se refroidit avec l'expansion. Commençons autour de $T \approx 300\,$GeV. Toutes les particules du modèle standard sont relativistes (voir [](#tab:gtable)). Lorsque toutes les particules sont relativistes, le nombre total de degrés de liberté est de :
\begin{equation}
  g_f = \underbrace{6}_{\mathrm{quarks}} \times \underbrace{2}_{q\bar q} \times \underbrace{2}_{\mathrm{spin}} \times \underbrace{3}_{\mathrm{couleur}} + \underbrace{3 \times 2 \times 2}_{\ell^\pm} + \underbrace{3 \times 2}_{\nu} = 90
\end{equation}
pour les fermions, et
\begin{equation}
  g_b = \underbrace{8 \times 2}_{\mathrm{gluons}} + \underbrace{3 \times 3}_{W,Z} + \underbrace{2}_{\gamma} + \underbrace{1}_{H}  = 28
\end{equation}
pour les bosons, ce qui donne
\begin{equation}
  g_\star = g_b + \frac{7}{8} g_f = 106.75
\end{equation}

Pour voir ce qui va se passer ensuite, il suffit de regarder les masses des particules énumérées dans le [](#tab:gtable). Le quark top s'annihile en premier car c'est la particule la plus lourde. Pour $k_BT<m_{\mathrm{top}}$, le plasma à l'équilibre ne peut plus produire de quarks top par annihilation de paires d'autres particules, réduisant le nombre de degrés de liberté à :
\begin{equation}
  g_\star(T<m_{\mathrm{top}}) = 106.75 - \frac{7}{8} \times 12 = 96.25
\end{equation}
Puis, nous avons donc le boson de Higgs, suivi des bosons électrofaibles $W^\pm$ et $Z^0$ : ce qui réduit $g_\star$ à 86.25. Ensuite, $b$ et $c$ s'annihilent, et $g_\star$ est alors réduit à 61.75.

L'événement suivant est la transition de phase QCD, qui se produit à $T \sim 150\ \mathrm{MeV}$.  Les quarks se combinent en hadrons (protons, neutrons et mésons). A cette température, tous sont non relativistes sauf les pions. A ce stade, les seules espèces relativistes restantes sont les photons, les neutrinos, les électrons et les muons et les 3 pions de spin 0 (avec donc  $g_\pi = 3 \cdot 1 = 3$ degrés de liberté internes). On en déduit le nombre de degrés de liberté relativiste restant :
\begin{equation}
  g_\star(T<T_{QCD}) = \underbrace{2}_{\gamma} + \underbrace{3}_{\pi^0,\pi^\pm} + \frac{7}{8} \times (\underbrace{4 + 4}_{e^{\pm}, \mu^\pm} + \underbrace{6}_{\nu}) = 17.25
\end{equation}

Ensuite, les pions et les muons s'annihilent, ce qui nous donne
\begin{equation}
  g_\star = 2 + \frac{7}{8} \times (4 + 6) = 10.75
\end{equation}

:::{figure} #ggstar_plot
:name: fig:ggstar_plot

Evolution du nombre effectif d'espèces relativistes $g_\star(T)$.
:::

Les deux événements significatifs suivants sont le découplage des neutrinos autour de $1\,\MeV$ puis l'annihilation des électrons et des positrons ($m_e = 511\,\keV$). 

### Entropie

#### Conservation de l'entropie

L'entropie de l'Univers $S(U,V,N_i)$ est une fonction des variables extensives énergie interne $U$, volume $V$ et des nombres $N_i$ de particules d'une espèce $i$. La variation d'entropie d'un volume comobile $V$ de plasma à l'équilibre thermodynamique obéit au seconde principe de la thermodynamique :
\begin{equation}
  \dd S(U, V, N) = \frac{\dd U}{T} + \frac{P}{T}\dd V - \sum_i \frac{\mu_i}{T} \dd N_i \geq 0
\end{equation}
Pour un volume d'Univers suffisamment grand pour être considéré homogène et isotrope, l'entropie ne peut qu'augmenter ou rester constante. De plus, les potentiels chimiques sont négligeables dans le plasma primordial ($\mu / (k_B T) \sim \eta$). Or, à l'équilibre thermodynamique on a : 
$$U(V, T) = \epsilon(T) V,\quad P = P(T)$$
où pression et densité d'énergie ne sont finalement que des fonctions que de la température d'équilibre, que les espèces soient relativistes ou non (voir formules précédentes). Dès lors, la variation d'entropie est une fonction du volume et de la température avec ({cite}`Weinberg1989` p.532):
$$
\dd S(V,T) = \frac{\dd(\epsilon(T) V)}{T} + \frac{P(T)}{T}\dd V = \frac{V}{T}\frac{\dd \epsilon}{\dd T} \dd T + \frac{P(T)+\epsilon(T)}{T} \dd V
$$
On identifie les dérivées partielles :
$$
\left.\frac{\partial S}{\partial T}\right\vert_V = \frac{V}{T}\frac{\dd \epsilon(T)}{\dd T}, \quad \left.\frac{\partial S}{\partial V}\right\vert_T = \frac{P(T)+\epsilon(T)}{T}
$$
et grâce aux relations de Maxwell (ou théorème de Schwartz), on a :
$$ \frac{\partial^2 S}{\partial T\partial V} = \frac{\partial^2 S}{\partial V\partial T} $$
\begin{align*}
& \Leftrightarrow \frac{\partial}{\partial T}\left[ \frac{P(T)+\epsilon(T)}{T} \right] = \frac{\partial}{\partial V}\left[ \frac{V}{T}\frac{\dd \epsilon(T)}{\dd T} \right] \\
& \Leftrightarrow \frac{1}{T} \frac{\dd ( P + \epsilon)}{\dd T} - \frac{1}{T^2}(P+\epsilon) = \frac{1}{T}
\frac{\dd \epsilon}{\dd T} \\
& \Leftrightarrow \frac{\dd P}{\dd T} = \frac{\epsilon + P}{T}
\end{align*}

Avec cette dernière relation, on peut terminer le calcul de la variation d'entropie :
\begin{align*}
\dd S(V,T) & = \frac{P(T)+\epsilon(T)}{T} \dd V + \frac{V}{T}\frac{\dd \epsilon}{\dd T} \dd T \\
& = \frac{P(T)+\epsilon(T)}{T} \dd V + \frac{V}{T}\left[\frac{\dd (\epsilon+P)}{\dd T} - \frac{\dd P}{\dd T} \right]\dd T \\
& = \frac{1}{T} \dd \left[V(P+\epsilon)\right] - \frac{V}{T} \frac{\dd P}{\dd T}\dd T \\
& = \frac{1}{T} \dd \left[V(P+\epsilon)\right] - \frac{V}{T^2}(\epsilon + P)\dd T \\
& = \dd \left[\frac{V}{T}(P+\epsilon)\right]
\end{align*}
Si on considère une variation par rapport au temps $t$ :
$$\frac{\dd S}{\dd t} = \frac{\dd}{\dd t}\left[ \frac{V}{T}(P+\epsilon)\right] = \frac{V}{T}\dot \epsilon + \frac{\epsilon + P}{T} \dot V + \frac{V}{T} \dot P - \frac{V}{T^2}(\epsilon + P)\dot T$$
et enfin en se souvenant de la relation de conservation de l'énergie $\dot \epsilon = -3H(\epsilon + P)$,
$$\boxed{\frac{\dd S}{\dd t} = 0}$$
L'entropie dans un volume comobile est donc conservée et s'écrit[^Sconst] :
$$\boxed{S(V, T) = \frac{V}{T}(P+\epsilon)}$$
On définit l'entropie volumique, fonction de la température uniquement :
$$\boxed{s(T) = \frac{P+\epsilon}{T}, \quad \dd(a^3 s) = 0}$$

#### Entropie du plasma primordial

Pour les espèces relativistes, comme $P=\epsilon/3$, nous obtenons les entropies volumiques :
\begin{equation}
  \boxed{s_r(T) = \frac{4}{3}\frac{\epsilon_r}{T} =
\left\lbrace
\begin{array}{ll}
     \dfrac{2\pi^2k_B^4}{45\hbar^3 c^3} T^3 & \text{pour les bosons}\\
     \dfrac{7}{8} \dfrac{2\pi^2 k_B^4}{45\hbar^3 c^3} T^3 & \text{pour les fermions}
  \end{array}
\right.}
\end{equation}
Pour une collection d'espèces (fermions et bosons) à l'équilibre aux températures $T_i$, nous avons :
\begin{equation}
    s_r(T) =  \sum_i^{m_i \ll T} \frac{\epsilon_i + P_i}{T_i} =  \frac{4}{3} \sum_i^{m_i \ll T} {\epsilon_i}{T_i} = \frac{2\pi^2 k_B^4}{45 \hbar^3 c^3} g_{\star S}(T) T^3
\end{equation}
avec
\begin{equation}
  g_{\star S}(T) = \sum_{\mathrm{bosons}} g_b \left(\frac{T_b}{T}\right)^3 + \frac{7}{8} \sum_{\mathrm{fermions}} g_f \left(\frac{T_f}{T}\right)^3
\end{equation}
Puisque l'entropie $S$ est conservée, alors :
\begin{equation}
\dd(s a^3) = 0 \Rightarrow   g_{\star S}(T) T^3 a^3 = \cst
\end{equation}


#### Température de l'Univers

Maintenant que nous avons une relation de conservation, on peut établir un lien entre l'expansion de l'Univers et sa température :
\begin{equation}\label{eq:Tagstar}
  \boxed{T \propto \left[g_{\star S}^{1/3}(T) a\right]^{-1}}
\end{equation}
Cette relation donne un lien entre température et facteur d'échelle à tout instant dans l'histoire de l'Univers. Elle varie bien avec le redshift en $(1+z)$ mais avec un facteur de proportionnalité $g_{\star S}^{1/3}(T)$ qui change par seuil selon la composition de l'Univers ([](#fig:Ta_plot)). 



:::{figure} #Ta_plot
:name: fig:Ta_plot

Evolution de la température au cours de l'expansion de l'Univers selon les espèces relativistes présentes (équation [](#eq:Tagstar)). En réalité les transitions de phase ne sont pas soudaines, donc la courbe réelle doit être lissée.
:::

### Expansion du plasma primordial

La loi d'expansion obéit à la première équation de Friedmann :
\begin{equation}
  H^2 = \frac{8\pi G}{3} \rho_r = \frac{8\pi G}{3} \frac{\pi^2}{30\hbar^3 c^5} g_\star(T) T^4
\end{equation}
et donc :
\begin{equation}
  \boxed{H(T) = \sqrt{\frac{8 \pi^3 G}{90 \hbar^3 c^5}} g_\star^{1/2}(T) (k_B T)^2}
\end{equation}
Ainsi, $H \propto T^2$ aux variations près du nombre effectif de degrés de liberté dans le plasma primordial. Gardez cela à l'esprit, cela sera utile pour comparer le taux d'expansion avec les divers taux de réaction entre les différentes espèces.


En injectant l'évolution de la température avec le facteur d'échelle (équation [](#eq:Tagstar)), on retrouve que $a(t) \propto t^{1/2}$ dans l'Univers primordial (équation [](#eq:a_rad_only)) avec le facteur de proportionalité qui change quand $g_{\star S}$ varie. Mais le taux d'expansion vaut alors simplement $H(t) = 1/(2t)$ ce qui donne :
\begin{equation}\label{eq:Ttoa}
  \boxed{T \approx \left[ 1.8 \times 10^{10}\,\mathrm{K}\right] \times  g_*(T)^{-1/4} \left(\frac{t}{\mathrm{1\ sec}}\right)^{-1/2} \approx \left[ 1.6\,\mathrm{MeV}\right] \times  g_*(T)^{-1/4} \left(\frac{t}{\mathrm{1\ sec}}\right)^{-1/2} } 
\end{equation}
Ainsi, lorsque l'Univers était âgé d'une seconde, l'énergie typique des particules relativistes était de l'ordre de $0.9\,\MeV$ avec $g_*=10.75$.


Histoire de la matière dans l'Univers jeune
--------------------------------------

Nous avons maintenant (presque) tout ce dont nous avons besoin pour discuter de l'évolution de la matière dans le plasma primordial. Lorsque la température est suffisamment élevée, le plasma primordial contient toutes les particules du modèle standard, sous forme relativiste (plus toutes les particules qui n'ont pas encore été découvertes, par exemple les particules hypothétiques qui constitueraient la matière sombre froide aujourd'hui). Toutes les espèces de particules sont en équilibre thermique (cinétique et chimique, même température $T$). Mais au fur et à mesure de l'expansion de l'Univers, la température diminue au rythme du taux d'expansion. L'une après l'autre, les différentes espèces massives deviennent non relativistes, s'anéantissent, et leurs densités d'énergie deviennent sous-dominantes par rapport aux espèces relativistes. 

Si l'Univers était en parfait équilibre thermique, et si cet équilibre avait persisté jusqu'à aujourd'hui, les abondances observées de particules massives seraient bien inférieures à ce qu'elles sont, puisque chaque espèce massive voit sa densité exponentiellement supprimée lorsqu'elle devient non relativiste. En fait, les équilibres thermiques et chimiques ont besoin de taux de collision (et/ou de réaction) fréquents pour être maintenus. Avec l'expansion de l'Univers, les particules se diluent, ce qui rend plus difficile le maintien des taux de réaction. 

Puisque $T \propto a^{-1}$ [](#eq:Ttoa), le taux de variation de la température est le taux de Hubble :
$$H = \frac{\dot a }{a} = \frac{\dot T}{T}$$
Pour pouvoir considérer que le système est à l'équilibre thermodynamique, il faut qu'il y ait suffisamment d'interactions dans un temps plus court que le temps de variation de la température.
La règle empirique est donc qu'il faut au moins plusieurs interactions par temps de Hubble pour pouvoir maintenir l'équilibre thermique et chimique. 
Ainsi, si on note $\Gamma$ le taux d'interaction, l'équilibre thermique et chimique est maintenu si $ \Gamma \gg H$. Lorsque le taux de réaction $\Gamma$ chute en dessous de $H$, l'équilibre thermodynamique n'est plus maintenu, les densités de particules sont gelées à leurs valeurs d'avant le découplage. Le gel des interactions est un mécanisme essentiel pour expliquer l'abondance actuelle des particules.


### Découplage des neutrinos et annihilations électron-positron

Le découplage des neutrinos est notre première illustration de l'effet de gel. Les neutrinos n'interagissent que par le biais de l'interaction faible.  Autour de $\sim 1\,\MeV$, ils sont encore thermalisés avec le bain de photons par des interactions telles que :
\begin{equation}
  \begin{split}
    \nu_e + \bar{\nu_e} & \rightleftharpoons e^+ + e^- \\
    e^- + \nu_e & \rightleftharpoons e^- + \nu_e  
  \end{split}
\end{equation}
A ces énergies, la section efficace de l'interaction faible est $\sigma_w \sim G_F^2 T^2$ avec $G_F/(\hbar c)^3=1.166 378 7(6)\times 10^{−5}\,\GeV^{−2}$ la constante de couplage de Fermi {cite:p}`PDG2010`. Par conséquent, le taux d'interaction $\Gamma = n_e \sigma_w c \propto G_F^2 T^5$ diminue beaucoup plus rapidement que le paramètre de Hubble ($\propto T^2$) :
$$
\frac{\Gamma}{H} \sim \frac{n_e \sigma_w}{H} \sim \left(\frac{T}{1\,\MeV}\right)^3
$$
Autour de $1\,\MeV$, $\Gamma \sim H$ et les interactions entre les neutrinos et les autres particules du modèle standard deviennent très improbables. Les neutrinos se découplent du plasma primordial mais restent relativistes ($m_\nu \ll 1\,\MeV$). Même s'ils n'interagissent plus avec d'autres particules, ils conservent dans une excellente approximation leur fonction de distribution de Fermi-Dirac (voir encadré) avec une température qui n'est affectée que par le décalage vers le rouge. Ainsi, à ce stade :
\begin{equation}
  T_\nu = T_\gamma \propto a^{-1}
\end{equation}
tant que l'évolution de la température des photons ne varie pas.


:::{note} Couplage de Fermi
La constante de couplage de Fermi est le couplage dans un diagramme à 4 fermions interagissant par interaction faible à basse énergie (bien inférieure à la masse des bosons de l'interaction faible). Il est lié à la masse du $W$ et à la valeur attendue du Higgs dans le vide $v$ :
$$ G_F = \frac{\sqrt{2}}{8} \left(\frac{g_W}{m_W c ^2}\right)^2(\hbar c)^3, \quad v = (\sqrt{2}G_F)^{-1/2} \sim 246.22\,\GeV$$


:::

:::{note} Le spectre des espèces découplées sans interaction XXX DRAFT

Pour les espèces ultra-relativistes, nous avons $pc \sim E$. Le nombre de particules à $t_1$ dans le volume de l'espace des phases $d^3p_1 \dd V_1$ est :
\begin{equation}
\dd N = \frac{g}{(2\pi)^3} \frac{\dd^3p_1 \dd V_1}{\exp((E(p_1) - \mu_1)/T_1) \pm 1}
\end{equation}
A $t_0$, un peu plus tard, les mêmes particules se trouvent dans le volume de l'espace des phases $\dd^3p_0 \dd V_0$.   Les moments s'échelonnent comme $a^{-1}$ et le volume comme $a^3$. On peut donc écrire
\begin{equation}
\begin{split}
  \dd N  & = \frac{g}{(2\pi)^3} \frac{\dd^3p_1 \dd V_1}{\exp((p_1 - \mu_1)/T_1) \pm 1} \\
      & = \frac{g}{(2\pi)^3} \frac{d^3p_0 \left(\frac{a_0}{a_1}\right)^3 \dd V_0\left(\frac{a_1}{a_0}\right)^3}{\exp((p_0\left(\frac{a_1}{a_0}\right) - \mu_1)/T_1) \pm 1} \\
      & = \frac{g}{(2\pi)^3} \frac{d^3p_0 \dd V_0}{\exp((p_0 - \mu_0)/T_0) \pm 1} \\
\end{split}
\end{equation}
avec $\mu_0 \equiv \frac{a_1}{a_0} \mu_1$ et $T_0 \equiv \frac{a_1}{a_0} T_1$.   

:::


XXXX TODO: voir fin de https://cmb.wintherscoming.no/milestone1.php 

### Annihilation $e^+ + e^-$ et température du fond diffus de neutrinos

Mais peu après le découplage des neutrinos, lorsque $T < 511\,\keV$ environ $6\,$s après le Big Bang, les électrons et les positrons s'annihilent :
\begin{equation}
    e^- + e^+ \rightarrow \gamma + \gamma  
\end{equation}
ce qui va produire suffisamment d'énergie et d'entropie pour chauffer le gaz de photons et mener à une différence entre la température des photons et ceux des neutrinos découplés $T_\nu < T_\gamma$. L'entropie étant conservée, nous avons avant l'annihilation :
\begin{equation}
  g_{\star S}(T > m_e) = \underbrace{2}_{\gamma} + \frac{7}{8}\left[ \underbrace{2\times 2}_{e^\pm} + \underbrace{2}_{\nu, \bar \nu} \times \underbrace{3}_{e,\mu,\tau} \right] 
\end{equation}
après annihilation : 
\begin{equation}
  g_{\star S}(T<m_e) = 2 + \frac{7}{8}\times 3 \times 2 \left(\frac{T_\nu}{T_\gamma}\right)^3
\end{equation}
En écrivant la conservation de l'entropie, nous avons :
\begin{equation}
  g_{\star S }(T > m_e)\ a^3_\mathrm{before}\ T^3_\mathrm{\gamma,before} = g_{\star S}(T < m_e)\ a^3_\mathrm{after}\ T^3_\mathrm{\gamma,after}
\end{equation}
Or on a  $T_\mathrm{\gamma,before}=T_\mathrm{\nu,before}$ donc :
\begin{align*}
  \left[2+\frac{7}{8}\left(2\times 2 + 2 \times 3  \right)\right] \ a^3_\mathrm{before}\ T^3_\mathrm{\nu,before} & = & \left[ 2 + \frac{7}{8}\times 3 \times 2 \left(\frac{T_\mathrm{\nu,after}}{T_\mathrm{\gamma,after}}\right)^3 \right] \ a^3_\mathrm{after}\ T^3_\mathrm{\gamma,after} \\
  \Leftrightarrow   \left[2+\frac{7}{8}\left(2\times 2 + 2 \times 3  \right)\right] \ a^3_\mathrm{before}\ T^3_\mathrm{\nu,before} & = & \left[ 2 \left(\frac{T_\mathrm{\gamma,after}}{T_\mathrm{\nu,after}}\right)^3  + \frac{7}{8}\times 3 \times 2 \right] \ a^3_\mathrm{after}\ T^3_\mathrm{\nu,after} \\
\end{align*}
Pour les neutrinos découplés, $a_\mathrm{after}T_\mathrm{\nu,after} = a_\mathrm{before}T_\mathrm{\nu,before}$ donc finalement :
\begin{equation}
  \boxed{T_\mathrm{\nu,after}\ = \left(\frac{4}{11}\right)^{1/3}\ T_\mathrm{\gamma,after}}
\end{equation}

Nous constatons donc qu'après l'annihilation $e^\pm$, la température du fond cosmique de neutrinos est effectivement inférieure à la température du CMB. Aujourd'hui, en utilisant $T_0 = 2.725\,\kelvin$, nous trouvons :
\begin{equation}
  T_\nu^0 \approx 1.95\,K = 0.17\,\mathrm{meV}
\end{equation}
Le rapport entre les températures des photons et des neutrinos se retrouve sur la [](#fig:BBN_Tnu) obtenue après un calcul précis de l'évolution du milieu pendant l'annihilation $e^\pm$.

:::{figure} #BBN_Tnu
:name: fig:BBN_Tnu
:align: center
:width: 70%

Evolution de la température des photons et des neutrinos au cours de l'annihilation $e^\pm$ (figure adaptée de {cite}`Weinberg1989` p. 529,540 et originellement de {cite}`Peebles1966`).
:::

Nous pouvons en déduire la densité de neutrinos $n_\nu$ en fonction de $n_\gamma$. Les neutrinos sont des fermions avec 3 saveurs donc si on les suppose sans masse, aujourd'hui leur densité serait : 
\begin{equation}
  n_\nu^0 = \frac{3}{4} \times 3 \times \frac{4}{11} n_\gamma^0
\end{equation}
ce qui donne $112\,\mathrm{cm}^{-3}$ par saveur ($336 \,\mathrm{cm}^{-3}$ au total). Pour la densité d'énergie du fond de neutrinos, nous trouvons :
\begin{equation}
  \rho_\nu = \frac{7}{8}  \frac{g_\nu}{g_\gamma} \left(\frac{T_\nu}{T_\gamma}\right)^4 \rho_\gamma =\frac{7}{8} \times \frac{3 \times 2}{2} \times \left(\frac{4}{11}\right)^{4/3} \rho_\gamma = 0.68\,\rho_\gamma
\end{equation}
et numériquement, on trouve $\Omega_\nu^0 h^2 \approx 1.7\times 10^{-5}$. On en déduit la proportion totale de matière relativiste dans l'Univers (si les neutrinos le sont) :
$$\Omega_r^0 = \Omega_\gamma^0 + \Omega_\nu^0 = \Omega_\gamma^0 \left(1 + \frac{\rho_\nu^0}{\rho_\gamma^0 } \right) = 1.68\,\Omega_\gamma^0$$

Le découplage des neutrinos s'est légèrement superposé à l'annihilation de $e^\pm$. Comme les neutrinos interagissaient encore au moment de l'annihilation, le bruit de fond des neutrinos a été légèrement affecté par l'énergie et l'entropie libérées par l'annihilation de $e^\pm$. Dans la littérature, cela est pris en compte en introduisant un _nombre effectif de neutrinos_ $N_{\mathrm{eff}}$, évaluer numériquement à $3.046$. En tenant compte de cela, le nombre de neutrinos et la densité d'énergie sont :
\begin{equation}
  \begin{split}
n_\nu(T_\gamma) & = \frac{3}{4} N_{\mathrm{eff}}\times \frac{4}{11} n_\gamma(T_\gamma) \\
\rho_\nu(T_\gamma) & = \frac{7}{8} N_{\mathrm{eff}}\times \left(\frac{4}{11}\right)^{4/3} \rho_\gamma(T_\gamma) \\
  \end{split}
\end{equation}

Enfin, les valeurs correctes $g_\star$ et $g_{\star S}$ après l'annihilation $e^\pm$ sont :
\begin{equation}
  \begin{split}
    g_\star & = 2 + \frac{7}{8}\times 2 N_{\mathrm{eff}} \times \left(\frac{4}{11}\right)^{4/3} \approx 3.36 \\
    g_{\star S} & = 2 + \frac{7}{8}\times 2 N_{\mathrm{eff}}\times \left(\frac{4}{11}\right) \approx 3.94 \\    
  \end{split}
\end{equation}


En fait, les neutrinos ont des masses, avec deux conséquences importantes (1) nous ne savons pas s'ils sont encore relativistes aujourd'hui (toutes saveurs confondues) (2) $\Omega_\nu h^2$ est plus grand que la valeur citée ci-dessus. Les expériences observant les oscillations de neutrinos imposent que la somme des masses des neutrinos, notée $\sum_\nu m_\nu$ est supérieure à $60\,\meV$ donc au moins une saveur de neutrino serait non relativiste aujourd'hui si on compare à $T_\nu^0$. Du point de vue de la cosmologie, si on impose de façon très prudente que $\Omega_\nu^0 < 1$ alors on aboutit à une contrainte $\sum_\nu m_\nu < 15\,\eV$, et les relevés cosmologiques regardant l'effondrement gravitationnel des grandes structures de l'Univers imposent $\sum_\nu m_\nu < 0.1\,\eV$ (<doi:10.48550/arXiv.2404.03002>).


### Big Bang Nucleosynthesis (BBN)

Revenons environ $1\,$ms après le Big Bang lorsque le température de l'Univers est de quelques dizaines de MeV. L'Univers est alors essentiellement une soupe chaude de baryons, de photons, d'électrons et de neutrinos sur le point de se découpler des autres particules. On rappelle que le rapport baryon sur photon est une constante  [](#eq:eta) et vaut plus précisément :
$$\label{eq:etaToObh2}
\eta = \frac{n_b}{n_\gamma} = \frac{\Omega_b^0 \rho_c^0}{m_p n^0_\gamma} = 2.73\times 10^{-8}\times \Omega_b^0 h^2 =  6.2 \times 10^{-10}
$$
avec la mesure de $\Omega_b^0 h^2$ sur le spectre de puissance des anisotropies de température du CMB {cite}`Planck2018`. L'Univers continuant son expansion, il se refroidit et les protons et neutrons peuvent fusionner pour former les premiers noyaux atomiques. C'est ce qu'on appelle la _nucléosynthèse primordiale_ (BBN).

#### Rapport neutron sur proton

Le taux de formation de ces noyaux va dépendre d'un paramètre essentiel : le rapport des nombres de neutrons et protons disponibles.

:::{note} Désintégration du neutron libre

Le neutron est instable s'il n'est pas lié à un proton dans un noyau atomique par interaction forte. Il se désintègre selon la réaction :
$$ n \rightarrow p + e^- + \bar{\nu}_e $$
car son énergie de masse est légèrement supérieure à celle du proton :
$$ Q_n = (m_n - m_p)c^2 = 1.29\,\mathrm{MeV}$$
La valeur de la durée de vie moyenne retenue par le Particle Data Group en 2022 est {cite:p}`PDG2022` :
$$\tau_n = 878.4 \pm 0.5\,\mathrm{s}$$ 
soit environ 15 minutes seulement. L'existence des neutrons libres dans l'Univers est donc fortement limitée dans le temps. Dans toute la suite, il faudra vérifier si l'age de l'Univers est petit devant ce temps de désintégration ($t\ll \tau_n$) pour voir s'il est légitime de négliger cette désintégration spontanée.
:::


A $t=1\,$ms, les protons et neutrons sont à l'équilibre thermodynamique l'un avec l'autre via les interactions :
\begin{align}\label{eq:betadecays}
n + \nu_e & \rightleftharpoons &  p + e^-\\
n + e^+ & \rightleftharpoons & p + \bar{\nu}_e
\end{align}
et même celle-ci (moins efficace) :
$$n  \rightleftharpoons  p + e^- + \bar{\nu}_e $$
Tant que ces interactions existent, le rapport neutron sur proton est donné par les densités particulaires à l'équilibre [](#eq:n_nonrel) pour des particules non-relativistes[^mp] :
\begin{align}
    n_n  & = g_n \left(\frac{m_n k_B T}{2\pi \hbar^2}\right)^{3/2} \exp\left(-\frac{(m_nc^2 - \mu_n)}{k_B T}\right) \\
    n_p  & = g_p \left(\frac{m_p k_B T}{2\pi \hbar^2}\right)^{3/2} \exp\left(-\frac{(m_pc^2 - \mu_p)}{k_B T}\right) 
\end{align}
Or $g_n=g_p=2$ et on peut supposer que $\mu_p=\mu_n$ si les potentiels chimiques des électrons et neutrinos sont négligeables. Alors le rapport neutron sur proton se simplifie en :
\begin{equation}\label{eq:np_eq}
\left.\frac{n_n}{n_p}\right\vert_{eq} = \left(\frac{m_n}{m_p}\right)^{3/2} \exp \left(- \frac{(m_n-m_p)c^2}{k_B T} \right) \approx \exp\left(-Q_n / k_B T\right).
\end{equation}
On en déduit que tant que la température est telle que $k_B T \gg Q_n = 1.29\,$MeV, alors il y a autant de neutrons que de protons dans l'Univers. Mais en deçà de $1\,$MeV, la proportion de neutrons chute exponentiellement. Posons $X_n^{eq}$ le rapport neutron sur baryon si les espèces sont à l'équilibre à la température $T$. Alors :
$$ X_n^{eq}(T) =  \frac{n_n^{eq} }{ n_b} = \frac{n_n^{eq}}{n_n^{eq} + n_p^{eq}} =\frac{\exp\left(-Q_n / k_B T\right)}{ 1 + \exp\left(-Q_n / k_B T\right)}.$$
Donc la densité de neutrons devraient être quasi nulle aujourd'hui, mais cette équation est valable seulement *tant que les réactions ont lieu*. En effet, si le taux d'expansion de l'Universe devient comparable ou supérieur au taux d'interaction, alors les réactions s'arrêtent et la proportion neutron sur proton est gelée. Le _mécanisme de gel_ des réactions impliquant des particules massives est important en cosmologie pour comprendre l'abondance des particules massives aujourd'hui.

Pour la réaction $p+e^- \rightarrow \nu_e + n$, le taux d'interaction est donné par ({cite}`KolbTurner` p.90, {cite}`Weinberg1989` p.547 et originellement dans {cite}`Peebles1966`) :
$$
\Gamma_{pe\to \nu n} = \frac{1}{(2\pi)^5}\int f_e(E_e)\left[ 1 - f_\nu(E_\nu)\right]\vert \mathcal{M}\vert^2_{pe\to \nu n}\delta^4(p_p+p_e-p_\nu-p_n) \frac{\dd^3 \vec p_e}{2 E_e}\frac{\dd^3 \vec p_\nu}{2 E_\nu}\frac{\dd^3 \vec p_n}{2 E_n}
$$
avec $f_i(E_i)$ les distributions de Fermi-Dirac des particules $i$ et :
$$\vert \mathcal{M} \vert ^2 \propto G_F^2 ( 1+ 3g_A^2)$$
avec $G_F = 1.16 \times 10^{-5}  \,\GeV^{-2}$ la constante de Fermi et $g_A = 1.26$ le couplage axial-vecteur des nucléons ({cite}`KolbTurner` p.91). Malheureusement ces intégrales doivent être calculées précisément pour obtenir la bonne proportion d'hélium, car on va voir que la proportion de neutron gèle à une température proche de $Q_n$ et $m_e$, ce qui empêche de faire des approximations brutales pour se concentrer sur un régime de haute ou basse énergie. 

:::{tip} Approximation numérique des intégrales
:class: dropdown

Une approximation numérique de la somme des intégrales pour les deux taux d'interaction des réactions [](#eq:betadecays) est {cite}`Bernstein1989` :
\begin{equation}\label{eq:Gnp} 
\Gamma_{np}(x) = \frac{255}{\tau_n x^5}(12+6x+x^2), \quad x= \frac{Q_n}{k_B T}
\end{equation}
Ensuite, pour obtenir l'évolution de la densité de neutrons, une méthode d'intégration numérique est proposée dans {cite}`Dodelson2003` p.67  en définissant la proportion de neutron $X_n = n_n / n_b = n_n / (n_n + n_p)$ :
\begin{equation}
\frac{\dd X_n}{\dd t} = \Gamma_{np} \left[(1-X_n)e^{-Q_n / k_B T} - X_n\right] - \frac{X_n}{\tau_n} 
\end{equation}

:::

Un bilan détaillé de la densité de neutrons permet d'écrire l'équation de Boltzmann suivante :
\begin{align}\label{eq:nn}
\frac{\dd n_n}{\dd t} & = - \Gamma_{n\to p}\,n_n +  \Gamma_{p\to n}\,n_p - 3\frac{\dot a}{a} n_n \\
\frac{\dd n_p}{\dd t} & = \;\;\;\Gamma_{n\to p}\,n_n -  \Gamma_{p\to n}\,n_p - 3\frac{\dot a}{a} n_p
\end{align}
où $\Gamma_{p\to n}=\Gamma_{pe\to \nu n}$ est le taux d'interaction pour la première réaction alors que $\Gamma_{n\to p}$ représente la somme des autres réactions formant des protons. Le dernier terme des équations correspond à la dilution des particules avec l'expansion si leur nombre est conservé dans un volume comobile. Le nombre total de protons et de neutrons est en revanche conservé dans un volume comobile :
$$
\frac{\dd (n_n+n_p)}{\dd t} = - 3\frac{\dot a}{a} (n_n + n_p) \Leftrightarrow \frac{\dd\left[a^3(n_n+n_p)\right]}{\dd t} = 0
$$

Définissons la proportion de neutrons $X_n = n_n / n_b = n_n / (n_n + n_p)$. La proportion de protons $X_p$ s'en déduit par $X_p=1-X_n$. L'équation différentielle pour la densité de neutrons se réécrit :
$$
\frac{\dd n_n}{\dd t}= \frac{\dd X_n(n_n+n_p)}{\dd t} =  (n_n+n_p)\frac{\dd X_n}{\dd t} - 3\frac{\dot a}{a} (n_n + n_p) X_n
$$
soit :
\begin{equation}\label{eq:Xn}
\frac{\dd X_n}{\dd t} = - \Gamma_{n\to p}\,X_n + \Gamma_{p\to n}\,(1-X_n) 
\end{equation}

Commençons par comparer le taux de disparition des neutrons au taux d'expansion de l'Univers ([](#fig:BBN_Gnp)).
Après intégration numérique, on observe que $\Gamma_{n\to p}$ décroit en fonction du temps et converge vers un plateau correspondant à l'inverse du temps de demi vie du neutron $\tau_n^{-1}$ (indépendant de l'expansion). Il est supérieur au taux $\Gamma_{p\to n}$ donc c'est celui-qui compte dans le mécanisme de gel. Le taux $\Gamma_{n\to p}$ est comparable au taux d'expansion $H$ à la température : 
$$
\boxed{T_{\mathrm{freeze}}= 0.7\,\MeV = 8\times 10^9 \,\kelvin}
$$
C'est la température de gel des neutrons. 


:::{figure} #BBN_Gnp
:name: fig:BBN_Gnp
:align: center
:width: 70%

Comparaison des taux de réaction $\Gamma_{n\to p}(T)$ et du taux d'expansion $H(T)$. La température de gel de la densité des neutrons est définie par le croisement des courbes. Le taux de réaction $\Gamma_{n\to p}(T)$ atteint un plateau correspondant au taux de désintégration du neutron, indépendant de l'expansion. La région grisée correspond à la formation des noyaux atomiques: il n'y a plus de neutrons libres à ce stade donc les courbes ne sont plus valables, mais cela met en évidence le plateau de $\Gamma_{n\to p}(T)$.
:::

Étudions maintenant la densité relative de neutrons $X_n(t)$. Après intégration numérique avec comme condition initiale :
$$
X_n(t \approx 1\,\mathrm{ms}) = X_n^{eq}(t\approx 1\,\mathrm{ms}), \quad g_*=10.75
$$
on obtient la [](#fig:BBN_Xn). _Si la désintégration spontanée du neutron est omise_ (courbe tiretée), la fraction de neutron converge vers $X_n^{\mathrm{frozen}} = 0.15$, soit :
$$
\frac{n_n}{n_p}(100\,\keV) = \frac{X_n(100\,\keV)}{1-X_n(100\,\keV)} = 0.17 \sim 1/6
$$
i.e. 1 neutron pour 6 protons[^Tfreeze].

:::{figure} #BBN_Xn
:name: fig:BBN_Xn
:align: center
:width: 70%

Fraction de neutrons $X_n$ en fonction du temps calculé par l'équation [](#eq:Xn) (trait plein). Si la désintégration du neutron est négligée, alors on obtient la courbe en pointillé ($\tau \to \infty$). La distribution d'équilibre $\left.n_n/n_p\right\vert_{eq}$ donne la proportion de neutrons si les réactions ne sont pas gelées par l'expansion de l'Univers.
:::


#### Synthèse du deutérium

Après la température de gel des neutrons, la proportion de neutrons et de protons est donc stable, à ceci près qu'un neutron libre est instable avec un temps de désintégration d'environ 15 minutes. Toutefois, si la température descend suffisamment, protons et neutrons peuvent se combiner pour former le plus léger des noyaux atomiques par interaction forte, le deutérium $\mathrm{D}$, via la réaction :
\begin{align}
p + n \rightleftharpoons \mathrm{D} + \gamma
\end{align}
La question est donc: quand a lieu la formation du deutérium et combien y a-t-il de neutrons restants à cet instant?

Le deutérium possède une énergie de liaison :
$$
B_{\mathrm{D}} = (m_n + m_p - m_\mathrm{D})c^2 = 2.22\,\mathrm{MeV}
$$
Il est donc plus favorable de former des atomes de deuterium que de garder des protons et des neutrons séparés. A l'équilibre, 
\begin{align}
\frac{n_\mathrm{D}}{n_pn_n} & = \frac{g_\mathrm{D}}{g_p g_n} \left(\frac{k_B T}{2\pi \hbar^2}\right)^{-3/2}\left(\frac{m_\mathrm{D}}{m_p m_n}\right)^{3/2} \exp \left( \frac{(m_p+m_n-m_\mathrm{D})c^2}{k_B T} \right) \\
 & \approx 6 \left(\frac{m_n k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_\mathrm{D}}{k_B T}\right)
\end{align}
avec $g_\mathrm{D}=3$ (car le deutérium est un boson massif de spin 1), $g_n=g_p=2$ et $\mu_p + \mu_n = \mu_D + \mu_\gamma = \mu_D$  ({cite}`ryden2017` p.219).

On définit la température de démarrage de la nucléosynthèse $T_{\mathrm{nuc}}$ pour laquelle la moitié des neutrons ont été consommés pour former du deutérium, c'est-à-dire lorsque $n_\mathrm{D}=n_n$. Le rapport deutérium sur neutron s'écrit :
\begin{equation}\label{eq:XD}
\frac{n_\mathrm{D}}{n_n} \approx 6 n_p \left(\frac{m_n k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_D}{k_B T}\right)
\end{equation}
En supposant que de toute façon le nombre de protons va peu diminuer au cours de la formation du deutérium, on peut estimer que la densité de protons à $T_{\mathrm{nuc}}$ est environ :
$$
n_p \approx (1-X_n(T_{\mathrm{nuc}})) n_b = (1-X_n(T_{\mathrm{nuc}})) \eta n_\gamma(T_{\mathrm{nuc}}) 
$$
On en déduit alors la température $T_{\mathrm{nuc}}$ par l'inversion numérique de l'équation :
$$ 
6 (1-X_n(T_{\mathrm{nuc}})) \eta n_\gamma(T_{\mathrm{nuc}}) \left(\frac{m_n k_B T_{\mathrm{nuc}}}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_D}{k_B T_{\mathrm{nuc}}}\right) = 1 
$$
On en déduit :
$$
\boxed{T_{\mathrm{nuc}}  = 70\,\keV = 8 \times 10^8\,\kelvin}
$$
soit $t_{\mathrm{nuc}} \approx 280\,$s après le Big Bang, avec $g_* = 3.36$ dorénavant puisque l'Univers possède une température inférieure à $m_e$. A ce moment précis, la fraction de neutrons encore présente est environ de : 
$$\boxed{\frac{n_n}{n_p}(T_{\mathrm{nuc}}) = \frac{X_n(T_{\mathrm{nuc}})}{1-X_n(T_{\mathrm{nuc}})} = 0.14 \sim 1/7}$$
La désintégration spontanée du neutron est donc notable à cette échelle de temps.

#### Synthèse de l'hélium 4

La formation des noyaux d'hélium n'est possible que via la fusion de noyaux de deutérium :
\begin{align}
p + n &\rightarrow &\mathrm{D} + \gamma \\
\mathrm{D} + p &\rightarrow &^3\mathrm{He} + \gamma \\
\mathrm{D} + \mathrm{D} &\rightarrow& ^4\mathrm{He} + \gamma 
\end{align}
car il est beaucoup plus improbable que deux protons et deux neutrons se rencontrent par hasard pour former un noyau d'hélium. Or l'énergie de liaison de l'hélium 4 est bien supérieure à celle du deutérium ($B_{\mathrm{He}} = 28.3\,\MeV$) donc c'est sa formation qui sera favorisée. On peut donc supposer que tous les neutrons disponibles à $t_\mathrm{nuc}$ vont terminer dans un noyau d'hélium. 

Comme deux neutrons vont dans un noyau d'hélium 4, le nombre maximum de noyaux d'hélium formables est égal à la moitié des neutrons disponibles (qu'ils soient libres ou dans les noyaux de deutérium). On en déduit l'abondance en hélium 4 en nombre de noyaux comme étant :
$$
n_{\mathrm{He}} = \frac{1}{2} n_n(t_\mathrm{nuc})
$$
En terme de masse, l'abondance d'hélium 4 dans l'Univers à la fin de la nucléosynthèse primordiale peut être au maximum de ([](#fig:BBN_Yp)):
\begin{equation}
\boxed{Y_p \equiv \frac{\rho(^4\mathrm{He})}{\rho_b} = \frac{4n_\mathrm{He}}{n_n + n_p} \approx 25\%}
\end{equation}
le reste étant de l'hydrogène (à $75\%$ en masse).

:::{figure} #BBN_Yp
:name: fig:BBN_Yp
:align: center
:width: 70%

Fraction massique des différentes noyaux légers dans l'Univers au cours du temps, calculée via le modèle simple détaillé dans ce chapitre.
:::

Des calculs plus précis montrent que la synthèse des noyaux atomiques démarre environ 3 minutes après le Big Bang et se termine 20 minutes après, et prédisent $Y_p$ autour de 24%, car une petite fraction des neutrons demeurent dans d'autres noyaux légers après $t_{\mathrm{nuc}}$ comme le deutérium, le lithium, etc ([](#fig:BBN)). Ces prédictions sont en bon accord avec les mesures (voir [](#fig:BBN_mes)). Avant la découverte des anisotropies de température du CMB dans les années 2000, la comparaison de la mesure des abondances des éléments légers (par l'observation du milieu interstellaire, des galaxies, etc: bandes grises horizontales de la [](#fig:BBN_mes)) avec ces prédictions était un moyen de mesurer $\eta$ et donc $\Omega_b^0h^2$ (voir équation [](#eq:etaToObh2)). La mesure de $\Omega_b^0h^2$ par les anisotropies de température (bande grise verticale  de la [](#fig:BBN_mes)) est plus précise mais en accord avec les prédictions de la BBN ce qui montre la robustesse du modèle standard de la cosmologie (sauf pour le lithium où un désaccord persiste).

Dans tous les cas, avec uniquement le mécanisme stellaire de fusion de l'hydrogène au coeur des étoiles en hélium (et ensuite la fusion de l'hélium en carbone, oxygène, etc), il n'est pas possible d'expliquer une telle abondance de l'hélium dans l'Univers. Seul le passage par un plasma chaud à des centaines de millions de degrés contenant des neutrons libres, même au plus 20 minutes en se refroidissant, permet d'expliquer les $24\%$ d'hélium présents dans l'Univers. C'est donc une preuve importante de l'existence d'un état où l'Univers était un plasma chaud et dense pendant au moins quelques minutes. 

:::{figure} ../../images/bbn.png
:width: 80%
:align: center
:label: fig:BBN

Synthèse des éléments légers dans l'Univers primordial (d'après {cite}`PospelovBBN2010`).
:::


:::{figure} ../../images/bbn_Yp.png
:width: 80%
:align: center
:label: fig:BBN_mes

Comparaison entre les prédictions théoriques pour les abondances des noyaux légers (bandes colorées) et les mesures (bandes grises) (d'après {cite}`Baumann`).
:::

:::{note} Au-delà de l'hélium

Il est très difficile de former des noyaux au-delà de l'hélium car ce dernier possède une énergie de liaison particulièrement supérieure aux atomes immédiatement plus lourds. En particulier il n'existe pas de noyaux stables avec $A=5$ nucléons donc pour aller au-delà de l'hélium il ne suffit pas d'absorber un des nombreux protons présents.

Aussi, un peu de lithium peut se former via les réactions :
$$^4\mathrm{He} + \mathrm{D} \rightleftharpoons\ \ ^6\mathrm{Li} + \gamma $$

```{figure} ../../images/Binding_energy_curve.svg
:width: 80%
:align: center
:label: fig:binding_energy

Energie de liaison par nucléons (source: Wikipedia <wiki:Nuclear_binding_energy>).
```
:::

### Recombinaison

La recombinaison se déroule en deux étapes comme nous allons le voir. D'abord il y a la formation des atomes d'hydrogène puis le découplage des électrons libres restants et des photons. A ce moment là, le plasma se transforme en gaz d'hydrogène et d'hélium (plus un peu de lithium etc) neutre. Après la recombinaison, les photons du bain thermique sont libres de se propager dans l'Univers puisque le milieu est (quasi) neutre. Cette première lumière correspond au fond diffus cosmologique et nous renseigne sur l'état de l'Univers jeune et la physique qui s'y est déroulée avant (et après). 

#### Formation des atomes d'hydrogène

La formation des atomes d'hydrogène se déroule par la réaction :
$$ p + e^- \rightleftharpoons \mathrm{H} + \gamma$$
et on rappelle que l'énergie de liaison de l'hydrogène vaut $B_\mathrm{H} = 13.6\,\eV$. Une rapide approximation nous donnerait que la température à laquelle a eu lieu la recombinaison est $T_\mathrm{rec} \approx B_\mathrm{H} / k_B \approx 1.5 \times 10^5\,$K, mais ce serait oublier qu'avec un milliard de photons pour un baryon, même à des températures plus basses l'Univers contient encore énormément de photons d'énergie assez haute pour ioniser les atomes d'hydrogène (queue de la distribution du corps noir). Ce qu'il faut c'est donc trouver la température pour laquelle l'intégrale de la distribution de corps à des énergies supérieures à $13.6\,\eV$ donne une densité de photons comparable à $n_b = \eta n_\gamma$. Le rapport $\eta$ est donc un paramètre important qui doit intervenir dans l'estimation de la température à la recombinaison.

Une meilleure estimation doit donc reposer au moins sur le rapport baryon sur photon $\eta$ et $B_\mathrm{H}$. Comme pour l'abondance du deutérium, à l'équilibre on peut décrire :
\begin{align}
\frac{n_\mathrm{H}}{n_pn_e} & =\frac{g_\mathrm{H}}{g_p g_e} \left(\frac{k_B T}{2\pi \hbar^2}\right)^{-3/2}\left(\frac{m_\mathrm{H}}{m_p m_e}\right)^{3/2} \exp \left(\frac{(m_p+m_e-m_\mathrm{H})c^2}{k_B T} \right) \\
& \approx \left(\frac{m_e k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_\mathrm{H}}{k_B T}\right)
\end{align}
avec $g_\mathrm{H}=4$[^spinH] et $g_p=g_e=2$. C'est *l'équation de Saha*. Posons $X_e$ la fraction d'électron libre dans le plasma primordial :
$$X_e = \frac{n_e}{n_b}$$
Par des arguments de neutralité électrique et de conservation du nombre de particules, on a aussi :
$$n_e\approx n_p,\quad X_e=\frac{n_p}{n_b}\approx  \frac{n_p}{n_p + n_\mathrm{H}} $$
en supposant qu'il n'y a que de l'hydrogène pour simplifier les calculs (pas d'hélium[^Heneglect]). Par conséquent, on a :
\begin{equation}
\frac{1-X_e}{X_e} = n_p \left(\frac{m_e k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_\mathrm{H}}{k_B T}\right)
\end{equation}
et simplement :
$$n_p \approx X_e \eta  n_\gamma = \eta X_e  \frac{2\zeta(3)}{\pi^2}\left(\frac{k_B T}{\hbar c}\right)^3 $$
donc :
\begin{equation}
\frac{1-X_e}{X_e^2} = \frac{2\zeta(3)}{\pi^2}\eta \left(2\pi\frac{k_B T}{m_e c^2}\right)^{3/2}  \exp\left(\frac{B_\mathrm{H}}{k_B T}\right) \equiv a_\mathrm{H}
\end{equation}
On a une équation du second degré en $X_e$ dont la solution est ({cite}`ryden2017` p.192) :
$$X_e = \frac{-1 + \sqrt{1+ 4a_\mathrm{H}}}{2a_\mathrm{H}}$$
On définit le moment de la recombinaison comme celui où le milieu est à moitié ionisé soit $X_e = 1/2$, alors la température du découplage est donnée par {cite:p}`ryden2017` :
$$k_B T_{\mathrm{rec}} = 0.32\,\mathrm{eV} = \frac{B_\mathrm{H}}{42}$$
$$ \boxed{T_{\mathrm{rec}} = 3760\,\mathrm{K},\quad z_\mathrm{rec} = 1378}$$
soit quand l'Univers avait $t_\mathrm{rec} = 250\,000$ ans et alors que son évolution est dorénavant dominée par son contenu en matière. D'après la [](#fig:saha_Xe), on voit toutefois que la recombinaison s'étend globalement entre les redshift 1200 et 1600, ce qui correspond tout de même à environ $70\,000$ ans, ce n'est donc pas un processus instantané. 

:::{figure} #saha_Xe
:name: fig:saha_Xe
:width: 70%

Fraction d'ionisation $X_e$ en fonction du redshift pendant la recombinaison.
:::

#### Photon decoupling

:::{figure} #rates_decoupling
:name: fig:rates_decoupling
:width: 70%

Comparaison entre le taux d'interaction $\Gamma_\gamma$ et le taux d'expansion $H$ en fonction du redshift.
:::

Pendant encore un certain temps après $z_{\mathrm{rec}}$, les photons restent couplés à la petite fraction d'électrons libres par la diffusion Thomson :
$$ e^- + \gamma \rightleftharpoons e^- + \gamma $$
Le taux d'interaction est donné par (voir équation [](#eq:lpm_thomson)) :
$$\Gamma_\gamma = n_e \sigma_T c = n_b X_e \sigma_T c=  \frac{2\zeta(3)}{\pi^2} \eta  \sigma_T c\left(\frac{k_B T}{\hbar c}\right)^3$$
avec la section efficace de la diffusion Thomson :
$$
\sigma_T = 0.665\,\mathrm{barns} = 6.65\times 10^{-29}\,\mathrm{m}^2
$$
Le découplage a lieu lorsque ce taux d'interaction devient petit devant le taux d'expansion de l'Univers ([](#fig:rates_decoupling)), soit :
$$
\Gamma_\gamma(T_\mathrm{dec}) = H(T_\mathrm{dec})
$$
L'Univers étant alors dominé par la matière ($z<3000$), on a :
$$
H(T_\mathrm{dec}) = H_0 \sqrt{\Omega_m^0(1+z)^3} = H_0 \sqrt{\Omega_m^0} \left(\frac{T_\mathrm{dec}}{T_0}\right)^{3/2}
$$
On aboutit à :
\begin{equation}
X_e(T_\mathrm{dec}) (k_B T_\mathrm{dec})^{3/2} \approx  \frac{\pi^2}{2\zeta(3)}\frac{H_0 \sqrt{\Omega_m^0} } {\eta  \sigma_T c} \left(\frac{k_B T_0}{\hbar c}\right)^{-3/2}
\end{equation}
Par une résolution numérique, on obtient :
$$
\boxed{T_{\mathrm{dec}} = 0.26\,\eV = 3055\,\kelvin, \quad z_{\mathrm{dec}}\sim 1100,  \quad t_{\mathrm{dec}}=370\,000\,\mathrm{ans}}
$$

:::{tip} Libre parcours moyen des photons
:class:dropdown

Une autre façon de voir le découplage entre photon et matière et donc le moment où l'Univers devient transparent, est de regarder le libre parcours moyen des photons $\ell_T(z) = 1/(\sigma_T n_e(z)c)$. Loin dans le passé de l'Univers, celui-ci était opaque mais le libre parcours moyen des photons pouvait tout de même être de l'ordre de quelques années-lumières. Après le découplage, celui-ci devient supérieur à la taille typique de l'Univers. 

```{figure} #photon_mean_free_path
:name: fig:photon_mean_free_path
:width: 70%

Comparaison entre le temps de libre parcours moyen des photons $\tau_T$ et le temps de Hubble $1/H(z)$.
```

:::

Le fond diffus cosmologique est donc un rayonnement de corps noir qui a été libéré environ $370\,000\,$ans après le Big Bang, quand l'Univers n'était quasiment plus ionisé puisque $X_e(T_{\mathrm{dec}}) = 6\times 10^{-3}$. 

:::{attention} Les trois piliers du Big Bang

**L'expansion de l'Univers, une abondance de $24\%$ d'hélium, et l'existence d'un fond diffus cosmologique micro-onde sont les trois piliers qui assoient la théorie du Big Bang.**

Toute théorie alternative doit expliquer ces trois observations.

:::


[^baryons]: les hadrons se scindent en deux familles : les mésons (2 quarks) et les baryons (3 quarks). on rappelle que parmi les baryons seuls les protons sont stables. Les neutrons liés dans les noyaux atomiques sont stables, mais libres ils se désintègrent en proton avec un temps de demie vie de 15 minutes. Les mésons sont tous instables avec des temps de demie vie plus courts que $10^{-7}\,$s. Les électrons sont 2000 fois plus légers que les protons. L'essentiel de la masse de la matière dite "ordinaire" est donc contenue dans les noyaux atomiques d'où le raccourci "matière baryonique".
[^mp]: on rappelle que les masses des protons et neutrons sont d'environ $1\,\GeV$.
[^neutrality]: puisque la charge électrique est associée aux forces de Coulomb et que l'expansion de l'univers n'est gouvernée que par les forces gravitationnelles, l'univers doit être globalement neutre.
[^Sconst]: stricto sensus une constante d'intégration entropique $S_0$ doit apparaître mais celle-ci est nulle en vertu du troisième principe de la thermodynamique.
[^Tfreeze]: dans un certain nombre de référence, ont trouve comme température de gel des neutrons $T_{\mathrm{freeze}} \approx 0.8\,\MeV$ ce qui correspond aussi à 1 neutron pour 6 protons si on suit la distribution d'équilibre [](#eq:np_eq) mais en admettant que cette température est un ordre de grandeur bien trouvé pour que ça marche à la fin.
[^spinH]: un atome d'hydrogène peut avoir un spin 0 (spins inversés) ou 1 (spins alginés) donc 4 degrés de liberté internes.
[^Heneglect]: avec un neutron pour 7 protons, $n_\mathrm{He} = n_\mathrm{H} / 12$ donc en nombre plus de $90\%$ des baryons sont des protons. 
