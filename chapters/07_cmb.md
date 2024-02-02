---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
  '\kelvin': '\mathrm{K}'
  '\GeV': '\mathrm{GeV}'
  '\MeV': '\mathrm{MeV}'
---

Histoire thermique de l'Univers
===============================

L'expansion cosmique réduit la quantité de mouvement des particules d'un facteur $\propto
a^{-1}$ et la densité des particules d'un autre $a^{-3}$. Dans les premiers temps, l'Univers était donc un état chaud et dense, dans lequel les particules pouvaient
échanger de l'énergie et de la quantité de mouvement de manière assez efficace, en d'autres termes, 
une sorte de plasma à température élevée en équilibre thermique (ou proche de l'équilibre thermique).


:::{figure} ../images/cmb_cn.jpg
:name: fig:distances_croquis
:align: center
:width: 60%

Ajustement d'un modèle de corps noir sur les diverses données mesurant le flux venant du fond diffus cosmologique.
:::

Le rayonnement cosmologique est probablement la preuve la plus directe de cet état de fait : l'Univers est rempli d'un gaz de photons micro-ondes suivant un spectre du corps noir (<wiki:Planck's_law>) :
\begin{equation}
  I_\nu(\nu, T_0) = \frac{2 h \nu^3}{c^2}\frac{1}{\exp(h\nu/k_B T_0) - 1}
\end{equation}
avec $T_0 = 2.726\,\kelvin$. 

Les photons du CMB ne sont _pas_ en équilibre thermique avec quoi que ce soit d'autres aujourd'hui. En effet, l'équilibre thermique implique des échanges fréquents d'énergie et de momentum par le biais de collisions entre particules, alors que l'immense majorité des photons du CMB n'ont jamais été en contact avec des particules. 
Cependant, cette absence d'interactions a préservé la forme originale du spectre du CMB, qui n'a été affecté que par le décalage vers le rouge. Un photon détecté à la fréquence $\nu$ a été émis à l'origine à la fréquence $\nu(1+z)$. En d'autres termes, le spectre d'origine était le suivant {cite:p}`Condon2018` :
\begin{equation}
I_\nu(\nu, T_0) = \frac{2 h \nu^3}{c^2}\frac{1}{\exp(h\nu/(1+z)k_B T_0) - 1}
\end{equation}
c'est-à-dire toujours une forme de corps noir, avec une température $(1+z) T_0$.  Ceci suggère que les photons du CMB étaient en équilibre thermique lorsqu'ils ont été émis, et, plus généralement, que le plasma primordial chaud était en équilibre thermique.

Description de l'Univers primordial
--------------------------

### Ordres de grandeurs

Remontons bien au-delà du décalage vers le rouge de la dernière surface de diffusion, et considérons l'Univers à, disons, $z \sim 10 000$. Que pouvons-nous en dire ?


#### Taux d'expansion

La valeur du paramètre de Hubble peut être déduite de l'équation de Friedmann :
\begin{equation}
  H(z) = H_0 \left( \Omega_m^0(1+z)^3 + \Omega_r^0 (1+z)^4 + \Omega_\Lambda^0\right)^{1/2}
\end{equation}
Prenons les valeurs canoniques $\Omega_m^0 = 0.3$, $\Omega_\Lambda^0 = 0.7$ et $w = -1$ et $\Omega_r^0 \sim 9 \times 10^{-5}$ pour la densité de matière relativiste (photons et neutrinos). A $z \sim 10\,000$, cela donne  :
\begin{equation}
  H(z) \approx 10^6 \times H_0
\end{equation}
L'expansion de l'Univers était beaucoup plus rapide qu'aujourd'hui !

#### Température

Pour un gaz de photons, nous savons que :
\begin{equation}
\epsilon_\gamma a^4 = cste
\end{equation}
Or, à l'équilibre thermique, nous avons la loi de Stefan-Boltzmann :
\begin{equation}
\epsilon_\gamma = \frac{4 \sigma_S T^4}{c}\text{ avec } \sigma_S = \frac{2 \pi^5 k_B^4}{15 h^3 c^2}
\end{equation}
La température d'équilibre des photons $T$ évolue donc comme suit :
\begin{equation}
T \propto a^{-1}
\end{equation}
La température des photons $T$ peut donc être utilisée comme paramètre temporel comme $a$ ou $z$ si $T$ est isotrope.

Les photons se sont découplés de la matière à $z_{\mathrm{dec}} \approx 1090$ et forment maintenant ce que l'on appelle le fond diffus cosmologique. Quelle était la température $T_{\mathrm{dec}}$ des photons au moment du découplage ?
\begin{equation}
a_{\mathrm{dec}} T_{\mathrm{dec}} = a_0 T_0 \Rightarrow T_{\mathrm{dec}} = (1+z_{\mathrm{dec}}) T_0 = 2972\,\kelvin
\end{equation}


#### Densités


Nous pouvons maintenant calculer la contribution actuelle des photons du CMB à la densité critique de l'univers en utilisant la température du corps noir :
\begin{equation}
\Omega_{\gamma}^0= {\epsilon_\gamma^0 \over c^2 \rho^0_c}= {4 \sigma T_0^4 \over c^3}{8 \pi G_N \over 3 H_0^2} \sim 5\times 10^{-5}
\end{equation}
Comme nous pouvons le voir, le CMB contribue à environ la moitié de la valeur estimée de $\Omega_r^0 \sim 9 \times 10^{-5}$. D'autres particules ultra relativistes telles que les neutrinos contribuent à la partie restante de $\Omega_r^0$.


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

Concentrons-nous maintenant sur les propriétés des photons.  Nous savons que $T_0 = T_\gamma \propto a^{-1}$, donc :
\begin{equation}
  T_\gamma(z=10\,000) \approx 2.726\times 10^{4}\,\kelvin
\end{equation}
L'énergie moyenne des photons du CMB est :
\begin{equation}
  k_B T_\gamma(z) = k_B T_0 (1+z) \approx 2.34\,\mathrm{eV}
\end{equation}
Par analyze dimensionnelle, la densité des photons à un redshift z vaut, à des facteurs numériques près que nous verrons plus loin :
\begin{equation}
  n_\gamma(z) \sim \frac{(k_B T_0 (1+z))^3}{c^3 \hbar^3}\sim  10^{21}\ \gamma / \mathrm{m^3}
\end{equation}

#### Baryons

Evaluons maintenant la densité de baryons (particules avec 3 quarks comme les protons et neutrons) à $z \sim 10\,000$. La densité de baryons est aujourd'hui $\Omega_b^0 = 0.048$. Avec une densité critique de $\rho_c^0 \sim 6\,m_p / m^{3}$,  cela donne environ $n_b^0 \approx 0.3\,\mathrm{baryons / m^{3}}$ aujourd'hui, puis à $z \sim 10\,000$ :
\begin{equation}
  n_b(z) \approx \Omega_b^0 \rho_c^0 (1+z)^3 \approx 3\times 10^{11} \ \mathrm{baryons} /  \mathrm{m^3}
\end{equation}
L'univers primordial est donc largement dominé par les photons en terme de densité de particules :
\begin{equation}\label{eq:eta}
\eta= \frac{n_b(z)}{n_\gamma(z)} \sim \frac{\Omega_b^0 \rho_c^0 c^3 \hbar^3}{(k_B T_0)^3} \sim 10^{-9}
\end{equation}


(lpm_photons)=
#### Libre parcours moyen des photons

Enfin, on peut s'interroger sur le libre parcours moyen des photons. Les photons interagissent préférentiellement avec les électrons par diffusion Thomson $e^- + \gamma \rightarrow e^- + \gamma$ et une bonne approximation du libre parcours moyen des photons est donnée par :
\begin{equation}\label{eq:lpm_thomson}
 l_{T} =\frac{1}{\sigma_T n_e}
\end{equation}
où $\sigma_T$ est la section efficace de diffusion de Thomson ($6.6529\times 10^{-29}\ \mathrm{m^2}$). Pour la densité électronique, considérons que l'Univers étant neutre, il y a un électron pour chaque proton donc $n_e = n_p \approx 0.3\,\mathrm{m^{-3}}$. Le temps typique entre deux interactions $\tau_T$ est alors :
\begin{equation}
 \tau_T = \frac{l_T}{c} = \frac{1}{\sigma_T n_e c} \approx 5\times 10^{12}\,\mathrm{yr} \gg t_H = \frac{1}{H_0}
\end{equation}
aujourd'hui et à l'époque :
\begin{equation}
\tau_T=  \frac{1}{\sigma_T n_e(1+z)^3 c} \approx 5\,\mathrm{yr} \ll \frac{1}{H(z)} \sim 10^{-6} t_H
\end{equation}


### Scénario du Big Bang

L'Univers à $z \approx 10\,000$ était beaucoup plus chaud et plus dense. 
La densité du nombre de photons était significativement plus grande que celle des baryons, comme aujourd'hui. 
Enfin, les interactions entre photons et particules chargées étaient beaucoup plus fréquentes (plusieurs par temps de Hubble), il est donc tout à fait logique de considérer l'Univers comme un fluide en équilibre thermique.

A partir de cette description, nous pouvons esquisser un scénario d'évolution du plasma primordial en cataloguant les différents phénomènes physiques qui peuvent se produire lorsque celui-ci se refroidit. En voici un résumé non exhaustif.

Tout d'abord, au sortir de l'inflation (environ $10^{-34}\,$s après le Big Bang), il y a dû y avoir eu une phrase dite de _baryogénèse_, où l'ensemble des baryons sont créés avec un léger avantage pour la matière face à l'antimatière. En dessous d'une température de $100\,\GeV$ environ ($t \sim 20\,$ps), la transition de phrase électrofaible a lieu, donnant la masse aux particules et faisant apparaître les bosons de jauge Z, W$^\pm$. Sous $150\,\MeV$ ($t\sim 20\,\mathrm{\mu s}$, c'est la transition de phase QCD :  l'interaction forte prend le dessus sur les effets thermiques. Les quarks et gluons coagulent pour former des baryons (trois quarks) et des mésons (2 quarks). Puis, $6\,\mathrm{s}$ plus tard, électrons et positrons s'annihilent car la température du bain de photons passe sous la masse de l'électron $T < 500\,\mathrm{keV}$. Pendant les trois minutes de l'Univers ($T > 100\,\mathrm{keV}$), les noyaux des éléments légers sont formés. Au bout de 380\,000 ans, les électrons se lient aux noyaux atomiques ($e^- + p \rightarrow \mathrm{H} + \gamma$), c'est la _recombinaison_, et les photons se découplent de la matière ($\tau_T \ll 1/H)$. Libre de se propager, ces photons forment le fond diffus cosmologique et fournissent une photographie du plasma primordial à la fin de la recombinaison.


Thermodynamique statistique à l'équilibre
-------------------------------

Nous allons aborder maintenant une description pus fine de ce qu'il s'est passé dans l'Univers primordial, en particulier comment les différentes particules ont interagi entre elles.

### Description statistique

Nous modélisons les fluides de l'Univers comme un gaz de particules interagissant faiblement. Nous utilisons le formalisme de la physique statistique et décrivons le gaz par les positions et les moments de toutes ses particules, définies sur l'espace $\{\vec{x}, \vec{p}\}$. 

Les états d'énergie $E$ dans un gaz de particules _à l'équilibre thermodynamique_ suivent une fonction de distribution statistique $f(\vec{x}, \vec{p})$
En cosmologie, en raison de l'homogénéité de l'Univers, $f$ ne peut pas varier en fonction de $\vec{x}$. De plus, en raison de l'isotropie, $f$ ne peut dépendre que de la norme de la quantité de mouvement  $p \equiv \Vert \vec{p}\Vert$.

Muni des fonctions de distribution, nous pouvons en déduire des propriétés macroscopiques du gaz en évaluant la probabilité d'occupation des états du système.
La mécanique quantique nous apprend que la densité des états dans l'espace est finie. En effet, considérons une boîte de taille $L$, avec des conditions périodiques et résolvons l'équation de Schrodinger, nous obtenons que les valeurs possibles de la quantité de mouvement sont :
\begin{equation}
  \vec{p} = \frac{h}{L}\left(n_x \vec{e}_x + n_y \vec{e}_y + n_z \vec{e}_z\right), \ \ \ n_i = 0, \pm 1, \pm 2, \ldots
\end{equation}
où $\vec{e}_x, \vec{e}_y$ et $\vec{e}_z$ sont les vecteurs unitaires et $h$ est la constante de Planck. En conséquence, dans l'espace des quantités de mouvement, il y un état par cube élémentaire de volume $h^3/L^3$. La densité d'état dans l'espace des quantités de mouvement est donc $L^3/h^3$ :
Ensuite, il n'y a qu'une particule dans la boite quantique donc un seul état de position : dans l'espace des positions la densité d'état est de $1/L^3$. Au total, la densité d'état dans l'espace des phases est :
\begin{equation}
  \frac{1}{h^3} = \frac{1}{(2\pi\hbar)^3}
\end{equation}
 La densité d'état est donc indépendante du volume. Elle reste la même pour un système arbitrairement grand. 

Les propriétés macroscopiques (densité de nombre, densité d'énergie, pression) se déduisent de la probabilité d'occupation des états $f(\vec{x}, \vec{p}, t)$ et de la densité d'état de l'espace des phases.
La densité volumique de particules d'impulsion comprise entre $p$  et $p+\dd p$ est par exemple donné par :
\begin{equation}\label{eqn:fweights}
 n(p) = \frac{1}{(2\pi\hbar)^3} f(p) \dd^3\mathbf{p}
\end{equation}

La densité volumique particulaire du gaz est:
\begin{equation}\label{eqn:number_density_general}
  \boxed{n = \frac{1}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p)}
\end{equation}

Pour la densité d'énergie, il suffit de faire la somme des énergies des particules pondérées la fonction de distribution : 
\begin{equation}\label{eqn:energy_density_general}  
  \boxed{\epsilon = \rho c^2 = \frac{1}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p) \sqrt{p^2c^2 + m^2 c^4}}
\end{equation}

:::{note}
Nous avons supposé ici que nous pouvions ignorer les énergies d'interaction
entre les particules (c'est-à-dire que nous avons affaire à un gaz de particules
particules interagissant faiblement). Dans ce cas, l'énergie est donnée par : $E(p) =
\sqrt{p^2 c^2 + m^2 c^4}$ et les états disponibles sont en effet les états de particules libres décrits ci-dessus.
décrits ci-dessus.
:::

Nous pouvons obtenir de la même manière la pression du gaz : 
\begin{equation}\label{eqn:pression_generale}
  \boxed{P = \frac{1}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p) \frac{p^2}{3E}}
\end{equation}


Au final, le tenseur énergie impulsion pour un ensemble de particules quantiques peut s'écrire :
\begin{equation}
\boxed{T^{\mu\nu}=\frac{1}{(2\pi\hbar)^3}\int{\dd^3\mathbf{p} f(p) \frac{p^\mu p^\nu}{p^0}}}
\end{equation}

:::{note} Pourquoi $p^2/3E$ ?

Considérons un élément de surface $\delta A$. Nous notons $\hat{n}$ son vecteur unitaire. Les particules de vitesse $v$ qui frappent $\delta A$ entre $t$ et $t + \delta t$ sont situées dans une coque sphérique autour de
$\delta$, entre les rayons $vt$ et $v(t + \delta t)$.

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

### L'équilibre cinétique

Lorsque les particules peuvent échanger souvent de l'énergie et de la quantité de mouvement, le gaz atteint un état d'entropie maximale, appelé équilibre cinétique. 
Les fonctions de distribution $f(p)$ peuvent être dérivées en évaluant l'entropie du gaz ($S = k_B \ln \Omega$) en fonction de l'énergie, et en la maximisant, pour une énergie totale donnée et un nombre total de particules donné.

Selon la nature fermionique ou bosonique des particules du gaz, les fonctions de distribution à l'équilibre thermodynamique à la température $T$ sont :
\begin{equation}
  \boxed{\text{Fermi-Dirac:\ } f(p) = \frac{g}{\exp\left({\frac{E(p) - \mu}{k_B T}}\right) + 1}}
\end{equation}
\begin{equation}
  \boxed{\text{Bose-Einstein:\ } f(p) = \frac{g}{\exp\left({\frac{E(p) - \mu}{k_B T}}\right) - 1}}
\end{equation}
avec $\mu$ le potentiel chimique de l'espèce et $g$ son nombre de degrés de libertés interne (par exemple le nombre d'état de spin).

A haute température, on retrouve la distribution de Maxwell-Boltzmann :
\begin{equation}
  \boxed{\text{Maxwell-Boltzmann:\ }f(p) = g\exp\left(-{\frac{E(p) - \mu}{k_B T}}\right)}
\end{equation}
valable pour les fermions et les bosons.



Les fonctions de distribution de Fermi-Dirac et de Bose-Einstein dépendent de deux paramètres : la température du gaz, $T$, et le potentiel chimique de l'espèce $\mu$, qui caractérise la variation d'entropie ou d'énergie lorsque le nombre de particules varie (voir détails dans détails dans l'encadré ci-dessous).

Si le gaz contient plusieurs espèces en interaction, chaque espèce $i$ est décrite par sa propre fonction de distribution, son propre potentiel chimique $\mu_i$. chimique $\mu_i$, et éventuellement (si elle est découplée) sa propre température $T_i$.  Nous pouvons en déduire la densité de nombre, la densité d'énergie et la température de chaque espèce. 

Si toutes les espèces sont en équilibre cinétique et partagent la même température : $T_i = T$, le système a atteint _l'équilibre thermique_.


### Equilibre chimique

:::{note} Potentiel chimique

Les variations d'énergie d'un système peuvent être exprimées en fonction de de son entropie, de son volume et de sa température :
\begin{equation}
\dd E = T \dd S - P \dd V + \mu \dd N
\end{equation}
ou encore :
\begin{equation}
\dd S = \frac{\dd E}{T} + \frac{P}{T} \dd V - \frac{\mu}{T} \dd N
\end{equation}

Considérons deux systèmes $S_1$ et $S_2$ à des températures $T_1$ et $T_2$ mis en contact.  Si les deux systèmes sont isolés 
1. l'énergie l'énergie totale de ($S_1+S_2$) est constante 
$$\dd E = \dd E_1 + \dd E_2 = 0 \Rightarrow \dd E_1 = -\dd E_2$$
2. l'entropie de ($S_1 + S_2$) atteint un maximum : 
$$\dd S = \dd S_1 + \dd S_2 = 0 \Rightarrow \dd E_1/T_1 + \dd E_2/T_2 = 0$$
ce qui donne $T_1 = T_2$ à l'équilibre.

Considérons maintenant que $S_1$ et $S_2$ peuvent échanger des particules (en gardant le nombre total de particules constant). Nous avons :
1. $\dd N = \dd N_1 + \dd N_2 = 0 \Rightarrow \dd N_1 = - \dd N_2$ 
2. et l'entropie de $(S_1 + S_2)$ atteint un maximum, ce qui donne : $-\frac{\mu_1}{T} \dd N_1 - \frac{\mu_2}{T} \dd N_2 = 0$ d'où $\mu_1 = \mu_2$. À l'équilibre, les deux potentiels chimiques sont égaux.

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

Les particules et les antiparticules sont de charges opposées, d'où,
_à l'équilibre_ :
\begin{equation}
  \mu_X = -\mu_{\bar{X}}
\end{equation}
On peut aussi utiliser la réaction $X + \bar{X} \rightleftharpoons \gamma + \gamma$ pour arriver à la même conclusion.

En résumé: 
- Un système composés de différentes espèces a atteint l'équilibre cinétique s'il a atteint un état d'entropie maximale décrit par une fonction de distribution de Fermi-Dirac ou de Bose-Einstein. 
- Un système composé de plusieurs espèces interagissant via une ou plusieurs réactions chimiques a atteint l'équilibre chimique s'il a atteint un état d'entropie maximale, où la somme des potentiels chimiques des réactifs est égale à la somme des potentiels chimiques des produits. 
- Un système a atteint l'équilibre thermodynamique s'il a atteint l'équilibre chimique et si toutes les espèces partagent la même température $T$, la "température de l'Univers".

### Densité et pression des fermions et bosons


Nous avons maintenant tout ce qu'il faut pour calculer la densité particulaire, la densité d'énergie et la pression des constituants de l'Univers. Les potentiels chimiques peuvent être négligés à haute température ($\mu \ll T$), et les équations [](#eqn:number_density_general), [](#eqn:energy_density_general) et [](#eqn:pression_generale) peuvent être réécrites :
\begin{equation}
  \begin{split}
    n &= \frac{g}{2\pi^2\hbar^3} \int \dd p \frac{p^2}{\exp\left(\sqrt{p^2c^2 + m^2 c^4}/k_B T\right) \pm 1} \\
    \epsilon &= \frac{g}{2\pi^2\hbar^3} \int \dd p \frac{p^2 \sqrt{p^2c^2 + m^2 c^4}}{\exp\left(\sqrt{p^2c^2 + m^2 c^4}/k_BT\right) \pm 1} \\
    P &= \frac{g}{2\pi^2\hbar^3} \frac{1}{3} \int \dd p \frac{p^4}{\sqrt{p^2c^2 + m^2 c^4} \left[\exp\left(\sqrt{p^2c^2 + m^2c^4}/k_B T\right) \pm 1\right]}\\    
  \end{split}
\end{equation}

Dans le cas général, les intégrales ci-dessus doivent être calculées numériquement. Il existe cependant deux limites intéressantes, qui permettent de comprendre les processus physiques en cours : le cas où les particules sont relativiste ($k_B T \gg m c^2$) et le cas opposé d'espèces non relativistes ($k_B T \ll m c^2$). 

Avant de poursuivre, définissons : $x \equiv m c^2/k_B T$ et $\xi \equiv pc/k_B T$,
nous pouvons alors réécrire $n$ et $\rho$ ci-dessus comme :
\begin{equation}
  \begin{split}
    n &= \frac{g(k_BT)^3}{2\pi^2\hbar^3 c^3}  I_\pm(x) \ \ \ \mathrm{with} \ \ I_\pm(x) = \int_0^\infty \dd \xi \frac{\xi^2}{\exp\left(\sqrt{\xi^2 + x^2}\right) \pm 1} \\
    \epsilon &= \frac{g(k_BT)^4}{2\pi^2\hbar^3 c^3}  J_\pm(x) \ \ \ \mathrm{with}\ \ J_\pm(x) = \int_0^\infty \dd \xi \frac{\xi^2 \sqrt{\xi^2 + x^2}}{\exp\left(\sqrt{\xi^2 + x^2}\right) \pm 1} \\
  \end{split}
\end{equation}

#### Limite relativiste

Dans la limite relativiste, nous pouvons négliger $x$ et les intégrales $I_\pm(0)$ et $J_\pm(0)$ peuvent être calculées exactement. Nous trouvons :
\begin{equation}
  \boxed{\begin{aligned}
           &        \mathrm{Bosons}                       &  \mathrm{Fermions} \\
    n = & \frac{g \zeta(3)(k_BT)^3}{\pi^2\hbar^3 c^3}   & n =\frac{3}{4} \frac{g \zeta(3)(k_BT)^3}{\pi^2\hbar^3 c^3}  \\
    \epsilon = & \frac{g\pi^2(k_BT)^4}{30\hbar^3 c^3}        & \epsilon =\frac{7}{8}\frac{g \pi^2(k_BT)^4}{30\hbar^3 c^3} \\
  \end{aligned}}
  \label{eqn:n_rho_relativistic_limit}
\end{equation}
Les photons sont des bosons avec $g_\gamma=2$ polarisations possibles, donc on a ici démontré la loi de Stefan-Boltzmann.

Concernant le calcul de la pression, on a $p^2 / E \sim p$ pour les particules relativistes, donc :
\begin{equation}
  P = \frac{1}{3} \frac{g}{2\pi^2\hbar^3 c^3} (k_BT)^4 \int \dd \xi \frac{\xi^3}{\exp\xi \pm 1} = \frac{1}{3} \frac{g}{2\pi^2\hbar^3} (k_BT)^4 J_\pm(0) = \frac{\epsilon}{3}
  \label{eqn:P_relativistic_limit}
\end{equation}
On retrouve l'équation d'état déjà introduite précédemment. 


:::{exercise}

Using $T_0 = 2.726 K$, compute the photon number density (today) and
the photon energy density (today). Show that:
\begin{equation*}
  \begin{split}
    n_\gamma & = 411\ \mathrm{cm}^{-3}\\
    \epsilon_\gamma &= 4.6 \times 10^{-34}\ \mathrm{g/cm^{3}} \\
    \end{split}
  \end{equation*}
  and recover the CMB photon density today (in units of the critical density):
  \begin{equation*}
    \Omega_\gamma = 2.5 h^{-2} 10^{-5}
  \end{equation*}
  To get the correct numerical answer, you will need to do a little bit of dimensional analysis.  Where did we drop the physical constant(s) you had to retrieve ?
:::


:::{note} Calculs de $I_\pm(0)$ et $J_\pm(0)$
:class: dropdown

To compute $I_{-}(0)$ it is useful to know the definition of the Riemann-zeta function:
$$
\zeta(s) = \sum_{i=1}^\infty \frac{1}{n^s} = \frac{1}{\Gamma(s)} \int_0^\infty \frac{x^s}{e^x - 1} \dd x
\ \ \mathrm{where}\ \ \ \Gamma(s) = \int_0^\infty x^{s-1} e^{-x} \dd x
$$

Pour les bosons, nous obtenons immédiatement 
$$
I_-(0) = 2 \zeta(3) \approx 
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

Dans le régime non relativiste, seule la densité de particules est quelque peu délicate à calculer.  Avec les mêmes définitions que ci-dessus : $x\equiv m c^2 / k_B T$, $\xi \equiv p c /k_B T$ et $x \gg 1$, les intégrales $I_-$ et $I_+$ se réduisent à une seule expression :
\begin{equation}
  I_\pm = \int_0^\infty \frac{\xi^2 \dd \xi}{\exp(\sqrt(x^2 + \xi^2))}
\end{equation}
$\xi \ll x$ et nous pouvons développer : $(x^2 + \xi^2)^{1/2} \approx x (1 + \frac{1}{2}\frac{\xi^2}{x^2})$, et nous pouvons approximer l'intégrale ci-dessus avec :
\begin{equation}
  \begin{split}
    I_\pm & \approx e^{-x} \int_0^\infty \xi^2 e^{-\frac{\xi^2}{2 x}} \dd \xi \\
         & \approx e^{-x} (2x)^{3/2} \frac{1}{2} \underbrace{\Gamma\left(\frac{3}{2}\right)}_{\sqrt{\pi}/2}
  \end{split}
\end{equation}

:::

:::{note} Gaz moléculaire

Si la particule considérée est composée de plusieurs atomes, alors elles possèdent plus de degrés de libertés que les 3 translations dans l'espace. Suivant une statistique de Boltzmann, elle peut stocker de l'énergie dans des degrés de liberté de rotation ou de vibration si le milieu est assez chaud, chacun comptant pour $k_B T / 2$ dans son énergie interne. Si on note $g_m$ le nombre de degrés de liberté d'une molécule, alors la densité d'énergie s'écrit
$$ \epsilon &\approx n m c^2 + \frac{g_m}{2} nk_B T = n m c^2 + \frac{1}{\gamma -1} n k_B T $$
avec $\gamma=C_p/C_V$ l'indice adiabatique, que l'on retrouve dans la loi de Laplace $pV^\gamma = cst$.
:::


### Nombre effectif d'espèces relativistes

Nous partons d'un plasma primordial en équilibre thermique et chimique, contenant des espèces $i$ à la température $T_i$.

Avant l'équivalence, le taux d'expansion est une fonction directe de la densité massique de matière relativiste :
\begin{equation}
  H^2 = \frac{8\pi G}{3} \rho_r(T)
\end{equation}
où $\rho_r(T)$ est la somme des densités de chaque espèce relativiste présente dans le fluide primordial :
\begin{equation}
  \rho_r(T) = \sum_i^{m_i \ll T} \rho_i(T)
\end{equation}
Nous avons vu dans la section précédente que $\rho_i \propto T_i^4$ tant que la particule reste relativiste, et chute exponentiellement quand la température tombe en dessous de la masse de la particule. Plus précisément, nous pouvons écrire
\begin{align*}
\rho_r & = \sum_{i=\mathrm{bosons}}^{m_i \ll T} \frac{g_i\pi^2}{30}T_i^4 +   \sum_{i=\mathrm{fermions}}^{m_i \ll T} \frac{7}{8}\frac{g_i\pi^2}{30}T_i^4 \\
& = T^4 \left(\frac{\pi^2}{30}\right) \sum_{i=\mathrm{bosons}} g_i \left(\frac{T_i}{T}\right)^4 +   \frac{7}{8} \sum_{i=\mathrm{fermions}} g_i \left(\frac{T_i}{T}\right)^4 
\end{align*}
On définit $g_\star(T)$ le nombre effectif de degrés de liberté _relativistes_ du plasma à la température $T$ : 
\begin{equation}
\rho_r(T) = g_\star(T) \left(\frac{\pi^2}{30\hbar^3 c^5}\right) (k_BT)^4
\end{equation}
\begin{equation}
g_\star(T) = \sum_{i=\mathrm{bosons}}^{m_i \ll T} g_i \left(\frac{T_i}{T}\right)^4 +   \frac{7}{8} \sum_{i=\mathrm{fermions}}^{m_i \ll T}  g_i \left(\frac{T_i}{T}\right)^4
\end{equation}
Lorsque l'espèce $i$ est encore à l'équilibre thermique avec les photons, alors $T_i=T$.
Lorsque la température descend en dessous de la masse $m_i$ de l'une des espèces, elle devient relativiste et disparaît de la somme ci-dessus. 


#### Expansion du plasma primordial

La loi d'expansion obéit à la première équation de Friedmann :
\begin{equation}
  H^2 = \frac{8\pi G}{3} \rho_r = \frac{8\pi G}{3} \frac{\pi^2}{30\hbar^3 c^5} g_\star(T) T^4
\end{equation}
et donc :
\begin{equation}
  \boxed{H = \sqrt{\frac{8 \pi^3 G}{90 \hbar^3 c^5}} g_\star^{1/2}(T) (k_B T)^2}
\end{equation}
Ainsi, $H \propto T^2$ aux variations du nombre effectif de degrés de liberté dans le plasma primordial près. Gardez cela à l'esprit, cela sera utile lorsque vous comparerez le taux d'expansion avec les divers taux de réaction entre les différentes espèces.

De plus, comme l'Univers est dominé par le rayonnement, nous avons [](#eq:a_rad_only) :
\begin{equation}
 a \propto t^{1/2} \Rightarrow H = \frac{1}{2 t}
\end{equation}
ce qui donne :
\begin{equation}
  \boxed{T \approx \left[ 1.8 \times 10^{10} \mathrm{K}\right] \times  g_*(T)^{-1/4} \left(\frac{t}{\mathrm{1\ sec}}\right)^{-1/2}} 
\end{equation}
Ainsi, lorsque l'Univers était âgé d'une seconde, l'énergie typique des particules relativistes était de l'ordre de 0.9 MeV avec $g_*=10.75$.


#### Évolution de $g_\star(T)$


:::{figure} #gtable
:name: tab:gtable
:::

La dernière pièce manquante est l'évolution de $g_\star(T)$, qui raconte simplement l'évolution de la matière relativiste du plasma primordial au fur et à mesure qu'il se refroidit avec l'expansion. Commençons autour de $T \approx 300\,$GeV. Toutes les particules du modèle standard sont relativistes (voir [](#tab:gtable)). Lorsque toutes les particules sont relativistes, le nombre total de degrés de liberté est de :
\begin{equation}
  g_f = \underbrace{6 \times 12}_{\mathrm{quarks}} + \underbrace{3 \times 4}_{\ell^\pm} + \underbrace{3 \times 2}_{\nu's} = 90
\end{equation}
pour les fermions, et
\begin{equation}
  g_b = \underbrace{8 \times 2}_{gluons} + \underbrace{3 \times 3}_{W,Z} + \underbrace{2}_{\gamma} + \underbrace{1}_{H}  = 28
\end{equation}
pour les bosons, ce qui donne
\begin{equation}
  g_\star = g_b + \frac{7}{8} g_f = 106.75
\end{equation}

Pour voir ce qui va se passer ensuite, il suffit de regarder les masses des particules énumérées dans le [](#tab:gtable). Le quark top s'annihile en premier, réduisant le nombre de degrés de liberté à :
\begin{equation}
  g_\star(T<m_{\mathrm{top}}) = 106.75 - \frac{7}{8} \times 12 = 96.25
\end{equation}
Puis, nous avons donc le boson de Higgs, suivi des bosons électrofaibles $W^\pm$ et $Z^0$ : ce qui réduit $g_\star$ à 86.25. Ensuite, $b$ et $c$ s'annihilent, et $g_\star$ est alors réduit à 61.75.

L'événement suivant est la transition de phase QCD, qui se produit à $T \sim 150\ \mathrm{MeV}$.  Les quarks se combinent en baryons (protons, neutrons et mésons), tous sauf les pions étant relativistes. A ce stade, les seules espèces relativistes restantes sont les photons, les neutrinos, les électrons et les muons et les 3 pions de spin 0, d'où : $g_\pi = 3 \cdot 1 = 3$. Donc :
\begin{equation}
  g_\star(T<T_{QCD}) = \underbrace{2}_{\gamma} + \underbrace{3}_{\pi} + \frac{7}{8} \times (\underbrace{4 + 4}_{e^{\pm}, \mu^\pm} + \underbrace{6}_{\nu's}) = 17.25
\end{equation}

Ensuite, les pions et les muons s'annihilent, ce qui nous donne
\begin{equation}
  g_\star = 2 + \frac{7}{8} \times (4 + 6) = 10.75
\end{equation}

:::{figure} #ggstar_plot
:name: fig:ggstar_plot
:::

Les deux événements significatifs suivants sont le découplage des neutrinos autour de 1 MeV puis l'annihilation des électrons et des positrons ($m_e = 511 \mathrm{keV}$). 


### Conservation de l'entropie


L'entropie de l'Univers ne peut qu'augmenter ou rester constante. Nous savons qu'à l'équilibre, l'entropie est conservée (voir encadré).  Le plasma primordial n'est pas _exactement_ à l'équilibre\footnote{c'est heureux, sinon, nous ne serions pas là pour réfléchir à tout cela} : l'expansion n'en fait qu'un équilibre local, nous verrons de nombreux exemples de processus hors équilibre dans la suite de l'article.  Cependant, comme l'entropie est au premier ordre proportionnelle au nombre de particules, et que les photons sont de loin l'espèce la plus abondante dans l'Univers, nous pouvons supposer sans risque que l'entropie est conservée, et que, à une très grande précision, l'expansion cosmique est un processus adiabatique.

Comment calculer l'entropie totale de l'Univers ? Nous pouvons commencer par :
\begin{equation}
  E = TS -PV + \sum_i \mu_i N_i
\end{equation}
ce qui donne :
\begin{equation}
  S = \frac{E}{T} + \frac{P}{T}V - \sum_i \frac{\mu_i}{T} N_i
\end{equation}
en négligeant les potentiels chimiques :
\begin{equation}
  S \approx \frac{E}{T} + \frac{P}{T}V
\end{equation}
Il est utile de prendre en compte l'entropie {\densité d'emprise} :
\begin{equation}
  s \equiv \frac{S}{V} \approx \frac{\rho + P}{T}
\end{equation}

Pour les espèces relativistes, en introduisant les expressions de la densité et de la pression (\ref{eqn:n_rho_relativistic_limit}, \ref{eqn:P_relativistic_limit}), nous trouvons :
\begin{equation}
  \boxed{\begin{split}
    s &= \frac{2\pi^2}{45} g T^3 \ \ \ \mathrm{for\ bosons}\\
    s &= \frac{7}{8} \frac{2\pi^2}{45} g T^3 \ \ \ \mathrm{for\ fermions}\\
  \end{split}}
\end{equation}
Pour une collection d'espèces (fermions et bosons), nous avons :
\begin{equation}
    s = \frac{2\pi^2}{45} g_{\star S}(T) T^3
\end{equation}
avec
\begin{equation}
  g_{\star S}(T) = \sum_{\mathrm{bosons}} g_b \left(\frac{T_b}{T}\right)^3 + \frac{7}{8} \sum_{\mathrm{fermions}} g_f \left(\frac{T_f}{T}\right)^3
\end{equation}


Si l'entropie $S$ est conservée, alors :
\begin{equation}
  \dd S = 0 \Rightarrow \boxed{\dd(s a^3) = 0}
\end{equation}
ce qui donne
\begin{equation}
  \boxed{g_{\star S}(T) T^3 a^3 = \mathrm{constante}}
\end{equation}



Dans les intervalles entre les masses des particules, $g_\star(T)$ reste pratiquement constant.  Puisque $\epsilon \propto g_\star(T) T^{4} \propto a^{-4}$, nous pouvons raffiner le lien entre température et facteur d'échelle dans le plasma primordial :
\begin{equation}
  \boxed{T \propto \left[g_\star^{1/3}(T) a\right]^{-1}}
\end{equation}


Histoire de la matière dans l'Univers jeune
--------------------------------------

Nous avons maintenant (presque) tout ce dont nous avons besoin pour discuter de l'évolution du plasma primordial. Lorsque la température est suffisamment élevée, le plasma primordial contient toutes les particules du modèle standard, sous forme relativiste (plus toutes les particules qui n'ont pas encore été découvertes, par exemple les particules hypothétiques qui constituent la matière noire froide).

Dans l'Univers primitif, toutes les espèces de particules sont en équilibre thermique (cinétique et chimique, même température $T$).  Au fur et à mesure de l'expansion de l'Univers, la température diminue ($T \propto a^{-1}$). L'une après l'autre, les différentes espèces massives deviennent non relativistes, s'anéantissent, et leur densité d'énergie devient sous-dominante par rapport aux espèces relativistes.

Si l'Univers était en parfait équilibre thermique, et si cet équilibre avait persisté jusqu'à aujourd'hui, les abondances observées de particules massives seraient bien inférieures à ce qu'elles sont, puisque chaque espèce massive est exponentiellement supprimée lorsqu'elle devient non relativiste.  En fait, les équilibres thermiques et chimiques ont besoin de taux de collision (et/ou de réaction) fréquents pour être maintenus. Avec l'expansion de l'Univers, les particules se diluent, ce qui rend plus difficile le maintien des taux de réaction. Une bonne règle empirique est qu'il faut plusieurs réactions par temps de Hubble pour maintenir l'équilibre thermique. Ainsi, si
\begin{equation}
  \Gamma \gg H
\end{equation}
l'équilibre est maintenu. Lorsque le taux de réaction chute en dessous de $H$, l'équilibre thermique n'est plus maintenu, les densités de particules sont gelées à leurs valeurs d'avant le découplage. Le gel est un mécanisme essentiel pour expliquer l'abondance actuelle des particules.


### Découplage des neutrinos et annihilations électron-positron


Le découplage des neutrinos est notre première expérience de freeze-out.  Les neutrinos n'interagissent que par le biais de l'interaction faible.  Autour de $\sim$ 1 MeV, ils sont encore thermalisés par des interactions telles que :
\begin{equation}
  \begin{split}
    \nu_e + p & \rightleftharpoons p + e^- \\
    \nu_e + \bar{\nu_e} & \rightleftharpoons e^+ + e^- \\
    e^- + \nu_e & \rightleftharpoons e^- + \nu_e \\    
  \end{split}
\end{equation}
Cependant, à ces énergies, la section efficace de l'interaction faible est $\sigma_w \sim G_F^2 T^2$, par conséquent, le taux d'interaction $\Gamma = n_e \sigma_w c \propto G_F^2 T^5$ diminue beaucoup plus rapidement que le paramètre de Hubble ($\propto T^2$).  Autour de 1 MeV, $\Gamma \sim H$ et les interactions entre les neutrinos et les autres particules du SM deviennent très improbables.  Les neutrinos se découplent et se déplacent librement le long des géodésiques.

À ce stade, les neutrinos sont encore relativistes ($m_\nu \ll 1 MeV$). Même s'ils n'interagissent plus avec d'autres particules, ils conservent dans une excellente approximation leur fonction de distribution de Fermi-Dirac (voir encadré) avec une température qui n'est affectée que par le décalage vers le rouge. Ainsi, à ce stade :
\begin{equation}
  T_\nu = T_\gamma \propto a^{-1}
\end{equation}



:::{note} Le spectre des espèces découplées sans interaction

Pour les espèces ultra-relativistes, nous avons $p \sim E$. Le nombre de particules à $t_1$ dans le volume de l'espace des phases $d^3p_1 \dd V_1$ est :
\begin{equation}
\dd N = \frac{g}{(2\pi)^3} \frac{d^3p_1 \dd V_1}{\exp((E(p_1) - \mu_1)/T_1) \pm 1}
\end{equation}
A $t_0$, un peu plus tard, les mêmes particules se trouvent dans le volume de l'espace des phases $d^3p_0 \dd V_0$.   Les moments s'échelonnent comme $a^{-1}$ et le volume comme $a^3$. On peut donc écrire
\begin{equation}
\begin{split}
  \dd N  & = \frac{g}{(2\pi)^3} \frac{d^3p_1 \dd V_1}{\exp((p_1 - \mu_1)/T_1) \pm 1} \\
      & = \frac{g}{(2\pi)^3} \frac{d^3p_0 \left(\frac{a_0}{a_1}\right)^3 \dd V_0\left(\frac{a_1}{a_0}\right)^3}{\exp((p_0\left(\frac{a_1}{a_0}\right) - \mu_1)/T_1) \pm 1} \\
      & = \frac{g}{(2\pi)^3} \frac{d^3p_0 \dd V_0}{\exp((p_0 - \mu_0)/T_0) \pm 1} \\
\end{split}
\end{equation}
avec $\mu_0 \equiv \frac{a_1}{a_0} \mu_1$ et $T_0 \equiv \frac{a_1}{a_0} T_1$.   

:::


### Annihilation $e^+ + e^-$ 

Peu après le découplage des neutrinos vers 1 MeV, les électrons et les positrons s'annihilent (511 keV).  Naïvement, on pourrait dire que $g_\star(T)$ devient alors :
$$
2 + \frac{7}{8} \times 6 = 7.25
$$
mais la Nature est plus subtile.  En effet, l'annihilation électron-positron produit suffisamment d'énergie et d'entropie pour chauffer le bain de photons et modifier la température des photons.  Les neutrinos ne sont pas affectés et leur température varie toujours comme $a^-1$.  Par conséquent, après l'annihilation de $e^+ + e^-$, nous avons $T_\nu < T_\gamma$.

Nous nous trouvons donc dans une nouvelle situation où nous avons plusieurs espèces relativistes avec des températures différentes.  Pour en tenir compte, nous pouvons modifier l'équation \ref{eqn:g_star_same_temp}, en permettant à chaque espèce d'avoir sa propre température :
\begin{equation}
  g_\star(T) = \sum_{\mathrm{bosons}} g_i \left(\frac{T_i}{T}\right)^4 + \frac{7}{8} \sum_{\mathrm{fermions}} g_i \left(\frac{T_i}{T}\right)^4
\end{equation}
Pour aller plus loin, nous devons déterminer $T_\nu$, ou plus exactement, relier $T_\nu$ et $T_\gamma$ (nous connaissons assez bien $T_\gamma$). La façon la plus simple de le faire est d'utiliser la conservation de l'entropie.

### La température du fond diffus de neutrinos

Revenons à la détermination de la relation entre la température des photons et la température du fond de neutrinos cosmiques.
cosmique. Lors de l'annihilation, l'entropie et l'énergie du $e^\pm$ sont transférées au bain de photons. L'entropie étant conservée, nous avons, avant l'annihilation, démonté l'entropie des neutrinos (qui est conservée) :
\begin{equation}
  g^\gamma_{\star S, \mathrm{before}}(T) = 2 + \frac{7}{8} (4) = \underbrace{\frac{11}{2}}_{e^\pm, \gamma} 
\end{equation}
après annihilation : 
\begin{equation}
  g^\gamma_{\star S, \mathrm{after}}(T) = 2 
\end{equation}
En écrivant la conservation de l'entropie, nous avons :
\begin{equation}
  a^3_\mathrm{before}\ g^\gamma_{\star S \mathrm{before}}\ T^3_\mathrm{before} = a^3_\mathrm{after}\ 
g^\gamma_{\star S \mathrm{after}}\ T^3_\mathrm{after}
\end{equation}
ce qui donne
\begin{equation}
  \underbrace{T^3_\mathrm{after}}_{T_\gamma} = \frac{g^\gamma_{\star S, \mathrm{before}}}{g^\gamma_{\star S, \mathrm{after}}} \underbrace{\left(\frac{a_{\mathrm{before}}}{a_{\mathrm{after}}}\right)^3 T^3_{\mathrm{before}}}_{T_\nu}
\end{equation}
et donc :
\begin{equation}
  \boxed{T_\nu = \left(\frac{4}{11}\right)^{1/3}\ T_\gamma}
\end{equation}

Nous constatons donc qu'après l'annihilation de $e^\pm$, la température du fond de neutrinos cosmiques est effectivement inférieure à la température du CMB. Aujourd'hui, en utilisant $T_0 = 2.726\,$K, nous trouvons :
\begin{equation}
  T_\nu \approx 1.95\,K
\end{equation}

Nous pouvons en déduire la densité de neutrinos $n_\nu$ en fonction de $n_\gamma$. Les neutrinos sont des fermions donc : 
\begin{equation}
  n_\nu = \frac{3}{4} \times 3 \times \frac{4}{11} n_\gamma
\end{equation}
ce qui donne $\approx 112 \mathrm{cm}^{-3}$ par saveur (336 cm$^{-3}$ au total).

Pour la densité d'énergie du fond de neutrinos, nous trouvons :
\begin{equation}
  \rho_\nu = \frac{7}{8} \times 3 \times \left(\frac{4}{11}\right)^{4/3} \rho_\gamma
\end{equation}
et numériquement, on trouve $\Omega_\nu h^2 \approx 1.7\times 10^{-5}$.

En fait, les neutrinos ont des masses, avec deux conséquences importantes (1) nous ne savons pas s'ils sont encore relativistes aujourd'hui 
(toutes espèces confondues) (2) $\Omega_\nu h^2$ est plus grand que la valeur citée ci-dessus.

Une autre remarque est que le découplage des neutrinos s'est légèrement superposé à l'annihilation de $e^\pm$.  
Comme les neutrinos interagissaient encore au moment de l'annihilation, le bruit de fond des neutrinos a été légèrement affecté par l'énorme énergie et l'entropie libérées par l'annihilation de $e^\pm$. Dans la littérature, cela est pris en compte en introduisant un "nombre effectif de neutrinos", $N_{\mathrm{eff}} \approx 3.046$. En tenant compte de cela, le nombre de neutrinos et la densité d'énergie sont :
\begin{equation}
  \begin{split}
    n_\nu(T_\gamma) & = 2 \times \frac{3}{4} N_{\mathrm{eff}} \frac{4}{11} n_\gamma(T_\gamma) \\
    \rho_\nu & = 2 \times \frac{7}{8} N_{\mathrm{eff}} \frac{4}{11} n_\gamma \\
  \end{split}
\end{equation}

Enfin, les valeurs correctes $g_\star$ et $g_{\star S}$ après l'annihilation $e^\pm$ sont :
\begin{equation}
  \begin{split}
    g_\star & = 2 + \frac{7}{8} 2 N_{\mathrm{eff}} \left(\frac{4}{11}\right)^{4/3} \approx 3.36 \\
    g_{\star S} & = 2 + \frac{7}{8} 2 N_{\mathrm{eff}} \left(\frac{4}{11}\right) \approx 3.94 \\    
  \end{split}
\end{equation}


### Big Bang Nucleosynthesis (BBN)

Environ 1ms après le Big Bang, l'Univers est donc essentiellement une soupe chaude de baryons, de photons, d'électrons et de neutrinos, thermodynamiquement découplés des autres particules. On rappelle que le rapport baryon sur photon est une constante  [](#eq:eta) et vaut plus précisément :
$$\eta = 6.2 \times 10^{-10}$$
L'Univers continuant son expansion, il se refroidit et les protons et neutrons peuvent fusionner pour former les premiers noyaux atomiques. 

#### Rapport neutron/proton

Le taux de formation de ces noyaux va dépendre d'un paramètre essentiel : le rapport des nombres de neutrons et protons disponibles.

:::{note} Free neutron decay
Le neutron est instable s'il n'est pas lié à un proton dans un noyau atomique par interaction forte. Il se désintègre selon la réaction :
$$ n \rightarrow p + e^- + \bar{\nu}_e $$
car son énergie de masse est légèrement supérieure à celle du proton :
$$ Q_n = (m_n - m_p)c^2 = 1.29\,\mathrm{MeV}$$
La valeur de la durée de vie moyenne retenue par le Particle Data Group en 2022 est {cite:p}`PDG2022` :
$$\tau_n = 878.4 \pm 0.5\,\mathrm{s}$$ 
soit environ 15 minutes seulement. L'existence des neutrons libres dans l'Univers est donc fortement limitée dans le temps. Dans toute la suite, il faudra vérifier si l'age de l'Univers est petit devant ce temps de désintégration ($t\ll \tau_n$) pour voir s'il est légitime de négliger cette désintégration spontanée.
:::


A $t=0.1\,$s, les protons et neutrons sont à l'équilibre thermodynamique l'un avec l'autre via les interactions :
\begin{align}
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
\left.\frac{n_n}{n_p}\right\vert_{eq} = \left(\frac{m_n}{m_p}\right)^{3/2} \exp \left(- \frac{(m_n-m_p)c^2}{k_B T} \right) \approx \exp\left(-\frac{Q_n}{k_B T}\right)
\end{equation}
On en déduit que tant que la température est telle que $k_B T \gg Q_n = 1.29\,$MeV alors il y a autant de neutrons que de protons dans l'Univers, mais qu'en deçà la proportion de neutrons chute exponentiellement *tant que les réactions ont lieu*. En effet, si le taux d'expansion de l'Universe devient comparable ou supérieur au taux d'interaction, alors les réactions s'arrêtent et la proportion neutron sur proton est gelée. Pour la réaction $p+e^- \rightarrow \nu_e + n$, le taux d'interaction est donné par ({cite}`KolbTurner` p.90, {cite}`Weinberg1989` p.547 et originellement dans {cite}`Peebles1966`) :
$$
\Gamma_{pe\to \nu n} = \frac{1}{(2\pi)^5}\int f_e(E_e)\left[ 1 - f_\nu(E_\nu)\right]\vert \mathcal{M}\vert^2_{pe\to \nu n}\delta^4(p+e-\nu-n) \frac{\dd^3 p_e}{2 E_e}\frac{\dd^3 p_\nu}{2 E_\nu}\frac{\dd^3 p_n}{2 E_n}
$$
avec $f_i(E_i)$ les distributions de Fermi-Dirac des particules $i$ et :
$$\vert \mathcal{M} \vert ^2 \propto G_F^2 ( 1+ 3g_A^2)$$
avec $G_F = 1.16\times 10^{-5}  \,\GeV^{-2}$ la constante de Fermi et $g_A = 1.26$ le couplage axial-vecteur des nucléons ({cite}`KolbTurner` p.91). Malheureusement ces intégrales doivent être calculées précisément pour obtenir la bonne proportion d'hélium, car on va voir que la proportion de neutron gèle à une température proche de $Q$ et $m_e$, ce qui empêche de faire des approximations brutales pour se concentrer sur un régime de haute ou basse énergie. Une méthode d'intégration numérique est proposée dans {cite}`Dodelson2003` p.67  et {cite}`Bernstein1989` en définissant la proportion de neutron $X_n = n_n / n_b = n_n / (n_n + n_p)$ :
\begin{equation}\label{eq:Xn}
\frac{\dd X_n}{\dd t} = \Gamma_{np} \left[(1-X_n)e^{-Q_n / k_B T} - X_n\right] - \frac{X_n}{\tau_n} 
\end{equation}
avec le taux de réaction :
\begin{equation}\label{eq:Gnp} 
\Gamma_{np}(x) = \frac{255}{\tau_n x^5}(12+6x+x^2), \quad x= \frac{Q_n}{k_B T}
\end{equation}
Après intégration numérique avec comme condition initiale et relation température-temps :
$$X_n(t \approx 0.1\,\mathrm{s}) = \frac{1}{1+e^(-Q_n / k_B T(t))},\quad T(t) = 1.0\times 10^{10} \left(\frac{t}{1\,\mathrm{s}}\right)^{-2}, \quad g_*=10.75$$
on obtient la figure [](#fig:BBN_Xn), convergeant vers $X_n^{\mathrm{freeze}} = 0.15$, soit 1 neutron pour 6 protons[^Tfreeze] si $\tau_n$ la désintégration spontanée du neutron est omise ($\tau_n \to \infty$). 

:::{figure} #BBN_Xn
:name: fig:BBN_Xn
:width: 70%

Fraction de neutrons $X_n$ en fonction du temps calculé par l'équation [](#eq:Xn) (trait plein). Si la désintégration du neutron est négligée, alors on obtient la courbe en pointillé ($\tau \to \infty$). La distribution d'équilibre $\left.n_n/n_p\right\vert_{eq}$ donne la proportion de neutrons si les réactions ne sont pas gelées par l'expansion de l'Univers.
:::

La proportion de neutrons $X_n$ converge vers un plateau tant que $t \lesssim \tau_n$ après la température $T_{\mathrm{freeze}}= 0.7\,\MeV$ pour laquelle le taux d'intéraction $\Gamma_{np}(T)$ est comparable au taux d'expansion $H(T)$ ([](#eq:Gnp))

:::{figure} #BBN_Gnp
:name: fig:BBN_Gnp
:width: 70%

Fraction de neutrons $X_n$ en fonction du temps calculé par l'équation [](#eq:Xn) pendant la recombinaison (trait plein). Si la désintégration du neutron est négligée, alors on obtient la courbe en pointillé ($\tau \to \infty$). La distribution d'équilibre $\left.n_n/n_p\right\vert_{eq}$ donne la proportion de neutrons si les réactions ne sont pas gelées par l'expansion de l'Univers.
:::

#### Synthèse du deutérium

A la température de gel des neutrons, la proportion de neutrons et de protons est donc stable, à ceci près qu'un neutron libre est instable avec un temps de désintégration d'environ 15 minutes. Toutefois, si la température descend suffisamment, protons et neutrons peuvent se combiner pour former le plus léger des noyaux atomiques par interaction forte, le deutérium $\mathrm{D}$, via la réaction
\begin{align}
p + n \rightleftharpoons \mathrm{D} + \gamma
\end{align}
Le deutérium possède une énergie de liaison :
$$B_{\mathrm{D}} = (m_n + m_p - m_\mathrm{D})c^2 = 2.22\,\mathrm{MeV}$$
A l'équilibre, 
\begin{equation}
\frac{n_\mathrm{D}}{n_pn_n} = \frac{g_\mathrm{D}}{g_p g_n} \left(\frac{k_B T}{2\pi \hbar^2}\right)^{-3/2}\left(\frac{m_\mathrm{D}}{m_p m_n}\right)^{3/2} \exp \left( \frac{(m_p+m_n-m_\mathrm{D})c^2}{k_B T} \right) \approx 6 \left(\frac{m_n k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_\mathrm{D}}{k_B T}\right)
\end{equation}
avec $g_\mathrm{D}=3$, $g_n=g_p=2$ et $\mu_p + \mu_n = \mu_D + \mu_\gamma = \mu_D$  ({cite}`ryden2017` p.219).

On définit la température de démarrage de la nucléosynthèse $T_{\mathrm{nuc}}$ celle où la moitié des neutrons ont été consommés pour former du deutérium, c'est-à-dire lorsque $n_\mathrm{D}=n_n$. Le rapport deutérium sur neutron s'écrit :
\begin{equation}\label{eq:XD}
\frac{n_\mathrm{D}}{n_n} \approx 6 n_p \left(\frac{m_n k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_D}{k_B T}\right)
\end{equation}
Le nombre de protons au moment de la nucléosynthèse est donné par :
$$n_p \approx (1-X_n(T_{\mathrm{nuc}})) n_b = (1-X_n(T_{\mathrm{nuc}})) \eta n_\gamma(T_{\mathrm{nuc}}) $$
On en déduit alors la température $T_{\mathrm{nuc}}$ par l'inversion numérique de l'équation [](#eq:XD) :
$$T_{\mathrm{nuc}} = 7.9 \times 10^8\,\mathrm{K}$$
soit $t_{\mathrm{nuc}}\approx 280\,$s après le Big Bang, avec $g_* = 3.36$ dorénavant puisque l'Univers possède une température inférieure à $m_e$. A ce moment précis, la fraction de neutrons encore présente est environ de : 
$$\frac{n_n}{n_p}(T_{\mathrm{nuc}}) = \frac{X_n(T_{\mathrm{nuc}})}{1-X_n(T_{\mathrm{nuc}})} = 0.14 \sim 1/7$$


:::{note} Free neutron decay again

A cause de leur désintégration spontanée, la proportion de neutrons libres continue de chuter, et peut s'écrire :
$$X_n(t) = X_n^{\mathrm{freeze}} e^-t/\tau_n$$
A $t_\mathrm{nuc}$ la proportion de neutrons a diminué de $0.17 \sim 1/6$ vers :
$$ \frac{n_n}{n_p}(t_\mathrm{nuc}) \approx \frac{e^{-t_\mathrm{nuc}/\tau_n}}{6 + [1- e^{-t_\mathrm{nuc}/\tau_n}]} \approx 0.12 $$
ce qui proche du résultat précédent mais moins exact que de prendre en compte cette désintégration directement dans l'équation différentielle [](#eq:Xn).

:::


#### Synthèse de l'hélium 4

La formation des noyaux d'hélium n'est possible que via la fusion de noyaux de deutérium :
\begin{align}
p + n &\rightarrow &\mathrm{D} + \gamma \\
\mathrm{D} + p &\rightarrow &^3\mathrm{He} + \gamma \\
\mathrm{D} + \mathrm{D} &\rightarrow& ^4\mathrm{He} + \gamma 
\end{align}
car il est beaucoup plus improbable que deux protons et deux neutrons se rencontrent par hasard pour former un noyau d'hélium.
Or l'énergie de liaison de l'hélium 4 est bien supérieure à celle du deutérium ($B_{\mathrm{He}} = 28.3\,\MeV$) donc c'est sa formation qui sera favorisée. On peut donc supposer que tous les neutrons disponibles à $t_\mathrm{nuc}$ vont terminer dans un noyau d'hélium. 

Comme deux neutrons vont dans un noyau d'hélium 4, le nombre maximum de noyaux d'hélium formables est égal à la moitié des neutrons disponibles (qu'ils soient libres ou dans les noyaux de deutérium). On en déduit l'abondance en hélium 4 en nombre de noyaux comme étant :
$$n_{\mathrm{He}} = \frac{1}{2} n_n(t_\mathrm{nuc})$$
En terme de masse, l'abondance d'hélium 4 dans l'Univers à la fin de la nucléosynthèse primordiale peut être au maximum de :
\begin{equation}
\boxed{Y_p \equiv \frac{\rho(^4\mathrm{He})}{\rho_b} = \frac{4n_\mathrm{He}}{n_n + n_p} \approx 25\%}
\end{equation}
en bon accord avec les mesures (voir Figure~[](#fig:BBN_mes). Des calculs plus précis donnent $Y_p$ autour de 24%, et notamment prédisent aussi la proportion des autres noyaux légers comme le deutérium après $t_{\mathrm{nuc}}$, le lithium, etc ([](#fig:BBN)).


```{figure} ../images/bbn.png
:width: 80%
:align: center
:label: fig:BBN

Synthèse des éléments légers dans l'Univers primordial (d'après {cite}`PospelovBBN2010`).
```


```{figure} ../images/bbn_Yp.png
:width: 80%
:align: center
:label: fig:BBN_mes

Comparaison entre les prédictions théoriques pour les abondances des noyaux légers (bandes colorées) et les mesures (bandes grises) (d'après {cite}`Baumann`).
```

:::{note} Au-delà de l'hélium

Il est très difficile de former des noyaux au-delà de l'hélium car ce dernier possède une énergie de liaison particulièrement supérieure aux atomes immédiatement plus lourds. En particulier il n'existe pas de noyaux stables avec $A=5$ nucléons donc pour aller au-delà de l'hélium il ne suffit pas d'absorber un des nombreux protons présents. Un peu de lithium peut se former via les réactions :
$$^4\mathrm{He} + \mathrm{D} \rightleftharpoons ^6\mathrm{Li} + \gamma $$

```{figure} ../images/Binding_energy_curve.svg
:width: 80%
:align: center
:label: fig:BBN_mes

Energie de liaison par nucléons (source: Wikipedia <wiki:Nuclear_binding_energy>).
```
:::

### Recombinaison

La recombinaison correspond au moment où les électrons vont se combiner aux atomes pour former les premiers atomes. A ce moment là, le plasma se transforme en gaz d'hydrogène et d'hélium (plus un peu de lithium etc) neutre, laissant les photons du bain thermique libre de se propager dans l'Univers. Cette première lumière correspond au fond diffus cosmologique et nous renseigne sur l'état de l'Univers jeune et la physique qui s'y est déroulée avant. 

La formation des atomes d'hydrogène se déroule par la réaction :
$$ p + e^- \rightleftharpoons \mathrm{H} + \gamma$$
et on rappelle que l'énergie de liaison de l'hydrogène vaut $B_\mathrm{H} = 13.6\,$eV. Une rapide approximation nous donnerait que la température à laquelle a eu lieu la recombinaison est $T_\mathrm{rec} \approx B_\mathrm{H} / k_B \approx 1.5 \times 10^5\,$K, mais ce serait oublier que même à des températures plus basses l'Univers contient encore énormément de photons d'énergie assez haute pour ioniser les atomes d'hydrogène. 

Une meilleure estimation doit donc reposer au moins sur le rapport baryon sur photon $\eta$ et $B_\mathrm{H}$. Comme pour l'abondance du deutérium, à l'équilibre on peut décrire 
\begin{align}
\frac{n_\mathrm{H}}{n_pn_e} & =\frac{g_\mathrm{H}}{g_p g_e} \left(\frac{k_B T}{2\pi \hbar^2}\right)^{-3/2}\left(\frac{m_\mathrm{H}}{m_p m_e}\right)^{3/2} \exp \left(\frac{(m_p+m_e-m_\mathrm{H})c^2}{k_B T} \right) \\
& \approx \left(\frac{m_e k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_\mathrm{H}}{k_B T}\right)
\end{align}
avec $g_\mathrm{H}=4$ et $g_p=g_e=2$. C'est *l'équation de Saha*. Posons $X_e$ la fraction d'électron libre dans le plasma primordial :
$$X_e = \frac{n_e}{n_b}$$
Par neutralité électrique et conservation du nombre de particules, on a aussi :
$$n_e=n_p,\quad X_e=\frac{n_p}{n_b}= \frac{n_p}{n_p + n_\mathrm{H}} $$
en supposant qu'il n'y a que de l'hydrogène pour simplifier les calculs. Par conséquent, on a :
\begin{equation}
\frac{1-X_e}{X_e} = n_p \left(\frac{m_e k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_\mathrm{H}}{k_B T}\right)
\end{equation}
et :
$$n_p = X_e \eta  n_\gamma = \eta X_e  \frac{2\zeta(3)}{\pi^2}\left(\frac{k_B T}{\hbar c}\right)^3 $$
donc :
\begin{equation}
\frac{1-X_e}{X_e^2} = \frac{2\zeta(3)}{\pi^2}\eta \left(2\pi\frac{k_B T}{m_e c^2}\right)^{3/2}  \exp\left(\frac{B_\mathrm{H}}{k_B T}\right) \equiv a_\mathrm{H}
\end{equation}
On a une équation du second degré en $X_e$ dont la solution est ({cite}`ryden2017` p.192) :
$$X_e = \frac{-1 + \sqrt{1+ 4a_\mathrm{H}}}{2a_\mathrm{H}}$$
On définit le moment de la recombinaison comme celui où le milieu est moins qu'à moitié ionisé soit $X_e = 1/2$, alors la température du découplage est donnée par {cite:p}`ryden2017` :
$$k_B T_{\mathrm{rec}} = 0.32\,\mathrm{eV} = \frac{B_\mathrm{H}}{42}$$
$$ \boxed{T_{\mathrm{rec}} = 3760\,\mathrm{K},\quad z_\mathrm{rec} = 1378}$$
soit quand l'Univers avait $t_\mathrm{rec} = 250\,000$ ans et alors que son évolution est dorénavant dominée par son contenu en matière. D'après la [](#fig:saha_Xe), on voit toutefois que la recombinaison s'étend globalement entre les redshift 1200 et 1600, se qui correspond tout de même à environ $70\,000$ ans, ce n'est donc pas un processus instantané. 

:::{figure} #saha_Xe
:name: fig:saha_Xe
:width: 70%

Fraction d'ionisation $X_e$ en fonction du redshift pendant la recombinaison.
:::

### Photon decoupling

:::{figure} #rates_decoupling
:name: fig:rates_decoupling
:width: 70%

Comparaison entre le taux d'interaction $\Gamma_\gamma$ et le taux d'expansion $H$ en fonction du redshift.
:::

Pendant encore un certain temps, les photons restent couplés à la petite fraction d'électrons libres par la diffusion Thomson :
$$ e^- + \gamma \rightleftharpoons e^- + \gamma $$
Le taux d'interaction est donné par (voir section [](#eq:lpm_thomson)) :
$$\Gamma_\gamma = n_e \sigma_T c = n_b X_e \sigma_T c=  \frac{2\zeta(3)}{\pi^2} \eta  \sigma_T c\left(\frac{k_B T}{\hbar c}\right)^3$$
avec la section efficace de la diffusion Thomson :
$$\sigma_T = 0.665\,\mathrm{barns} = 6.65\times 10^{-29}\,\mathrm{m}^2$$
Le découplage a lieu lorsque ce taux d'interaction devient petit devant le taux d'expansion de l'Univers ([](#fig:rates_decoupling)), soit :
$$\Gamma_\gamma(T_\mathrm{dec}) = H(T_\mathrm{dec})$$
L'Univers étant dominé par la matière, on a :
$$H(T_\mathrm{dec}) = H_0 \sqrt{\Omega_m^0(1+z)^3} = H_0 \sqrt{\Omega_m^0} \left(\frac{T_\mathrm{dec}}{T_0}\right)^{3/2}$$
On aboutit à :
\begin{equation}
X_e(T_\mathrm{dec}) (k_B T_\mathrm{dec})^{3/2} \approx  \frac{\pi^2}{2\zeta(3)}\frac{H_0 \sqrt{\Omega_m^0} } {\eta  \sigma_T c} \left(\frac{k_B T_0}{\hbar c}\right)^{-3/2}
\end{equation}
Par une résolution numérique, on obtient :
$$\boxed{T_{\mathrm{dec}} = 0.26\,\mathrm{eV} = 3055\,\mathrm{K}, \quad z_{\mathrm{dec}}\sim 1100,  \quad t_{\mathrm{dec}}=370\,000\,\mathrm{ans}}$$
Le fond diffus cosmologique est donc une lumière qui a été émise il y a environ $370\,000\,$ans et l'Univers n'était quasiment plus ionisé puisque $X_e(T_{\mathrm{dec}}) = 6\times 10^{-3}$. Avec l'expansion de l'Univers et la prédiction d'une abondance de $24\%$ d'hélium, l'existence de ce fonds diffus est un des trois piliers qui assoit la théorie du Big Bang.


:::{note} Profondeur optique

On définit la profondeur optique $\tau$ par le rapport du nombre de photons reçus sur Terre sans avoir subi aucune diffusion Thomson $N(t_0)$ sur le nombre de photons $N(t)$ émis à un instant $t$:
$$\frac{N(t_0)}{N(t)} = e^{-\tau}$$
avec
$$\tau = \int_t^{t_0} \Gamma_\gamma(t) \mathrm{d}t$$
Le temps $t_{\mathrm{ls}}$ pour lequel $\tau=1$ est appelé temps de dernière diffusion. C'est le temps depuis lequel un photon du CMB n'a plus interagi avec un électron. Plus précisément,
\begin{equation}
\tau(z) = \int_0^z \frac{\Gamma_\gamma(z)}{H(z)}\frac{\dd z}{1+z}
\end{equation}
C'est un des six paramètres du modèle standard $\Lambda$CDM. En effet, après l'émission du fond diffus cosmologique, on entre dans les Ages Sombres de l'Univers, où l'Univers est transparent mais aucun astre n'émet encore de lumière. Mais avec l'apparition des premières étoiles et galaxies, peut-être 150 millions d'années après le Big Bang, le milieu neutre est de nouveau ionisé. Bien que très peu dense, les photons du CMB interagissent de nouveau avec les électrons par diffusion Thomsom, ce qui diminue l'amplitude des anisotropies de petites échelles dans le spectre de puissance du CMB, et introduit de nouvelles anisotropies dans les anisotropies de polarisation. C'est le paramètre le moins bien mesuré du modèle $\Lambda$CDM pour le moment, mais il informe sur l'apparition des premiers astres lumineux.

```{figure} ../images/tau_history.png
:width: 80%
:align: center
:label: fig:tau

The optical depth to reionization $\tau$ (d'après [](https://lambda.gsfc.nasa.gov/education/graphic_history/taureionzation.html), image credit: NASA / LAMBDA Archive Team).
```

:::

[^mp]: on rappelle que les masses des protons et neutrons sont d'environ 1\,GeV.
[^Tfreeze]: dans un certains nombres de référence, ont trouve comme température de gel des neutrons $T_{\mathrm{freeze}} \ approx 0.8\,\MeV$ ce qui correspond aussi à 1 neutron pour 5 protons si on suit la distribution d'équilibre [](#eq:np_eq) mais en admettant que cette température est un ordre de grandeur bien trouvé pour que ça marche à la fin.

