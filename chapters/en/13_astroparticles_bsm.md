---
short_title: Astroparticle physics beyond the standard model 
authors:
  - jbiteau
keywords: dark matter, lorentz invariance violation
---

Indirect searches for dark matter and signatures of physics beyond the Standard Model
=============================================


Shortcomings of the Standard Model
--------------------------------

### Observational facts: baryons at subdominant at most scales

Particle and nuclear physics allow us to understand the arrangement of observable matter in terms of baryons and 
leptons. Although the census of baryons seems to be consistent between estimates from big bang nucleosynthesis, CMB 
observations and probes of the intergalactic plasma (see {cite}`2021NatAs...5..852D`), the gravitational field 
arising from this baryonic matter does not seem to be strong enough, whether at the scale of galaxies, of galaxy 
clusters or even the cosmic microwave background.

#### Galactic scales

Kinematics is a fundamental tool for studying the distribution of matter in the universe. The distribution of the 
position and velocity of the stars in our Galaxy, measured by the Gaia satellite, can be used to reconstruct the 
rotation curve of the Milky Way, i.e. the rotation velocity of the stars as a function of their distance from Sgr A*,
as shown in [](fig:MWrotcurve).

:::{figure}  ../../images/rotation_curve_Jiao.png
:name: fig:MWrotcurve
:align: center
:width: 100%

 Rotation curve of the Milky Way, i.e. circular velocity as a function of distance to the center of the Milky Way. 
 _Extracted from {cite}`2023A&A...678A.208J`_.
:::

Modelling this data provides an estimate of the total kinematic mass of the Milky Way of
$(2.0 \pm 0.1) \times 10^{11}\,M_\odot$  ({cite}`2023A&A...678A.208J`). This estimate seems reliable insofar as the 
Gaia data hints at the presence of a Keplerian decline, i.e. $m \frac{v^2}{r} = \frac{GmM}{r^2} \Rightarrow v \propto r^
{-1/2}$ 
(for a circular orbit). Such a Keplerian decline is at odds with MOdified Newtonian Dynamics (MOND) theories,
which suggest a flat rotation curve at long distances. Despite this undeniable success in the field of stellar 
kinematics, it should be noted that the estimate of the total mass of the Milky Way remains uncertain: it could be 
up to $5-6$ times higher than the mass derived from stellar kinematics if one uses instead dwarf galacies orbiting the 
Milky Way (see discussion in {cite}`2025arXiv250104075H`).

By comparison, the directly observable mass in our Galaxy, i.e. its stellar mass, represents only
$(0.6 \pm 0.1) \times 10^{11}\,M_\odot$ ({cite}`2015ApJ...806...96L`) with an expected contribution from gas and dust 
of ${\sim}\,10\%$ and ${\sim}\,1\%$, respectively. At least 70% of the mass of the Milky Way is **dark** (emitting no, or 
barely any, radiation).

In addition, modelling of the Gaia 6D data provides an estimate of the speed at which the Sun revolves around Sgr A*,
i.e. $v_\odot = 233 \pm 3\,\text{km\,s}^{-1}$ as well as of the escape velocity from the Milky Way halo, i.e. 
$v_\text{esc} = 528 \pm 25\,\text{km\,s}^{-1}$ (see {cite}`2018arXiv181011468E`). This relatively low escape 
velocity indicates that dark matter moves at low speed ($< v_\text{esc}$): dark matter must be **cold**.

The local energy density of cold dark matter is inferred at 
$\varepsilon_{\text{DM}, \odot} = 0.44 \pm 0.02\,\text{GeV\,cm}^{-3}$, that is, for comparison, about $10^6$ times 
the energy density of photon fields, magnetic fields or cosmic rays in the Milky Way.

#### Galaxy clusters

On a larger scale, galaxy clusters are the structures in the cosmic web whose matter distribution is best known (see 
e.g. {cite}`2013ApJ...778...14G`). Their gas content is estimated from their thermal Bremsstrahlung emission in X 
rays. Their stellar content is measured from their total near-infrared emission. 

The total gravitational mass of galaxy clusters can be estimated by several methods:
- Lensing, if Einstein rings from a background source can be observed ;
- Virial theorem, applied to the galaxies in the cluster, i.e. $2E_\text{c} + E_\text{p} = 0$, where $E_\text{c}$ 
  and $E_\text{p}$ are the kinetic and potential energies respectively;
- Density and temperature profiles of the hot X-ray emitting gas, assuming hydrostatic equilibrium (self-gravity = 
  internal pressure).

As shown in [](fig:ClusterBaryonFrac), the sum of the stellar mass fraction and the gas mass fraction, i.e. the baryon fraction,
is relatively independent of the total mass of the cluster: baryons contribute between 10% and 20% of the total mass in
clusters.

:::{figure}  ../../images/clusters_baryon_fraction.png
:name: fig:ClusterBaryonFrac
:align: center
:width: 100%

 Stellar, gas and baryon fraction as a function of total mass in a sample of 15 galaxy clusters.
 _Extracted from {cite}`2013ApJ...778...14G`_.
:::

#### CMB angular power spectrum

The CMB power spectrum is a powerful tool for determining the energy density of the various components when matter 
and radiation decoupled. A detailed discussion of the CMB spectrum is beyond the scope of this course. However, it 
should be noted that the amplitude of the fluctuations observed on angular scales ranging from a few arcminutes to a 
degree depends directly on the total matter density ($\equiv$ dark + baryonic mater), whereas the amplitude of the 
fluctuations on smaller angular 
scales depends on the baryon density. Detailed modelling of the CMB power spectrum measured with the Planck satellite
({cite}`Planck2018`) yields a ratio of the baryon energy density to the total matter density
$$
\frac{\Omega_\text{b}}{\Omega_\text{m}} = 15.7 \pm 0.1 \%.
$$
Whether the universe is observed at the kpc scale (galaxies), the Mpc scale (galaxy clusters) or the Gpc scale (CMBs)
, it appears that nearly $80\%$ of the mass needed to hold the various observed structures together is missing. The 
relative coherence of the baryonic fraction at all these scales leads to the hypothesis of the existence of cold 
dark matter, the nature of which is still unknown.

### Notes on numerical approaches

The study of the formation of large structures in the nonlinear regime using N-body simulations (dark matter) and 
hydrodynamical simulations (including baryonic physics) has led to tremendous advances in our understanding of the 
cosmic web and galaxy populations, as illustrated in [](#fig:LambdaCDMsims). 

:::{figure}  ../../images/figure_simulations_LambdaCDM.png
:name: fig:LambdaCDMsims
:align: center
:width: 100%

 Slices of simulations of the cosmic web and of zoomed-in regions (dedicated simulations) in a $\Lambda\text
 {CDM}$ framework.
 _Extracted from {cite}`2020NatRP...2...42V`_.
:::

It should be noted that simulations on small and intermediate scales (kpc-Mpc) have historically encountered a 
number of difficulties. These include:
- The core-cusp problem: the simulated dark matter density profiles appear too pointy compared to what can be 
  inferred from kinematic observations. The likely solution to this problem lies in outflows in the vicinity of 
  supermassive black holes (jets, winds) or in central regions of high star formation (collective winds from stellar 
  explosions);
- The number of satellites of giant galaxies: the simulations tend to produce too many (100-1000) dwarf satellite 
  galaxies compared to the hundred or so observed around the Milky Way at masses above $300\,M_\odot$. The solution 
  to this problem probably lies in the lower efficiency of galaxy formation at the lower masses of dark matter halos.
- Size of the largest satellites: Simulated halos of satellite galaxies tend to be larger than those of the largest 
  galaxies orbiting the Milky Way and Andromeda. The likely solution to this problem lies in tidal stripping effects on baryons.

In all three cases, the inclusion of feedback from outflows and tidal effects appears to be crucial for the 
agreement between simulations and observations.



Dark-matter candidates and beyond-standard model physics
--------------------------------

The two main properties inferred for dark matter are
- Cold: a low bulk/rms velocity, i.e. $\langle v \rangle < v_\text{esc}$ and $\langle v^2 \rangle < v_\text{esc}^2$, 
  so that dark matter does not escape from the Milky Way halo.
- Dark: while being coupled to the gravitational sector, dark matter should be weakly coupled to the particles of 
  the Standard Model. Otherwise we would see dark matter e.g. through its electromagnetic emission. This darkness 
  suggests candidates with no electric charge or colour, and a lifetime longer than the age of the Universe.

The three main candidates put forward that appear to meet these criteria are discussed below.

### Wave dark matter candidates

The first quantity to consider for a candidate $a$ of wave nature is its de Broglie wavelength:
$$
\lambda_a = \frac{h}{p_a} = \frac{h}{m_a v_a},
$$
with velocity $v_a < v_\text{esc}$, e.g. $v_a \approx 10 \,\text{km\,s}^{-1}$. Consider a wave that extends at most 
on the kpc scale to keep the packet sufficiently concentrated in the centre of the galaxies, i.e.
$\lambda_a \leq 1\,\text{kpc}$. This condition imposes a minimum mass on the candidate:
\begin{align}
m_a c^2 &= \frac{hc}{\lambda_a} \left(\frac{v_a}{c}\right)^{-1}\\
& =  \frac{2 \pi \times 0.197 \times 10^{-6} }{3.1 \times 10^{19}} \left(\frac{10}{300\,000}\right)^{-1}\,\text{eV} 
\times \left(\frac{v_a}{10\,\text{km\,s}^{-1}}\right)^{-1} \left(\frac{\lambda_a}{1\,\text{kpc}}\right)^{-1}\\
& =  1.2\times 10^{-21}\,\text{eV} 
\times \left(\frac{v_a}{10\,\text{km\,s}^{-1}}\right)^{-1} \left(\frac{\lambda_a}{1\,\text{kpc}}\right)^{-1}.
\end{align}

On the opposite end of the mass range, one can use the local energy density of
$\varepsilon_{\text{DM}, \odot} = 0.44 \pm 0.02\,\text{GeV\,cm}^{-3}$ 
to set the maximum mass a wave dark-matter candidate. Such a candidate would have to be bosonic in nature and a 
sufficient number of particles would have to occupy a cell for a condensate to form, i.e.
$(\lambda_a/2\pi)^3 \times (\varepsilon_{\text{DM}, \odot}/m_ac^2) > 1$. With a bit of algebra, one finds
\begin{align}
m_a c^2 &< \left[\varepsilon_{\text{DM}, \odot} \left( \frac{v_a}{c}\right)^{-3} \left(\hbar c \right)^
{3} \right]^{1/4}\\
&\lesssim 50\,\text{eV}\times\left(\frac{\varepsilon_{\text{DM}, \odot}}{0.44\,\text{GeV\,cm}^{-3}}\right)^{1/4}
\times\left(\frac{v_a}{10\,\text{km\,s}^{-1}}\right)^{-3/4}
\end{align}

Wave dark-matter candidates are therefore searched for in a broad mass range covering $10^{-21}-10^2\,\text{eV}$. 
The most promising candidates from particle physics are the axions, which remain unobserved to date. These 
hypothetical particles have been invoked to solve the strong CP problem in quantum chromodynamics, i.e. the fact 
that the electric dipole moment of neutrons is observed to be $>10^{10}$ times weaker than expected from the 
Standard Model.

Axions from quantum chromodynamics exhibit a mass-dependent coupling to photons, $g_{a\gamma\gamma}$. More generally, 
axion-like particles are searched for in the whole parameter space $\{m_a, g_{a\gamma\gamma}\}$. Gamma-ray astronomy 
at GeV-TeV energies currently places the strongest constraints on the coupling of axion-like particles to the 
electromagnetic sector for masses in the neV energy range. The mass range that remains open for axions to explain 
dark matter goes up to ${\sim}\,1\,eV$ while the entire mass range remain open for axion_like particles.

### Particle dark matter candidates

Weakly interacting massive particles (WIMPs) with $m_\text{text} = O(100\,\text{GeV}$ decouple ("freeze out") at the 
right time, $T_\text{freeze-out} \approx 5\,\text{GeV}$, to produce today's relic abundance. This is the so-called 
WIMP miracle, which is seriously put to the test by recent measurements around $100\,GeV$.

The relic abundance depends on the annihilation cross section, $\sigma$, or on the decay time in one or more 
channels that are hopefully linked to the Standard Model. The equation that governs the evolution of the comoving 
density of the number of dark matter particles, $n$, is $\dd (na^3)/\dd t = 0$, with $a$ the scale factor, i.e.
\begin{align}
a^3 \frac{\dd n}{\dd t} + 3 \dot a a^2 n &= 0\\
\frac{\dd n}{\dd t} + 3 H n &= 0,
\end{align}
where $H = \frac{\dot a}{a}$.

With losses due to annihilation, the equation becomes
$$
\frac{\dd n}{\dd t} + 3 H n &= -n^2 \langle \sigma v \rangle + C,
$$
where $C=n_{eq}^2 \langle \sigma v \rangle$ is a constant such that without loss term $n = n_{eq}$.

Freeze-out occurs for $3 H n \approx n^2 \langle \sigma v \rangle$ i.e. for $\Omega_\text{DM} \propto n \propto \frac
{1}{ \langle \sigma v \rangle}$. The thermal averaged annihilation cross section, such as $\Omega_\text{DM} = 
\Omega_\text{DM}|_\text{CMB}$, is $\langle \sigma v \rangle \approx 2 \times 10^{-26}\,\text{cm}^3\,\text{s}^{-1}$. 
As illustrated in [](#fig:WIMPs), annihilation of WIMPs in the $b \bar b$ channel has been ruled out for masses up 
to ${\sim}\,200\,\text{GeV}$ by Fermi-LAT observations of dwarf galaxies, where little gamma-ray emission from 
astrophysical sources is expected. The mass range remains open at higher energies. This channel is expected to be 
probed down to the thermal cross section for masses up to ${\sim}\,10\,\text{TeV}$ with the Cherenkov Telescope 
Array Observatory (CTAO). CTAO observations should then either close the mass range usually inferred for WIMP dark 
matter (if dark decays through the $b\bar b$ channel) or discover its signature.

:::{figure}  ../../images/WIMPs.png
:name: fig:WIMPs
:align: center
:width: 100%

 Upper limits on the annihilation cross section of WIMPs as a function of the mass the dark matter candidate. The 
 thermal cross section is shown in yellow. _Extracted from {cite}`2024arXiv240601705C`_.
:::

### Macroscopic dark matter candidates

Let's conclude this overview with the macroscopic dark matter candidates. A wide range of masses have been ruled out 
by lensing studies, namely masses greater than $10^{-11}\,M_\odot$, i.e. heavier than large asteroids. At lower 
masses, the remaining viable candidates are primordial black holes, formed not by the collapse of stars but by that 
of initial overdensities, for example during the radiation era.

Such small black holes are expected to emit a blackbody spectrum with a temperature of ({cite}`1974Natur.248...30H`):
\begin{align}
T_\bullet &= \frac{\hbar c^3}{8\pi k_\text{B} GM_\bullet}\\
& \approx 10^{-7}\,\text{K} \left(\frac{M_\bullet}{M_\odot} \right)^{-1}
\end{align}

The energy loss rate then follows the Stefan-Boltzmann law:
$$
\frac{\dd M_\bullet c^2}{\dd t} = - A \sigma_\text{SB}T_\bullet^4,
$$
where $\sigma_\text{SB} = \frac{\pi^2 k_\text{B}^4}{60 \hbar^3 c^2}$ is the  Stefan-Boltzmann constant and where $A 
= 4\pi R_\text{S}^2$ with $R_\text{S} = \frac{2GM_\bullet}{c^2}$  the Schwarzschild radius.

This yields
\begin{align}
\frac{\dd M_\bullet}{\dd t} &= - \frac{1}{15360\pi} \frac{\hbar c^4}{G^2M^2}\\
3M^2\frac{\dd M_\bullet}{\dd t} &= - \frac{1}{5120\pi} \frac{\hbar c^4}{G^2}\\
\frac{\dd M_\bullet^3}{\dd t} &= - \frac{1}{5120\pi} \frac{\hbar c^4}{G^2}\\
M_\bullet^3 &= M_0^3 \times (1-t/\tau_0), 
\end{align}
where
\begin{align}
\tau_0 & = 5120\pi \frac{G^2 M_0^3}{\hbar c^4}\\
&\approx 2 \times 10^{10}\,\text{yr} \times \left( \frac{M_0}{10^{-19} M_\odot} \right)^3,
\end{align}
that is a timescale comparable to the age of the universe for an initial mass $M_0 = 10^{-19} M_\odot$. Such an 
initial mass yields an initial black-body temperature $T_0 \approx 10^{12}\,K \approx 100\,\text{MeV}$ which should 
increase as the primordial black hole evaporates.

We therefore expect Standard Model particles with energy/mass ${>}\,100\,\text{MeV}$ to be emitted during the final 
stages of the evaporation of the primordial black hole. Searching for the time signature of such events through 
their emission of cosmic rays, gamma rays and neutrinos has ruled out the possibility that primordial black holes of 
less than $10^{-17}\,M_\odot$ make up 100% of the dark matter. 

The mass range between $10^{-17}\,M_\odot$ and $10^{-11}\,M_\odot$ remains open for macroscopic dark matter.

### Other searches beyond the standard model

A last type of search for physics beyond the Standard Model using astroparticles is worth mentioning here, although 
it does not involve dark matter. Because of their high energies and the large distances they travel, astroparticles 
are remarkable probes of the violation of Lorentz invariance. The reference energy at which such violations might be 
expected, in theories attempting to unify gravity with the other fundamental forces, is Planck's energy, $E_\text{Pl}
\approx 1.2 \times 10^{28}\,\text{eV}$. The Planck energy may seem far from the energies reached by 
astrophysical sources (let alone by humans), but the distance helps...

The observational constraints are most often placed on corrective terms (Taylor expansion like) to the dispersion 
relation that is expected in effective field theories:
$$
\label{eq:liv}
E^2 = p^2 c^2 + m^2 c^4 \pm E^2 \left(\frac{E}{E_\text{LIV}} \right)^n,
$$
where $(E, \vec{p}c)$ is the four momentum of the particle of interest, $m$ its mass, $E_\text{LIV}$ the energy of 
the violation (presumably close to the Planck scale) and $n$ the order of the modification. The sign $\pm$ indicates 
that both signs are considered for the modification, with the $+$ sign corresponding to a so-called superluminal 
term and the $-$ sign to a subluminal term.

Note that corrective terms with an even order (e.g. $n=2$ for quadratic term) emerge from operators that are 
invariant under charge/parity/time-reversal (CPT) symmetries, although the CPT symmetry could be violated at 
energies close to the Planck scale.

Two types of signatures emerging from the corrective term are searched: a temporal signal and a spectral signature. The 
search for such effects requires the use of the most variable and most energetic extragalactic sources, namely 
jetted active galactic nuclei and gamma-ray bursts. The best constraints using both channels and the types of 
sources nowadays exclude a linear modification of the dispersion relation up to a few times the Planck scale. 

#### Temporal signature of Lorentz invariance violation

The energy-dependent time signature can be understood using the mechanical Hamiltonian $v \equiv \frac{\dd E}{\dd t}$.
By differentiating Equation [](eq:liv), we get
$$
2E\dd E = 2pc^2\dd p \pm (2+n)\left(\frac{E}{E_\text{LIV}} \right)^n E \dd E,
$$
that is
\begin{align}
v & \equiv \frac{\dd E}{\dd p}\\
& = c \times \frac{pc}{E} \times \frac{1}{1 \mp \left(n+\frac{1}{2}\right) \left(\frac{E}{E_\text{LIV}} \right)^n}\\
& \approx c \times \left[ 1 \pm \left(n+\frac{1}{2}\right) \left(\frac{E}{E_\text{LIV}} \right)^n \right],
\end{align}
as $\frac{pc}{E} \approx 1$ for the energies relevant to astroparticles. This equation justifies the use of the term 
super/subluminal for the positive/negative corrective term in Equation [](eq:liv).

The difference in arrival time between two photons of energies $E_1$ and $E_2$ emitted at the same time by a source 
located at a light-travel distance $d$ is thus:
\begin{align}
t(E_2) - t(E_1) &\approx \frac{d}{v(E_2)} - \frac{d}{v(E_1)}\\
& \approx \mp \left(n+\frac{1}{2}\right) \times \frac{d}{c} \times \frac{E_2^n-E_1^n}{E_\text{LIV}^n},
\end{align}
where we have neglected the redshift dependence.

For a subluminal linear modification of the dispersion relation of gamma-rays, if $E_2-E_1 \approx 1\,\text{TeV} 
(\approx 10^{-16}E_\text{Pl})$ and for a source located at $d = 1\,\text{Gpc} \approx 3.1 \times 10^{25}\,\text{m}$, 
one gets
\begin{align}
t(E_2) - t(E_1) &\approx - \frac{3}{2} \frac{d}{c} \times \frac{E_2-E_1}{E_\text{LIV}}\\
 &\approx - \frac{3}{2} \times\frac{3.1 \times 10^{25}}{3\times 10^8} \times 10^{-16} \,\text{s} \left(\frac{E_\text
{LIV}}{E_\text{Pl}}\right)^{-1}\\
&\approx - 15\,\text{s} \times \left(\frac{E_\text{LIV}}{E_\text{Pl}}\right)^{-1}.
\end{align}

This corresponds to the observed short timescale variability e.g. of gamma-ray bursts, enabling to place stringent  
lower limits on $E_\text{LIV}$ for a linear modification. 

#### Spectral signature of Lorentz invariance violation

The second signature is based on the modification of the pair-production threshold, for gamma-rays traveling over 
cosmic distances and interacting with photons of the cosmic infrared background.

A subluminal modification of the dispersion relation of photons, of energy $E$ (assuming that the electrons are not 
affected for the sake of simplicity) yields a modification of the infrared photon threshold energy as ({cite}`2008PhRvD..78l4010J`):
\begin{align}
\epsilon_\text{th} &= \frac{m_e^2c^4}{E} + \frac{1}{4} \left(\frac{E}{E_\text{LIV}} \right)^n E\\
&= \frac{m_e^2c^4}{E} \times \left[ 1 + \left(\frac{E}{E_{\gamma\text{, mod}}} \right)^{n+2}  \right],
\end{align}
where 
\begin{align}
E_{\gamma\text{, mod}} &= \left[ (2m_ec^2)^2 E_\text{LIV}^n \right]^{\frac{1}{n+2}}\\
& \approx 20\,\text{TeV} \times  \left(\frac{E_\text{LIV}}{E_\text{Pl}}\right)^{\frac{1}{3}}\text{ for n = 1}.
\end{align}

This is precisely the energy up to which $\gamma$-rays at distances around $100\,\text{Mpc}$ have been observed, 
enabling to place stringent lower limits on $E_\text{LIV}$ for a linear modification. Although a linear modification 
of the dispersion relation is now ruled out up to the Planck scale, the energy range beyond $10^{-8} E_\text{Pl}$ 
remains open for the quadratic subluminal term, which arises from an operator invariant by CPT symmetry.

:::{tip}
**Notions from this chapter**

_Dark matter_
- What are the dynamical arguments for dark matter?
- What are the three main candidates for dark matter?

_Lorentz invariance violation_
- What effects can be used to probe Lorentz invariance violation up to the Planck energy scale?
:::