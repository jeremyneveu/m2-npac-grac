---
short_title: Acceleration mechanisms
authors:
  - jbiteau
keywords: acceleration
---

Acceleration mechanisms
=============================================



Cosmic-ray accelerators
--------------------------------

### Maximum energy: the Hillas criterion


A necessary condition for accelerating particles up to a given maximum energy is that their astrophysical source is 
large enough, or magnetised enough, to confine them for at least one radius of gyration. This relatively simple 
criterion, attributed to Michael Hillas, is used to classify astrophysical accelerators in a so-called Hillas 
diagram, as shown in [figure %s](#fig:cr_hillas).

:::{figure}  ../../images/CR_Hillas.jpeg
:name: fig:cr_hillas
:align: center
:width: 60%

Magnetic field in Gauss vs size in km of candidate cosmic-ray sources. The Hillas limit, which provides the minimum 
magnetic field at a fixed size needed to accelerate cosmic rays to a given magnetic rigidity, is shown in blue for 
protons at the knee energy and in brown for protons at the ankle energy. Adapted from {cite}`2020PhR...872....1B`.
:::

The gyro-radius, $r_\mathrm{g}$, of a particle of four-velocity $(\gamma, \gamma\vec{\beta})$ derives from the 
equation of motion $\frac{\dd}{\dd t}\big(\gamma m \vec{v} \big) = Ze \vec{v}\times \vec{B}$, where $m$ and $Z$ are 
the mass and charge of the particle. As the magnetic field does no work, $\gamma m$ is constant so that the particle 
moves along an helicoidal trajectory characterized by $\gamma m \frac{v_\perp^2}{r_\mathrm{g}} = Z e B v_\perp$, 
where $p_\perp = \gamma m v_\perp$ is the momentum in the plane perpendicular to the $B$ field. Thus

$$
\begin{align}
r_\mathrm{g} &= \frac{p_\perp}{Z e B}\\
&= \frac{R}{Bc}\\
&= 1.1\,\mathrm{pc} \times \Big(\frac{R}{10^{15}\,\mathrm{V}}\Big) \times \Big(\frac{B}{1\,\mu\mathrm{G}}\Big)^{-1},
\end{align}
$$
where $R = \frac{p_\perp c}{Z e} \approx \frac{E}{Z e}$ is the magnetic rigidity in volts.


The Hillas criterion states that accelerating a particle up to a given rigidity $R$ within a region of size $L$ is 
only possible if $r_\mathrm{g}<L$, which imposes $R < L B c$. Accounting for relativistic bulk motion of the 
emitting region $(\Gamma, \Gamma\vec{\beta})$, the relativistic Hillas criterion on the observed rigidity reads


$$
\begin{align}
R_\mathrm{obs} < \Gamma \beta L' B' c\\\
&< 0.9 \times 10^{15}\,\mathrm{V} \times \Big(\frac{L'}{1\,\,\mathrm{pc}}\Big) \Big(\frac{B'}{1\,\mu\mathrm{G}}\Big)\Big(\frac{\Gamma\beta}{1}\Big), \mathrm{\ or}\\
&< 3 \times 10^{18}\,\mathrm{V} \times \Big(\frac{L'}{1\,\,\mathrm{pc}}\Big) \Big(\frac{B'}{1\,\mathrm{mG}}\Big)\Big(\frac{\Gamma\beta}{3}\Big)
\end{align}
$$

The classes of Galactic sources satisfying this condition up to the magnetic rigidity corresponding to the knee and 
second knee of the cosmic-ray spectrum, i.e. a proton energy of $\approx 4 \times 10^{15}\,\mathrm{eV}$ and an 
energy of $\approx 10^{17}\,\mathrm{eV}$ for fully ionized iron are shown in [figure %s](#fig:cr_hillas). 
Extragalactic sources are also shown and can be compared to the Hillas criterion up to the ankle and cut-off of the 
cosmic-ray spectrum, i.e. for maximum proton energy of $\approx 4 \times 10^{18}\,\mathrm{eV}$ and iron energy of 
$\approx 10^{20}\,\mathrm{eV}$.

### Cosmic-ray production rate

Cosmic-ray accelerators must not only be able to achieve a given maximum rigidity, but must also be sufficiently 
luminous that their cumulative emission reproduces the observed intensity,
$I_\mathrm{CR} = \frac{c}{4\pi} \varepsilon_\mathrm{CR}$.

A particularly useful quantity for studying the origin of Galactic cosmic rays is the energy production rate:
$w_\mathrm{GCR} = \varepsilon_\mathrm{GCR}({>}\,1\,\mathrm{GeV})/\tau_\mathrm{esc}$, where $\varepsilon_\mathrm{GCR}({>}\,1\,\mathrm{GeV})\approx 1.2 \times 10^6\,\mathrm{eV\,m}^{-3} \approx 6 \times 10^{45}\,\mathrm{J\,kpc}^{-3}$ was determined in [exercise %s](#exo:milky_way) and where $\tau_\mathrm{esc} \gtrsim 15\,$Myr is the residence time of cosmic rays in the Galaxy. This residence time is estimated from so called cosmic-ray clocks (see e.g. {cite}`2014arXiv1407.5223L`), e.g. through the ratio between $^{10}$Be ($t_{1/2} = 1.4\,$Myr) and its stable isotope $^{9}$Be, both formed by the fragmentation of carbon and oxygen nuclei confined in the Milky Way.

If we model the Milky Way as a disk with diameter $2r_\mathrm{MW} = 25\,$kpc and height $h_\mathrm{MW} = 0.3\,$kpc, 
then the energy production rate of Galactic cosmic rays integrated over the volume of the Milky Way yields the 
cumulative luminosity of the cosmic-ray sources:
\begin{align}
\sum_{\mathrm{src} \in \mathrm{MW}} L_\mathrm{src}(> 1\,\mathrm{GeV}) &= w_\mathrm{GCR} \times \pi r_\mathrm{MW}^2 h_\mathrm{MW}\\
&\approx 2 \times 10^{33}\,\mathrm{W} \times \left(\frac{\tau_\mathrm{esc}}{15\,\mathrm{Myr}} \right).
\end{align}

The kinetic energy of a core-collapse supernova can be estimated to 
\begin{align}
T_\mathrm{CC} &= \frac{1}{2}M_\mathrm{ejecta} v_\mathrm{shock}^2 \\
&\approx 10^{44}\,\mathrm{J} \times \Big( \frac{M_\mathrm{ejecta}}{10\,M_\odot} \Big) \times \Big( \frac{v_\mathrm{shock}}{3\times 10^3 \,\mathrm{km\,s}^{-1}} \Big)^2
\end{align}
and their explosion rate in the Milky-Way is estimated as $\lambda_\mathrm{CC} = (1.6 \pm 0.5)\times 10^{-2}\,\mathrm{yr}^{-1}$ ({cite}`2021NewA...8301498R`).

If core-collapse supernovae are responsible for accelerating the majority of cosmic rays to energies greater than 1 
GeV, then the efficiency of the conversion of kinetic energy into cosmic rays, $\eta_\mathrm{GCR}$, should satisfy 
the relation
\begin{align}
\eta_\mathrm{GCR} &= \frac{\sum_{\mathrm{src} \in \mathrm{MW}} L_\mathrm{src}(> 1\,\mathrm{GeV})}{T_\mathrm{CC}\lambda_\mathrm{CC} } \\
&\approx 2\% \times \left(\frac{\tau_\mathrm{esc}}{15\,\mathrm{Myr}} \right),
\end{align}
a reasonable constraint suggesting that core-collapse supernovae may be responsible for accelerating the bulk of 
Galactic cosmic rays at GeV energies.

This energy criterion enables us to identify supernovae as the primary sources of Galactic cosmic rays in the GeV 
range. However, it does not enable us to determine whether this population of sources is predominant in the PeV 
range. Alternative classes that are sub-dominant at GeV energies but may be dominant at PeV energies, such as 
microquasars, are therefore being studied. Like the search for extragalactic EeVatrons, the search for Galactic  
PeVatrons is an active area of research.

Acceleration processes
--------------------------------

### Astrophysical plasmas


Consider a fully ionized plasma, composed e.g. of protons and electrons. Astrophysical plasmas are usually neutral 
on large scales, i.e. $n_p = n_e = n$ where $n_p$ and $n_e$ are the number density of protons and electrons respectively. 

Neutrality on a large spatial scale, $L$, means $L \gg \lambda_\mathrm{D}$, where $\lambda_\mathrm{D}$ is the Debye length, beyond which charge screening occurs (see Chap. 11.1 in {cite}`2011hea..book.....L`). The Debye length depends on the thermal velocity of the electrons, $v_e$, and the plasma frequency, $\omega_e$:
\begin{align}
\lambda_\mathrm{D} &= \frac{v_e}{\omega_e}\\
     &= \frac{\sqrt{kT/m_e}}{\sqrt{e^2 n/\epsilon_0 m_e}}\\
     &= \sqrt{\frac{kT\epsilon_0}{e^2 n}}\\
     &\approx 27\,\mathrm{km} \times \left(\frac{kT}{13.6\,\mathrm{eV}}\right)^{1/2} \left(\frac{n}{1\,\mathrm{m}^3}\right)^{-1/2} \\
\end{align}

This microphysics-relevant scale can be compared to the much larger astrophysical source sizes in [](fig:cr_hillas). 

In a rarefied plasma, it is improbable for a test particle to encounter another particle. The system is said to be 
colisionless, i.e. the motion of a charged particle is determined by its overall interaction with the plasma and the 
magnetic fields attached to it.

A few properties of astrophysical plasmas are worth noting here ({cite}`1962pfig.book.....S`). Firstly, 
astrophysical plasmas have a high conductivity (low resistivity), which is comparable to that of metals. This high 
conductivity leads to the short-circuiting of any large-scale electric field and to the phenomenon of magnetic-flux 
freezing, i.e. magnetic field lines behave as if anchored into the plasma.

A second notable feature of a plasma is the speed at which disturbances propagate along the field lines. The 
equivalent of the speed of sound, called the Alfvén speed, is provided by the ratio of the magnetic energy density, 
$u_B$, to the mass density of the medium $\rho = n m_p$, i.e. $v_\mathrm{A} \propto \sqrt{\frac{u_B}{\rho}}$. More 
specifically, $v_\mathrm{A} = \frac{B}{\sqrt{\rho\mu_0}}$ that is
\begin{align}
\frac{v_\mathrm{A}}{c} &= \frac{B}{\sqrt{n m_pc^2\mu_0}}\\
     &= 7 \times 10^{-3} \times \left(\frac{B}{10^{-10}\,\mathrm{T}}\right) \left(\frac{n}{1\,\mathrm{m}^3}\right)^{-1/2}
\end{align}

The diffusion of charged particles in an astrophysical plasma is determined by their resonance with magnetic-field 
perturbations such as Alfvén waves and other hydromagnetic waves.


### Fermi mechanisms


Electromagnetic interaction is responsible for the acceleration of charged particles in astrophysical environments, 
via the Lorentz force $\vec{F} = q(\vec{E} + \vec{v}\times\vec{B})$. Since the magnetic term does not work, an 
effective electric field is required for acceleration. Note, however, that an electromagnetic field such that
$\vec{E} = \vec{0}$ and $\vec{B} \neq \vec{0}$ can always be transformed to
$\vec{E'} \neq \vec{0}$ and $\vec{B'} \neq \vec{0}$ through a change of frame. The relevant quantities for 
discussing the different types of acceleration mechanisms are the Lorentz invariants of the electromagnetic tensor
$F_{\mu\nu}$, namely $F_{\mu\nu}F^{\mu\nu} = 2\left[ (Bc)^2-E^2 \right]$ and $\mathrm{det}(F) = \vec{E} \cdot \vec{B}$
({cite}`2019PhRvD..99h3006L`).

The acceleration mechanism most commonly used by humans on Earth is linear acceleration, i.e.
$\vec{E} \cdot \vec{B} \neq \vec{0}$ or $E^2 > (Bc)^2$. These cases, for which ideal magnetohydrodynamics does not 
apply (ideal Ohm's law with no resistive term: $\vec{E} + \vec{v}\times\vec{B} = \vec{0}$), are only found in a 
limited number of astrophysical environments, such as the gaps in the magnetospheres of pulsars.

The case more generally found in astrophysical environments, for which $E^2 < (Bc)^2$ and $\vec{E} \cdot \vec{B} = \vec{0}$,
allows us to describe acceleration by shock waves, magnetic turbulence or in sheared flows. Two seminal publications 
by Enrico Fermi described the concepts in the 1950s {cite:p}`1949PhRv...75.1169F,1954ApJ...119....1F`. In both 
cases, acceleration results from particle scattering on magnetic-field perturbations such as Alfvén waves, which 
move with a characteristic velocity $v_\mathrm{A}$. A head-on / receding collision with a pertuburation leads to a 
gain / loss of momentum $\frac{\Delta p}{p} \approx \pm \frac{v_\mathrm{A}}{c}$. In the case of an isotropic 
distribution of the velocities of the scattering centers, found for example in a turbulent magnetic field, head-on 
collisions are more frequent by a factor $\frac{v_\mathrm{A}}{c}$, so that the rate of energy gain is favored over 
the rate of loss (see chapter 7.3 in {cite}`2011hea..book.....L`). This mechanism is known as second-order Fermi 
acceleration. In the case where only head-on collisions take place, for the geometry of a contracting magnetic 
bottle found for example on either side of a shock front, the mechanism is said to be first-order.

The denomination of first- and second-order Fermi acceleration is more explicit when we consider the acceleration time,
$t_\mathrm{acc}$, which depends on the mean free path between scattering centers, $l_\mathrm{mfp}$:
\begin{align}
t_\mathrm{acc}^{-1} &= \frac{\dd E/\dd t}{E}\\

&\approx \frac{c}{l_\mathrm{mfp}} \times \left\langle \frac{\Delta p}{p} \right\rangle\\
&\approx \left\{\begin{array}{lr}
        \frac{c}{l_\mathrm{mfp}} \times \left(\frac{v_\mathrm{A}}{c} \right), & \text{for first order Fermi acceleration}\\
        \frac{c}{l_\mathrm{mfp}} \times \left(\frac{v_\mathrm{A}}{c} \right)^2, & \text{for second order Fermi acceleration}
        \end{array}\right.
\end{align}

Spectrum of accelerated particles
--------------------------------

### The Fokker-Planck equation

The equation that governs the evolution of the momentum and position of a collection of particles is a partial 
differential equation known as the diffusion-loss equation. Its formal derivation uses the diagram provided in
[](fig:coord_space_diagram) {cite:p}`{see also chapter 7.5 in}2011hea..book.....L`. The reasoning is limited here to 
one spatial and one momentum dimension, but can easily be extended to 6D if one wishes to consider anisotropic 
phenomena such as the different diffusion coefficients along and perpendicular to a magnetic-field line.


:::{figure}  ../../images/Fig7.6_Longair.svg
:name: fig:coord_space_diagram
:align: center
:width: 60%

Coordinate space diagram of momentum against spatial coordinate. Adapted from chapter 7.5 in {cite}`2011hea..book.....L`.
:::

Consider an initial Maxwellian momentum distribution for a number of particles $n(x, p, t)\dd x \dd p$. The 2D 
phase-space density, $n$, is analoguous to the 6D phase-space density $\dd \mathcal{N}/\dd^3 x\dd^3 p$ defined in 
chapter [](05_astroparticle_sources.md). 

 The rate at which the number of particles in the box changes is given by:
\begin{align}
\frac{\partial n}{\partial t} \dd x \dd p &= \left[ \phi_x(x,p,t) - \phi_p(x+\dd x, p, t) \right]\dd p\\
&+ \left[ \phi_p(x,p,t) - \phi_p(x, p+\dd p, t) \right]\dd x\\
&+ \left[ Q - \frac{n}{\tau} \right]\dd x \dd p,
\end{align}
i.e.
\begin{align}
\label{eq_Fokker_start}
\frac{\partial n}{\partial t} &= -\frac{\partial \phi_x}{\partial x} -\frac{\partial \phi_p}{\partial p} + Q - \frac{n}{\tau},
\end{align}
where $Q$ is the source term characterizing the injection of new particles and $\tau$ is the time scale of 
 catastrophic energy losses, relevant e.g. to radioactive decay, spallation, or simply the escape of the particle 
 from the region of interest.

$\phi_p$ is the flux of particles of momentum between $p$ and $p + \dd p$ through $\dd x$. Assuming, for simplicty, 
no momentum diffusion, it reads:
$$
\phi_p = n \dot p,
$$
where $\dot p = \frac{p}{t_\mathrm{acc}} - \frac{p}{t_\mathrm{loss}}$ for Fermi acceleration at a rate $t_\mathrm{acc}^{-1}$ and continuous energy losses, such as synchrotron losses, at a  rate $t_\mathrm{loss}^{-1}$.

$\phi_x$ is the flux of particles of position between $x$ and $x + \dd x$ through $\dd p$:
$$
\phi_x = v_\mathrm{adv} n -D \frac{\partial n}{\partial x},
$$
i.e. an advection term, with $v_\mathrm{adv}$ the advection velocity, and a diffusion term from Fick's law with $D$ 
the diffusion coefficient. For isotropic diffusion,
$D = \frac{1}{3} c l_\mathrm{mfp}$. Writing $\eta = l_\mathrm{mfp}/r_\mathrm{g}$ the number of gyroradii in a mean 
free path:
$$
 D = \frac{1}{3} c \eta r_\mathrm{g},
$$
where $\eta \geq 1$ as the mean free path is at least a gyroradius. The mimimum diffusion coefficient, obtained for $\eta=1$, is referred to as the Bohm limit. 

The terms of Equation [](eq_Fokker_start) being defined, we get the Fokker-Planck equation describing the diffusion-loss of the particles:
\begin{align}
\label{eq_FokkerPlanck}
\frac{\partial n}{\partial t} &= \frac{\partial}{\partial x}\left(D \frac{\partial n}{\partial x}\right) - \frac{\partial}{\partial x}\left(v_\mathrm{adv} n\right)  -\frac{\partial}{\partial p}\left[ \left(\frac{1}{t_\mathrm{acc}} - \frac{1}{t_\mathrm{loss}}\right) pn \right]   - \frac{n}{\tau} + Q.
\end{align}

:::{note}
There is no term explicitly dependent on $c$ in the Fokker-Planck equation. If we consider diffusion only and 
constant diffusion coefficient, the mean displacement reached at time $t$ is $r = \sqrt{4Dt}$ that is an effective 
velocity $v = r/t = \sqrt{4D/t}$, which can be superluminal (!) at small $r$ and $t$. This is a known problem of 
diffusion equations, which is further discussed e.g. in {cite}`2009ApJ...693.1275A` in the context of astroparticle 
physics.
:::

### Where power laws come from

The simplest application of the Fokker-Planck equation is highly relevant to understanding acceleration (see also 
chapter 7.4 in {cite}`2011hea..book.....L` for an introduction to diffusive shock acceleration). Consider a 
stationary system, with no diffusion or advection, no energy loss, for which catastrophic losses are limited to 
escape ($\tau = t_\mathrm{esc}$) and with particle injection in the past, then:

$$
\frac{\partial}{\partial p}\left(\frac{pn}{t_\mathrm{acc}}\right) =   - \frac{n}{t_\mathrm{esc}} 
$$
where $t_\mathrm{acc}$ does not depend on $p$ for Fermi acceleration. This gives

$$
n + p\frac{\partial n}{\partial p} =   - n\frac{t_\mathrm{acc}}{t_\mathrm{esc}} 
$$

$$
\frac{\partial \ln n}{\partial  \ln p} =   -\left(1 + \frac{t_\mathrm{acc}}{t_\mathrm{esc}}\right)
$$

$$
n = n_0 \left( \frac{p}{p_0}\right)^{- \left(1 + \frac{t_\mathrm{acc}}{t_\mathrm{esc}}\right)}
$$

That is a power-law spectrum of index $s=1 + \frac{t_\mathrm{acc}}{t_\mathrm{esc}}$.

The value of the index can be determined with multiple approaches, depending on the considered astrophysical 
environment. In the case of shock acceleration or magnetic reconnection, one can use box models such as developped 
by {cite}`1999A&A...347..370D,2012MNRAS.422.2474D` and show that
$\frac{t_\mathrm{acc}}{t_\mathrm{esc}} = \frac{3}{|r-1|}$, where $r=\rho_2/\rho_1$ is the compression ratio between 
the shocked medium and the undisturbed medium.

For a shock acceleration at high Mach number and assuming a plasma described as a perfect gaz of adiabatic index 
$\gamma = \frac{c_P}{c_V}$, the compression ratio is equal to $r = \frac{\gamma +1}{\gamma -1}$. As $\gamma = 5/3$ 
for a monoatomic gaz of protons or electrons, we get $r = \frac{\frac{5}{3} +1}{\frac{5}{3} -1} = 4$. In such a 
system, the power-law spectrum has an index $s = 1 + \frac{3}{|4-1|} = 2$, that is:

$$
\frac{\partial N}{\partial p} \propto n \propto \left( \frac{p}{p_0}\right)^{-2}
$$

The universality of this power law of index 2, whose presence is inferred in many non-thermal astrophysical systems, 
is one of the great successes of diffusive shock acceleration theory.

:::{exercise} Rankine-Hugoniot equations for a shock
:label: exo:rankine_hugoniot

The jump conditions of Rankine and Hugoniot are continuity equations at a shock front. The shock is due to a 
supersonic disturbance moving at supersonic speed, $v_\mathrm{sh}$, from the shocked medium, index as 2, towards the 
undisturbed medium, indexed as 1. In the shock frame, the undisturbed plasma is moving towards the shock at velocity 
$u_1 = -v_\mathrm{sh}$ while plasma in the shocked medium is moving away from the shock front at velocity $u_2$. The 
continuity equations at the shock front are the following:
- $\rho_1 u_1 = \rho_2 u_2$ (mass conservation),
- $P_1 + \rho_1 u_1^2 = P_2 + \rho_2 u_2^2$ (momentum conservation),
- $\frac{1}{2}u_1^2 + \frac{\gamma}{\gamma-1} \frac{P_1}{\rho_1} = \frac{1}{2}u_2^2 + \frac{\gamma}{\gamma-1} \frac{P_2}{\rho_2}$ (energy conservation),
where $u$, $\rho$ and $P$ are the velocity, mass density and pressure of each medium. The plasma has an adiabatic 
  index $\gamma$.

1. Show that 
$$P_2 - P_1 + \rho_1u_1(u_2-u_1) = 0$$

2. Using the mass-conservation equation and the equation above, show that 
$$ \frac{P_2}{\rho_2} - \frac{P_1}{\rho_1} = (u_2 - u_1)\left( \frac{P_1}{\rho_1 u_1} -u_2\right) $$

3. Using the equation above and the energy-conservation equation, show that
$$\frac{u_2}{u_1} = \frac{\gamma-1}{\gamma+1} + \frac{2}{\gamma+1}\frac{\gamma P_1}{\rho_1 u_1^2}$$

4. Assuming a highly supersonic shock with $\mathcal{M} = v_\mathrm{sh}/c_s = v_\mathrm{sh} / \sqrt{\frac{\gamma P_1}{\rho_1}} \gg 1$, determine the velocity ratio and the density ratio in the shocked and undisturbed media.

:::

:::{solution} exo:rankine_hugoniot
:class: dropdown

1.
$$
\begin{align}
P_2 - P_1 &= - (\rho_2 u_2^2 - \rho_1 u_1^2 ) \text{ , from the momentum equation}\\
 &= - (\rho_1 u_1 \times u_2 - \rho_1 u_1^2 ) \text{ , using the mass equation}\\
&= - \rho_1 u_1(u_2-u_1)
\end{align}
$$

2. As a hint, one should start by showing that $$ \frac{P_2}{\rho_2} - \frac{P_1}{\rho_1} = \frac{P_2 u_2 - P_1 u_1}{\rho_1 u_1},$$ which is clear when we write
$$
\frac{P_2}{\rho_2} - \frac{P_1}{\rho_1} = \frac{\frac{P_2}{\rho_2} \times \rho_2 u_2 - \frac{P_1}{\rho_1} \times \rho_1 u_1}{\rho_1 u_1}
$$

Then

$$
\begin{align}
\frac{P_2}{\rho_2} - \frac{P_1}{\rho_1} &= \frac{P_2 u_2 - P_1 u_1}{\rho_1 u_1}\\
 &= \frac{\left[P_1 - \rho_1 u_1(u_2-u_1)\right]  u_2 - P_1 u_1}{\rho_1 u_1} \text{ , using the equation demonstrated in question 1}\\
&= \frac{u_2 - u_1}{\rho_1 u_1} \left( P_1 - \rho_1 u_1u_2\right)\\ 
&= (u_2 - u_1)\left( \frac{P_1}{\rho_1 u_1} -u_2\right)
\end{align}
$$

3. The energy-conservation equation can be rewritten as

$$
\begin{align}
\frac{1}{2}(u_2-u_1)(u_2+u_1) + \frac{\gamma}{\gamma-1}\left( \frac{P_2}{\rho_2} - \frac{P_1}{\rho_1} \right) &=0 \\
\frac{1}{2}(u_2-u_1)(u_2+u_1) + \frac{\gamma}{\gamma-1} (u_2 - u_1)\left( \frac{P_1}{\rho_1 u_1} -u_2\right) &=0 \\
u_2+u_1 + \frac{2\gamma}{\gamma-1}\left( \frac{P_1}{\rho_1 u_1} -u_2\right) &=0 \\
\frac{u_2}{u_1}\left(1 -  \frac{2\gamma}{\gamma-1}\right) + 1 + \frac{2}{\gamma-1} \frac{\gamma P_1}{\rho_1 u_1^2} &=0 \\
\end{align}
$$

That is

$$
\frac{u_2}{u_1} = \frac{\gamma-1}{\gamma+1} + \frac{2}{\gamma+1}\frac{\gamma P_1}{\rho_1 u_1^2}
$$

4. The Mach number of the shock is such as $M^2 = \rho_1 v_\mathrm{sh}^2 / \gamma P_1 = \rho_1 u_1^2 / \gamma P_1 \gg 1$, thus

$$
\frac{u_2}{u_1} \approx \frac{\gamma-1}{\gamma+1} = 1/4
$$

and

$$
\frac{\rho_2}{\rho_1} \approx \frac{\gamma+1}{\gamma-1} = 4
$$
:::



:::{tip}
**Notions from this chapter**

_Galactic cosmic rays and the supernova paradigm_
- What are Galactic cosmic rays? Which energy range do they cover?
- What are supernovae? Why are they believed to be the main sources of Galactic cosmic rays in the GeV energy range?

_Acceleration processes_
- What are the two Fermi mechanisms? 
- What do the particles bounce off on either side of a shock front?

:::


:::{tip}
**Calculations / demonstrations**

_Hillas criterion: $R<\Gamma\beta L' B' c$_
- What are $R$, $\Gamma$, $\beta$, $L'$, $B'$ and their units? 
- Can I prove this relation in the non-relativistic case?

_Charged particle acceleration: $\dd N / \dd E \propto E^{-(1+ t_\mathrm{acc} / t_\mathrm{esc})}$_
- What are $t_\mathrm{acc}$ and $t_\mathrm{esc}$? 
- Can I prove this from a simplified version of the Fokker-Planck equation? 
- What is the value of the power-law index $1+ t_\mathrm{acc} / t_\mathrm{esc}$ for acceleration in a shock wave at high Mach number?
:::
