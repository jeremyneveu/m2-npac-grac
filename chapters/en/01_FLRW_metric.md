---
short_title: Metric FLRW
authors:
  - jneveu
keywords: FLRW, cosmological principle, comoving, coordinates
---


The Friedmann-Lemaître-Robertson-Walker metric
================================


Cosmological principle
-----------------------



:::{iframe} https://www.youtube.com/embed/UTlYUxucEZA?si=WZpcAuL1ElZuyvf6
:name: fig:sdss
:align: center
:width: 60%

Galaxy distribution compiled by the eBOSS survey. Every dot in this “pie” diagram is a galaxy, color coded by type: green for nearby galaxies, magenta and red for old red galaxies, blue for young blue galaxies, yellow and white for quasars. Credit: A. Raichoor (EPFL) / A. Ross (Ohio State Univ.) / SDSS Collaboration
:::

:::{figure} ../../images/CMB_planck.jpg
:name: fig:cmb_planck
:align: center
:width: 70%

Temperature map of the Cosmic Microwave Background (CMB) observed by the Planck satellite. The relative difference observed between the  temperature of hot (red) and cold (blue) spots relative to the mean the mean is of the order of $\delta \theta / \theta \approx 10^{-5}$.
:::

To be able to build a model of the Universe, i.e. a theoretical construct capable of describing the contents of the Universe and its evolution, we need to be able to Einstein's equation of General Relativity. But how much detail is needed to describe the Universe sufficiently well on large scales? Parametrizing Einstein's equation to include the scale of the solar system is both illusory and unnecessary. What is the the structure of the Universe on larger scales? Here, nature has given us a wonderful gift, which will considerably simplify the writing of a cosmological model based on the equations of General Relativity. of General Relativity.

:::{important} Cosmological principle

At sufficiently large scales, the universe is spatially homogeneous and isotropic.
:::

1. the Universe is homogeneous: the metric therefore does not depend on an observer's position in space, so no position is particular in the Universe. This assertion, based on the Copernican principle, is only statistically true, as we can observe that matter has formed lumps (planets, stars, galaxies, etc.) in the middle of large voids. However, observation of the Universe on large scales shows that the Universe is indeed globally homogeneous on scales larger than $100\,$Mpc[^pc] (see [](#fig:sdss) and for example {cite:t}`Scrimgeour2012` for a measure of the Universe's homogeneity by counting galaxies).

2. the Universe is isotropic: no direction is privileged. This means that observations made in two different directions across the sky are equivalent. This is well verified by observations of the cosmic microwave background (CMB), whose temperature is measured to be identical at $2.725pm0.002\,$K in all directions of space {cite:p}`Mather1999`. Only temperature fluctuations of the order of $10^{-5}$\,K are detected in this image of the young Universe (see [](#fig:cmb_planck) and for example {cite:t}`ThePlanckCollaboration2013XIII` for a verification of the isotropy principle using the Sunyaev-Zeldovich effect).

Completely ignoring what happens at “insufficiently” large scales is the first step towards building a cosmological solution to General Relativity. Armed with these observational facts, we will impose homogeneity and isotropy on the metric and distribution of matter (i.e. the energy-impulsion tensor).

:::{note} About the homogeneity of the Universe
:class: dropdown 

Before presenting this cosmological solution, it's worth asking why the cosmological principle should apply. While gravity, the dominant force shaping the large-scale structures of the universe, tends to destroy homogeneity (a slightly over-dense region in a homogeneous universe will attract matter and become increasingly over-dense), it takes longer for matter at large scales to form lumps. Since large scales appear to be more homogeneous in observations, we can assume that the universe was much more homogeneous in the past at all scales, and is becoming less so under the action of gravity. But why was it originally homogeneous? One logical answer is that an interaction other than gravity contributed to it (as, for example, pressure in a perfect gas). However, General Relativity stipulates that no interaction can propagate faster than the speed of light. We'll see that in a theory where the evolution of the universe stems from an initial Big Bang, this creates a potential difficulty: homogenization should only be possible up to scales equal to the distance traveled by a photon between the Big Bang and today.
:::


Universe of maximum symmetry
------------------

Given the cosmological principle, we seek to determine the form that the metric of a Universe of maximum symmetry must take, i.e. a Universe whose properties are invariant by rotation and translation {cite:p}`Weinberg1972`[p. 379].


### Metric of an isotropic Universe

:::{figure} ../../images/foliation.svg

The space-time diagram of a homogeneous, isotropic Universe has a time axis orthogonal to the spatial base vectors, due to the isotropy of the Universe. Each hypersurface at time $t$ is then a Universe of homogeneous density.
:::


First of all, if the Universe is isotropic, we can check that the crossed components $g_{i0}$ and $g_{i0}$ are zero. If this were not the case, we would have a privileged direction in the universe. We can convince ourselves of this by noticing that these components are non-zero if we perform a Lorentz transformation [](#eq:lorentz)-[](#eq:lorentz2), precisely when we take a frame of reference in uniform translation with respect to another, thus moving in a chosen direction. 

Another way of convincing ourselves is to consider a 2D spacetime. If the metric has the form :
\begin{equation}
g=\begin{pmatrix} g_{00} & g_{01} \\\ g_{01} & g_{11} \end{pmatrix}
\end{equation}
then the equation for light-like trajectories is :
$$
\dd s^2=0=g_{00}c^2\dd t^2+2g_{01},c\,\dd x\,\dd t+g_{11}\dd x^2.$$
We can then check, by solving the second-degree equation in $\dd t$ that if $g_{01} \neq 0$, two opposite $\dd x$ give two different values of positive $\dd t$. In other words, an observer will receive at different times the light pulses emitted simultaneously by two sources located at the same distance in opposite $\pm \dd x$ directions. This obviously breaks isotropy. The $g_{0i}$ and $g_{i0}$ terms of the metric are therefore zero. This means that the time vector $\vec e_0$ is orthogonal to the spatial basis vectors $\vec e_i$.


What's more, if the Universe is homogeneous, then the $g_{00}(t,\vec x)$ component can only depend on time $t$, so that clocks do not depend on position in space. So $g_{00}(t,\vec x) = g_{00}(t)$ {cite:p}`Weinberg1972`[p. 403]. If we call the parameter $t$ time, we see that we have a universal time at every point in space, called cosmological time. Since the Universe is homogeneous, this means that each date can be associated with a density of matter or energy that is identical for all observers, so that with a densimeter we can construct a clock common to all observers present in the Universe. 

Combining the two previous results, the space-time interval can be written in the following form:
\begin{equation}
\dd s^2= g_{00}(t) c^2 \dd t^2 + \dd \vec l^2
\end{equation}
where $\dd \vec l$ is an elementary space vector. It is then possible to set $g_{00}$ to $-1$, even if it means redefining the variable time[^g00]. The metric thus takes the form :
\begin{equation}
g_{\mu\nu}=\begin{pmatrix} -1& 0 & 0 & 0\\
 0 & \gamma_{11} & \gamma_{12} & \gamma_{13} \\ 
0&\gamma_{12} & \gamma_{22} & \gamma_{23} \\ 
0&\gamma_{13} & \gamma_{23} & \gamma_{33} 
\end{pmatrix}
\end{equation}
where $\gamma_{ij}$ is the spatial metric, which can depend on time and position, and has 6 independent unknown components (a metric is a symmetrical tensor).

:::{attention} Signature convention for the metric

In this course, as in many cosmology courses, the [signature](https://en.wikipedia.org/wiki/Metric_signature) chosen for the metric is $(-,+,+,+)$. Indeed, in cosmology we manipulate distances a lot, so it's more convenient to have positive length elements. In theoretical high-energy physics, the $(+,-,-,-)$ metric is often preferred. A compilation of the different signatures used is presented [here](https://en.wikipedia.org/wiki/Sign_convention).

:::


### Geometry of a maximally symmetrical Universe

Now let's find an explicit form for $\dd \vec l^2$. A maximally symmetrical Universe (homogeneous and isotropic) must have spatially constant curvature. This is fairly intuitive, but can also be demonstrated in General Relativity {cite:p}`Weinberg1972` [p. 381]. Let $a$ be the associated radius of curvature, and let $\vec \xi = (\xi^1, \xi^2, \xi^3)$ be a position vector in 3D space:
\begin{equation}
\dd \vec l^2 = \gamma_{ij} \dd \xi^i \dd \xi^j, \quad \text{with}\quad i=1,2,3
\end{equation}


First of all, if this space has zero curvature, then the elementary distance $\dd \vec l$ is simply written :
\begin{equation}
\dd \vec l^2 = \delta_{ij} \dd \xi^i \dd \xi^j,\quad \gamma_{ij} = \delta_{ij}
\end{equation}

Now let's work on the case where the curvature is non-zero. To describe the curvature of a surface with the usual geometric notions, let's study it in a space with an extra dimension. Let's place this non-Euclidean (curved) 3D space in a 4D space of metric $C_{AB}$ with Cartesian coordinates $(x, y, z, w)$. Let $r^2 = x^2 + y^2 + z^2$ be the Euclidean distance in the 3D subspace. We then have two possible 3D hyper-surfaces, of constant Gaussian curvature $1/a^2$ {cite:p}`Baumann` :
- a 3-sphere of radius $a$ if immersed in a 4D Euclidean space: 
\begin{equation}
\quad C_{AB} = \mathrm{diag}(1,1,1,1), \quad r^2 + w^2= a^2,\quad \dd \vec l^2 = \dd r^2 + \dd w^2
\end{equation}
- a 3-hyperboloid of curvature $a$ if it is immersed in a 4D Lorentzian space:
\begin{equation}
 \quad C_{AB} = \mathrm{diag}(1,1,1,-1),\quad r^2 - w^2= -a^2,\quad \dd \vec l^2 = \dd r^2 - \dd w^2
\end{equation}

:::{figure} ../../images/sphere_euclid.svg

2D spherical space of radius $a$ represented in a 3D Euclidean space $(x,y,w)$. At a coordinate $\vec \xi = (\xi_1, \xi_2)$, we wish to express the length of an elementary vector tangent to the sphere $\dd \vec l$ in both spaces.
:::

The last two cases of strictly positive or negative curvature are therefore defined by *the constraint equation* :
:::{math}
:label: eq_hyp_sph
r^2 \pm w^2= \pm a^2(t) 
:::
where here we allow the radius $a(t)$ to depend on time, since a priori $\gamma_{ij}$ can depend on time.

:::{tip} Notion of curvature
:class: dropdown

If you're confused by this reasoning, remember that it's like describing the curvature of a circle of radius $R$. A circle is a one-dimensional object, as there is only one direction of motion on it (parametrized by an angle $\theta$, for example). But it can also be described in a 2D plane, with two coordinates $x$ and $y$ linked by the equation :
\begin{equation*}
x^2 + y^2 = R^2
\end{equation*}
Similarly, a sphere (a two-dimensional object) can be studied in a space with a third dimension, i.e. three coordinates $(x,y,z)$ linked by the equation:
\begin{equation*}
x^2 + y^2 + z^2 = R^2
\end{equation*}

The notion of curvature can be calculated either intrinsically or using an additional dimension. Intrinsically, a living being on a circle can measure its curvature by measuring the distance covered during one revolution: it will deduce that the curvature of its circle is $1/R^2$ with $R$ deduced from the perimeter covered $l = 2\pi R$. If he's able to leave the circle and travel in a second dimension, he'll be able to observe his circle from the outside and measure the curvature of his Universe too.

:::

The infinitesimal distance $\dd \vec l^2$ between two points of the hypersurface defined in curved 3D space of metric $\gamma_{ij}$ must be identical to that measured in 4D space, so :
\begin{equation}
\dd \vec l^2= \gamma_{ij} \dd \xi^i \dd \xi^j = \dd r^2 \pm \dd w^2
\end{equation}
where the $+$ case corresponds to spherical geometry, the $-$ case to hyperbolic geometry {cite:p}`Weinberg1972` [p. 390-391].

However, the closure equation [](#eq_hyp_sph) links $r, w$ and $a$, so we can replace $\dd w$ by an expression that is a function of $r$ and $a$ (i.e. without the fourth dimension). Differentiating equation [](#eq_hyp_sph) gives the relation 
$$
(\vec r \cdot \dd \vec r) \pm w\dd w=0,$$
so, injecting equation [](#eq_hyp_sph) again, we obtain :
\begin{equation}
(\vec r \cdot \dd \vec r)^2=(w\dd w)^2 \Rightarrow (\dd w)^2= \frac{(\vec r \cdot \dd \vec r)^2}{w^2} = \frac{(\vec r \cdot \dd \vec r)^2}{a^2(t) \mp r^2}
\end{equation}
The infinitesimal distance between 2 points in non-Euclidean 3D space of constant non-zero curvature $a^{-2}$ is then :
\begin{equation}
\dd \vec l^2= \dd \vec r^2 \pm \frac{(\vec r \cdot \dd \vec r)^2}{a^2(t)\mp r^2} 
\end{equation}

At this stage, we can now combine the result obtained for the two non-zero curvatures with the Euclidean case by introducing the *parameter of curvature* $k$ :
\begin{equation}
\label{K-def}
k = \left\lbrace
\begin{array}{rl}
 +1 & \text{3-sphere} \}
 0 & \text{flat space} \text
 -1 & \text{3-hyperboloid} \\
\end{array}\right.
\end{equation}
For the three possible geometries[^flat] of a maximally symmetrical Universe, we have :
\begin{equation}
\dd \vec l^2= \dd \vec r^2 + k\frac{ (\vec r \cdot \dd \vec r)^2}{a^2(t) - k r^2}
\end{equation}
where in the case of a flat space we'd have $\vec r = \vec \xi$.

Finally, let's introduce the rescaled variable $\vec\sigma=\vec r/a(t)$, and we get a new expression:
\begin{equation}
\dd \vec{l}^2= a^2(t) \left(\dd \vec{\sigma}^2 + k\frac{(\vec{\sigma} \cdot \dd \vec{\sigma})^2}{1 - k \sigma^2} \right)
\end{equation}

The Friedmann-Lemaître-Robertson-Walker metric describing a homogeneous, isotropic Universe is finally written :
\begin{equation}
\label{FLRW-metric}
\dd s^2=-c^2\dd t^2 + a^2(t) \left(\dd \sigma^2 + k\frac{(\sigma \cdot \dd \sigma)^2}{1 - k \sigma^2} \right)
\end{equation}

The Friedmann-Lemaître-Robertson-Walker (FLRW) metric is the basic framework of the Standard Cosmological Model. The assumptions of homogeneity and isotropy led directly to a metric describing a universe with only three possible geometries (flat, 3-sphere, 3-hyperboloid) and a scaling factor $a(t)$ affecting distances. Note that, thanks to the imposition of homogeneity and isotropy symmetries, we have reduced the writing of the metric $g_{\mu\nu}$ (which is a symmetric tensor) consisting a priori of 10 unknown independent components to a tensor with a single unknown function $a(t)$.


:::{important} Where are the units?
The distance element $\dd s$ has the dimension of a length, so do all the terms in equation [](#FLRW-metric). 

Some works propose that the scale factor is a dimensionless function of time, and that $\sigma$ retains the dimension of a length, normalized by $a(t)$. This makes it possible to define everything, in particular by assuming that today the scale factor is $a_0=1$, but then we need to redefine $k$ and give it the unit of curvature (inverse of distance squared).

In this course, we'll be dealing extensively with distances in cosmology, and in this case it's more convenient to think of the scale factor as homogeneous to a length, and the spatial coordinates $\vec \sigma$ as a dimensionless vector. The curvature parameter $k$ is then also a dimensionless integer.

:::


It's important to understand the physical significance of the expansion factor $a(t)$. First of all, according to equation [](#FLRW-metric), this factor relates the physical distance $\vec r$ and the coordinate distance $\sigma$ by $\vec r=a(t)\vec \sigma$. A particle with fixed spatial coordinates $\vec \sigma$ will see its physical distance from an observer in $\vec \sigma=\vec 0$ increase (or decrease) with time. This variation in distance is achieved at apparent speed:
$$
\frac{\dd \vec r}{\dd t} = \frac{\dd a(t)\vec \sigma}{\dd t} = \dot a \vec \sigma + a \dot{\vec \sigma} = \frac{\dot a}{a} \vec r
$$
because $\dot{\vec \sigma} = \vec 0$ if the particle has no motion of its own, with the point $\;\dot{}\;$ expressing a derivative with respect to time $t$. We thus obtain a direct relationship between distance from a central observer and apparent velocity: this is Hubble's law. The distance rate is given by the Hubble parameter, which quantifies the rate of change of the scale factor: 
\begin{equation}
\label{eq:H-def}
\boxed{\displaystyle H(t) = \frac{\dot a(t)}{a(t)}}
\end{equation}

For a spherical universe, the scale factor $a(t)$ also represents its radius of curvature. A dynamic spherical universe therefore corresponds to a universe with a time-varying radius of curvature. A flat space has no characteristic scale, so the value of $a(t)$ is not a physical observable. The physically meaningful quantity for such a universe is the Hubble parameter $H(t)$.

To simplify notation, the time dependence of the parameters is not always made explicit, so $a(t)=a$. Parameters evaluated at the present time $t_0$ are designated by the subscript or exponent 0, so that $a(t_0)=a_0$. In the following, we'll work in the system where $a_0$ *isn't fixed* at 1. 

:::{list-table} Representation of the two-dimensional equivalents of the three solution spaces of cosmological principles: the 2-sphere, the plane, the 2-hyperboloid.
:header-rows: 0
:name: fig:spaces

* - :::{image} ../../images/sphere.jpeg
    :alt: sphere
    :width: 95%
    :align: center
    :::
  - :::{image} ../../images/plan.jpeg
    :alt: plan
    :width: 100%
    :align: center
    :::
  - :::{image} ../../images/hyperboloid.jpeg
    :alt: hyperboloid
    :width: 90%
    :align: center
    :::
:::

:::{note} What does it mean to live in a curved space?

The [](#fig:spaces) represent 2D surfaces immersed in 3D spaces. But how can we imagine living in a 3-sphere? And what does this imply? Living in a curved space means that the sum of the angles of a triangle is not equal to 180°: it's greater for a 3-sphere and less for a 3-hyperboloid. Thus, the two blue triangles [](#fig:triangles_on_sphere) have a sum of angles greater than 180°. In a 3-sphere, we may have the impression that two objects are angularly distant, when in fact the distance separating them is smaller than it would be in flat space. And this is true in every direction of space. 

In short, living in a curved space means that the relationship between angles and lengths is distorted in relation to our Euclidean intuition, at least at cosmological distances.


```{figure}../../images/triangles_on_sphere.svg
:name: fig:triangles_on_sphere 
:align: center

Take two galaxies: they form a triangle with the Earth, which, in a 3-sphere, has three angles whose sum is greater than 180°. 
```

:::

Comobiles coordinates
---------------------

It's important to note that not all observers see the Universe as isotropic, but only so-called *mobile* observers, who are locally at rest with most of the matter in their vicinity. We, for example, are not mobile observers: when we observe the temperature of the CMB, the first feature we see is a large temperature dipole (warmer on one side, colder on the opposite side), which is the result of the particular motion of our solar system in the galaxy, and of our galaxy in the Universe (and of our group of galaxies). If we were to subtract this own motion from the CMB frame of reference, then we would be comoving observers. Thus, we can define a coordinate system associated with observers without proper motion, whose relative proper distances increase only with the scaling factor $a(t)$ {cite:p}`Weinberg1972`[p. 409].

In the FLRW metric, where the expansion of the Universe is factorized by a scale factor $a(t)$, the spatial coordinates $\vec \sigma$ are called *comoving coordinates*. There is considerable freedom in the choice of comoving coordinates. 

### Spherical coordinates

We often prefer spherical coordinates $(ct, \sigma, \theta, \phi)$ with the observer (ourselves) at the origin, such as :
\begin{equation}
\begin{aligned}
\sigma_1 &= \sigma \sin \theta \cos \phi \\
\sigma_2 &= \sigma \sin \theta \sin \phi \\
\sigma_3 &= \sigma \cos \theta
\end{aligned}
\end{equation}
After some simple but lengthy calculations (see notebook and [here](`https://en.wikipedia.org/wiki/Spherical_coordinate_system#Integration_and_differentiation_in_spherical_coordinates`)), in all three cases of curvature the FLRW metric is written :
\begin{equation}
\label{eq:FLRW-metric-spherical}
\dd s^2=-c^2\dd t^2 + a^2(t) \left( {1 \over 1-k\sigma^2}\dd \sigma^2 + \sigma^2 \dd \theta^2 + \sigma^2 \sin^2 \theta \dd \phi^2\right)
\end{equation}

:::{note} Curvature and finitude of the Universe
:class: dropdown

For the 3-sphere, 3-hyperboloid and the plane, the curvature of these surfaces is {cite:p}`Weinberg1972`[p. 412]:
$$ K(t) = \frac{k}{a^2(t)}$$
The 3-hyperboloid and the plane have infinite extension. On the other hand, the 3-sphere has finite extension, but remains unbounded: a particle will never encounter an edge 
but a volume can be defined:
$$V(t) = 2 \pi^2 a^3(t)$$
and a perimeter (length of a meridian):
$$L(t) = 2 \pi a(t)$$
:::


### Cartesian coordinates

The flat-universe case greatly simplifies the calculations that follow. Since the assumption of zero curvature is compatible with the ever-stricter constraints of cosmological observations, we will henceforth concentrate our analytical developments on the flat universe, mentioning results for the general case where necessary. In the case of zero curvature, it may be convenient to use Cartesian comoving coordinates $(ct, x, y, z)$, such as :
\begin{equation}
\sigma_1 = x,\quad \sigma_2 = y,\quad \sigma_3 = z,\quad \sigma^2 = x^2 + y^2 + z^2
\end{equation}
The FLRW metric is written in a flat universe:
\begin{equation}
g_{pmatrix} = 
\begin{pmatrix}
-1 & 0 & 0 & 0 \\ 
0 & a^2(t) & 0 & 0\\
0 & 0 & a^2(t) & 0 \\
0 & 0 & 0 & a^2(t)
\end{pmatrix}
\end{equation}

Geodesics in FLRW metric
---------------------------------

What is the trajectory of a free-falling particle in an FLRW metric? From General Relativity, we know that such a particle moves along a geodesic $x^\mu(s)$ whose equation is as follows:
\begin{equation}
\label{geodesic}
{\dd^2 x^\mu \over \dd s^2} +\Gamma^{\mu}_{\,\,\nu\kappa} {\dd x^\nu \over \dd s}{\dd x^\kappa \over \dd s}=0,
\end{equation} 
where $s$ is any parameter describing the position along the geodesic (e.g. proper time). Another form of the geodesic equation will help us here, obtained from the definition of the covariant derivative [](#eq:dcov-cov):
\begin{equation}
\label{geodesic-cov}
{\dd^2 x_\mu \over \dd s^2} -\Gamma^{\nu}_{\,\,\mu\kappa} {\dd x_\nu \over \dd s}{\dd x^\kappa \over \dd s}=0.
\end{equation} 
Let's define the quadri-velocity $U^\mu$ along a Universe line by $U^\mu = \dd x^\mu / \dd s$. Then :
\begin{equation}
{\dd U_\mu \over \dd s} = \Gamma^{\nu}_{\,\,\mu\kappa} U_\nu U^\kappa= \frac{1}{2} \frac{\partial g_{\alpha\beta}}{\partial x^\mu} U^\alpha U^\beta.
\end{equation} 

:::{note} Demonstration
:class: dropdown

The preceding equality is demonstrated in {cite:t}`hobson2006general`[p. 81]. Here is the gist of it:
\begin{align*}
\Gamma^{\nu}_{\,\,\mu\kappa} U_\nu U^\kappa
& = \frac{1}{2}g^{\lambda\nu}\left( \frac{\partial g_{\lambda\kappa}}{\partial x^\mu} + \frac{\partial g_{\mu\lambda}}{\partial x^\kappa} - \frac{\partial g_{\mu\kappa}}{\partial x^\lambda} \right) U_\nu U^\kappa \\\\\
& = \frac{1}{2}\left( \frac{\partial g_{\lambda\kappa}}{\partial x^\mu} + \frac{\partial g_{\mu\lambda\kappa}}{\partial x^\kappa} - \frac{\partial g_{\mu\kappa}}{\partial x^\lambda\kappa}{\partial x^\lambda} \right) U^\lambda U^\kappa  
= \frac{1}{2} \frac{\partial g_{\lambda\kappa}}{\partial x^\mu} U^\lambda U^\kappa
\end{align*}
because the metric is a symmetrical tensor so ${\partial_\kappa g_{\muambda}} - {\partial_\lambda g_{\mu\kappa}} = $0.
:::

From this form of the geodesic equation (see {cite:p}`hobson2006general`[p. 81] for a demonstration), let's calculate the form that the contravariant vector $U^\nu$ must take in a FLRW metric for a particle in free fall.

Let's start with the case $\mu=3$ and use the spherical coordinates $(\sigma,\theta,\phi)$. Since the FLRW metric does not depend on $\phi$, then :
$$
\frac{\dd U_3}{\dd s} = 0
$$
so $U_3$ is a motion constant. Furthermore:
$$
U_3 = g_{33} U^3 = a^2(t) (\sigma \sin \theta)^2 U^3 $$
whose expression cancels at the origin at $\sigma=0$, where we observe. Since the $U_3$ component is constant, it is identically zero along the trajectory. We deduce:
$$U^3 = \frac{\dd \phi }{ \dd s} = 0 \Rightarrow \phi = \text{constant}$$.

Let's move on to the $\mu=2$ case. The only component of the metric depending on $\theta$ is 
$g_{33}$ but $U_3$ is identically zero, so :
$$frac{\dd U_2}{\dd s} = \frac{1}{2} \frac{\partial g_{\alpha\beta}}{\partial x^2} U^\alpha U^\beta = \frac{1}{2} \frac{\partial g_{33}}{\partial x^2} U^3 U^3 = 0.$$
In the same way, we also have :
$$U_2 = g_{22} U^2 = a^2(t) \sigma^2 U^2 $$
which cancels out at $\sigma=0$, so $U^2$ is zero all along the trajectory. From this we deduce:
$$U^2 = \frac{\dd \theta }{ \dd s} = 0 \Rightarrow \theta = \text{constant}$$

:::{important}
In spherical coordinates, the geodesics passing through the origin are the trajectories verifying :
$$
\boxed{\theta=\text{constant},\quad \phi=\text{constant}}
$$
:::


Spectral shift, or redshift
----------------------------------


:::{figure} ../../images/distances2.svg
:name: fig:distances_croquis
:align: center
:width: 60%

Notations for calculating redshift and cosmological distances in comoving coordinates.
:::

To measure the expansion history of the Universe, we need access to the scale parameter $a(t)$. This is made possible by measuring the spectral shift of light coming from distant sources. In the FLRW metric, let's place ourselves by convention at the center ($\sigma=0$), and consider an object located at comoving coordinates $\left(\sigma_E,\theta_E,\phi_E\right)$, emitting a photon at time $t_E$ (see [](#fig:distances_croquis)). For this photon, traveling at the speed of light, in the FLRW metric we have, at any instant:
:::{math}
:label: eq:ds2_lumiere

\dd s^2=0=-c^2 \dd t^2+\frac{a^2(t)}{1-k\sigma^2}\dd \sigma^2.
:::
because along its geodesic $\theta$ and $\phi$ are constant ($\dd \theta = \dd \phi=0$). Let's assume $t_0$ is the instant of reception of this wave at $\sigma=0$. Then, thanks to the previous equation, we have the relation : 
:::{math}
:label: eq:comoving

\int_{t_E}^{t_0} \frac{c\dd t}{a(t)} = -\int_{t_0}^{t_E} \frac{c\dd t}{a(t)} = \int_0^{\sigma_E}\frac{c\dd\sigma}{sqrt{1-k\sigma^2}} = \left\lbrace
\begin{array}{cl}
    \sigma_E & \text{ si } k=+1 \arcsin
    \sigma_E & \text{ si } k=0 \\
    \text{arcsh},\sigma_E & \text{ si } k=-1 
\end{array}
\right. .
::: 
with $\dd \sigma < 0$ for $\dd t > 0$ considering a photon going from the source to the observer in 0.


For an electromagnetic wave with period $T$, the expression [](#eq:ds2_lumiere) being valid at any instant, we can calculate the same integral for the wave emitted at instant $t_E+T_E$ and received at instant $t_0+T_0$ (we assume that the period $T$ will vary with time): 
$$
\label{eq:comovingT}
\int_{t_E+T_E}^{t_0+T_0} \frac{c \dd t}{a(t)}= \int_0^{\sigma_E}\frac{\dd \sigma}{1-k\sigma^2}.
$$
Equating the expressions [](#eq:comoving) and [](#eq:comovingT), since the period $T$ is small compared to the variations in the scale factor $a(t)$ for usual electromagnetic waves, we obtain: 
$$
\begin{aligned}
\int_{t_E+T_E}^{t_0+T_0} \frac{c\dd t}{a(t)} & =\int_{t_E}^{t_0} \frac{c\dd t}{a(t)}  
\Leftrightarrow \int_{t_E+T_E}^{t_E} \frac{c\dd t}{a(t)} =\int_{t_0+T_0}^{t_0} \frac{c\dd t}{a(t)} \\
\Leftrightarrow \frac{cT_0}{a(t_0)} & = \frac{c T_E}{a(t_E)}  
\Leftrightarrow \frac{\lambda_0}{\lambda_E} = \frac{a(t_0)}{a(t_E)}{eq:redshift2}
\end{aligned}
$$
Directly, if space is expanding, then $a(t_E) < a(t_0)$ and the received wavelength $\lambda_0$ is therefore greater than the transmitted wavelength $\lambda_E$. We then define the spectral shift, commonly called _redshift_ due to the fact that almost all observed galaxy spectra are redshifted, as :
:::{math}
:label: eq:redshift

 \fbox{$ \displaystyle{z = \frac{\lambda_0-\lambda_E}{\lambda_E} \Leftrightarrow 1+z = \frac{a_0}{a(t_E)}} $}.
:::
The spectral shift is both directly related to the scaling parameter $a(t)$, and to an experimental quantity that can be directly measured on the emission spectrum of distant objects. Indeed, by looking at the position of the absorption and emission lines of distant objects, we can deduce their spectral shifts relative to the same chemical elements located on Earth, at rest. This experimental data is therefore often associated with the definition of distances in cosmology.


:::{exercise} Measuring redshift
:label: exo:redshift

Calculate the redshifts of the two galaxies whose spectra are shown below.
The $H\beta$ line of hydrogen (from the Balmer series) is measured at $486.1\,$nm in the rest frame of the atom.

```{list-table}
:header-rows: 0
:name: fig:redshifts

* - :::{image} ../../images/spectra_galaxy.png
    :alt: sphere
    :width: 95%
    :align: center
    :::
* - :::{image} ../../images/spectra_galaxy2.png
    :alt: plan
    :width: 100%
    :align: center
    :::
```

:::


:::{solution} exo:redshift
:class: dropdown

For the first galaxy spectrum, the $H\beta$ line is emitted at $\lambda_E = 4861\,$Å and measured at $\lambda_0\approx 5100\,$Å, so the galaxy's redshift is :
\begin{equation}
z = \frac{\lambda_0-\lambda_E}{\lambda_E} = \frac{5100-4861}{4861} = 0.049
\end{equation} 
 
For the second galaxy spectrum, the $H\beta$ line is measured at $\lambda_0\approx 5000\,$Å so the redshift of the galaxy is :
\begin{equation}
z = \frac{\lambda_0-\lambda_E}{\lambda_E} = \frac{5000-4861}{4861} = 0.028
\end{equation}

:::



Proper distance and comoving distance
------------------------------

*Proper distance* defines the physical distance between two objects at a time $t$. 
Let a transmitting object be located at comoving coordinates $(\sigma_E, \theta_E, \phi_E)$. By definition, the proper distance between this object and an observer located at the origin is along a curve at constant $\theta$ and $\phi$ and is equal to :
:::{math}
:label: eq:dist-prop

D_p(\sigma_E, t) = \int_0^{\sigma_E}
 \sqrt{g_{\sigma\sigma}}\dd\sigma' = \int_0^{\sigma_E}\frac{a(t)\dd\sigma'}{\sqrt{1-k\sigma'^2}} = a(t) \chi(\sigma_E)
:::
where $\chi(\sigma_E)$ is the _distance comoving_ between this object and the observer:
:::{math}
:label: eq:dist-comoving

\chi(\sigma_E) = \int_0^{\sigma_E}\frac{\dd\sigma'}{\sqrt{1-k\sigma'^2}} = \left\lbrace\begin{array}{cl}
    \arcsin\sigma_E & \text{ si } k=+1 \\
    \sigma_E & \text{ si } k=0 \\
    \text{arcsh},\sigma_E & \text{ si } k=-1 
\end{array}
\right.
:::
We can see that the proper distance $D_p$ has the unit of a length, whereas the comoving distance is dimensionless. The latter represents distance in coordinate space and is independent of the expansion of the Universe. The proper distance, on the other hand, evolves over time with the scale factor.

Reciprocally, we define $f_k(\chi)$ as follows:
\begin{equation}
\sigma = f_k(\chi) = \left\lbrace\begin{array}{cl}
    \sin\chi & \text{ si } k=+1 \\
    \chi & \text{ si } k=0 \\
    \sinh\chi & \text{ si } k=-1 
\end{array}
\right.
\end{equation}

Now let's imagine that this distance can be perceived through the journey of a photon. Light travels along a geodesic, so in the FLRW metric we have $\dd \theta=\dd \phi=0$ and :
\begin{equation}
\dd s^2=0=-c^2 \dd t^2+\frac{a^2(t)}{1-k\sigma^2}\dd\sigma^2.
 \end{equation} 
Therefore:
$$
\frac{\dd\sigma}{\sqrt{1-k\sigma^2}} = - \frac{c \dd t}{a(t)}
$$ 
with the photon traveling along the direction $\dd \sigma<0$ for $\dd t > 0$. The comoving distance is rewritten as
\begin{equation}
\chi(\sigma_E) = \int_0^{\sigma_E}\frac{\dd\sigma}{\sqrt{1-k\sigma^2}} = \int_{t_0}^{t_E} -\frac{c\dd t'}{a(t')}= \int_{t_E}^{t_0} \frac{c\dd t'}{a(t')} = \chi(t_E)
\end{equation}
Let's express this distance in terms of the redshift $z$, which, as we all know, is an experimental observable. Integrals can be transformed between the variables $t$, $a$ by defining the expansion rate $H(t)$, and between the variables $a$ and $z$ by defining the redshift:
\begin{equation}
H= \frac{1}{a}\frac{\dd a}{\dd t} \Rightarrow \dd t = \frac{1}{aH} \dd a
\end{equation}
\begin{equation}
a = \frac{a_0}{1+z} \Rightarrow \dd a = -a_0 \frac{\dd z}{(1+z)^2}\Rightarrow \frac{\dd a}{a} = -\frac{\dd z}{1+z}
\end{equation}
Hence the comoving distance in terms of time $t$, scale factor $a$ and redshift $z$ :
\begin{align}
\chi(\sigma_E) & = \chi(t_E) = \int_{t_E}^{t_0} \frac{c\dd t'}{a(t')} = \int_{a_E}^{a_0} \frac{c\dd a}{a^2 H(a)} \\
& = - \int_z^0 \frac{1+z}{a_0}\frac{c\dd z}{(1+z)H(z)} = \frac{1}{a_0}\int_0^z\frac{c\dd z}{H(z)} = \chi(z)
\end{align}
Table [](#tab:atz) summarizes how the parameters $a$, $t$ and $z$ are converted at different times in the chronology of the Universe.

:::{table} Conversion of parameters $a$, $t$ and $z$. Note $t_U$, the age of the Universe today.
:align: center
:label: tab:atz

|                           | a | t | z |
|---------------------------| --- | --- | --- | 
| reception (today)         | $a_0$ | $t_U$ | 0 |
| emission (past)           | $a_E$ | $t_E$ | $z$ |
| beginning of the Universe | $0$ | $0$ | $+\infty$ |
| end of time               | $+\infty$ | $+\infty$ | -1 |

:::

The proper distance is the distance that could actually be measured between two objects at time $t$. If we choose an object located at the comoving coordinate $\sigma_E$ and a comoving observer in 0, then the proper distance today at $t_0$ is simply written for the three curvature cases:
$$D_p(z) = a_0 \chi(z) =\int_0^z\frac{c \dd z}{H(z)} $$
and is expressed in units of length. The notion of proper distance is illustrated [](#fig:distances).


:::{figure} ../../images/distances.svg
:name: fig:distances
:align: center
:width: 100%

Proper distance between the Earth and a distant galaxy with no apparent proper velocity. (a) Today, the measured distance between the Earth and this galaxy is $a_0 \sigma$ light-years in flat space. (b) At another date $t$, this distance evolves to $a(t) \sigma$. (c) Proper distance in spherical space.

:::


:::{exercise} Comobiles coordinates on the sphere
:label: exo:sphere-comoving 
To get a feel for curved geometry and comoving coordinates, let's study a 2D sphere of radius $a(t)$.On this sphere, coordinates are given by the polar angle $\chi$ and the longitude $\theta$ (the $\phi$ coordinate is therefore omitted compared with the FLRW case). 
Let's consider that an observer is located at $(\chi,\theta)=(0, 0)$ and a galaxy at $(\chi, 0)$. 

1. Represent a sphere and draw the meridian $\theta = 0$. Place the following quantities: observer, galaxy, $a(t)$, $\chi$, proper distance between observer and galaxy $D_p$. Relate these quantities to the coordinate $\sigma$ and the expression for $D_p$.


2. Now consider two galaxies at the same coordinate $\chi$, separated by the physical distance $l$. Show that the angle $\theta$ under which they are observed on the sphere is $\theta = l / (a(t) \sigma)$ if $\theta \ll 1$.

:::

:::{solution} exo:sphere-comoving
:label: exo:sphere-comoving-sol
:class: dropdown

1. The comoving coordinates $\chi$ is explicitly the polar angle between the observer and the galaxy. The proper distance is the arc length, which is $D_p = a(t) \chi$ as in usual geometry. The coordinate $\sigma$ is related to the length $b$ of the chord at this angle $\chi$ by :
\begin{equation}
\sigma = \sin \chi = \frac{b}{a(t)}
\end{equation}
Note also that $b$ is the radius of the circle of colatitude $\chi$: $b = a(t) \sin \chi$. 

2. Using polar projection [](#fig:projection_polaire), we see that $\theta$ is the angle delimiting an arc of size $l$ and radius $b$, the radius of $\chi$'s latitude circle. Thus :
\begin{equation}
\theta = \frac{l}{b} = \frac{l}{a(t) \sin \chi} = \frac{l}{a(t) \sigma}
\end{equation}
Thanks to the parameterization $\sigma=f_k(\chi)$, we can see that this equality works in both flat and curved space.

If we prefer to reason mathematically rather than graphically, using the FLRW metric, we can also demonstrate :
\begin{equation}
l = \int_0^d \dd l' = \int_0^\theta \sqrt{g_{\theta\theta}} a(t)\dd\theta' = a(t) \int_0^\theta f_k(\chi) \dd\theta' = a(t) \theta \sin\chi = a(t) \theta \sigma
\end{equation}
So again we get $\theta = l / a(t) \sigma$.

It's easy to check that we have the same expressions in the flat case, and we'll admit them in hyperbolic geometry. The $\sigma$ coordinate is therefore useful for making calculations and drawings in the flat case and translating these results into the curved case (which isn't so easy with $\chi$).


```{figure} ../../images/spherical_universe.svg
:width: 100%
:align: center
:label: fig:projection_polaire
    
Geometry in a spherical universe.
```

:::



:::{warning}

Neither proper distance nor comoving distance are measurable, since they presuppose the ability to free oneself from the expansion of the Universe. In cosmology, however, we want to measure distances and their evolution in order to deduce the behavior of $a(t)$ and thus the behavior of the contents of the Universe. Traditionally, cosmology uses photons as messengers from the most distant galaxies. The observation of luminous stars can lead us to determine distances according to at least two of their aspects: luminosity and apparent size. We can thus define two distances based on the observation of luminous flux $\Phi$ and angular size $\delta$ :
$$
\Phi = \frac{L}{4\pi D_L^2}, \qquad \delta = \frac{l}{D_A}
$$
where $L$ is an object's intrinsic luminosity (in watts) and $l$ a physical size (in meters).

:::


Cosmic time and conformal time
--------------------------------

Time deserves a special mention. In our ideal Universe, with no over- or under-densities of matter, all clocks that follow expansion (i.e. with no motion of their own) beat the second at the same rate. With infinite time at our disposal to set all the clocks in the Universe, we can propose a universal convention for synchronizing our clocks. For example, when the temperature of the CMB reaches a given value, all the civilizations in the Universe can decide that this corresponds to a certain date. It is therefore possible to define a cosmic time, common to all comoving observers {cite:p}`Weinberg1972` [p. 409]. 



[^gammat]: Nothing forbids it, since $\gamma_{ij}$ can depend on time

[^g00]: We can introduce a new time variable $t'$ such that $\dd t' = \sqrt{\vert g_{00}\vert }\dd t$.

[^pc]: 1 parsec (pc) $= 3.262$ light-years $= 3.086\times 10^{16}\,$m. $100\,\text{Mpc}\approx 3\times 10^8\;$ light-years.