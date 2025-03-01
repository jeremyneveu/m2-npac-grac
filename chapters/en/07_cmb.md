---
short_title: Thermal history
authors:
  - jneveu
keywords: cosmological microwave background, CMB, neutrinos, nucleosynthesis
---

Thermal history of the Universe
===============================

The expansion of the Universe is now well described by the flat $\Lambda$CDM model ($\Omega_k^0=0$). The proportions of each of these components are now estimated at {cite}`Planck2018`:
$$ \Omega_\Lambda^0 = 0.685,\quad \Omega_m^0=0.315$$

In this chapter, we will study the thermal history of the Universe and the evolution of its composition. Up to now in this course, non-relativistic matter has been treated as a single entity, slowing down the expansion of the Universe through its gravitational interaction. But to study its evolution with temperature and its interactions with the other components, we need to separate them into two contributions: dark matter $\Omega_{c}^0$ and baryonic matter [^baryons] $\Omega_b^0$. In 1933, while studying the Coma cluster, astrophysicist Fred Zwicky showed that the mass deduced from the motion of the seven galaxies that make up the cluster was 400 times greater than the mass deduced from counting luminous objects. This measurement was repeated in 1936 on the Virgo cluster, this time giving a factor of 200. However, these somewhat inaccurate measurements were forgotten until the 1970s, when astronomer Vera Rubin observed that the rotational speed of the stars in the Andromeda Galaxy was much higher than its observed luminous mass would suggest {cite:p}`Rubin1970`. The observation is quickly repeated for many galaxies: part of the matter making up the galaxy is therefore dark matter, escaping detection and often representing the majority of the total mass of galaxies. The presence of abundant dark matter can even be seen in the amplitude of the temperature anisotropies of the cosmic microwave background (see end of chapter). Today, it is estimated that the proportion of these two forms of cold matter is {cite}`Planck2018`:
$$ \Omega_{c}^0=0.264,\quad \Omega_b^0=0.049$$

Description of the primordial Universe
--------------------------

### The Cosmic Microwave Background

If the Universe is expanding today, then it was smaller in the past. Cosmic expansion reduces the momentum of particles by a factor $\propto a^{-1}$ and the density of particles by another $a^{-3}$. In the early days, the Universe was therefore hot and dense. There must therefore have been a moment when the Universe was hot enough for atoms to be ionised, and therefore in a plasma state where photons interact with free electrons. Through these frequent interactions, if thermodynamic equilibrium is reached the radiation follows a blackbody spectrum defined by the temperature of the medium (<wiki:Planck's_law>). During the transition from the plasma state to the neutral state, at around $3\,000\,\kelvin$ for a hydrogen gas, the Universe suddenly becomes transparent and photons propagate freely. This high-temperature black-body radiation is released at this instant. This so-called fossil radiation has been cooled by the expansion of the Universe. This cosmic microwave background was predicted in 1948 by Ralph Alpher, Robert Herman {cite:p}`Alpher1948` and George Gamow {cite:p}`Gamow1948` around $5,\kelvin$, and discovered fortuitously by Arno Penzias and Robert Wilson in 1964 {cite:p}`Penzias1965a,Penzias1965b` at a temperature of $3.5\,\kelvin$ ([](#fig:cmb_antenna)). 

:::{figure} ../../images/Horn_Antenna.jpg
:name: fig:cmb_antenna
:align: center
:width: 80%

The 15-metre Holmdel horn antenna at Bell Telephone Laboratories in Holmdel, with Arno Penzias and Robert Wilson, which led to the discovery of the CMB. It was built in 1959 as part of work on communications satellites for NASA ECHO I (By NASA, restored by Bammesk).
:::

The spectrum of the cosmic microwave background has been characterised thanks to the COBE satellite, and its temperature has now been established at {cite:p}`Mather1999`:
$$T_0 = 2.725\pm 0.002\,\kelvin$$
by modelling its data by Planck's radiation law:
\begin{equation}
  I_\nu(\nu, T_0) = \frac{2 h \nu^3}{c^2}\frac{1}{\exp(h\nu/k_B T_0) - 1}
\end{equation}
This is the best black-body radiation ever detected ([](#fig:cmb_cn)). The cosmic microwave background radiation (CMB) is probably the most direct evidence that the Universe was indeed in the form of a hot, dense plasma at equilibrium in the distant past.

:::{figure} ../../images/cmb_cn.jpg
:name: fig:cmb_cn
:align: center
:width: 60%

Fitting a blackbody model to various data measuring the flux from the cosmic microwave background {cite:p}`Mather1999`.
:::


### Orders of magnitude

Let's go well beyond the redshift of the last scattering surface, and consider the Universe at, say, $z \sim 10\,000$. What can we say?


#### Temperature

For a gas of photons, we know that :
\begin{equation}
\epsilon_\gamma \propto a^{-4}
\end{equation}
At thermal equilibrium, the energy density of a gas of photons is the integral of Planck's law:
\begin{equation}
\epsilon_\gamma = \frac{2 \pi^2 (k_B T)^4}{15 h^3 c^3}
\end{equation}
The equilibrium temperature of the photons $T_\gamma$ evolves as follows:
\begin{equation}
T_\gamma \propto a^{-1}
\end{equation}
The photon temperature $T_\gamma$ can therefore be used as a time parameter like $a$ or $z$ if $T$ is isotropic.

:::{exercise} CMB redshift
:label: exo:Tdec

Photons decoupled from matter when the Universe shifted from plasma to neutral at $z_{athrm{dec}}. \approx 1090$. They now form what is known as the cosmic microwave background. What was the temperature $T_{mathrm{dec}}$ of the photons at the moment of decoupling?

:::

:::{solution} exo:Tdec
:class: dropdown

\begin{equation}
a_{\mathrm{dec}} T_{\mathrm{dec}} = a_0 T_0 \Rightarrow T_{\mathrm{dec}} = (1+z_{\mathrm{dec}}) T_0 = 2972\,\kelvin
\end{equation}

:::

#### Densities

We can now calculate the current contribution of CMB photons to the critical density of the universe using the blackbody temperature :
\begin{equation}
\Omega_{\gamma}^0= {\epsilon_\gamma^0 \over c^2 \rho^0_c}= {4 \sigma_S T_0^4 \over c^3}{8 \pi \GN \over 3 H_0^2} \sim 5 \times 10^{-5}
\end{equation}
It is therefore a negligible energy density compared to cold matter and dark energy.
Of course, other ultra-relativistic particles such as neutrinos contribute to the remaining $\Omega_r^0$. But with 3 massless neutrinos, we would only end up with $\Omega_r^0 \sim 9 \times 10^{-5}$ as we will see at the end of the chapter.

We define _equivalence_ as the moment when relativistic and non-relativistic matter are in equal proportion.
Let's calculate the redshift $z_{\rm eq}$ at the moment when the proportions of matter and radiation are equal:
\begin{equation}
 \rho_r(z)= \rho_r^0 (1+z)^4\text{ and } \rho_m(z) = \rho_m^0(1+z)^3
 \end{equation} 
We deduce that :
\begin{equation}
\frac{\rho_r(z)}{\rho_m(z)} = \frac{\rho_r^0}{\rho_m^0}(1+z) = \frac{\Omega_r^0}{\Omega_m^0}(1+z)
\end{equation}
\begin{equation}
\frac{\rho_r}{\rho_m} = 1 = \frac{\Omega_r^0}{\Omega_m^0}(1+z_{\rm eq}) \Rightarrow z_{\rm eq} = \frac{\Omega_m^0}{\Omega_r^0}-1 \approx \frac{0.3}{9\times 10^{-5}}-1 \approx 3332
\end{equation}
So at $z> z_{\mathrm{eq}}$, the contents of the Universe are dominated by relativistic matter.

#### Photons

Let's now concentrate on the properties of photons. We know that $T_\gamma \propto a^{-1}$, so at $z=10^4$ their temperature is :
\begin{equation}
  T_\gamma(z=10\,000) = (1+z)T_0 \approx 2.726\times 10^{4}\,\kelvin
\end{equation}
The average energy of the photons at $z=10^4$ is :
\begin{equation}
  k_B T_\gamma(z) = (1+z)k_B T_0 \approx 2.34\,\mathrm{eV}
\end{equation}
By dimensional analysis, the density of photons at a redshift z is, apart from the numerical factors we will see later :
\begin{equation}
  n_\gamma(z) \sim \epsilon_\gamma(z)/ (k_B T_\gamma(z)) \sim \frac{\left[(1+z)k_B T_0\right]^3}{c^3 \hbar^3}\sim 
\left\lbrace
\begin{array}{ll}
10^{21}\ \gamma / \mathrm{m^3} & \text{à}\ z=10^4 \\
10^{9}\ \gamma / \mathrm{m^3} & \text{à}\ z=0 \
\end{array}
\right.
\end{equation}

#### Baryons

Let's now estimate the density of baryons (particles with 3 quarks like protons and neutrons) at $z \sim 10\,000$. The baryon density today is $\Omega_b^0 = 0.049$. With a critical density of $\rho_c^0 \sim 6\,m_p / m^{3}$, this gives approximately $n_b^0 \approx 0.3\,\mathrm{baryons / m^{3}}$ today, then at $z \sim 10\,000$ :
\begin{equation}
  n_b(z) \approx \Omega_b^0 \rho_c^0 (1+z)^3/m_p \approx 3\times 10^{11} \mathrm{baryons} / \mathrm{m^3}
\end{equation}
The Universe is therefore largely dominated by photons in terms of particle density, and this proportion remains constant throughout the history of the Universe:
\begin{equation}\label{eq:eta}
\boxed{\eta= \frac{n_b(z)}{n_gamma(z)} \sim \frac{\Omega_b^0 \rho_c^0 c^3 \hbar^3}{(k_B T_0)^3} \sim 10^{-9}}
\end{equation}


#### Expansion rate

The value of the Hubble expansion rate can be deduced from the Friedmann equation:
\begin{equation}
  H(z) = H_0 \left( \Omega_m^0(1+z)^3 + \Omega_r^0 (1+z)^4 + \Omega_\Lambda^0\right)^{1/2}
\end{equation}
Let's take the canonical values $\Omega_m^0 = 0.315$, $\Omega_\Lambda^0 = 0.685$ and $\Omega_r^0 \sim 9 \times 10^{-5}$ for the relativistic matter density (photons and neutrinos). At $z \sim 10\,000$, this gives :
\begin{equation}
  H(z) \approx 10^6 \times H_0
\end{equation}
The expansion of the Universe was much faster than it is today!

(lpm_photons)=
#### Mean photon free path

Finally, we can look at the mean free path of photons. Photons interact preferentially with electrons by Thomson scattering $e^- + \gamma \rightarrow e^- + \gamma$ and a good approximation of the mean free path of photons is given by :
\begin{equation}\label{eq:lpm_thomson}
 l_{T} =\frac{1}{\sigma_T n_e}
\end{equation}
where $\sigma_T$ is the effective Thomson scattering cross section ($6.6529times 10^{-29}\ \mathrm{m^2}$). For the electron density, let's assume that since the Universe is neutral, there is one electron for each proton, so $n_e = n_p \approx 0.3\,e^-/\mathrm{m^{3}}$. The typical time between two $\tau_T$ interactions is then :
\begin{equation}
 \tau_T = \frac{l_T}{c} = \frac{1}{\sigma_T n_e c} \approx 5\times 10^{12},\mathrm{yr} \gg t_H = \frac{1}{H_0}
\end{equation}
today if matter is in an ionised state, and at the time :
\begin{equation}
\tau_T= \frac{1}{\sigma_T n_e(1+z)^3 c} \approx 5\,\mathrm{yr} \ll \frac{1}{H(z)} \sim 10^{-6} t_H \sim 10\,000\,\mathrm{yr}
\end{equation}

So we can see that, in the past, the interactions between matter and photons were sufficiently frequent to reach thermal equilibrium in a short time, given the expansion of the Universe. But today, even if all matter were ionised, these photons no longer interact with it. The CMB photons are therefore _not_ in thermal equilibrium with anything else today. The vast majority of CMB photons have never been in contact with particles since they were emitted. 
However, this absence of interactions has preserved the original shape of the CMB spectrum, which has only been affected by the red shift. A photon detected at frequency $\nu$ was originally emitted at frequency $(1+z)\nu$. In other words, the original spectrum was {cite:p}`Condon2018`:
\begin{equation}
I_\nu(\nu, T_0, z) = \frac{2 h \nu^3}{c^2}\frac{1}{\exp(h\nu/(1+z)k_B T_0) - 1}
\end{equation}
i.e. still black-body radiation, but with a temperature $(1+z) T_0$.


### Big Bang scenario

The Universe at $z \approx 10\,000$ was much hotter and denser. At this temperature, atoms are ionised and we therefore have a plasma.
Just as today, the density of photons was significantly greater than that of baryons.
Finally, interactions between photons and charged particles were much more frequent (several per Hubble time), so it is quite logical to consider the Universe as a plasma in thermal equilibrium.

On the basis of this description, we can sketch out a scenario for the evolution of primordial plasma by cataloguing the various physical phenomena that can occur as it cools. Here is a non-exhaustive summary.

First of all, at the end of inflation (about $10^{-34}\,$s after the Big Bang), there must have been a phase known as _baryogenesis_, where all the particles and antiparticles are created with a slight advantage for matter over antimatter leading to $\eta \sim 10^{-9}$. Below a temperature of about $100\,\GeV$ ($t \sim 20\,$ps), the electroweak phase transition takes place, giving mass to the particles and giving rise to the Z-gauge bosons, W$^\pm$. Under $150\,\MeV$ ($t\sim 20\,\mathrm{\mu s}$), this is the QCD phase transition: the strong interaction takes over from the thermal effects. The quarks and gluons coagulate to form baryons (three quarks) and mesons (two quarks). Then, $6\,\mathrm{s}$ later, electrons and positrons annihilate as the temperature of the photon bath falls below the mass of the electron $T < m_e=511\,\keV$. During the first three minutes of the Universe ($T > 100\,\keV$), the atomic nuclei of the light elements are formed. After 380,000 years, the electrons bind to the atomic nuclei ($e^- + p \rightarrow \mathrm{H} + \gamma$), this is _recombination_, and the photons decouple from the matter ($\tau_T \ll 1/H)$. Free to propagate, these photons form the cosmic microwave background and provide a snapshot of the primordial plasma at the end of recombination.


Statistical thermodynamics at equilibrium
-------------------------------

We now turn to a more detailed description of what happened in the primordial Universe using statistical physics. 

### Statistical description

Let's model the contents of the Universe as a gas of weakly interacting particles. We can then use the formalism of statistical physics and describe the gas by the positions and momentum of all its particles, defined on the space $\vec{x}, \vec{p}\}$. 

In a gas of particles _at thermodynamic equilibrium_, the number of particles that can occupy an energy state $(\vec{x}, \vec{p})$ follows a statistical distribution function $f(\vec{x}, \vec{p}, t)$. In cosmology, because of the homogeneity of the Universe, $f$ cannot depend on the position $\vec{x}$. Furthermore, due to isotropy, $f$ can only depend on the norm of the momentum $p \equiv \Vert \vec{p}\Vert$ and not on its direction.

Armed with the distribution functions, we can deduce the macroscopic properties of the gas by evaluating the probability of occupying the states of the system. But what are they? First of all, quantum mechanics dictates that the density of states in phase space is finite. In fact, if we consider a box of size $L$, with periodic conditions and solve Schrodinger's equation, we obtain that the possible values of the momentum are :
\begin{equation}
  \vec{p} = \frac{h}{L}\left(n_x \vec{e}_x + n_y \vec{e}_y + n_z \vec{e}_z\right), \ \ n_i = 0, \pm 1, \pm 2, \ldots
\end{equation}
where $\vec{e}_x, \vec{e}_y$ and $\vec{e}_z$ are the unit vectors and $h$ is Planck's constant. Consequently, in momentum space, there is one state per elementary cube of volume $h^3/L^3$. The density of state in momentum space is therefore $L^3/h^3$ :
Secondly, there is only one particle in the quantum box, so only one state of position: in the space of positions, the density of state is $1/L^3$. In total, if the particle has $g$ internal degrees of freedom, the density of state in phase space is :
\begin{equation}
 g \times \frac{L^3}{h^3} \times \frac{1}{L^3} = \frac{g}{h^3} = \frac{g}{(2\pi\hbar)^3}
\end{equation}
 The density of state is therefore independent of the volume $L^3$. It remains the same for an arbitrarily large system. 

The macroscopic properties (number density, energy density, pressure) are deduced from the probability of occupation of the states $f(\vec{x}, \vec{p}, t)$ and the density of state of the phase space. The volume density of momentum particles between $p$ and $p+\dd p$ is for example given by :
\begin{equation}\label{eqn:fweights}
 n(p) = \frac{g}{(2\pi\hbar)^3} f(p) \dd^3\mathbf{p}
\end{equation}

The mean particle density of the gas is:
\begin{equation}\label{eqn:number_density_general}
  \boxed{n = \frac{g}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p,t)}
\end{equation}

For the mean energy density, since we consider that the particles interact weakly and are not confined, then the energy levels $E(p)$ are those of a free particle $E(p)=\sqrt{p^2c^2 + m^2 c^4}$. To obtain the energy density of the gas, we simply sum the energy levels weighted by their probability of occupation: 
\begin{equation}\label{eqn:energy_density_general}  
  \boxed{\epsilon = \rho c^2 = \frac{g}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p,t) E(p) = \frac{g}{(2\pi\hbar)^3} \dd^3\mathbf{p} f(p,t) \sqrt{p^2c^2 + m^2 c^4}}
\end{equation}

We can obtain the gas pressure in the same way: 
\begin{equation}\label{eqn:pression_generale}
  \boxed{P = \frac{g}{(2\pi\hbar)^3} \int \dd^3\mathbf{p} f(p,t) \frac{p^2}{3E}}
\end{equation}

In the end, the energy-momentum tensor for a set of quantum particles can be written :
\begin{equation}
\boxed{T^{\mu\nu}=\frac{g}{(2\pi\hbar)^3}\int{\dd^3\mathbf{p} f(p,t) \frac{p^\mu p^\nu}{p^0}}}
\end{equation}
Note that this formula is the quantum version in the continuous limit of the formula [](#eq:TmunuGaz) obtained for a classical perfect gas.

:::{note} Why $p^2/3E$ ?

Let's consider a surface element $\delta A$. We denote its unit vector $\hat{n}$. The particles of velocity $v$ which hit $\delta A$ between $t$ and $t + \delta t$ are located in a spherical shell around $\delta$.
between the radii $vt$ and $v(t + \delta t)$.

\begin{equation}
  \dd N = \frac{g}{(2\pi\hbar)^3} f(E) R^2 v \dd t \dd\Omega 
\end{equation}

Not all these particles reach the surface. Only those whose velocity is directed towards $\delta A$, i.e. those whose velocity vector is in the solid angle subtended by $\delta A$. Therefore :
\begin{equation}
    \dd N_{hit} = \dd N \times \frac{|\hat{v}\cdot\hat{n}|}{4\pi R^2} = \frac{g}{(2\pi\hbar)^3} f(E) \frac{\hat{v}\cdot\hat{n}}{4\pi}\ \dd A\dd t\dd \dd \Omega
\end{equation}  
Let's assume that the interactions are elastic and that each particle transfers a momentum $2|\vec{p}\vec{n}|$ to the surface. The resulting pressure is :
\begin{equation}
  \begin{split}
    \dd P(v) & = \int \frac{2|\vec{p}\cdot\vec{n}|}{\dd A\ \dd t} \dd N_A \\ & = \frac{2|\vec{p}\cdot\vec{n}|}{\dd A\ \dd t} \dd N_A \\
    & = \frac{g}{(2\pi\hbar)^3} f(E) \frac{p^2}{2\pi E} \int \cos^2\theta \sin\theta \dd\theta \dd\phi \\ & = \frac{g}{(2\pi\hbar)^3} f(E) \\
    & = \frac{g}{(2\pi\hbar)^3} f(E) \frac{p^2}{3E}
  \end{split}  
\end{equation}

:::


#### Kinetic equilibrium

When particles can exchange energy and momentum frequently through elastic collisions, the gas reaches a state of maximum entropy, called kinetic equilibrium. The distribution functions $f(p,t)$ can be obtained by evaluating the entropy of the gas ($S = k_B \ln \Omega$) and maximising it, for a given total energy and a given total number of particles.

Depending on the fermionic or bosonic nature of the particles in the gas, the combinatorics giving the occupation probabilities of all the $\Omega$ microstates is different because of the Pauli exclusion principle. At a fixed total energy and total number of particles, after using the Lagrange multipliers, these constraints impose that the distribution functions at thermodynamic equilibrium are :
\begin{equation}
  \boxed{\text{Fermi-Dirac:\ } f(p) = \frac{g}{\exp\left({\dfrac{E(p) - \mu}{k_B T}}\right) + 1}}
\end{equation}
\begin{equation}
  \boxed{\text{Bose-Einstein:\ } f(p) = \frac{g}{\exp\left({\dfrac{E(p) - \mu}{k_B T}}\right) - 1}}
\end{equation}
with $T$ the temperature of the gas, $\mu$ the chemical potential of the species and $g$ its number of internal degrees of freedom (for example the number of spin states). They give the number of particles that can occupy an energy state $E$, depending on whether they are bosons or fermions, at thermodynamic equilibrium.

At high temperatures, we find the Maxwell-Boltzmann distribution:
\begin{equation}
  \boxed{\text{Maxwell-Boltzmann:\ }f(p) = g\exp\left(-{\frac{E(p) - \mu}{k_B T}}\right)}
\end{equation}
valid for fermions and bosons.

The Fermi-Dirac and Bose-Einstein distribution functions depend on two parameters: the temperature of the gas, $T$, and the chemical potential of the species $\mu$, which characterises the variation in entropy or energy when the number of particles varies (see box below).

If the gas contains several interacting species, each species $i$ is described by its own distribution function, its own chemical potential $\mu_i$. chemical potential $\mu_i$, and possibly (if decoupled) its own temperature $T_i$.  From this we can deduce the number density, energy density and temperature of each species. 

If all the species are in kinetic equilibrium and share the same temperature: $T_i = T$, the system has reached _thermal equilibrium_.


#### Chemical equilibrium

:::{note} Chemical potential

Changes in the energy of a system can be expressed as a function of its entropy, volume and temperature:
\begin{equation}
\dd U = T \dd S - P \dd V + \mu \dd N
\end{equation}
or :
\begin{equation}
\dd S = \frac{\dd U}{T} + \frac{P}{T} \dd V - \frac{\mu}{T} \dd N
\end{equation}

Consider two systems $\mathcal{S}_1$ and $\mathcal{S}_2$ at temperatures $T_1$ and $T_2$ brought into contact.  If the two systems are isolated :
1. the energy the total energy of ($S_1+S_2$) is constant 
$$\dd U = \dd U_1 + \dd U_2 = 0 \Rightarrow \dd U_1 = -\dd U_2$$
2. the entropy of ($S_1 + S_2$) reaches a maximum 
$$\dd S = \dd S_1 + \dd S_2 = 0 \Rightarrow \dd U_1/T_1 + \dd U_2/T_2 = 0$$
which gives $T_1 = T_2$ at equilibrium.

Now consider that $\mathcal{S}_1$ and $\mathcal{S}_2$ can exchange particles (keeping the total number of particles constant). We have :
1. $\dd N = \dd N_1 + \dd N_2 = 0 \Rightarrow \dd N_1 = - \dd N_2$ 
2. and the entropy of $(\mathcal{S}_1 + \mathcal{S}_2)$ reaches a maximum, which gives :
$$-\frac{\mu_1}{T} \dd N_1 - \frac{\mu_2}{T} \dd N_2 = 0$$
hence $\mu_1 = \mu_2$. At equilibrium, the two chemical potentials are equal.

Let's now consider the case of a chemical reaction: 
$$1 + 2 \rightleftharpoons 3 + 4$$
i.e. the case where four systems $S_1$, $S_2$, $S_3$ and $S_4$ are brought into contact. Using the same reasoning, we can show that :
1. they reach the same equilibrium temperature $T$, and 
2. and that at equilibrium we have :
$$\mu_1 + \mu_2 = \mu_3 + \mu_4$$

:::

We saw in the box above that if several species interact through a reaction, for example :
\begin{equation}
  \nu_1 X_1 + \nu_2 X_2 + \ldots \rightleftharpoons \nu'_1 Y_1 + \nu'_2 Y_2 + \ldots
\end{equation}
and reach chemical equilibrium (i.e. the state of maximum entropy), the chemical potentials satisfy: 
\begin{equation}
  \sum_i \nu_i \mu_i = \sum_j \nu'_j \mu_j 
\end{equation}
plus any conservation equation imposed by a conserved charge (number of particles, electric charge, baryonic charge, etc.).

For photons, there is no conserved charge. Even the number of photons is not conserved.  For example, we have Compton double scattering $e^- + \gamma \rightarrow e^- + \gamma + \gamma$ or Bremstrahlung $e^- + p \rightarrow e^- + p + \gamma$. Hence :
\begin{equation}
  \mu_\gamma = 0
\end{equation}

Particles and antiparticles have opposite charges, hence, _at equilibrium_ :
\begin{equation}
  \mu_X = -\mu_{\bar{X}}
\end{equation}
The reaction $X + \bar{X} \rightleftharpoons \gamma + \gamma$ can also be used to reach the same conclusion.

To summarise: 
- A system composed of different species has reached kinetic equilibrium if it has reached a state of maximum entropy described by a Fermi-Dirac or Bose-Einstein distribution function. 
- A system composed of several species interacting via one or more chemical reactions has reached chemical equilibrium if it has reached a state of maximum entropy, where the sum of the chemical potentials of the reactants is equal to the sum of the chemical potentials of the products. 
- A system has reached thermodynamic equilibrium if it has reached chemical equilibrium and if all the species share the same temperature $T$, the _temperature of the Universe_.


### Density and pressure of fermions and bosons

We now have everything we need to calculate the particle density, energy density and pressure of the constituents of the Universe. Chemical potentials can be neglected at high temperatures ($\mu \ll T$), and the equations [](#eqn:number_density_general), [](#eqn:energy_density_general) and [](#eqn:pression_generale) can be rewritten:
\begin{equation}
  \begin{split}
    n &= \frac{g}{2\pi^2\hbar^3} \int \dd p \frac{p^2}{\exp\left(\sqrt{p^2c^2 + m^2 c^4}/k_B T\right) \pm 1} \\
    \epsilon &= \frac{g}{2\pi^2\hbar^3} \int \dd p \frac{p^2 \sqrt{p^2c^2 + m^2 c^4}}{\exp\left(\sqrt{p^2c^2 + m^2 c^4}/k_BT\right) \pm 1} \\
    P &= \frac{g}{2\pi^2\hbar^3} \frac{1}{3} \int \dd p \frac{p^4}{\sqrt{p^2c^2 + m^2 c^4} \left[\exp\left(\sqrt{p^2c^2 + m^2c^4}/k_B T\right) \pm 1\right]}\\    
  \end{split}
\end{equation}
with the sign $+$ for fermions and the sign $-$ for bosons.

In the general case, the above integrals must be calculated numerically. However, there are two interesting limits, which help us to understand the physical processes involved: the case where the particles are relativistic ($k_B T \gg m c^2$) and the opposite case of non-relativistic species ($k_B T \ll m c^2$). 

Before continuing, let us define: $x \equiv m c^2/k_B T$ and $\xi \equiv pc/k_B T$,
we can then rewrite $n$ and $\rho$ above as :
\begin{equation}
  \begin{split}
    n &= \frac{g(k_BT)^3}{2\pi^2\hbar^3 c^3} I_\pm(x)\ \ \ \mathrm{with} \ I_\pm(x) = \int_0^\infty \dd \xi \frac{\xi^2}{\exp\left(\sqrt{\xi^2 + x^2}\right) \pm 1} \\
    \epsilon &= \frac{g(k_BT)^4}{2\pi^2\hbar^3 c^3} J_\pm(x)\ \ \ \mathrm{with}\ J_\pm(x) = \int_0^\infty \dd \xi \frac{\xi^2 \sqrt{\xi^2 + x^2}}{\exp\left(\sqrt{\xi^2 + x^2}\right) \pm 1} \\
  \end{split}
\end{equation}

#### Relativistic limit

In the relativistic limit, we have $x\ll 1$ and the integrals $I_\pm(0)$ and $J_\pm(0)$ can be calculated exactly:
$$
J_-(0) = \frac{\pi^4}{15},\quad J_+(0) = \frac{7}{8}\frac{\pi^4}{15},\quad I_-(0) = 2 \zeta(3),\quad I_+(0) = \frac{3}{2}\zeta(3)
$$
where $\zeta$ is the Riemann function.



We find :
\begin{equation}
  \boxed{\begin{aligned}
           &        \mathrm{Bosons}                       &  \mathrm{Fermions} \\
    n = & \frac{g \zeta(3)(k_BT)^3}{\pi^2\hbar^3 c^3}   & n =\frac{3}{4} \frac{g \zeta(3)(k_BT)^3}{\pi^2\hbar^3 c^3}  \\
    \epsilon = & \frac{g\pi^2(k_BT)^4}{30\hbar^3 c^3}        & \epsilon =\frac{7}{8}\frac{g \pi^2(k_BT)^4}{30\hbar^3 c^3} \\
  \end{aligned}}
  \label{eqn:n_rho_relativistic_limit}
\end{equation}
We can see that the particle and energy densities are identical for relativistic bosons and fermions to within a numerical factor. Furthermore, photons are bosons with $g_\gamma=2$ possible polarisations, so we have re-demonstrated Stefan-Boltzmann's law.

To calculate the pressure, we have $p^2 / E \sim p$ for relativistic particles, so :
\begin{equation}
  P = \frac{1}{3} \frac{g}{2\pi^2\hbar^3 c^3} (k_BT)^4 \int \dd \xi \frac{\xi^3}{\exp\xi \pm 1} = \frac{1}{3} \frac{g}{2\pi^2\hbar^3 c^3} (k_BT)^4 J_\pm(0) = \frac{epsilon}{3}
  \label{eqn:P_relativistic_limit}
\end{equation}
We find the equation of state already introduced earlier. 


:::{exercise}

Using $T_0 = 2.726 K$, calculate the photon number density (today) and the photon energy density (today). Show that :
\begin{equation*}
  \begin{split}
    n_\gamma & = 411\ \mathrm{cm}^{-3}\\
    \epsilon_\gamma &= 4.6 \times 10^{-34}\ \mathrm{g/cm^{3}} \\
    \end{split}
  \end{equation*}
:::


:::{note} $I_\pm(0)$ and $J_\pm(0)$ calculations
:class: dropdown

To compute $I_{-}(0)$ it is useful to know the definition of the Riemann-zeta function:
$$
\zeta(s) = \sum_{i=1}^\infty \frac{1}{n^s} = \frac{1}{\Gamma(s)} \int_0^\infty \frac{x^s}{e^x - 1} \dd x
\ \ \text{où}\ \ \ \Gamma(s) = \int_0^\infty x^{s-1} e^{-x} \dd x
$$

Pour les bosons, nous obtenons immédiatement 
$$
I_-(0) = 2 \zeta(3) \approx 2.40411
$$
Pour les fermions, nous avons
\begin{equation}
  \begin{split}
    I_+(0) & = \int_0^\infty \xi^2 \left(\frac{1}{e^\xi - 1} - \frac{2}{e^{2\xi} - 1}\right) \dd \xi \\
    & = I_-(0) - 2 \int_0^\infty \frac{\xi^2}{e^{2\xi} - 1} \dd \xi \\
    & = \frac{3}{4} I_-(0) \\
  \end{split}
\end{equation}

$J_\pm(0)$ peut aussi être exprimé comme une fonction de $\zeta$. Pour les bosons, on obtient immédiatement
$$ J_-(0) = \underbrace{\Gamma(4)}_{3!}\ \underbrace{\zeta(4)}_{\pi^4/90} = \frac{\pi^4}{15}$$
Pour le fermion, nous utilisons la même astuce que ci-dessus, et nous obtenons :
$$
J_+(0) = \frac{7}{8} J_-(0)
$$
  
:::

#### Non-relativistic limit

In the non-relativistic limit, the energy of particles is equal to their rest mass ($m c ^2 \gg k_B T \Leftrightarrow x \gg 1$). The chemical potential $\mu$ is not necessarily negligible either. The integrals $I$ and $J$ defined above are the same for fermions and bosons and we find :

\begin{equation}
\boxed{\begin{aligned}
n &\approx g \left(\frac{m k_B T}{2\pi \hbar^2}\right)^{3/2} \exp\left(-\frac{(mc^2 - \mu)}{k_B T}\right)\label{eq:n_nonrel} \\
\rho &\approx n m + \frac{3}{2} \frac{nk_B T}{c^2} \\
P &= n k_B T \ll \epsilon = nmc^2 \\
\end{aligned}}
\end{equation}
When the temperature falls below the rest mass of the particles, the density of the number of particles falls exponentially. The energy density and pressure are (to first order) proportional to $n$ and decrease accordingly. Non-relativistic species therefore behave like a gas without pressure (because $P \ll \epsilon$ i.e. $w_m=0$). It is this description of non-relativistic matter that we have used to calculate the expansion of the Universe in the so-called ‘matter-dominated’ regime.

:::{note} Calculating particle density in the non-relativistic regime
:class: dropdown

With the same definitions as above: $x \equiv m c^2 / k_B T$, $\xi \equiv p c /k_B T$ and with $y = \mu/k_B T$ to reintroduce the chemical potential, the integrals $I_-$ and $I_+$ are reduced to a single expression if $x \gg 1$ :
\begin{equation}
  I_\pm(x\gg 1) = \int_0^\infty \frac{\xi^2 \dd \xi}{\exp(\sqrt(x^2 + \xi^2) - y)}
\end{equation}
$xi \ll x$ and we can develop: $(x^2 + \xi^2)^{1/2} \approx x (1 + \frac{1}{2}\frac{\xi^2}{x^2})$, and we can approximate the above integral with:
\begin{equation}
    I_\pm(x\gg 1) \approx e^{-(x-y)} \int_0^\infty \xi^2 e^{-\frac{\xi^2}{2 x}} \dd \xi \approx e^{-(x-y)} (2x)^{3/2} \frac{1}{2} \underbrace{\Gamma\left(\frac{3}{2}\right)}_{\sqrt{\pi}/2}
\end{equation}

:::

:::{note} Molecular gas
:class: dropdown

If the particle under consideration is made up of several atoms, then they have more degrees of freedom than the 3 translations in space. According to Boltzmann statistics, it can store energy in rotational or vibrational degrees of freedom if the medium is hot enough, each of which counts as $k_B T / 2$ in its internal energy. If we denote $g_m$ the number of degrees of freedom of a molecule, then the energy density is written :
$$ \epsilon \approx n m c^2 + \frac{g_m}{2} nk_B T = n m c^2 + \frac{1}{\gamma -1} n k_B T $$
with $\gamma=C_p/C_V$ the adiabatic index, found in Laplace's law $PV^\gamma = \cst$.
:::


:::{note} Order of magnitude of chemical potentials
:class: dropdown

For fermions, let's show that their chemical potentials are negligible. Let us compare the particle densities before and after the annihilation of particles with their antiparticles (see {cite:p}`KolbTurner` p.89):

\begin{align*}
n_f - n_{\bar f} & = \frac{g}{2\pi^2\hbar^3} \int \dd p \left[ \frac{p^2}{\exp\left((\sqrt{p^2c^2 + m^2 c^4}-\mu)/k_B T\right) + 1} - \frac{p^2}{\exp\left((\sqrt{p^2c^2 + m^2 c^4}+\mu)/k_B T\right) + 1}\right] \\
& = \frac{g}{6\pi^2\hbar^3}(k_B T)^3 \left[\pi^2 \left(\frac{\mu}{k_B T}\right) + \left(\frac{\mu}{k_B T}\right)^3 \right] \text{ si } mc^2 \ll k_B T \\
& = 2 g \left(\frac{m k_B T}{2\pi \hbar^2}\right)^{3/2} \sinh\left(\frac{\mu}{k_B T}\right) e^{-mc^2/(k_B T)} \text{ si } mc^2 \gg k_B T \\
\end{align*}


Now for baryons, their particle density is $(n_b - n_{\bar b}) \approx \eta n_\gamma \propto \eta (k_B T)^3$. For the relativistic and non-relativistic cases, we have $\mu_b / k_B T \sim \eta \ll 1$ so the chemical potential of baryons is negligible. For electrons, as the Universe is electrically neutral [^neutrality] then we have the same order of magnitude. Concerning neutrinos, it is more ambiguous because the diffuse neutrino background has not yet been detected, but as a first approximation we can think that here again the chemical potential must be negligible ({cite}`Weinberg1989` p.531).

:::


### Effective number of relativistic species

#### Definition

We start with a primordial plasma in thermal and chemical equilibrium, containing $i$ species at temperature $T_i$.
Before equivalence, the expansion rate is a direct function of the mass density of relativistic matter:
\begin{equation}
H^2 = \frac{8\pi G}{3} \rho_r(T)
\end{equation}
where $rho_r(T)$ is the sum of the densities of each relativistic species present in the primordial fluid:
\begin{equation}
  \rho_r(T) = \sum_i^{m_i \ll T} \rho_i(T)
\end{equation}
We saw in the previous section that $\rho_i \propto T_i^4$ as long as the particle remains relativistic, whereas the density falls exponentially when the temperature falls below the mass of the particle. More precisely, we can write :
\begin{align*}
\rho_r & = \sum_{i=\mathrm{bosons}}^{m_i \ll T} \frac{g_i\pi^2}{30\hbar^3c^3}(k_BT_i)^4 + \sum_{i=\mathrm{fermions}}^{m_i \ll T} \frac{7}{8}\frac{g_i\pi^2}{30\hbar^3c^3}(k_BT_i)^4 \\
& = (k_BT)^4 \left(\frac{\pi^2}{30\hbar^3c^3}\right) \sum_{i=\mathrm{bosons}} g_i \left(\frac{T_i}{T}\right)^4 + \frac{7}{8} \sum_{i=\mathrm{fermions}} g_i \left(\frac{T_i}{T}\right)^4 
\end{align*}
We define $g_\star(T)$ as the effective number of _relativistic_ degrees of freedom of the plasma at temperature $T$: 
\begin{equation}
\rho_r(T) = g_\star(T) \left(\frac{\pi^2}{30\hbar^3 c^5}\right) (k_BT)^4
\end{equation}
\begin{equation}
g_\star(T) = \sum_{i=\mathrm{bosons}}^{m_i \ll T} g_i \left(\frac{T_i}{T}\right)^4 + \frac{7}{8} \sum_{i=\mathrm{fermions}}^{m_i \ll T} g_i \left(\frac{T_i}{T}\right)^4
\end{equation}
When the species $i$ is still in thermal equilibrium with the photons, then $T_i=T$. When the temperature falls below the mass $m_i$ of one of the species, it becomes relativistic and disappears from the sum above. If it decouples from the photons with a temperature $T_i$ different from the photons, while remaining relativistic, then it remains present in $g_*(T)$ with a weight $(T_i/T)^4$.


#### Evolution of $g_\star(T)$


:::{figure} #gtable
:name: tab:gtable

Characteristics of Standard Model particles to calculate $g_*(T)$. In the absence of right neutrinos, there is only one spin state for neutrinos. Since gluons can carry 2 colour charges from the strong interaction among $r\lbrace r, g, b\rbrace$, this makes 9 possible states but the linear combination of white colour $r\bar r + g \bar g + b \bar b=0$ removes a degree of freedom from the strong interaction so there are ultimately only 8 independent states (<wiki:Gluon>).

:::

Let's now study the evolution of $g_\star(T)$, which simply tells the story of the evolution of the relativistic matter of the primordial plasma as it cools with the expansion. Let's start around $T \approx 300\,$GeV. All particles in the Standard Model are relativistic (see [](#tab:gtable)). When all particles are relativistic, the total number of degrees of freedom is :
\begin{equation}
  g_f = \underbrace{6}_{\mathrm{quarks}} \times \underbrace{2}_{q\bar q} \times \underbrace{2}_{\mathrm{spin}} \times \underbrace{3}_{\mathrm{couleur}} + \underbrace{3 \times 2 \times 2}_{\ell^\pm} + \underbrace{3 \times 2}_{\nu} = 90
\end{equation}
for fermions, and
\begin{equation}
  g_b = \underbrace{8 \times 2}_{\mathrm{gluons}} + \underbrace{3 \times 3}_{W,Z} + \underbrace{2}_{\gamma} + \underbrace{1}_{H} = 28
\end{equation}
for the bosons, which gives
\begin{equation}
  g_\star = g_b + \frac{7}{8} g_f = 106.75
\end{equation}

To see what happens next, just look at the masses of the particles listed in the [](#tab:gtable). The top quark annihilates first because it is the heaviest particle. For $k_BT<m_{\mathrm{top}}$, the plasma at equilibrium can no longer produce top quarks by annihilating pairs of other particles, reducing the number of degrees of freedom to :
\begin{equation}
  g_\star(T<m_{\mathrm{top}}) = 106.75 - \frac{7}{8} \times 12 = 96.25
\end{equation}
Then we have the Higgs boson, followed by the electroweak bosons $W^\pm$ and $Z^0$: this reduces $g_\star$ to 86.25. Then $b$ and $c$ annihilate, and $g_\star$ is reduced to 61.75.

The next event is the QCD phase transition, which occurs at $T \sim 150\ \mathrm{MeV}$.  The quarks combine into hadrons (protons, neutrons and mesons). At this temperature, all but the pions are non-relativistic. At this stage, the only remaining relativistic species are photons, neutrinos, electrons and muons and the 3 spin 0 pions (with $g_\pi = 3 \cdot 1 = 3$ internal degrees of freedom). From this we can deduce the number of remaining relativistic degrees of freedom:
\begin{equation}
  g_\star(T<T_{QCD}) = \underbrace{2}_{\gamma} + \underbrace{3}_{\pi^0,\pi^\pm} + \frac{7}{8} \times (\underbrace{4 + 4}_{e^{\pm}, \mu^\pm} + \underbrace{6}_{\nu}) = 17.25
\end{equation}

Next, the pions and muons annihilate, giving us
\begin{equation}
  g_\star = 2 + \frac{7}{8} \times (4 + 6) = 10.75
\end{equation}

:::{figure} #ggstar_plot
:name: fig:ggstar_plot

Evolution of the effective number of relativistic species $g_\star(T)$.
:::

The next two significant events are the decoupling of neutrinos around $1\,\MeV$ and the annihilation of electrons and positrons ($m_e = 511\,\keV$). 


### Entropy

#### Conservation of entropy

The entropy of the Universe $S(U,V,N_i)$ is a function of the extensive variables internal energy $U$, volume $V$ and the numbers $N_i$ of particles of a species $i$. The entropy variation of a comobile volume $V$ of plasma at thermodynamic equilibrium obeys the second principle of thermodynamics:
\begin{equation}
\dd S(U, V, N) = \frac{\dd U}{T} + \frac{P}{T}\dd V - \sum_i \frac{\mu_i}{T} \dd N_i \geq 0
\end{equation}
For a volume of the Universe large enough to be considered homogeneous and isotropic, entropy can only increase or remain constant. Moreover, chemical potentials are negligible in primordial plasma ($\mu / (k_B T) \sim \eta$). At thermodynamic equilibrium we have : 
$$U(V, T) = \epsilon(T) V,\quad P = P(T)$$
where pressure and energy density are ultimately only functions of equilibrium temperature, whether the species are relativistic or not (see previous formulae). Consequently, the variation in entropy is a function of volume and temperature with ({cite}`Weinberg1989` p.532):
$$
\dd S(V,T) = \frac{\dd(\epsilon(T) V)}{T} + \frac{P(T)}{T}\dd V = \frac{V}{T}\frac{\dd \epsilon}{\dd T} \dd T + \frac{P(T)+\epsilon(T)}{T} \dd V
$$
We identify the partial derivatives:
$$
\left.\frac{\partial S}{\partial T}\right\vert_V = \frac{V}{T}\frac{\dd \epsilon(T)}{\dd T}, \quad \left.\frac{\partial S}{\partial V}\right\vert_T = \frac{P(T)+\epsilon(T)}{T}
$$
and thanks to Maxwell's relations (or Schwartz's theorem), we have :
$$ \frac{\partial^2 S}{\partial T\partial V} = \frac{\partial^2 S}{\partial V\partial T} $$
\begin{align*}
& \Leftrightarrow \frac{\partial}{\partial T}\left[ \frac{P(T)+\epsilon(T)}{T} \right] = \frac{\partial}{\partial V}\left[ \frac{V}{T}\frac{\dd \epsilon(T)}{\dd T} \right] \\
& \Leftrightarrow \frac{1}{T} \frac{\dd ( P + \epsilon)}{\dd T} - \frac{1}{T^2}(P+\epsilon) = \frac{1}{T}
\frac{\dd \epsilon}{\dd T} \\
& \Leftrightarrow \frac{\dd P}{\dd T} = \frac{\epsilon + P}{T}
\end{align*}

With this last relation, we can complete the calculation of the entropy variation:
\begin{align*}
\dd S(V,T) & = \frac{P(T)+\epsilon(T)}{T} \dd V + \frac{V}{T}\frac{\dd \epsilon}{\dd T} \dd T \\
& = \frac{P(T)+\epsilon(T)}{T} \dd V + \frac{V}{T}\left[\frac{\dd (\epsilon+P)}{\dd T} - \frac{\dd P}{\dd T} \right]\dd T \\
& = \frac{1}{T} \dd \left[V(P+\epsilon)\right] - \frac{V}{T} \frac{\dd P}{\dd T}\dd T \\
& = \frac{1}{T} \dd \left[V(P+\epsilon)\right] - \frac{V}{T^2}(\epsilon + P)\dd T \\
& = \dd \left[\frac{V}{T}(P+\epsilon)\right]
\end{align*}
If we consider a variation with respect to time $t$ :
$$\frac{\dd S}{\dd t} = \frac{\dd}{\dd t}\left[ \frac{V}{T}(P+\epsilon)\right] = \frac{V}{T}\dot \epsilon + \frac{\epsilon + P}{T} \dot V + \frac{V}{T} \dot P - \frac{V}{T^2}(\epsilon + P)\dot T$$
and finally by remembering the conservation of energy relation $\dot \epsilon = -3H(\epsilon + P)$,
$$\boxed{\frac{\dd S}{\dd t} = 0}$$
The entropy in a comobile volume is therefore conserved and is written [^Sconst] :
$$\boxed{S(V, T) = \frac{V}{T}(P+\epsilon)}$$
We define the volume entropy as a function of temperature only:
$$\boxed{s(T) = \frac{P+\epsilon}{T}, \quad \dd(a^3 s) = 0}$$

#### Entropy of primordial plasma

For relativistic species, such as $P=\epsilon/3$, we obtain the volume entropies :
\begin{equation}
  \boxed{s_r(T) = \frac{4}{3}\frac{\epsilon_r}{T} =
\left\lbrace
\begin{array}{ll}
     \dfrac{2\pi^2k_B^4}{45\hbar^3 c^3} T^3 & \text{pour les bosons}\\
     \dfrac{7}{8} \dfrac{2\pi^2 k_B^4}{45\hbar^3 c^3} T^3 & \text{pour les fermions}
  \end{array}
\right.}
\end{equation}
For a collection of species (fermions and bosons) at equilibrium at temperatures $T_i$, we have :
\begin{equation}
    s_r(T) = \sum_i^{m_i \ll T} \frac{\epsilon_i + P_i}{T_i} = \frac{4}{3} \sum_i^{m_i \ll T} {\epsilon_i}{T_i} = \frac{2\pi^2 k_B^4}{45 \hbar^3 c^3} g_{\star S}(T) T^3
\end{equation}
with
\begin{equation}
  g_{\star S}(T) = \sum_{\mathrm{bosons}} g_b \left(\frac{T_b}{T}\right)^3 + \frac{7}{8} \sum_{\mathrm{fermions}} g_f \left(\frac{T_f}{T}\right)^3
\end{equation}
Since the entropy $S$ is conserved, then :
\begin{equation}
\dd(s a^3) = 0 \Rightarrow g_{\star S}(T) T^3 a^3 = \cst
\end{equation}


#### Temperature of the Universe

Now that we have a conservation relation, we can establish a link between the expansion of the Universe and its temperature:
\begin{equation}\label{eq:Tagstar}
  \boxed{T \propto \left[g_{\star S}^{1/3}(T) a\right]^{-1}}
\end{equation}
This relation gives a link between temperature and scale factor at any instant in the history of the Universe. It varies with the redshift in $(1+z)$ but with a proportionality factor $g_{\star S}^{1/3}(T)$ which changes by threshold according to the composition of the Universe ([](#fig:Ta_plot)). 



:::{figure} #Ta_plot
:name: fig:Ta_plot

Evolution of the temperature during the expansion of the Universe according to the relativistic species present (equation [](#eq:Tagstar)). In reality, phase transitions are not sudden, so the real curve must be smoothed.
:::

### Expansion of primordial plasma

The expansion law obeys Friedmann's first equation:
\begin{equation}
  H^2 = \frac{8\pi G}{3} \rho_r = \frac{8\pi G}{3} \frac{8\pi^2}{30\hbar^3 c^5} g_\star(T) T^4
\end{equation}
and therefore :
\begin{equation}
  \boxed{H(T) = \sqrt{\frac{8 \pi^3 G}{90 \hbar^3 c^5}} g_\star^{1/2}(T) (k_B T)^2}
\end{equation}
So $H \propto T^2$ to within variations of the effective number of degrees of freedom in the primordial plasma. Keep this in mind, as it will be useful for comparing the expansion rate with the various reaction rates between the different species.


Injecting the temperature evolution with the scaling factor (equation [](#eq:Tagstar)), we find that $a(t) \propto t^{1/2}$ in the primordial Universe (equation [](#eq:a_rad_only)) with the proportionality factor changing as $g_{\star S}$ varies. But the expansion rate is then simply $H(t) = 1/(2t)$ which gives :
\begin{equation}\label{eq:Ttoa}
  \boxed{T \approx \left[ 1.8 \times 10^{10}\,\mathrm{K}\right] \times g_*(T)^{-1/4} \left(\frac{t}{\mathrm{1\ sec}}\right)^{-1/2} \approx \left[ 1.6\,\mathrm{MeV}\right] \times g_*(T)^{-1/4} \left(\frac{t}{\mathrm{1\ sec}}\right)^{-1/2} } 
\end{equation}
Thus, when the Universe was one second old, the typical energy of relativistic particles was of the order of $0.9\,\MeV$ with $g_*=10.75$.


History of matter in the early Universe
--------------------------------------

We now have (almost) everything we need to discuss the evolution of matter in primordial plasma. When the temperature is sufficiently high, the primordial plasma contains all the particles of the Standard Model, in relativistic form (plus all the particles that have not yet been discovered, for example the hypothetical particles that would constitute cold dark matter today). All particle species are in thermal equilibrium (kinetic and chemical, same temperature $T$). But as the Universe expands, the temperature decreases at the same rate as the expansion. One after another, the various massive species become non-relativistic, annihilating each other, and their energy densities become sub-dominant compared with the relativistic species. 

If the Universe were in perfect thermal equilibrium, and if this equilibrium had persisted until today, the observed abundances of massive particles would be much lower than they are, since each massive species sees its density exponentially suppressed when it becomes non-relativistic. In fact, thermal and chemical equilibria need frequent collision (and/or reaction) rates to be maintained. As the Universe expands, particles become diluted, making it more difficult to maintain reaction rates. 

Since $T \propto a^{-1}$ [](#eq:Ttoa), the rate of temperature change is the Hubble rate:
$$H = \frac{\dot a }{a} = \frac{\dot T}{T}$$
To be able to consider that the system is in thermodynamic equilibrium, there must be sufficient interactions in a time shorter than the time taken for the temperature to change.
The rule of thumb is that you need at least several interactions per Hubble time to maintain thermal and chemical equilibrium. 
Thus, if we note $\Gamma$ the rate of interaction, thermal and chemical equilibrium is maintained if $ \Gamma \gg H$. When the $\Gamma$ reaction rate falls below $H$, thermodynamic equilibrium is no longer maintained and the particle densities are frozen at their pre-decoupling values. The freezing of interactions is an essential mechanism in explaining the current abundance of particles.


### Neutrino decoupling and electron-positron annihilation

Neutrino decoupling is our first illustration of the freezing effect. Neutrinos interact only through the weak interaction.  Around $\sim 1\,\MeV$, they are still thermalised with the photon bath by interactions such as :
\begin{equation}
  \begin{split}
    \nu_e + \bar{\nu_e} & \rightleftharpoons e^+ + e^- \\
    e^- + \nu_e & \rightleftharpoons e^- + \nu_e  
  \end{split}
\end{equation}
At these energies, the effective cross section of the weak interaction is $\sigma_w \sim G_F^2 T^2$ with $G_F/(\hbar c)^3=1.166 378 7(6)\times 10^{-5}\,\GeV^{-2}$ the {cite:p}`PDG2010` Fermi coupling constant. Consequently, the interaction rate $\Gamma = n_e \sigma_w c \propto G_F^2 T^5$ decreases much faster than the Hubble parameter ($\propto T^2$):
$$
\frac{\Gamma}{H} \sim \frac{n_e \sigma_w}{H} \sim \left(\frac{T}{1\,\MeV}\right)^3
$$
Around $1, \MeV$, $\Gamma \sim H$ and interactions between neutrinos and the other particles of the Standard Model become very unlikely. Neutrinos decouple from the primordial plasma but remain relativistic ($m_\nu \ll 1\,\MeV$). Even if they no longer interact with other particles, they retain to an excellent approximation their Fermi-Dirac distribution function (see box) with a temperature that is affected only by the red shift. Thus, at this stage :
\begin{equation}
  T_\nu = T_\gamma \propto a^{-1}
\end{equation}
as long as the evolution of the photon temperature does not vary.


:::{note} Fermi coupling
The Fermi coupling constant is the coupling in a diagram with 4 fermions interacting by weak interaction at low energy (well below the mass of the weak interaction bosons). It is related to the mass of the $W$ and the expected value of the Higgs in vacuum $v$ :
$$G_F = \frac{sqrt{2}}{8} \left(\frac{g_W}{m_W c ^2}\right)^2(\hbar c)^3, \quad v = (\sqrt{2}G_F)^{-1/2} \sim 246.22\,\GeV$$


:::

:::{note} The spectrum of decoupled species without interaction XXX DRAFT

For ultra-relativistic species, we have $pc \sim E$. The number of particles at $t_1$ in the volume of phase space $d^3p_1 \dd V_1$ is :
\begin{equation}
\dd N = \frac{g}{(2\pi)^3} \frac{d^3p_1 \dd V_1}{\exp((E(p_1) - \mu_1)/T_1) \pm 1}
\end{equation}
At $t_0$, a little later, the same particles are in the volume of phase space $\dd^3p_0 \dd V_0$.   The moments scale as $a^{-1}$ and the volume as $a^3$. We can therefore write
\begin{equation}
\begin{split}
\dd N & = \frac{g}{(2\pi)^3} \frac{\dd^3p_1 \dd V_1}{\exp((p_1 - \mu_1)/T_1) \pm 1} \\
& = \frac{g}{(2\pi)^3} \frac{d^3p_0 \left(\frac{a_0}{a_1}\right)^3 \dd V_0\left(\frac{a_1}{a_0}\right)^3}{\exp((p_0\left(\frac{a_1}{a_0}\right) - \mu_1)/T_1) \pm 1} \\
& = \frac{g}{(2\pi)^3} \frac{d^3p_0 \dd V_0}{\exp((p_0 - \mu_0)/T_0) \pm 1} \\
\end{split}
\end{equation}
with $\mu_0 \equiv \frac{a_1}{a_0} \mu_1$ and $T_0 \equiv \frac{a_1}{a_0} T_1$.   

:::


### Annihilation of $e^+ + e^-$ and the temperature of the diffuse neutrino background

But shortly after the neutrinos decoupled, when $T < 511\,\keV$ about $6\,$s after the Big Bang, the electrons and positrons annihilated:
\begin{equation}
    e^- + e^+ \rightarrow \gamma + \gamma  
\end{equation}
which will produce enough energy and entropy to heat the photon gas and lead to a difference between the temperature of the photons and those of the decoupled neutrinos $T_\nu < T_\gamma$. Since entropy is conserved, before annihilation we have :
\begin{equation}
  g_{\star S}(T > m_e) = \underbrace{2}_{\gamma} + \frac{7}{8}\left[ \underbrace{2}_{e^pm} + \underbrace{2}_{\nu, \bar \nu} \times \underbrace{3}_{e,\mu,\tau} \right]. 
\end{equation}
after annihilation : 
\begin{equation}
  g_{\star S}(T<m_e) = 2 + \frac{7}{8}\times 3 \times 2 \left(\frac{T_\nu}{T_\gamma}\right)^3
\end{equation}
Writing the conservation of entropy, we have :
\begin{equation}
  g_{\star S}(T > m_e)\ a^3_\mathrm{before}\ T^3_\mathrm{\gamma,before} = g_{\star S}(T < m_e)\ a^3_\mathrm{after}\ T^3_\mathrm{\gamma,after}
\end{equation}
Now we have $T_\mathrm{\gamma,before}=T_\mathrm{\nu,before}$ so :
\begin{align*}
  \left[2+\frac{7}{8}\left(2\times 2 + 2 \times 3  \right)\right] \ a^3_\mathrm{before}\ T^3_\mathrm{\nu,before} & = & \left[ 2 + \frac{7}{8}\times 3 \times 2 \left(\frac{T_\mathrm{\nu,after}}{T_\mathrm{\gamma,after}}\right)^3 \right] \ a^3_\mathrm{after}\ T^3_\mathrm{\gamma,after} \\
  \Leftrightarrow   \left[2+\frac{7}{8}\left(2\times 2 + 2 \times 3  \right)\right] \ a^3_\mathrm{before}\ T^3_\mathrm{\nu,before} & = & \left[ 2 \left(\frac{T_\mathrm{\gamma,after}}{T_\mathrm{\nu,after}}\right)^3  + \frac{7}{8}\times 3 \times 2 \right] \ a^3_\mathrm{after}\ T^3_\mathrm{\nu,after} \\
\end{align*}
For decoupled neutrinos, $a_\mathrm{after}T_\mathrm{\nu,after} = a_\mathrm{before}T_\mathrm{\nu,before}$ so finally:
\begin{equation}
  \boxed{T_\mathrm{\nu,after}\ = \left(\frac{4}{11}\right)^{1/3}\ T_\mathrm{\gamma,after}}
\end{equation}

We can therefore see that after $e^\pm$ annihilation, the temperature of the cosmic neutrino background is indeed lower than the temperature of the CMB. Today, using $T_0 = 2.725\,\kelvin$, we find :
\begin{equation}
  T_\nu^0 \approx 1.95\,K = 0.17\,\mathrm{meV}
\end{equation}
The ratio between the temperatures of photons and neutrinos can be seen on the [](#fig:BBN_Tnu) obtained after a precise calculation of the evolution of the medium during $e^\pm$ annihilation.

:::{figure} #BBN_Tnu
:name: fig:BBN_Tnu
:align: center
:width: 70%

Temperature evolution of photons and neutrinos during $e^\pm$ annihilation (figure adapted from {cite}`Weinberg1989` p. 529,540 and originally from {cite}`Peebles1966`).
:::

We can deduce the neutrino density $n_\nu$ as a function of $n_\gamma$. Neutrinos are fermions with 3 flavours, so if we assume that they have no mass, their density today would be : 
\begin{equation}
  n_\nu^0 = \frac{3}{4} \times 3 \times \frac{4}{11} n_\gamma^0
\end{equation}
which gives $112\,\mathrm{cm}^{-3}$ per flavour ($336 \,\mathrm{cm}^{-3}$ in total). For the energy density of the neutrino background, we find :
\begin{equation}
\rho_\nu = \frac{7}{8} \frac{g_\nu}{g_\gamma} \left(\frac{T_\nu}{T_\gamma}\right)^4 \rho_\gamma = \frac{7}{8} \times \frac{3 \times 2}{2} \times \left(\frac{4}{11}\right)^{4/3} \rho_\gamma = 0.68\,\rho_\gamma
\end{equation}
and numerically we find $\Omega_\nu^0 h^2 \approx 1.7\times 10^{-5}$. From this we can deduce the total proportion of relativistic matter in the Universe (if neutrinos are relativistic):
$$\Omega_r^0 = \Omega_\gamma^0 + \Omega_\nu^0 = \Omega_\gamma^0 \left(1 + \frac{\rho_\nu^0}{\rho_\gamma^0 } \right) = 1.68\,\Omega_\gamma^0$$

The decoupling of the neutrinos was slightly superimposed on the annihilation of $e^\pm$. As the neutrinos were still interacting at the time of annihilation, the neutrino background was slightly affected by the energy and entropy released by the annihilation of $e^\pm$.In the literature, this is taken into account by introducing an _effective number of neutrinos_ $N_{\mathrm{eff}}$, numerically evaluated at $3.046$. 
Taking this into account, the number of neutrinos and the energy density are :
\begin{equation}
\begin{split}
n_\nu(T_\gamma) & = \frac{3}{4} N_{\mathrm{eff}}\times \frac{4}{11} n_\gamma(T_\gamma) \\
\rho_\nu(T_\gamma) & = \frac{7}{8} N_{\mathrm{eff}}\times \left(\frac{4}{11}\right)^{4/3} \rho_\gamma(T_\gamma) \\
\end{split}
\end{equation}

Finally, the correct values $g_\star$ and $g_{\star S}$ after annihilation $e^\pm$ are :
\begin{equation}
\begin{split}
g_\star & = 2 + \frac{7}{8}\times 2 N_{\mathrm{eff}} \times \left(\frac{4}{11}\right)^{4/3} \approx 3.36 \\
g_{\star S} & = 2 + \frac{7}{8}\times 2 N_{\mathrm{eff}}\times \left(\frac{4}{11}\right) \approx 3.94 \\ 
\end{split}
\end{equation}


In fact, neutrinos have masses, with two important consequences (1) we do not know whether they are still relativistic today (all flavours taken together) (2) $\Omega_\nu h^2$ is greater than the value quoted above. Experiments observing neutrino oscillations dictate that the sum of neutrino masses, noted $\sum_\nu m_\nu$ is greater than $60\,\meV$ so at least one neutrino flavour would be non-relativistic today if compared to $T_\nu^0$. From a cosmological point of view, if we very conservatively impose that $\Omega_\nu^0 < 1$ then we end up with a constraint $\sum_\nu m_\nu < 15\,\eV$, and cosmological surveys looking at the gravitational collapse of the Universe's Large-scale structures impose $\sum_\nu m_\nu < 0.1\,\eV$ (<doi:10.48550/arXiv.2404.03002>).

### Big Bang Nucleosynthesis (BBN)

Let's go back to about $1\,$ms after the Big Bang, when the temperature of the Universe was a few tens of MeV. The Universe is essentially a hot soup of baryons, photons, electrons and neutrinos about to decouple from the other particles. Remember that the ratio of baryons to photons is a constant [](#eq:eta) and is more precisely :
$$\label{eq:etaToObh2}
\eta = \frac{n_b}{n_\gamma} = \frac{\Omega_b^0 \rho_c^0}{m_p n^0_\gamma} = 2.73\times 10^{-8}\times \Omega_b^0 h^2 = 6.2 \times 10^{-10}
$$
with the measurement of $\Omega_b^0 h^2$ on the CMB {cite}`Planck2018` power spectrum of temperature anisotropies. As the Universe continues to expand, it cools and protons and neutrons can fuse together to form the first atomic nuclei. This is known as primordial nucleosynthesis (BBN).

#### Neutron to proton ratio

The rate of formation of these nuclei will depend on an essential parameter: the ratio of the number of neutrons and protons available.

:::{note} Free neutron decay

A neutron is unstable if it is not bound to a proton in an atomic nucleus by strong interaction. It decays according to the reaction :
$$ n \rightarrow p + e^- + \bar{\nu}_e $$
because its mass energy is slightly greater than that of the proton:
$$Q_n = (m_n - m_p)c^2 = 1.29\,\mathrm{MeV}.$$
The value of the average lifetime used by the Particle Data Group in 2022 is {cite:p}`PDG2022` :
$$\tau_n = 878.4 \pm 0.5\,\mathrm{s}$$ 
i.e. only about 15 minutes. The existence of free neutrons in the Universe is therefore strongly limited in time. In what follows, we will have to check whether the age of the Universe is small compared with this decay time ($t\ll \tau_n$) to see whether it is legitimate to neglect this spontaneous decay.
:::


At $t=1\,$ms, the protons and neutrons are in thermodynamic equilibrium with each other via the interactions :
\begin{align}\label{eq:betadecays}
n + \nu_e & \rightleftharpoons & p + e^-\\
n + e^+ & \rightleftharpoons & p + \bar{\nu}_e
\end{align}
and even this one (less effective):
$$n \rightleftharpoons p + e^- + \bar{\nu}_e $$
As long as these interactions exist, the neutron to proton ratio is given by the equilibrium particle densities [](#eq:n_nonrel) for non-relativistic particles[^mp] :
\begin{align}
n_n & = g_n \left(\frac{m_n k_B T}{2\pi \hbar^2}\right)^{3/2} \exp\left(-\frac{(m_nc^2 - \mu_n)}{k_B T}\right) \\
n_p & = g_p \left(\frac{m_p k_B T}{2\pi \hbar^2}\right)^{3/2} \exp\left(-\frac{(m_pc^2 - \mu_p)}{k_B T}\right) 
\end{align}
Now $g_n=g_p=2$ and we can suppose that $\mu_p=\mu_n$ if the chemical potentials of the electrons and neutrinos are negligible. Then the neutron to proton ratio is simplified to :
\begin{equation}\label{eq:np_eq}
\left.\frac{n_n}{n_p}\right\vert_{eq} = \left(\frac{m_n}{m_p}\right)^{3/2} \exp \left(- \frac{(m_n-m_p)c^2}{k_B T} \right) \approx \exp\left(-Q_n / k_B T\right).
\end{equation}
We deduce that as long as the temperature is such that $k_B T \gg Q_n = 1.29\,$MeV, then there are as many neutrons as protons in the Universe. But below $1\,$MeV, the proportion of neutrons falls exponentially. Let $X_n^{eq}$ be the ratio of neutrons to baryons if the species are in equilibrium at temperature $T$. Then :
$$ X_n^{eq}(T) = \frac{n_n^{eq} }{ n_b} = \frac{n_n^{eq}}{n_n^{eq} + n_p^{eq}} =\frac{\exp\left(-Q_n / k_B T\right)}{ 1 + \exp\left(-Q_n / k_B T\right)}.$$
So the neutron density should be almost zero today, but this equation is only valid *as long as the reactions are taking place*. In fact, if the rate of expansion of the Universe becomes comparable to or greater than the rate of interaction, then the reactions stop and the neutron-to-proton ratio is frozen. The _freeze mechanism_ of reactions involving massive particles is important in cosmology to understand the abundance of massive particles today.

For the reaction $p+e^- \rightarrow \nu_e + n$, the interaction rate is given by ({cite}`KolbTurner` p.90, {cite}`Weinberg1989` p.547 and originally in {cite}`Peebles1966`):
$$
\Gamma_{pe\to \nu n} = \frac{1}{(2\pi)^5}\int f_e(E_e)\left[ 1 - f_\nu(E_\nu)\right]\vert \mathcal{M}\vert^2_{pe\to \nu n}\delta^4(p_p+p_e-p_\nu-p_n) \frac{\dd^3 \vec p_e}{2 E_e}\frac{\dd^3 \vec p_\nu}{2 E_\nu}\frac{\dd^3 \vec p_n}{2 E_n}
$$
with $f_i(E_i)$ the Fermi-Dirac distributions of the $i$ particles and :
$$\vert \mathcal{M} \vert ^2 \propto G_F^2 ( 1+ 3g_A^2)$$
with $G_F = 1.16 \times 10^{-5}  \GeV^{-2}$ the Fermi constant and $g_A = 1.26$ the axial-vector coupling of nucleons ({cite}`KolbTurner` p.91). Unfortunately, these integrals have to be calculated precisely to obtain the right proportion of helium, as we shall see that the neutron proportion freezes at a temperature close to $Q_n$ and $m_e$, which makes it impossible to make crude approximations in order to concentrate on a high- or low-energy regime. 

:::{tip} Numerical approximation of integrals
:class: dropdown

A numerical approximation of the sum of the integrals for the two reaction interaction rates [](#eq:betadecays) is {cite}`Bernstein1989` :
\begin{equation}\label{eq:Gnp} 
\Gamma_{np}(x) = \frac{255}{\tau_n x^5}(12+6x+x^2), \quad x= \frac{Q_n}{k_B T}
\end{equation}
Next, to obtain the evolution of the neutron density, a numerical integration method is proposed in {cite}`Dodelson2003` p.67 by defining the neutron proportion $X_n = n_n / n_b = n_n / (n_n + n_p)$ :
\begin{equation}\frac{\dd X_n}{\dd t} = \Gamma_{np} \left[(1-X_n)e^{-Q_n / k_B T} - X_n\right] - \frac{X_n}{\tau_n} 
\end{equation}

:::




A detailed assessment of the neutron density leads to the following Boltzmann equation:
\begin{align}\label{eq:nn}
\frac{\dd n_n}{\dd t} & = - \Gamma_{n\to p}\,n_n + \Gamma_{p\to n}\,n_p - 3\frac{\dot a}{a} n_n \\
\frac{\dd n_p}{\dd t} & = \Gamma_{n\to p}\,n_n - \Gamma_{p\to n}\,n_p - 3\frac{\dot a}{a} n_p
\end{align}
where $\Gamma_{p\to n}=\Gamma_{pe\to \nu n}$ is the interaction rate for the first reaction whereas $\Gamma_{n\to p}$ represents the sum of the other reactions forming protons. The last term in the equations corresponds to the dilution of the particles with expansion if their number is conserved in a comobile volume. On the other hand, the total number of protons and neutrons is conserved in a comobile volume:
$$
\frac{\dot (n_n+n_p)}{\dd t} = - 3\frac{\dot a}{a} (n_n + n_p) \Leftrightarrow \frac{\dd\left[a^3(n_n+n_p)\right]}{\dd t} = 0
$$

Let's define the proportion of neutrons $X_n = n_n / n_b = n_n / (n_n + n_p)$. The proportion of protons $X_p$ can be deduced by $X_p=1-X_n$. The differential equation for the neutron density is rewritten:
$$ \frac{\dd n_n}{\dd t}= \frac{\dd X_n(n_n+n_p)}{\dd t} = (n_n+n_p)\frac{\dd X_n}{\dd t} - 3\frac{\dot a}{a} (n_n + n_p) X_n$$.
or :
\begin{equation}\label{eq:Xn}
\frac{\dd X_n}{\dd t} = - \Gamma_{n\to p}\,X_n + \Gamma_{p\to n}\,(1-X_n) 
\end{equation}

Let's start by comparing the neutron disappearance rate with the expansion rate of the Universe ([](#fig:BBN_Gnp)).
After numerical integration, we observe that $\Gamma_{n\to p}$ decreases as a function of time and converges towards a plateau corresponding to the inverse of the neutron half-life time $\tau_n^{-1}$ (independent of the expansion). It is greater than the rate $\Gamma_{p\to n}$ so it is the rate that counts in the freezing mechanism. The rate $\Gamma_{n\to p}$ is comparable to the rate of expansion $H$ at temperature: 
$$\boxed{T_{\mathrm{freeze}}= 0.7\,\MeV = 8\times 10^9\,\kelvin}$$.
This is the neutron freezing temperature. 


:::{figure} #BBN_Gnp
:name: fig:BBN_Gnp
:align: center
:width: 70%

Comparison of the reaction rate $\Gamma_{n\to p}(T)$ and the expansion rate $H(T)$. The neutron density freezing temperature is defined by the intersection of the curves. The reaction rate $\Gamma_{n\to p}(T)$ reaches a plateau corresponding to the neutron decay rate, independent of expansion. The shaded region corresponds to the formation of atomic nuclei: there are no more free neutrons at this stage so the curves are no longer valid, but this highlights the $\Gamma_{n\to p}(T)$ plateau.
:::

Let's now study the relative neutron density $X_n(t)$. After numerical integration with the initial condition :
$$ 
X_n(t \approx 1\,\mathrm{ms}) = X_n^{eq}(t \approx 1\,\mathrm{ms}), \quad g_*=10.75
$$
we obtain the [](#fig:BBN_Xn). If the spontaneous decay of the neutron is omitted_ (dashed curve), the neutron fraction converges to $X_n^{\mathrm{frozen}} = 0.15$, i.e. :
$$
\frac{n_n}{n_p}(100\,\keV) = \frac{X_n(100\,\keV)}{1-X_n(100\,\keV)} = 0.17 \sim 1/6
$$
i.e. 1 neutron for 6 protons[^Tfreeze].

:::{figure} #BBN_Xn
:name: fig:BBN_Xn
:align: center
:width: 70%

Neutron fraction $X_n$ as a function of time calculated by equation [](#eq:Xn) (solid line). If neutron decay is neglected, then we obtain the dotted curve ($\tau \to \infty$). The equilibrium distribution $\left.n_n/n_p\right\vert_{eq}$ gives the proportion of neutrons if the reactions are not frozen by the expansion of the Universe.
:::



#### Synthesis of deuterium

After the neutron freezing temperature, the proportion of neutrons and protons is stable, except that a free neutron is unstable with a decay time of about 15 minutes. However, if the temperature drops sufficiently, protons and neutrons can combine to form the lightest atomic nucleus by strong interaction, deuterium $\mathrm{D}$, via the reaction :
\begin{align}
p + n \rightleftharpoons \mathrm{D} + \gamma
\end{align}
The question is: when is deuterium formed and how many neutrons are left at that moment?

Deuterium has a binding energy :
$$B_{\mathrm{D}} = (m_n + m_p - m_\mathrm{D})c^2 = 2.22\,\mathrm{MeV}$$
It is therefore more favourable to form deuterium atoms than to keep protons and neutrons separate. At equilibrium, 
\begin{align}
\frac{n_\mathrm{D}}{n_pn_n} & = \frac{g_\mathrm{D}}{g_p g_n} \left(\frac{k_B T}{2\pi \hbar^2}\right)^{-3/2}\left(\frac{m_\mathrm{D}}{m_p m_n}\right)^{3/2} \exp \left( \frac{(m_p+m_n-m_\mathrm{D})c^2}{k_B T} \right) \\
 & \approx 6 \left(\frac{m_n k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_\mathrm{D}}{k_B T}\right)
\end{align}
with $g_\mathrm{D}=3$ (because deuterium is a massive spin 1 boson), $g_n=g_p=2$ and $\mu_p + \mu_n = \mu_D + \mu_\gamma = \mu_D$ ({cite}`ryden2017` p.219).

We define the starting temperature of nucleosynthesis $T_{\mathrm{nuc}}$ for which half of the neutrons have been consumed to form deuterium, i.e. when $n_\mathrm{D}=n_n$. The ratio of deuterium to neutrons is written :
\begin{equation}\label{eq:XD}
\frac{n_\mathrm{D}}{n_n} \approx 6 n_p \left(\frac{m_n k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_D}{k_B T}\right)
\end{equation}
Assuming that in any case the number of protons will decrease very little during the formation of deuterium, we can estimate that the proton density at $T_{\mathrm{nuc}}$ is approximately :
$$ n_p \approx (1-X_n(T_{\mathrm{nuc}})) n_b = (1-X_n(T_{\mathrm{nuc}})) \eta n_\gamma(T_{\mathrm{nuc}}) $$
We then deduce the temperature $T_{\mathrm{nuc}}$ by the numerical inversion of the equation:
$$ 6 (1-X_n(T_{\mathrm{nuc}})) \eta n_\gamma(T_{\mathrm{nuc}}) \left(\frac{m_n k_B T_{\mathrm{nuc}}}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_D}{k_B T_{\mathrm{nuc}}}\right) = 1 $$
From this we deduce:
$$\boxed{T_{\mathrm{nuc}} = 70\,\keV = 8 \times 10^8\,\kelvin}$$
or $t_{\mathrm{nuc}} \approx 280\,$s after the Big Bang, with $g_* = 3.36$ from now on since the Universe has a temperature lower than $m_e$. At this precise moment, the fraction of neutrons still present is about : 
$$\boxed{\frac{n_n}{n_p}(T_{\mathrm{nuc}}) = \frac{X_n(T_{\mathrm{nuc}})}{1-X_n(T_{\mathrm{nuc}})} = 0.14 \sim 1/7}$$
Spontaneous neutron decay is therefore significant on this time scale.

#### Helium-4 synthesis

Helium nuclei can only be formed by the fusion of deuterium nuclei:
\begin{align}
p + n &\rightarrow &\mathrm{D} + \gamma \\
\mathrm{D} + p &\rightarrow &^3\mathrm{He} + \gamma \\
\mathrm{D} + \mathrm{D} &\rightarrow& ^4\mathrm{He} + \gamma 
\end{align}
because it is much more unlikely that two protons and two neutrons would meet by chance to form a helium nucleus. However, the binding energy of helium-4 is much higher than that of deuterium ($B_{\mathrm{He}} = 28.3\,\MeV$) so its formation will be favoured. We can therefore assume that all the neutrons available at $t_{\mathrm{nuc}}$ will end up in a helium nucleus. 

As two neutrons go into a helium-4 nucleus, the maximum number of formable helium nuclei is equal to half the available neutrons (whether free or in deuterium nuclei). The helium-4 abundance in number of nuclei can be deduced as :
$$
n_{\mathrm{He}} = \frac{1}{2} n_n(t_\mathrm{nuc})
$$
In terms of mass, the abundance of helium 4 in the Universe at the end of primordial nucleosynthesis may be at most ([](#fig:BBN_Yp)):
\begin{equation}
\boxed{Y_p \equiv \frac{\rho(^4\mathrm{He})}{\rho_b} = \frac{4n_\mathrm{He}}{n_n + n_p} \approx 25\%}
\end{equation}
the remainder being hydrogen ($75\%$ by mass).

:::{figure} #BBN_Yp
:name: fig:BBN_Yp
:align: center
:width: 70%

Mass fraction of the various light nuclei in the Universe over time, calculated using the simple model detailed in this chapter.
:::

More precise calculations show that the synthesis of atomic nuclei starts about 3 minutes after the Big Bang and ends 20 minutes later, and predict $Y_p$ to be around 24%, because a small fraction of neutrons remain in other light nuclei after $t_{\mathrm{nuc}}$ such as deuterium, lithium, etc ([](#fig:BBN)). These predictions are in good agreement with measurements (see [](#fig:BBN_mes)). Before the discovery of the CMB's temperature anisotropies in the 2000s, comparing measurements of the abundances of light elements (by observing the interstellar medium, galaxies, etc: horizontal grey bands in the [](#fig:BBN_mes)) with these predictions was a way of measuring $\eta$ and therefore $\Omega_b^0h^2$ (see equation [](#eq:etaToObh2)). The measurement of $\Omega_b^0h^2$ by temperature anisotropies (vertical grey band in [](#fig:BBN_mes)) is more precise but in agreement with the BBN predictions, which shows the robustness of the Standard Model of cosmology (except for lithium, where a disagreement persists).

In any case, with only the stellar mechanism of fusion of hydrogen at the heart of stars into helium (and then fusion of helium into carbon, oxygen, etc), it is not possible to explain such an abundance of helium in the Universe. Only the passage through a hot plasma at hundreds of millions of degrees containing free neutrons, even for a maximum of 20 minutes as it cools, can explain the $24\%$ of helium present in the Universe. This is therefore important evidence for the existence of a state in which the Universe was a hot, dense plasma for at least a few minutes. 

:::{figure} ../../images/bbn.png
:width: 80%
:align: center
:label: fig:BBN

Synthesis of light elements in the primordial Universe (from {cite}`PospelovBBN2010`).
:::


:::{figure} ../../images/bbn_Yp.png
:width: 80%
:align: center
:label: fig:BBN_mes

Comparison between theoretical predictions for the abundances of light nuclei (coloured bands) and measurements (grey bands) (from {cite}`Baumann`).
:::

:::{note} Beyond helium

It is very difficult to form nuclei beyond helium because helium has a binding energy that is much higher than that of the next heaviest atoms. In particular, there are no stable nuclei with $A=5$ nucleons, so to go beyond helium it is not enough to absorb one of the many protons present.

A little lithium can also be formed via the reactions :
$$^4\mathrm{He} + \mathrm{D} \rightleftharpoons\ ^6\mathrm{Li} + \gamma $$

```{figure} ../../images/Binding_energy_curve.svg
:width: 80%
:align: center
:label: fig:binding_energy

Binding energy per nucleon (source: Wikipedia <wiki:Nuclear_binding_energy>).
```
:::

### Recombination

Recombination takes place in two stages, as we shall see. First there is the formation of hydrogen atoms and then the decoupling of the remaining free electrons and photons. At this point, the plasma is transformed into a neutral gas of hydrogen and helium (plus a little lithium, etc.). After recombination, the photons in the thermal bath are free to propagate in the Universe, since the medium is (almost) neutral. This first light corresponds to the cosmic microwave background and provides us with information about the state of the young Universe and the physics that took place there before (and after). 

#### Formation of hydrogen atoms

Hydrogen atoms are formed by the reaction :
$$ p + e^- \rightleftharpoons \mathrm{H} + \gamma$$
and remember that the binding energy of hydrogen is $B_\mathrm{H} = 13.6\,\eV$. A quick approximation would give us that the temperature at which recombination took place is $T_\mathrm{rec} \approx B_\mathrm{H} / k_B \approx 1.5 \times 10^5\,$K, but this would be forgetting that with a billion photons for a baryon, even at lower temperatures the Universe still contains an enormous number of photons with energies high enough to ionise hydrogen atoms (the tail of the black body distribution). We therefore need to find the temperature for which the integral of the distribution of bodies at energies greater than $13.6\,\eV$ gives a photon density comparable to $n_b = \eta n_\gamma$. The ratio $\eta$ is therefore an important parameter that must be taken into account when estimating the recombination temperature.

A better estimate should therefore be based at least on the baryon to photon ratio $\eta$ and $B_\mathrm{H}$. As with the abundance of deuterium, at equilibrium we can describe :
\begin{align}
\frac{n_\mathrm{H}}{n_pn_e} & =\frac{g_\mathrm{H}}{g_p g_e} \left(\frac{k_B T}{2\pi \hbar^2}\right)^{-3/2}\left(\frac{m_\mathrm{H}}{m_p m_e}\right)^{3/2} \exp \left(\frac{(m_p+m_e-m_\mathrm{H})c^2}{k_B T} \right) \\
& \approx \left(\frac{m_e k_B T}{2\pi \hbar^2}\right)^{-3/2} \exp\left(\frac{B_\mathrm{H}}{k_B T}\right)
\end{align}
with $g_\mathrm{H}=4$[^spinH] and $g_p=g_e=2$. This is *Saha's equation*. Let $X_e$ be the fraction of free electrons in the primordial plasma:
$$X_e = \frac{n_e}{n_b}$$.
By arguments of electrical neutrality and conservation of the number of particles, we also have :
$$n_e\approx n_p,\quad X_e=\frac{n_p}{n_b}\approx \frac{n_p}{n_p + n_\mathrm{H}} $$
assuming there is only hydrogen to simplify the calculations (no helium [^Heneglect]). Consequently, we have :
\begin{equation}
\frac{1-X_e}{X_e} = n_p \left(\frac{m_e k_B T}{2\pi \hbar^2}\right)^{-3/2}  \exp\left(\frac{B_\mathrm{H}}{k_B T}\right)
\end{equation}
and simply
$$n_p \approx X_e \eta n_\gamma = \eta X_e \frac{2\zeta(3)}{\pi^2}\left(\frac{k_B T}{\hbar c}\right)^3 $$
so :
\begin{equation}
\frac{1-X_e}{X_e^2} = \frac{2\zeta(3)}{\pi^2}\eta \left(2\pi\frac{k_B T}{m_e c^2}\right)^{3/2}  \exp\left(\frac{B_\mathrm{H}}{k_B T}\right) \equiv a_\mathrm{H}
\end{equation}
We have a second-degree equation in $X_e$ whose solution is ({cite}`ryden2017` p.192):
$$X_e = \frac{-1 + \sqrt{1+ 4a_\mathrm{H}}}{2a_\mathrm{H}}$$.
We define the moment of recombination as the moment when the medium is half ionized, i.e. $X_e = 1/2$, then the decoupling temperature is given by {cite:p}`ryden2017` :
$$k_B T_{\mathrm{rec}} = 0.32\,\mathrm{eV} = \frac{B_\mathrm{H}}{42}$$
$$ \boxed{T_{\mathrm{rec}} = 3760\,\mathrm{K},\quad z_\mathrm{rec} = 1378}$$
i.e. when the Universe was $t_\mathrm{rec} = 250,000$ years old and its evolution is now dominated by its matter content. From the [](#fig:saha_Xe), however, we can see that recombination extends globally between redshift 1200 and 1600, which still corresponds to about $70\,000$ years, so it is not an instantaneous process. 

:::{figure} #saha_Xe
:name: fig:saha_Xe
:width: 70%

Ionisation fraction $X_e$ as a function of redshift during recombination.
:::

#### Photon decoupling

:::{figure} #rates_decoupling
:name: fig:rates_decoupling
:width: 70%

Comparison between the interaction rate $\Gamma_\gamma$ and the expansion rate $H$ as a function of redshift.
:::

For some time after $z_{\mathrm{rec}}$, the photons remain coupled to the small fraction of free electrons by Thomson scattering:
$$ e^- + \gamma \rightleftharpoons e^- + \gamma $$
The interaction rate is given by (see equation [](#eq:lpm_thomson)) :
$$\Gamma_\gamma = n_e \sigma_T c = n_b X_e \sigma_T c=  \frac{2\zeta(3)}{\pi^2} \eta  \sigma_T c\left(\frac{k_B T}{\hbar c}\right)^3$$
with the effective cross-section of Thomson scattering:
$$\sigma_T = 0.665\,\mathrm{barns} = 6.65\times 10^{-29}\,\mathrm{m}^2$$
Decoupling occurs when this interaction rate becomes small compared to the expansion rate of the Universe ([](#fig:rates_decoupling)), i.e. :
$$\Gamma_\gamma(T_\mathrm{dec}) = H(T_\mathrm{dec})$$
Since the Universe is then dominated by matter ($z<3000$), we have :
$$H(T_\mathrm{dec}) = H_0 \sqrt{\Omega_m^0(1+z)^3} = H_0 \sqrt{\Omega_m^0} \left(\frac{T_\mathrm{dec}}{T_0}\right)^{3/2}$$
The result is :
\begin{equation}
X_e(T_\mathrm{dec}) (k_B T_\mathrm{dec})^{3/2} \approx \frac{\pi^2}{2\zeta(3)}\frac{H_0 \sqrt{\Omega_m^0} } {\eta \sigma_T c} \left(\frac{k_B T_0}{\hbar c}\right)^{-3/2}
\end{equation}
By numerical resolution, we obtain :
$$
\boxed{T_{\mathrm{dec}} = 0.26\,\eV = 3055\,\kelvin, \quad z_{\mathrm{dec}}\sim 1100,  \quad t_{\mathrm{dec}}=370\,000\,\mathrm{ans}}
$$

:::{tip} Mean photon free path
:class:dropdown

Another way of looking at the decoupling of photons and matter, and therefore the moment when the Universe becomes transparent, is to look at the mean free path of photons $\ell_T(z) = 1/(\sigma_T n_e(z)c)$. In the distant past, the Universe was opaque but the mean free path of photons could still be of the order of a few light-years. After decoupling, this becomes greater than the typical size of the Universe. 

```{figure} #photon_mean_free_path
:name: fig:photon_mean_free_path
:width: 70%

Comparison between the mean free path time of photons $\tau_T$ and the Hubble time $1/H(z)$.
```

:::

The cosmic microwave background is therefore black-body radiation that was released about $380,000\,$ years after the Big Bang, when the Universe was almost completely neutral, since $X_e(T_{\mathrm{dec}}) = 6\times 10^{-3}$. 

:::{attention} The three pillars of the Big Bang

**The expansion of the Universe, an abundance of $24\%$ of helium, and the existence of a cosmic microwave background are the three pillars on which the Big Bang theory is based**.

Any alternative theory must explain these three observations.

:::


[^baryons]: hadrons are divided into two families: mesons (2 quarks) and baryons (3 quarks). among the baryons, only protons are stable. The neutrons bound in atomic nuclei are stable, but when free they disintegrate into a proton with a half-life of 15 minutes. Mesons are all unstable with half-lives shorter than $10^{-7}\,$s. Electrons are 2000 times lighter than protons. Most of the mass of so-called ‘ordinary’ matter is therefore contained in atomic nuclei, hence the shorthand ‘baryonic matter’.
[^mp]: remember that the masses of protons and neutrons are about $1\,\GeV$.
[^neutrality]: since electric charge is associated with Coulomb forces and the expansion of the universe is governed only by gravitational forces, the universe must be globally neutral.
[^Sconst]: stricto sensus an entropic integration constant $S_0$ must appear but this is zero by virtue of the third principle of thermodynamics.
[^Tfreeze]: in a certain number of references, the neutron freezing temperature $T_{\mathrm{freeze}}$ is found. \approx 0.8\,\MeV$ which also corresponds to 1 neutron for 6 protons if we follow the equilibrium distribution [](#eq:np_eq) but admitting that this temperature is a good order of magnitude for it to work in the end.
[^spinH]: a hydrogen atom can have a spin 0 (inverted spins) or 1 (alginate spins) so 4 internal degrees of freedom.
[^Heneglect]: with one neutron for every 7 protons, $n_\mathrm{He} = n_\mathrm{H} / 12$ so more than $90\%$ of baryons are protons. 
