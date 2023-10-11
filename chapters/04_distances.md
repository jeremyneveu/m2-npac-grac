---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---

Distances en cosmologie
==========

Distance comobile
-----------------

Soit un objet situé à la coordonnée comobile $\sigma$ et un observateur situé en 0.
La lumière voyage en suivant une géodésique, donc dans la métrique FLRW on a $\dd \theta=\dd \phi=0$ et :
\begin{equation}\label{eq:ds2_lumiere}
\dd \tau^2=0=c^2 \dd t^2-\frac{a^2(t)}{1-k\sigma^2}\dd\sigma^2.
 \end{equation} 
Donc
$$\dd\sigma/\sqrt{1-k\sigma^2} = - c \dd t/a(t)$$ 
avec le photon voyageant le long de la direction $\dd \sigma<0$ pour $\dd t > 0$. La distance comobie s'écrit :
\begin{equation}
\chi(r_E) =  \int_0^{r_E}\frac{\dd\sigma}{\sqrt{1-k\sigma^2}} = \int_{t_0}^{t_E} -\frac{c\dd t'}{a(t')}= \int_{t_E}^{t_0} \frac{c\dd t'}{a(t')} = \chi(t_E)
\end{equation}
Exprimons cette distance en fonction du redshift $z$, qui, on le rappelle, est une observable expérimentale. Les intégrales
peuvent se transformer entre les variables $t$, $a$ grâce à la définition du taux d'expansion $H(t)$, et entre les variables $a$ et $z$ grâce à la définition du redshift :
\begin{equation}
H= \frac{1}{a}\frac{\dd a}{\dd t} \Rightarrow \dd t = \frac{1}{aH} \dd a
\end{equation}
\begin{equation}
a = \frac{a_0}{1+z} \Rightarrow \dd a = -a_0 \frac{\dd z}{(1+z)^2}\Rightarrow \frac{\dd a}{a} = -\frac{\dd z}{1+z}
\end{equation}
D'où la distance comobile en terme de temps $t$, facteur d'échelle $a$ et redshift $z$ :
\begin{align}
\chi(\sigma_E) & = \chi(t_E) = \int_{t_E}^{t_0} \frac{c\dd t'}{a(t')} = \int_{a_E}^{a_0} \frac{c\dd a}{a^2 H(a)} \\
& = \int_z^0 \frac{1+z}{a_0}\frac{-\dd z}{(1+z)H(z)} = \frac{1}{a_0}\int_0^z\frac{c\dd z}{H(z)} = \chi(z)
\end{align}

En général, $a_0$ n'est pas directement mesurable, mais les paramètres cosmologiques et $H_0$ peuvent être déterminés. 
Il est donc utile de savoir comment se débarrasser de $a_0$ dans le cas général. A $t=0$, on peut écrire :
\begin{equation}
\Omega_k^0 = - \frac{kc^2}{H_0^2 a_0^2} \Rightarrow a_0 = \left\lbrace\begin{array}{l}
    \displaystyle{\frac{c}{H_0\sqrt{-\Omega_k^0}}}  \text{ if } k=+1 \\
    \text{indéterminé mais usuellement valant } 1 \text{ if } k=0 \\
    \displaystyle{\frac{c}{H_0\sqrt{\Omega_k^0}}}  \text{ if } k=-1 
\end{array}
\right.
\end{equation}
Dans cette paramétrisation, la valeur de $a_0$ est égale au rayon de l'univers dans les cas courbes (avec $a$ ayant la dimension d'une longueur, $\sigma$ non dimensionné). Dans ce cas :
\begin{equation}
\displaystyle{\chi(z) = \left\lbrace\begin{array}{cl}
    \displaystyle{H_0\sqrt{-\Omega_k^0}\int_0^z\frac{dz}{H(z)}}  & \text{ if } k=+1 \\
    \displaystyle{\frac{1}{a_0}\int_0^z\frac{cdz}{H(z)}} & \text{ if } k=0 \\
    \displaystyle{H_0\sqrt{\Omega_k^0}\int_0^z\frac{dz}{H(z)} } & \text{ if } k=-1 
\end{array}
\right.}
\end{equation}

Distance propre
---------------

La distance propre est la distance que l'on pourrait mesurer
effectivement à un instant $t$ entre deux objets. Sans perdre en généralité,
on peut choisir un objet situé à la coordonné comobile $\sigma$ et un osbervateur comobile en 0.
La distance propre est alors définie naturellement selon une ligne $\dd \theta = \dd \phi=0$ par :
$$d_p(t) \equiv \int_{0}^{\sigma} \sqrt{-g_{\sigma\sigma}}\dd \sigma' = \int_{0}^{\sigma}\frac{a(t) \dd \sigma'}{\sqrt{1-k\sigma'^2}} = a(t)\chi(t) = a(t)\left\lbrace
\begin{array}{cl}
    \arcsin \sigma_E & \text{ si } k=+1 \\
    \sigma_E & \text{ si } k=0 \\
    \text{arcsh } \sigma_E & \text{ si } k=-1 
\end{array}
\right. ,$$ 
et s'exprime bien en unités de longueur. Cette distance s'exprime simplement en fonction du décalage
spectral :
$$d_p(z)=a_0\chi(z)=\int_0^z\frac{c \dd z}{H(z)}.$$ 
pour les trois cas de courbure. La notion de distance propre est illustrée [](#fig:distances).

```{figure} ../images/distances.svg
:name: fig:distances
:align: center
:width: 100%

Distance propre entre la Terre et la Galaxie d'Andromède. (a)
Aujourd'hui, la distance mesurée entre la Terre et la Galaxie
d'Andromède est de $a_0 \sigma = 2.5 \times 10^6$ années-lumière dans un
espace plat. (b) A une autre date $t$, cette distance évolue et vaut
$a(t) \sigma$. (c) Distance propre dans un espace
sphérique.
```

Distance de luminosité 
-----------------------

Considérons une source située en $r_E$, émettant à l'instant $t_E$ $n_E$
photons de fréquence moyenne $\nu_E$ (se reporter encore à la
[](#fig:distances_croquis)). Sa luminosité est :
$$L_E = \frac{n_E h\nu_E}{dt_E}.$$ 
Alors le flux surfacique reçu par un observateur est : 
$$\Phi_0 = \frac{n_0 h \nu_0}{dt_0 dS}.$$ 
La surface sur laquelle se répartit, à l'instant $t_0$, le flux émis est:
$$S = \int_0^{2\pi} \int_0^\pi \sqrt{-g} d\theta d\phi = \int_0^{2\pi} \int_0^\pi a^2(t_0)r^2(t_0)\sin^2\theta \dd\theta d\phi = 4 \pi a^2_0 r^2_E.$$
avec $\sigma(t_0)=\sigma_E$. Or à partir de l'équation
[](#eq:redshift2), on a
$\nu_E = \nu_0 a(t_0)/a(t_E) = \nu_0 (1+z)$ et $\dd t_E = \dd t_0/(1+z)$. Le
nombre de photons émis $n_E$ intercepté par la surface collectrice de
taille $\dd S$ est 
$$n_0 = n_E \dd S/(4 \pi a^2_0 \sigma^2_E),$$
d'où le flux reçu :
$$\Phi_0 = \frac{n_0 h \nu_0}{\dd t_0 dS} =  \frac{h \nu_0 n_E}{\dd t_0 4 \pi a^2_0 \sigma^2_E} = \frac{L_E}{4 \pi a^2_0 \sigma^2_E(1+z)^2}.$$
Dans un espace statique et plat, la luminosité apparente d'une source au
repos à distance $d_L$ serait $L_E/4\pi d_L^2$. On peut donc définir la
distance de luminosité d'une source $d_L(z)$ par:
$$\Phi_0 = \frac{L_E}{4 \pi d_L^2(z)} \Rightarrow d_L(z) = a_0 r_E (1+z) = a_0 (1+z)\left\lbrace
\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \text{sh } \chi(z) & \text{ si } k=-1 
\end{array}
\right. .$$

Distances angulaires
------------------

Dernière distance importante en cosmologie, la distance angulaire d'un
objet $D_A(z)$. Soit un objet de taille transverse $D$ situé en
$r=r_E,t=t_E$ et observé en $r=0,t=t_0$. Dans l'espace comobile, il
serait vu sous un angle $\delta \approx D /r_E$ (avec $\delta\ll 1$). On
définit la distance angulaire comobile ou distance transverse comobile
simplement par:
$$d_A(z) = \frac{D}{\delta} = r_E = \left\lbrace\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \text{sh } \chi(z) & \text{ si } k=-1 
\end{array}
\right. .$$ Dans un espace non statique, son diamètre apparent à $t_0$
est $D'=D a_0/a_E$ et l'objet est à une distance $a_0 r_E$: il est donc
vu sous un angle $\delta' = D'/a_0 r_E$ . La distance angulaire $D_A(z)$
est la distance sous laquelle son diamètre apparent serait à nouveau $D$
et vu sous le même angle $\delta'$:
$$\delta' = \frac{D}{D_A(z)} = \frac{D'}{a_0 r_E}$$
$$\Rightarrow D_A(z)=a(t_E) r_E=\frac{a_0 r_E}{1+z} = \frac{a_0}{1+z}d_A(z)=\frac{d_L(z)}{(1+z)^2}= \frac{a_0}{1+z} \left\lbrace\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \text{sh } \chi(z) & \text{ si } k=-1 
\end{array}
\right. .$$


