---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---


Astrophysical emissions
=============================================

Reminders of Special Relativity
--------------------------------

The underlying principle of the theory of Special Relativity is that the laws of physics must be invariant to changes in the space-time coordinate system. 
In the special case of Maxwell's theory of electromagnetism, a velocity appears that is invariant to changes in the
coordinate system. This speed is identified with the celerity of light, the maximum speed that can be reached by a particle of zero mass. If 
electromagnetic theory had not been written in 1905, one argument might also have been that there must be a maximum velocity in the Universe if we believe that no 
transport of information can be instantaneous. At that point, the pivotal speed of the theory of Special Relativity would have been the speed of the interaction
which propagates the fastest. In our Universe, this would be the electromagnetic interaction {cite:p}`landau1989theory`.

:::{note} Covariant derivative

The affine connection $\Gamma^\nu_{\ \mu\rho}$ is also involved in the definition of the covariant derivative.
$V^\nu{}_{;\mu}$ of a vector $V^\nu$ with respect to the $x'^\mu$ coordinate:
$$
V^\nu{}_{;\mu} \equiv \partial_\mu V^\nu + \Gamma^\nu_{\ \mu\rho}V^\rho
$$
:::


```{figure} ../images/effet_eintein.svg
:name: fig:effet_einstein
:align: center
:width: 90%

Illustration of the Einstein effect. A photon falling into a gravitational well
gains energy, so its frequency increases. equivalently
equivalently, we can say that clocks in a gravitational field
delay compared to identical clocks outside. The
GPS receivers have to take this effect into account to deduce their position
position relative to the satellites.
```

:::{important}

The Bianchi identity and the Einstein equation
[](#eq:einstein1) imposes the conservation of energy, therefore
directly from geometric properties:
$$\label{eq:conservation_energie_tenseur}
T^{\mu\nu}_{\;\;\;;\mu}=0
$$
:::




Using the Bianchi identity, we can also see that Einstein's equation can be
be defined to within one constant[^b] while retaining the conservation of energy. This constant is 
called the cosmological constant. Here's Einstein's equation in its definitive form {cite:p}`Einstein1917` :
$$\label{eq:einstein2}
\fbox{$ G_{\mu\nu}-\Lambda g_{\mu\nu} = -\frac{8\pi G_N}{c^4} T_{\mu\nu} $}
$$

[^b]: Because we also have $g^{\mu\nu}_{\;\;;\mu}=0$.


:::{exercise} Modèle de Sitter
:label: exo:desitter

Peu après Einstein, de Sitter a publié un autre type de modèle cosmologique. Il a proposé un univers plat avec seulement 
une constante cosmologique non nulle et aucune matière à l'intérieur (ou une quantité négligeable de matière). 
Montrer qu'un tel univers croît de manière exponentielle avec le temps. 
C'est l'univers de de Sitter. Trouvez également un système de coordonnées dans lequel il est statique. 


:::

:::{solution} exo:desitter
:class: dropdown

Dans un univers plat $k=0$ et la première équation de Friedmann donne dans le modèle de Sitter :
\begin{equation}
\frac{\dot{a}^2}{a^2} = \frac{c^2 \Lambda}{3} \Leftrightarrow -\sqrt{\frac{3}{c^2 \Lambda}}\frac{\dd a }{\dd t}+a=0
\end{equation}
La solution de cette équation différentielle est
\begin{equation}
a(t) = a_0 e^{\sqrt{c^2 \Lambda/3}t}
\end{equation}
L'univers de de Sitter croît exponentiellement avec le temps. 

:::
