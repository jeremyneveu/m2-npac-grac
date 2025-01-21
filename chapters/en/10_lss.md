---
short_title: Large-scale structures in the Universe
authors:
  - jneveu
keywords: cosmological microwave background, CMB, neutrinos, nucleosynthesis
---


Formation of the large-scale structures of the Universe
===============================

Until now, we have studied the evolution of a homogeneous Universe, at least on very large scales beyond about $100\,\Mpc$. Today, however, we can see that matter is agglomerated in the form of planets, stars, galaxies, clusters of galaxies and superclusters of galaxies. The question that arises in this chapter is: how do these structures form in an expanding Universe? While the formation of the smallest stars involves many physical processes and is highly dependent on local initial conditions, it is possible to develop a simple linear model of the evolution of the largest $\sim 50\,\Mpc$ structures, such as galaxy clusters or superclusters. To do this, we simply use a Newtonian theory of linear perturbations, and calculate the evolution of these perturbations in an expanding Universe.



:::{figure} ../../images/universe_scales.svg
:width: 100%
:align: center
:label: fig:universe_scales

Scales of size and mass in the Universe.
:::


(sec-validity)=
Validity regime
-----------------------------

However, let us state the conditions necessary for the validity of the Newtonian perturbation theory. The first obvious condition is that the perturbation of the metric $g_{\mu\nu}$ and the energy-momentum tensor $T^{\mu\nu}$ must be small. In the case of non-relativistic matter, this means that the perturbations of the density $\delta \rho$ must remain small in front of the mean density $\rho_0$ i.e. $\delta \rho/\rho_0 \ll 1$. The perturbations of the gravity field $\delta \phi$ are also weak compared to the mean gravity field $\phi_0$ i.e. $\delta \phi / \phi_0 \ll 1$.

But in order to return to Newtonian gravity in a homogeneous expanding space-time and study only density perturbations, there is another condition. The size of the regions showing a deviation from the average properties of the universe (or the wavelength of the modes considered) must be much smaller than the Hubble radius $R_H={c / H}$, because in Newtonian gravity the interaction propagates instantaneously. If this is not the case, by the time the information from a collapsing region has travelled to the other side of the region, the expansion factor has changed significantly: a situation that obviously cannot be dealt with using Newtonian gravity in a homogeneously expanding space-time. 



Preamble about classical acoustics
----------

The non-relativistic matter field is described by a perfect fluid model. To look at the evolution of disturbances in a perfect fluid is to be interested in the field of acoustics. Here are a few useful concepts.

In an Eulerian description of fluids, for a fluid at rest and perfect, we define its velocity field $\vec v(t, \vec r)$, its pressure field $P(t, \vec r)$ and its mass density field $\rho(t, \vec r)$ as constant:
$$\vec v(t, \vec r)= \vec 0, P(t, \vec r) = p_0, \rho(t, \vec r) = \rho_0.$$
On top of this, we superimpose low-amplitude perturbations:
\begin{align*}
\vec v(t, \vec r) & = \vec v_0 + \delta \vec v(t, \vec r) \\
P(t, \vec r) & = P_0 + \delta P(t, \vec r) \\
\rho(t, \vec r) & = \rho_0 + \delta \rho(t, \vec r) 
\end{align*}
In acoustics, it is assumed that compressions are adiabatic and reversible, i.e. if the size of the disturbance is greater than the mean free path of the fluid particles, then heat conduction can be neglected. On the other hand, overpressure generates pressure work which changes the internal energy of a disturbance and therefore its temperature, and this work allows acoustic energy to propagate. We therefore use isentropic compressibility $\chi_S$ instead of isothermal compressibility $\chi_T$ :
$$\chi_S = -\frac{1}{V} \left.\frac{\partial V}{\partial P} \right\vert_S \approx \frac{1}{\rho_0} \frac{\delta \rho}{\delta P}.$$
We deduce the link between pressure and density perturbations via isentropic compressibility:
$$\delta \rho = \rho_0 \chi_S \delta P.$$

There is also local conservation of mass:
$$ \frac{\partial \rho}{\partial t} + \diverg \left(\rho \vec v\right) = 0 \Rightarrow \frac{\partial \delta \rho}{\partial t} + \rho_0 \diverg \delta \vec v = 0$$
As the fluid is perfect, its dynamics is governed by the Euler equation (Navier-Stokes without viscosity):
$$ \frac{\partial \vec v}{\partial t} + \left(\vec v \cdot \grad\right)\vec v = - \frac{1}{\rho} \grad P + \cancel{\vec g} \Rightarrow \frac{\partial \delta \vec v}{\partial t} = - \frac{1}{\rho_0} \grad \delta P $$
where gravitation is usually neglected. By combining these three equations, we obtain a d'Alembert equation:
$$ \boxed{ \frac{\partial^2 \delta \vec \rho}{\partial t^2} - \frac{1}{\rho_0 \chi_S} \triangle \delta \rho = 0, \quad c_s = \frac{1}{\sqrt{\rho_0\chi_S}} }$$
where $c_s$ is the sound speed. 
For a perfect gas and isentropic transformations, we have Laplace's Law $PV^\gamma = \cst$ with $\gamma=C_P / C_V$ the ratio of heat capacities at constant pressure $C_P$ and volume $C_V$, also called the adiabatic index. If the fluid particles have $N_{dof}$ degrees of freedom (translations, rotations, vibrations) to store energy in kinetic (thermal) form, then the adiabatic index is $\gamma = 1+2/N_{dof}$. For a diatomic gas such as air at the usual temperature, there are $N_{dof}=5$ degrees of freedom (3 translations and 2 rotations) so $\gamma = 7/5$. From this we derive a formula for the sound velocity as a function of temperature and particle mass[^cisotherm] :
$$PV^\gamma = \cst \Rightarrow \chi_S \approx \frac{1}{\gamma P_0}.$$
$$\boxed{ c_s = \sqrt{\frac{\gamma P_0}{\rho_0}} = \sqrt{\frac{\gamma RT}{M}} = \sqrt{\frac{\gamma k_B T}{m_{\text{air}}}} }$$
with $M$ the molar mass of the fluid and $m_{\text{air}}$ the effective mass of a particle of air if this is the medium under consideration, calculated by :
$$\label{eq:mair}
m_{\text{air}} = 78\%\,m_{N_2} + 22\%\,m_{O_2}
$$

Acoustics in an expanding space
------------------------------------------

The CMB emission shows that the Universe is slightly inhomogeneous, with small overdensities of the order of $\delta \rho / \rho_0 \sim 10^{-5}$. These fluctuations are likely to increase over time, leading to a Universe where the density contrast is of the order of $\delta \rho / \rho_0 \sim 1$[^deltas] ([](#fig:universe_scales),[](#fig:desiCMBBAO)). What are the mechanisms behind this growth? 

The formation of the large-scale structures of the Universe can be understood by a linear theory of perturbations in the perfect fluid constituted by non-relativistic matter after recombination. To study the evolution of these density perturbations in the matter field, we need to rewrite the previous acoustic equations in the specific context of an expanding medium subject to the law of gravity.

:::{figure} ../../images/noirlab2408a-2.jpg
:label: fig:desiCMBBAO

An artistic celebration of the Dark Energy Spectroscopic Instrument (DESI) Year 1 data, showing a slice of the larger 3D map that DESI is constructing during its five-year survey. DESI is mounted on the Nicholas U. Mayall 4-meter Telescope at Kitt Peak National Observatory. Credit: DESI Collaboration/KPNO/NOIRLab/NSF/AURA/P. Horálek/R. Proctor
:::


### Coordinate systems

The equations of classical physics are valid using physical (non comoving) quantities: proper distance, proper time, etc... However, using physical distances as a coordinate system is impractical in an expanding Universe. A more practical method is to write the equation in comoving space. Note
- $\vec{r}$ the physical position vector (whose norm is the proper distance $D_p(t)$),
- $\vec{\sigma}$ the comoving position vector (whose norm is the comoving distance $\chi$), 
- $\vec{v}_r$ the physical velocity,
- $\vec{v}_{\sigma}$ the comoving velocity. 

We have the following relationships:
\begin{align}
\vec{r}& =a(t) \vec{\sigma} \notag
\vec{v}_r& = \dot{a}\vec{\sigma}+a \vec{v}_{\sigma} \label{vel-rel}
\end{align}
Although the Hubble flow (first term of [](#vel-rel)) should not be considered as a real velocity, it appears in the relationship between $\vec{v}_r$ and $\vec{v}_{\sigma}$. This would be a problem if it could take values of the order of $c$ (or larger). But the condition that $\vec{r} \ll R_H$ guarantees that $\dot{a}\vec{\sigma} \ll c$ (see section [](#sec-validity)). 

How do you go from the physical coordinate system to the comoving coordinates system? The conversion of spatial partial derivatives is fairly straightforward:
\begin{equation}
\nabla_\mathbf{r} = {\partial \over \partial r^i} = {1 \over a} {\partial \over \partial \sigma^i} = \frac{1}{a} \nabla^2_\sigma,\qquad \nabla^2_\mathbf{r} = \frac{1}{a^2} \nabla^2_{\sigma}
\end{equation}

The partial time derivative requires closer examination. Let's write the differential of any function of time and space $f(t,\vec{r})$ :
\begin{align}
\dd f&= \left. {\partial f\over \partial t} \right|_\mathbf{r} \dd t + \left.{\partial f\over \partial r^i}\right|_\mathbf{t} \dd r^i   \\
&=  \left. {\partial f\over \partial t} \right|_\mathbf{r} \dd t + \left.{\partial f\over \partial r^i}\right|_\mathbf{t} \dd(a \sigma^i)  \\
&=  \left. {\partial f\over \partial t} \right|_\mathbf{r} \dd t + {1 \over a}\left.{\partial f\over \partial \sigma^i}\right|_\mathbf{t} (\sigma^i \dd a + a \dd \sigma^i)\\
&= \left( \left. {\partial f\over \partial t} \right|_\mathbf{r} + {\dot{a} \over a} (\vec{\sigma}\cdot \vec \nabla_{\sigma})f \right) \dd t + \left.{\partial f\over \partial \sigma^i}\right|_\mathbf{t} \dd \sigma^i 
\end{align}
So by identification :
\begin{equation}
\left. {\partial \over \partial t} \right|_\mathbf{r}= \left. {\partial \over \partial t} \right|_{\sigma} - H (\vec{\sigma}\cdot \vec \nabla_{\sigma})
\end{equation}



### Conservation of mass

In physical space, the continuity equation is written :
\begin{equation}
\left.{\partial \rho \over \partial t}\right|_\mathbf{r} + \vec \nabla_\mathbf{r} \cdot (\rho \vec{v}_\mathbf{r})=0
\end{equation} 

Using the comoving density $\rho_{\sigma}=\rho a^3$, we can express this equation in comoving space:
\begin{align}
\left.{\partial \rho_{\sigma}\, a^{-3} \over \partial t}\right|_{\sigma} - H (\vec{\sigma}.\nabla_{\sigma})(\rho_{\sigma} \, a^{-3})+{1 \over a} \nabla_{\sigma}\left[\rho_{\sigma} \, a^{-3} (\dot{a}\vec{\sigma}+a \vec{v}_{\sigma})\right] &=&0
\end{align}
By introducing the classic vector calculus formula 
$$\vec \nabla \cdot (\phi \vec{A})=\vec{A}\cdot \vec \nabla \phi+ \phi\c \nabla \cdot \vec{A}$$
where $\phi$ is a scalar and $\vec{A}$ a vector, the above equation reduces to :
\begin{equation}\label{Cont_comov}
\boxed{\left.{\partial \rho_{\sigma}\over \partial t}\right|_{\sigma} + \vec \nabla_{\sigma} \cdot (\rho_{\sigma} \vec{v}_{\sigma})=0}
\end{equation}
The continuity equation therefore takes exactly the same form in comoving space, using comoving variables. However, this is not the case if we use the particular velocity $a \vec{v}_{\sigma}$.


### Euler equation

In physical space, the Euler equation for a perfect (non-viscous) self-gravitating fluid takes the usual form:
\begin{equation}
\left. {\partial \vec{v_r} \over \partial t} \right|_\mathbf{r}+ \left(\vec{v}_r\cdot \vec \nabla_\mathbf{r}\right) \vec{v_r}=-\vec \nabla_\mathbf{r}\phi - \frac{1}{\rho} \vec \nabla_\mathbf{r} P
\end{equation}
In comobile space, it becomes :
\begin{align*}
\left. {\partial (\dot{a}\vec{\sigma}+a\vec{v}_{\sigma}) \over \partial t} \right|_{\sigma} & - H \vec{\sigma}\cdot \vec \nabla_{\sigma}(\dot{a}\vec{\sigma} + a\vec{v}_{\sigma}) + (\dot{a}\vec{\sigma}+a\vec{v}_{\sigma}) \cdot  {1 \over a}\vec \nabla_{\sigma} (\dot{a}\vec{\sigma}+a\vec{v}_{\sigma}) \\
& = -{1 \over a^2} \vec  \nabla_{\sigma}\phi_{\sigma} - \frac{1}{a \rho} \vec \nabla_{\sigma} P
\end{align*}
with $\phi_\sigma = a \phi$ the comobile potential. Ensuring that :
$$\left. {\partial (\dot{a}\vec{\sigma}+a\vec{v}_{\sigma}) \over \partial t} \right|_{\sigma}=\ddot{a}\vec{\sigma}+a \left.{\partial \vec{v}_{\sigma} \over \partial t}\right|_{\sigma}$$
the Euler equation in comoving coordinates reduces to :
\begin{equation}\label{Euler_comv}
\boxed{\left.{\partial \vec{v}_{\sigma} \over \partial t} \right|_{\sigma} + 2 H \vec{v}_{\sigma}+(\vec{v}_{\sigma} \cdot \vec \nabla_{\sigma})\vec{v}_{\sigma}= -{1 \over a^3} \vec \nabla_{\sigma}\phi_{\sigma} - \frac{1}{a^2 \rho} \vec\nabla_{\sigma}P - {\ddot{a} \over a} \vec{\sigma} }
\end{equation}

We can see two additional terms compared to the version of the Euler equation written in physical coordinates. The extra term $2 H \vec{v}_{\sigma}$ is a drag force created by the expansion on the moving velocities.

The last term seems strange. It seems to cancel out the Newtonian force created at $\vec{\sigma}$ by a non-zero homogeneous density background. It could be argued that this force should be zero, for reasons of symmetry. However, by applying Gauss's theorem, we can find a non-zero force directed towards the origin of the coordinates (wherever that may be!). The fact is that Poisson's equation behaves badly (and should not be used) for a source field whose $L^2$ norm is not finite. 
But of course this implies scales beyond $R_H$ where we don't expect our theory to hold up. As far as density perturbations are concerned, we will subtract the non-zero mean value and thus get rid of this large-scale inconsistency.  


### Poisson equation

In a universe with no cosmological constant, from general relativity we derive the usual Poisson equation in the limit of weak fields [](#eq:poisson) :
\begin{equation}
\triangle_\mathbf{r} \phi = 4 \pi \GN \rho
\end{equation}
where $\phi$ is the gravitational potential. Given the relationship between the potential and the Newtonian force, the comoving potential is naturally defined as $\phi_{\sigma}=\phi a$, and Poisson's equation is also unchanged in comoving space:
\begin{equation}
\triangle_{\sigma} \phi_{\sigma} = 4 \pi \GN \rho_{\sigma}
\label{Fish_comov}
\end{equation}

:::{note} Influence of the cosmological constant

If we consider a cosmological constant, in the limit of the weak field, gravitation is governed by the modified Poisson equation 
$$ \triangle_\mathbf{r} \phi = 4 \pi \GN \rho -c^2 \Lambda$$
which turns into 
$$ \triangle_{\sigma} \phi_{\sigma} = 4 \pi \GN \rho_{\sigma} -c^2 \Lambda a^3$$
:::


Newtonian perturbation theory 
-----------------------------------------

### Solution of order 0

The conservation of mass equation in comoving space [](#Cont_comov) has the following 0th order solution for a homogeneous and isotropic Universe:
\begin{equation}
\rho_{{\sigma},0}= \cst, \qquad \vec{v}_{{\sigma},0}= \vec 0
\end{equation}
At order 0, the mass density remains stationary and homogeneous and there is no particular velocity.
Integration of the Poisson equation [](#Poisson_comov) in spherical coordinates [^SphericalLaplacian] gives :
$$ \phi_{\vec{sigma},0} = \frac{4}{6} \pi \GN \rho_{\sigma,0} \sigma^2 $$
If we use Friedmann's equations [](#eq:ddota) :
$$\frac{\ddot a}{a} = -\frac{4 \pi \GN}{3}(\epsilon + 3P)$$
for a Universe dominated by matter with $\Lambda=0$ and $\epsilon = c^2 \rho_{\sigma,0} a^{-3} \gg P$, we obtain the gravitational force:
$$-\vec \nabla \phi_{\sigma,0} = -{4 \pi \GN \rho_{\sigma,0} \over 3 } \vec{\sigma} \approx a^3 \frac{\ddot a}{a} \vec{\sigma}$$
The gradient of the gravitational field gives a centrifugal force of order 0. 

From Euler's equation [](#Euler_comv) and the previous results, we arrive at :
$$P = \cst = P_0$$


### Linear solution of order 1

Consider small perturbations around the zeroth-order solution:
\begin{equation}
\rho_{\sigma}=\rho_0(1+\delta) \qquad \vec{v}_{\sigma}=\vec{v}_0+\delta\vec{v} \qquad \phi_{\sigma}=\phi_0 + \delta \phi_{\sigma}, \qquad P = P_0 + \delta P
\end{equation}
The quantity $\delta$ is called the density contrast and is widely used in the theory of structure formation. Note that it has the same value in physical space as in comobile space. By injecting these expressions into the continuity, Poisson and Euler equations, the zeroth-order solution cancels out (as expected) and by removing the second-order terms, we obtain the linearised set of equations:
$$
\label{eq:lssMassOrder1}
{\partial \delta \over \partial t} + \vec{\nabla}_{\sigma} \cdot \delta\vec{v}_r = 0
$$
$$
\label{eq:lssEuler1}
{\partial \delta\vec{v}_r \over \partial t} + 2 H \delta\vec{v}_r = - {1 \over a^3} \vec \nabla_{\sigma} \delta \phi_{\sigma} - \frac{1}{a^2 \rho_0} \vec \nabla_{\sigma} \delta P
$$
$$
\label{eq:lssPoissonOrder1}
\triangle_{\sigma}^2 \delta \phi_{\sigma} = 4 \pi \GN \rho_{\sigma,0} \delta 
$$

By taking the divergence of the linearised Euler equation [](#eq:lssEuler1), the time derivative of the linearised mass conservation equation [](#eq:lssMassOrder1) and reinjecting the Poisson equation [](#eq:lssPoissonOrder1), we finally obtain :
$$\ddot{\delta}+ 2 H \dot{\delta} - \frac{1}{a^2 \rho_0} \triangle_{\sigma} \delta P = 4 \pi \GN {\rho_0 } \delta$$
We introduce the speed of sound $c_s$ in the medium for adiabatic compression:
$$c_s^2 = \frac{1}{\rho_0 \chi_S} = \left.\frac{\partial P}{\partial \rho}\right\vert_{S} \approx \frac{\delta P}{\delta \rho}\Rightarrow \delta P \approx c_s^2 \rho_0 \delta $$
Then we obtain the equation for the growth of perturbations in comoving space:
\begin{equation}\label{fluct_growth}
\boxed{ 
\ddot{\delta}+ 2 H \dot{\delta} - \frac{c_s^2}{a^2} \triangle_{\sigma} \delta = 4 \pi \GN \rho_0 \delta
}
\end{equation}



### Sound speed

In a Universe dominated by radiation, the properties of relativistic gas are :
$$\rho_r \propto T^4, \quad P_r = \rho_r c^2 /3$$
hence the sound speed in relativistic plasma:
$$c_s^2 = \left.\frac{\partial P_r}{\partial \rho_r}\right\vert_{S} \approx \frac{c^2 \delta \rho_r}{3\delta \rho_r}
\Rightarrow \boxed{c_s = \frac{c}{\sqrt{3}} \approx 0.58 c}$$

In a Universe dominated by non-relativistic matter, the thermodynamic properties of baryons are :
$$\rho_b = n_b m_b + \frac{n_b k_B T}{(\gamma_b -1)c^2},\quad P_b = n_b k_B T$$
with $m_b=(1-Y_p)m_\mathrm{H} + Y_p m_{\mathrm{He}} \approx 1.72 m_p$ the effective mass of the baryons in a gas mixture of atomic hydrogen and helium (note the similarity with [](#eq:mair)), and $\gamma_b=5/3$ the adiabatic index of the baryons because the hydrogen is in atomic form (and the helium, of course). For a reversible adiabatic transformation, with Laplace's law we have $P_b \rho_b^{-\gamma_b}=\cst$, the temperature of the baryons $T_b$ evolves as :
$$P_b = n_b k_B T_b \propto a^{-3\gamma_b}.$$
Now $n_b \propto a^{-3}$ therefore 
$$T_b = T_{\mathrm{dec}} \left(\frac{a}{a_{\mathrm{dec}}}\right)^{-3(\gamma_b -1)}$$
The sound speed in the baryon gas is :
$$c_s^2 = \left.\frac{\partial P_b}{\partial \rho_b}\right\vert_{S} \approx \gamma_b \rho^{\gamma_b-1} = \frac{\gamma_b n_b k_B T_b}{n_b m_b} \Rightarrow \boxed{c_s(T_b) = \sqrt{\frac{\gamma_b k_B T_b}{m_b}} \ll c}$$
Just after the photons and electrons have decoupled, the temperature of the baryons is $T_{\mathrm{dec}} = 3055\,\kelvin$ so the speed of sound in the baryon gas is about $1.5\times 10^{-5}c \approx 5\,\mathrm{km}/\mathrm{s}$. The change is of several orders of magnitude, so the evolution of the perturbations changes drastically at this instant. Then the temperature of the baryons decreases in $a^{-2}$, at least until heating by interstellar radiation changes the situation (around $z\sim 10$), so the sound speed decreases in $a^{-1}$. 

:::{figure} #LSS_cs
:name: fig:LSS_cs
:align: center
:width: 70%

Sound speed in the Universe as a function of the scale factor $a$. The slight decrease between equivalence and decoupling is given by equation [](#eq:csrhobrhog) (see box). The calculation is inaccurate when we enter the non-linear regime of structure growth, i.e. when $\delta \sim 1$ (shaded region). In addition, also around this redshift, the baryon gas is heated by stellar radiation, so the temperature of the baryons no longer evolves in $a^{-2}$.
:::

:::{note} Mixture of baryons and coupled photons
:class: dropdown

As long as photons are coupled to free electrons, they are mechanically coupled to the baryon gas by the Coulomb force. During the period when the Universe is dominated by matter but photons are still coupled to electrons ({cite}`Weinberg1989` p.509,566) :
$$\rho_{\mathrm{tot}} = \rho_b + \frac{n_b k_B T}{(\gamma_b -1)c^2} + \rho_\gamma \approx \eta m_b n_\gamma + \rho_\gamma $$
$$P_{\mathrm{tot}} = n_b k_B T + \frac{1}{3}\epsilon_\gamma \approx \frac{1}{3}\rho_\gamma c^2 $$
\begin{align*}
c_s^2 & = \left.\frac{\partial P_{\mathrm{tot}}}{\partial \rho_{\mathrm{tot}}}\right\vert_{S} \approx  \frac{\delta P_{\mathrm{tot}}}{\delta \rho_{\mathrm{tot}}} \approx \frac{\frac{4}{3}\frac{\delta T}{T}\epsilon_\gamma}{3 \eta m_b n_\gamma \frac{\delta T}{T} +  4 \frac{\delta T}{T}\rho_\gamma} \\
& = \frac{c^2}{3} \frac{1}{\left(1 + \frac{3}{4} \frac{\eta n_\gamma m_b c^2}{\epsilon_\gamma}  \right)} = \frac{c^2}{3} \frac{1}{\left(1 + \frac{3}{4} \frac{\rho_b}{\rho_\gamma}  \right)} 
\end{align*}
$$
\label{eq:csrhobrhog}
c_s = \frac{c}{\sqrt{3}} \frac{1}{\sqrt{\left(1 + \dfrac{3}{4} \dfrac{\Omega_b^0}{\Omega_\gamma^0(1+z)}  \right)} }
$$

:::

### Jeans instability

The solutions to the perturbation evolution equation [](#fluct_growth) will be studied next semester, but we can already study their behaviour from their dispersion relation. Let's look for plane wave solutions of the form :
$$\delta \propto e^{i(\omega t - \vec k_\sigma \cdot \vec \sigma)}$$
and study the solutions in the Fourier domain. The dispersion relation is written :
$$-\omega^2 + 2 i H \omega - \frac{c_s^2}{a^2} k^2_\sigma = 4 \pi \GN \rho_0$$.
By neglecting the damping term (of the order of the age of the Universe) in front of the characteristic time of evolution of the perturbations ($\omega \gg H$), we end up with :
$$\boxed{\omega^2 = c_s^2 \left( k_r^2 - \frac{4\pi \GN \rho_0}{c^2_s}\right) }$$
where $k_\sigma = 2 \pi / \chi = a k_r$. This is the same dispersion relation as for electromagnetic waves in a plasma. We define the Jeans wavelength (<doi:10.1098/rsta.1902.0012>) $k_J$ and the Jeans length $\lambda_J$ by :
$$\boxed{k_J = \sqrt{\frac{4\pi \GN \rho_0}{c^2_s}},\quad \lambda_J = \frac{2\pi}{k_J} = c_s \sqrt{\frac{\pi}{\GN}}\rho_0 }.$$
* If $k_r > k_J \Leftrightarrow \lambda < \lambda_J$, then $\omega^2 > 0$ so we have an oscillating solution i.e. an acoustic wave which propagates: the perturbations of small size compared to the length of Jeans oscillate thanks to the pressure force.
* If $k_r < k_J \Leftrightarrow \lambda > \lambda_J$, $\omega^2 < 0$ then we have a non-oscillating solution in exponential: the large structures evolve only under the effect of gravity and increase (and the voids decrease).

As the $\lambda$ scale evolves with the expansion ($\lambda \propto a$) as well as the Jeans length, the discussion is not easy to conduct along the history of the Universe. Let's define $M$ the mass in a sphere of radius $\lambda$, conserved with expansion, and compare it with the mass of Jeans $M_J$.
$$M_J = \frac{4}{3} \pi \rho_0 \lambda_J^3 \propto \frac{c_s^3}{\GN^{3/2}n \rho_0^{1/2}}$$
* If $M < M_J$, then the structure is too light and the pressure can compensate for the force of gravity: the structure oscillates.
* If $M > M_J$, then the structure is too heavy and collapses gravitationally.

Plotting the Jeans mass as a function of the scale factor $a$ allows us to predict which structures can collapse gravitationally and which are prevented from growing [](#fig:LSS_MJ) ({cite}`Weinberg1989` p. 565).

:::{figure} #LSS_MJ
:name: fig:LSS_MJ
:align: center
:width: 70%

Evolution of the mass of Jeans as a function of the scale factor $a$. The calculation is inaccurate when we enter the non-linear regime of structure growth, i.e. when $\delta \sim 1$ (shaded region). In addition, also around this redshift, the baryon gas is heated by stellar radiation, so the temperature of the baryons no longer evolves in $a^{-2}$.
:::

Describing the growth of structures before recombination contradicts the non-relativistic hypothesis on which our study is based. However, the sound speed scale remains a relevant scale and moreover non-relativistic matter dominates after equivalence. Knowing this (and that the relativistic study does not give fundamentally different results from what follows), we will take the liberty of discussing the growth of large structures in the primordial and recent Universe (although it is non-linear today).

From the [](#fig:LSS_MJ), we can see that before decoupling, structures with the mass of a galaxy or a cluster of galaxies are not heavy enough to collapse (or only in the first instants of the Universe). Pressure waves travel through them and they oscillate. However, after decoupling, the speed of sound drops by 5 orders of magnitude. The decoupling of photons freezes the pressure waves and structures the mass of galaxies and even dwarf galaxies can begin to grow.





### Acoustic waves in the primordial Universe 

Before decoupling, acoustic waves travel through the primordial plasma. Let's define the comoving sound horizon as :
$$r_s^c = \int_0^{t_\mathrm{dec}} \frac{c_s(t) \dd t}{a(t)} = \int_{z_\mathrm{dec}}^\infty \frac{c_s(z)}{H(z)}\dd z $$
the maximum comoving distance travelled by an acoustic wave since the beginning of the Universe. At the moment of decoupling, it is $150\,\Mpc/a_\mathrm{dec}$ or $r_s = a_\mathrm{dec} r_s^c \approx 0.13\,\Mpc$. This is therefore the distance that a wave from an overdensity present at the Big Bang was able to travel.
This wave propagation results in a positive correlation on the presence of matter on this fundamental spatial scale. This scale is converted into an angular separation on the sky, printed on the CMB temperature anisotropy map and given by :
$$\boxed{ \theta_s = \frac{r_s}{D_A(z_{\mathrm{dec}})} }$$
A scale in distance space gives a sinusoidal power spectrum in reciprocal space. Measuring the position of maxima in the CMB temperature anisotropy power spectrum gives an extremely accurate {cite:p}`Planck2018` sound horizon:
$$100 \theta_s = 1.04123 \pm 0.00046\,\mathrm{rad}, \quad \mathrm{i.e.}\quad \theta_s \sim 0.6\,\degree$$
which is one of the 6 free parameters of the $\Lambda$CDM model.

:::{figure} ../../notebooks/movie.mp4
:name: fig:cmb_anisotropies
:width: 100%

Time evolution of an initial Gaussian field under the effect of acoustic propagation.
:::

:::{note} Adiabatic or isocurvature initial conditions?
:class: dropdown

TODO

:::



### Optical depth

The optical depth $\tau$ is defined as the ratio of the number of photons received on Earth without having undergone any Thomson scattering $N(t_0)$ to the number of photons $N(t)$ emitted at a time $t$:
$$\frac{N(t_0)}{N(t)} = e^{-\tau}$$
with
$$\tau = \int_t^{t_0} \Gamma_\gamma(t) \mathrm{d}t$$
The time $t_{\mathrm{ls}}$ for which $\tau=1$ is called the time of last diffusion. This is the time since which a CMB photon has not interacted with an electron. More precisely
\begin{equation}
\tau(z) = \int_0^z \frac{\Gamma_\gamma(z)}{H(z)}\frac{\dd z}{1+z}
\end{equation}
This is one of the six parameters of the standard $\Lambda$CDM model. After the emission of the cosmic microwave background, we enter the Dark Ages of the Universe, when the Universe is transparent but no stars are yet emitting light. But with the appearance of the first stars and galaxies, perhaps 150 million years after the Big Bang, the neutral medium is ionised once again. Although very sparse, CMB photons again interact with electrons by Thomson scattering, which reduces the amplitude of the small-scale anisotropies in the CMB power spectrum, and introduces new anisotropies in the polarisation anisotropies. It is the least well measured parameter of the $\Lambda$CDM model at the moment ([](#fig:tau)) $\tau = 0.058 \pm 0.006$ {cite:p}`Planck2023`, but it informs about the appearance of the first luminous stars ([](#fig:tau_reio)).

:::{figure} ../../images/tau_history.png
:width: 80%
:align: center
:label: fig:tau

The optical depth to reionization $\tau$ measured as a smearing of the CMB angular power spectrum (from [https://lambda.gsfc.nasa.gov/education/graphic_history/taureionzation.html](https://lambda.gsfc.nasa.gov/education/graphic_history/taureionzation.html), image credit: NASA / LAMBDA Archive Team).
:::

:::{figure} #tau_reio
:width: 80%
:align: center
:label: fig:tau_reio

Assuming that the Universe is once again completely ionised, the calculation of its optical depth shows that if today we measure $\tau=0.058$ then the reionisation of the Universe should be complete around $z_{\mathrm{reio}} \sim 7$ giving the start of galaxy formation earlier than 1 billion years after the Big Bang.
:::



[^cisotherm]: if we had used the isothermal hypothesis, we would instead use the equation of state $PV=\cst$ and the speed of sound would be different by a factor $\sqrt{\gamma}$.

[^deltas]: with the orders of magnitude of [](#fig:universe_scales) and $\rho_0\sim 6\text{ protons/m}^3$, for a planet $\delta \sim 10^{32}$ whereas for a supercluster $\delta \sim 6$

[^SphericalLaplacian]: $$\triangle_\sigma = \frac{1}{\sigma^2} \frac{\partial}{\partial \sigma}\left( \sigma^2 \frac{\partial}{\partial \sigma}\right)$$.