---
short_title: General Relativity
authors:
  - jneveu
keywords: special relativity, general relativity, metric
---

Brief Introduction to General Relativity
========================================

Special Relativity Review
-------------------------

### Principle of Special Relativity

At the end of the 19th century, Maxwell's theory of electromagnetism established itself as the description of electrical and magnetic phenomena. Better yet, it predicted the existence of electromagnetic waves which were discovered in 1888 by Heinrich Hertz. Their study showed that they have all the known properties of light waves (reflection and refraction, interference, polarization and diffraction) and especially the same speed $c = 1/\sqrt{\epsilon_0\mu_0}$ which emerges from Maxwell's equations. Hertzian and light waves are therefore electromagnetic waves, but Maxwell's electromagnetism says nothing about the reference frame in which this speed would be defined. Furthermore, the Michelson and Morley experiment (1887) <wiki:Michelson–Morley_experiment> shows that the speed of light does not seem to compose with the Earth's velocity around the Sun, while Fizeau's experiment (1849) <wiki:Fizeau_experiment> shows that it partially composes with that of a moving fluid. We therefore understand that electromagnetic theory is poorly aligned with Newtonian mechanics and seems to need patching up according to contradictory experimental results.

:::{figure} ../../images/michelson_morley_setup_en.svg
:name: fig-michelson-morley-en
:width: 100%

Diagram of the Michelson-Morley experiment (1887). Light is split into two perpendicular beams that travel equal distances before recombining at the detector. The absence of interference fringes demonstrates the invariance of the speed of light.
:::

Rather than undertaking this hazardous path which would have caused the theory to lose its predictive power when bodies are in motion, Albert Einstein proposes a revolutionary approach in his famous 1905 article *On the electrodynamics of moving bodies* {cite:p}`Einstein1905`. He postulates that the speed of light is the same in every reference frame and thus calls into question the Galilean composition of velocities, and even the notions of space and time. The fundamental principle of this new physics is the principle of special relativity.

:::{important} Principle of Special Relativity

The laws of physics are identical in all Galilean reference frames.
:::

If a physical law appears to be true in an inertial reference frame, within the experimental uncertainties defining its domain of validity, then it must remain true in another Galilean reference frame. This is the case, for example, with Newton's fundamental principle of dynamics. However, imposing this on electromagnetic theory poses a serious problem, as it requires calling into question the Galilean composition of velocities for electromagnetic waves.

### Lorentz Transformations

*If electromagnetic theory is verified in a Galilean reference frame, what are the spatio-temporal coordinate transformations that can leave this speed invariant?*
Consider two events with spatio-temporal coordinates $(t_1,x_1,y_1,z_1)$ and $(t_2, x_2, y_2, z_2)$ in a reference frame $\mathcal{R}$ linked by the exchange of a light signal, then:
$$ c^2(t_2-t_1)^2 = (x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2 $$
Imposing the constancy of velocity implies that in another Galilean reference frame $\mathcal{R}'$ we also verify:
$$ c^2(t'_2-t'_1)^2 = (x'_2-x'_1)^2 + (y'_2-y'_1)^2 + (z'_2-z'_1)^2 $$
It therefore appears judicious to define the spacetime interval for an interval between two infinitely close events:
$$ \dd s^2 = -c^2 \dd t^2 + \dd x^2 + \dd y^2 + \dd z^2 $$

Consider a four-vector of coordinates $x^\alpha$, where component $\alpha=0$ corresponds to time[^x0] $ct$ (with $c$ the famous maximum speed and $t$ the time) and components $\alpha=1,2,3$ correspond to Cartesian coordinates $x,y,z$. In this course, we will use Greek letters for components ranging from 0 to 3 and Latin letters for spatial components ranging from 1 to 3. We define the Minkowski metric:
\begin{equation}\label{eq:minkowski}
\eta_{\alpha\beta} = \begin{pmatrix}
-1 & 0& 0& 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 \end{pmatrix}
\end{equation}
such that in Cartesian coordinates we can define the spacetime interval between two close spatio-temporal coordinates:
$$ \dd s^2 = - c^2 \dd t^2 + \dd \vec x^2 = \eta_{\alpha\beta}\dd x^\alpha \dd x^\beta $$

:::{important} Conventions of this course
- Metric signature: $(-,+,+,+)$
- Greek indices: 0,1,2,3 (spacetime)
- Latin indices: 1,2,3 (space only)
:::

To switch to another coordinate system $x'^\alpha$, we introduce the Lorentz transformation $\Lambda^\alpha_{\;\beta}$ as follows:
\begin{equation}\label{eq:boost}
x'^{\alpha} = \Lambda^\alpha_{\;\beta} x^\beta + a^\alpha,
\end{equation}
where $a^\alpha$ is a simple temporal and spatial translation.

What form should this linear transformation take[^linearity]? To ensure that the speed of light is invariant under coordinate system changes $x'^{\alpha}$, we must preserve $\vert \dd \vec x' / \dd t'\vert = c$ for the propagation of a light ray, hence $\dd s'^2=\dd s^2 = 0$. The Lorentz transformation must therefore ensure conservation of the spacetime interval:
$$
\dd s'^2 =  \eta_{\alpha\beta}\dd x'^\alpha \dd x'^\beta = \eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta}  \dd x^\gamma \dd x^\delta = \eta_{\gamma\delta} \dd x^\gamma \dd x^\beta = \dd s^2
$$
Hence the closure relation:
$$
\label{eq:dscons}
\eta_{\alpha\beta} \Lambda^{\alpha}_{\;\gamma} \Lambda^{\beta}_{\;\delta} =  \eta_{\gamma\delta}
$$

From the constitutive relation [](#eq:dscons), we can demonstrate that Lorentz transformations form a group defined by $\Lambda^{0}_{\;0}\geqslant 1$ and $\mathrm{det}\;\Lambda=+1$. A few calculations later (see {cite:t}`raimond` or {cite:t}`langlois2013RG` for example), we show that the coordinate transformation between two reference frames where one moves at velocity $\vec v = v \vec e_{1}$ is uniquely written as:
\begin{equation}
\label{eq:lorentz}
\Lambda^{\alpha}_{\;\beta} = 
\begin{pmatrix}
\gamma & -\beta \gamma & 0 & 0 \\
-\beta \gamma & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 &0 & 1 
\end{pmatrix},
\quad \beta = \frac{v}{c},\quad \gamma = \frac{1}{\sqrt{1 - \beta^2}}
\end{equation}
to guarantee the constancy of the speed of light in all Galilean reference frames.

If we include spatial rotations, with a reference frame moving at constant velocity $\vec v$ relative to another reference frame, the components of tensor $\Lambda^\alpha_{\;\beta}$ are finally written as:
\begin{equation}\label{eq:lorentz2}
\Lambda^0_{\;0} = \gamma,\quad \Lambda^i_{\;0} = -\gamma v_i / c,\quad \Lambda^0_{\;j} = -\gamma v_j / c,\quad \Lambda^i_{\;j} = \delta_{ij} +  (\gamma - 1)  \frac{v_i v_j}{v^2}
\end{equation}

:::{note} Link between light and relativity
Why should the speed of light specifically be invariant? What is the link between light and a new formulation of mechanics? Since light is carried by the photon, a massless particle, this is also the maximum velocity that can be reached in our Universe. If electromagnetic theory had not been written in 1905, an argument could also have been that there must exist a maximum velocity in the Universe if we think that no information transport can be instantaneous. At that point, the principle of relativity imposes that this limiting velocity must be the same in all inertial reference frames and the pivotal speed of Special Relativity theory would have been the velocity of the fastest-propagating interaction. Which in our Universe turns out to be the electromagnetic interaction {cite:p}`landau1989theory`. In both approaches, the Principle of Special Relativity imposes that there exists a maximum velocity $c$ invariant under coordinate system changes.
:::

Lorentz transformations impose that not only does the speed of light not compose with the velocity of an observer or source, but also that it is unsurpassable. However, gravitational force propagates instantaneously over infinite distance in Newtonian theory. The displacement of a mass is instantly felt gravitationally throughout the Universe. After having to rewrite the equations of kinematics to preserve Maxwell's equations, Einstein worked for the following 10 years to reformulate Newtonian gravitational theory so that it would fit into this new framework. The main ingredient of his approach is the observation that gravitational mass and inertial mass are identical, which is an indication that gravitation could be described by a kinematic effect.

From Newton to General Relativity
----------------------------------

General Relativity is the theory of gravitation at the basis of modern cosmology. It provides a geometric explanation for the gravitational force introduced by Newton three centuries earlier. In this theory, falling to the ground is no longer due to a force vector unfortunately oriented towards the soil, but to the deformation of spacetime caused by the Earth. Formulated this way, General Relativity seems quite complicated for little gain. But the general principles at the base of this theory and the richness of its implications (including Newtonian theory) make it the flagship theory for describing gravitation. Throughout this section, we will introduce step by step several concepts of General Relativity such as the geodesic equation, the metric and the covariant derivative, to arrive at Einstein's equation of General Relativity, the basis of modern cosmology. This introduction is largely inspired by {cite:t}`Weinberg1972` and {cite:t}`Gourgoulhon2013`. 

### The Equivalence Principle

In Newton's fundamental principle of dynamics, why is the mass involved in the inertia term strictly the same as that involved in Newtonian gravitation? This troubling equality between inertial mass and gravitational mass, validated by centuries of experimentation (Newton's pendulums, Eötvös' balance, etc.), sets gravitation apart from other interactions, such as Coulomb's force, which depends on the electrical charge of the bodies considered. This suggests that gravitation is not a property of the bodies themselves, but of the space in which they move. 

:::{tip} Eötvös Experiments (1889)
:class: dropdown

In this experiment performed in 1889, Eötvös showed that a wooden mass and a platinum mass undergo the same gravitational force to within $10^{-9}$, by observing the torsion of a balance {cite:p}`VonEotvos1890`. The balance compares the torque exerted by gravitational force (dependent on gravitational mass) and the torque exerted by centrifugal force due to Earth's rotation (dependent on inertial mass). See a description of the experiment here <wiki:Eötvös_experiment>.
:::

Let us consider a point mass subjected to a uniform and constant external gravitational field $\vec g$ and to non-gravitational forces $\vec f_{\rm ng}$. Then the fundamental principle of dynamics applied in a Galilean reference frame $\mathcal{R}$ to this object allows us to predict its position $\vec x$ at an instant $t$ by solving the differential equation:
$$m_i\frac{\dd^2\vec x}{\dd t^2} = m_g\vec g + \vec f_{\rm ng}$$ 
with $m_g$ the gravitational mass and $m_i$ the inertial mass.
Let us place ourselves in an accelerated (non-Galilean) reference frame $\mathcal{R}'$ relative to the initial Galilean reference frame with an entrainment acceleration $\vec a_e$. In $\mathcal{R}'$ equipped with coordinates $(t, x')$, the fundamental principle of dynamics is written with an inertial force $-m\vec a_e$ (also called fictitious force because it comes from a kinematic effect) due to the entrainment acceleration:
$$m_i\frac{\dd^2\vec x'}{\dd t^2} = m_g\vec g  -m_i\vec a_e + \vec f_{\rm ng}$$
Thanks to the equality between inertial mass and gravitational mass $m_i=m_g=m$, we notice that we can make a *particular* choice of reference frame $\mathcal{R}'$ such that $\vec g = \vec a_e$, such that the fundamental principle of dynamics is written as if there were neither acceleration nor gravitation:
$$m\frac{\dd ^2\vec x'}{\dd t^2} = \vec f_{\rm ng}$$
The laws of physics therefore appear identical for an observer linked to a Galilean reference frame considering that the object undergoes a gravitational force and for an observer linked to a free-falling reference frame considering that the object does not undergo any gravitational force. The gravitational effect has been incorporated into a coordinate change $\vec x' = \vec x - g t^2/2$. What if this approach were possible for any gravitational field, at least locally in a region where $\vec g$ is quasi-constant and during an experiment duration where $\vec g$ is quasi-stationary? The Equivalence Principle formulated by Einstein acknowledges the equivalence between gravitation and acceleration due to the equality of inertial and gravitational masses, at least for gravitational fields that vary weakly in time and space, and elevates it to a construction principle for physical laws.

:::{important} The Equivalence Principle

*At each point of spacetime in an arbitrary gravitational field it is possible to choose a local particular system of inertial coordinates such that, in a sufficiently small region around the point in question, all laws of nature take the same form as in a non-accelerated Cartesian coordinate system without gravitation* {cite:p}`Weinberg1972`. 
:::

This is therefore a generalization of the principle of special relativity to all reference frames, in the presence of gravitation or not. This principle is verified experimentally with very good precision, notably by *Lunar Laser Ranging* {cite:p}`Williams2004` and by the MICROSCOPE satellite with a precision of $2.7\times 10^{−15}$ {cite:p}`Microscope2022`.

### Equations of motion

Let us apply the Equivalence Principle to the problem of a massive object in free fall. For this object, there therefore exists locally a *particular* coordinate system such that the equation of its trajectory $x'^\mu$ can be written in the same way as if the reference frame were non-accelerated and without gravitation:
\begin{equation}\label{eq:eqm1}
\frac{\dd^2 x'^\mu}{\dd\tau^2}=0,
\end{equation}
with $\dd\tau$ the proper time[^tau]:
$$
\label{eq:proper-time}
\dd \tau^2 \equiv -\eta_{\mu\nu} \dd x'^\mu \dd x'^\nu.
$$ 
The parameter $\tau$ will allow us to parameterize the curve $x'^\mu(\tau)$, like a curvilinear abscissa. In this equation it only plays the role of a label to parameterize the successive positions of the object, but it has the immense advantage of being Lorentz invariant and of being the time measured by the observer in the particle's reference frame.

According to the Equivalence Principle, this equation is also valid in a certain neighborhood of the object in question with another choice of spatio-temporal coordinates. There therefore exists another arbitrary coordinate system in which we have the right to rewrite the equation of its trajectory $x^\mu$. Let us look for the form it would take for these coordinates $x^\mu$:
$$
0=\frac{\dd^2 x'^\mu}{\dd\tau^2}=\frac{\dd}{\dd\tau}\left(\frac{\partial x'^\mu}{\partial x^\nu} \frac{\dd x^\nu}{\dd\tau}\right) = \frac{\partial x'^\mu}{\partial x^\nu} \frac{\dd^2 x^\nu}{\dd\tau^2} + \frac{\partial^2 x'^\mu}{\partial x^\nu \partial x^\rho}\frac{\dd x^\nu}{\dd\tau}\frac{\dd x^\rho}{\dd\tau}.$$
After multiplication by $\partial x^\gamma/\partial x'^\mu$, we obtain[^inv] the new equation of motion:
$$
\label{eq:eqm2}
\frac{\dd^2x^\nu}{\dd\tau^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd\tau}\frac{\dd x^\rho}{\dd\tau}=0,
$$
where $\Gamma^\nu_{\ \mu\rho}$ is the *affine connection* defined by:
$$
\Gamma^\nu_{\ \mu\rho} \equiv \frac{\partial x^\nu}{\partial x'^\lambda}\frac{\partial^2 x'^\lambda}{\partial x^\mu \partial x^\rho}.$$
The proper time is rewritten:
$$
\dd \tau^2=-\eta_{\mu\nu} \dd x'^\mu \dd x'^\nu = -g_{\mu\nu} \dd x^\mu \dd x^\nu
$$
which thus defines the metric tensor $g_{\mu\nu}$:
$$
\boxed{g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial x'^\alpha}{\partial x^\mu} \frac{\partial x'^\beta}{\partial x^\nu}}
$$
The tensor $g_{\mu\nu}$ describes the geometry of spacetime in the new coordinate system $x^\mu$ and replaces the Cartesian metric $\eta_{\mu\nu}$. It is the fundamental object of General Relativity because it allows describing distances traveled in non-Euclidean (curved) spacetime.

:::{tip} The metric tensor in simple cases
:class: dropdown

* Consider a 2D Euclidean space with metric $\eta_{\alpha\beta} = \text{diag}(1, 1)$ and coordinates $\vec X=(x,y)$. We perform a rotation of space by an angle $\theta$, passing to coordinates $\vec X'=(x',y')$ by:
\begin{equation*}
\left\lbrace\begin{array}{ll}
x' &= x\cos \theta + y \sin \theta \\
y' &= y\cos \theta - x \sin\theta
\end{array}
\right. \Rightarrow g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial X'^\alpha}{\partial X^\mu} \frac{\partial X'^\beta}{\partial X^\nu}
\end{equation*}
Let us calculate $g_{11}$ for the example:
\begin{equation*}
g_{11} = \eta_{\alpha\beta} \frac{\partial X'^\alpha}{\partial X^1} \frac{\partial X'^\beta}{\partial X^1} = \left(\frac{\partial x'}{\partial x}\right)^2 +  \left(\frac{\partial y'}{\partial x}\right)^2 = \cos^2 \theta + \sin^2 \theta = 1
\end{equation*}
After calculating the other terms, we have:
\begin{equation*}
g_{\mu\nu} = 
\begin{pmatrix}
1 & 0 \\
0& 1
\end{pmatrix}
\end{equation*}
so the space remains Euclidean after rotation. Equivalently, we could have obtained the metric $g_{\mu\nu}$ by studying the conservation of a length element under rotation:
\begin{equation*}
\dd \vec l^2 = \dd x^2 + \dd y^2 = \cdots = (\dd x')^2 + (\dd y')^2.
\end{equation*}

* Consider a 2D spherical space of radius $a$. A position on the sphere is given by two angles $\vec \xi = (\theta, \phi)$. An elementary vector $\dd \vec l$ on the sphere has length:
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
whose curvature is half the Ricci scalar (see <wiki:Scalar_curvature>) and equals $1/a^2 > 0$ as expected for a sphere.

* Consider a 2D Euclidean spacetime with metric $\eta_{\alpha\beta} = \text{diag}(1, 1, 1)$ and coordinates $\vec X=(ct, x,y)$. We perform a Galilean translation of space with constant velocity $\vec V=V\vec e_x$, passing to coordinates $\vec X'=(ct', x',y')$ by:
\begin{equation*}
\left\lbrace\begin{array}{ll}
ct' & = ct \\
x' &= x + Vt \\
y' &= y
\end{array}
\right. 
\Rightarrow g_{\mu\nu} = \eta_{\alpha\beta} \frac{\partial X'^\alpha}{\partial X^\mu} \frac{\partial X'^\beta}{\partial X^\nu} \approx 
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
g^{\nu\rho}g_{\mu\nu} & = \eta^{\alpha\beta} \frac{\partial x^\nu}{\partial x'^\alpha} \frac{\partial x^\rho }{\partial x'^\beta} 
\eta_{\gamma\delta} \frac{\partial x'^\gamma}{\partial x^\mu} \frac{\partial x'^\delta}{\partial x^\nu} \\
& = \delta^\delta_\alpha  \eta^{\alpha\beta} \frac{\partial x^\rho }{\partial x'^\beta} \eta_{\gamma\delta} 
\frac{\partial x'^\gamma}{\partial x^\mu}
\text{ with } \frac{\partial x^\nu}{\partial x'^\alpha}\frac{\partial x'^\delta}{\partial x^\nu} = \delta^\delta_\alpha \\
& = \frac{\partial x^\rho}{\partial x'^\beta}\frac{\partial x'^\beta}{\partial x^\mu} 
= \delta^\rho_\mu,\end{aligned}$$
where $\delta^\rho_\mu$ is the Kronecker symbol ($\delta^\rho_\mu=1$ if $\rho=\mu$, 0 otherwise).
:::

We could subsequently show that $\Gamma^\nu_{\ \mu\rho}$ can be written using only a single coordinate system and the metric tensor:
$$
\label{eq:connexion}
\Gamma^\nu_{\ \mu\rho} = \frac{1}{2}g^{\lambda\nu}\left( \frac{\partial g_{\lambda\rho}}{\partial x^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x^\rho}  - \frac{\partial g_{\mu\rho}}{\partial x^\lambda} \right)
$$
If present, forces other than gravitation acting on the test particle can be added to the right-hand side of equation [](#eq:eqm3):
$$\label{eq:eqm4}
\boxed{\frac{\dd^2x^\nu}{\dd \tau^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd \tau}\frac{\dd x^\rho}{\dd \tau}=\frac{f_{\rm ng}^\mu}{m}}
$$
with $m$ the mass of the object and $f_{\rm ng}^\mu$ the contravariant vector of non-gravitational forces acting on a massive particle[^2prime]. The correct formulation of the fundamental principle of dynamics according to the Equivalence Principle is therefore equation [](#eq:eqm4), because we can show that the latter is indeed invariant under local coordinate system transformations (demonstration {cite:t}`Weinberg1972`[p. 102]) and reduces to the fundamental principle of dynamics in the absence of gravitation (null affine connection).

:::{tip} Equation of motion for massless particles
:class: dropdown

For a massless particle, such as the photon or neutrino, the proper time defined by equation [](#eq:proper-time) is zero. Instead of $\tau$ we can then use another curvilinear abscissa, such as the coordinate $s = x^0$ to parameterize the trajectory of the curve. By similar reasoning we arrive at this equation of motion:
$$
\label{eq:eqm3}
\frac{\dd^2x^\nu}{\dd \lambda^2} + \Gamma^\nu_{\ \mu\rho}\frac{\dd x^\mu}{\dd \lambda}\frac{\dd x^\rho}{\dd \lambda}=0.
$$
:::

### Covariant derivative

The affine connection $\Gamma^\nu_{\ \mu\rho}$ also appears in the definition of the covariant derivative $V^\nu{}_{;\mu}$ of a vector $V^\nu$ with respect to coordinate $x'^\mu$:
$$
V^\nu{}_{;\mu} \equiv \partial_\mu V^\nu + \Gamma^\nu_{\ \mu\rho}V^\rho.
$$
The first term corresponds to the ordinary variation of a vector when displaced in its neighborhood. The second term takes into account the changes in the coordinate system that is also displaced, since the Christoffel symbol describes the changes in the reference frame basis vectors.

:::{figure} ../../images/covariant_derivative.svg

Illustration of the variation of a vector $V^\mu$ (cyan) in the neighborhood of a basis $(e_\mu, e_\nu)$ of a curved space. Following a displacement in its neighborhood (here along $e_\mu$), the vector changes size (first term of the covariant derivative) and the basis that defines its projections and thus coordinates also changes. The covariant derivative calculates the variation of the vector components $V^\mu$ due to these two changes.
:::

This definition of the derivative in General Relativity correctly expresses the variation of a vector along a coordinate in curved space. This variation vector transforms like a contravariant tensor under coordinate changes (unlike the usual derivative): the variation vector $V^\nu{}_{;\mu}$ is therefore correctly defined for any coordinate system.

To illustrate its full depth, here is the definition of the covariant derivative $DV^\mu/D\tau$ not with respect to a coordinate, but along any curve parameterized by proper time $\tau$ (invariant under coordinate changes):
$$
\frac{DV^\mu}{D\tau} \equiv \frac{\dd V^\mu}{\dd\tau} + \Gamma^\mu_{\ \nu\lambda}\frac{\dd x^\lambda}{\dd\tau} V^\nu.$$
Let $U^\mu$ be the velocity vector $\dd x^\mu/\dd\tau$. The equation of motion [](#eq:eqm4) can then be written very simply as:
$$
\boxed{\frac{DU^\mu}{D\tau}=\frac{f_{\rm ng}^\mu}{m}}
$$ 
This equation, written this way, strongly recalls the fundamental principle of dynamics, but places mechanics in a relativistic framework, invariant under any change of coordinate system and in the presence of gravitation. The notion of covariant derivative is therefore well suited to General Relativity calculations and properly replaces the usual derivative in this framework.

In general, replacing the usual derivatives of a physical theory with covariant derivatives leads to a formulation of physical laws that respects the equivalence principle, thus achieving invariance under reference frame changes and in the presence of gravitation. If a theory is true without gravitation and locally in Minkowski space, then it remains true in any reference frame with gravitation. For example, in the absence of gravitational field, Maxwell's equations are written:
$$
\frac{\partial F^{\alpha\beta}}{\partial x^\alpha} = - J^\beta
$$
where $J^\beta$ is the electric current four-vector and $F^{\alpha\beta}$ is the electromagnetic tensor. If we introduce tensors $F^{\mu\nu}$ and $J^\mu$ such that they reduce to $F^{\alpha\beta}$ and $J^\beta$ in an inertial Minkowski reference frame, then electromagnetic theory respects the equivalence principle if we use the covariant derivative:
$$
F^{\mu\nu}{}_{;\mu} = - J^\mu
$$
and this formulation is valid in any coordinate system since it is true in Minkowski.

:::{note} Covariant derivative of a covariant vector

Note that for a covariant vector, the covariant derivative is written:
$$\label{eq:dcov-cov}
\frac{DV_\mu}{D\tau} \equiv \frac{\dd V_\mu}{\dd\tau} - \Gamma^\nu_{\ \mu\lambda}\frac{\dd x^\lambda}{\dd\tau} V_\nu.
$$
:::


### Toward Einstein's equation

Armed with these tools, let us now move toward a simple derivation of Einstein's equation which summarizes gravitation as a deformation of spacetime by matter. Let us begin by considering a massive particle moving slowly in a weak gravitational field, constant but arbitrary this time. According to the Equivalence Principle, we have seen that there exists an inertial coordinate system $\left(ct',\vec x'\right)$ such that the equation of motion [](#eq:eqm1) is still valid in another reference frame $\left(ct,\vec x\right)$ but with gravitational field. The assumption of low velocity allows us to neglect $\dd\vec x/\dd\tau$ compared to $c\dd t/\dd\tau$. We then have to first order in a weak and quasi-stationary gravity field:
$$
\frac{\dd^2x^\mu}{\dd\tau^2} + \Gamma^\mu_{\ 00}\left(c\frac{\dd t}{\dd\tau}\right)^2=0, \qquad \Gamma^\mu_{\;\;00} \approx -\frac{1}{2}\eta^{\mu\nu}\frac{\partial g_{00}}{\partial x^\nu}.
$$

Under the assumption of a weak gravitational field, we can adopt an almost Cartesian metric:
$$
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad \vert h_{\mu\nu} \vert \ll 1,
$$
and we obtain to first order:
$$
\left\lbrace
\begin{array}{rl}
    \mu=1,2,3\ : & \displaystyle{\frac{\dd^2\vec x}{\dd\tau^2} = \frac{1}{2}\left(c\frac{\dd t}{\dd\tau}\right)^2\vec{\nabla} h_{00} } \\
    \mu=0\ : &  \displaystyle{\frac{\dd^2 t}{\dd\tau^2} = 0.}
\end{array}
\right.
$$ 
From the second equation we deduce that $\dd t/\dd\tau$ is a constant. Therefore we can divide the first equation by $\dd t / \dd \tau$ and we obtain:
$$
\label{eq:vers_einstein}
\frac{\dd^2\vec x}{\dd t^2} = \frac{1}{2}c^2\vec{\nabla} h_{00}.
$$ 
But we know that in the Newtonian limit we have:
$$
\frac{\dd^2\vec x}{\dd t^2} = -\vec{\nabla} \phi$$
with $\phi$ the gravitational potential (i.e. $\phi=-\GN M /r$ if generated by a mass $M$ at distance $r$, $\GN$ being Newton's constant). Comparing with [](#eq:vers_einstein), we have $h_{00}=-2\phi/c^2+\text{constant}$. But the metric must be Minkowski at infinity (weak perturbation assumption), therefore $h_{00}=-2\phi/c^2$ and:
$$
\label{eq:g00}
g_{00}=-\left(1+\frac{2\phi}{c^2}\right),
$$ 
Consequently, the spacetime metric will be able to contain gravitational effects. The element $g_{00}$ corresponding to the temporal component of the metric, the beating of clocks therefore depends on the intensity of the gravitational field. This corresponds to the Einstein effect, the only consequence of General Relativity currently used technologically (in GPS, see [](#fig:effet_einstein)).


:::{figure} ../../images/effet_eintein.svg
:name: fig:effet_einstein
:align: center
:width: 90%

Illustration of the Einstein effect. A photon falling into a gravitational well gains energy so its frequency increases. Equivalently, we can say that clocks in a gravitational field run slow compared to identical clocks located outside. GPS receivers must take this effect into account to deduce their position relative to satellites.
:::

This exercise on a point particle teaches us that the gravitational field is ultimately contained in the metric, and that this metric therefore depends on the presence of matter. It is therefore possible to imagine a generalization of this observation. The Newtonian potential is determined by Poisson's equation:
\begin{equation}\label{eq:poisson}
\nabla^2\phi = 4\pi \GN \rho_m
\end{equation}
where $\rho_m$ is the mass density and $\GN$ is Newton's constant. The latter is associated with the energy density $\epsilon$ of the matter energy-momentum tensor $T_{00} = \epsilon = \rho_m c^2 $ (see chapter [](./02_friedmann_equations.md)), so with equation [](#eq:g00) we can obtain:
$$
\nabla^2 g_{00}=-\frac{8\pi \GN}{c^4} T_{00}.
$$ 
This equation is not invariant under Lorentz transformations, hence the necessity to modify Newtonian gravitational theory if we admit the principle of special relativity. Tensors are the right objects that can allow us to achieve this goal. We can then imagine that there exists a tensor $G_{\mu\nu}$ combining first and second derivatives of the metric $g_{\mu\nu}$ generalizing this last equation to all coordinates such that:
$$
\label{eq:einstein1}
G_{\mu\nu}=-\frac{8\pi \GN}{c^4} T_{\mu\nu}.
$$ 
This last equation corresponds to a first version of *Einstein's equation*. This reasoning only allowed us to intuit its form, but another more rigorous demonstration allows us to obtain the expression of Einstein's tensor $G_{\mu\nu}$:
$$
G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R
$$
with $R_{\mu\nu}$ the Ricci tensor and $R$ the scalar curvature (trace of the Ricci tensor $R^\mu_{\;\mu}$), themselves obtained from the Riemann tensor $R^\mu_{\ \nu\alpha\beta}$:
$$
\begin{aligned}
R^\mu_{\ \nu\alpha\beta} & = -\partial_\alpha \Gamma^\mu_{\ \nu\beta} +  \partial_\beta \Gamma^\mu_{\ \nu\alpha} - \Gamma^\mu_{\ \alpha\sigma}\Gamma^\sigma_{\ \nu\beta} + \Gamma^\mu_{\ \beta\sigma}\Gamma^\sigma_{\ \nu\alpha} \\
R_{\mu\nu} & =R^\alpha_{\ \mu\alpha\nu}.
\end{aligned}
$$
*Since Einstein's tensor $G_{\mu\nu}$ contains second derivatives of the metric, Einstein's equation links the curvature of spacetime and thus the trajectories of bodies to its energy and matter content.*


Moreover, $G_{\mu\nu}$ appears to have zero divergence. This is Bianchi's identity:
$$G^{\mu\nu}_{\;\;\;;\mu}=0.$$

:::{important} Conservation of $T^{\mu\nu}$

Bianchi's identity and Einstein's equation [](#eq:einstein1) imposes energy conservation, therefore directly derived from geometric properties:
$$
\label{eq:conservation_energie_tenseur}
T^{\mu\nu}_{\;\;\;;\mu}=0
$$
:::

By Bianchi's identity, we also see that Einstein's equation can be defined up to a constant[^gmunu] while keeping energy conservation. This constant is now called the cosmological constant. Here is Einstein's equation in its final form {cite:p}`Einstein1917`:
$$\label{eq:einstein2}
\boxed{G_{\mu\nu}-\Lambda g_{\mu\nu} = -\frac{8\pi \GN}{c^4} T_{\mu\nu}}
$$


:::{important} Key Points

- General Relativity was built on the Equivalence Principle, exploiting the coincidence that is the apparent equality between gravitational mass and inertial mass.
- Physical laws must be invariant under coordinate system changes and in the presence or absence of gravitation, which becomes an integral part of the spacetime metric.
- The geodesic equation is the GR equivalent of Newton's second law, while Einstein's equation is the equivalent of Poisson's equation of Newtonian gravitation.

:::

:::{seealso} To Go Further

- History of gravitation and founding experiments: {cite:t}`Weinberg1972`[chap.1]
- Demonstration of Lorentz transformations: {cite:t}`raimond` or J.M Levi-Leblond <doi:10.1119/1.10490> https://web.physics.utah.edu/~lebohec/P3740/levy-leblond_ajp_44_271_76.pdf 
- Metric and simple examples: {cite:t}`langlois2013RG`
- Covariant derivative: {cite:t}`Weinberg1972`[chap.4]
- Einstein effect and GPS: {cite:t}`Gourgoulhon2013` 

:::



[^tau]: Through this definition, we have chosen a metric signature $(-,+,+,+)$ which we will keep throughout.

[^x0]: Hereafter, the index $0$ of tensors will correspond to the temporal coordinate, while the following indices will correspond to spatial coordinates.

[^linearity]: Linearity is imposed by the invariance of physics under translation in space and time {cite:p}`raimond`.

[^inv]: Knowing that $\frac{\partial x'^\rho}{\partial x^\mu} \frac{\partial x^\mu}{\partial x'^\nu} = \delta^\rho_\nu$, because $\frac{\partial x'^\rho}{\partial x^\mu}$ is the Jacobian of the coordinate transformation $x^\mu \to x'^\nu $ and the second factor is its inverse.

[^2prime]: If studying a massless particle, it suffices to replace $f_{\rm ng}^\mu/m$ by the model of the interaction applying to this particle.

[^gmunu]: Because we also have $g^{\mu\nu}{}_{;\mu}=0$.

## References

{bibliography}