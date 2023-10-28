---
# Math frontmatter:
math:
  # Note the 'single quotes'
  '\dd': '\mathrm{d}'
---


Astrophysical emissions on cosmic scales
=============================================


A homogeneous and isotropic universe?
--------------------------------

The cosmological models that we have discussed postulate that the universe is homogeneous and isotropic on large scales, i.e. typical distances greater than 100 Mpc. Below this characteristic scale, the galaxies observed in large optical surveys are distributed according to the cosmic web. The large structures that weave this web formed as a result of the growth of the fluctuations in the CMB. Due to the properties of gravitation, an initially ellipsoidal overdensity collapses preferentially along its smallest axis, resulting in a sheet (so called Zel'dovich pancake). These sheets can collapse in the form of filaments, which themselves converge towards galaxy clusters. The areas not populated by the cosmic web constitute the cosmic voids, which occupy most of space.

### Distance from local large-scale structures

These structures arrange themselves in a network resembling that of soap bubbles. A simplified crystallographic representation is given below, with $l$ the characteristic cell size and $w$ the typical diameter of clusters or the cross-section of filaments. Cosmological simulations suggest a void occupancy rate of the order of $(1-w/l)³ = 75\%$ (see exercise below). Knowing that the characteristic radius of the clusters we observe is $w \approx 1\,$Mpc, we deduce a typical cell size of the order of $l \approx 10\,$Mpc.


```{figure} ../images/bubble_network_2019GReGr..51....9F_ 2022A&A...662A..87O.jpg
:name: fig:bubble_network
:align: center
:width: 100%

Network of soap bubbles and cubic model illustrating the structure of the cosmic web. On the right-hand side, the nodes in orange correspond to the clusters, the sheets and filaments are in sky blue and the voids in dark blue. Images taken from {cite}`2019GReGr..51....9F` and {cite}`2022A&A...662A..87O`.


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

These four types of structure are visible in the disitribution of nearby galaxies. Our galaxy, its neighbour Andromeda at $0.75\,$Mpc and their satellites, such as the Large Magellanic Cloud at $50\,$kpc, form the Local Group. As illustrated in 
[](#fig:council-giants), the Local Group is at the heart of the Local Sheet. This sheet is a planar structure with a diameter of ${\sim}\,10\,$Mpc, delimiting one side of the Local Void.


```{figure}  ../images/mccall_fig3.pdf
:name: fig:council-giants
:align: center
:width: 70%

Local Sheet galaxies ($R \approx 5\,$Mpc) surrounding the local group ($R \approx 0.5\,$ Mpc). From {cite}`2014MNRAS.440..405M`.
```

Opposite the galaxy NGC 253, about $16\,$Mpc from the Milky Way, is the Virgo cluster of galaxies, which has a rugby ball structure, as can be seen below. Galaxy clusters can contain several thousand galaxies.

```{figure}  ../images/virgo_2007ApJ...655..144M.jpg
:name: fig:virgo
:align: center
:width: 70%

Spatial distribution of galaxies in the Virgo cluster with well constrained distances in  supergalactic coordinates (the supergalactic plane is an historical structure almost identical to the Local Sheet, with a tilt of 8°). The brightest galaxies are shown in red. From {cite}`2007ApJ...655..144M`.
```

Clusters of galaxies such as Virgo are connected to the cosmic web by filaments of galaxies, whose position in the celestial plane and radial velocity projection can be inferred by spectroscopy, as illustrated below.

```{figure}  ../images/virgo_filaments_2022ApJS..259...43C
:name: fig:filaments
:align: center
:width: 100%

The filaments around the Virgo cluster. The distribution of galaxies in the sky is shown in equatorial coordinates (right ascension, R.A., and declination, Dec, in degrees). From {cite}`2022ApJS..259...43C`.
```

On an even larger scale, typically $100\,$Mpc, the clusters are grouped into superclusters such as Laniakea, which hosts us.

```{figure}  ../images/laniakea_2014Natur.513...71T.jpg
:name: fig:supercluster
:align: center
:width: 100%

The local superclusters. Velocity streamlines of our supercluster, Laniakea, are shown in white. From {cite}`2014Natur.513...71T`.
```

### Mass of local large-scale structures

Not only can astronomers measure the position of galaxies in the sky, they can also measure the radial component of their velocity as well as their distance from the stars that calibrate the cosmic distance ladder. The velocity field of galaxies can thus be used to constrain the gravitational field of Laniakea or its companion supercluster Perseus-Pisces. The mass of the Laniakea supercluster is estimated at ${\sim}\,10^{17}\, M_\odot$ {cite:p}`2014Natur.513...71T` [^a]. On a smaller scale, the mass of the Virgo cluster is estimated at ${\sim}\,10^{14}\, M_\odot$ {cite:p}`2016A&A...596A.101P`. Such dynamical arguments also yield an estimate of the mass of the Local Group of galaxies at ${\sim}\,3 \times 10^{12}\, M_\odot$. The Local Group dynamical mass is dominated by that of the Milky Way, $(1. 2 \pm 0.2) 10^{12}\, M_\odot$ and Andromeda, $(1.8 \pm 0.5) 10^{12}\, M_\odot$ {cite:p}`2022ApJ...928L...5B`.


[^a]: The sun has a mass measured with better than $10^{-4}$ accuracy at  $M_\odot = 1.9885 \times 10^{30}\,$kg.


These masses are deduced using dynamical arguments such as Viriel's theorem (|kinetic energy| = |potential energy|/2 for a system at equilibrium) or using the projected trajectories of the tracers. Using stars as tracers, we estimate the mass of the central black hole of the Milky Way, Sgr A*, at $(4.15 \pm 0.01) \times 10^{6}\, M_\odot$ {cite:p}`2019A&A...625L..10G` (see [](#fig:S2-trajectory) ). The latter has a small contribution to the mass of our galaxy compared with the stars that make it up $(6 \pm 1)  \times 10^{10}\, M_\odot$ {cite:p}`2015ApJ...806...96L`. The mass of the Milky Way contained in the stars (and dust) is itself about 20 times less than its dynamic mass.

```{figure}  ../images/S2_orbit.jpg
:name: fig:S2-trajectory
:align: center
:width: 100%

The 16-year orbit of the star S2 around the massive black hole Sgr A*, which has also been followed spectroscopically for 27 years. From {cite}`2019A&A...625L..10G`.
```

The mass deficit observed in the Milky Way is also inferred at the level of galaxy populations. The stellar mass of each galaxy can be estimated using near-infrared observations. At these wavelengths (around $1-3\,$µm), the emission from medium-sized stars like the Sun is high compared with that from dust, which emits mainly at wavelengths greater than $5\,$µm, and from more massive and younger stars, which emit mainly in the UV and blue band.


:::{exercise} Mass in stars
:label: exo:stellar_mass

Assuming that the mass (or associated luminosity) follows a distribution law according to a Schechter function, 
$$f(M_\star) \dd M_\star= n_\star \left(\frac{M_\star}{M_0} \right)^{-\alpha} \exp\left(-\frac{M_\star}{M_0} \right) \dd M_\star,
$$
calculate the stellar-mass energy density using [](#fig:stellar_mass).

```{figure}  ../images/stellar_mass_fun_2022MNRAS.513..439D.jpg
:name: fig:stellar_mass
:align: center
:width: 100%

The stellar mass function of the galaxies in the local Universe ($z<0.1$). From  {cite}`2022MNRAS.513..439D`.
```

:::

:::{solution} exo:stellar_mass

The first panel represents the function $g(M_\star)$ such as $\int g(M_\star) \dd \log_{10}M_\star = 1/V$, where $V$ is the considered volume. Thus $f(M_\star) = g(M_\star)/(\ln(10)M_\star)$.

From the first panel, we estimate by eye a cut-off at $M_0 \approx 2 \times 10^{11}
\,M_\odot$ where the density is $\ln(10) M_0 n_{\star}/e \approx 3  \times  10^{-4}\,$Mpc$^{-3}$dex$^{-1}$. We find $n_{\star} M_0 \approx 4 \times 10^{-4} \,$Mpc$^{-3}$. The index is similarly estimated at $\alpha=1.5$.

The stellar mass energy density is then
$$
\begin{align}
\int f(M_\star) M_\star c^2 \dd M_\star &= n_\star M_0 \times M_0  c^2 \int \dd x \, x^{1-\alpha} \exp(-x) dx \nonumber\\
							&=\Gamma(2-\alpha) \times n_\star M_0 \times M_0  c^2 \nonumber\\					
							&\approx \sqrt{\pi} \times 4 \cdot 10^{-4} \times 2 \cdot 10^{11} \times  1.1 \cdot 10^{66}/(3.1 \cdot 10^{22})^3\,\mathrm{eV\,m}^{-3} \nonumber\\
														&\approx 5 \times 10^{6}\,\mathrm{eV\,m}^{-3} 
\end{align}

Estimation using the exact form of the mass distribution function gives a stellar matter density up to $z < 0. 1$  or $D_L < 500\,$Mpc of $\rho_{\star, 0}= (2.97 \pm 0.04) \times 10^8 \,h_{70}\, M_\odot \, \mathrm{Mpc}^{-3}$, where $h_{70} = H_0 / (70\,$km$\,$s$^{-1}\,$Mpc$^{-1})$. This corresponds to an energy density twice larger than we estimated, i.e. $\rho_{\star, 0} \approx (11.0 \pm 0.1) \, h_{70} \times 10^{6}\,\mathrm{eV\,m}^{-3}$

:::


:::{note} $M_\odot$ per Mpc$^{3}$ and eV per m$^3$

The rest-mass energy of the sum is energy $M_\odot c^2 \approx 1.8\times 10^{47} \, \mathrm{J} \approx 1.1\times 10^{66}\,\mathrm{eV}$. The typical distance between neighboring galaxies is $1\, \mathrm{Mpc} \approx 3.1 \times 10^{22}\, \mathrm{m}$. The good  match between powers of ten makes it fairly easy to convert stellar mass density into energy density.

:::


### Cosmic energy inventory

For an energy density today equal to the critical density $\rho_{c,0} = \frac{3 H_0  c^2}{8ⲡG} = 1.36 \times 10^{11}\, h_{70}\, M_\odot\,\mathrm{Mpc}^{-3} \approx 5.1\, h_{70}\,$GeV$\,$m$^{-3}$, we can see that only two thousandths of the universe's energy budget is made up of stars. A detailed breakdown of the different energy budgets of the universe is shown below.

```{figure}  ../images/cosmic_inventory.png
:name: fig:cosmic_inventory
:align: center
:width: 100%

The cosmic energy inventory of {cite}`2004ApJ...616..643F`. Adapted from this [page](https://www2.mpia-hd.mpg.de/home/poessel/UT2012/).
```


:::{important}
Most of what we know about the universe comes from  four messengers: photons, neutrinos, cosmic rays and gravitational waves. As shown in  [](#fig:cosmic_inventory), the energy density associated with these tracers is only a few parts per million. Despite this, estimates of the amount of baryonic matter from radiation are increasingly precise. Of particular note is the potential resolution of a long-standing problem, the location of the missing half of the universe's baryons, which could be found in the warm/hot intergalactic plasma that makes up the cosmic web (see {cite}`2021NatAs...5..852D`).
:::



Cosmic-scale engines behind astrophysical emissions
--------------------------------

The processes responsible for most astrophysical emissions are star formation, the accretion of baryonic matter and the ejection of plasma jets by black holes, particularly supermassive black holes.

### Star formation



### Accretion



### Ejection
