

:::{exercise} Temps conforme
:label: exo:conformal-time

Transformer la partie spatiale de la métrique FLRW dy système de coordonnées comobiles $(\sigma,\theta,\phi)$ [](#eq:FLRW-metric-spherical) au système de coordonnées comobiles équivalent $(\chi,\theta,\phi )$ avec $\chi$ la distance comobile. Étendre cette transformation aux coordonnées temporelles et proposer une définition du temps conforme $\eta$ et l'écrire sous la forme :
\begin{equation}
\dd s^2 = a^2(t) \left[ -c^2 \dd\eta^2 + \dd\chi^2 + f_k^2(\chi)\dd\theta^2 + f_k^2(\chi)\sin^2\theta \dd\phi^2 \right]
\end{equation}
avec $f_k(\chi)$ une fonction de $k$ et $\chi$ à définir. 

:::

:::{solution} exo:conformal-time
:label: exo:conformal-time-sol
:class: dropdown

On commence par la définition de la métrique FLRW :
\begin{align}
\dd s^2 & = -c^2\dd t^2 + a^2(t) \left[ \frac{\dd\sigma^2}{1-k\sigma^2} + \sigma^2\dd\theta^2 + \sigma^2 \sin^2\theta \dd\phi^2 \right]  \\
& = -c^2\dd t^2 + a^2(t) \left[ \dd\chi^2 + \sigma^2\dd\theta^2 + \sigma^2 \sin^2\theta \dd\phi^2 \right] \\
& = -c^2\dd t^2 + a^2(t) \left[ \dd\chi^2 + f_k^2(\chi)\dd\theta^2 +f_k^2(\chi) \sin^2\theta \dd\phi^2 \right]
\end{align}
avec $\dd\chi = \dd\sigma/\sqrt{1-k\sigma^2}$ et :
\begin{equation}
\sigma = f_k(\chi) = \left\lbrace\begin{array}{cl}
    \sin\chi & \text{ si } k=+1  \\
    \chi  & \text{ si } k=0 \\
    \sinh\chi & \text{ si } k=-1 
\end{array}
\right.
\end{equation}
On définit $\dd\eta =  \dd t / a(t)$ le temps conforme, et on aboutit à :
\begin{equation}
\dd s^2 = a^2(t) \left[ -c^2 \dd\eta^2 + \dd\chi^2 + f_k^2(\chi)\dd\theta^2 + f_k^2(\chi)\sin^2\theta \dd\phi^2 \right]
\end{equation}
Le temps conforme $\eta$ possède la dimension d'une durée. 


D'ailleurs, en utilisant le temps conforme $\eta$ défini par $\dd \eta = \dd t / a(t)$, pour un photon on obtient :
$$
\chi = c \int_{\eta_E}^{\eta_0} \dd \eta = c (\eta_0 - \eta_E)$$
donc on reconnait la relation traditionnelle entre distance et temps, mais dans l'espace comobile sans dimension.

:::




:::{exercise} Evolution des densités d'énergie et interprétation
:label: exo:rhos

1. Démontrer la formule [](#eq:conservation_energie).
2. Trouver l'évolution de la densité de matière $\rho_m$ en fonction de $a$. Même question pour la densité de rayonnement $\rho_r$. 
On rappelle que $P_m=0$ pour la matière non relativiste et $P_r=\epsilon_r/3$ pour le rayonnement.
3. A partir d'un raisonnement sur un cube comobile qui se dilate, avec des arguments physiques sur des nombres de galaxies,
retrouvez le même résultat.
4. Pour un fluide parfait dont l'équation d'état $w$ est constante ($P=w\rho c^2$), donner l'évolution de sa densité d'énergie.
5. Identifier le terme $\Lambda g_{\mu\nu}$ avec le tenseur énergie-contrainte d'un fluide parfait. Trouver la densité d'énergie $\rho_\Lambda$ 
et la pression $P_\Lambda$ exercées par la constante cosmologique ainsi que son équation d'état.
6. À partir de ces dernières questions, réfléchissez au comportement de la densité d'énergie liée au vide. Considérons une chambre à piston cylindrique de section $A$ "remplie" d'énergie du vide. Le piston est tiré sur une distance linéaire $\dd x$.  Montrez que l'énergie créée par le retrait du piston est égale au travail effectué par le vide, à condition que :
\begin{equation}
 P_{\rm vac} = - \rho_{\rm vac} c^2 
 \end{equation} % voir Hobson exo piston 15,5 p422
Cette équation d'état du vide peut être établie à l'aide de la théorie quantique des champs. Elle montre donc que, dans ce cas, la densité d'énergie du vide est constante lorsque le piston se retire.

:::

:::{solution} exo:rhos
:class: dropdown

1. Commençons :
\begin{align}
8\pi \GN \dot{\rho} & = 6\dot{H}H - \frac{6c^2 k \dot{a}}{a^3} \\
& = 3H \left[-8\pi \GN P / c^2 + c^2 \Lambda - 3 H^2 - \frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi \GN P / c^2 -8 \pi G \rho + 2\frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi \GN P / c^2 -8 \pi G \rho \right]
\end{align}
et $\dot{\rho} c^2 = -3 H(\rho c^2 + P )$. 


2. En utilisant la définition du paramètre de Hubble $H = (\dd a/\dd t)/a$, nous pouvons transformer les dérivées temporelles en dérivées par rapport au facteur d'échelle $a$ (ou décalage vers le rouge $z$) :
\begin{equation}
\frac{\dd}{\dd t}=Ha\frac{\dd}{\dd a}
\end{equation}
La formule de conservation de l'énergie se transforme en :
\begin{equation}
a\frac{\dd\rho}{da} = -3 (\rho c^2 + P)
\end{equation}
En ce qui concerne la matière non relativiste, $P_m=0$ donc :
\begin{equation}
\frac{\dd\rho_m}{\rho_m} = -3 \frac{\dd a}{a} \Rightarrow \rho_m(a) = \rho_m^0 \left(\frac{a_0}{a}\right)^3
\end{equation}
En ce qui concerne le rayonnement, $P_r=\rho_r c^2 / 3$ donc :
\begin{equation}
\frac{\dd\rho_r}{\rho_r} = -4 \frac{\dd a}{a} \Rightarrow \rho_r(a) = \rho_r^0 \left(\frac{a_0}{a}\right)^4
\end{equation}


3. 
```{list-table} Conservation de l'énergie pour la matière et le rayonnement dans un univers en expansion.
:header-rows: 0
:name: fig:cubes

* - :::{image} ../../images/cube_galaxies.svg
    :alt: galaxies
    :width: 100%
    :align: center
    :::
  - :::{image} ../../images/cube_waves.svg
    :alt: light
    :width: 100%
    :align: center
```

Dans le cube isolé, l'énergie et la matière se conservent. Ainsi, en ce qui concerne les galaxies présentes dans un cube en expansion, nous pouvons écrire que leur nombre est conservé par l'expansion de la manière suivante :
\begin{equation}
N_{\rm gal} = \rho_m^0 a_0^3 = \rho_m(a) a^3 \Rightarrow \rho_m(a) = \rho_m^0 \left(\frac{a_0}{a}\right)^3
\end{equation}
Considérons une onde électromagnétique dans un cube en expansion. La longueur d'onde physique $\lambda$ augmente mais la longueur d'onde en coordonnées $\lambda/a$ est conservée. La conservation de l'énergie de rayonnement dans un cube en mouvement s'écrit :
\begin{equation}
a_0 \frac{h c}{\lambda_0} = a \frac{h c}{\lambda}
\end{equation}
La densité d'énergie est alors
\begin{equation}
\rho_r(a) = \frac{(hc/\lambda)}{a^3} = \frac{a_0(hc/\lambda_0)}{a^4} = \rho_r^0 \left(\frac{a_0}{a}\right)^4
\end{equation}
Le comportement en $a^{-4}$ est donc dû à la dilatation de la longueur d'onde du photon.

4. On montre que
\begin{align}
\dot{\rho}c +3\frac{\dot{a}}{ac}(\rho c^2+P)=0 & \Leftrightarrow \dot{\rho}c =-3\frac{\dot{a}}{ac}(1+w)\rho c^2=0 \\
& \Leftrightarrow \frac{d\rho}{\rho} = -3(1+w) \frac{da}{a} \\
& \Rightarrow \rho = \rho_0 \left( \frac{a}{a_0}\right)^{-3(1+w)}
\end{align}

5. En utilisant l'équation d'Einstein, en passant le terme $\Lambda$ du côté du tenseur énergie-contrainte de l'équation, nous identifions cette contribution comme un fluide parfait :
\begin{equation}
\Lambda g_{\mu\nu} = \frac{8\pi \GN}{c^4} \begin{pmatrix} \rho_\Lambda c^2 & 0 & 0 & 0 \\ 0 &a^2 p_\Lambda & 0 & 0 \\ 0&0&a^2 p_\Lambda &0 \\ 0&0&0&a^2 p_\Lambda \end{pmatrix}
\end{equation}
Nous obtenons :
\begin{align}
\Lambda & = \frac{8\pi \GN}{c^4} \rho_\Lambda c^2 \Leftrightarrow \rho_\Lambda c^2 = c^4 \Lambda / 8\pi \GN \\
-a^2 \Lambda & = \frac{8\pi \GN}{c^4} a^2 P_\Lambda \Leftrightarrow p_\Lambda = - c^4 \Lambda / 8 \pi \GN = - \rho_\Lambda c^2
\end{align}
Pour la constante cosmologique, l'équation d'état est constante et sa valeur est $w=-1$. En utilisant la question précédente, nous avons :
\begin{equation}
\rho = \rho_0 \left( \frac{a}{a_0}\right)^{-3(1+w)} = \rho_0
\end{equation}
La densité d'énergie associée à la constante cosmologique est constante tout au long de l'expansion de l'univers.

6. L'énergie créée par le retrait du piston est :
\begin{equation}
\dd U = \dd\left(\rho_{\rm vac} c^2 V\right) = c^2 V \dd\rho_{\rm vac} + \rho_{\rm vac} c^2 \dd V
\end{equation}
Pour une transformation adiabatique, le premier principe de la thermodynamique donne :
\begin{equation}
\dd U = \delta W = -P_{\rm vac} \dd V
\end{equation}
En supposant que $P_{\rm vac}= - \rho_{\rm vac} c^2$, pour la densité d'énergie du vide nous avons $d\rho_{\rm vac} = 0$ et le premier principe $ dU = \delta W$ est vérifié.

:::
