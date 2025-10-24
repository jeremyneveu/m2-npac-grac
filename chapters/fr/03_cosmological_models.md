---
short_title: Modèles cosmologiques
authors:
  - jneveu
keywords: cosmological models, EdS model, mechanical analogy
---

Modèles cosmologiques
=======================

Modèles simples
---------------

Maintenant que nous avons un modèle pour décrire la dynamique de l'Univers, calculons son évolution dans quelques cas simples pour s'entraîner.

### Univers plat, matière seule

Commençons par le cas d'un Univers plat, contenant uniquement de la matière non relativiste. C'est le modèle dit _d'Einstein et de Sitter_. C'est le plus simple auquel on puisse penser en 1930. La première équation de Friedmann s'écrit :
\begin{equation*}
& 3 \frac{\dot{a}^2}{a^2} = 8\pi \GN \rho_m = 8 \pi \GN \rho_m^0 \left(\frac{a_0}{a}\right)^{3} 
& \Leftrightarrow (\dot a)^2 = 8 \pi \GN \rho_m^0 a_0^3 / 3 a = H_0^2 \Omega_m^0 \frac{a_0^3}{a}
\end{equation*}
Avant d'intégrer cette équation différentielle, rappelons nous que les paramètres de densité d'énergie sont liés par une relation de fermeture [](#eq:omega_sum). Par conséquent, dans un Univers plat avec seulement de la matière, on a $\Omega_m^0=1$. Intégrons maintenant l'équation différentielle entre $0$ et un facteur d'échelle $a$ quelconque :
\begin{equation*} 
\int_0^{a}\sqrt{\frac{a'}{a_0}} \frac{\dd a'}{a_0} = \int_0^t H_0  \dd t' \Rightarrow \frac{2}{3}\left(\frac{a(t)}{a_0}\right)^{3/2} = H_0  t
\end{equation*}
$$
\label{eq:a_matiere_only}
\Rightarrow \frac{a(t)}{a_0} = \left( \frac{3}{2}H_0  t\right)^{2/3}$$
avec au début de l'Univers $t=0$ lorsque $a=0$. On a obtenu ainsi une relation direct entre le facteur d'échelle et l'âge de l'Univers.

### Univers plat, radiation seule

Par un raisonnement similaire, on montre que pour un Univers plat dominé par le rayonnement on a une évolution différente du facteur d'échelle :
$$
\label{eq:a_rad_only}
\frac{a(t)}{a_0} = \left( 2 H_0  t\right)^{1/2}
$$

### Univers vide (Milne)

Supposons que l'Univers est vide, ou du moins avec une densité d'énergie totale très faible devant la densité critique. Alors l'Univers doit être courbé puisque dans ce cas :
$$\Omega_k^0 = 1 - \Omega_m^0  - \Omega_r^0  - \Omega_\Lambda^0 \approx 1$$
Cet Univers est donc hyperbolique[^ksign]. La première équation de Friedmann s'écrit :
$$
\frac{\dot{a}^2}{a^2}   = H_0^2 \Omega_k^0 \frac{a_0^2}{a^2} = H_0^2 \frac{a_0^2}{a^2}
$$
puis :
$$ 
\dot a = \sqrt{a_0^2 H_0^2} = a_0 H_0
$$
L'intégration donne donc un Univers en expansion à vitesse constante :
$$\label{eq:a_empty}
a(t) = a_0 H_0 t$$

:::{important}

La constante de Hubble $H_0$ apparaît dans les trois modèles d'Univers précédents. Le taux d'expansion de l'Univers aujourd'hui n'est pas une prédiction des modèles mais une donnée externe, lors de l'intégration des équations différentielles de Friedmann.
:::



Modèles à plusieurs compostantes
-------------------

La cosmologie moderne est née avec la Relativité Générale. Depuis l'écriture de ces équations, les scientifiques ont commencé à décrire mathématiquement l'univers comme un système physique. De nombreux modèles ont été proposés pour décrire les différentes histoires de l'univers.




### Modèle de Eddington-Lemaître (1927)


:::{exercise} Modèle de Lemaître
:label: exo:lemaitre

Friedmann et Lemaître ont été les premiers cosmologistes à proposer, indépendamment, des modèles non statiques d'univers avec des courbures arbitraires. Les équations de Friedmann ont été largement étudiées dans ce cours, mais Lemaître a été le premier à proposer l'idée que l'Univers s'est développé à partir d'un atome primitif. Son modèle repose sur un univers composé uniquement de matière froide, avec une constante cosmologique et une courbure spatiale arbitraire (pas de rayonnement). 

1. Dans un tel modèle, montrer que, juste après un big bang à $t=0$, au début de l'univers le facteur d'échelle augmente comme :
\begin{equation}
\frac{a(t)}{a_0} =\left( \frac{3}{2}H_0\sqrt{\Omega_m^0}t\right)^{2/3}
\end{equation}

2. Au fur et à mesure que l'univers s'étend, cependant, la densité d'énergie de la matière diminue et la constante cosmologique finit par dominer. Montrer que, pour les grands $t$, le facteur d'échelle augmente comme :
\begin{equation}
a(t) \propto e^{H_0\sqrt{\Omega_\Lambda^0}t}
\end{equation}

3. Calculez $\ddot{a}$ et montrez que l'expansion de l'univers décélère d'abord, puis s'accélère. Calculer $a_*$ le facteur d'échelle à la transition.

:::

:::{solution} exo:lemaitre
:class: dropdown

1. Dans le modèle de Lemaître à matière seule, la première équation de Friedmann s'écrit :
\begin{equation}\label{eq:lemaitre}
\frac{\dot{a}^2}{a^2} = H_0^2\left[\Omega_m^0 \left(\frac{a_0}{a}\right)^{3} + \Omega_\Lambda^0 + \Omega_k^0 \left(\frac{a_0}{a}\right)^{2}\right] \Leftrightarrow \dot{a}^2 = H_0^2\left[\Omega_m^0 \frac{a_0^3}{a} + \Omega_\Lambda^0 a^2 + \Omega_k^0 a_0^2 \right]
\end{equation}
A $t\approx 0$, l'Univers était extrêmement petit donc le terme de matière domine :
\begin{equation}
\dot a^2 \approx H_0^2\left[\Omega_m^0 \frac{a_0^3}{a}\right] \Leftrightarrow \sqrt{\frac{a}{a_0}}\frac{\dot{a}}{a_0}= H_0 \sqrt{\Omega_m^0} \Leftrightarrow \frac{a(t)}{a_0} = \left(\frac{3}{2}H_0\sqrt{\Omega_m^0}t\right)^{2/3}
\end{equation}

2. Puis, après un certain temps, $a$ devient grand et le terme de constante cosmologique domine :
\begin{equation}
\dot{a}^2 \approx H_0^2\left(\Omega_\Lambda^0 a^2\right) \Leftrightarrow \dot{a}= H_0 \sqrt{\Omega_m^0} a(t) \Rightarrow a(t) \propto e^{H_0\sqrt{\Omega_\Lambda^0}t}
\end{equation}

3. En dérivant l'équation [](#eq:lemaitre), on trouve que :
\begin{equation}
2\dot{a}\ddot{a} = H_0^2\left[ -\dot{a}\Omega_m^0 \frac{a_0^3 }{a^{2}} + 2 \dot{a} a \Omega_\Lambda^0 \right] \Leftrightarrow \frac{\ddot{a}}{a_0} = \frac{H_0^2}{2}\left[2 \Omega_\Lambda^0 \left(\frac{a}{a_0}\right) - \Omega_m^0\left(\frac{a_0}{a}\right)^2\right]
\end{equation}
Lorsque $a$ est petit, nous constatons que $\ddot{a}$ est négatif et que l'expansion décélère. Cependant, lorsque $a$ est grand, $\ddot{a}>0$ et l'expansion de l'univers s'accélère. La transition se produit à :
\begin{equation}
\ddot{a}=0 \Leftrightarrow 0=\frac{H_0^2}{2}\left[2 \Omega_\Lambda^0 \frac{a_*}{a_0} - \frac{\Omega_m^0a_0^2}{a_*^2}\right] \Leftrightarrow \frac{a_*}{a_0} = \left( \frac{\Omega_m^0}{2\Omega_\Lambda^0}\right)^{1/3}
\end{equation}
Pour le modèle $\Lambda$CDM avec $\Omega_m^0\approx 0.3$ et $\Omega_\Lambda^0\approx 0.7$, on a $a_*/a_0 \approx 0.6$ d'où un redshift de transition à $z\approx 0.67$.
:::


### $\Lambda$CDM

L'expansion de l'Univers est aujourd'hui bien décrite par le modèle $\Lambda$CDM plat ($\Omega_k^0=0$). Les proportions de chacune de ces composantes sont aujourd'hui évaluées à {cite}`Planck2018`:
$$\Omega_\Lambda^0 = 0.685,\quad \Omega_m^0=315$$
Concernant la matière froide, celle-ci peut être séparée en deux contributions: la matière sombre $\Omega_{c}^0=0.264$ et la matière baryonique[^baryons] $\Omega_b^0=0.049$.


Analogie mécanique
-------------------

:::{exercise} Analogie mécanique
:label: exo:analogmeca

1. Écrire la première équation de Friedmann comme suit:
\begin{equation}
\frac{1}{2}\Omega_k^0 = f(\Omega_i^0,a)
\end{equation}
Interpréter cette équation par analogie avec l'équation de conservation de l'énergie mécanique d'un corps massif suivant un mouvement unidimensionnel, et décrire le rôle de chaque terme d'"énergie potentielle".

2. Dériver cette équation par rapport au temps et faire l'analogie avec la loi de Newton appliquée à un corps massif en mouvement unidimensionnel. Analyser à nouveau le rôle de chaque terme de "force".

Dans ce qui suit, nous négligeons la composante de rayonnement. Tracez les termes d'énergie potentielle en fonction du facteur d'échelle $a$ et décrivez le destin des univers suivants.

3. Modèle sphérique ($k=+1$) avec $\Lambda=4\pi \GN \rho_m / c^2$ (montrez que le modèle statique d'Einstein est un cas particulier de ce modèle et qu'il est instable).

4. Modèles de matière seule avec différents signes de courbure (le modèle d'Einstein-de Sitter correspond au cas de la courbure plate).

5. $\Lambda$CDM modèles avec différents signes pour la constante cosmologique et des courbures arbitraires (calculer le facteur d'échelle de transition $a_*$ entre la décélération et l'accélération de l'expansion).

:::


:::{solution} exo:analogmeca
:class: dropdown


1. En termes de $\Omega_i^0$, la première équation de Friedmann s'écrit :
\begin{equation}
H^2 = \left(\frac{\dot{a}}{a}\right)^2 = H_0^2 \left( \frac{\Omega_m^0}{a^3} + \frac{\Omega_r^0}{a^4} + \Omega_\Lambda^0 + \frac{\Omega_k^0}{a^2} \right)
\end{equation}
ce qui donne
\begin{equation}
\frac{1}{2}\Omega_k^0 = \frac{1}{2}\frac{\dot{a}^2}{H_0^2} - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{2}\frac{\Omega_r^0}{a^2} - \frac{1}{2}\Omega_\Lambda^0 a^2
\end{equation}

Cette dernière équation ressemble à l'équation de conservation de l'énergie mécanique pour un corps massif suivant un mouvement unidimensionnel. Faisons l'analogie :
- $\frac{1}{2}\Omega_k^0$ est constant avec $a$ peut être identifié comme l'énergie mécanique conservée du corps massif
- $\frac{1}{2}\frac{\dot{a}^2}{H_0^2}$ représente l'énergie cinétique du corps massif.
- $- \frac{1}{2}\frac{\Omega_m^0}{a}$ ressemble à un potentiel gravitationnel centré autour de $a=0$.
- $ -\frac{1}{2}\frac{\Omega_r^0}{a^2}$ est un autre type de potentiel attractif.
- $- \frac{1}{2}\Omega_\Lambda^0 a^2$ est un potentiel harmonique inversé (répulsif) centré autour de $a=0$.

2. \begin{equation}
\frac{\ddot{a}}{H_0^2} = - \frac{1}{2}\frac{\Omega_m^0}{a^2 } -\frac{\Omega_r^0}{a^3 } + \Omega_\Lambda^0 a
\end{equation}
Cette équation ressemble à la loi de Newton appliquée à un corps massif en mouvement unidimensionnel. Faisons l'analogie :
- $\frac{\ddot{a}}{H_0^2}$ accélération du corps massif
- $- \frac{1}{2}\frac{\Omega_m^0}{a^2 }$ force gravitationnelle (attractive)
- $+ \Omega_\Lambda^0 a$ force élastique répulsive

Définissons :
\begin{equation}
V_{\rm eff}(a) = - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{2}\Omega_\Lambda^0 a^2
\end{equation}

3. Dans ce modèle d'univers, nous avons $\Omega_\Lambda^0 = \Omega_m^0 / 2$ et :
\begin{equation}
V_{\rm eff}(a) = - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{4}\Omega_m^0 a^2
\end{equation}
\begin{equation}
\frac{\dd V_{\rm eff} }{\dd a}= 0 \Rightarrow \left(\frac{1}{a^2}-a\right)\Omega_m^0 = 0 \Rightarrow a=1\text{ (aujourd'hui)}
\end{equation}
A $a=1$ ou $t=0$, la première équation de Friedmann donne :
\begin{equation}
1 = \Omega_m^0 + \Omega_\Lambda^0 + \Omega_k^0 \Rightarrow \Omega_k^0 = 1 - \frac{3}{2}\Omega_m^0
\end{equation}
Le modèle est sphérique donc $\Omega_k^0 = -k c^2 / H_0^2 < 0$ avec $k=+1$ ce qui implique que $\Omega_m^0 > 2/3$. Dans l'Univers d'Einstein, $\Omega_m^0=1$.

```{figure} #E-spherical
:width: 60%
:align: center
:label:fig:einstein

Energies potentielles dans le cas d'un univers sphérique avec $\Omega_m^0=1$.
```

D'après la figure [](#fig:einstein), la solution d'Einstein à $a=a_0$ est instable. 

4.  
```{list-table} Energies potentielles dans le cas de modèles à matière seule avec différentes courbures :  (en haut à gauche), $\Omega_m^0=1.5\Rightarrow k=+1$ (en haut à droite), $\Omega_m^0=0.5\Rightarrow k=-1$ (en bas)
:header-rows: 1
:name: fig:analogmeca

* - $\Omega_m^0=1\Rightarrow k=0$
  - $\Omega_m^0=1.5\Rightarrow k=+1$
  - $\Omega_m^0=0.5\Rightarrow k=-1$

* - :::{image} #EdS-Om1
    :alt: galaxies
    :width: 100%
    :align: center
    
    :::
  - :::{image} #EdS-Om15
    :alt: light
    :width: 100%
    :align: center
    
  - :::{image} #EdS-Om05
    :alt: light
    :width: 100%
    :align: center
```

Dans ces modèles, la courbure est à nouveau donnée par :
\begin{equation}
1 = \Omega_m^0 + \Omega_k^0 \Rightarrow \Omega_k^0 = 1 -\Omega_m^0 \Rightarrow 
\left\lbrace\begin{array}{ll}
k=+1 & \text{ if } \Omega_m^0 > 1\\
k=0 & \text{ if } \Omega_m^0 = 1 \\
k=-1 & \text{ if } \Omega_m^0 < 1 
\end{array}\right.
\end{equation}

En analysant les trois tracés de la figure [](#fig:analogmeca), nous pouvons dire qu'un univers sphérique composé uniquement de matière s'effondrera nécessairement à un moment donné, quelles que soient ses conditions initiales (nécessité pour Einstein d'ajouter la constante cosmologique). Un univers plat en expansion s'étend indéfiniment et arrête asymptotiquement son expansion à $t\rightarrow \infty$. Un univers hyperbolique en expansion s'étend également à l'infini.

5. Le facteur d'échelle de transition est donné par : 
\begin{equation}
\frac{d V_{\rm eff} }{da}= 0 \rightarrow a_* = \left(\frac{\Omega_m^0}{2 \Omega_\Lambda^0}\right)^{1/3}
\end{equation}

```{list-table} Energies potentielles dans le cas de modèles à matière seule avec différentes courbures :  (en haut à gauche), $\Omega_m^0=1.5\Rightarrow k=+1$ (en haut à droite), $\Omega_m^0=0.5\Rightarrow k=-1$ (en bas)
:header-rows: 0
:name: fig:analogmeca-LCDM

* - $\Omega_m^0=0.3, \Omega_\Lambda^0=0.7$
  - $\Omega_m^0=0.3, \Omega_\Lambda^0=1.5$

* - :::{image} #LCDM-Om03OL07
    :width: 100%
    :align: center
    
    :::
  - :::{image} #LCDM-Om03OL15
    :width: 100%
    :align: center

* - $\Omega_m^0=0.3, \Omega_\Lambda^0=0.5$
  - $\Omega_m^0=0.3, \Omega_\Lambda^0=-0.7$

* - :::{image} #LCDM-Om03OL05
    :width: 100%
    :align: center
    
    :::
  - :::{image} #LCDM-Om03OL-07
    :width: 100%
    :align: center
    
```

Selon les valeurs des paramètres, l'échelle de transition se produit dans le futur ou dans le passé. Si la constante cosmologique est positive, les univers en expansion ont une expansion décélérée et, après l'échelle de transition, une expansion accélérée.  Si la constante cosmologique est négative, l'univers doit s'effondrer après un certain temps.

Pourquoi l'Univers est-il donc en expansion aujourd'hui? Cela dépend entièrement des conditions initiales, donc en particulier parce que l'univers est né d'un Big Bang. Et pourquoi il y a eu un Big Bang ? On peut laisser libre son imagination: collisions de branes, Dieu, souris pan-dimensionnelles... mais la réponse n'est pas (encore) donnée par les sciences physiques.

:::




Evolution des paramètres cosmologiques
------------------------------------


:::{figure} #omegas
:width: 100%
:align: center
:label: fig:omegas

Evolution des paramètres cosmologiques.
:::




:::{important} A retenir

- L'intégration de la première équation de Friedmann en y injectant les propriétés d'évolution des différents fluides permet d'obtenir l'évolution du facteur d'échelle en fonction du temps.

- Que ce soit avec de la matière relativiste, non-relativiste ou pour un Univers vide, on obtient des fonctions croissantes du temps puisqu'on mesure $H_0>0, donc des scénarios d'univers en expansion. 

- L'écriture de la première équation de Friedmman sous la forme d'une équation analogue à la conservation de l'énergie en mécanique classique permet d'avoir une intuition sur l'évolution d'un Univers en fonction des différentes compostantes présentes. Entre autres, la matière non-relativiste retient l'expansion par son effet gravitationnel attractif, alors qu'une constante cosmologique positive amène à une accélération de l'expansion dans le futur.


::: 


:::{seealso}  Pour approfondir

- Autres modèles cosmologiques historiques : <wiki:Einstein%27s_static_universe>, <wiki:De_Sitter_universe>

- Modèle standard de la cosmologie $\Lambda$CDM : <wiki:Lambda-CDM_model>

:::



[^ksign]: Le signe de $k$ est l'inverse du signe de $\Omega_k^0$.
[^Mach]: En physique théorique, en particulier dans les discussions sur les théories de la gravitation, le principe de Mach 
est le nom donné par Einstein à une hypothèse imprécise souvent attribuée au physicien et philosophe Ernst Mach. 
L'idée est que les cadres inertiels locaux sont déterminés par la distribution de la matière à grande échelle.


