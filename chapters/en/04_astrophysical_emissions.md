---
short_title: []
authors:
  - jbiteau
keywords: []
---


Astrophysical emissions on cosmic scales
=============================================


*Note 1: energy densities written either as u or $\rho$: to be solved*

*Note 2: final plot dJ/dE -> J(E), same in slide*

*Note 3: discussion on various backgrounds to be written*

A homogeneous and isotropic universe?
--------------------------------

The cosmological models that we have discussed postulate that the universe is homogeneous and isotropic on large scales, i.e. typical distances greater than 100 Mpc. Below this characteristic scale, the galaxies observed in wide-field optical surveys are distributed according to the cosmic web. The large structures that weave this web formed as a result of the growth of the fluctuations in the CMB. Due to the properties of gravitation, an initially ellipsoidal overdensity collapses preferentially along its smallest axis, resulting in a sheet (so called Zel'dovich pancake). These sheets can collapse in the form of filaments, which themselves converge towards galaxy clusters. The areas not populated by the cosmic web constitute the cosmic voids, which occupy most of space.

### Distance from local large-scale structures

These structures arrange themselves in a network resembling that of soap bubbles. A simplified crystallographic representation is given below, with $l$ the characteristic cell size and $w$ the typical diameter of clusters, or the cross-section of filaments. Cosmological simulations suggest a void occupancy rate of the order of $(1-w/l)³ = 75\%$ (see exercise below). Knowing that the characteristic radius of the clusters we observe is $w \approx 1\,$Mpc, we deduce a typical cell size of the order of $l \approx 10\,$Mpc.


:::{figure} ../../images/bubble_network_2019GReGr..51....9F_ 2022A&A...662A..87O.jpg
:name: fig:bubble_network
:align: center
:width: 100%

Network of soap bubbles and cubic model illustrating the structure of the cosmic web. On the right-hand side, the nodes in orange correspond to the clusters, the sheets and filaments are in sky blue and the voids in dark blue. Images taken from {cite}`2019GReGr..51....9F` and {cite}`2022A&A...662A..87O`.
:::

:::{exercise} Volume filling factor rate of large-scale structures
:label: exo:volume_filling

Assess the relative volume occupancy of clusters, filaments and sheets using a crystallographic approach as presented above.
:::

:::{solution} exo:volume_filling
:class: dropdown

In the crystallographic approach presented above, the volume filling factors of clusters, $\mathrm{VFF}_\mathrm{c}$, filaments, $\mathrm{VFF}_\mathrm{f}$, sheets, $\mathrm{VFF}_\mathrm{s}$ and voids, $\mathrm{VFF}_\mathrm{v}$ are

$$
\begin{aligned}
\mathrm{VFF}_\mathrm{c} &= \left(\frac{w}{l}\right)^3 \nonumber \\
\mathrm{VFF}_\mathrm{f} &= 3\left(\frac{w}{l}\right)^2 \left(1 - \frac{w}{l}\right) \nonumber \\
\mathrm{VFF}_\mathrm{s} &= 3\frac{w}{l} \left(1-\frac{w}{l}\right)^2 \nonumber \\
\mathrm{VFF}_\mathrm{v} &= \left(1-\frac{w}{l}\right)^3
\end{aligned}
$$

Note that the sum is equal to 1 because of the binomial identity $\left(\frac{w}{l} + \left(1-\frac{w}{l}\right)\right)^3 = 1$.


The following table, adapted from {cite}`2022A&A...662A..87O`, provides a comparison between our simple estimate and values inferred in a typical set of cosmological simulations.

| Structure type | Cubic cell $w/l = 0.1$ |  Cosmic simulation results |
| :------------- | :--------------------: | :------------------------: |
| Voids          | 72.9%                  | 76%                        |
| Sheets         | 24.3%                  | 18%                        |
| Filaments      |  2.7%                  |  5%                        |
| Clusters       |  0.1%                  |0.5%                        |

Large-scale cosmological simulations indicate that at $z=0$, clusters and filaments encompass ${\sim}\,50\%$ and ${\sim}\,45\%$ of dark matter respectively. Taking into account feedback from galaxy winds and jets suggests a more diffuse baryon distribution: ${\sim}\,25\%$ of baryons would be found in clusters, ${\sim}\,45\%$ in filaments and sheets, ${\sim}\,30\%$ in voids {cite:p}`2016MNRAS.457.3024H`.
:::

These four types of structure are visible in the distribution of nearby galaxies. Our galaxy, its neighbour Andromeda at $0.75\,$Mpc and their satellites, such as the Large Magellanic Cloud at $50\,$kpc, form the Local Group. As illustrated in 
[](#fig:council-giants), the Local Group is at the heart of the Local Sheet. This sheet is a planar structure with a diameter of ${\sim}\,10\,$Mpc, delimiting one side of the Local Void.


:::{figure}  ../../images/mccall_fig3.jpeg
:name: fig:council-giants
:align: center
:width: 70%

Local Sheet galaxies ($R \approx 5\,$Mpc) surrounding the local group ($R \approx 0.5\,$ Mpc). From {cite}`2014MNRAS.440..405M`.
:::

Opposite the galaxy NGC 253, about $16\,$Mpc from the Milky Way, is the Virgo cluster of galaxies, which has a rugby ball structure, as can be seen below. Galaxy clusters can contain several thousand galaxies.

:::{figure}  ../../images/virgo_2007ApJ...655..144M.jpg
:name: fig:virgo
:align: center
:width: 70%

Spatial distribution of galaxies in the Virgo cluster with well constrained distances in  supergalactic coordinates (the supergalactic plane is an historical structure almost identical to the Local Sheet, with a tilt of 8°). The brightest galaxies are shown in red. From {cite}`2007ApJ...655..144M`.
:::

Clusters of galaxies such as Virgo are connected to the cosmic web by filaments of galaxies, whose position in the celestial plane and radial velocity projection can be inferred by spectroscopy, as illustrated below.

:::{figure}  ../../images/virgo_filaments_2022ApJS..259...43C
:name: fig:filaments
:align: center
:width: 100%

The filaments around the Virgo cluster. The distribution of galaxies in the sky is shown in equatorial coordinates (right ascension, R.A., and declination, Dec, in degrees). From {cite}`2022ApJS..259...43C`.
:::

On an even larger scale, typically $100\,$Mpc, the clusters are grouped into superclusters such as Laniakea, which hosts us.

:::{figure}  ../../images/laniakea_2014Natur.513...71T.jpg
:name: fig:supercluster
:align: center
:width: 100%

The local superclusters. Velocity streamlines of our supercluster, Laniakea, are shown in white. From {cite}`2014Natur.513...71T`.
:::

### Mass of local large-scale structures

Not only can astronomers measure the position of galaxies in the sky, they can also measure the radial component of their velocity as well as their distance from the stars that calibrate the cosmic distance ladder. The velocity field of galaxies can thus be used to constrain the gravitational field of Laniakea or its companion supercluster Perseus-Pisces. The mass of the Laniakea supercluster is estimated at ${\sim}\,10^{17}\, M_\odot$ {cite:p}`2014Natur.513...71T` [^a]. On a smaller scale, the mass of the Virgo cluster is estimated at ${\sim}\,10^{14}\, M_\odot$ {cite:p}`2016A&A...596A.101P`. Such dynamical arguments also yield an estimate of the mass of the Local Group of galaxies at ${\sim}\,3 \times 10^{12}\, M_\odot$. The Local Group dynamical mass is dominated by that of the Milky Way, $(1. 2 \pm 0.2)  \times 10^{12}\, M_\odot$ and Andromeda, $(1.8 \pm 0.5) 10^{12}\, M_\odot$ {cite:p}`2022ApJ...928L...5B`.


[^a]: The sun has a mass measured with better than $10^{-4}$ accuracy at  $M_\odot = 1.9885 \times 10^{30}\,$kg.


These masses are deduced using dynamical arguments such as Viriel's theorem (|kinetic energy| = |potential energy|/2 for a system at equilibrium) or using the projected trajectories of the tracers. Using stars as tracers, astronomers estimate the mass of the central black hole of the Milky Way, Sgr A*, at $(4.15 \pm 0.01) \times 10^{6}\, M_\odot$ {cite:p}`2019A&A...625L..10G` (see [](#fig:S2-trajectory) ). The latter has a small contribution to the mass of our galaxy compared with the stars that make it up $(6 \pm 1)  \times 10^{10}\, M_\odot$ {cite:p}`2015ApJ...806...96L`. The mass of the Milky Way contained in the stars (and dust) is itself about 20 times less than its dynamic mass.

:::{figure}  ../../images/S2_orbit.jpg
:name: fig:S2-trajectory
:align: center
:width: 100%

The 16-year orbit of the star S2 around the massive black hole Sgr A*, which has also been followed spectroscopically for 27 years. From {cite}`2019A&A...625L..10G`.
:::

The mass deficit observed in the Milky Way is also inferred at the level of galaxy populations. The stellar mass of each galaxy can be estimated using near-infrared observations. At these wavelengths (around $1-3\,$µm), the emission from medium-sized stars like the Sun is high compared with that from dust, which emits mainly at wavelengths greater than $5\,$µm, and from more massive and younger stars, which emit mainly in the UV and blue band.


:::{exercise} Mass in stars
:label: exo:stellar_mass

Assuming that the mass (or associated luminosity) follows a distribution law according to a Schechter function, 
$$f(M_\star) \dd M_\star= n_\star \left(\frac{M_\star}{M_0} \right)^{-\alpha} \exp\left(-\frac{M_\star}{M_0} \right) \dd M_\star,
$$
calculate the stellar-mass energy density using [](#fig:stellar_mass).
:::

:::{figure}  ../../images/stellar_mass_fun_2022MNRAS.513..439D.jpg
:name: fig:stellar_mass
:align: center
:width: 100%

The stellar mass function of the galaxies in the local Universe ($z<0.1$). From  {cite}`2022MNRAS.513..439D`.
:::

:::{solution} exo:stellar_mass
:class: dropdown

The first panel represents the function $g(M_\star)$ such as $\int g(M_\star) \dd \log_{10}M_\star = 1/V$, where $V$ is the considered volume. Thus $f(M_\star) = g(M_\star)/(\ln(10)M_\star)$.

From the first panel, we estimate by eye a cut-off at $M_0 \approx 1 \times 10^{11}
\,M_\odot$ where the density is $\ln(10) M_0 n_{\star}/e \approx 2  \times  10^{-3}\,\mathrm{Mpc}^{-3}\,\mathrm{dex}^{-1}$. We find $n_{\star} M_0 \approx 2 \times 10^{-3} \,\mathrm{Mpc}^{-3}$. The index is similarly estimated at $\alpha=1.5$.

The stellar mass energy density is then

$$
\begin{align}
\int f(M_\star) M_\star c^2 \dd M_\star &= n_\star M_0 \times M_0  c^2 \int \dd x \, x^{1-\alpha} \exp(-x) dx \nonumber\\
							&=\Gamma(2-\alpha) \times n_\star M_0 \times M_0  c^2 \nonumber\\					
							&\approx \sqrt{\pi} \times 2 \cdot 10^{-3} \times 10^{11} \times  1.1 \cdot 10^{66}/(3.1 \cdot 10^{22})^3\,\mathrm{eV\,m}^{-3} \nonumber\\
														&\approx 13 \times 10^{6}\,\mathrm{eV\,m}^{-3} 
\end{align}
$$

Estimation using the exact form of the mass distribution function gives a stellar matter density up to $z < 0. 1$  or $D_L < 500\,$Mpc of $\rho_{\star, 0}= (2.97 \pm 0.04) \times 10^8 \,h_{70}\, M_\odot \, \mathrm{Mpc}^{-3}$, where $h_{70} = H_0 / (70\,\mathrm{km}\,\mathrm{s}^{-1}\,\mathrm{Mpc}^{-1})$. This corresponds to an energy density comparable to our crude estimate, namely $\epsilon_{\star, 0} \approx (11.0 \pm 0.1) \, h_{70} \times 10^{6}\,\mathrm{eV\,m}^{-3}$
:::


:::{note} $M_\odot$ per Mpc$^{3}$ and eV per m$^3$
The rest-mass energy of the sun is $M_\odot c^2 \approx 1.8\times 10^{47} \, \mathrm{J} \approx 1.1\times 10^{66}\,\mathrm{eV}$. The typical distance between neighboring galaxies is $1\, \mathrm{Mpc} \approx 3.1 \times 10^{22}\, \mathrm{m}$. The good  match between powers of ten ($66 = 22 \times 3$) makes it fairly easy to convert stellar mass density into energy density.
:::

### Cosmic energy inventory

For an energy density today equal to the critical density $\rho_{c,0} = \frac{3 H_0^2  c^2}{8\pi G} = 1.36 \times 10^{11}\, h_{70}\, M_\odot\,\mathrm{Mpc}^{-3}$, i.e. $\epsilon_{c,0} = \approx 5.1\, h_{70}\,$GeV$\,$m$^{-3}$, where $h_{70} = H_0 / 70 \,\mathrm{km}\,\mathrm{s}^{-1}\,\mathrm{Mpc}^{-1}$, we can see that only two thousandths of the universe's energy budget is made up of stars. A detailed breakdown of the different energy budgets of the universe is shown below.

:::{figure}  ../../images/cosmic_inventory.png
:name: fig:cosmic_inventory
:align: center
:width: 100%

The cosmic energy inventory of {cite}`2004ApJ...616..643F`. Adapted from this [page](https://www2.mpia-hd.mpg.de/home/poessel/UT2012/).
:::


:::{important}
Most of what we know about the universe comes from  four messengers: photons, neutrinos, cosmic rays and gravitational waves. As shown in  [](#fig:cosmic_inventory), the energy density associated with these tracers is only a few parts per million. Despite this, estimates of the amount of baryonic matter from radiation are increasingly precise. Of particular note is the potential resolution of a long-standing problem, the location of the missing half of the universe's baryons, which could be found in the warm/hot intergalactic plasma that makes up the cosmic web (see {cite}`2021NatAs...5..852D`).
:::



Cosmic-scale engines behind astrophysical emissions
--------------------------------

The processes responsible for most astrophysical emissions are star formation, the accretion of baryonic matter and the ejection of plasma jets by black holes, particularly supermassive black holes.

### Star formation

The evolution of baryonic matter and light emission follows the cosmic history of formation of stars. Their rate of formation per unit comoving volume is illustrated in the figure below.

:::{figure}  ../../images/SFRD_2014ARA&A..52..415M.png
:name: fig:csfh
:align: center
:width: 80%

The cosmic star formation rate history. From {cite:p}`2014ARA&A..52..415M`.
:::

In this figure, the redshift is converted to cosmological age using a flat $\Lambda$CDM cosmology, with Hubble constant $H_0 = 70\,\mathrm{km},\mathrm{s}^{-1}\,\mathrm{Mpc}^{-1}$ and dark energy density $\Omega_\Lambda = 0.7$, i.e. with $\Omega_\mathrm{m} = 0.3$. The look-back time is the counterpart of the cosmic age, i.e. $t_{L}(z) = \frac{1}{H_0} -  t_\mathrm{age}(z) = \int_0^z \dd z' \left|\frac{\dd t}{\dd z'} \right|$, where 

$$
\begin{align}
\frac{\dd t}{\dd z} &= \left[\frac{\dd z}{\dd t}\right]^{-1} \nonumber \\
					&= -\left[\frac{1}{a^2} \frac{\dd a}{\dd t}\right]^{-1} \nonumber \\
					&= -\left[(1+z)H(z)\right]^{-1} 
\end{align}
$$
That is


$$			
\left|\frac{\dd t}{\dd z}\right| =  \frac{1}{H_0} \frac{1}{(1+z)\sqrt{\Omega_\Lambda + \Omega_\mathrm{m}  (1+z)^3}},
$$

with a negligible contribution from the energy density associated with the radiation, $\Omega_\mathrm{r}$. The evolution of the star formation rate, $\Psi$, determines the evolution of the fraction of the baryonic mass contained in stars and gas, as well as the enrichment of the interstellar medium in galaxies. For example, the mass density contained in stars, $\rho_\star$, can be calculated from the following conservation equation:
$$
\frac{\dd \rho_\star}{\dd t} = (1-R) \Psi
$$

Here $R$ is the "return fraction", i.e. the proportion of matter reinjected into the interstellar medium by stellar winds and explosions. The value of $R$ is estimated at $30-40\%$, depending on the initial distribution of stellar mass, called the initial mass function.

:::{figure}  ../../images/smd_2014ARA&A..52..415M.png
:name: fig:csmh
:align: center
:width: 80%

Cosmic evolution of the stellar mass density. From {cite:p}`2014ARA&A..52..415M`.
:::

The evolution of star formation in the universe has led to an enrichment of interstellar media in atoms heavier than carbon, known as metals in thermal astrophysics. This enrichment is due to nucleosynthesis in the first stars from primordial hydrogen and helium (see [pp chain](wiki:Proton–proton_chain) and [CNO cycle](wiki:CNO_cycle)). These first stars, known as Population III stars, contributed to the reionisation of their environment during their short lifetime of a few million years. The most massive stars (${>}\,8\,M_\odot$) exploded in supernovae and ejected metals that fuelled subsequent generations of stars, and so on up to the Sun, which belongs to Population I. Gas, molecules - such as the most abundant H$_2$ and CO - and dust - in the form of carbonaceous and amorphous silicate grains - continued to accumulate in the interstellar medium throughout the first three billion years of the universe until the cosmic peak of star formation around a redshift $z \sim 2$, a period known as the "cosmic noon". Since then, the universe has been populated mainly by long-lived Population I stars, typically $t_\odot \approx 10\,$Gyr for the Sun. Their average rate of formation has decreased as the reservoir of gas available in the interstellar medium has been depleted until today.


As with the mass of matter contained in stars today, the cumulative emission of nucleosynthesis processes is proportional to the integral of the cosmic star formation rate.


:::{exercise} Cosmic energy density of photons produced by nucleosynthesis
:label: exo:photons_nucl

1. Estimate the efficiency of conversion of matter into light, $\epsilon_\odot$, within stars similar to the Sun. Its bolometric luminosity is $L_\odot = 3.8 \times 10^{26}\,$W.

2. Discuss the efficiency of this light production compared with that of the pp chain ($4 p + 2 e^- \rightarrow\ ^{4}\mathrm{He}^{2+} + 2 \nu_e$), which releases $26.1\,$MeV of energy in the form of photons (and $0.6\,$MeV in the form of neutrino kinetic energy).

3. From the light-to-matter conversion efficiency in the sun and the star formation rate density, calculate the energy density in the field of photons emitted by all the stars in the universe.
:::

:::{solution} exo:photons_nucl

1. $$\begin{align}
\epsilon_\odot &= \frac{L_\odot t_\odot}{M_\odot c^2} \nonumber \\
& \approx 7 \times 10^{-4}
\end{align}$$

2. $$\epsilon_\mathrm{pp} \approx \frac{26.1}{4\times 938} \approx 7 \times 10^{-3}$$

The efficiency of matter-to-light conversion in the Sun is therefore only one tenth of the theoretical maximum efficiency. It should be noted that although the pp chain is dominant within the Sun, this does not mean that all its protons are involved in the fusion processes.

3. $$\begin{align}
\rho_{\gamma, \mathrm{nucl}} &= \epsilon_\odot c^2 \int \dd t \Psi(t) \nonumber \\
& \approx 7 \cdot 10^{-4} \times 10^{10} \times 0.05 M_\odot c^2 \,\mathrm{Mpc}^{-3}  \nonumber\\
& \approx 3.5\cdot 10^{5} \times 1.1\cdot 10^{66}/(3.1\cdot 10^{22})^3 \mathrm{\,eV\,m}^{-3}  \\
& \approx 13 \times 10^{3}\mathrm{\,eV\,m}^{-3}
\end{align}$$

For comparison, the energy density contained in CMB is twenty times greater, i.e. $\rho_{\gamma, \mathrm{CMB}} = 260 \times 10^3\mathrm{\,eV\,m}^{-3}$ (or $0.26\mathrm{\,eV\,cm}^{-3}$).
:::

### Accretion

Galaxies formed in a hierarchical fashion, first by the concentration of baryonic matter in their low-mass halos, then by merging with other galaxies in the cosmic web. The evolution of galaxies is accompanied by the growth of their central massive black hole. The mass of these black holes, $M_\bullet \approx 10^6 - 10^{10} M_\odot$, is about two thousandths of the stellar mass of the bulge of the host galaxy {cite:p}`2020ApJ...888...37D`. This relation illustrates the co-evolution of central black holes and their host galaxies. Many other correlations between observables support this link: for example the $M_\bullet - \sigma_\star$ relation between the black hole mass and the dispersion of stellar velocities within spheroids (elliptical galaxy or central bulge for a spiral galaxy). The rate of accretion of matter by massive black holes thus follows an evolution, $\Psi_\mathrm{accr}$, comparable to that of the star formation rate, with a density $2000-3000$ times lower.

:::{figure}  ../../images/accr_2014ARA&A..52..415M.png
:name: fig:csmh
:align: center
:width: 80%

The evolution of the star formation rate (black curve) and the accretion rate of massive black holes (coloured curves and bands). The accretion-rate estimates are multiplied by a factor of ${\sim}\,3000$ to bring them up to the scale of the star formation rate. From {cite:p}`2014ARA&A..52..415M`.
:::

Matter accretion around supermassive black holes, in particular around active galactic nuclei, is the second most important power-source for light emission after star formation. The energy released by accretion in the form of photons can be estimated using Soltan's argument {cite:p}`1982MNRAS.200..115S`. The energy of a test particle accreted by a black hole from the last marginally stable orbit is only a fraction of the energy of its rest mass. The rest can be released in the form of radiation. The radiative efficiency of the accretion process, $\epsilon_\mathrm{accr}$, is defined as the ratio of the radiated power to the rate of mass-energy deposition in the disc, measured by an observer at infinity. Taking into account the deceleration of the black hole's rotation by the accreted photons, Thorne calculates a radiative efficiency of $5.7\% < \epsilon_\mathrm{accr} < 30.8\%$ {cite:p}`1974ApJ...191..507T`.[^b]

[^b]: The upper bound of this range is lower than the 42% expected for a maximally rotating Kerr black hole. The difference with the value estimated by Thorne is due to the capture of photons.

:::{exercise} Cosmic energy density of photons from accretion
:label: exo:photons_accr

1. What is the fraction of mass energy that can be converted to radiation for a black hole accreting at the rate $\dot M$ for a radiative efficiency $\epsilon_\mathrm{accr}$?

2. Estimate the energy density of photons from matter accreted by massive black holes.
:::

:::{solution} exo:photons_accr
1. Let us consider for the exercise $\epsilon_\mathrm{accr} \approx 20\%$. The fraction of mass actually accreted by the black hole is $1-\epsilon_\mathrm{accr}$. The mass energy that can be converted into radiation is therefore proportional to $\frac{\epsilon_\mathrm{accr}}{1-\epsilon_\mathrm{accr}} \dot M$.

2. For $\psi_\mathrm{accr}(t) = f_\mathrm{accr} \psi(t)$ with $f_\mathrm{accr} = 1/3000$, the energy density of the photon field emitted by the accretion processes is
$$\begin{align}
\rho_{\gamma, \mathrm{accr}} &= \frac{\epsilon_\mathrm{accr}}{1-\epsilon_\mathrm{accr}} c^2 \int \dd t \Psi_\mathrm{accr}(t) \nonumber \\
	&=  f_\mathrm{accr} \frac{\epsilon_\mathrm{accr}/\epsilon_\odot}{1-\epsilon_\mathrm{accr}} \rho_{\gamma, \mathrm{nucl}} \nonumber \\
& \approx 1.5 \times 10^{3}\mathrm{\,eV\,m}^{-3}
\end{align}$$

The emission produced by accretion is not negligible, especially if we realise that only 1% of galaxies have an active nucleus {cite:p}`2010ApJ...723.1447H`.
:::

### Ejection

Around 10% of active galactic nuclei develop a jet on either side of the accretion disc {cite:p}`2019ARA&A..57..467B`. The presence of jets is deduced or observed in many astrophysical systems: collapse of a massive star leading to the formation of a long gamma-ray burst, binary of compact objects for a short gamma-ray burst, binary of a star and a white dwarf for a Nova, binary of a star and a compact object such as a black hole or a neutron star for a micro-quasar. Plasma ejection in the jets results from the conversion of electromagnetic energy at their base into kinetic energy at their termination. The kinetic energy of the jets can be estimated for some active galactic nuclei by the size of the radio cavities they form in the intracluster medium {cite:p}`2012ARA&A..50..455F`. Synthetic evolution models that attempt to reproduce these observations estimate that ${\sim}\,0.5\%$ of the mass energy associated with accretion is injected into the jets of active galactic nuclei {cite:p}`2008MNRAS.388.1011M`. However, the uncertainties surrounding the mechanisms of jet formation and the different accretion regimes mean that this ratio is merely a rough estimate of the blance between the kinetic energy and accreted energy.

The conversion of the Poynting flux (electromagnetic energy) into global plasma motion (kinetic energy) is accompanied by the acceleration of charged particles, for example by shock waves in the jets or at its boundary (shear), or by magnetic reconnection. Accelerated particles lose energy through conventional emission processes: synchrotron and inverse Compton for electrons and positrons, as well as production of pairs and pions for protons and nuclei. It is these radiative losses that produce the emission of jets from radio waves to gamma rays. The efficiency of converting kinetic energy into radiation is estimated at $10\%$ for jets of active galactic nuclei, gamma-ray bursts and microquasars.

:::{exercise} Cosmic energy density of photons from jets
:label: exo:photons_jet

Estimate the energy density of photons from jets emitted in the vicinity of massive black holes.
:::

:::{solution} exo:photons_jet
Using the ratio of jet kinetic energy to accreted mass energy of $0.5\%$, we obtain an energy conversion factor between accreted mass and photon emission by the jets $\eta_\mathrm{jet} \approx 0.05\%$ on cosmic scales. The energy density of photons radiated by the jets should then be of the order of

$$\begin{align}
\rho_{\gamma, \mathrm{accr}} &=\eta_\mathrm{jet} c^2 \int \dd t \Psi_\mathrm{accr}(t) \nonumber \\
	&=  f_\mathrm{accr} \frac{\eta_\mathrm{jet}}{\epsilon_\odot} \rho_{\gamma, \mathrm{nucl}} \nonumber \\
& \approx 3 \mathrm{\,eV\,m}^{-3}
\end{align}$$
:::

Now that we have estimated the energy densities associated with the photon fields emitted by the three major astrophysical processes, we can compare them with observations.


Multi-messenger emissions on cosmic scales
--------------------------------

### Energy density, surface brightness, flux density and luminosity

An observable directly related to the energy density of an isotropic photon field is the sky surface brightness, from which all the foregrounds have been subtracted. Following the notation of {cite}`1986rpa..book.....R`, the bolometric surface brightness or bolometric intensity, $I$, is defined as the energy passing through a surface $\dd A$ during a time $\dd t$ and from a solid angle $\dd \Omega$:
$$
\dd E = I \dd A \dd t \dd \Omega,
$$
with $[I] = \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}$.

The radiative energy density, $u$, in a volume $\dd V = c \dd t \dd A$ is such as $dE = u \dd V$, so that the average intensity integrated over the sphere is
$$
I = \frac{c}{4\pi} u
$$ 

:::{important}
The specific intensity, $I_\nu$, is the derivative of the bolometric intensity, $I$:
$$
I = \int \dd \nu\ I_{\nu}, \quad \mathrm{with\ } [I_{\nu}] =  \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{Hz}^{-1}
$$

Specific intensity is often represented in the form $\nu I_\nu$ as a function of $\ln \nu$, since the integral under the curve then gives the bolometric intensity:
$$\int \dd \ln \nu\ \nu I_{\nu} = \int \dd \nu\ I_{\nu} = I$$

Specific intensity has notable transformation properties. Indeed, it can be shown that $I_\nu / \nu^3$ is a Lorentz invariant. 
:::

:::{note}
The literature sometimes uses the notation $I_{\mathrm{dex}}$ with $[I_{\mathrm{dex}}] = \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{dex}$. With this notation, 
$$\int \dd \log_{10} \nu\ I_{\mathrm{dex}} = \int \dd \nu\ I_{\nu} = I$$
Note that $I_\mathrm{dex}$ differs by a factor $\nu \ln 10$ from $I_{\nu}$
:::

Following again {cite}`1986rpa..book.....R`, the energy density in a field of particles with momentum between $p$ and $p + \dd p$ depends on the number of particles per phase volume, $\dd \mathcal{N}/\dd^3 x \dd^3 p$ as

$$
u_\nu \dd \nu = h\nu  \frac{\dd \mathcal{N}}{\dd^3 x \dd^3 p} 4\pi p^2 \dd p
$$

$\dd \mathcal{N}/\dd^3 x \dd^3 p$ is invariant under a Lorentz transformation. Indeed $\dd \mathcal{N}$ is countable and thus invariant. Under a boost $(\beta, \gamma)$ along the x-axis from the comving frame (K') towards the observer's frame (K), one finds $\dd x = \gamma^{-1} \dd x'$ (length contraction) and $\dd p_x = \gamma (\dd p_{x'} + \beta \dd E') = \gamma \dd p_{x'}$ for particles with fixed energy (total momentum fixed between $p$ and $p + \dd p$). Thus $\dd^3 x \dd^3 p$ is invariant, *quod erat demonstrandum*.
 
 
One finds
$$
I_\nu \dd \nu = \frac{h}{c} (h\nu)^3  \frac{\dd \mathcal{N}}{\dd^3 x \dd^3 p} \dd \nu
$$

so that 

$$
I_\nu / \nu^3 = \mathrm{Lorentz\ invariant}
$$

:::{note}
Radio-to-optical astronomers often plot $\nu I_\nu$, while X-ray and higher-energy astronomers often consider $E^2 J(E) = \nu I_\nu$, where both are in units of power per unit area per unit solid angle. 

Similarly, the specific flux density from a point source, denoted as $S_\nu$ or $F_\nu$ with $[F_\nu] = \mathrm{W}\,\mathrm{m}^{-2}$, is represented as $\nu F_\nu = E^2 \frac{\dd N}{\dd E}$, where $\left[\frac{\dd N}{\dd E}\right] = \mathrm{m}^{-2}\,\mathrm{s}^{-1}\,\mathrm{eV}^{-1}$. The specific and bolometric luminosity are estimated from the flux and distance as $L_\nu = 4\pi D_L^2 F_\nu$ and $L = 4\pi D_L^2 F$.

The net flux received from a region covering a solid angle $\dd \Omega$ at zenith angle $\theta$ can be computed from the surface brightness of that region as
$$
F = \int \dd\Omega\ I \cos \theta 
$$ 

Note that if $I$ is isotropic, the net flux is zero as the energy crossing the surface $\dd A$ in the $+\vec{n}$ direction is the opposite of that from $-\vec{n}$ direction.
:::


### The spectrum of the universe


:::{figure}  ../../images/The_Fitted_MM_EGAL_Background_2023.png
:name: fig:mm_spectrum
:align: center
:width: 100%

The multi-messenger extragalactic spectrum. Adapted from this [page](https://zenodo.org/records/7842239).
:::

TBD: discussion


:::{exercise} Energy densities in the Milky Way
:label: exo:milky_way

The Galaxy can be seen as a disc of bolometric luminosity $1.5-2.0 \times 10^{10} \ L_\odot$, approximated by a cylinder of diameter $2R=25\,$kpc and height $h=300\,$pc, and a bulge of bolometric luminosity $0.5 \times 10^{10} \ L_\odot$, approximated as a bar or spheroid of diameter $3\,$kpc. The bolometric luminosity of the Sun is $L_\odot = 3.85 \times 10^{26}\,$W. 


1. Calculate the energy density of the photon field in the disc in eV$\,$m$^{-3}$.

2. The magnetic field of the Milky Way is inferred to range in $1-10\,\mu$G that is $(1-10)\times 10^{-10}\,$T. Estimate the magnetic energy density in the Milky Way.

3. From the local cosmic-ray spectrum presented in [](#fig:cr_spectrum), estimate the energy density of cosmic rays in the Milky Way.

:::{figure}  ../../images/The_CR_Spectrum_2023.png
:name: fig:cr_spectrum
:align: center
:width: 60%

The local cosmic-ray spectrum. Components from the Milky Way dominate the brightness of the sky at least up to the knee structure at $E \approx 3\,$PeV. From this [page](https://zenodo.org/records/7948212).
:::

:::

:::{solution} exo:milky_way
1. We assume the photon field to be isotropic in the disc of Milky Way. Then, we can estimate the photon density as:

\begin{align}
u_\mathrm{O-IR} &= \frac{4\pi}{c} I_\mathrm{O-IR} \nonumber \\
		 &= \frac{4\pi}{c} \frac{F_\mathrm{O-IR}}{\int \dd \Omega \cos \theta}
\end{align}

where $F_\mathrm{O-IR}$ is the net flux emitted from one side of the disc and $\int \dd \Omega \cos \theta = 2\pi \int_0^1 \cos \theta \dd  \cos \theta = \pi$. The total flux emitted by the two sides of the disc is $2F_\mathrm{O-IR} = \frac{L_\mathrm{O-IR}}{\pi R^2}$, so that

\begin{align}
u_\mathrm{O-IR} &= \frac{4\pi}{c} I_\mathrm{O-IR} \\
		 &= \frac{2}{c} \frac{L_\mathrm{O-IR}}{\pi R^2}
 		 &= \frac{2}{c} \frac{L_\mathrm{O-IR}}{\pi R^2}
 		 &\approx (0.5-0.7) \times 10^{6} \,\mathrm{eV\,m}^{-3},
\end{align}
i.e. two-to-three times the energy density of the CMB.

2. 
\begin{align}
u_B & = \frac{B^2}{2\mu_0} \\
 & \approx \frac{(1-100) \cdot 10^{-20} \times 6.2 \cdot 10^{18}}{2 \times 4\pi \times 10^{-7}} \,\mathrm{eV\,m}^{-3} \\
 & \approx (0.02-2) \times 10^{6} \,\mathrm{eV\,m}^{-3},
\end{align}

3. The local cosmic-ray intensity can be approximated as $J(E) = J_0 \left(\frac{E}{E_0} \right)^{-p} = 2 \times 10^4\, \mathrm{GeV^{-1}}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}\,\mathrm{sr}^{-1}\times \left(\frac{E}{1\,\mathrm{GeV}} \right)^{-2.7}$.

Considering the cosmic-ray velocity to be near the speed of light (which is wrong near $1\,$GeV), the energy density of cosmic rays in the Milky Way above $E_0 = 1\,\mathrm{GeV} \approx m_p c^2$ can be approximated by

\begin{align}
u_\mathrm{CR} &= \frac{4\pi}{c} \int_{E_0} \dd E\ E J(E) \\
			 &= \frac{4\pi}{c} \frac{E_0^2 J_0}{p-2} \\
 			 &\approx 1.2 \times 10^{6} \,\mathrm{eV\,m}^{-3}
\end{align}

Interestingly, all three components are close to equipartition.
:::

