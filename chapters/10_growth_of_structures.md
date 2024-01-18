---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
  '\kelvin': '\mathrm{K}'
  '\GeV': '\mathrm{GeV}'
  '\MeV': '\mathrm{MeV}'
---

Formation des grandes structures de l'Univers
===============================

Jusqu'à présent, nous avons étudié l'évolution d'un Univers homogène, au moins aux très grandes échelles au-delà d'environ $100\,$Mpc. Or, aujourd'hui on observe que la matière est clusterisée sous forme de planètes, étoiles, galaxies, amas de galaxies et super-amas de galaxies. La question qui se pose alors dans ce chapitre est : comment se forment ces structures dans un Univers en expansion ? Si la formation des astres les plus petits impliquent beaucoup de processus physiques et sont très dépendants des conditions initiales locales, il est possible d'élaborer un modèle de l'évolution des structures les plus grandes de taille $\sim 50\,$Mpc, comme les amas ou super-amas de galaxies. Pour ce faire, on va simplement utiliser une théorie newtonienne des perturbations linéaires, et calculer l'évolution de ces perturbations dans un Univers en expansion.


Régime de validité
-----------------------------

Toutefois, énonçons les conditions nécessaires à la validité de la théorie newtonienne des perturbations. Une première condition évidente est que la
perturbation de la métrique et du tenseur contrainte-énergie doit être faible. Dans le cas de la matière non relativiste, cela signifie que les perturbations de la densité doivent rester faibles. Mais pour pouvoir revenir à la gravité newtonienne dans un espace-temps homogène en expansion et n'étudier que les perturbations de la densité, il y a une autre condition. La taille des régions montrant un écart par rapport aux propriétés moyennes de l'univers (ou la longueur d'onde des modes considérés) doit être beaucoup plus petite que le rayon de Hubble $R_H={c \over H}$, car en gravitation newtonienne l'interaction se propage instantanément. Si ce n'est pas le cas, le temps que l'information d'une région en effondrement ait voyagé jusqu'à l'autre côté de la région, le facteur d'expansion a changé de manière significative : une situation qui ne peut évidemment pas être traitée en utilisant la gravité newtonienne dans un espace-temps en expansion homogène. 

Préambule
----------




Acoustique dans un espace en expansion
------------------------------------------

### Systèmes de coordonnées

Les équations de la physique classique sont valables en utilisant des quantités physiques (non comobiles) : distance propre, temps propre, etc... L'utilisation des distances physiques comme système de coordonnées est cependant peu pratique. Une méthode plus pratique consiste à écrire l'équation dans l'espace comobile. Notons :
- $\mathbf{r}$ le vecteur position physique (dont la norme est la distance propre $D_p(t)$),
- $\mathbf{x}$ le vecteur position comobile (dont la norme est la distance comobile $\chi$), 
- $\mathbf{v}$ la vitesse physique,
- $\mathbf{v_x}$ la vitesse comobile. 

Nous avons les relations suivantes :
\begin{align}
\mathbf{r}& =a(t) \mathbf{x} \\ \notag
\mathbf{v}& =\dot{a}\mathbf{x}+a \mathbf{v_x} \label{vel-rel}
\end{align}
Bien que le flot de Hubble (premier terme de [](#vel-rel)) ne doive pas être considéré comme une vitesse réelle, il apparaît dans la relation entre $\mathbf{v_r}$ et $\mathbf{v_x}$. Cela poserait un problème si elle pouvait prendre des valeurs de l'ordre de $c$ (ou plus grandes). Mais la condition selon laquelle $\mathbf{r} \ll R_H$ garantit que $\dot{a}\mathbf{x} \ll c$. 

Comment passer du système de coordonnées physique au système de coordonnées comobiles ? La conversion des dérivées partielles spatiales est assez simple :
\begin{equation}
\nabla_\mathbf{r} = {\partial \over \partial r^i} = {1 \over a} {\partial \over \partial x^i}  = \frac{1}{a} \nabla_\mathbf{x},\qquad \nabla^2_\mathbf{r} = \frac{1}{a^2} \nabla^2_\mathbf{x}
\end{equation}

La dérivée partielle temporelle nécessite un examen plus attentif. Écrivons la différentielle de $f(t,\mathbf{r})$ :
\begin{align}
\dd f&= \left. {\partial f\over \partial t} \right|_\mathbf{r} \dd t + \left.{\partial f\over \partial r^i}\right|_\mathbf{t} \dd r^i   \\
&=  \left. {\partial f\over \partial t} \right|_\mathbf{r} \dd t + \left.{\partial f\over \partial r^i}\right|_\mathbf{t} \dd(a x^i)  \\
&=  \left. {\partial f\over \partial t} \right|_\mathbf{r} \dd t + {1 \over a}\left.{\partial f\over \partial x^i}\right|_\mathbf{t} (x^i \dd a + a \dd x^i)\\
&= \left( \left. {\partial f\over \partial t} \right|_\mathbf{r} + {\dot{a} \over a} (\mathbf{x}.\nabla_\mathbf{x})f \right) \dd t + \left.{\partial f\over \partial x^i}\right|_\mathbf{t} \dd x^i 
\end{align}
 Donc par identification :
\begin{equation}
 \left. {\partial \over \partial t} \right|_\mathbf{r}= \left. {\partial \over \partial t} \right|_\mathbf{x} - H (\mathbf{x}.\nabla_\mathbf{x})
\end{equation}

### Équation de continuité

Dans l'espace physique, l'équation de continuité s'écrit :
\begin{equation}
\left.{\partial \rho \over \partial t}\right|_\mathbf{r} + \nabla_\mathbf{r} .(\rho \mathbf{v}_\mathbf{r})=0
\end{equation} 

En utilisant la densité comobile $\rho_\mathbf{x}=\rho a^3$, nous pouvons exprimer cette équation dans l'espace comobile :
\begin{align}
\left.{\partial \rho_\mathbf{x}\, a^{-3} \over \partial t}\right|_\mathbf{x} - H (\mathbf{x}.\nabla_\mathbf{x})(\rho_\mathbf{x} \, a^{-3})+{1 \over a} \nabla_\mathbf{x}\left[\rho_\mathbf{x} \, a^{-3} (\dot{a}\mathbf{x}+a \mathbf{v_x})\right] &=&0
\end{align}
En introduisant la formule classique du calcul vectoriel 
$$\nabla.(\phi \mathbf{A})=\mathbf{A}.\nabla\phi+ \phi \nabla.\mathbf{A}$$
où $\phi$ est un scalaire et $\mathbf{A}$ un vecteur, l'équation ci-dessus se réduit à :
\begin{equation}\label{Cont_comov}
\left.{\partial \rho_\mathbf{x}\over \partial t}\right|_\mathbf{x} + \nabla_\mathbf{x} .(\rho_\mathbf{x} \mathbf{v_x})=0,
\end{equation}
L'équation de continuité prend donc exactement la même forme dans l'espace comobile, en utilisant des variables comobile. Ce n'est toutefois pas le cas si l'on utilise la vitesse particulière $a \mathbf{v_x}$.


### Équation d'Euler

Dans l'espace physique, l'équation d'Euler pour un fluide parfait (non visqueux)autogravitant prend la forme habituelle :
\begin{equation}
\left. {\partial \mathbf{v_r} \over \partial t} \right|_\mathbf{r}+ \left(\mathbf{v_r}.\nabla_\mathbf{r}\right) \mathbf{v_r}=-\nabla_\mathbf{r}\phi - \frac{1}{\rho} \nabla_\mathbf{r}p 
\end{equation}
Dans l'espace comobile, elle se transforme en :
\begin{equation}
\left. {\partial (\dot{a}\mathbf{x}+a\mathbf{v_x}) \over \partial t} \right|_\mathbf{x} - H \mathbf{x}.\nabla_\mathbf{x}(\dot{a}\mathbf{x}+a\mathbf{v_x}) + (\dot{a}\mathbf{x}+a\mathbf{v_x}). {1 \over a}\nabla_\mathbf{x} (\dot{a}\mathbf{x}+a\mathbf{v_x})= -{1 \over a^2} \nabla_\mathbf{x}\phi_\mathbf{x} - \frac{1}{a \rho} \nabla_\mathbf{x}p .
\end{equation}
En veillant à ce que  :
$$\left. {\partial (\dot{a}\mathbf{x}+a\mathbf{v_x}) \over \partial t} \right|_\mathbf{x}=\ddot{a}\mathbf{x}+\dot{a}\mathbf{v_x}+a \left.{\partial \mathbf{v_x} \over \partial t}\right|_\mathbf{x}$$
l'équation d'Euler en coordonnées comobiles se réduit à :
\begin{equation}\label{Euler_comv}
\left.{\partial \mathbf{v_x} \over \partial t} \right|_\mathbf{x} + 2 H \mathbf{v_x}+\mathbf{v_x}.\nabla_\mathbf{x}\mathbf{v_x}= -{1 \over a^3}  \nabla_\mathbf{x}\phi_\mathbf{x} - \frac{1}{a^2 \rho} \nabla_\mathbf{x}p  - {\ddot{a} \over a} \mathbf{x} 
\end{equation}

Nous pouvons voir deux termes supplémentaires par rapport à la version de l'équation d'Euler écrite en coordonnées physiques. Le terme supplémentaire $2 H \mathbf{v_x}$ est une force de traînée créé par l'expansion sur les vitesses comobiles. 

::: {note}
Ce terme de traînée existe également, avec un coefficient numérique différent, si nous utilisons la vitesse particulière comme variable. On peut vérifier qu'en l'absence de gravité, dans le régime linéaire, $\mathbf{v_x}\propto a^{-2}$. 
:::

Le second  nouveau terme paraît étrange. En effet, il semble annuler la force newtonienne créée à $\mathbf{x}$ par un fond de densité homogène non nul. On pourrait arguer que cette force devrait être nulle, pour des raisons de symétrie. Cependant, en appliquant le théorème de Gauss, on peut trouver une force non nulle dirigée vers l'origine des coordonnées (où qu'elle soit choisie !). Le fait est que l'équation de Poisson se comporte mal (et ne doit pas être utilisée) pour un champ source dont la norme $L^2$ n'est pas finie. 
Mais bien sûr, cela implique des échelles au-delà de $R_H$ où nous ne nous attendons pas à ce que notre théorie tienne la route. En ce qui concerne les perturbations de la densité, nous soustrairons la valeur moyenne non nulle et nous nous débarrasserons ainsi de cette incohérence à grande échelle.  


### Equation de Poisson

Dans un univers sans constante cosmologique, de la relativité générale on en déduit l'équation de Poisson habituelle dans la limite des champs faibles [](#eq:poisson) :
\begin{equation}
\nabla^2_\mathbf{r} \phi = 4 \pi G_N \rho
\end{equation}
où $\phi$ est le potentiel gravitationnel. Compte tenu de la relation entre le potentiel et la force newtonienne, le potentiel comobile est naturellement défini comme $\phi_\mathbf{x}=\phi a$, et l'équation de Poisson est également inchangée dans l'espace comobile :
\begin{equation}
\nabla^2_\mathbf{x} \phi_\mathbf{x} = 4 \pi G_N \rho_\mathbf{x}
\label{Poisson_comov}
\end{equation}

:::{note} Influence de la constante cosmologique

Si l'on considère une constante cosmologique, dans la limite du champ faible, la gravitation est régie par l'équation de Poisson modifiée 
$$ \nabla^2_\mathbf{r} \phi = 4 \pi G_N \rho -c^2 \Lambda$$
qui se transforme en 
$$ \nabla^2_\mathbf{x} \phi_\mathbf{x} = 4 \pi G_N \rho_\mathbf{x} -c^2 \Lambda a^3$$
:::


Théorie newtonienne des perturbations 
-----------------------------------------

### Solution d'ordre zéro

L'équation de continuité dans l'espace comobile [](#Cont_comov)
admet la solution homogène suivante :
\begin{equation}
\rho_{\mathbf{x},0}= cst, \qquad \mathbf{v}_{\mathbf{x},0}=0
\end{equation}
L'intégration de l'équation de Poisson en coordonnées sphériques donne :
$$ \phi_{\mathbf{x},0} = \frac{4}{6} \pi G_N \rho_{\mathbf{x},0} $$
$$\nabla \phi_{\mathbf{x},0} = {4 \pi G_N \rho_{\mathbf{x},0} \over 3 } \mathbf{x}$$
en accord avec l'équation d'Euler si on utilise les équations de Friedmann [](#eq:ddota) :
$$\frac{\ddot a}{a} = -\frac{4 \pi G_N}{3}(\epsilon + 3p)$$
avec $\Lambda=0$ ici.

Dans l'espace comobile, une solution homogène des équations de continuité, de Poisson et d'Euler ([](#Cont_comov), [](#Poisson_comov) et [](#Euler_comv)) est :
\begin{equation}
\rho_{\mathbf{x},0}= cst, \qquad \mathbf{v}_{\mathbf{x},0}=0, \qquad \nabla \phi_{\mathbf{x},0} = - a^3 {\ddot{a} \over a} \mathbf{x}, \qquad p_{\mathbf{x},0} = cst, 
\end{equation}

### Solution linéaire d'ordre un

Considérons de petites perturbations autour de la solution d'ordre zéro :
\begin{equation}
\rho_\mathbf{x}=\rho_0(1+\delta) \qquad \mathbf{v}_\mathbf{x}=\mathbf{v}_0+\delta\mathbf{v} \qquad \phi_\mathbf{x}=\phi_0 + \delta \phi_\mathbf{x}, \qquad p = p_0 + \delta p
\end{equation}
La quantité $\delta$ est appelée contraste de densité et est très utilisée dans la théorie de la formation des structures. Notons qu'elle a la même valeur dans l'espace physique et dans l'espace comobile. En injectant ces expressions dans les équations de continuité, de Poisson et d'Euler, la solution d'ordre zéro s'annule (comme prévu) et en supprimant les termes d'ordre 2, nous obtenons l'ensemble d'équations linéarisé :
\begin{align}
\nabla_\mathbf{x}^2 \delta \phi_\mathbf{x} &= 4 \pi G_N \rho_0 \delta \\
{\partial \delta \over \partial t} + \nabla_\mathbf{x}. \delta\mathbf{v}&= 0\\
{\partial \delta\mathbf{v} \over \partial t} + 2 H \delta\mathbf{v} &=  - {1 \over a^3} \nabla_\mathbf{x} \delta \phi_\mathbf{x} - \frac{1}{a^2 \rho} \nabla_\mathbf{x} \delta p
\end{align}

En prenant la divergence de l'équation d'Euler linéarisée et en réinjectant l'équation de Poisson et les équations de continuité, nous obtenons finalement :
$$\ddot{\delta}+ 2 H \dot{\delta}  - \frac{1}{a^2 \rho} \triangle_\mathbf{x} \delta p = 4 \pi G_N {\rho_0 \over a^3} \delta$$
On introduit la vitesse du son $c_s$ dans le milieu pour des compressions adiabatiques :
$$c_s^2 = \frac{1}{\rho \chi_S} =  \left.\frac{\partial p}{\partial \rho}\right\vert_{adiabatique} \approx \frac{\delta p}{\delta \rho} = w c^2 $$
avec $w = p/\epsilon$ le paramètre d'équation d'état du milieu de propagation. Alors on obtient l'équation de croissance des perturbations dans l'espace comobile :
\begin{equation}\label{fluct_growth}
\boxed{ \ddot{\delta}+ 2 H \dot{\delta}  - \frac{c_s^2}{a^2} \triangle_\mathbf{x} \delta = 4 \pi G_N \rho \delta  }
\end{equation}



### Le champ de perturbation de la densité initiale

#### Champs aléatoires gaussiens
#### Champs aléatoires

Un champ aléatoire 3D est un ensemble de variables aléatoires $Y(\mathbf{x})$, une pour chaque emplacement (ou cube infinitésimal de volume $dx^3$) dans l'espace 3D. Un tel champ est caractérisé par une collection de fonctions de distribution de probabilités conjointes :

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
\item La transformée de Fourier du champ aléatoire gaussien est un champ aléatoire gaussien. Ainsi, les parties réelle et imaginaire de $\hat{\delta}(\mathbf{k})$ (la transformée de Fourier de $\delta(\mathbf{x})$) sont des variables aléatoires avec des fonctions de distribution de probabilité gaussiennes.
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
\hat{f}(\mathbf{k})= \int f(\mathbf{x}) e^{-i \mathbf{k.x}} d^3x
\end{equation} 
\begin{equation}
f(\mathbf{x})= {1 \over (2 \pi)^3}\int \hat{f}(\mathbf{k}) e^{i \mathbf{k.x}} d^3k
\end{equation} 
La fonction de corrélation en deux points de la surdensité (ou de toute autre quantité) est définie comme suit :

\begin{equation}
\xi(\mathbf{x_1},\mathbf{x_2})=\langle \delta(\mathbf{x_1}) \delta(\mathbf{x_2})\rangle
\end{equation}
où $\langle\dots \rangle$ désigne la moyenne sur de nombreuses réalisations du champ aléatoire, également appelée "moyenne d'ensemble". Puisque $\xi$ est complètement déterminé par les $P_1$ et $P_2$ sous-jacents, qui sont invariants par translation et rotation en raison du principe cosmologique, $\xi$ est une fonction de $r=|\mathbf{x_2}-\mathbf{x_1}|$ seulement.
Pour montrer la relation entre $\xi$ et le spectre de puissance, insérons la transformée de Fourier de $\delta_1$. 
transformée de Fourier de $\delta$ dans l'expression simplifiée $\xi(r)$.
\begin{align}
\xi(r)&=&\langle \delta(\mathbf{x}) \delta(\mathbf{x}+\mathbf{r}) \rangle \\
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



#### BACKUP

