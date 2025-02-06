---
short_title: Grandes structures de l'Univers
authors:
  - jneveu
keywords: fonds diffus cosmologique, CMB, neutrinos, nucléosynthèse
---


Formation des grandes structures de l'Univers
===============================

Jusqu'à présent, nous avons étudié l'évolution d'un Univers homogène, au moins aux très grandes échelles au-delà d'environ $100\,\Mpc$. Or, aujourd'hui on observe que la matière est agglomérée sous forme de planètes, étoiles, galaxies, amas de galaxies et super-amas de galaxies. La question qui se pose alors dans ce chapitre est : comment se forment ces structures dans un Univers en expansion ? Si la formation des astres les plus petits impliquent beaucoup de processus physiques et sont très dépendants des conditions initiales locales, il est possible d'élaborer un modèle linéaire simple de l'évolution des structures de taille les plus grandes $\sim 50\,\Mpc$, comme les amas ou super-amas de galaxies. Pour ce faire, on va simplement utiliser une théorie newtonienne des perturbations linéaires, et calculer l'évolution de ces perturbations dans un Univers en expansion.


:::{figure} ../../images/universe_scales.svg
:width: 100%
:align: center
:label: fig:universe_scales

Échelles de taille et de masse dans l'Univers.
:::


(sec-validity)=
Régime de validité
-----------------------------

Toutefois, énonçons les conditions nécessaires à la validité de la théorie newtonienne des perturbations. Une première condition évidente est que la  perturbation de la métrique $g_{\mu\nu}$ et du tenseur énergie-impulsion $T^{\mu\nu}$ doit être faible. Dans le cas de la matière non relativiste, cela signifie que les perturbations de la densité $\delta \rho$ doivent rester faibles devant la densité moyenne $\rho_0$ i.e. $\delta \rho/\rho_0 \ll 1$. Les perturbations du champ de gravité $\delta \phi$ sont également faibles devant le champ gravitationnel moyen $\phi_0$ i.e. $\delta \phi / \phi_0 \ll 1$.

Mais pour pouvoir revenir à la gravité newtonienne dans un espace-temps homogène en expansion et n'étudier que les perturbations de la densité, il y a une autre condition. La taille des régions montrant un écart par rapport aux propriétés moyennes de l'univers (ou la longueur d'onde des modes considérés) doit être beaucoup plus petite que le rayon de Hubble $R_H={c / H}$, car en gravitation newtonienne l'interaction se propage instantanément. Si ce n'est pas le cas, le temps que l'information d'une région en effondrement ait voyagé jusqu'à l'autre côté de la région, le facteur d'expansion a changé de manière significative : une situation qui ne peut évidemment pas être traitée en utilisant la gravité newtonienne dans un espace-temps en expansion homogène. 



Préambule d'acoustique classique
----------

Le champ de matière non-relativiste est décrit par un modèle de fluide parfait. Regarder l'évolution de perturbations dans un fluide parfait, c'est s'intéresser au domaine de l'acoustique. Rappelons-en ici quelques notions utiles.

Dans une description eulérienne des fluides, pour un fluide au repos et parfait, on définit son champ de vitesse $\vec v(t, \vec r)$, son champ de pression $P(t, \vec r)$ et son champ de densité massique $\rho(t, \vec r)$ comme constants :
$$\vec v(t, \vec r)=\vec 0, P(t, \vec r) = p_0, \rho(t, \vec r) = \rho_0$$
Par dessus, on superposent des perturbations de faible amplitude :
\begin{align*}
\vec v(t, \vec r) & = \vec v_0 + \delta \vec v(t, \vec r)   \\
P(t, \vec r) & = P_0 + \delta P(t, \vec r)  \\
\rho(t, \vec r) & = \rho_0 + \delta \rho(t, \vec r)  \\
\end{align*}
En acoustique, on fait l'hypothèse que les compressions sont adiabatiques et réversibles, c'est-à-dire que si la taille des perturbations est supérieure au libre parcours moyen des particules du fluide alors on peut négliger la conduction de chaleur. Par contre, les surpressions engendrent un travail des force de pression qui change l'énergie interne d'une perturbation et donc sa température, et ce travail permet la propagation de l'énergie acoustique. On utilise donc la compressibilité isentropique $\chi_S$ au lieu de la compressibilité isotherme $\chi_T$ :
$$\chi_S = -\frac{1}{V} \left.\frac{\partial V}{\partial P}\right\vert_S \approx \frac{1}{\rho_0} \frac{\delta \rho}{\delta P}$$
On en déduit le lien entre perturbations de pression et de densité via la compressibilité isentropique :
$$\delta \rho = \rho_0 \chi_S \delta P$$

On a également conservation locale de la masse :
$$ \frac{\partial \rho}{\partial t} + \diverg \left(\rho \vec v\right) = 0 \Rightarrow  \frac{\partial \delta \rho}{\partial t} + \rho_0 \diverg \delta \vec v = 0$$
Comme le fluide est parfait, sa dynamique est régi par l'équation d'Euler (Navier-Stokes sans viscosité) :
$$ \frac{\partial \vec v}{\partial t} + \left(\vec v \cdot \grad\right)\vec v = - \frac{1}{\rho} \grad P + \cancel{\vec g} \Rightarrow \frac{\partial \delta \vec v}{\partial t} = - \frac{1}{\rho_0} \grad \delta P $$
où usuellement on néglige la gravitation. En combinant ces trois équations, on obtient une équation de d'Alembert :
$$ \boxed{ \frac{\partial^2 \delta \vec \rho}{\partial t^2}  - \frac{1}{\rho_0 \chi_S} \triangle \delta \rho = 0, \quad c_s = \frac{1}{\sqrt{\rho_0\chi_S}} }$$
avec $c_s$ la célérité du son. 

Pour un gaz parfait et des transformations isentropiques, on a la Loi de Laplace $PV^\gamma = \cst$ avec $\gamma=C_P / C_V$ le rapport des capacités calorifiques à pression $C_P$ et volume $C_V$ constants, aussi appelé l'indice adiabatique. Si les particules du fluide possèdent $N_{dof}$ degrés de liberté (translations, rotations, vibrations) pour stocker de l'énergie sous forme cinétique (thermique), alors l'indice adiabatique vaut $\gamma = 1+2/N_{dof}$. Pour un gaz diatomique comme l'air à température usuelle, il y a $N_{dof}=5$ degrés de liberté (3 translations et 2 rotations) donc $\gamma = 7/5$. On en déduit une formule pour la célérité du son fonction de la température et de la masse des particules[^cisotherme] :
$$PV^\gamma = \cst \Rightarrow \chi_S \approx \frac{1}{\gamma P_0}$$
$$\boxed{ c_s = \sqrt{\frac{\gamma P_0}{\rho_0}} = \sqrt{\frac{\gamma RT}{M}} = \sqrt{\frac{\gamma k_B T}{m_{\text{air}}}} }$$
avec $M$ la masse molaire du fluide et $m_{\text{air}}$ la masse effective d'une particle d'air si c'est le milieu considéré, calculée par :
$$\label{eq:mair}
m_{\text{air}} = 78\%\,m_{N_2} + 22\%\,m_{O_2}
$$

Acoustique dans un espace en expansion
------------------------------------------

A l'émission du CMB, on constate que l'Univers est légèrement inhomogène, avec des surdensités de taille réduite et de l'ordre de $\delta \rho / \rho_0 \sim 10^{-5}$. Ces fluctuations vont a priori s'accentuer au cours du temps pour aboutir à un Univers où le contraste de densité est de l'ordre de $\delta \rho / \rho_0 \sim 1$[^deltas] ( [](#fig:universe_scales),[](#fig:desiCMBBAO)). Quelles sont les mécanismes permettant cette croissance? 

La formation des grandes structures de l'Univers peut être appréhendée par une théorie linéaire des perturbations dans le fluide parfait constitué par la matière non-relativiste après la recombinaison. Pour étudier l'évolution de ces perturbations de densité dans le champ de matière, il s'agit donc de réécrire les équations de l'acoustique précédentes, dans le contexte particulier d'un milieu en expansion et soumis au loi de la gravité.

:::{figure} ../../images/noirlab2408a-2.jpg
:label: fig:desiCMBBAO

An artistic celebration of the Dark Energy Spectroscopic Instrument (DESI) Year 1 data, showing a slice of the larger 3D map that DESI is constructing during its five-year survey. DESI is mounted on the Nicholas U. Mayall 4-meter Telescope at Kitt Peak National Observatory. Credit: DESI Collaboration/KPNO/NOIRLab/NSF/AURA/P. Horálek/R. Proctor
:::


### Systèmes de coordonnées

Les équations de la physique classique sont valables en utilisant des quantités physiques (non comobiles) : distance propre, temps propre, etc... L'utilisation des distances physiques comme système de coordonnées est cependant peu pratique dans un Univers en expansion. Une méthode plus pratique consiste à écrire l'équation dans l'espace comobile. Notons :
- $\vec{r}$ le vecteur position physique (dont la norme est la distance propre $D_p(t)$),
- $\vec{\sigma}$ le vecteur position comobile (dont la norme est la distance comobile $\chi$), 
- $\vec{v}_r$ la vitesse physique,
- $\vec{v}_{\sigma}$ la vitesse comobile. 

Nous avons les relations suivantes :
\begin{align}
\vec{r}& =a(t) \vec{\sigma} \\ \notag
\vec{v}_r& =\dot{a}\vec{\sigma}+a \vec{v}_{\sigma} \label{vel-rel}
\end{align}
Bien que le flot de Hubble (premier terme de [](#vel-rel)) ne doive pas être considéré comme une vitesse réelle, il apparaît dans la relation entre $\vec{v}_r$ et $\vec{v}_{\sigma}$. Cela poserait un problème si elle pouvait prendre des valeurs de l'ordre de $c$ (ou plus grandes). Mais la condition selon laquelle $\vec{r} \ll R_H$ garantit que $\dot{a}\vec{\sigma} \ll c$ (voir section [](#sec-validity)). 

Comment passer du système de coordonnées physiques au système de coordonnées comobiles ? La conversion des dérivées partielles spatiales est assez simple :
\begin{equation}
\nabla_\mathbf{r} = {\partial \over \partial r^i} = {1 \over a} {\partial \over \partial \sigma^i}  = \frac{1}{a} \nabla_\sigma,\qquad \nabla^2_\mathbf{r} = \frac{1}{a^2} \nabla^2_{\sigma}
\end{equation}

La dérivée partielle temporelle nécessite un examen plus attentif. Écrivons la différentielle d'une fonction du temps et de l'espace quelconque $f(t,\vec{r})$ :
\begin{align}
\dd f&= \left. {\partial f\over \partial t} \right|_\mathbf{r} \dd t + \left.{\partial f\over \partial r^i}\right|_\mathbf{t} \dd r^i   \\
&=  \left. {\partial f\over \partial t} \right|_\mathbf{r} \dd t + \left.{\partial f\over \partial r^i}\right|_\mathbf{t} \dd(a \sigma^i)  \\
&=  \left. {\partial f\over \partial t} \right|_\mathbf{r} \dd t + {1 \over a}\left.{\partial f\over \partial \sigma^i}\right|_\mathbf{t} (\sigma^i \dd a + a \dd \sigma^i)\\
&= \left( \left. {\partial f\over \partial t} \right|_\mathbf{r} + {\dot{a} \over a} (\vec{\sigma}\cdot \vec \nabla_{\sigma})f \right) \dd t + \left.{\partial f\over \partial \sigma^i}\right|_\mathbf{t} \dd \sigma^i 
\end{align}
 Donc par identification :
\begin{equation}
 \left. {\partial \over \partial t} \right|_\mathbf{r}= \left. {\partial \over \partial t} \right|_{\sigma} - H (\vec{\sigma}\cdot \vec \nabla_{\sigma})
\end{equation}

### Conservation de la masse

Dans l'espace physique, l'équation de continuité s'écrit :
\begin{equation}
\left.{\partial \rho \over \partial t}\right|_\mathbf{r} + \vec \nabla_\mathbf{r} \cdot (\rho \vec{v}_\mathbf{r})=0
\end{equation} 

En utilisant la densité comobile $\rho_{\sigma}=\rho a^3$, nous pouvons exprimer cette équation dans l'espace comobile :
\begin{align}
\left.{\partial \rho_{\sigma}\, a^{-3} \over \partial t}\right|_{\sigma} - H (\vec{\sigma}.\nabla_{\sigma})(\rho_{\sigma} \, a^{-3})+{1 \over a} \nabla_{\sigma}\left[\rho_{\sigma} \, a^{-3} (\dot{a}\vec{\sigma}+a \vec{v}_{\sigma})\right] &=&0
\end{align}
En introduisant la formule classique du calcul vectoriel 
$$\vec \nabla \cdot (\phi \vec{A})=\vec{A}\cdot \vec \nabla\phi+ \phi\  \vec  \nabla \cdot \vec{A}$$
où $\phi$ est un scalaire et $\vec{A}$ un vecteur, l'équation ci-dessus se réduit à :
\begin{equation}\label{Cont_comov}
\boxed{\left.{\partial \rho_{\sigma}\over \partial t}\right|_{\sigma} + \vec \nabla_{\sigma} \cdot (\rho_{\sigma} \vec{v}_{\sigma})=0}
\end{equation}
L'équation de continuité prend donc exactement la même forme dans l'espace comobile, en utilisant des variables comobile. Ce n'est toutefois pas le cas si l'on utilise la vitesse particulière $a \vec{v}_{\sigma}$.


### Équation d'Euler

Dans l'espace physique, l'équation d'Euler pour un fluide parfait (non visqueux) autogravitant prend la forme habituelle :
\begin{equation}
\left. {\partial \vec{v_r} \over \partial t} \right|_\mathbf{r}+ \left(\vec{v}_r\cdot \vec \nabla_\mathbf{r}\right) \vec{v_r}=-\vec \nabla_\mathbf{r}\phi - \frac{1}{\rho} \vec \nabla_\mathbf{r} P
\end{equation}
Dans l'espace comobile, elle se transforme en :
\begin{align*}
\left. {\partial (\dot{a}\vec{\sigma}+a\vec{v}_{\sigma}) \over \partial t} \right|_{\sigma} & - H \vec{\sigma}\cdot \vec \nabla_{\sigma}(\dot{a}\vec{\sigma} + a\vec{v}_{\sigma}) + (\dot{a}\vec{\sigma}+a\vec{v}_{\sigma}) \cdot  {1 \over a}\vec \nabla_{\sigma} (\dot{a}\vec{\sigma}+a\vec{v}_{\sigma}) \\
& = -{1 \over a^2} \vec  \nabla_{\sigma}\phi_{\sigma} - \frac{1}{a \rho} \vec \nabla_{\sigma} P
\end{align*}
avec $\phi_\sigma = a \phi$ le potentiel comobile. En veillant à ce que  :
$$\left. {\partial (\dot{a}\vec{\sigma}+a\vec{v}_{\sigma}) \over \partial t} \right|_{\sigma}=\ddot{a}\vec{\sigma}+\dot{a}\vec{v}_{\sigma}+a \left.{\partial \vec{v}_{\sigma} \over \partial t}\right|_{\sigma}$$
l'équation d'Euler en coordonnées comobiles se réduit à :
\begin{equation}\label{Euler_comv}
\boxed{\left.{\partial \vec{v}_{\sigma} \over \partial t} \right|_{\sigma} + 2 H \vec{v}_{\sigma}+(\vec{v}_{\sigma} \cdot \vec \nabla_{\sigma})\vec{v}_{\sigma}= -{1 \over a^3} \vec  \nabla_{\sigma}\phi_{\sigma} - \frac{1}{a^2 \rho} \vec\nabla_{\sigma}P  - {\ddot{a} \over a} \vec{\sigma} }
\end{equation}

Nous pouvons voir deux termes supplémentaires par rapport à la version de l'équation d'Euler écrite en coordonnées physiques. Le terme supplémentaire $2 H \vec{v}_{\sigma}$ est une force de traînée créée par l'expansion sur les vitesses comobiles.

Le dernier terme paraît étrange. En effet, il semble annuler la force newtonienne créée à $\vec{\sigma}$ par un fond de densité homogène non nul. On pourrait arguer que cette force devrait être nulle, pour des raisons de symétrie. Cependant, en appliquant le théorème de Gauss, on peut trouver une force non nulle dirigée vers l'origine des coordonnées (où qu'elle soit choisie !). Le fait est que l'équation de Poisson se comporte mal (et ne doit pas être utilisée) pour un champ source dont la norme $L^2$ n'est pas finie. 
Mais bien sûr, cela implique des échelles au-delà de $R_H$ où nous ne nous attendons pas à ce que notre théorie tienne la route. En ce qui concerne les perturbations de la densité, nous soustrairons la valeur moyenne non nulle et nous nous débarrasserons ainsi de cette incohérence à grande échelle.  


### Equation de Poisson

Dans un univers sans constante cosmologique, de la relativité générale on en déduit l'équation de Poisson habituelle dans la limite des champs faibles [](#eq:poisson) :
\begin{equation}
\triangle_\mathbf{r} \phi = 4 \pi \GN \rho
\end{equation}
où $\phi$ est le potentiel gravitationnel. Compte tenu de la relation entre le potentiel et la force newtonienne, le potentiel comobile est naturellement défini comme $\phi_{\sigma}=\phi a$, et l'équation de Poisson est également inchangée dans l'espace comobile :
\begin{equation}
\triangle_{\sigma} \phi_{\sigma} = 4 \pi \GN \rho_{\sigma}
\label{Poisson_comov}
\end{equation}

:::{note} Influence de la constante cosmologique

Si l'on considère une constante cosmologique, dans la limite du champ faible, la gravitation est régie par l'équation de Poisson modifiée 
$$ \triangle_\mathbf{r} \phi = 4 \pi \GN \rho -c^2 \Lambda$$
qui se transforme en 
$$ \triangle_{\sigma} \phi_{\sigma} = 4 \pi \GN \rho_{\sigma} -c^2 \Lambda a^3$$
:::


Théorie newtonienne des perturbations 
-----------------------------------------

### Solution d'ordre 0

L'équation de conservation de la masse dans l'espace comobile [](#Cont_comov) admet la solution d'ordre 0 suivante pour un Univers homogène et isotrope :
\begin{equation}
\rho_{{\sigma},0}= \cst, \qquad \vec{v}_{{\sigma},0}= \vec 0
\end{equation}
A l'ordre 0, La densité massique reste donc stationnaire et homogène et il n'y a aucune vitesse particulière.
L'intégration de l'équation de Poisson [](#Poisson_comov) en coordonnées sphériques[^LaplacienSphérique] donne :
$$ \phi_{\vec{\sigma},0} = \frac{4}{6} \pi \GN \rho_{\sigma,0} \sigma^2 $$
Si on utilise les équations de Friedmann [](#eq:ddota) :
$$\frac{\ddot a}{a} = -\frac{4 \pi \GN}{3}(\epsilon + 3P)$$
pour un Univers dominé par la matière avec $\Lambda=0$ et $\epsilon = c^2 \rho_{\sigma,0} a^{-3} \gg P$, on obtient la force gravitationnelle :
$$-\vec \nabla \phi_{{\sigma},0} = -{4 \pi \GN \rho_{\sigma,0} \over 3 } \vec{\sigma} \approx a^3 \frac{\ddot a}{a} \vec{\sigma}$$
Le gradient du champ gravitationnel donne à l'ordre 0 une force centrifuge. 

A partir de l'équation d'Euler [](#Euler_comv) et des résultats précédents, on aboutit alors à :
$$P = \cst = P_0$$


### Solution linéaire d'ordre 1

Considérons de petites perturbations autour de la solution d'ordre zéro :
\rho_{\sigma}=\rho_0(1+\delta) \qquad \vec{v}_{\sigma}=\vec{v}_0+\delta\vec{v} \qquad \phi_{\sigma}=\phi_0 + \delta \phi_{\sigma}, \qquad P = P_0 + \delta P
\end{equation}
La quantité $\delta$ est appelée contraste de densité et est très utilisée dans la théorie de la formation des structures. Notons qu'elle a la même valeur dans l'espace physique et dans l'espace comobile. En injectant ces expressions dans les équations de continuité, de Poisson et d'Euler, la solution d'ordre zéro s'annule (comme prévu) et en supprimant les termes d'ordre 2, nous obtenons l'ensemble d'équations linéarisé :
$$
\label{eq:lssMassOrder1}
{\partial \delta \over \partial t} + \vec{\nabla}_{\sigma} \cdot \delta\vec{v}_r = 0
$$
$$
\label{eq:lssEuler1}
{\partial \delta\vec{v}_\sigma \over \partial t} + 2 H \delta\vec{v}_\sigma =  - {1 \over a^3} \vec \nabla_{\sigma} \delta \phi_{\sigma} - \frac{1}{a^2 \rho_0} \vec \nabla_{\sigma} \delta P
$$
$$
\label{eq:lssPoissonOrder1}
\triangle_{\sigma}^2 \delta \phi_{\sigma} = 4 \pi \GN \rho_{\sigma,0} \delta 
$$

En prenant la divergence de l'équation d'Euler linéarisée [](#eq:lssEuler1), la dérivée temporelle de l'équation de conservation de la masse linéarisée [](#eq:lssMassOrder1) et en réinjectant l'équation de Poisson [](#eq:lssPoissonOrder1), nous obtenons finalement :
$$\ddot{\delta}+ 2 H \dot{\delta}  - \frac{1}{a^2 \rho_0} \triangle_{\sigma} \delta P = 4 \pi \GN {\rho_0 } \delta$$
On introduit la vitesse du son $c_s$ dans le milieu pour des compressions adiabatiques :
$$c_s^2 = \frac{1}{\rho_0 \chi_S} =  \left.\frac{\partial P}{\partial \rho}\right\vert_{S} \approx \frac{\delta P}{\delta \rho}\Rightarrow \delta P \approx c_s^2 \rho_0 \delta $$
Alors on obtient l'équation de croissance des perturbations dans l'espace comobile :
\begin{equation}\label{fluct_growth}
\boxed{ 
\ddot{\delta}+ 2 H \dot{\delta}  - \frac{c_s^2}{a^2} \triangle_{\sigma} \delta = 4 \pi \GN \rho_0 \delta
}
\end{equation}

### Vitesse du son

Dans un Univers dominé par la radiation, les propriétés du gaz relativiste sont :
$$\rho_r \propto T^4, \quad P_r = \rho_r c^2 /3$$
d'où la vitesse du son dans le plasma relativiste :
$$c_s^2 = \left.\frac{\partial P_r}{\partial \rho_r}\right\vert_{S} \approx \frac{c^2 \delta \rho_r}{3\delta \rho_r}
\Rightarrow \boxed{c_s = \frac{c}{\sqrt{3}} \approx 0.58 c}$$

Dans un Univers dominé par la matière non relativiste, les propriétés thermodynamiques des baryons sont :
$$
\rho_b = n_b m_b + \frac{n_b k_B T}{(\gamma_b -1)c^2},\quad P_b = n_b k_B T
$$
avec $m_b=(1-Y_p)m_\mathrm{H} + Y_p m_{\mathrm{He}} \approx 1.72 m_p$ la masse effective des baryons dans un mélange de gaz d'hydrogène atomique et d'hélium (notez la ressemblance avec [](#eq:mair)), et $\gamma_b=5/3$ l'indice adiabatique des baryons car l'hydrogène est sous forme atomique (et l'hélium bien sûr). Pour une transformation adiabatique réversible, avec la loi de Laplace on a $P_b \rho_b^{-\gamma_b}=\cst$, la température des baryons $T_b$ évolue en :
$$P_b = n_b k_B T_b \propto a^{-3\gamma_b}$$
Or $n_b \propto a^{-3}$ donc 
$$T_b = T_{\mathrm{dec}} \left(\frac{a}{a_{\mathrm{dec}}}\right)^{-3(\gamma_b -1)}$$
La vitesse du son dans le gaz de baryons est :
$$c_s^2 = \left.\frac{\partial P_b}{\partial \rho_b}\right\vert_{S} \approx \gamma_b \rho^{\gamma_b-1} = \frac{\gamma_b n_b k_B T_b}{n_b m_b} \Rightarrow \boxed{c_s(T_b) = \sqrt{\frac{\gamma_b k_B T_b}{m_b}} \ll c}$$
Juste après le découplage des photons et des électrons, la température des baryons est de $T_{\mathrm{dec}} = 3055\,\kelvin$ donc la vitesse du son dans le gaz de baryons est d'environ $1.5 \times 10^{-5}c \approx 5\,\mathrm{km}/\mathrm{s}$. Le changement est de plusieurs ordres de grandeur donc l'évolution des perturbations change drastiquement à cet instant. Puis la température des baryons décroît en $a^{-2}$, du moins tant que le chauffage par le rayonnement interstellaire ne change la donne (autour de $z\sim 10$), donc la vitesse du son décroît en $a^{-1}$. 

:::{figure} #LSS_cs
:name: fig:LSS_cs
:align: center
:width: 70%

Vitesse du son dans l'Univers en fonction du facteur d'échelle $a$. La légère diminution entre l'équivalence et le découplage est donnée par l'équation [](#eq:csrhobrhog) (voir encadré). Le calcul est inexact quand on rentre dans le régime non-linéaire de la croissance des structures i.e. lorsque $\delta \sim 1$ (région grisée). De plus, vers ce redshift également, le gaz de baryons est chauffé par le rayonnement stellaire donc la température des baryons n'évolue plus en $a^{-2}$.
:::

:::{note} Mélange de baryons et de photons couplés
:class: dropdown

Tant que les photons sont couplés aux électrons libres, ils sont mécaniquement couplés au gaz de baryons par la force de Coulomb. Pendant la période où l'Univers est dominé par la matière mais où les photons sont encore couplés aux électrons ({cite}`Weinberg1989` p.509,566) :
$$\rho_{\mathrm{tot}} = \rho_b + \frac{n_b k_B T}{(\gamma_b -1)c^2} + \rho_\gamma \approx \eta m_b n_\gamma + \rho_\gamma $$
$$P_{\mathrm{tot}} = n_b k_B T + \frac{1}{3}\epsilon_\gamma \approx \frac{1}{3}\rho_\gamma c^2 $$
\begin{align*}
c_s^2 & = \left.\frac{\partial P_{\mathrm{tot}}}{\partial \rho_{\mathrm{tot}}}\right\vert_{S} \approx  \frac{\delta P_{\mathrm{tot}}}{\delta \rho_{\mathrm{tot}}} \approx \frac{\frac{4}{3}\frac{\delta T}{T}\epsilon_\gamma}{3 \eta m_b n_\gamma \frac{\delta T}{T} +  4 \frac{\delta T}{T}\rho_\gamma} \\
& = \frac{c^2}{3} \frac{1}{\left(1 + \frac{3}{4} \frac{\eta n_\gamma m_b c^2}{\epsilon_\gamma}  \right)} = \frac{c^2}{3} \frac{1}{\left(1 + \frac{3}{4} \frac{\rho_b}{\rho_\gamma}  \right)} 
\end{align*}
$$
\label{eq:csrhobrhog}
c_s = \frac{c}{\sqrt{3}} \frac{1}{\sqrt{\left(1 + \dfrac{3}{4} \dfrac{\Omega_b^0}{\Omega_\gamma^0(1+z)}  \right)} }
$$

:::

### Instabilité de Jeans

Les solutions à l'équation d'évolution des perturbations [](#fluct_growth) seront étudiées au prochain semestre, mais on peut déjà étudier leurs comportements à partir de leur relation de dispersion. Recherchons des solutions en ondes planes de la forme :
$$\delta \propto e^{i(\omega t - \vec k_\sigma \cdot \vec \sigma)}$$
et étudions les solutions dans le domaine de Fourier. La relation de dispersion s'écrit :
$$-\omega^2 + 2 i H \omega - \frac{c_s^2}{a^2} k^2_\sigma = 4 \pi \GN \rho_0$$
En négligeant le terme d'amortissement (de l'ordre de l'âge de l'Univers) devant le temps caractéristique d'évolution des perturbations ($\omega \gg H$), on aboutit à :
$$\boxed{\omega^2 = c_s^2 \left( k_r^2 - \frac{4\pi \GN \rho_0}{c^2_s}\right) }$$
avec $k_\sigma = 2 \pi / \chi =  a k_r$. C'est la même relation de dispersion que celle des ondes électromagnétiques dans un plasma. On définit la longueur d'onde de Jeans (<doi:10.1098/rsta.1902.0012>) $k_J$ et la longueur de Jeans $\lambda_J$ par :
$$\boxed{k_J = \sqrt{\frac{4\pi \GN \rho_0}{c^2_s}},\quad  \lambda_J = \frac{2\pi}{k_J} = c_s \sqrt{\frac{\pi}{\GN}}\rho_0 }$$
* Si $k_r > k_J \Leftrightarrow \lambda < \lambda_J$, alors $\omega^2 > 0$ donc on a une solution oscillante i.e. une onde acoustique qui se propage : les perturbations de taille petite devant la longueur de Jeans oscillent grâce à la force de pression.
* Si $k_r < k_J \Leftrightarrow \lambda > \lambda_J$, $\omega^2 < 0$ donc on a une solution non oscillante en exponentielle : les grandes structures évoluent seulement sous l'effet de la gravité et s'accroissent (et les vides décroissent).

Comme l'échelle $\lambda$ évolue avec l'expansion ($\lambda \propto a$) ainsi que la longueur de Jeans, la discussion n'est pas aisée à mener le long de l'histoire de l'Univers. Définissons $M$ la masse dans une sphère de rayon $\lambda$, conservée avec l'expansion, et comparons-la à la masse de Jeans $M_J$
$$M_J = \frac{4}{3} \pi \rho_0 \lambda_J^3 \propto \frac{c_s^3}{\GN^{3/2}n \rho_0^{1/2}}$$
* Si $M < M_J$, alors la structure est trop légère et la pression peut compenser la force de gravité: la structure oscille.
* Si $M > M_J$, alors la structure est trop lourde et s'effondre gravitationnellement.

Le tracé de la masse de Jeans en fonction du facteur d'échelle $a$ permet de prédire quelles sont les structures pouvant s'effondrer gravitationnellement et celles dont la croissance est empêchée [](#fig:LSS_MJ) ({cite}`Weinberg1989` p. 565).

:::{figure} #LSS_MJ
:name: fig:LSS_MJ
:align: center
:width: 70%

Evolution de la masse de Jeans en fonction du facteur d'échelle $a$. Le calcul est inexact quand on rentre dans le régime non-linéaire de la croissance des structures i.e. lorsque $\delta \sim 1$ (région grisée). De plus, vers ce redshift également, le gaz de baryons est chauffé par le rayonnement stellaire donc la température des baryons n'évolue plus en $a^{-2}$.
:::

Décrire la croissance des structures avant la recombinaison contredit l'hypothèse non-relativiste sur laquelle repose notre étude. Cependant, l'échelle de la vitesse du son reste une échelle pertinente et de plus la matière non-relativiste domine après l'équivalence. Sachant cela (et que l'étude relativiste ne donne pas de résultats fondamentalement différence de ce qui suit), on va se permettre de discuter de la croissance des grandes structures dans l'Univers primordial et récent (bien qu'elle soit non-linéaire aujourd'hui).

D'après la [](#fig:LSS_MJ), on voit qu'avant le découplage des structures ayant la masse d'une galaxie ou d'un amas de galaxie ne sont pas suffisamment lourdes pour s'effondrer (ou alors juste dans les premiers instants de l'Univers). Des ondes de pression les parcourent et elles oscillent. Toutefois après le découplage, la vitesse du son chute de 5 ordres de grandeur. Le découplage des photons gèl les ondes de pression et des structures de la masse de galaxies et même de galaxies naines peuvent commencer leur croissance.





### Description statistique des perturbations AWFUL DRAFT


Nous définissons le spectre de puissance $P(k)$ à l'aide de la relation :
\begin{equation}
\langle \hat{\delta}(\mathbf{k}) \hat{\delta}(\mathbf{k^\prime}) \rangle= P(k) (2 \pi)^3 \delta_D(\mathbf{k+k^\prime}) 
\end{equation}
où $\delta_D$ désigne la fonction delta de Dirac. En se rappelant que les parties réelles et imaginaires des coefficients de Fourier de $\delta$ sont des réalisations indépendantes d'une fonction de probabilité gaussienne, et que puisque $\delta$ est réel, $\hat{\delta}(\mathbf{k})$ et $\hat{\delta}(\mathbf{-k})$ sont des conjugués complexes, il est assez facile de montrer que $\P(k)$ est proportionnel à la variance de la distribution de probabilité gaussienne des coefficients de Fourier. En injectant cette relation dans [](#correl_transf) et en intégrant sur $k$, nous obtenons :
\begin{equation}
\xi(r)= {1 \over (2 \pi)^3} \int P(k^\prime) e^{i\mathbf{k^\prime.r}} d^3k\prime
\end{equation}

$$\Delta^2(k)= {k^3 \over 2 \pi^2}. P(k)$$

#### Champs aléatoires

Un champ aléatoire 3D est un ensemble de variables aléatoires $Y(\vec{\sigma})$, une pour chaque emplacement (ou cube infinitésimal de volume $dx^3$) dans l'espace 3D. Un tel champ est caractérisé par une collection de fonctions de distribution de probabilités conjointes :

\begin{equation}
P_n(Y(\mathbf{x_1})=y_1,\dots, Y(\mathbf{x_n})=y_n)
\end{equation}

La fluctuation initiale de la densité peut être décrite comme un type particulier de champ aléatoire.
\subsubsection{Le principe cosmologique et les champs aléatoires}
D'une manière très générale, nous avons énoncé le principe cosmologique comme étant \textit{l'univers étant homogène et isotrope à des échelles suffisamment grandes}. Si l'on considère maintenant que les fluctuations de densité initiales de notre univers, décrites par la surdensité $\delta$, sont 
simplement une réalisation d'un champ aléatoire caractérisé par les fonctions de distribution de probabilité jointes $P_n$, nous pouvons appliquer les conditions d'homogénéité et d'isotropie aux fonctions de distribution elles-mêmes. Ainsi, nous exigeons qu'elles soient invariantes par translation et rotation. Par exemple, la fonction de distribution en un point de
la surdensité ne doit pas dépendre de l'emplacement. 

#### Champs aléatoires gaussiens

La variante la plus simple de l'inflation prédit que les fluctuations de la densité primordiale sont en fait un champ aléatoire gaussien homogène. Dans ce cas, la fonction $P_1$ est
simplement une fonction de probabilité gaussienne avec une variance indépendante de l'emplacement. 
Les valeurs de $\delta$ à deux endroits différents ne sont cependant pas non corrélées, et il n'est donc pas si facile de construire une réalisation des fluctuations de densité initiales dans l'espace réel. Il est beaucoup plus facile de le faire dans l'espace de Fourier en raison des deux propriétés suivantes :

\begin{enumerate}
\item La transformée de Fourier du champ aléatoire gaussien est un champ aléatoire gaussien. Ainsi, les parties réelle et imaginaire de $\hat{\delta}(\mathbf{k})$ (la transformée de Fourier de $\delta(\vec{\sigma})$) sont des variables aléatoires avec des fonctions de distribution de probabilité gaussiennes.
\item L'exigence d'homogénéité se traduit dans l'espace de Fourier par le fait que les coefficients de Fourier sont des réalisations indépendantes de la fonction de probabilité (dépendant de k).
\end{itemize}

Ainsi, un champ aléatoire gaussien est plus facilement décrit et généré dans l'espace de Fourier.
La seule chose dont nous avons besoin pour caractériser le champ est une prescription sur la façon dont la
variance de la fonction de probabilité gaussienne dépend de $\mathbf{k}$. Cette information est fournie par ce que l'on appelle le spectre de puissance. 
\sous-section{fonction de corrélation à 2 points et spectre de puissance}
Nous avons mentionné que dans l'espace réel, les valeurs d'un champ aléatoire gaussien homogène sont tirées d'une seule fonction de probabilité, mais ne sont pas indépendantes (fonction de corrélation non nulle). En revanche, dans l'espace de Fourier, elles sont indépendantes mais tirées d'une fonction gaussienne dont la variance dépend de la valeur de la fonction de corrélation.
fonction gaussienne dont la variance dépend de $\mathbf{k}$. En fait, les corrélations dans l'espace réel sont déterminées par la dépendance k de la variance dans l'espace de Fourier. Cette dépendance est quantifiée par la relation entre les
est quantifiée par la relation entre la fonction de corrélation en 2 points et le spectre de puissance.

Utilisons la convention suivante pour les transformées de Fourier directe et inverse :

\begin{equation}
\hat{f}(\mathbf{k})= \int f(\vec{\sigma}) e^{-i \mathbf{k.x}} d^3x
\end{equation} 
\begin{equation}
f(\vec{\sigma})= {1 \over (2 \pi)^3}\int \hat{f}(\mathbf{k}) e^{i \mathbf{k.x}} d^3k
\end{equation} 
La fonction de corrélation en deux points de la surdensité (ou de toute autre quantité) est définie comme suit :

\begin{equation}
\xi(\mathbf{x_1},\mathbf{x_2})=\langle \delta(\mathbf{x_1}) \delta(\mathbf{x_2})\rangle
\end{equation}
où $\langle\dots \rangle$ désigne la moyenne sur de nombreuses réalisations du champ aléatoire, également appelée "moyenne d'ensemble". Puisque $\xi$ est complètement déterminé par les $P_1$ et $P_2$ sous-jacents, qui sont invariants par translation et rotation en raison du principe cosmologique, $\xi$ est une fonction de $r=|\mathbf{x_2}-\mathbf{x_1}|$ seulement.
Pour montrer la relation entre $\xi$ et le spectre de puissance, insérons la transformée de Fourier de $\delta_1$. 
transformée de Fourier de $\delta$ dans l'expression simplifiée $\xi(r)$.
\begin{align}
\xi(r)&=&\langle \delta(\vec{\sigma}) \delta(\vec{\sigma}+\vec{r}) \rangle \\
      &=& \left\langle {1 \over (2 \pi)^6} \int \int \hat{\delta}(\mathbf{k}) e^{i \mathbf{k.x}} \hat{\delta}(\mathbf{k^\prime}) e^{i \mathbf{k^\prime.(x+r)}} d^3k \,\,d^3k^\prime \right\rangle \\
      &=& {1 \over (2 \pi)^6} \int \int \langle \hat{\delta}(\mathbf{k}) \hat{\delta}(\mathbf{k^\prime}) \rangle \,\, e^{i \mathbf{(k+k^\prime).x}}\,  e^{i \mathbf{k^\prime.r}} d^3k \,\,d^3k^\prime  \label{correl_transf}
\end{align}

Nous définissons le spectre de puissance $P(k)$ à l'aide de la relation :
\begin{equation}
\langle \hat{\delta}(\mathbf{k}) \hat{\delta}(\mathbf{k^\prime}) \rangle= P(k) (2 \pi)^3 \delta_D(\mathbf{k+k^\prime}) 
\end{equation}
où $\delta_D$ désigne la fonction delta de Dirac. En se rappelant que les parties réelles et imaginaires des coefficients de Fourier de $\delta$ sont des réalisations indépendantes d'une fonction de probabilité gaussienne, et que puisque $\delta$ est réel, $\hat{\delta}(\mathbf{k})$ et $\hat{\delta}(\mathbf{-k})$ sont des conjugués complexes, il est assez facile de montrer que $\P(k)$ est proportionnel à la variance de la distribution de probabilité gaussienne des coefficients de Fourier. En injectant cette relation dans [](#correl_transf) et en intégrant sur $k$, nous obtenons :
\begin{equation}
\xi(r)= {1 \over (2 \pi)^3} \int P(k^\prime) e^{i\mathbf{k^\prime.r}} d^3k\prime
\end{equation}
Cela montre que la fonction de corrélation en deux points est simplement la transformée de Fourier du spectre de puissance.
Les deux encodent les mêmes informations sur le champ aléatoire gaussien.

On notera que même lorsqu'elle est appliquée à une quantité sans dimension, $P(k)$ a une dimension de $k^{-3}$. Il est donc tout à fait habituel de définir le spectre de puissance "sans dimension" $\Delta^2(k)= {k^3 \over 2 \pi^2}. P(k)$. Cette quantité est significative lorsque l'on considère la variance du signal dans l'espace réel, qui peut être calculée comme suit :
\begin{align}
 \langle \delta(x)^2 \rangle &=& \xi(0) \\
&=& {1 \over (2 \pi)^3} \int  P(k) d^3 k \\
&=& \int  \Delta^2(k)\,\, d\,\ln(k)
\end{align}
Nous voyons que $\Delta^2$ quantifie la contribution à la variance (en quelque sorte la densité d'énergie) du signal de l'espace réel par cellule logarithmique.



### Ondes acoustiques dans l'Univers primordial 

Avant le découplage, des ondes acoustiques parcourent le plasma primordial. Définissons l'horizon sonore comobile comme :
$$r_s^c = \int_0^{t_\mathrm{dec}} \frac{c_s(t) \dd t}{a(t)} = \int_{z_\mathrm{dec}}^\infty \frac{c_s(z)}{H(z)}\dd z $$
la distance comobile maximum parcouru par une onde acoustique depuis le début de l'Univers. Au moment du découplage, elle vaut $150\,\Mpc/a_\mathrm{dec}$ soit $r_s = a_\mathrm{dec} r_s^c \approx 0.13\,\Mpc$. C'est donc la distance qu'a pu parcourir une onde issue d'une surdensité présente au Big Bang.
Cette propagation des ondes se traduit par une corrélation positive sur la présence de matière à cette échelle spatiale fondamentale. Cette échelle se convertit en séparation angulaire sur le ciel, imprimée sur la carte des anisotropies de température du CMB et donnée par :
$$\boxed{ \theta_s = \frac{r_s}{D_A(z_{\mathrm{dec}})} }$$
Une échelle dans l'espace des distances donne un spectre de puissance de forme sinusoïdale dans l'espace réciproque. La mesure de la position des maxima dans le spectre de puissance des anisotropie de température du CMB permet d'aboutir à une extrêmement précise de l'horizon sonore {cite:p}`Planck2018`:
$$100 \theta_s = 1.04123 \pm 0.00046\,\mathrm{rad}, \quad \mathrm{i.e.}\quad \theta_s \sim 0.6\,\degree$$
qui constitue un des 6 paramètres libres du modèle $\Lambda$CDM.

:::{figure} ../../notebooks/movie.mp4
:name: fig:cmb_anisotropies
:width: 100%

Evolution temporelle d'un champ Gaussien initial sous l'effet de la propagation acoustique.
:::

:::{note} Conditions initiales adiabatiques ou isocourbures?
:class: dropdown

TODO

:::



### Profondeur optique

On définit la profondeur optique $\tau$ par le rapport du nombre de photons reçus sur Terre sans avoir subi aucune diffusion Thomson $N(t_0)$ sur le nombre de photons $N(t)$ émis à un instant $t$:
$$\frac{N(t_0)}{N(t)} = e^{-\tau}$$
avec
$$\tau = \int_{t_{\mathrm{ls}}}^{t_0} \Gamma_\gamma(t) \mathrm{d}t$$
Le temps $t_{\mathrm{ls}}$ pour lequel $\tau=1$ est appelé temps de dernière diffusion. C'est le temps depuis lequel un photon du CMB n'a plus interagi avec un électron. Plus précisément,
\begin{equation}
\tau(z) = \int_0^z \frac{\Gamma_\gamma(z)}{H(z)}\frac{\dd z}{1+z}
\end{equation}
C'est un des six paramètres du modèle standard $\Lambda$CDM. En effet, après l'émission du fond diffus cosmologique, on entre dans les Ages Sombres de l'Univers, où l'Univers est transparent mais aucun astre n'émet encore de lumière. Mais avec la naissance des premières étoiles et galaxies, peut-être 150 millions d'années après le Big Bang, le milieu neutre est de nouveau ionisé. Bien que très peu dense, les photons du CMB interagissent de nouveau avec les électrons par diffusion Thomson, ce qui diminue l'amplitude des anisotropies de petites échelles dans le spectre de puissance du CMB, et introduit de nouvelles anisotropies dans les anisotropies de polarisation. C'est le paramètre le moins bien mesuré du modèle $\Lambda$CDM pour le moment ([](#fig:tau)) $\tau = 0.058 \pm 0.006$ {cite:p}`Planck2023`, mais il informe sur l'apparition des premiers astres lumineux ([](#fig:tau_reio)).

:::{figure} ../../images/tau_history.png
:width: 80%
:align: center
:label: fig:tau

The optical depth to reionization $\tau$ measured as a smearing of the CMB angular power spectrum (d'après [https://lambda.gsfc.nasa.gov/education/graphic_history/taureionzation.html](https://lambda.gsfc.nasa.gov/education/graphic_history/taureionzation.html), image credit: NASA / LAMBDA Archive Team).
:::

:::{figure} #tau_reio
:width: 80%
:align: center
:label: fig:tau_reio

En supposant que l'Univers est de nouveau complètement ionisé, le calcul de sa profondeur optique montre que si aujourd'hui on mesure $\tau=0.058$ alors la reionization de l'Univers devait être complète autour de $z_{\mathrm{reio}} \sim 7$ donnant un début de la formation des galaxies antérieure à 1 milliard d'années après le Big Bang.
:::


:::{iframe} https://www.youtube.com/embed/AgX3lZEr240?si=Bz-eTpQWw3NxU_e3
:name: fig:desi_growth_de
:align: center
:width: 60%

Cette simulation montre comment la gravité affecte la position des galaxies observées, modifiant ainsi la façon dont la matière s’agglomère pour former les structures cosmiques. Comme différents modèles de gravité prédisent différentes formations des structures, les scientifiques de DESI peuvent comparer les observations avec les prédictions et ainsi tester la gravité aux échelles cosmiques. Credit: Claire Lamman et Michael Rashkovetskyi / DESI collaboration:::





#### BACKUP

[^cisotherme]: si on avait utiliser l'hypothèse isotherme, on utiliserait plutôt l'équation d'état $PV=\cst$ et la vitesse du son serait différente d'un facteur $\sqrt{\gamma}$.

[^deltas]: avec les ordres de grandeurs de [](#fig:universe_scales) et $\rho_0\sim 6\text{ protons/m}^3$, pour une planète $\delta \sim 10^{32}$ alors que pour un super-amas $\delta \sim 6$

[^LaplacienSphérique]: $$\triangle_\sigma = \frac{1}{\sigma^2} \frac{\partial}{\partial \sigma}\left( \sigma^2 \frac{\partial}{\partial \sigma}\right)$$.
