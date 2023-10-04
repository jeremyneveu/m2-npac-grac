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
$$  \sqrt{\frac{a}{a_0}} \frac{\dd a}{a_0} = H_0  \dd t \Rightarrow \frac{a}{a_0}^{3/2} = \frac{3}{2}H_0  t $$
$$\label{eq:a_matiere_only}
\Rightarrow \frac{a(t)}{a_0} = \left( \frac{3}{2}H_0  t\right)^{2/3}$$
avec au début de l'Univers $t=0$ et $a=0$. On a obtenu ainsi une relation direct entre le facteur d'échelle et l'âge de l'Univers.

### Univers plat, radiation seule

Par un raisonnement similaire, on montre que pour un Univers plat dominé par le rayonnement on a une évolution différente du facteur d'échelle :
$$\label{eq:a_rad_only}
\Rightarrow \frac{a(t)}{a_0} = \left( \frac{1}{2}H_0  t\right)^{1/2}$$

### Univers vide

Supposons que l'Univers est vide, ou du moins avec une densité d'énergie totale très faible devant la densité critique. 
Alors l'Univers doit être courbé puisque dans ce cas :
$$\Omega_k^0 = 1 - \Omega_m^0  - \Omega_r^0  - \Omega_\Lambda^0 \approx 1$$
Cet Univers est donc hyperbolique[^ksign]. La première équation de Friedmann s'écrit :
$$
\frac{\dot{a}^2}{a^2} + \frac{c^2 k}{a^2} \right) = 0 
$$
puis :
$$ 
\dot a = \sqrt{-c^2 k} = \sqrt{c^2 H_0^2 \Omega_k^0} = H_0 c
$$
L'intégration donne donc un Univers en expansion à vitesse constante :
$$\label{eq:a_empty}
a(t) = H_0 c t$$
où l'échelle aujourd'hui $a_0$ n'apparaît pas. 

:::{important}

La constante de Hubble $H_0$ apparaît dans les trois modèles d'Univers précédents. Ce n'est pas une prédiction des modèles cosmologiques
mais bien une mesure externe qui permet de calculer l'histoire de l'Univers en fonction de son taux d'expansion aujourd'hui. 
:::



Modèles historiques
-------------------



Analogie mécanique
-------------------






Age de l'Universe
------------------




Evolution des paramètres cosmologiques
------------------------------------



![](#omegas) 


This will embed the output of a notebook cell

:::{note} Test
![](#om-slider)

:::


[^^sign]: Le signe de $k$ est l'inverse du signe de $\Omega_k^0$.


