Distances en cosmologie
==========

Distance propre
---------------

La distance propre est la distance que l'on pourrait mesurer
effectivement à un instant $t$ entre deux objets situés en $r_1$ et
$r_2$. Elle est donc homogène à une longueur. Sans perdre en généralité,
on peut choisir $r_1=0$ et $r_2=r$. La distance propre est alors définie
naturellement par:
$$d(t) \equiv \int_{0}^{r} \sqrt{-g_{rr}}dr' = \int_{0}^{r}\frac{a(t) dr'}{\sqrt{1-kr'^2}} = a(t)\chi(t) = a(t)\left\lbrace
\begin{array}{cl}
    \arcsin r_E & \text{ si } k=+1 \\
    r_E & \text{ si } k=0 \\
    \text{arcsh } r_E & \text{ si } k=-1 
\end{array}
\right. ,$$ et s'exprime bien en unités de longueur. A la date $t_0$
aujourd'hui, cette distance s'exprime simplement en fonction du décalage
spectral: $$d(z)=a_0\chi(z)=\int_0^z\frac{c dz}{H(z)}.$$ La notion de
distance propre est illustrée [](#fig:distances).

```{figure} ../images/distances3.png
:name: fig:distances
:align: center
:width: 100%

Distance propre entre la Terre et la Galaxie d'Andromède. (a)
Aujourd'hui, la distance mesurée entre la Terre et la Galaxie
d'Andromède est de $a_0 r = 2.5 \times 10^6$ années-lumière dans un
espace plat. (b) A une autre date $t$, cette distance évolue et vaut
$a(t) r$. (c) Distance propre dans un espace
sphérique.
```

Distance de luminosité 
-----------------------

Considérons une source située en $r_E$, émettant à l'instant $t_E$ $n_E$
photons de fréquence moyenne $\nu_E$ (se reporter encore à la
[](#fig:distances_croquis)). Sa luminosité est:
$$L_E = \frac{n_E h\nu_E}{dt_E}.$$ 
Alors le flux surfacique reçu par un
observateur est: 
$$\Phi_0 = \frac{n_0 h \nu_0}{dt_0 dS}.$$ 
La surface sur laquelle se répartit, à l'instant $t_0$, le flux émis est:
$$S = \int_0^{2\pi} \int_0^\pi \sqrt{-g} d\theta d\phi = \int_0^{2\pi} \int_0^\pi a^2(t_0)r^2(t_0)\sin^2\theta d\theta d\phi = 4 \pi a^2_0 r^2_E.$$
avec $r(t_0)=r_E$. Or à partir de l'équation
[](#eq:redshift2), on a
$\nu_E = \nu_0 a(t_0)/a(t_E) = \nu_0 (1+z)$ et $dt_E = dt_0/(1+z)$. Le
nombre de photons émis $n_E$ intercepté par la surface collectrice de
taille $dS$ est $n_0 = n_E dS/(4 \pi a^2_0 r^2_E)$, d'où le flux reçu:
$$\Phi_0 = \frac{n_0 h \nu_0}{dt_0 dS} =  \frac{h \nu_0 n_E}{dt_0 4 \pi a^2_0 r^2_E} = \frac{L_E}{4 \pi a^2_0 r^2_E(1+z)^2}.$$
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


