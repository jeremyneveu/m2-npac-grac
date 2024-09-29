---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
  '\GN': '\mathcal{G}'  # newton constant
---

A brief introduction to General Relativity
=============================================

Reminders of Special Relativity
--------------------------------

:::{important} Principle of Special Relativity

The laws of physics are identical in all Galilean reference frames. 
:::

If a physical law seems true in one inertial reference frame, then it must remain true in another. This is the case, for example, with Newton's second law, but imposing it on the theory of electromagnetism posed a serious problem, by calling into question the Galilean composition of velocities.

In the special case of Maxwell's theory of electromagnetism, a velocity appears that is invariant to changes in the coordinate system: this velocity is identified with the celerity of light. As light is carried by the photon, a particle of zero mass, this is also the maximum speed that can be reached in our Universe. If electromagnetic theory hadn't been written in 1905, one argument might also have been that there must be a maximum speed in the Universe if we believe that no transport of information can be instantaneous. At that point, this limiting speed must be the same in all inertial reference frames, and the pivotal celerity of the theory of Special Relativity would have been the speed of the fastest-propagating interaction. In our Universe, this is the electromagnetic interaction {cite:p}`landau1989theory`. In both approaches, the principle of special relativity dictates that there is a maximum velocity $c$ that is invariant to any change of coordinate system. _If electromagnetism is verified in a Galilean reference frame, what are the space-time coordinate transformations that can leave this velocity invariant?_

Let's consider a quadri-vector with coordinates $x^\alpha$, where the $\alpha=0$ component corresponds to time $ct$ (with $c$ the famous maximum celerity and $t$ time) and the $\alpha=1,2,3$ components correspond to Cartesian coordinates $x^1,x^2, x^3$. In this course, we'll use Greek letters for components from 0 to 3 and Latin letters for spatial components from 1 to 3. To switch to another coordinate system $x'^\alpha$, we introduce the Lorentz transformation $\Lambda^\alpha_\beta$ as follows:
:::{math}
:label: eq:boost

x'^{\alpha} = \Lambda^\alpha_{\;\beta} x^\alpha + a^\alpha,

:::
where $a^\alpha$ is a simple temporal and spatial translation. We define the Minkowski metric:
:::{math}
:label: eq:minkowski

\eta_{\alpha\beta} = \begin{pmatrix}
-1 & 0& 0& 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix}

:::
so that in Cartesian coordinates we can define the space-time interval between two nearby space-time coordinates as follows:
$$ \dd s^2 = - c^2 \dd t^2 + \dd \vec x^2 = \eta_{\alpha}\dd x^\alpha \dd x^\beta $$
To ensure that the speed of light is invariant to the change of coordinate system $x'^{\alpha}$, we must keep $\vert \dd \vec x' / \dd t'\vert = c$ for the propagation of a light ray, so $\dd s'^2=\dd s^2 = 0$. The Lorentz transformation must therefore ensure the conservation of the space-time interval:
$$
\dd s'^2 = \eta_{\alpha\beta}\dd x'^\alpha \dd x'^\beta = \eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta}  \dd x'^\gamma \dd x'^\delta = \eta_{\gamma\delta} \dd x^\gamma \dd x^\beta = \dd s^2
$$
Hence the closure relation:
$$\label{eq:dscons}
\eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta} = \eta_{\gamma\delta}
$$

From the constitutive relation [](#eq:dscons), we can show that Lorentz transformations form a group defined by $\Lambda^{0}_{\;0}\geqslant 1$ and $\mathrm{det}\;\Lambda=+1$. A few calculations later (see {cite:t}`raimond` for example), we can show that the Lorentz transformation between two reference frames, one of which is moving at the speed $\vec v = v \vec e_{1}$ relative to the other, can only be written:
:::{math}
:label: eq:lorentz

\Lambda^{\alpha}_{\;\beta} = \begin{pmatrix}
\gamma & -\beta\gamma & 0& 0 \
\beta\gamma & \gamma & 0 & 0 \
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix},\quad \beta = \frac{v}{c},\quad \gamma = \frac{1}{\sqrt{1 - \beta^2}}

:::
If we include space rotations, with one frame of reference moving at a constant $\vec v$ velocity relative to another frame of reference, the components of the $\Lambda^\alpha_{\;\beta}$ tensor can finally be written as follows:
:::{math}
:label: eq:lorentz2

\Lambda^0_{\;0} = \gamma,\quad \Lambda^i_{\;0} = \gamma v_i / c,\quad \Lambda^0_{\;j} = \gamma v_j / c,\quad \Lambda^i_{\;j} = \delta_{ij} + (\gamma - 1) \frac{v_i v_j}{v^2}
:::

From Newton to General Relativity
----------------------------------

General Relativity is the theory of gravitation that underpins modern cosmology. It gives a geometric explanation to the gravitational force introduced by Newton three centuries earlier. In this theory, falling to the ground is no longer due to a force vector unfortunately oriented towards the ground, but to the deformation of space-time caused by the Earth. Formulated in this way, General Relativity seems complicated for very few reasons. But the general principles underlying this theory and the wealth of its implications (including Newtonian theory) make it the leading theory for describing gravitation. In this section, we will introduce step by step several concepts of General Relativity, such as the covariant derivative and the Riemann tensor, leading to Einstein's equation of General Relativity, the basis of modern cosmology. This introduction is largely inspired by {cite:t}`Weinberg1972` and {cite:t}`Gourgoulhon2013`. 

### The Equivalence Principle

In Newton's fundamental principle of dynamics, why is the mass involved in the inertia term strictly the same as that involved in Newtonian gravitation? This troubling equality between inertial mass and gravitational mass, validated by centuries of experimentation (Newton's pendulums, Eötvös' balance, etc.), sets gravitation apart from other interactions, such as Coulomb's force, which depends on the electrical charge of the bodies considered. This suggests that gravitation is not a property of the bodies themselves, but of the space in which they move. 

Let's consider a point mass of mass $m$ subjected to a uniform and constant external gravitational field $g$ and to no other force. The fundamental principle of dynamics applied to this object in a Galilean frame of reference allows us to predict its position $x$ at time $t$ by solving the differential equation:
$$m\frac{\dd^2\vec x}{\dd t^2} = m\vec g$$ 
Let's place ourselves in the object's (non-galilean) frame of reference using the following coordinate transformation:
$$ \vec x' = \vec x - \frac{1}{2}\vec g t^2, \qquad t'=t$$

Then in this frame of reference the gravitational force is “absorbed” by the inertial term:
$$ m\frac{\dd^2\vec x}{\dd t^2} = m\vec g \Leftrightarrow m\frac{\dd ^2\vec x'}{\dd t'^2} = 0.$$
The laws of physics therefore appear identical for an observer linked to a Galilean reference frame, assuming that the object is subject to a gravitational force, and for an observer linked to a uniformly accelerated reference frame, assuming that the object is not subject to a gravitational force. However, the two frames of reference are not equivalent when the Galilean frame of reference is transformed. The gravitational force felt by a point mass is therefore equivalent to the choice of a uniformly accelerated reference frame with respect to a Galilean reference frame, at least locally in a region where g$ is quasi-constant and for an experiment duration where g$ is quasi-stationary. The Equivalence Principle formulated by Einstein takes note of this observation, and extends it to gravitational fields that vary only slightly in time and space.

:::{important} The Equivalence Principle

*At any point in space-time in an arbitrary gravitational field, it is possible to choose a local system of inertial coordinates such that, in a sufficiently small region around the point in question, all the laws of nature take the same form as in an unaccelerated, gravitation-free Cartesian coordinate system* {cite:p}`Weinberg1972`. 
:::

This is a generalization of the principle of special relativity to all reference frames, with or without gravitation. This principle has been verified experimentally with very good accuracy, notably by the *Lunar Laser Ranging* {cite:p}`Williams2004`.

### Equations of motion

Let's apply the Equivalence Principle to the problem of a massive object in free fall. For this object, there exists a *particular* local coordinate system such that the equation of its trajectory $x^\mu$ is written in the same way as if the frame of reference were unaccelerated and without gravitation:
\begin{equation}\label{eq:eqm1}
\frac{\dd^2 x^\mu}{\dd\tau^2}=0,
\end{equation}
with $\dd\tau$ the proper time[^1] :
$$
\label{eq:proper-time}
\dd\tau^2 \equiv -\eta_{\mu\nu} \dd x^\mu \dd x^\nu.
  $$ 
According to the Equivalence Principle, this equation is also valid in a certain neighborhood of the object in question, with a different choice of space-time coordinates. So there's another arbitrary coordinate system in which we're allowed to rewrite the equation of its trajectory $x'^\mu$. Let's find the form it would take for these $x'^\mu$ coordinates:
$$0=\frac{\dd^2 x^\mu}{\dd\tau^2}=\frac{\dd}{\dd\tau}\left(\frac{\partial x^\mu}{\partial x'^\nu} \frac{\dd x'^\nu}{\dd\tau}\right) = \frac{\partial x^\mu}{\partial x'^\nu} \frac{\dd^2 x'^\nu}{\dd\tau^2} + \frac{\partial^2 x^\mu}{\partial x'^\nu}{\partial x'^\rho}\frac{\dd x'^\nu}{\dd\tau}\frac{\dd x'^\rho}{\dd\tau}. $$
After multiplying by $\partial x'^\nu/\partial x^\mu$, we obtain the new equation of motion:
$$
\label{eq:eqm2}
\frac{\dd^2x'^\nu}{\dd\tau^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x'^\mu}{\dd\tau}\frac{\dd x'^\rho}{\dd\tau}=0,
$$
where $\Gamma^\nu_{\mu\rho}$ is the *affine connection* defined by:
$$\Gamma^\nu_{\mu\rho} \equiv \frac{\partial x'^\nu}{\partial x^\lambda}\frac{\partial^2 x^\lambda}{\partial x'^\mu \partial x'^\rho}.$$
The proper time is rewritten:
$$\dd\tau^2=-\eta_{\mu\nu} \dd x^\mu \dd x^\nu = -g_{\mu\nu} \dd x'^\mu \dd x'^\nu$$
which defines the metric tensor $g_{\mu\nu}$:
$$
g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial x^\alpha}{\partial x'^\mu} \frac{\partial x^\beta}{\partial x'^\nu}
$$
$g_{\mu\nu}$ describes the geometry of space-time in the new coordinate system $x'^\mu$ and replaces the Cartesian metric $\eta_{\mu\nu}$. 

:::{note} Inverse metric
The inverse metric tensor is defined by:
$$g^{\mu\nu} = \eta^{\alpha\beta} \frac{\partial x'^\mu}{\partial x^\alpha} 

\frac{\partial x'^\nu}{\partial x^\beta}.$$
 Indeed, by definition we have: 
$$
\begin{aligned}
g^{\nu\rho}g_{\mu\nu} & = \eta^{\alpha\beta} \frac{\partial x'^\nu}{\partial x^\alpha} \frac{partial x'^\rho }{partial x^\beta} \eta_{gammadelta} \frac{\partial x^\gamma}{\partial x'^\mu} \frac{\partial x^\delta}{\partial x'^\nu} \\\
& = \delta^\delta_\alpha \eta^{\alpha\beta}   \frac{partial x'^\rho }{partial x^\beta} \eta_{\gamma\delta} \frac{\partial x^\gamma}{\partial x'^\mu} \text{ with } \frac{\partial x'^\nu}{\partial x^\alpha}\frac{\partial x^\delta}{\partial x'^\nu} = \delta^\delta_\alpha \\
& = \frac{\partial x'^\rho}{\partial x^\beta}\frac{\partial x^\beta}{\partial x'^\mu} = \delta^rho_\mu,\end{aligned}$$
where $\delta^\rho_\mu$ is the Kronecker symbol ($\delta^\rho_\mu=1$ if $\rho=\mu$, 0 otherwise). 
:::

We could then show that $\Gamma^\nu_{\ \mu\rho}$ can only be written using a single coordinate system and the metric tensor: 
$$\label{eq:connection}
\Gamma^\nu_{\mu\rho} = \frac{1}{2}g^{\lambda\nu}\left( \frac{\partial g_{\lambda\rho}}{\partial x'^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x'^\rho} - \frac{\partial g_{\mu\rho}}{\partial x'^\lambda} \right)
$$

For a massless particle, such as a photon or neutrino, the proper time defined by equation [](#eq:proper-time) cancels out. Instead of $\tau$ we can then use the coordinate $s = x^0$ to parameterize the trajectory of the curve, and by similar reasoning we arrive at this equation of motion:
$$
\label{eq:eqm3}
$$


$$


If present, the non-gravitational forces applying to the test particle can be added to the right-hand side of equation [](#eq:eqm3):
$$


\label{eq:eqm4}
\boxed{\frac{\dd^2x'^\nu}{\dd s^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x'^\mu}{\dd s}\frac{\dd x'^\rho}{\dd s}=\frac{f^\mu}{m}}



$$
with $m$ the mass of the object and $f^\mu$ the contravariant vector of non-gravitational forces. The equation [](eq:eqm4) is therefore the correct expression of the fundamental principle of dynamics according to the Equivalence Principle, since it is invariant to a local transformation of the coordinate system (demonstration {cite:t}`Weinberg1972`[p. 102]). 

### Covariant derivative

The affine connection $\Gamma^\nu_{;\mu\rho}$ is also used to define the covariant derivative $V^\nu{}_{;\mu}$ of a vector $V^\nu$ with respect to the coordinate $x'^\mu$:
$$
V^\nu{}_{;\mu} \equiv \partial_\mu V^\nu + \Gamma^\nu_{\ \mu\rho}V^\rho.
$$
This definition of the derivative in General Relativity correctly expresses the variation of a vector along a coordinate in curved space. It is transformed in the same way as a vector by a change of coordinates, unlike the usual derivative: the variation vector $V^\nu{}_{;\mu}$ is therefore correctly defined for any coordinate system.

To illustrate its depth, here's the definition of the covariant derivative $DV^\mu/D\tau$ not with respect to a coordinate, but along any curve parametrized by the proper time $\tau$ (invariant by coordinate change):
$$frac{DV^\mu}{D\tau} \equiv \frac{\dd V^\mu}{\dd\tau} + \Gamma^\mu_{\ \nu\lambda}\frac{\dd x^\lambda}{\dd\tau} V^\nu. $$
Let $U^\mu$ be the velocity vector $\dd x^\mu/\dd\tau$. The equation of motion [](#eq:eqm4) is then written very simply
$$\boxed{m\frac{DU^\mu}{D\tau}=f^\mu}$$ 
This equation is strongly reminiscent of the fundamental principle of dynamics, but places mechanics in a relativistic framework, invariant to any transformation of coordinate systems. The notion of covariant derivative is therefore well suited to General Relativity calculations, and replaces the usual derivative in this framework. 

Generally speaking, replacing the usual derivatives of a physical theory with covariant derivatives means that the laws of physics are written in such a way as to respect the equivalence principle, i.e. they are invariant to changes of reference frame in the presence of gravitation. If this is true without gravitation and locally in a Minkowski space, then it remains true in a reference frame that is true in any space-time with gravitation. For example, in the absence of a gravitational field, Maxwell's equation can be written as follows:
$$
\frac{partial F^{alpha\beta}}{partial x^alpha} = - J^\beta
$$
where $J^\beta$ is the quadri-vector electric current and $F^{\alpha\beta}$ the electromagnetic tensor. If we introduce the tensors $F^{\mu\nu}$ and $J^\mu$ such that the latter reduce to $F^{\alpha\beta}$ and $J^\beta$ in a Minkowski inertial reference frame, then electromagnetic theory respects the equivalence principle if we write:
$$
F^{\mu\nu}{}_{;\mu} = - J^\mu
$$
and is valid in any coordinate system, since it is true in Minkowski.

:::{note} Covariant derivative of a covariant vector

Note that for a covariant vector, the covariant derivative is written :
$$\label{eq:dcov-cov}
\frac{DV_\mu}{D\tau} \equiv \frac{dd V_\mu}{\dd\tau} - \Gamma^\nu_{\ \mu\lambda}\frac{dd x^\lambda}{\dd\tau} V_\nu.
$$
:::


### Towards the Einstein equation

Armed with these tools, let's move on to a simple derivation of Einstein's equation, which sums up gravitation as a deformation of space-time by matter. Let's start with a massive particle moving slowly in a weak, constant gravitational field, but any gravitational field this time. According to the Equivalence Principle, we have seen that there exists an inertial coordinate system $\left(ct,\vec x'\right)$[^2] such that the equation of motion [](#eq:eqm2) is also valid in this new situation with a gravitational field. The low-velocity hypothesis allows us to neglect $c\dd t/\dd tau$ in front of $c\dd x/\dd tau$. In a weak, quasi-stationary gravitational field, we have to first order:
$$
\frac{\dd^2x'^\mu}{\dd\tau^2} + \Gamma^\mu_{\ 00}\left(c\frac{\dd t}{\dd\tau}\right)^2=0, \quad \Gamma^\mu_{\ 00} \approx -\frac{1}{2}g^{\mu\nu}\frac{\partial g_{00}}{\partial x'^\nu}.
$$

Assuming a weak gravitational field, we can adopt an almost Cartesian metric:
$$g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad \vert h_{\mu\nu}$ 1,$$
and we obtain to first order: 
    $$left\lbrace
\begin{array}{rl}
    \mu=1,2,3\ : & \displaystyle{\frac{\dd^2\vec x'}{\dd\tau^2} = \frac{1}{2}\left(c\frac{\dd t}{\dd\tau}\right)^2\vec{\nabla} h_{00} } \\
    \mu=0\ : & \displaystyle{\frac{\dd^2t}{\dd\tau^2} = 0.}
\end{array}
\right.$$ 
From the second equation, we deduce that $\dd t/\dd\tau$ is a constant and so the first equation gives :
$$label{eq:vers_einstein}
\frac{\dd^2\vec x'}{\dd t^2} = \frac{1}{2}c^2\vec{\nabla} h_{00}.
$$ 
Now, we know that in the Newtonian limit we have :
$$frac{dd^2\vec x'}{dd t^2} = -\vec{nabla} \phi$$
with $\phi$ the gravitational potential (i.e. $\phi=-\GN M /r$ if generated by a mass $M$ at a distance $r$, $\GN$ being Newton's constant). Comparing with [](#eq:vers_einstein), we have $h_{00}=-2\phi/c^2+\text{constant}$.  The chosen coordinate system must be Cartesian at infinity (low perturbation assumption), so $h_{00}=-2\phi/c^2$ and :
$$\label{eq:g00}
g_{00}=-\left(1+\frac{2\phi}{c^2}\right),
$$ 
The $g_{00}$ element corresponds to the time component of the metric, so the clocks' beat depends on the intensity of the gravitational field. This corresponds to the Einstein effect, the only consequence of General Relativity in technological use today (in GPS, see [](#fig:effet_einstein)).


:::{figure}../images/effet_eintein.svg
:name: fig:effet_einstein
:align: center
:width: 90%

Illustration of the Einstein effect. A photon falling into a gravitational well
gains energy, so its frequency increases.  equivalently
equivalently, we can say that clocks in a gravitational field
delay compared to identical clocks outside. The
GPS receivers need to take this effect into account to deduce their position
position relative to the satellites.
:::

This exercise on a point particle teaches us that the gravitational field is ultimately contained within the metric, and that this metric therefore depends on the presence of matter. It is therefore possible to imagine a generalization of this observation. The Newtonian potential is determined by Poisson's equation:
\begin{equation}\label{eq:poisson}
\nabla^2\phi = 4\pi \GN \rho
\end{equation}
where $\rho$ is the mass density and $\GN$ is Newton's constant. The latter is associated with the energy density $\epsilon$ of the energy-impulse tensor of matter $T_{00} = \epsilon = \rho c^2 $ (see chapter [](./02_friedmann_equations.md)), so with equation [](#eq:g00) we can obtain:
$$
\nabla^2 g_{00}=-\frac{8\pi \GN}{c^4} T_{00}.
$$ 
This equation is not invariant to a change of reference frame, nor is it invariant to the Lorentz transformation, hence the need to modify the theory of Newtonian gravitation if we accept the principle of special relativity. Tensors are the right objects to achieve this goal. We can then imagine that there exists a tensor $G_{\mu\nu}$ combining first and second derivatives of the metric $g_{\mu\nu}$ generalizing the latter equation to all coordinates such that 
$$label{eq:einstein1}
G_{\mu\nu}=-\frac{8\pi \GN}{c^4} T_{\mu\nu}.
$$ 
This last equation corresponds to a first version of Einstein's equation. This reasoning has only allowed us to intuit its form, but another more rigorous demonstration allows us to obtain the expression of the Einstein tensor $G_{\mu\nu}$ : 
$$
G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R
$$
with $R_{\mu\nu}$ the Ricci tensor and $R$ the scalar curvature (trace of the Ricci tensor $R^\mu_{\;\mu}$), themselves obtained by the Riemann tensor $R^\mu_{\ \nu\alpha\beta}$ : 
$$
\begin{aligned}
R^\mu_{\ \nu\alpha\beta} & = -\partial_\alpha \Gamma^\mu_{\ \nu\alpha\beta} + \partial_\beta \Gamma^\mu_{\ \nu\alpha\beta} - $$ \nu\alpha\beta}. \Gamma^\mu_{\ \alpha\sigma}\Gamma^\sigma_{\ \nu\beta} + \Gamma^\mu_{\ \beta\sigma}\Gamma^\sigma_{\ \nu\alpha} \\
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

Using Bianchi's identity, we can also see that Einstein's equation can be defined to within one constant [^3] while retaining the conservation of energy. Today, this constant is known as the cosmological constant. Here's Einstein's equation in its definitive form {cite:p}`Einstein1917` :
$$\label{eq:einstein2}
\boxed{G_{\mu\nu}-\Lambda g_{\mu\nu} = -\frac{8\pi \GN}{c^4}  T_{\mu\nu}}
$$


[^1]: Through this definition, we have chosen a signature metric $(-,+,+,+)$ which we will keep hereafter.

[^2]: Hereafter, the $0$ index of the tensors will correspond to the time coordinate, while the following indices will correspond to the space coordinates.

[^3]: Because we also have $g^{\mu\nu}{}_{;\mu}=0$.

[^4]: 1 parsec (pc) $= 3.262$ light-years $= 3.086\times 10^{16}\,$m. $100,\text{Mpc}\approx 3\times 10^8\;$ light-years.

[^5]: These historical considerations are developed in reference {cite:t}`Astier2012`.

[^6]:       More precise calculations taking into account renormalization problems show that the disagreement can be reduced from 120 to about fifty orders of magnitude, which is still enormous {cite:p}`Martin2012`.     
