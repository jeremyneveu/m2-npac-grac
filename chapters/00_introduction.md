---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---


A brief introduction to General Relativity
=============================================

Reminders of Special Relativity
--------------------------------

The underlying principle of the theory of Special Relativity is that the laws of physics must be invariant to changes in the space-time coordinate system. 
In the special case of Maxwell's theory of electromagnetism, a velocity appears that is invariant to changes in the
coordinate system. This speed is identified with the celerity of light, the maximum speed that can be reached by a particle of zero mass. If 
electromagnetic theory had not been written in 1905, one argument might also have been that there must be a maximum velocity in the Universe if we believe that no 
transport of information can be instantaneous. At that point, the pivotal speed of the theory of Special Relativity would have been the speed of the interaction
which propagates the fastest. In our Universe, this would be the electromagnetic interaction {cite:p}`landau1989theory`.

Consider a coordinate system $x^\alpha$, where coordinate $\alpha=0$ corresponds to time $ct$ and coordinates $\alpha=1,2,3$ correspond to Cartesian coordinates $x^\alpha$.
In this course, we'll use Greek letters for components from 0 to 3 and Latin letters for spatial components from 1 to 3. To switch to another coordinate system $x'^\alpha$, we introduce the Lorentz transformation 
Lorentz transformation $\Lambda^\alpha_\beta$ defined by :
```{math}
:label: eq:boost

x'^{\alpha} = \Lambda^\alpha_{\;\beta} x^\alpha + a^\alpha,
```
where $a^\alpha$ is a simple temporal and spatial translation. We define the Minkowski metric:
```{math}
:label: eq:minkowski

\eta_{\alpha\beta} = \begin{pmatrix}
-1 & 0& 0& 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix}

```
so that in Cartesian coordinates we can define the space-time interval between two nearby space-time coordinates as follows:
$$ \dd s^2 = - c^2 \dd t^2 + \dd \vec x^2 = \eta_{\alpha}\dd x^\alpha \dd x^\beta $$
To ensure that $c$ is invariant to a change of coordinate system, the Lorentz transformation must conserve the space-time interval [^consc]:
$$
\dd s'^2 =  \eta_{\alpha\beta}\dd x'^\alpha \dd x'^\beta = \eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta}  \dd x'^\gamma \dd x'^\delta = \eta_{\gamma\delta} \dd x^\gamma \dd x^\beta = \dd s^2
$$
$$\label{eq:dscons}
\Rightarrow \eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta} =  \eta_{\gamma\delta}
$$

From the symmetry [](#eq:dscons) it can be shown that the Lorentz transformation between two reference frames, one of which is moving at the speed $\vec v = v \vec e_{1}$ with respect to the other, must be written :
```{math}
:label: eq:lorentz

\Lambda^{\alpha}_{\;\beta} = \begin{pmatrix}
\gamma & -\beta\gamma & 0& 0 \\
\beta\gamma & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix},\quad \beta = \frac{v}{c},\quad \gamma = \frac{1}{\sqrt{1 - \beta^2}}

```
If we include space rotations, with one frame of reference moving at a constant $\vec v$ velocity relative to another frame of reference,
the $\Lambda^\alpha_{\;\beta}$ tensor is written :
```{math}
:label: eq:lorentz2

\Lambda^0_{\;0} = \gamma,\quad \Lambda^i_{\;0} = \gamma v_i / c,\quad \Lambda^0_{\;j} = \gamma v_j / c,\quad \Lambda^i_{\;j} = \delta_{ij} + (\gamma - 1)  \frac{v_i v_j}{v^2}
```

From Newton to General Relativity
----------------------------------

General Relativity is the theory of gravitation that is the basis of modern
cosmology. It gives a geometrical explanation to the gravitational force
introduced by Newton three centuries earlier. In
this theory, a fall is no longer due to a force vector
unfortunately directed towards the ground, but to the deformation of space-time
of space-time caused by the Earth. Formulated in this way, General Relativity
seems complicated for very little. But the general principles
theory and the wealth of its implications (including Newtonian theory) make it the leading theory for describing
gravitation. In this section, we will introduce step by step
General Relativity concepts such as the covariant derivative
and the Riemann tensor, culminating in Einstein's equation of General Relativity, the basis of modern cosmology.
This introduction is largely inspired by {cite:t}`Weinberg1972` and
{cite:t}`Gourgoulhon2013`. 

### The Equivalence Principle

In Newton's fundamental principle of dynamics, why is it that
is the mass involved in the inertia term strictly the same as that involved in gravitation?
Newtonian gravitation? This
disturbing coincidence sets gravitation apart from other interactions
interactions, and suggests that gravitation is not a property of the bodies
but of the space in which they move. Let's consider a
point mass of mass $m$ subject to a uniform and constant external
and no other force. Then the
fundamental principle of dynamics applied to this object in a galilean
allows us to predict its position $x$ at time $t$ by means of a differential equation to be integrated:
$$m\frac{\dd^2\vec x}{\dd t^2} = m\vec g$$ 
Let's place ourselves in the
(non-galilean) frame of reference by the following coordinate transformation:
$$\vec x' = \vec x - \frac{1}{2}\vec g t^2, \qquad t'=t$$ 
Then, in this frame of reference, the gravitational force is "absorbed" by the inertial term
inertial term:
$$m\frac{\dd^2\vec x}{\dd t^2} = m\vec g \Leftrightarrow m\frac{\dd ^2\vec x'}{\dd t'^2} = 0.$$
The laws of physics therefore appear identical for an observer
observer bound to a galilean reference frame, considering that the object is subject to a gravitational force.
and for an observer linked to a uniformly accelerated frame of reference
accelerated frame of reference, assuming the object is not subject to
gravitational force. The force of gravity felt by a point mass
is therefore (locally) equivalent to the choice of a uniformly accelerated frame of reference
accelerated relative to a Galilean reference frame. However, the two
reference frames are not equivalent through a transformation from a
Galilean reference frame. The Principle of Equivalence formulated by Einstein
takes note of this observation, and extends it to gravitational fields that
vary only slightly in time and space. It states that *at every
point of space-time in an arbitrary gravitational field, it is possible to
possible to choose a local system of inertial coordinates such that,
in a sufficiently small region around the point in question, all laws of nature
laws of nature take on the same form as in a non-accelerated and
Cartesian coordinate system* {cite:p}`Weinberg1972`.
This principle has been verified experimentally to a very high degree of accuracy,
by the *Lunar Laser Ranging* {cite:p}`Williams2004`.

### Equations of motion

Let's apply the Equivalence Principle to a massive object in free fall. For this
object, there exists a *particular* local coordinate system
$x^\mu$ such that the equation of motion can be written in the same way
as if the frame of reference were unaccelerated and gravitation-free:
\begin{equation}\label{eq:eqm1}
\frac{\dd^2 x^\mu}{\dd\tau^2}=0,
\end{equation}
with $\dd\tau$ the proper time[^1] :
$$\label{eq:proper-time}
\dd\tau^2 \equiv -\eta_{\mu\nu} \dd x^\mu \dd x^\nu.
$$ 
According to the
Equivalence Principle, this equation is also valid within a certain
neighborhood of the object in question. So there's another, more general
coordinate system in which to rewrite this equation.
Let's find the form it would take for these $x'^\mu$ coordinates:
$$0=\frac{\dd^2 x^\mu}{\dd\tau^2}=\frac{d}{\dd\tau}\left(\frac{\partial x^\mu}{\partial x'^\nu} \frac{\dd x'^\nu}{\dd\tau}\right) = \frac{\partial x^\mu}{\partial x'^\nu} \frac{\dd^2x'^\nu}{\dd\tau^2} + \frac{\partial^2 x^\mu}{\partial x'^\nu \partial x'^\rho}\frac{\dd x'^\nu}{\dd\tau}\frac{\dd x'^\rho}{\dd\tau}.$$
After multiplying by $\partial x'^\nu/\partial x^\mu$, we obtain the new
new equation of motion in the $x'^\mu$ coordinate system:
$$\label{eq:eqm2} 
\frac{\dd^2x'^\nu}{\dd\tau^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x'^\mu}{\dd\tau}\frac{\dd x'^\rho}{\dd\tau}=0,
$$ 
where $\Gamma^\nu_{\mu\rho}$ is the affine connection defined by:
$$\Gamma^\nu_{\ \mu\rho} \equiv \frac{\partial x'^\nu}{\partial x^\lambda}\frac{\partial^2 x^\lambda}{\partial x'^\mu \partial x'^\rho}.$$
The proper time is rewritten: 
$$\dd\tau^2=-\eta_{\mu\nu} \dd x^\mu \dd x^\nu = -g_{\mu\nu} \dd x'^\mu \dd x'^\nu$$
which defines the metric tensor $g_{\mu\nu}$ :
$$g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial x^\alpha}{\partial x'^\mu} \frac{\partial x^\beta}{\partial x'^\nu}$$
$g_{\mu\nu}$ describes the geometry of space-time in the new
coordinate system $x'^\mu$ and replaces the Cartesian metric
$\eta_{\mu\nu}$. The inverse metric tensor is defined by:
$$g^{\mu\nu} = \eta^{\alpha\beta} \frac{\partial x'^\mu}{\partial x^\alpha} \frac{\partial x'^\nu}{\partial x^\beta}.$$
Indeed, by definition we have: 
$$\begin{aligned}
g^{\nu\rho}g_{\mu\nu} & = \eta^{\alpha\beta} \frac{\partial x'^\nu}{\partial x^\alpha} \frac{\partial x'^\rho }{\partial x^\beta} \eta_{\gamma\delta} \frac{\partial x^\gamma}{\partial x'^\mu} \frac{\partial x^\delta}{\partial x'^\nu} \\
& = \delta^\delta_\alpha \eta^{\alpha\beta} \frac{\partial x'^\rho }{\partial x^\beta} \eta_{\gamma\delta} \frac{\partial x^\gamma}{\partial x'^\mu} \text{ with } \frac{\partial x'^\nu}{\partial x^\alpha}\frac{\partial x^\delta}{\partial x'^\nu} = \delta^\delta_\alpha \\
& = \frac{\partial x'^\rho}{\partial x^\beta}\frac{\partial x^\beta}{\partial x'^\mu} = \delta^\rho_\mu,
\end{aligned}$$
where $\delta^\rho_\mu$ is the Kronecker symbol ($\delta^\rho_\mu=1$ if $\rho=\mu$, 0 otherwise).
We could then show that $\Gamma^\nu_{\ \mu\rho}$ can only be written using a single coordinate system and the metric tensor.
and the metric tensor: 
$$\label{eq:connexion}
\Gamma^\nu_{\mu\rho} = \frac{1}{2}g^{\lambda\nu}\left( \frac{\partial g_{\lambda\rho}}{\partial x'^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x'^\rho} - \frac{\partial g_{\mu\rho}}{\partial x'^\lambda} \right)
$$

For a massless particle, such as a photon or neutrino, the proper time defined by equation [](#eq:proper-time) cancels out. A 
instead of $\tau$ we can then use the coordinate $s = x^0$ to parameterize the trajectory of the curve, and by a similar 
equation of motion:
$$\label{eq:eqm3}
\frac{\dd^2x'^\nu}{\dd s^2} + \Gamma^\nu_{\mu\rho}\frac{\dd x'^\mu}{\dd s}\frac{\dd x'^\rho}{\dd s}=0.
$$
If present, the forces other than gravitation applying to the test particle can be added to the right-hand member 
of equation [](#eq:eqm3).

:::{note} Covariant derivative

The affine connection $\Gamma^\nu_{\ \mu\rho}$ is also involved in the definition of the covariant derivative.
$V^\nu{}_{;\mu}$ of a vector $V^\nu$ with respect to the $x'^\mu$ coordinate:
$$
V^\nu{}_{;\mu} \equiv \partial_\mu V^\nu + \Gamma^\nu_{\ \mu\rho}V^\rho
$$
This definition of the derivative in General Relativity expresses
the variation of a vector along a coordinate in non-flat space.
It is transformed in the same way as a vector by a
a change of coordinates, unlike the usual derivative: the
variation vector is therefore correctly defined. To illustrate its depth, 
here's the definition of the covariant derivative $DV^\mu/D\tau$,
not with respect to a coordinate, but along any curve
curve parametrized by the proper time $\tau$ (invariant to coordinate
change of coordinates):
$$\frac{DV^\mu}{D\tau} \equiv \frac{\dd V^\mu}{\dd\tau} + \Gamma^\mu_{\ \nu\lambda}\frac{\dd x^\lambda}{\dd\tau} V^\nu.$$
The equation of motion [](#eq:eqm2) is then written very simply
$$\frac{DU^\mu}{D\tau}=0,$$ 
with $U^\mu$ the velocity vector $\dd x^\mu/\dd\tau$. This equation is strongly reminiscent of
the initial equation of motion [](#eq:eqm1). The notion of covariant derivative is therefore well suited to General Relativity
General Relativity and replaces the usual derivative in this context. 
Note that for a covariant vector, the covariant derivative is written :
$$\label{eq:dcov-cov}
\frac{DV_\mu}{D\tau} \equiv \frac{\dd V_\mu}{\dd\tau} - \Gamma^\nu_{\ \mu\lambda}\frac{\dd x^\lambda}{\dd\tau} V_\nu.
$$
:::


### Towards the Einstein equation

Armed with these tools, let's move on to a simple derivation of the
Einstein's equation, which reduces gravitation to a deformation of
space-time by matter. Let's start with a  
massive particle moving slowly through a weak gravitational field. 
According to the Equivalence Principle, we have seen that there exists a system of inertial coordinates
coordinates $\left(ct,\vec x'\right)$[^2] such that the equation of motion
of motion [](#eq:eqm2) is also valid in this new situation
with gravitational field. The weak velocity
allows us to neglect $\dd\vec x/\dd\tau$ in front of $c\dd t/\dd\tau$. We then have, to first order in a weak, quasi-stationary
quasi-stationary gravity field:
$$
\frac{\dd^2x'^\mu}{\dd\tau^2} + \Gamma^\mu_{\ 00}\left(c\frac{\dd t}{\dd\tau}\right)^2=0, \qquad \Gamma^\mu_{\ 00} \approx -\frac{1}{2}g^{\mu\nu}\frac{\partial g_{00}}{\partial x'^\nu}.
$$

Assuming a weak gravitational field, we can adopt an almost Cartesian
Cartesian metric:
$$g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad \vert h_{\mu\nu}\vert \ll 1,$$
and we obtain to first order: 
$$\left\lbrace
\begin{array}{rl}
    \mu=1,2,3\ : & \displaystyle{\frac{\dd^2\vec x'}{\dd\tau^2} = \frac{1}{2}\left(c\frac{\dd t}{\dd\tau}\right)^2\vec{\nabla} h_{00} } \\
    \mu=0\ : & \displaystyle{\frac{\dd^2t}{\dd\tau^2} = 0.}
\end{array}\right.$$ 
From the second equation we deduce that $\dd t/\dd\tau$ is
a constant and so the first equation gives :
$$\label{eq:vers_einstein}
\frac{\dd^2\vec x'}{\dd t^2} = \frac{1}{2}c^2\vec{\nabla} h_{00}.
$$
Now, we know that in the Newtonian limit we have :
$$\frac{\dd^2\vec x'}{dd t^2} = -\vec{\nabla} \phi$$
with $\phi$ the gravitational potential (like $\phi=-G_N M / r$ generated by a mass $M$ at a distance
distance $r$ with $G_N$ being Newton's constant). Comparing with
[](#eq:vers_einstein), we have $h_{00}=-2\phi/c^2+\text{constant}$. Now
the chosen coordinate system must be Cartesian at infinity
(low perturbation assumption), so $h_{00}=-2\phi/c^2$ and :
$$\label{eq:g00}
g_{00}=-\left(1+\frac{2\phi}{c^2}\right),
$$ 
The $g_{00}$ element corresponds to the time component
of the metric, the beat of the clocks therefore depends on the
intensity of the gravitational field. This corresponds to the Einstein effect,
the only consequence of General Relativity in use today
(in GPS, see [](#fig:effet_einstein)).


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

This exercise on a point particle teaches us that the gravitational field
is ultimately contained within the metric, and that this metric therefore
depends on the presence of matter. It is therefore possible
a generalization of this observation. The Newtonian potential is
determined by the Poisson equation :
$$\nabla^2\phi = 4\pi G_N \rho,$$
where $\rho$ is the matter density and $G_N$ is the Newton constant. The latter is associated with the energy density
energy density $\epsilon$ of the energy-impulsion tensor of matter $T_{00} = \epsilon = \rho c^2 $ (see chapter [](./02_friedmann_equations.md)), so with equation
[](#eq:g00) we can obtain :
$$
\nabla^2 g_{00}=-\frac{8\pi G_N}{c^4} T_{00}.
$$ 
We can then imagine that there exists a tensor $G_{\mu\nu}$ combining first and second derivatives of the metric $g_{00}$.
second derivatives of the metric $g_{\mu\nu}$ generalizing the latter
equation to all coordinates such that 
$$\label{eq:einstein1}
G_{\mu\nu}=-\frac{8\pi G_N}{c^4} T_{\mu\nu}.
$$ 
This last equation corresponds to a first version of Einstein's equation. This line of reasoning
only allowed us to intuit its form, but a more rigorous
rigorous demonstration gives us the expression of the Einstein tensor
$G_{\mu\nu}$ : 
$$
G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R
$$
with $R_{\mu\nu}$ the Ricci tensor and $R$ the scalar curvature (trace
of the Ricci tensor $R^\mu_{\;\mu}$), themselves obtained by the Riemann tensor
Riemann tensor $R^\mu_{\nu\alpha\beta}$ : 
$$
\begin{aligned}
R^\mu_{\ \nu\alpha\beta} & = -\partial_\alpha \Gamma^\mu_{\ \nu\beta} +  \partial_\beta \Gamma^\mu_{\ \nu\alpha} - \Gamma^\mu_{\ \alpha\sigma}\Gamma^\sigma_{\ \nu\beta} + \Gamma^\mu_{\ \beta\sigma}\Gamma^\sigma_{\ \nu\alpha} \\
R_{\mu\nu} & =R^\alpha_{\ \mu\alpha\nu}.
\end{aligned}
$$
$G_{\mu\nu}$ appears to have zero divergence because :
$$G^{\mu\nu}_{\;\;;\mu}=0\quad\text{(Bianchi identity)}.$$

:::{important}

The Bianchi identity and the Einstein equation
[](#eq:einstein1) imposes the conservation of energy, therefore
directly from geometric properties:
$$\label{eq:conservation_energie_tenseur}
T^{\mu\nu}_{\;\;\;;\mu}=0
$$
:::

Using the Bianchi identity, we can also see that Einstein's equation can be
be defined to within one constant[^3] while retaining the conservation of energy. This constant is 
called the cosmological constant. Here's Einstein's equation in its definitive form {cite:p}`Einstein1917` :
$$\label{eq:einstein2}
\fbox{$ G_{\mu\nu}-\Lambda g_{\mu\nu} = -\frac{8\pi G_N}{c^4} T_{\mu\nu} $}
$$



[^consc]: We must keep $\vert \dd \vec x' / \dd t'\vert = c$ for the propagation of a light ray so $\dd s^2 = 0$.

[^1]: Through this definition, we have chosen a signature metric
    $(-,+,+,+)$ which we'll keep hereafter.

[^2]: Hereafter, the $0$ index of the tensors will correspond to the time
    time coordinates, while the following indices
    correspond to the spatial coordinates.

[^3]: Because we also have $g^{\mu\nu}_{\;\;;\mu}=0$.

[^4]: 1 parsec (pc) = 3.262 light-years = 3.086e16 m. 100 $\approx$
    light-years.

[^5]: These historical considerations are developed in reference
    {cite:t}`Astier2012`.

[^6]: More precise calculations taking into account renormalization
    renormalization problems show that the detuning can be reduced from 120 to
    about fifty orders of magnitude, which is still enormous.
    {cite:p}`Martin2012`.