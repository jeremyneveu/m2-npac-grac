---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---

Modèles cosmologiques
=======================



Modèles simples
---------------


Maintenant que nous avons un modèle pour décrire la dynamique de l'Univers, calculons son évolution dans quelques cas simples
pour s'entraîner.

### Univers plat, matière seule

Commençons par le cas d'un Univers plat, contenant uniquement de la matière non relativiste. C'est le modèle dit _d'Einstein et de Sitter_.
C'est le plus naïf auquel on puisse penser à partir de l'observation. La première équation de Friedmann s'écrit :
$$ \begin{align*}
& 3 \frac{\dot{a}^2}{a^2} = 8\pi G_N \rho_m = 8 \pi G_N \rho_m^0 \left(\frac{a_0}{a}\right)^{3} 
& \Leftrightarrow (\dot a)^2 = 8 \pi G_N \rho_m^0 a_0^3 / 3 a = H_0^2 \Omega_m^0 \frac{a_0^3}{a}
\end{align*}
$$
Avant d'intégrer cette équation différentielle, rappelons nous que les paramètres de densité d'énergie sont liés par une relation
de fermeture [](#eq:omega_sum). Par conséquent, dans un Univers plat avec seulement de la matière, on a $\Omega_m^0=1$. Intégrons maintenant
l'équation différentielle :
$$  \sqrt{\frac{a}{a_0}} \frac{\dd a}{a_0} = H_0  \dd t \Rightarrow \left(\frac{a}{a_0}\right)^{3/2} = \frac{3}{2}H_0  t $$
$$\label{eq:a_matiere_only}
\Rightarrow \frac{a(t)}{a_0} = \left( \frac{3}{2}H_0  t\right)^{2/3}$$
avec au début de l'Univers $t=0$ et $a=0$. On a obtenu ainsi une relation direct entre le facteur d'échelle et l'âge de l'Univers.

### Univers plat, radiation seule

Par un raisonnement similaire, on montre que pour un Univers plat dominé par le rayonnement on a une évolution différente du facteur d'échelle :
$$\label{eq:a_rad_only}
\frac{a(t)}{a_0} = \left( 2 H_0  t\right)^{1/2}$$

### Univers vide (Milne)

Supposons que l'Univers est vide, ou du moins avec une densité d'énergie totale très faible devant la densité critique. 
Alors l'Univers doit être courbé puisque dans ce cas :
$$\Omega_k^0 = 1 - \Omega_m^0  - \Omega_r^0  - \Omega_\Lambda^0 \approx 1$$
Cet Univers est donc hyperbolique[^ksign]. La première équation de Friedmann s'écrit :
$$
\frac{\dot{a}^2}{a^2} + \frac{c^2 k}{a^2}  = 0 
$$
puis :
$$ 
\dot a = \sqrt{-c^2 k} = \sqrt{c^2 H_0^2 \Omega_k^0} = c H_0
$$
L'intégration donne donc un Univers en expansion à vitesse constante :
$$\label{eq:a_empty}
a(t) = c H_0 t$$
où l'échelle aujourd'hui $a_0$ n'apparaît pas. 

:::{important}

La constante de Hubble $H_0$ apparaît dans les trois modèles d'Univers précédents. Or $H_0$ n'est pas une prédiction des modèles cosmologiques
mais bien une mesure externe qui permet de calculer l'histoire de l'Univers en fonction de son taux d'expansion aujourd'hui. C'est en 
quelque sorte les conditions initiales du modèle, où aujourd'hui est l'instant initial.
:::


### Univers avec une constante cosmologique seulement (de Sitter)

:::{exercise} Modèle de Sitter
:label: exo:desitter

Peu après Einstein, de Sitter a publié un autre type de modèle cosmologique. Il a proposé un univers plat avec seulement 
une constante cosmologique non nulle et aucune matière à l'intérieur (ou une quantité négligeable de matière). 
Montrer qu'un tel univers croît de manière exponentielle avec le temps. 
C'est l'univers de de Sitter. Trouvez également un système de coordonnées dans lequel il est statique. 


:::

:::{solution} exo:desitter


Dans un univers plat $k=0$ et la première équation de Friedmann donne dans le modèle de Sitter :
\begin{equation}
\frac{\dot{a}^2}{a^2} = \frac{c^2 \Lambda}{3} \Leftrightarrow -\sqrt{\frac{3}{c^2 \Lambda}}\frac{\dd a }{\dd t}+a=0
\end{equation}
La solution de cette équation différentielle est
\begin{equation}
a(t) = a_0 e^{\sqrt{c^2 \Lambda/3}t}
\end{equation}
L'univers de de Sitter croît exponentiellement avec le temps. 

Pour montrer qu'un univers de de Sitter peut être considéré comme un univers statique, écrivons $T_0 = \sqrt{c^2 \Lambda / 3}$ et changeons les coordonnées $r'(t) = a_0 e^{t/T_0}\sigma$. La métrique FLRW devient alors
\begin{equation}
\dd s^2 =- \dd t^2 + a^2 (\dd \sigma^2 + \sigma^2 \dd \theta^2 + \sigma^2 \sin\theta \dd  \phi^2) =- \dd t^2 + \left[\left(\dd r' - r' \dd t / T_0\right)^2 + r'^2 \dd \theta^2 + r'^2 \sin\theta \dd \phi^2\right]
\end{equation}
En utilisant la transformation :
\begin{equation}
t = t' + \frac{T_0}{2}\log \left( \frac{r'^2}{T_0^2} - 1 \right) 
\end{equation}
nous trouvons :
\begin{equation}
\dd s^2 = \left(1-\frac{r'^2}{T_0^2}\right) \dd t'^2 - \left(1-\frac{r'^2}{T_0^2}\right)^{-1} \dd r'^2 - r'^2 \dd \theta^2 -r'^2 \sin\theta \dd \phi^2 
\end{equation}
Historiquement, le modèle de Sitter a été découvert comme un univers statique avec ce système de coordonnées. Dès que l'idée d'un univers en expansion a été admise par la communauté scientifique, l'univers de Sitter a été considéré comme un univers en expansion exponentielle, dominé par l'énergie noire.

:::


Modèles historiques
-------------------

### Premier modèle d'Einstein

:::{exercise} Premiers modèles cosmologiques
:label: exo:einstein_first

La cosmologie moderne est née avec la relativité générale. Depuis l'écriture de ces équations, les scientifiques 
ont commencé à décrire mathématiquement l'univers comme un système physique. De nombreux modèles ont été proposés pour 
décrire les différentes histoires de l'univers. Dans cet exercice, nous allons passer en revue certains d'entre eux.

Einstein a été le premier à construire un modèle pour l'ensemble de l'univers, en 1917. Il croyait en un univers 
statique et éternel qui ne contenait que de la matière.

1. Dans une perspective moderne, avec les équations de Friedmann (ci-dessous), montrez qu'un univers statique ne 
contenant que de la matière doit avoir une constante cosmologique non nulle $\Lambda=4\pi G \rho_m / c^2$ et doit être 
sphérique. Calculer le rayon de l'univers sphérique d'Einstein $R\equiv a_{\rm Einstein}$.

\begin{equation} \left\lbrace
\begin{array}{l}
   \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{c^2k}{a^2} \right) = 8\pi G_N \rho_m + c^2 \Lambda}  \\ 
    \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{a^2} = - 8\pi G_N P/c^2 + c^2 \Lambda }
\end{array}
\right.
\end{equation}

2. À l'aide des équations de Friedmann, montrez que cet univers sphérique est instable. Considérer une perturbation 
$\delta R$ du rayon de l'univers et $\delta \rho$ de la densité de matière pour calculer l'évolution du rayon.

:::


:::{solution} exo:einstein_first
1. Pour un univers avec seulement de la matière non relativiste, $P_m=0$. S'il est statique, alors $\ddot{a}=\dot{a}=0$ et la seconde équation de Friedmann s'écrit donc :
\begin{equation}
\frac{c^2 k}{a^2}=c^2 \Lambda
\end{equation}
L'injection de cette équation dans la première équation de Friedmann donne :
\begin{align}
3\frac{c^2 k}{a^2} = 8\pi G \rho_m + c^2 \Lambda & \Leftrightarrow 2 c^2 \Lambda = 8 \pi G \rho_m \\
& \Leftrightarrow \Lambda = 4 \pi G \rho_m / c^2 > 0 
\end{align}
Ainsi, pour obtenir un univers statique, Einstein a dû introduire une constante cosmologique non nulle. 
De plus, nous déduisons que $c^2 k / a^2 > 0$ donc $k=+1$ : l'univers statique doit être sphérique. 
À l'origine, Einstein soutenait que l'univers devait être sphérique en utilisant le principe de Mach[^Mach],
mais les équations de Friedmann constituent un point de départ plus facile pour retrouver le modèle d'univers d'Einstein. 

Le facteur d'échelle qui paramètre la croissance de l'univers peut être associé au rayon de l'univers sphérique. 
Nous trouvons que la valeur du rayon est :
\begin{equation}
R\equiv a_E = \Lambda^{-1/2}
\end{equation}

2. En combinant les deux équations de Friedmann pour un univers avec de la matière froide seulement, nous trouvons :
\begin{equation}
\frac{2 \ddot{a}}{a} = - \frac{8\pi G \rho}{3} + \frac{2 c^2 \Lambda}{3}
\end{equation}
Considérons une perturbation du rayon, $a=\Lambda^{-1/2} + \delta a$, qui induit une perturbation de la densité de matière sur la sphère $\rho_m = \rho_0 + \delta \rho = c^2 \Lambda/4 \pi G + \delta \rho$. Cette dernière équation devient
\begin{align}
2 \frac{\delta \ddot{a}}{a} = - \frac{2 c^2 \Lambda}{3} - \frac{8 \pi G \delta \rho}{3 c^2}+ \frac{2 c^2 \Lambda}{3} 
 = - \frac{8 \pi G \delta \rho}{3 c^2}
\end{align}
La quantité de matière se conserve ainsi :
$$\rho a^3 = cste \Rightarrow \frac{\delta \rho}{\rho} = -3 \frac{\delta a}{a}$$
et :
\begin{equation}
\delta \ddot{a} = 4 \pi G \rho_0 \delta a \Leftrightarrow \delta \ddot{a} - c^2 \Lambda \delta a = 0
\end{equation}
c'est-à-dire que la perturbation $\delta a$ croît exponentiellement avec le temps ($\Lambda>0$). L'univers est instable.


:::

### Modèle de Lemaître


:::{exercise} Modèle de Lemaître
:label: exo:lemaitre

Friedmann et Lemaître ont été les premiers cosmologistes à proposer, indépendamment, des modèles non statiques d'univers 
avec des courbures arbitraires. Les équations de Friedmann ont été largement étudiées dans ce cours, mais Lemaître a été le premier à proposer l'idée que l'Univers s'est développé à partir d'un atome primitif. 
Son modèle repose sur un univers composé uniquement de matière, avec une constante cosmologique et une courbure spatiale 
arbitraire (mais pas de rayonnement). 

1. Dans un tel modèle, montrer que, juste après un big bang à $t=0$, au début de l'univers le facteur d'échelle augmente comme :
\begin{equation}
\frac{a(t)}{a_0} =\left( \frac{3}{2}H_0\sqrt{\Omega_m^0}t\right)^{2/3}
\end{equation}

2. Au fur et à mesure que l'univers s'étend, cependant, la densité d'énergie de la matière diminue et la constante 
cosmologique finit par dominer. Montrer que, pour les grands $t$, le facteur d'échelle augmente comme :
\begin{equation}
a(t) \propto e^{H_0\sqrt{\Omega_\Lambda^0}t}
\end{equation}

3. Calculez $\ddot{a}$ et montrez que l'expansion de l'univers décélère d'abord, puis s'accélère. 
Calculer $a_*$ le facteur d'échelle à la transition.

:::

:::{solution} exo:lemaitre
1. Dans le modèle de Lemaître à matière seule, la première équation de Friedmann s'écrit :
\begin{equation}\label{eq:lemaitre}
\frac{\dot{a}^2}{a^2} = H_0^2\left(\Omega_m^0 a^{-3} + \Omega_\Lambda^0 + \Omega_k^0 a^{-2}\right) \Leftrightarrow \dot{a}^2 = H_0^2\left(\Omega_m^0 a^{-1} + \Omega_\Lambda^0 a^2 + \Omega_k^0 \right) 
\end{equation}
A $t=0$, l'Univers était extrêmement petit et le terme de matière domine :
\begin{equation}
\dot{a}^2 \approx H_0^2\left(\Omega_m^0 a^{-1}\right) \Leftrightarrow \sqrt{a}\dot{a}= H_0 \sqrt{\Omega_m^0} \Leftrightarrow a(t) = \left(\frac{3}{2}H_0\sqrt{\Omega_m^0}t\right)^{2/3}
\end{equation}

2. Puis, après un certain temps, $a$ devient grand et le terme de constante cosmologique domine :
\begin{equation}
\dot{a}^2 \approx H_0^2\left(\Omega_\Lambda^0 a^2\right) \Leftrightarrow \dot{a}= H_0 \sqrt{\Omega_m^0} a(t) \Rightarrow a(t) \propto e^{H_0\sqrt{\Omega_\Lambda^0}t}
\end{equation}

3. En dérivant l'équation [](#eq:lemaitre), on trouve que :
\begin{equation}
2\dot{a}\ddot{a} = H_0^2\left(-\dot{a}\Omega_m^0 a^{-2} + 2 \dot{a} a \Omega_\Lambda^0 \right) \Leftrightarrow \ddot{a} = \frac{H_0^2}{2}\left(2 \Omega_\Lambda^0 a - \frac{\Omega_m^0}{a^2}\right)
\end{equation}
Lorsque $a$ est petit, nous constatons que $\ddot{a}$ est négatif et que l'expansion décélère. Cependant, lorsque $a$ est grand, $\ddot{a}>0$ et l'expansion de l'univers s'accélère. La transition se produit à :
\begin{equation}
\ddot{a}=0 \Leftrightarrow 0=\frac{H_0^2}{2}\left(2 \Omega_\Lambda^0 a_* - \frac{\Omega_m^0}{a_*^2}\right) \Leftrightarrow a_* = \left( \frac{\Omega_m^0}{2\Omega_\Lambda^0}\right)^{1/3}
\end{equation}

:::


Analogie mécanique
-------------------

:::{exercise} Analogie mécanique
:label: exo:analogmeca

1. Écrire la première équation de Friedmann comme suit:
\begin{equation}
\frac{1}{2}\Omega_k^0 = f(\Omega_i^0,a)
\end{equation}
Interpréter cette équation par analogie avec l'équation de conservation de l'énergie mécanique d'un corps massif suivant un 
mouvement unidimensionnel, et décrire le rôle de chaque terme d'"énergie potentielle".

2. Dériver cette équation par rapport au temps et faire l'analogie avec la loi de Newton appliquée à un corps massif en 
mouvement unidimensionnel. Analyser à nouveau le rôle de chaque terme de "force".

Dans ce qui suit, nous négligeons la composante de rayonnement. Tracez les termes d'énergie potentielle en fonction 
du facteur d'échelle $a$ et décrivez le destin des univers suivants.

3. Modèle sphérique ($k=+1$) avec $\Lambda=4\pi G_N \rho_m / c^2$ (montrez que le modèle statique d'Einstein est un 
cas particulier de ce modèle et qu'il est instable).

4. Modèles de matière seule avec différents signes de courbure (le modèle d'Einstein-de Sitter correspond au cas de la courbure plate).

5. $\Lambda$CDM modèles avec différents signes pour la constante cosmologique et des courbures arbitraires (calculer le facteur d'échelle de transition $a_*$ entre la décélération et l'accélération de l'expansion).

:::


:::{solution} exo:analogmeca


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
\frac{d V_{\rm eff} }{da}= 0 \Rightarrow \left(\frac{1}{a^2}-a\right)\Omega_m^0 = 0 \Rightarrow a=1\text{ (aujourd'hui)}
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

D'après la figure [](#fig:einstein), la solution d'Einstein à $a=1$ est instable. 

4.  
```{list-table} Energies potentielles dans le cas de modèles à matière seule avec différentes courbures :  (en haut à gauche), $\Omega_m^0=1.5\Rightarrow k=+1$ (en haut à droite), $\Omega_m^0=0.5\Rightarrow k=-1$ (en bas)
:header-rows: 1
:name: fig:analogmeca

* - $\Omega_m^0=1\Rightarrow k=0$
  - $\Omega_m^0=1.5\Rightarrow k=+1$
  - $\Omega_m^0=0.5\Rightarrow k=-1$

* - ```{image} #EdS-Om1
    :alt: galaxies
    :width: 100%
    :align: center
    
    ```
  - ```{image} #EdS-Om15
    :alt: light
    :width: 100%
    :align: center
    
  - ```{image} #EdS-Om05
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

* - ```{image} #LCDM-Om03OL07
    :width: 100%
    :align: center
    
    ```
  - ```{image} #LCDM-Om03OL15
    :width: 100%
    :align: center

* - $\Omega_m^0=0.3, \Omega_\Lambda^0=0.5$
  - $\Omega_m^0=0.3, \Omega_\Lambda^0=-0.7$

* - ```{image} #LCDM-Om03OL05
    :width: 100%
    :align: center
    
    ```
  - ```{image} #LCDM-Om03OL-07
    :width: 100%
    :align: center
    
```

Selon les valeurs des paramètres, l'échelle de transition se produit dans le futur ou dans le passé. 
Si la constante cosmologique est positive, les univers en expansion ont une expansion décélérée et, 
après l'échelle de transition, une expansion accélérée.  Si la constante cosmologique est négative, 
l'univers doit s'effondrer après un certain temps.

Pourquoi l'Univers est-il donc en expansion aujourd'hui? Cela dépend entièrement des conditions initiales, 
donc en particulier parce que l'univers est né d'un Big Bang. 
Et pourquoi il y a eu un Big Bang ? On peut laisser libre son imagination: collisions de branes, Dieu, 
souris pan-dimensionnelles... mais la réponse n'est pas (encore) donnée par les sciences physiques.

:::




Âge de l'Univers
------------------

:::{exercise} Age de l'Univers
:label: exo:Uage

1. Calculer $a(t)$ et l'âge de l'univers pour trois modèles différents en supposant que $H_0\approx 70\,\text{km/s/Mpc}$ :
- $\Omega_m^0=1, \Omega_\Lambda^0=0, \Omega_r^0 \approx 0$ (modèle plat d'Einstein-de Sitter)
- $\Omega_m^0=\Omega_\Lambda^0\approx 0, \Omega_r^0 \approx 0$ (univers vide)
- $\Omega_m^0=\Omega_r^0\approx 0, \Omega_\Lambda^0 = 1$ (modèle plat dominé par le vide)
Nous avons besoin de $1\,$Mpc$=3\times 10^{19}\,$km.

2. Quel univers est le plus ancien ? Pour un modèle $\Lambda$CDM avec $32\%$ de matière et $68\%$ d'énergie noire, 
les cosmologistes estiment l'âge de l'univers à $13.8\,\text{Gyr}$. Ce chiffre peut être comparé à l'âge des étoiles les plus anciennes, 
qui est mesuré à {cite:p}`hobson2006general`[p. 410] :
\begin{equation}
t_{\text{premières étoiles}} = 11.5\pm 1.3\,\text{Gyr}
\end{equation}
 
3. Supposons maintenant que $H_0\approx 500\,$km/s/Mpc comme cela a été estimé au début par Edwin Hubble. 
Calculer à nouveau l'âge de l'univers pour le premier cas, qui était le modèle le plus raisonnable à l'époque (plat, plein de matière...). Concluez.


:::


:::{solution} exo:Uage
:class: dropdown


1. Nous utilisons la première équation de Friedmann :
\begin{equation}
H^2 = \left(\frac{1}{a}\frac{da}{dt}\right)^2 = H_0^2 \left[ \frac{\Omega_m^0}{a^3}+\Omega_\Lambda^0+ \frac{\left(1-\Omega_m^0-\Omega_\Lambda^0)\right)}{a^2}\right].
\end{equation}
car à $a(t_0)=1$ nous avons toujours $1=\Omega_k^0 + \Omega_m^0 + \Omega_\Lambda^0$.

- On a $\Omega_m^0=1, \Omega_\Lambda^0=0, \Omega_r^0 \approx 0$ alors :
\begin{equation}
\frac{\dd a}{\dd t} = a H_0 \sqrt{\frac{\Omega_m^0}{a^3}+\Omega_\Lambda^0+ \frac{\left(1-\Omega_m^0-\Omega_\Lambda^0\right)}{a^2}} = a H_0 \sqrt{\frac{\Omega_m^0}{a^3}} = H_0 a^{-1/2} 
\end{equation}
Avec $t=0$ au Big Bang, 
\begin{equation}
\sqrt{a}\dd a = H_0 \dd t \Rightarrow \int_0^a \sqrt{a'}\dd a' = H_0 \int_0^t \dd t' \Rightarrow \frac{2}{3}a^{3/2} = H_0 t
\end{equation}
Nous obtenons donc :
\begin{equation}
a(t) = \left( \frac{3}{2}H_0 t\right)^{2/3}\quad\text{et}\quad t_U = \frac{2}{3}\frac{1}{H_0} = 9.1\,\text{Gyr} 
\end{equation}
avec :
\begin{equation}
\frac{1}{H_0} = \frac{1}{70\,\text{km/s/Mpc}}= 4.3\times 10^{17}\,\text{s} = 13.6\,\text{Gyr} 
\end{equation}

- $\Omega_m^0=\Omega_\Lambda^0\approx 0,\Omega_r^0 \approx 0$ alors :
\begin{equation}
\frac{\dd a}{\dd t} = a H_0 \sqrt{\frac{\left(1-\Omega_m^0-\Omega_\Lambda^0\right)}{a^2}} = a H_0 \frac{\sqrt{1}}{a} = H_0 
\end{equation}
Avec $t=0$ au Big Bang, 
\begin{equation}
a(t) = H_0 t \Rightarrow t_U = \frac{1}{H_0} = 13.6\,\text{Gyr} 
\end{equation}

- $\Omega_m^0=\Omega_r^0\approx 0, \Omega_\Lambda^0 = 1$ alors :
\begin{enumerate}
\frac{da}{dt} = a H_0 \sqrt{\Omega_\Lambda^0} 
\end{equation}
Avec $t=t_0$ maintenant, 
\begin{equation}
\frac{\dd a}{a} = H_0 \sqrt{\Omega_\Lambda^0} \dd t \Rightarrow \int_a^{a_0} \frac{\dd a'}{a'} = H_0 \sqrt{\Omega_\Lambda^0} \int_t^{t_0} \dd t' \Rightarrow a(t) = a_0 e^{H_0 \sqrt{\Omega_\Lambda^0} (t-t_0)}
\end{equation}
On a $a(t)\Rightarrow 0$ quand $t\rightarrow -\infty$ donc l'âge de l'univers est infini dans le modèle de Sitter.

2. La valeur d'Einstein de-Sitter est incompatible avec la mesure de l'âge des premières étoiles avec une telle valeur de $H_0$. 
Cependant, le modèle $\Lambda$CDM est en accord avec le modèle de "l'univers vide". Cependant, dans l'"univers vide", l'hypothèse que la 
matière ne joue aucun rôle est très forte.

3. 
\begin{equation}
\frac{1}{H_0} = \frac{1}{500\,\text{km/s/Mpc}}= 4.3\times 10^{17}\,\text{s} = 1.9\,\text{Gyr} 
\end{equation}

La première mesure de la constante de Hubble était incompatible avec les mesures de l'âge de la Terre. Les premiers modèles cosmologiques ont donc été affectés par ce fait tant que la mesure de la constante $H_0$ n'était pas corrigée.

:::


Evolution des paramètres cosmologiques
------------------------------------


```{figure} #omegas
:width: 100%
:align: center
:label: fig:omegas

Evolution des paramètres cosmologiques.
```


This will embed the output of a notebook cell

:::{note} Test
![](#om-slider)

:::


[^ksign]: Le signe de $k$ est l'inverse du signe de $\Omega_k^0$.
[^Mach]: En physique théorique, en particulier dans les discussions sur les théories de la gravitation, le principe de Mach 
est le nom donné par Einstein à une hypothèse imprécise souvent attribuée au physicien et philosophe Ernst Mach. 
L'idée est que les cadres inertiels locaux sont déterminés par la distribution de la matière à grande échelle.


