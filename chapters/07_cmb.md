---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---

Histoire thermique de l'Univers
===============================

L'expansion cosmique réduit la quantité de mouvement des particules d'un facteur $\propto
a^{-1}$ et la densité des particules d'un autre $a^{-3}$.  Dans les premiers temps, l Univers était donc un état chaud et dense, dans lequel les particules pouvaient
échanger de l'énergie et de la quantité de mouvement de manière assez efficace, en d'autres termes, une sorte de plasma à température élevée en équilibre thermique.
une sorte de plasma à température élevée en équilibre thermique (ou proche de l'équilibre thermique).
d'un certain type d'équilibre thermique).


Le rayonnement cosmique est probablement la preuve la plus directe de cet état de fait.  Nous avons vu que
l'Univers est rempli d'un gaz de photons micro-ondes suivant un spectre de
spectre du corps noir :
\begin{equation}
  I_\nu = \frac{8\pi \nu^3}{\exp(\nu/T_0) - 1}
\end{equation}
avec $T_0 = 2,726 K$. Les photons du CMB ne sont _pas_ en équilibre thermique avec quoi que ce soit : l'équilibre thermique implique des échanges fréquents d'énergie et de momentum par le biais de collisions entre particules, alors que l'immense majorité des photons du CMB n'ont jamais été en contact avec des particules. majorité des photons du CMB n'ont jamais interagi depuis leur émission.
Cependant, cette absence d'interactions a préservé la forme originale du spectre du CMB, qui n'a été affecté que par le décalage vers le rouge. Un photon détecté à la fréquence $\nu$ a été émis à l'origine à la fréquence $\nu(1+z)$. En d'autres termes, le spectre d'origine était le suivant :
\begin{equation}
  I_\nu \propto \frac{8\pi \nu^3}{e^{\nu/((1+z) T_0)} - 1}
\end{equation}
c'est-à-dire toujours une forme de corps noir, avec une température $(1+z) T_0$.  Ceci Cela suggère que les photons du CMB étaient en équilibre thermique lorsqu'ils ont été émis, et plus généralement que les photons du CMB étaient en équilibre thermique lorsqu'ils ont été émis. émis, et plus généralement, que le plasma primordial chaud était en équilibre thermique. en équilibre thermique.

Dans ce chapitre, nous discutons des propriétés de ce plasma primordial précoce. primordial. 

L'Univers à $z \sim 10000$
--------------------------

Remontons bien au-delà du décalage vers le rouge de la dernière surface de diffusion, et considérons l'Univers à, disons, $z_1 \sim 10 000$. Que pouvons-nous en dire ? à son sujet ?

Tout d'abord, nous savons qu'il est dominé par le rayonnement.  En effet, nous avons vu dans les devoirs que le décalage vers le rouge de l'égalité matière-rayonnement est : $1+z_{eq} = \Omega_m/\Omega_r \approx 3450$, assez longtemps après $z. = 10000$\footnote{Exercice : combien de temps ?}. Etant dominé par le rayonnement l'Univers se dilate comme $a \propto t^{1/2}$.

### Taux d'expansion

La valeur du paramètre de Hubble à $z_1$ peut être déduite de l'équation de Friedmann équation de Friedmann :
\begin{equation}
  H(z) = H_0 \left( \Omega_m(1+z)^3 + \Omega_r (1+z)^4 + \Omega_X (1+z)^{3(1+z)}\right)^{1/2}
\end{equation}
Prenons les valeurs canoniques $\Omega_m = 0.3$, $\Omega_X = 0.7$ et $w = -1$. Pour la densité de rayonnement, nous avons vu en classe que $\Omega_\gamma = 10^{-5}$ (à partir de la température du CMB). A cela, il faut
ajouter la contribution des neutrinos (voir plus loin dans ce chapitre), ce qui donne un total de $\approx 9 \times 10^{-5}$ pour la densité de rayonnement. Cela donne :
\begin{equation}
  H(z_1) = 1.1\ 10^6 \times H_0
\end{equation}
L'expansion de l'Univers était beaucoup plus rapide qu'aujourd'hui !

### Photons
Concentrons-nous maintenant sur les propriétés des photons.  Nous savons que $T_\gamma \propto a^{-1}$, donc :
\begin{equation}
  T_\gamma(z_1) \approx 2.726\times 10^{4}
\end{equation}
L'énergie moyenne des photons du CMB est :
\begin{equation}
  2.7 k_B T_0(z_1) = 2,7 k_B T_0 (1+z_1) \approx 6.34 \mathrm{eV}
\end{equation}
à comparer avec la valeur actuelle de $6.34\times 10^{-4} eV$. Enfin, la densité de photons est $(1+z_1)^3 \approx 10^{12}$ la densité de photons aujourd'hui, c'est-à-dire
\begin{equation}
  n_\gamma \approx 4.11\times 10^{20}\ \gamma / \mathrm{m^3}
\end{equation}

### Baryons

La densité de baryons à $z_1$ peut être calculée de la même manière. Rappelons que la densité de baryons est aujourd'hui de $\Omega_b \approx 0.048$. Avec une densité critique de $5.49\ \mathrm{protons / m^{-3}}$,  cela donne environ $n_b \approx 0.263 \mathrm{baryons / m^{-3}}$ et :
\begin{equation}
  n_b \approx 0.263\ 10^{12}  \mathrm{baryons / m^{-3}}\text{ et } n_b \approx 0.263\ 10^{12}.
\end{equation}

### Moyen libre parcours des photons

Enfin, on peut s'interroger sur le libre parcours moyen des photons. Les photons interagissent préférentiellement avec les électrons par diffusion Thomson et une bonne approximation du libre parcours moyen des photons est donnée par :
\begin{equation}
  \frac{1}{\sigma_T n_e c}
\end{equation}
où $\sigma_T$ est la section efficace de diffusion de Thomson ($6.6529\times 10^{-29} \mathrm{m^2}$), $c$, la vitesse de la lumière (vitesse du photon). Pour la densité électronique, considérons que l'Univers étant neutre, il y a un électron pour chaque proton et $n_p \approx 0.2\times \mathrm{m^{-3}}$. Cela donne :
\begin{equation}
  \frac{1}{\sigma_T n_e c} \approx 7.9\ 10^{12} \mathrm{yr} \gg t_H
\end{equation}
aujourd'hui et
\begin{equation}
  \frac{1}{\sigma_T n_e(1+z_1)^3 c} \approx 7.9 \mathrm{yr} \ll t_H
\end{equation}
à l'époque.

### En résumé 

L'Univers à $z \approx 10,000$ était beaucoup plus chaud et plus chaud et plus dense. 
La densité du nombre de photons était significativement baryons et des électrons, comme aujourd'hui, 
mais les densités d'énergie des les densités d'énergie des photons et des baryons étaient comparables.
Enfin, les interactions entre photons et particules chargées étaient beaucoup plus fréquentes 
(plusieurs par temps de Hubble), il est donc tout à fait logique de considérer l'Univers comme 
un fluide en équilibre thermique. 
Dans la section, nous introduisons les outils de la thermodynamique d'équilibre.

Thermodynamique à l'équilibre
-------------------------------

Nous modélisons les fluides de l'Univers comme un gaz de particules interagissant faiblement. Nous utilisons le formalisme de la physique statistique et décrivons le gaz par les positions et les moments de toutes ses particules. les positions et les moments de toutes ses particules.  Pour rester pratiques, nous utilisons des fonctions de distribution définies sur l'espace $\{\vec{x}, \vec{p}\}$.

La mécanique quantique nous apprend que la densité des états dans l'espace est limitée. Considérons une boîte de taille $L$, avec des conditions périodiques et résolvons l'équation de Schrodinger, nous obtenons que les valeurs possibles de la quantité de mouvement sont :
\begin{equation}
  \vec{p} = \frac{h}{L}\left(n_x \vec{x} + n_y \vec{y} + n_z \vec{z}\right), \ \ \ n_i = 0, \pm 1, \pm 2, \ldots
\end{equation}
où $\vec{x}, \vec{y}$ et $\vec{z}$ sont les vecteurs unitaires et $h$ est la constante de Planck. En conséquence, la densité d'état dans l'espace des quantités de mouvement est :
\begin{equation}
  \frac{L^3}{h^3} = \frac{V}{h^3}
\end{equation}
et la densité d'état dans l'espace des phases est :
\begin{equation}
  \frac{1}{h^3} = \frac{1}{(2\pi)^3 \hbar^3}
\end{equation}
ou simplement $1 / (2\pi)^3$ dans un système d'unités où $\hbar = 1$.  Comme on peut comme on le voit, la densité d'état est indépendante du volume. Elle reste la même pour un système arbitrairement grand.  Si les particules ont $g$ degrés de liberté
 degrés de liberté internes (par exemple le spin), la densité d'états est :
\begin{equation}
  \frac{g}{(2\pi)^3 \hbar^3}
\end{equation}

Les propriétés (densité de nombre, densité d'énergie, pression) d'un gaz donné
dépendent de la fonction de distribution $f(\vec{x}, \vec{p}, t)$,
qui décrit comment les particules sont distribuées dans l'espace des phases.
En raison de l'homogénéité, $f$ ne peut pas varier en fonction de $\vec{x}$.
En raison de l'isotropie, $f$ ne peut dépendre que de la norme de la quantité de mouvement
$p \equiv |\vec{p}|$. Le nombre de particules d'impulsion $p$ est donné par :
\begin{equation}\label{eqn:fweights}
  \frac{g}{(2\pi)^3} f(p,t)
\end{equation}

Connaissant la fonction de distribution, nous pouvons calculer les propriétés macroscopiques du gaz,
en particulier, la densité numérique :
\begin{equation}
  \boxed{n = \frac{g}{(2\pi)^3} \int d^3p f(p)}
  \label{eqn:number_density_general}
\end{equation}

Pour la densité d'énergie, il suffit de faire la somme des énergies des particules
pondérées par \ref{eqn:fweights}. 
\begin{equation}
  \boxed{\rho = \frac{g}{(2\pi)^3} \int d^3 p f(p) \sqrt{p^2 + m^2}}
  \label{eqn:energy_density_general}  
\end{equation}
Nous avons supposé ici que nous pouvions ignorer les énergies d'interaction
entre les particules (c'est-à-dire que nous avons affaire à un gaz de particules
particules interagissant faiblement). Dans ce cas, l'énergie est donnée par : $E(p) =
\sqrt{p^2 + m^2}$ et les états disponibles sont en effet les états de particules libres décrits ci-dessus.
décrits ci-dessus.

Nous pouvons obtenir de la même manière la pression du gaz : 
\begin{equation}
  \boxed{P = \frac{g}{(2\pi)^3} \int d^3p f(p) \frac{p^2}{3E}}
  \label{eqn:pression_générale}
\end{equation}
On peut se demander d'où vient ce $p^2/3E$. Nous l'expliquons
dans l'encadré ci-dessous. 

:::{note} Pourquoi $p^2/3E$ ?

Considérons un élément de surface $\delta A$. Nous notons $\hat{n}$ son vecteur unitaire. Les particules de vitesse $v$ qui frappent $\delta A$ entre $t$ et $t + \delta t$ sont situées dans une coque sphérique autour de
$\delta$, entre les rayons $vt$ et $v(t + \delta t)$.

\begin{equation}
  \dd N = \frac{g}{(2\pi)^3} f(E) R^2 v \dd t \dd\Omega 
\end{equation}

Toutes ces particules n'atteignent pas la surface. Seules celles dont la vitesse sont dirigées vers $\delta A$, c'est-à-dire celles dont le vecteur vitesse est dans l'angle solide sous-tendu par $\delta A$.
angle solide sous-tendu par $\delta A$. Donc :
\begin{equation}
  \begin{split}
    \dd N_{hit} & = \dd N \times \frac{|\hat{v}\cdot\hat{n}|}{4\pi R^2} \\
            & = \frac{g}{(2\pi)^3} f(E) \frac{\hat{v}\cdot\hat{n}}{4\pi}\ \dd A\ \dd t\ \dd\Omega
  \end{split}
\end{equation}  
Supposons que les interactions soient élastiques et que chaque particule  transfère une quantité de mouvement $2|\vec{p}\vec{n}|$ à la surface. La pression  pression résultante est :
\begin{equation}
  \begin{split}
    \dd P(v) & = \int \frac{2|\vec{p}\cdot\vec{n}|}{\dd A\ \dd t} \dd N_A \\ & = \frac{2|\vec{p}\cdot\vec{n}|}{\dd A\ \dd t} \dd N_A \\
    & = \frac{g}{(2\pi)^3} f(E) \frac{p^2}{2\pi E} \int \cos^2\theta \sin\theta \dd\theta \dd\phi \\ & = \frac{g}{(2\pi)^3} f(E) \\
    & = \frac{g}{(2\pi)^3} f(E) \frac{p^2}{3E}
  \end{split}  
\end{equation}

:::

### L'équilibre cinétique

Lorsque les particules peuvent échanger souvent de l'énergie et de la quantité de mouvement, le gaz atteint un état d'entropie maximale, appelé équilibre cinétique.
un état d'entropie maximale, appelé équilibre cinétique. C'est un
de la physique statistique que les fonctions de distribution de l'entropie
des fermions et des bosons sont données par les fonctions de distribution de l'entropie maximale de _Fermi-Dirac_ et _Bose-Einstein_ respectivement :
\begin{equation}
  \boxed{f(p) = \frac{1}{\exp\left({\frac{E(p) - \mu}{T}}\right) \pm 1}}
\end{equation}
$(+)$ étant pour Fermi-Dirac et (-) pour Bose-Einstein. Ces fonctions
peuvent être dérivées en évaluant l'entropie du gaz ($S = \ln \Gamma$)
en fonction de l'énergie, et en la maximisant, pour une énergie totale donnée
et un nombre total de particules donné.

A basse température, on retrouve la fameuse distribution de Maxwell-Boltzmann bien connue de Maxwell-Boltzmann :
\begin{equation}
  \boxed{f(p) = \exp\left(-{\frac{E(p) - \mu}{T}}\right)}
\end{equation}
est valable pour les fermions et les bosons.

Les fonctions de distribution de Fermi-Dirac et de Bose-Einstein dépendent de deux paramètres : la température du gaz, $T$, et le potentiel chimique de l'espèce $\mu$, qui caractérise la variation d'entropie ou d'énergie lorsque le nombre de particules varie (voir détails dans détails dans l'encadré ci-dessous).

:::{note} Potentiel chimique

Les variations d'énergie d'un système peuvent être exprimées en fonction de de son entropie, de son volume et de sa température :
\begin{equation}
\dd E = T \dd S - P \dd V + \mu \dd N
\end{equation}
ou encore, les variations d'entropie du même système peuvent être écrites comme suit :
\begin{equation}
\dd S = \frac{\dd E}{T} + \frac{P}{T} \dd V - \frac{\mu}{T} \dd N
\end{equation}

Considérons deux systèmes $S_1$ et $S_2$ à des températures $T_1$ et $T_2$ mis en contact.  Si les deux systèmes sont isolés (1), l'énergie l'énergie totale de ($S1+S2$) est constante 
$$\dd E = \dd E_1 + \dd E_2 = 0 \Rightarrow \dd E_1 = -\dd E_2$$
(2) l'entropie de ($S_1 + S_2$) atteint un maximum : 
$$\dd S = \dd S_1 + \dd S_2 = 0 \Rightarrow \dd E_1/T_1 + \dd E_2/T_2 = 0$$
ce qui donne $T_1 = T_2$ à l'équilibre.

Considérons maintenant que $S_1$ et $S_2$ peuvent échanger des particules (en gardant le nombre total de particules constant). Nous avons (1) $\dd N = \dd N_1 + \dd N_2 = 0 \Rightarrow \dd N_1 = - \dd N_2$ et (2) l'entropie de $(S_1 + S_2)$ atteint un maximum, ce qui donne : $-\frac{\mu_1}{T} \dd N_1 - \frac{\mu_2}{T} \dd N_2 = 0$ d'où $\mu_1 = \mu_2$. À l'équilibre, les deux potentiels chimiques sont égaux.

Considérons maintenant le cas d'une réaction chimique : 
$$1 + 2 \leftarrow 3 + 4$$
c'est-à-dire le cas de quatre systèmes $S_1$, $S_1$, $S_2$, $S_3$ et $S_4$ mis en contact. En suivant le même même raisonnement, on peut montrer que (1) ils atteignent une même température d'équilibre température $T$ et (2) qu'à l'équilibre, on a :
$$\mu_1 + \mu_2 = \mu_3 + \mu_4 = \mu_4$$

Plus généralement, lorsque nous avons une charge conservée $Q = \sum_i q_i N_i$, on obtient une contrainte : $dQ = 0 = \sum_i q_i \dd N_i$, ainsi que la contrainte d'entropie maximale : $\sum_i \mu_i \dd N_i = 0$. Cela signifie qu'il existe une constante $\mu$ telle que $\mu_i = \mu q_i$.
:::

Si le gaz contient plusieurs espèces en interaction, chaque espèce $i$ est décrite par sa propre fonction de distribution, son propre potentiel chimique $\mu_i$. chimique $\mu_i$, et éventuellement (si elle est découplée) sa propre température $T_i$.  Nous pouvons en déduire la densité de nombre, la densité d'énergie et la température de chaque espèce. d'énergie et la température de chaque espèce.

Si toutes les espèces sont en équilibre cinétique et partagent la même température : $T_i = T$, le système a atteint _thermal thermique_.


### Equilibre chimique

Nous avons vu dans l'encadré ci-dessus que si plusieurs espèces interagissent par le biais d'une réaction, par exemple :
\begin{equation}
  \nu_1 X_1 + \nu_2 X_2 + \ldots \leftrightharpoons \nu'_1 Y_1 + \nu'_2 Y_2 + \ldots
\end{equation}
et atteignent l'équilibre chimique (c'est-à-dire l'état d'entropie maximale), les potentiels chimiques satisfont : 
\begin{equation}
  \sum_i \nu_i \mu_i = \sum_j \nu'_j \mu_j 
\end{equation}
plus toute équation de conservation imposée par une charge conservée (nombre de particules, charge électrique, charge baryonique, etc.)

Pour les photons, il n'y a pas de charge conservée. Même le nombre de photons n'est pas conservé.  Par exemple, nous avons une double diffusion Compton $e^- + \gamma \leftrightharpoons e^- + \gamma + \gamma$ ou Bremstrahlung  $e^- + p \Rightarrow e^- + p + \gamma$. D'où :
\begin{equation}
  \mu_\gamma = 0
\end{equation}

Les particules et les antiparticules sont de charges opposées, d'où,
_à l'équilibre_ :
\begin{equation}
  \mu_X = -\mu_{\bar{X}}
\end{equation}
(on peut aussi utiliser la réaction $X + \bar{X} \leftrightharpoons \gamma + \gamma$ pour arriver à la même conclusion).

En résumé, Une espèce de système a atteint l'équilibre cinétique si elle a atteint un état d'entropie maximale entropie maximale décrite par une fonction de distribution de Fermi-Dirac ou de Bose-Einstein. de Bose-Einstein.  Un système composé de plusieurs espèces interagissant par une ou plusieurs réactions chimiques a atteint l'équilibre chimique chimique s'il a atteint un état d'entropie maximale, où la somme des potentiels chimiques des réactions est égale ou supérieure à la somme des potentiels chimiques des réactions. des potentiels chimiques des réactifs est égale à la somme des potentiels chimiques des produits. des potentiels chimiques des produits.  Un système a atteint l'équilibre thermique thermique s'il a atteint l'équilibre chimique et si toutes les espèces partagent la même température.

Densité et pression des fermions et bosons
----------------------------------------------

Nous avons maintenant tout ce qu'il faut pour calculer la densité de nombre, la densité d'énergie et la pression des constituants de l'univers. d'énergie et la pression des constituants de l'univers. Comme le montre l'encadré ci-dessous, les potentiels chimiques peuvent être négligés en toute sécurité, et les équations \ref{eqn:number_density_general}, \ref{eqn:densité_énergétique_générale} et \ref{eqn:pression_générale} peuvent être réécrites :
\begin{equation}
  \begin{split}
    n &= \frac{g}{2\pi^2} \int \dd p \frac{p^2}{\exp\left(\sqrt{p^2 + m^2}/T\right) \pm 1} \\
    \rho &= \frac{g}{2\pi^2} \int \dd p \frac{p^2 \sqrt{p^2 + m^2}}{\exp\left(\sqrt{p^2 + m^2}/T\right) \pm 1} \\
    P &= \frac{g}{2\pi^2} \frac{1}{3} \int \dd p \frac{p^4}{\sqrt{p^2 + m^2} \left[\exp\left(\sqrt{p^2 + m^2}/T\right) \pm 1\right]}\\    
  \end{split}
\end{equation}

Dans le cas général, les intégrales ci-dessus doivent être calculées numériquement. Il existe cependant deux limites intéressantes, qui permettent de de comprendre les processus physiques en cours : le cas où les particules sont relativistes, c'est-à-dire $T \gg m$ et le cas opposé d'espèces espèces non relativistes : $T \ll m$. 

Avant de poursuivre, définissons : $x \equiv m/T$ et $\xi \equiv p/T$,
nous pouvons alors réécrire $n$ et $\rho$ ci-dessus comme :
\begin{equation}
  \begin{split}
    n &= \frac{g}{2\pi^2} T^3 I_\pm(x) \ \ \ \mathrm{with} \ \ I_\pm(x) = \int_0^\infty \dd \xi \frac{\xi^2}{\exp\left(\sqrt{\xi^2 + x^2}\right) \pm 1} \\
    \rho &= \frac{g}{2\pi^2} T^4 J_\pm(x) \ \ \ \mathrm{with}\ \ J_\pm(x) = \int_0^\infty \dd \xi \frac{\xi^2 \sqrt{\xi^2 + x^2}}{\exp\left(\sqrt{\xi^2 + x^2}\right) \pm 1} \\
  \end{split}
\end{equation}


### Limite relativiste

Dans la limite relativiste, nous pouvons négliger $x$ et les intégrales
$I_\pm(0)$ et $J_\pm(0)$ peuvent être calculées exactement, à condition d'être familier avec les fonctions $\Gamma$ et $\zeta$ (voir l'encadré ci-dessous). Nous
trouvons :

\begin{equation}
  \boxed{\begin{aligned}
           &        \mathrm{Bosons}                       &  \mathrm{Fermions} \\
    n    = & \frac{\zeta(3)}{\pi^2} g T^3  & \frac{3}{4} \frac{\zeta(3)}{\pi^2} g T^3 \\
    \rho = & \frac{\pi^2}{30} g T^4        & \frac{7}{8}\frac{\pi^2}{30} g T^4 \\
  \end{aligned}}
  \label{eqn:n_rho_relativistic_limit}
\end{equation}

For the pressure, we have $p^2 / E \sim p$ for relativistic particles. We find that:
\begin{equation}
  P = \frac{1}{3} \frac{g}{2\pi^2} T^4 \int \dd \xi \frac{\xi^3}{\exp\xi \pm 1} = \frac{1}{3} \frac{g}{2\pi^2} T^4 J_\pm(0) = \frac{\rho}{3}
  \label{eqn:P_relativistic_limit}
\end{equation}
We recover the equation of state of radiation (we used it when computing the expansion rate for a radiation dominated Universe).

Another known fact we can recover from the integrals above is the CMB photon density:

:::{exercise}

Using $T_0 = 2.726 K$, compute the photon number density (today) and
the photon energy density (today). Show that:
\begin{equation*}
  \begin{split}
    n_\gamma & = 411\ \mathrm{cm}^{-3}\\
    \rho_\gamma &= 4.6 \times 10^{-34}\ \mathrm{g/cm^{3}} \\
    \end{split}
  \end{equation*}
  and recover the CMB photon density today (in units of the critical density):
  \begin{equation*}
    \Omega_\gamma = 2.5 h^{-2} 10^{-5}
  \end{equation*}
  To get the correct numerical answer, you will need to do a little bit of dimensional analysis.  Where did we drop the physical constant(s) you had to retrieve ?
:::


:::{note} Computing $I_\pm(0)$ and $J_\pm(0)$

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


### Limite non relativiste

Dans la limite non relativiste, l'énergie des particules est égale à leur masse au repos : $m \gg T$, c'est-à-dire $x \gg 1$. Les intégrales $I$ et $J$ définies ci-dessus sont les mêmes pour les fermions et les bosons et nous trouvons :

\begin{equation}
  \boxed{\begin{aligned}
    n    &\approx g \left(\frac{m T}{2\pi}\right)^{3/2} \exp\left(-\frac{m}{T}\right) \\
    \rho &\approx n m \\
    P    &= n T \ll \rho = m n \\
  \end{aligned}}
\end{equation}
Lorsque la température descend en dessous de la masse au repos des particules, la densité du nombre de particules chute exponentiellement : les particules massives et leurs antiparticules s'anihilent tandis que l'énergie du bain de photons n'est plus suffisante pour équilibrer les anihilations par la production de paires particule-antiparticule.  La densité d'énergie et la pression sont (au premier ordre) proportionnelles à $n$ et diminuent en conséquence. Les espèces non relativistes se comportent donc comme un gaz sans pression, dont la densité d'énergie est égale à la densité de masse.  C'est cette description de la matière non relativiste que nous avons utilisée pour calculer l'expansion de l'Univers dans le régime dit "dominé par la matière".

:::{note} Calcul de la densité de nombre dans le régime non relativiste

Dans le régime non relativiste, seule la densité de particules est quelque peu délicate à calculer.  Avec les mêmes définitions que ci-dessus : $x\equiv m/T$, $\xi \equiv p/T$ et $x \gg 1$, les intégrales $I_-$ et $I_+$ se réduisent à une seule expression :
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


Histoire thermique de l'Univers jeune
--------------------------------------

Nous avons maintenant (presque) tout ce dont nous avons besoin pour discuter de l'évolution du plasma primordial. Lorsque la température est suffisamment élevée, le plasma primordial contient toutes les particules du modèle standard, sous forme relativiste (plus toutes les particules qui n'ont pas encore été découvertes, par exemple les particules hypothétiques qui constituent la matière noire froide).

Dans l'Univers primitif, toutes les espèces de particules sont en équilibre thermique (cinétique et chimique, même température $T$).  Au fur et à mesure de l'expansion de l'Univers, la température diminue ($T \propto a^{-1}$). L'une après l'autre, les différentes espèces massives deviennent non relativistes, s'anéantissent, et leur densité d'énergie devient sous-dominante par rapport aux espèces relativistes.

Si l'Univers était en parfait équilibre thermique, et si cet équilibre avait persisté jusqu'à aujourd'hui, les abondances observées de particules massives seraient bien inférieures à ce qu'elles sont, puisque chaque espèce massive est exponentiellement supprimée lorsqu'elle devient non relativiste.  En fait, les équilibres thermiques et chimiques ont besoin de taux de collision (et/ou de réaction) fréquents pour être maintenus. Avec l'expansion de l'Univers, les particules se diluent, ce qui rend plus difficile le maintien des taux de réaction. Une bonne règle empirique est qu'il faut plusieurs réactions par temps de Hubble pour maintenir l'équilibre thermique. Ainsi, si
\begin{equation}
  \Gamma \gg H
\end{equation}
l'équilibre est maintenu. Lorsque le taux de réaction chute en dessous de $H$, l'équilibre thermique n'est plus maintenu, les densités de particules {\em freeze out} à leurs valeurs d'avant le découplage. {Le gel est un mécanisme essentiel pour expliquer l'abondance actuelle des particules.


### Nombre effectif d'espèces relativistes

Nous partons d'un plasma primordial en équilibre thermique et chimique. Toutes les espèces partagent la même température que nous notons $T$. $T$ est en particulier la température du bain de photons.

Le taux d'expansion est une fonction directe de la densité d'énergie totale :
\begin{equation}
  H^2 = \frac{8\pi G}{3} \rho(T)
\end{equation}
où $\rho(T)$ est la somme des densités de chaque espèce présente dans le fluide primordial.
dans le fluide primordial.
\begin{equation}
  \rho(T) = \sum_i \rho_i(T)
\end{equation}
nous avons vu dans la section précédente que $\rho_i \propto T^4$ tant que la particule reste relativiste, et tombe à presque rien quand la température tombe en dessous de la masse de la particule. Plus précisément, nous pouvons écrire
\begin{equation}
  \rho(T) = \frac{\pi^2}{30} g_\star(T) T^4
\end{equation}
où $g_\star(T)$ est le nombre effectif de degrés de liberté {\em relativiste} du plasma à la température $T$ : 
\begin{equation}
  g_\star(T) = \sum_{i=b} g_i + \frac{7}{8}\sum_{i=f} g_i
  \label{eqn:g_star_same_temp}
\end{equation}
Lorsque la température descend en dessous de la masse de l'une des espèces, $m_i$, elle devient relativiste et disparaît de la somme ci-dessus.  Dans les intervalles entre les masses des particules, $g_\star(T)$ reste pratiquement constant.  Comme le rayonnement domine, nous avons $p = \rho/3$ et donc $\rho \propto a^{-4}$. Puisque $\rho \propto T^{4}$, nous avons l'habituel
\begin{equation}
  \boxed{T \propto a^{-1}}
\end{equation}
dans le plasma primordial.

### Expansion du plasma primordial

La loi d'expansion obéit à la première équation de Friedmann, que nous connaissons bien maintenant :
\begin{equation}
  H^2 = \frac{8\pi G}{3} \rho = \frac{8\pi G}{3} \frac{\pi^2}{30} g_\star(T) T^4
\end{equation}
et donc :
\begin{equation}
  \boxed{H = \sqrt{\frac{8 \pi^3 G}{90}} g_\star^{1/2}(T) T^2}
\end{equation}
Ainsi, $H \propto T^2$ modulo les variations du nombre effectif de degrés de liberté dans le plasma primordial.  Gardez cela à l'esprit, cela sera utile lorsque vous comparerez le taux d'expansion avec les divers taux de réaction entre les différentes espèces.

De plus, comme l'Univers est dominé par le rayonnement, nous avons :
\begin{equation}
  H = \frac{1}{2 t}\ \ \ \ \ (a \propto t^{1/2})
\end{equation}
ce qui donne
\begin{equation}
  \boxed{T \approx [10^{10} \mathrm{K}] \left(\frac{t}{\mathrm{1\ sec}}\right)^{-1/2}} 
\end{equation}
Ou, de manière équivalente, nous pouvons dériver l'évolution de l'énergie typique des particules en fonction du temps.
\begin{equation}
  \boxed{E \approx [3\ \mathrm{MeV}]\ \left(\frac{t}{\mathrm{1\ sec}}\right)^{-1/2}}  
\end{equation}
Ainsi, lorsque l'Univers était âgé d'une seconde, l'énergie typique des particules était de l'ordre de 1 MeV.


### Évolution du plasma primordial



\begin{table}
  \begin{center}
    \caption{Particles of the standard model.}
    \label{tab:sm_particles}
  \begin{tabular}{lcrcl}
    \hline
    \hline
    Type   & & mass & spin & g \\
           & &      &      &   \\
    \hline
    quarks & $t,\bar{t}$ & 173 GeV & $\frac{1}{2}$ & $2 \cdot 2 \cdot 3 = 12$ \\
           & $b,\bar{b}$ &   4 GeV &               &                          \\
           & $c,\bar{c}$ &   1 GeV &               &                          \\
           & $s,\bar{s}$ & 100 MeV &               &                          \\
           & $d,\bar{d}$ &   5 MeV &               &                          \\            
           & $u,\bar{u}$ &   2 MeV &               &                          \\                
    \hline
    gluons & $g_i$       &    0    & 1             & $8 \cdot 2 = 16$ \\
    \hline
    leptons & $\tau^\pm$ & 1777 MeV &  $\frac{1}{2}$ & $2 \cdot 2 = 4$ \\
            & $\mu^\pm$  &  106 MeV &                &                 \\
            & $e^\pm$    &  511 keV &                &                 \\
            & $\nu_\tau, \bar{\nu}_\tau$ & $< 0.6$eV &  $\frac{1}{2}$ & $2 \cdot 1 = 2$ \\
            & $\nu_\mu, \bar{\nu}_\mu$   & $< 0.6$eV &                &                 \\
            & $\nu_e, \bar{\nu}_e$      & $< 0.6$eV &                &                 \\        
    \hline
    gauge bosons & $W^+$ & 80 GeV  & 1 & 3 \\
                 & $W^-$ & 80 GeV  & 1 & 3 \\
                 & $Z^0$ & 91 GeV  & 1 & 3 \\
                 & $\gamma$ & 0    & 1 & 2 \\
    \hline
    Higgs boson  & $H$   & 125 GeV & 0 & 1 \\
    \hline 
  \end{tabular}
  \end{center}
\end{table}

:::{figure} #gtable
:name: tab:gtable
:::

La dernière pièce manquante est l'évolution de $g_\star$, qui raconte simplement l'évolution du plasma primordial au fur et à mesure qu'il se refroidit avec l'expansion.  Commençons autour de $T \leq 100 $GeV. Toutes les particules du modèle standard sont relativistes (voir le tableau \ref{tab:sm_particles}).  Lorsque toutes les particules sont relativistes, le nombre total de degrés de liberté est de :
\begin{equation}
  g_f = \underbrace{6 \times 12}_{\mathrm{quarks}} + \underbrace{3 \times 4}_{\ell^\pm} + \underbrace{3 \times 2}_{\nu's} = 90
\end{equation}
pour les fermions, et
\begin{equation}
  g_b = \underbrace{8 \times 2}_{g_i's} + \underbrace{3 \times 3}_{W,Z} + \underbrace{2}_{\gamma} + \underbrace{1}_{H}  = 28
\end{equation}
pour les bosons, ce qui donne
\begin{equation}
  g_\star = g_b + \frac{7}{8} g_f = 106.75
\end{equation}

Pour voir ce qui va se passer ensuite, il suffit de regarder les masses des particules énumérées dans le tableau \ref{tab:sm_particles}. Le quark supérieur s'annihile en premier, réduisant le nombre de degrés de liberté à :
\begin{equation}
  g_\star(T<m_{\mathrm{top}}) = 106.75 - \frac{7}{8} \times 12 = 96.25
\end{equation}
nous avons donc le Higgs, suivi des bosons électrofaibles $W^\pm$ et $Z^0$ : ce qui réduit $g_\star$ à 86.25. Ensuite, $b$ et $c$ s'annihilent, et $g_\star$ est alors réduit à 61,75.

L'événement suivant est la transmission de phase QCD, qui se produit à $T \sim 150\ \mathrm{MeV}$.  Les quarks se combinent en baryons (protons, neutrons et mésons), tous sauf les pions étant relativistes. A ce stade, les seules espèces relativistes restantes sont (1) les photons (2) dans la famille des leptons, les neutrinos, les électrons et les muons et (3) pour les baryons les pions de spin 0, d'où : $g_\pi = 3 \cdot 1 = 3$. Donc :
\begin{equation}
  g_\star = \underbrace{2}_{\gamma} + \underbrace{3}_{\pi} + \frac{7}{8} \times (\underbrace{4 + 4}_{e^{\pm}, \mu^\pm} + \underbrace{6}_{\nu's}) = 17.25
\end{equation}

\begin{figure}[t]
  \begin{enumerate}
    \includegraphics[width=0.9\linewidth]{g_star_T.png}
    \caption{L'évolution du nombre effectif d'espèces en fonction de $T$ (d'après Baumann).}
  \end{center}
\end{figure}
Ensuite, les pions et les muons s'annihilent, ce qui nous donne
\begin{enumerate}
  g_\star = 2 + \frac{7}{8} \N- fois (4 + 6) = 10,75
\end{equation}

:::{figure} #ggstar_plot
:name: fig:ggstar_plot
:::

Les deux événements significatifs suivants sont (1) le découplage des neutrinos autour de 1 MeV et (2) l'annihilation des électrons et des positrons ($m_e = 511 \mathrm{keV}$). C'est le sujet de la section suivante.



Découplage des neutrinos et annihilations électron-positron
--------------------------------------------------

### Découplage des neutrinos

Le découplage des neutrinos est notre première expérience de freeze-out.  Les neutrinos n'interagissent que par le biais de l'interaction faible.  Autour de $\sim$ 1 MeV, ils sont encore thermalisés par des interactions telles que :
\begin{equation}
  \begin{split}
    \nu_e + p & \rightleftharpoons p + e^- \\
    \nu_e + \bar{\nu_e} & \rightleftharpoons e^+ + p^- \\
    e^- + \nu_e & \rightleftharpoons e^+ + \nu_e \\    
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


\subsection{$e^+ - e^-$ anihilation}

Peu après le découplage des neutrinos vers 1 MeV, les électrons et les positrons s'anihilent (511 keV).  Naïvement, on pourrait dire que $g_\star(T)$ devient alors :
$$
2 + \frac{7}{8} \times 6 = 7,25
$$
mais la Nature est plus subtile.  En effet, l'anihilation électron-positron produit suffisamment d'énergie et d'entropie pour chauffer le bain de photons et modifier la température des photons.  Les neutrinos ne sont pas affectés et leur température varie toujours comme $a^-1$.  Par conséquent, après l'anihilation de $e^+-e^-$, nous avons $T_\nu < T_\gamma$.

Nous nous trouvons donc dans une nouvelle situation où nous avons plusieurs espèces relativistes avec des températures différentes.  Pour en tenir compte, nous pouvons modifier l'équation \ref{eqn:g_star_same_temp}, en permettant à chaque espèce d'avoir sa propre température :
\begin{equation}
  g_\star(T) = \sum_{\mathrm{bosons}} g_i \left(\frac{T_i}{T}\right)^4 + \frac{7}{8} \sum_{\mathrm{fermions}} g_i \left(\frac{T_i}{T}\right)^4
\end{equation}
Pour aller plus loin, nous devons déterminer $T_\nu$, ou plus exactement, relier $T_\nu$ et $T_\gamma$ (nous connaissons assez bien $T_\gamma$). La façon la plus simple de le faire est d'utiliser la conservation de l'entropie.



Conservation de l'entropie
-----------------------------

L'entropie de l'Univers ne peut qu'augmenter ou rester constante. Nous savons qu'à l'équilibre, l'entropie est conservée (voir encadré).  Le plasma primordial n'est pas {\em exactement} à l'équilibre\footnote{c'est heureux, sinon, nous ne serions pas là pour réfléchir à tout cela} : l'expansion n'en fait qu'un équilibre local, nous verrons de nombreux exemples de processus hors équilibre dans la suite de l'article.  Cependant, comme l'entropie est au premier ordre proportionnelle au nombre de particules, et que les photons sont de loin l'espèce la plus abondante dans l'Univers, nous pouvons supposer sans risque que l'entropie est conservée, et que, à une très grande précision, l'expansion cosmique est un processus adiabatique.

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


### La température du fond diffus cosmologique

Revenons à la détermination de la relation entre la température des photons et la température du fond de neutrinos cosmiques.
cosmique. Lors de l'annihilation, l'entropie et l'énergie du $e^\pm$ sont transférées au bain de photons. L'entropie étant conservée, nous avons, avant l'annihilation, démonté l'entropie des neutrinos (qui est conservée) :
\begin{equation}
  g^\gamma_{\star S, \mathrm{before}}(T) = 2 + \frac{7}{8} (4) = \underbrace{\frac{11}{2}}_{e^\pm, \gamma} 
\end{equation}
après annihilation : 
\begin{enumerate}
  g^\gamma_{{star S, \mathrm{after}}(T) = 2 
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
  T_\gamma = \left(\frac{11}{4}\right)^{1/3}\ T_\nu
\end{equation}

Nous constatons donc qu'après l'annihilation de $e^\pm$, la température du fond de neutrinos cosmiques est effectivement inférieure à la température du CMB. Aujourd'hui, en utilisant $T_{CMB} = 2,726 K$, nous trouvons :
\begin{equation}
  T_\nu \approx 1.95 K
\end{equation}

Nous pouvons en déduire la densité de neutrinos $n_\nu$ en fonction de $n_\gamma$. Les neutrinos sont des fermions (d'où le facteur 3/4) : 
\begin{equation}
  n_\nu = \frac{3}{4} \times 3 \times \frac{4}{11} n_\gamma
\end{equation}
ce qui donne $\approx 112 \mathrm{cm}^{-3}$ par saveur (336 cm$^{-3}$ au total).

Pour la densité d'énergie du fond de neutrinos, nous trouvons :
\begin{equation}
  \rho_\nu = \frac{7}{8} \times 3 \times \left(\frac{4}{11}\right)^{4/3} \rho_\gamma
\end{equation}
et numériquement, on trouve $\Omega_\nu h^2 \approx 1.7\times 10^{-5}$.

En fait, les neutrinos ont des masses, avec deux conséquences importantes (1) nous ne savons pas s'ils sont encore relativistes aujourd'hui (toutes espèces confondues) (2) $\Omega_\nu h^2$ est plus grand que la valeur citée ci-dessus. La cosmologie avec des neutrinos massifs fera l'objet d'un prochain devoir.  

Une autre remarque est que le découplage des neutrinos s'est légèrement superposé à l'anihilation de $e^\pm$.  Comme les neutrinos interagissaient encore au moment de l'anihilation, le bruit de fond des neutrinos a été légèrement affecté par l'énorme énergie et l'entropie libérées par l'anihilation de $e^\pm$. Dans la littérature, cela est pris en compte en introduisant un "nombre effectif de neutrinos", $N_{\mathrm eff} \approx 3.046$. En tenant compte de cela, le nombre de neutrinos et la densité d'énergie sont :
\begin{equation}
  \begin{split}
    n_\nu & = \frac{3}{4} N_{\mathrm{eff}} \frac{4}{11} n_\gamma \\
    \rho_\nu & = \frac{7}{8} N_{\mathrm{eff}} \frac{4}{11} n_\gamma \\
  \end{split}
\end{equation}

Enfin, les valeurs correctes $g_\star$ et $g_{\star S}$ après l'anihilation $e^\pm$ sont :
\begin{equation}
  \begin{split}
    g_\star & = 2 + \frac{7}{8} 2 N_{\mathrm{eff}} \left(\frac{4}{11}\right)^{4/3} \approx 3.36 \\
    g_{\star S} & = 2 + \frac{7}{8} 2 N_{\mathrm{eff}} \left(\frac{4}{11}\right) \approx 3.94 \\    
  \end{split}
\end{equation}
