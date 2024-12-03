---
short_title: Acceleration mechanisms
authors:
  - jbiteau
keywords: acceleration
---

Acceleration mechanisms
=============================================


Acceleration processes
--------------------------------

### Astrophysical plasmas


Consider a fully ionized plasma, composed e.g. of protons and electrons. Astrophysical plasmas are usually neutral on large scales, i.e. $n_p = n_e = n$ where $n_p$ and $n_e$ are the number density of protons and electrons respectively. 

Neutrality on a large spatial scale, $L$, means $L \gg \lambda_\mathrm{D}$, where $\lambda_\mathrm{D}$ is the Debye length, beyond which charge screening occurs (see Chap. 11.1 in {cite}`2011hea..book.....L`). The Debye length depends on the thermal velocity of the electrons, $v_e$, and the plasma frequency, $\omega_e$:
\begin{align}
\lambda_\mathrm{D} &= \frac{v_e}{\omega_e}\\
     &= \frac{\sqrt{kT/m_e}}{\sqrt{e^2 n/\epsilon_0 m_e}}\\
     &= \sqrt{\frac{kT\epsilon_0}{e^2 n}}\\
     &\approx 27\,\mathrm{km} \times \left(\frac{kT}{13.6\,\mathrm{eV}}\right)^{1/2} \left(\frac{n}{1\,\mathrm{m}^3}\right)^{-1/2} \\
\end{align}

This microphysics-relevant scale can be compared to the much larger astrophysical source sizes in [](05_astroparticle_sources.md#fig:cr_hillas) of chapter [](05_astroparticle_sources.md). 

In a rarefied plasma, it is improbable for a test particle to encounter another particle. The system is said to be colisionless, i.e. the motion of a charged particle is determined by its overall interaction with the plasma and the magnetic fields attached to it.

A few properties of astrophysical plasmas are worth noting here ({cite}`1962pfig.book.....S`). Firstly, astrophysical plasmas have a high conductivity (low resistivity), which is comparable to that of metals. This high conductivity leads to the short-circuiting of any large-scale electric field and to the phenomenon of magnetic-flux freezing, i.e. magnetic field lines behave as if anchored into the plasma.

A second notable feature of a plasma is the speed at which disturbances propagate along the field lines. The equivalent of the speed of sound, called the Alfvén speed, is provided by the ratio of the magnetic energy density, $u_B$, to the mass density of the medium $\rho = n m_p$, i.e. $v_\mathrm{A} \propto \sqrt{\frac{u_B}{\rho}}$. More specifically, $v_\mathrm{A} = \frac{B}{\sqrt{\rho\mu_0}}$ that is
\begin{align}
\frac{v_\mathrm{A}}{c} &= \frac{B}{\sqrt{n m_pc^2\mu_0}}\\
     &= 7 \times 10^{-3} \times \left(\frac{B}{10^{-10}\,\mathrm{T}}\right) \left(\frac{n}{1\,\mathrm{m}^3}\right)^{-1/2}
\end{align}

The diffusion of charged particles in an astrophysical plasma is determined by their resonance with magnetic-field perturbations such as Alfvén waves and other hydromagnetic waves.


### Fermi mechanisms


Electromagnetic interaction is responsible for the acceleration of charged particles in astrophysical environments, via the Lorentz force $\vec{F} = q(\vec{E} + \vec{v}\times\vec{B})$. Since the magnetic term does not work, an effective electric field is required for acceleration. Note, however, that an electromagnetic field such that $\vec{E} = \vec{0}$ and $\vec{B} \neq \vec{0}$ can always be transformed to $\vec{E'} \neq \vec{0}$ and $\vec{B'} \neq \vec{0}$ through a change of frame. The relevant quantities for discussing the different types of acceleration mechanisms are the Lorentz invariants of the electromagnetic tensor $F_{\mu\nu}$, namely $F_{\mu\nu}F^{\mu\nu} = 2\left[ (Bc)^2-E^2 \right]$ and $\mathrm{det}(F) = \vec{E} \cdot \vec{B}$ ({cite}`2019PhRvD..99h3006L`).

The acceleration mechanism most commonly used by humans on Earth is linear acceleration, i.e. $\vec{E} \cdot \vec{B} \neq \vec{0}$ or $E^2 > (Bc)^2$. These cases, for which ideal magnetohydrodynamics does not apply (ideal Ohm's law with no resistive term: $\vec{E} + \vec{v}\times\vec{B} = \vec{0}$), are only found in a limited number of astrophysical environments, such as the gaps in the magnetospheres of pulsars.

The case more generally found in astrophysical environments, for which $E^2 < (Bc)^2$ and $\vec{E} \cdot \vec{B} = \vec{0}$, allows us to describe acceleration by shock waves, magnetic turbulence or in sheared flows. Two seminal publications by Enrico Fermi described the concepts in the 1950s ({cite}`1949PhRv...75.1169F,1954ApJ...119....1F`). In both cases, acceleration results from particle scattering on magnetic-field perturbations such as Alfvén waves, which move with a characteristic velocity $v_\mathrm{A}$. A head-on / receding collision with a pertuburation leads to a gain / loss of momentum $\frac{\Delta p}{p} \approx \pm \frac{v_\mathrm{A}}{c}$. In the case of an isotropic distribution of the velocities of the scattering centers, found for example in a turbulent magnetic field, head-on collisions are more frequent by a factor $\frac{v_\mathrm{A}}{c}$, so that the rate of energy gain is favored over the rate of loss. This mechanism is known as second-order Fermi acceleration. In the case where only head-on collisions take place, for the geometry of a contracting magnetic bottle found for example on either side of a shock front, the mechanism is said to be first-order.

The denomination of first- and second-order Fermi acceleration is more explicit when we consider the acceleration time, $t_\mathrm{acc}$, which depends on the mean free path between scattering centers, $l_\mathrm{mfp}$:
\begin{align}
t_\mathrm{acc}^{-1} &\approx \frac{c}{l_\mathrm{mfp}} \times \left\langle \frac{\Delta p}{p} \right\rangle\\
&\approx \left\{\begin{array}{lr}
        \frac{c}{l_\mathrm{mfp}} \times \left(\frac{v_\mathrm{A}}{c} \right), & \text{for first order Fermi acceleration}\\
        \frac{c}{l_\mathrm{mfp}} \times \left(\frac{v_\mathrm{A}}{c} \right)^2, & \text{for second order Fermi acceleration}
        \end{array}\right.
\end{align}

Spectrum of accelerated particles
--------------------------------

### The Fokker-Planck equation

The equation that governs the evolution of the momentum and position of a collection of particles is a partial differential equation known as the diffusion-loss equation. Its formal derivation uses the diagram provided in [](fig:coord_space_diagram) (see also chapter 7.5 in {cite}`2011hea..book.....L`). The reasoning is limited here to one spatial and one momentum dimension, but can easily be extended to 6D if one wishes to consider anisotropic phenomena such as the different diffusion coefficients along and perpendicular to a magnetic-field line.


:::{figure}  ../../images/Fig7.6_Longair.svg
:name: fig:coord_space_diagram
:align: center
:width: 60%

Coordinate space diagram of momentum against spatial coordinate. Adapted from chapter 7.5 in {cite}`2011hea..book.....L`.
:::

Consider an initial Maxwellian momentum distribution for a number of particles $n(x, p, t)\dd x \dd p$. The 2D phase-space density, $n$, is analoguous to the 6D phase-space density $\dd N/\dd^3 x\dd^3 p$ defined in chapter [](05_astroparticle_sources.md). 

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
where $Q$ is the source term characterizing the injection of new particles and $\tau$ is the time scale of catastrophic energy losses, relevant e.g. to radioactive decay, spallation, or simply the escape of the particle from the region of interest.

$\phi_p$ is the flux of particles of momentum between $p$ and $p + \dd p$ through $\dd x$. Assuming, for simplicty, no momentum diffusion, it reads:
$$
\phi_p = n \dot p,
$$
where $\dot p = \frac{p}{t_\mathrm{acc}} - \frac{p}{t_\mathrm{loss}}$ for Fermi acceleration at a rate $t_\mathrm{acc}^{-1}$ and continuous energy losses, such as synchrotron losses, at a  rate $t_\mathrm{loss}^{-1}$.

$\phi_x$ is the flux of particles of position between $x$ and $x + \dd x$ through $\dd p$:
$$
\phi_x = v_\mathrm{adv} n -D \frac{\partial n}{\partial x},
$$
i.e. an advection term, with $v_\mathrm{adv}$ the advection velocity, and a diffusion term from Fick's law with $D$ the diffusion coefficient. For isotropic diffusion, $D = \frac{1}{3} c l_\mathrm{mfp}$. Writing $\eta = l_\mathrm{mfp}/r_\mathrm{g}$ the number of gyroradii in a mean free path:
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
There is no term explicitly dependent on $c$ in the Fokker-Planck equation. If we consider diffusion only and constant diffusion coefficient, the mean displacement reached at time $t$ is $r = \sqrt{4Dt}$ that is an effective velocity $v = r/t = \sqrt{4D/t}$, which can be superluminal (!) at small $r$ and $t$. This is a known problem of diffusion equations, which is further discussed e.g. in {cite}`2009ApJ...693.1275A` in the context of astroparticle physics.
:::

### Where power laws come from

The simplest application of the Fokker-Planck equation is highly relevant to understanding acceleration. Consider a stationary system, with no diffusion or advection, no energy loss, for which catastrophic losses are limited to escape ($\tau = t_\mathrm{esc}$) and with particle injection in the past, then:

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

The value of the index can be determined with multiple approaches, depending on the considered astrophysical environment. In the case of shock acceleration or magnetic reconnection, one can use box models such as developped by {cite}`1999A&A...347..370D,2012MNRAS.422.2474D` and show that $\frac{t_\mathrm{acc}}{t_\mathrm{esc}} = \frac{3}{|r-1|}$, where $r=\rho_2/\rho_1$ is the compression ratio between the downstream medium and the upstream medium.

For a shock acceleration at high Mach number and assuming a plasma described as a perfect gaz of adiabatic index $\gamma = \frac{c_P}{c_V}$, the compression ratio is equal to $r = \frac{\gamma +1}{\gamma -1}$. As $\gamma = 5/3$ for a monoatomic gaz of protons or electrons, we get $r = \frac{\frac{5}{3} +1}{\frac{5}{3} -1} = 4$. In such a system, the power-law spectrum has an index $s = 1 + \frac{3}{|4-1|} = 2$, that is:

$$
\frac{\partial N}{\partial p} \propto n \propto \left( \frac{p}{p_0}\right)^{-2}
$$

The universality of this power law of index 2, whose presence is inferred in many non-thermal astrophysical systems, is one of the great successes of diffusive shock acceleration theory.
