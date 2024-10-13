---
short_title: General Relativity
authors:
  - jneveu
keywords: special relativity, general relativity, metric

---

A brief introduction to General Relativity
=============================================

Reminders of Special Relativity
--------------------------------

:::{important} Principle of Special Relativity

The laws of physics are identical in all Galilean reference frames. 
:::

If a physical law seems true in one inertial reference frame, then it must remain true in another. This is the case, for example, with Newton's second law, but imposing it on the theory of electromagnetism posed a serious problem, by calling into question the Galilean composition of velocities.

In the special case of Maxwell's theory of electromagnetism, a velocity appears that is invariant to changes in the coordinate system: this velocity is identified with the celerity of light. As light is carried by the photon, a particle of zero mass, this is also the maximum speed that can be reached in our Universe. If electromagnetic theory hadn't been written in 1905, one argument might also have been that there must be a maximum speed in the Universe if we believe that no transport of information can be instantaneous. At that point, this limiting speed must be the same in all inertial reference frames, and the pivotal celerity of the theory of Special Relativity would have been the speed of the fastest-propagating interaction. In our Universe, this is the electromagnetic interaction {cite:p}`landau1989theory`. In both approaches, the principle of special relativity dictates that there is a maximum velocity $c$ that is invariant to any change of coordinate system. *If electromagnetism is verified in a Galilean reference frame, what are the space-time coordinate transformations that can leave this velocity invariant?

Let's consider a quadri-vector with coordinates $x^\alpha$, where the $\alpha=0$ component corresponds to time[^2] $ct$ (with $c$ the famous maximum celerity and $t$ time) and the $\alpha=1,2,3$ components correspond to Cartesian coordinates $x^1,x^2, x^3$. In this course, we'll use Greek letters for components from 0 to 3 and Latin letters for spatial components from 1 to 3. To switch to another coordinate system $x'^\alpha$, we introduce the Lorentz transformation $\Lambda^\alpha_{\;\beta}$ as follows:
\begin{equation}\label{eq:boost}
x'^{\alpha} = \Lambda^\alpha_{\;\beta} x^\alpha + a^\alpha,
\end{equation}
where $a^\alpha$ is a simple temporal and spatial translation. We define the Minkowski metric:
\begin{equation}\label{eq:minkowski}
\eta_{\alpha\beta} = \begin{pmatrix}
-1 & 0& 0& 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix}
\end{equation}
so that in Cartesian coordinates we can define the space-time interval between two nearby space-time coordinates as follows:
$$ \dd s^2 = - c^2 \dd t^2 + \dd \vec x^2 = \eta_{\alpha\beta}\dd x^\alpha \dd x^\beta $$
To ensure that the speed of light is invariant to the change of coordinate system $x'^{\alpha}$, we must keep $\vert \dd \vec x' / \dd t'\vert = c$ for the propagation of a light ray, so $\dd s'^2=\dd s^2 = 0$. The Lorentz transformation must therefore ensure the conservation of the space-time interval:
$$
\dd s'^2 = \eta_{\alpha\beta}\dd x'^\alpha \dd x'^\beta = \eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta}  \dd x'^\gamma \dd x'^\delta = \eta_{\gamma\delta} \dd x^\gamma \dd x^\beta = \dd s^2
$$
Hence the closure relation:
$$
\label{eq:dscons}
\eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta} = \eta_{\gamma\delta}
$$

From the constitutive relation [](#eq:dscons), we can show that Lorentz transformations form a group defined by $\Lambda^{0}_{\;0}\geqslant 1$ and $\mathrm{det}\;\Lambda=+1$. A few calculations later (see {cite:t}`raimond` for example), we can show that the Lorentz transformation between two reference frames, one of which is moving at the speed $\vec v = v \vec e_{1}$, is uniquely written:
\begin{equation}\label{eq:lorentz}
\Lambda^{alpha}_{\;\beta} = \begin{pmatrix}
\gamma & -\beta \gamma & 0& 0 \\
-\beta \gamma & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix},\quad \beta = \frac{v}{c},\quad \gamma = \frac{1}{\sqrt{1 - \beta^2}}
\end{equation}

If we include space rotations, with one frame of reference moving at a constant $\vec v$ velocity relative to another frame of reference, the components of the $\Lambda^\alpha_{\;\beta}$ tensor can finally be written as:
\begin{equation}\label{eq:lorentz2}
\Lambda^0_{\;0} = \gamma,\quad \Lambda^i_{\;0} = \gamma v_i / c,\quad \Lambda^0_{\;j} = \gamma v_j / c,\quad \Lambda^i_{\;j} = \delta_{ij} + (\gamma - 1) \frac{v_i v_j}{v^2}
\end{equation}


From Newton to General Relativity
----------------------------------

General Relativity is the theory of gravitation that underpins modern cosmology. It provides a geometric explanation for the gravitational force introduced by Newton three centuries earlier. In this theory, falling to the ground is no longer due to a force vector unfortunately oriented towards the ground, but to the deformation of space-time caused by the Earth. Formulated in this way, General Relativity seems complicated for very few reasons. But the general principles underlying this theory and the wealth of its implications (including Newtonian theory) make it the leading theory for describing gravitation. In this section, we will introduce step by step several concepts of General Relativity, such as the geodesic equation, the metric and the covariant derivative, culminating in Einstein's equation of General Relativity, the basis of modern cosmology. This introduction is largely inspired by {cite:t}`Weinberg1972` and {cite:t}`Gourgoulhon2013`. 

### The Equivalence Principle

In Newton's fundamental principle of dynamics, why is the mass involved in the inertia term strictly the same as that involved in Newtonian gravitation? This troubling equality between inertial mass and gravitational mass, validated by centuries of experimentation (Newton's pendulums, Eötvös' balance, etc.), sets gravitation apart from other interactions, such as Coulomb's force, which depends on the electrical charge of the bodies considered. This suggests that gravitation is not a property of the bodies themselves, but of the space in which they move. 

Let's consider a point mass of mass $m$ subjected to a uniform and constant external gravitational field $\vec g$ and to no other force. Then the fundamental principle of dynamics applied in a Galilean reference frame to this object allows us to predict its position $\vec x$ at an instant $t$ by solving the differential equation:
$$m\frac{\dd^2\vec x}{\dd t^2} = m\vec g$$ 
Let's place ourselves in the object's (non-galilean) frame of reference using the following coordinate transformation:
$$
\vec x' = \vec x - \frac{1}{2}\vec g t^2, \qquad t'=t$$ 
Then in this frame of reference the gravitational force is “absorbed” by the inertial term:
$$m\frac{\dd^2\vec x}{\dd t^2} = m\vec g \Leftrightarrow m\frac{\dd ^2\vec x'}{\dd t'^2} = 0.$$
The laws of physics therefore appear identical for an observer bound to a Galilean frame of reference and considering that the object is subject to a gravitational force, and for an observer bound to a uniformly accelerated frame of reference and considering that the object is not subject to a gravitational force. The gravitational force felt by a point mass is therefore equivalent to the choice of a uniformly accelerated reference frame relative to a Galilean reference frame, at least locally in a region where $\vec g$ is quasi-constant and for an experiment duration where $\vec g$ is quasi-stationary. The Equivalence Principle formulated by Einstein acknowledges the equivalence between gravitation and acceleration due to the equality of inertial and gravitational masses, at least for gravitational fields that vary only slightly in time and space.

:::{important} The Equivalence Principle

*At any point in space-time in an arbitrary gravitational field, it is possible to choose a local system of inertial coordinates such that, in a sufficiently small region around the point in question, all the laws of nature take the same form as in an unaccelerated, gravitation-free Cartesian coordinate system* {cite:p}`Weinberg1972`. 
:::

This is a generalization of the principle of special relativity to all reference frames, with or without gravitation. This principle has been verified experimentally with very good accuracy, notably by the *Lunar Laser Ranging* {cite:p}`Williams2004`.

### Equations of motion

Let's apply the Equivalence Principle to the problem of a massive object in free fall. For this object, there exists a *particular* coordinate system such that the equation of its trajectory $x'^\mu$ is written in the same way as if the frame of reference were unaccelerated and without gravitation:
\begin{equation}\label{eq:eqm1}
\frac{\dd^2 x'^\mu}{\dd\tau^2}=0,
\end{equation}
with $\dd\tau$ the proper time[^1] :
$$
\label{eq:proper-time}
\dd \tau^2 \equiv -\eta_{\mu\nu} \dd x'^\mu \dd x'^\nu.
$$ 
The parameter $\tau$ will enable us to parameterize the curve $x'^\mu(\tau)$, as a curvilinear abscissa. In this equation, it only plays the role of a label to parameterize the successive positions of the object, but it has the immense advantage of being Lorentz invariant and of being the time measured by the observer in the particle's frame of reference.

According to the Equivalence Principle, this equation is also valid in a certain neighborhood of the object in question, with a different choice of space-time coordinates. So there's another arbitrary coordinate system in which we're allowed to rewrite the equation of its trajectory $x^\mu$. Let's find the form it would take for these $x^\mu$ coordinates:
$$
0=\frac{\dd^2 x'^\mu}{\dd\tau^2}=\frac{\dd}{\dd\tau}\left(\frac{\partial x'^\mu}{\partial x^\nu} \frac{\dd x^\nu}{\dd\tau}\right) = \frac{\partial x'^\mu}{\partial x^\nu} \frac{\dd^2 x^\nu}{\dd\tau^2} + \frac{\partial^2 x'^\mu}{\partial x^\nu \partial x^\rho}\frac{\dd x^\nu}{\dd\tau}\frac{\dd x^\rho}{\dd\tau}. $$
After multiplying by $\partial x^\gamma/\partial x'^\mu$, we obtain [^inv] the new equation of motion:
$$
\label{eq:eqm2}
\frac{\dd^2x^\nu}{\dd\tau^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd\tau}\frac{\dd x^\rho}{\dd\tau}=0,
$$
where $\Gamma^\nu_{\mu\rho}$ is the *affine connection* defined by:
$$\Gamma^\nu_{\mu\rho} \equiv \frac{\partial x^\nu}{\partial x'^\lambda}\frac{\partial^2 x'^\lambda}{\partial x^\mu \partial x^\rho}.$$
The proper time is rewritten:
$$
\dd\tau^2=-\eta_{\mu\nu} \dd x'^\mu \dd x'^\nu = -g_{\mu\nu} \dd x^\mu \dd x^\nu
$$
which defines the metric tensor $g_{\mu\nu}$:
$$
\boxed{g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial x'^\alpha}{\partial x^\mu} \frac{\partial x'^\beta}{\partial x^\nu}}
$$
The tensor $g_{\mu\nu}$ describes the geometry of space-time in the new coordinate system $x^\mu$ and replaces the Cartesian metric $\eta_{\mu\nu}$. It is the fundamental object of General Relativity, as it allows us to describe distances traveled in a non-Euclidean (curved) space-time.


:::{tip} The metric tensor in simple cases

* Let be a 2D Euclidean space of metric $\eta_{\alpha\beta} = \text{diag}(1, 1)$ of coordinates $\vec X=(x,y)$. Rotate space by an angle $\theta$, passing through coordinates $\vec X'=(x',y')$ by :
\begin{equation*}
\left\lbrace\begin{array}{ll}
x' &= x\cos \theta + y \sin \theta \\
y' &= y\cos \theta - x \sin\theta
\end{array}\right. \Rightarrow g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial X'^\alpha}{\partial X^\mu} \frac{\partial X'^\beta}{\partial X^\nu}
\end{equation*}
Let's calculate $g_{11}$ for the example:
\begin{equation*}
g_{11} = \eta_{\alpha\beta} \frac{\partial X'^\alpha}{\partial X^1} \frac{\partial X'^\beta}{\partial X^1} = \left(\frac{\partial x'}{\partial x}\right)^2 + \left(\frac{\partial y'}{\partial x}\right)^2 = \cos^2 \theta + \sin^2 \theta = 1
\end{equation*}
After calculating the other terms, we have :
\begin{equation*}
g_{\mu\nu} = 
\begin{pmatrix}
1 & 0 \\
0& 1
\end{pmatrix}
\end{equation*}
so the space remains Euclidean after rotation. Equivalently, we could have obtained the metric $g_{\mu\nu}$ by studying the conservation of an element of length by rotation:
\begin{equation*}
\dd \vec l^2 = \dd x^2 + \dd y^2 = \cdots = (\dd x')^2 + (\dd y')^2.
\end{equation*}

* Let be a 2D spherical space of radius $a$. A position on the sphere is given by two angles $\vec \xi = (\theta, \phi)$. An elementary vector $\dd \vec l$ on the sphere has length :
\begin{equation*}
\dd \vec l^2 = a^2\dd \theta^2 + a^2 \sin^2 \theta \dd \phi^2 = g_{ij} \dd \xi^i \dd \xi^j
\end{equation*}

```{figure} ../../images/sphere_gmunu


```

Hence the metric on this curved space:
\begin{equation*}
g_{\mu\nu} = \begin{pmatrix}
a^2 & 0 \\
0& a^2\sin^2\theta
\end{pmatrix}
\end{equation*} 
whose curvature is half the Ricci scalar (see <wiki:Scalar_curvature>) and is $1/a^2 > 0$ as expected for a sphere. 

* Let be a 2D Euclidean space-time of metric $\eta_{\alpha\beta} = \text{diag}(1, 1, 1)$ of coordinates $\vec X=(ct, x,y)$. We perform a Galilean translation of space with a constant velocity $\vec V=V\vec e_x$, passing at coordinates $\vec X'=(ct', x',y')$ through :
\begin{equation*}
\left\lbrace\begin{array}{ll}
ct' & = ct \\
x' &= x + Vt \\
y' &= y
\end{array}\right. \Rightarrow g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial X'^\alpha}{\partial X^\mu} \frac{\partial X'^\beta}{\partial X^\nu} \approx 
\begin{pmatrix}
1 & V/c & 0 \\
V/c & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
\end{equation*}



:::




:::{note} Inverse metric
:class: dropdown

The inverse metric tensor is defined by:
$$
g^{\mu\nu} = \eta^{\alpha\beta} \frac{\partial x^\mu}{\partial x'^\alpha} \frac{\partial x^\nu}{\partial x'^\beta}.$$
Indeed, by definition we have: 
$$
\begin{aligned}
g^{\nu\rho}g_{\mu\nu} & = \eta^{\alpha\beta} \frac{\partial x^\nu}{\partial x'^\alpha} \frac{\partial x^\rho }{\partial x'^\beta} \eta_{\gamma\delta} \frac{\partial x’^\gamma}{\partial x^\mu} \frac{\partial x’^\delta}{\partial x^\nu} \frac{\partial x'^delta}{\partial x^\nu} \frac{\partial x’^\gamma}{\partial x^\mu} \frac{\partial x’^\delta}{\partial x^\nu} \frac{\partial x’^\delta}{\partial x^\nu}
& = \delta^\delta_\alpha \eta^{\alpha\beta} \frac{\partial x^\rho }{\partial x'^\beta} \eta_{\gamma\delta} \frac{\partial x'^\gamma}{\partial x^\mu} \text{ with } \frac{\partial x^\nu}{\partial x'^\alpha}\frac{\partial x'^\delta}{\partial x^\nu} = \delta^\delta_\alpha \alpha
& = \frac{\partial x^\rho}{\partial x'^\beta}\frac{\partial x'^\beta}{\partial x^\mu} = \delta^\rho_\mu,\end{aligned}$$
where $\delta^\rho_\mu$ is the Kronecker symbol ($\delta^\rho_\mu=1$ if $\rho=\mu$, 0 otherwise). 
:::

We could later show that $\Gamma^\nu_{\ \mu\rho}$ can only be written using a single coordinate system and the metric tensor : 
$$
\label{eq:connection}
\Gamma^\nu_{\mu\rho} = \frac{1}{2}g^{\lambda\nu}\left( \frac{\partial g_{\lambda\rho}}{\partial x^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x^\rho} - \frac{\partial g_{\mu\rho}}{\partial x^\lambda} \right)
$$

For a massless particle like the photon or neutrino, the proper time defined by equation [](#eq:proper-time) is zero. Instead of $\tau$, we can use another curvilinear abscissa, such as the coordinate $\lambda = x^0$, to parameterize the trajectory of the curve. Similar reasoning leads to this equation of motion:
$$
\label{eq:eqm3}
\frac{\dd^2x^\nu}{\dd \lambda^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd \lambda}\frac{\dd x^\rho}{\dd \lambda}=0.
$$
If present, non-gravitational forces on the test particle can be added to the right-hand side of equation [](#eq:eqm3):
$$\label{eq:eqm4}
\boxed{\frac{\dd^2x^\nu}{\dd \lambda^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd \lambda}\frac{\dd x^\rho}{\dd \lambda}=\frac{f^\mu}{m}}
$$
with $m$ the mass of the object and $f^\mu$ the contravariant vector of non-gravitational forces applying to a massive particle[^2prime]. The equation [](#eq:eqm4) is therefore the correct equation for the Equivalence Principle of the Fundamental Principle of Dynamics, since it can be shown to be invariant to a local transformation of the coordinate system (see {cite:t}`Weinberg1972`[p. 102]). 

### Covariant derivative

The affine connection $\Gamma^\nu_{\ \mu\rho}$ is also used to define the covariant derivative $V^\nu{}_{;\mu}$ of a vector $V^\nu$ with respect to the coordinate $x'^\mu$:
$$
V^\nu{}_{;\mu} \equiv \partial_\mu V^\nu + \Gamma^\nu_{\ \mu\rho}V^\rho.
$$
The first term corresponds to the ordinary variation of a vector when moved in its vicinity. The second term takes into account changes in the coordinate system, which is also displaced, as the Christoffel symbol describes changes in the reference frame's base vectors.

:::{figure} ../../images/covariant_derivative.svg

Illustration of the variation of a vector $V^\mu$ (cyan) in the vicinity of a base $(e_\mu, e_\nu)$ of a curved space. Following a displacement in its neighborhood (here along $e_\mu$), the vector changes size (first term of the covariant derivative) and so does the basis that defines its projections and hence its coordinates. The covariant derivative calculates the variation in the components of vector $V^\mu$ due to these two changes.
::: 

This definition of the derivative in General Relativity correctly expresses the variation of a vector along a coordinate in curved space. This variation vector is transformed in the same way as a contravariant vector by a coordinate change (unlike the usual derivative): the variation vector $V^\nu{}_{;\mu}$ is therefore correctly defined for any coordinate system. 

To illustrate its depth, here's the definition of the covariant derivative $DV^\mu/D\tau$ not with respect to a coordinate, but along any curve parametrized by the proper time $\tau$ (invariant by coordinate change):
$$
\frac{DV^\mu}{D\tau} \equiv \frac{\dd V^\mu}{\dd\tau} + \Gamma^\mu_{\ \nu\lambda}\frac{\dd x^\lambda}{\dd\tau} V^\nu.$$
Let $U^\mu$ be the velocity vector $\dd x^\mu/\dd\tau$. The equation of motion [](#eq:eqm4) is then very simply written
$$
\boxed{m\frac{DU^\mu}{D\tau}=f^\mu}
$$ 
This equation is strongly reminiscent of the fundamental principle of dynamics, but places mechanics in a relativistic framework, invariant to any change of coordinate system. The notion of covariant derivative is therefore well suited to General Relativity calculations, and replaces the usual derivative in this framework. 

Generally speaking, replacing the usual derivatives of a physical theory with covariant derivatives means that the laws of physics can be written in such a way as to respect the equivalence principle, i.e. invariant to any change of reference frame and in the presence of gravitation. If this is true without gravitation and locally in a Minkowski space, then it remains true in any reference frame with gravitation. For example, in the absence of a gravitational field, Maxwell's equation can be written as follows:
$$
\frac{\partial F^{\alpha\beta}}{\partial x^\alpha} = - J^\beta
$$
where $J^\beta$ is the quadri-vector electric current and $F^{\alpha\beta}$ the electromagnetic tensor. If we introduce the tensors $F^{\mu\nu}$ and $J^\mu$ such that the latter reduce to $F^{\alpha\beta}$ and $J^\beta$ in a Minkowski inertial reference frame, then electromagnetic theory respects the equivalence principle if we use the covariant derivative:
$$
F^{\mu\nu}{}_{;\mu} = - J^\mu
$$
and this is valid in any coordinate system, since it is true in Minkowski.

:::{note} Covariant derivative of a covariant vector

Note that for a covariant vector, the covariant derivative is written :
$$\label{eq:dcov-cov}
\frac{DV_\mu}{D\tau} \equiv \frac{\dd V_\mu}{\dd\tau} - \Gamma^\nu_{\ \mu\lambda}\frac{\dd x^\lambda}{\dd\tau} V_\nu.
$$
:::


### Towards Einstein's equation

Armed with these tools, let's move on to a simple derivation of Einstein's equation, which summarizes gravitation as a deformation of space-time by matter. Let's start with a massive particle moving slowly in a weak, constant gravitational field, but any gravitational field this time. According to the Equivalence Principle, we have seen that there exists an inertial coordinate system $\left(ct',\vec x'\right)$ such that the equation of motion [](#eq:eqm1) is still valid in another reference frame $\left(ct,\vec x'\right)$ but with a gravitational field. The low-speed hypothesis allows us to neglect $\dd\vec x/\dd\tau$ in front of $c\dd t/\dd\tau$. In a weak, quasi-stationary gravitational field, we have to first order:
$$
\frac{\dd^2x^\mu}{\dd\tau^2} + \Gamma^\mu_{\ 00}\left(c\frac{\dd t}{\dd\tau}\right)^2=0, \qquad \Gamma^\mu_{\;\; 00} \approx -\frac{1}{2}g^{\mu\nu}\frac{\partial g_{00}}{\partial x^\nu}.
$$

Assuming a weak gravitational field, we can adopt an almost Cartesian metric:
$$
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad \vert h_{\mu\nu} \vert \ll 1,
$$
and we obtain to first order: 
$$
\left\lbrace
\begin{array}{rl}
    \mu=1,2,3\ : & \displaystyle{\frac{\dd^2\vec x}{\dd\tau^2} = \frac{1}{2}\left(c\frac{\dd t}{\dd\tau}\right)^2\vec{\nabla} h_{00} } \\
    \mu=0\ : & \displaystyle{\frac{\dd^2 t}{\dd\tau^2} = 0.}
\end{array}
\right.
$$ 
From the second equation we deduce that $\dd t/\dd\tau$ is a constant. So we can divide the first equation by $\dd t / \dd \tau$ and obtain :
$$
\label{eq:vers_einstein}
\frac{\dd^2\vec x}{\dd t^2} = \frac{1}{2}c^2\vec{\nabla} h_{00}.
$$ 
Now we know that in the Newtonian limit we have :
$$
\frac{\dd^2\vec x}{\dd t^2} = -\vec{\nabla} \phi$$
with $\phi$ the gravitational potential (i.e. $\phi=-\GN M /r$ if generated by a mass $M$ at a distance $r$, $\GN$ being Newton's constant). Comparing with [](#eq:vers_einstein), we have $h_{00}=-2\phi/c^2+\text{constant}$. Now the metric must be Minkowski at infinity (weak perturbation assumption), so $h_{00}=-2\phi/c^2$ and :
$$
\label{eq:g00}
g_{00}=-\left(1+\frac{2\phi}{c^2}\right),
$$ 
As a result, the space-time metric will be able to contain gravitational effects. The element $g_{00}$ corresponds to the time component of the metric, so the beat of the clocks depends on the intensity of the gravitational field. This corresponds to the Einstein effect, the only consequence of General Relativity in technological use today (in GPS, see [](#fig:effet_einstein)).


:::{figure} ../../images/effet_eintein.svg
:name: fig:effet_einstein
:align: center
:width: 90%

Illustration of the Einstein effect. A photon falling into a gravity well gains energy, so its frequency increases. Equivalently, clocks in a gravitational field lag behind identical clocks outside it. GPS receivers need to take this effect into account to deduce their position relative to the satellites.
:::

This exercise on a point particle teaches us that the gravitational field is ultimately contained within the metric, and that this metric therefore depends on the presence of matter. It is therefore possible to imagine a generalization of this observation. The Newtonian potential is determined by Poisson's equation:
\begin{equation}\label{eq:poisson}
\nabla^2\phi = 4\pi \GN \rho_m
\end{equation}
where $\rho_m$ is the mass density and $\GN$ is Newton's constant. The latter is associated with the energy density $\epsilon$ of the energy- momentum tensor of matter $T_{00} = \epsilon = \rho_m c^2 $ (see chapter [](./02_friedmann_equations.md)), so with equation [](#eq:g00) we can obtain:
$$
\nabla^2 g_{00}=-\frac{8\pi \GN}{c^4} T_{00}.
$$ 
This equation is not invariant to the Lorentz transformation, hence the need to modify the theory of Newtonian gravitation if we accept the principle of special relativity. Tensors are the right objects to achieve this goal. We can then imagine that there exists a tensor $G_{\mu\nu}$ combining first and second derivatives of the metric $g_{\mu\nu}$ generalizing the latter equation to all coordinates such that 
$$
\label{eq:einstein1}
G_{\mu\nu}=-\frac{8\pi \GN}{c^4} T_{\mu\nu}.
$$ 
This last equation corresponds to a first version of *Einstein's equation*. This reasoning only allowed us to intuit its form, but another more rigorous demonstration gives us the expression of the Einstein tensor $G_{\mu\nu}$ : 
$$
G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R
$$
with $R_{\mu\nu}$ the Ricci tensor and $R$ the scalar curvature (trace of the Ricci tensor $R^\mu_{\;\mu}$), themselves obtained by the Riemann tensor $R^\mu_{\ \nu\alpha\beta}$ : 
$$
\begin{aligned}
R^\mu_{\ \nu\alpha\beta} & = -\partial_\alpha \Gamma^\mu_{\ \nu\alpha\beta} + \partial_\beta \Gamma^\mu_{\ \nu\alpha\beta} - \Gamma^\mu_{\ \alpha\sigma}\Gamma^\sigma_{\ \nu\beta} + \Gamma^\mu_{\ \beta\sigma}\Gamma^\sigma_{\ \nu\alpha} \\
R_{\mu\nu} & =R^\alpha_{\ \mu\alpha\nu}.
\end{aligned}
$$
*Since Einstein's tensor $G_{\mu\nu}$ contains second derivatives of the metric, Einstein's equation links the curvature of space-time, and hence the trajectories of bodies, to its energy and matter content.*


What's more, $G_{\mu\nu}$ appears to have zero divergence. This is the Bianchi identity:
$$G^{\mu\nu}_{\;\;\;;\mu}=0.$$

:::{important} Conservation of $T^{\mu\nu}$$

Bianchi's identity and Einstein's equation [](#eq:einstein1) impose the conservation of energy, therefore directly derived from geometrical properties:
$$
\label{eq:conservation_energie_tenseur}
T^{\mu\nu}_{\;\;\;;\mu}=0
$$
:::

Using Bianchi's identity, we can also see that Einstein's equation can be defined to within one constant [^3] while retaining the conservation of energy. Today, this constant is known as the cosmological constant. Here's Einstein's equation in its definitive form {cite:p}`Einstein1917` :
$$\label{eq:einstein2}
\boxed{G_{\mu\nu}-\Lambda g_{\mu\nu} = -\frac{8\pi \GN}{c^4} T_{\mu\nu}}
$$


[^1]: Through this definition, we've chosen a signature metric $(-,+,+,+)$ which we'll keep hereafter. 

[^2]: Hereafter, the $0$ index of the tensors will correspond to the time coordinate, while the following indices will correspond to the space coordinates.

[^inv]: Knowing that $\frac{\partial x'^\rho}{\partial x^\mu} \frac{\partial x^\mu}{\partial x'^\nu} = \delta^\rho_\nu$, since $\frac{\partial x'^\rho}{\partial x^\mu}$ is the Jacobian of the coordinate transformation $x^\mu \to x'^\nu $ and the second factor is its inverse.

[^2prime]: If studying a zero-mass particle, simply replace $f^\mu/m$ by the interaction model applying to that particle.

[^3]: Because we also have $g^{\mu\nu}{}_{;\mu}=0$.
