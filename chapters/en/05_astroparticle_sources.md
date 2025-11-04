---
short_title: Jetted and non-jetted astroparticle sources
authors:
  - jbiteau
keywords: jet
---

Jetted and non-jetted astroparticle sources in the universe
=============================================


Electromagnetic emissions on cosmic scales
--------------------------------

### Energy density, surface brightness, flux density and luminosity

An observable directly related to the energy density of an isotropic field of relativistic particles is the sky surface 
brightness. Following the notation of {cite}`1986rpa..book.....R`, the bolometric surface brightness or bolometric 
intensity, $I$, is defined as the energy passing through a surface $\dd A$ during a time $\dd t$ and coming from a 
solid angle $\dd \Omega$:
$$
\dd E = I \dd A \dd t \dd \Omega,
$$
with $[I] = \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}$.

The energy density of the field of relativistic particles, $\varepsilon$, in a volume $\dd V = c \dd t \dd A$ is 
such as $dE = \varepsilon \dd V$, so that the average intensity integrated over the sphere is
$$
I = \frac{c}{4\pi} \varepsilon
$$ 

:::{important}
The specific intensity, $I_\nu$, is the derivative of the bolometric intensity, $I$:

$$
I = \int \dd \nu\ I_{\nu}, \quad \mathrm{with\ } [I_{\nu}] =  \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{Hz}^{-1}
$$

Specific intensity is often represented in the form $\nu I_\nu$ as a function of $\ln \nu$, since the integral under 
the curve then gives the bolometric intensity:
$$\int \dd \ln \nu\ \nu I_{\nu} = \int \dd \nu\ I_{\nu} = I$$

Radio-to-optical astronomers often plot $\nu I_\nu$, while X-ray and higher-energy astronomers often consider 
$E^2 J(E) = \nu I_\nu$, where both quantities are in units of power per unit area per unit solid angle. The 
differential particle intensity, $J(E)$, where "differential" means "per unit energy", is thus in units of
$\#\, \mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{s}^{-1}\,\mathrm{eV}^{-1}$ with $\#$ indicating a number of particles.

Similarly, the specific flux density from a point source, denoted as $S_\nu$ or $F_\nu$ with
$[F_\nu] = \mathrm{W}\,\mathrm{m}^{-2}$, is represented as $\nu F_\nu = E^2 \frac{\dd N}{\dd E}$, where
$\frac{\dd N}{\dd E}$ is the differential particle flux in units of
$\mathrm{m}^{-2}\,\mathrm{s}^{-1}\,\mathrm{eV}^{-1}$. Note that $\frac{\dd N}{\dd E}$ should formally be written as
$\frac{\dd N}{\dd E \dd A \dd t}$. In practice the surface and time differentiation are omitted in the standard
notation $\frac{\dd N}{\dd E}$ found in the litterature. 

The specific and bolometric luminosities are estimated from the flux, $F_\nu$, and luminosity distance, $D_L$ as 
$L_\nu = 4\pi D_L^2 F_\nu$ and $L = 4\pi D_L^2 F$.

The net flux emitted by a region over a solid angle $\dd \Omega$ at zenith angle $\theta$ can be computed from 
the surface brightness of that region as
$$
F = \int \dd\Omega\ I \cos \theta 
$$ 

Note that if $I$ is isotropic, the total net flux is zero as the energy crossing the surface $\dd A$ in the $+\vec{n}$ 
direction is the opposite of that from $-\vec{n}$ direction.


:::

:::{note}
The literature sometimes uses the notation $I_{\mathrm{dex}}$ with
$[I_{\mathrm{dex}}] = \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{dex}^{-1}$. With this notation, 
$$\int \dd \log_{10}(\nu)\ I_{\mathrm{dex}} = \int \dd \nu\ I_{\nu} = I$$
As $\log_{10}(x) = \ln(x)/\ln(10)$, one can note that $I_\mathrm{dex}$ differs by a factor $\nu \ln 10$ from $I_{\nu}$
:::

Following again {cite}`1986rpa..book.....R`, the energy density of a field of particles with momentum between $p$ and 
$p + \dd p$ depends on the number of particles per phase volume, $\dd \mathcal{N}/\dd^3 x \dd^3 p$ as

$$
\varepsilon_\nu \dd \nu = h\nu  \frac{\dd \mathcal{N}}{\dd^3 x \dd^3 p} 4\pi p^2 \dd p
$$

$\dd \mathcal{N}/\dd^3 x \dd^3 p$ is invariant under a Lorentz transformation. Indeed $\dd \mathcal{N}$ is countable 
and thus invariant. Under a boost $(\beta, \gamma)$ along the x-axis from the comoving frame (K') towards the 
observer's frame (K), one finds $\dd x = \gamma^{-1} \dd x'$ (length contraction) and $\dd p_x = \gamma (\dd p_{x'} + \beta \dd E') = \gamma \dd p_{x}'$ for particles with fixed energy (total momentum fixed between $p$ and $p + \dd p$). Thus $\dd^3 x \dd^3 p$ is invariant, *quod erat demonstrandum*.
 
 
One finds
$$
I_\nu \dd \nu = \frac{h}{c} (h\nu)^3  \frac{\dd \mathcal{N}}{\dd^3 x \dd^3 p} \dd \nu
$$

so that 

$$
I_\nu / \nu^3 \equiv \mathrm{Lorentz\ invariant}
$$


### The multi-wavelength spectrum of the universe


:::{figure}  ../../images/The_Fitted_MWL_EGAL_Background_2025.png
:name: fig:mm_spectrum
:align: center
:width: 100%

The multi-messenger extragalactic spectrum. Adapted from this [page](https://zenodo.org/records/7842239).
:::

The broadband emission from all galaxy populations (and from sources within these galaxies) is responsible for the 
spectrum of the universe shown in [](#fig:mm_spectrum). In particular, electromagnetic radiations include the cosmic 
radio background (CRB) from both active and star-forming galaxies, the cosmic infrared and optical backgrounds (CIB 
and COB) mostly from nucleosynthesis and dust emission in star-forming galaxies, the cosmic X-ray background (CXB) from 
active galaxies and 
the cosmic gamma-ray background (CGB) from jetted active galaxies. The differential measurements of these cosmic 
backgrounds are of fundamental value: they reflect our knowledge of the distribution of light emitted by star 
formation, accretion and ejection integrated since the formation of the first astrophysical sources. Although these 
emissions are only a negligible part of the cosmic energy inventory, they provide us with a cosmological consistency 
test that is essential for understanding the content and evolution of the post-recombination universe {cite:p}`2004ApJ...616..643F`. 

The values indicated by vertical text in [](#fig:mm_spectrum) correspond to the energy density of each component, i.e.
the integral of the specific intensity multiplied by $4\pi/c$. In particular, it can be verified that the 
expected energy density from the nucleosynthesis and accretion processes calculated in the previous chapter, i.e.
${\sim}\,(13+1.5) \times 10^3\,\mathrm{eV}\,\mathrm{m^{-3}}$, is found nearly in its entirety in the COB and CIB. The 
energy density from ejection processes around supermassive black holes,  expected at
${\sim}\,3 \,\mathrm{eV}\,\mathrm{m^{-3}}$, is found in the CGB.

The measurements shown in [](#fig:mm_spectrum) also quantify the degree of darkness of the night sky once the 
foregrounds are subtracted. It is the history of their emission that provides the solution to the Olbers paradox. 
The present intensity of these backgrounds determines the darkness (or rather grayness) of the night sky, once all 
foregrounds (Solar System, Milky Way) have been removed. We can understand the extragalactic backgrounds at all 
electromagnetic wavelengths, the so-called extragalactic background light, using synthetic models of galaxy populations.
Some unknowns in the extragalactic background light, including tensions between measurements, are nonetheless still 
the subject of active research {cite:p}`2025arXiv250917954B`.

Light emission is fundamentally the result of heating, acceleration and decay of matter. We will explore in the next 
section the knowledge established with photons, in particular through multi-wavelength observations of gamma-ray 
sources. We will also explore in the following lessons to which extent this multi-wavelength knowledge allows us 
to understand extragalactic backgrounds observed today with other messengers, in particular the extragalactic 
neutrino background (ENB) between $30\,$TeV and $3\,$PeV and the extragalactic cosmic-ray background (ECRB) between 
$200\,$PeV and $200\,$EeV.



Electromagnetic emission of non-thermal sources
----------------------------------
### Multi-wavelength astronomy

The development of radio astronomy around the Second World War led to the emergence of multi-wavelength astronomy as 
a powerful tool for understanding the Milky Way and extragalactic sources. Karl Jansky first used this approach for 
Galactic observations in the 1930s, and from the 1960s onwards, Martin Schmidt and others employed it to study the 
first active galactic nuclei, known as quasars at the time. The subsequent emergence of X-ray and gamma-ray 
astronomy in the 1970s and 1990s, respectively, has led to our current understanding of non-thermal emitters — 
astrophysical sources that emit radiation beyond the optical and infrared spectrum.

[](#fig:MWL_SkyMap) provides a multi-wavelength view of the entire sky in Galactic coordinates. In this spherical 
coordinate system, the Galactic centre is in the middle of the map and the Galactic plane 
separates the northern and southern Galactic hemispheres. Note that the skymaps are shown as a function of decreasing 
Galactic longitude, ranging from $+180^\circ$ on the left to $-180^\circ$ on the right. This is the opposite of how 
we represent the Earth (i.e. with increasing longitude from left to right), because we are observing the sphere from 
within when we look at the sky.

:::{figure}  ../../images/multiwavelength_sky.jpg
:name: fig:MWL_SkyMap
:align: center
:width: 50%

Multiwavelength view of the sky in Galactic coordinates. From this [page](https://imagine.gsfc.nasa.gov/science/toolbox/multiwavelength1.html).

:::

Much of the radio emission shown in [](#fig:MWL_SkyMap) originates from high-energy electrons and positrons radiating 
within the magnetic field 
of the Milky Way. Shock waves in supernova remnants also produce intense radio emissions near these sources. 
Most of the infrared emission comes from relatively cool stars located in the disc and bulge of the Milky Way. 
Interstellar dust is relatively transparent at these wavelengths. At visible wavelengths (between 0.4 and 0.6 
microns), strong absorption by gas and dust clouds limits the depth of observations. As a consequence, the visible 
light along the Galactic plane mainly originates from stars located a few kiloparsecs from the Sun. The composite 
X-ray image is reconstructed from bands centred at 0.25, 0.75 and 1.5 keV (red, green and blue, respectively). The 
hot, shocked gas in the Milky Way emits low-energy X-rays (also known as 'soft X-rays'). The interstellar medium 
strongly 
absorbs soft X-rays, enabling us to perceive cold clouds of interstellar gas as shadows against the X-ray emission 
background. The black areas indicate gaps in the survey. 

The gamma-ray image includes all photons with energies above 1 GeV. At these high energies, much of the gamma-ray 
emission along the Galactic plane originates from interactions of cosmic rays with hydrogen and helium nuclei in 
the interstellar medium. Bright, point-like sources are observed along the Galactic plane, such as the Vela, 
Geminga and Crab pulsars, which are located at longitudes of about $-95^\circ$, $-165^\circ$ and $-175^\circ$, 
respectively. Point-like sources are also found outside the Galactic plane, primarily in the form of jetted active 
galactic nuclei. A more detailed introduction to the observations in each band, from which the previous two 
paragraphs are adapted, can be found on this [page](https://asd.gsfc.nasa.gov/archive/mwmw/mmw_images.html).


Zooming in on a square measuring approximately 0.1° centred on Galactic coordinates of l = -175.44° and b = -5.78° 
reveals in [](#fig:MWL_Crab) the emission surrounding the Crab pulsar. This extended emission is known as the Crab 
Nebula. The Crab Nebula is the result of a core-collapse supernova that exploded in 1054 AD. The pulsar at the 
heart of the nebula has a period of about 33 milliseconds. The rotation of the neutron star powers the radiation 
observed in the pulsar wind nebula.

:::{figure}  ../../images/Crab_Nebula_in_Multiple_Wavelengths_2.png
:name: fig:MWL_Crab
:align: center
:width: 80%

Multiwavelength view of the Crab Nebula. From this [page](https://commons.wikimedia.org/wiki/File:Crab_Nebula_in_Multiple_Wavelengths_2.png).

:::

In [](#fig:MWL_Crab), radio observations depict the pulsar wind nebula in red and the emission of free electrons in 
green. The blue-white region in the infrared image corresponds to electrons trapped in the magnetic field, 
while the red filaments reveal the rest of the star's original outer layers. The network of filaments is 
clearly visible in the optical image, surrounding the bluish core of the pulsar wind nebula. The Crab Nebula extends 
slightly further in the ultraviolet than in X-rays. This is because the electrons responsible for UV emission lose 
their energy more slowly than those emitting at higher energies. The X-ray image reveals impressive structures that 
trace the magnetic field surrounding the pulsar, including a compact object, two concentric tori, and jets on both 
sides. A more extensive introduction to Crab Nebula can be found on this
[page](https://chandra.harvard.edu/graphics/resources/handouts/lithos/crab_litho.pdf) and that
[page](https://imagine.gsfc.nasa.gov/science/toolbox/multiwavelength2.html).

The angular resolution of gamma-ray observatories is barely sufficient to resolve the Crab pulsar wind nebula, which 
therefore appears almost as a point-like source. Interestingly, a slight extension can nonetheless be measured 
beyond the extent of the point spread function, ranging from 0.035° ± 0.003° above 1 GeV to 0.014° ± 0.005° above 10 
TeV {cite:p}`2024A&A...686A.308A`. The Crab pulsar wind nebula therefore presents a complex morphology that depends 
on energy, tracing the structure of the magnetic field and the injection of leptons in the pulsar's environment.

### Non-thermal sources

#### Bestiary of sources

Photons detected in the radio to PeV range offer a significant advantage over other astroparticles, such as 
neutrinos and charged cosmic rays. Their larger interaction cross sections make them easier to detect than neutrinos.
Furthermore, like neutrinos, photons propagate along geodesics (i.e. in a straight line, to first approximation), 
whereas charged cosmic rays are deflected by the magnetic fields they pass through.

Of all the gamma-ray surveys performed to date, the most complete is that obtained by the Fermi-LAT satellite in the 
GeV energy range. This map is shown in Galactic coordinates in [](fig:lat_skymap).

:::{figure}  ../../images/Fermi_5_year_scaled.jpg
:name: fig:lat_skymap
:align: center
:width: 100%

Skymap in Galactic coordinates of the excess of gamma-rays with energies above $1\,$GeV from 5 years of observations with Fermi-LAT. From this [page](https://svs.gsfc.nasa.gov/11342).
:::

Most of the ${\sim}\,7000$ sources observed at GeV energies are located outside the Galactic Plane. They are mainly 
jetted active 
galactic nuclei, the brightest of which are "blazars", whose axis of emission is aligned with the line of sight. 
Other jetted active galactic nuclei with a "misaligned" jet are called radio galaxies. Approximately a dozen 
starburst galaxies have also been detected in the extragalactic universe observed in gamma rays. These galaxies 
exhibit a higher rate of star formation per unit of stellar mass than our own galaxy. With respect to the Milky Way, 
starburst galaxies produce 
more short-lived, massive stars that end their lives in supernovae. Several hundred gamma-ray bursts have also been 
detected in the extragalactic gamma-ray sky, primarily long gamma-ray bursts resulting from the explosions of massive 
stars up to a redshift of $z > 4$. 

Diffuse emissions from our galaxy can be seen firstly along the Galactic plane and secondly as a fainter peanut-shaped 
emissions on either side of the Galactic centre: the Fermi bubbles. These bubbles have a similar morphology to those 
observed in microwaves by the WMAP and Planck satellites and in X-rays by the eROSITA satellite. The mainstream 
explanation for the Fermi bubbles is the past acceleration of cosmic rays in the inner regions of the Milky Way, 
followed by the diffusion of these charged particles in the Galactic magnetic field.

Finally, our galaxy is populated by a myriad of stellar-sized sources. Hollow shells are the remains of supernovae 
(of which there are two types: core-collapse and thermonuclear, also known as SN1a). Core-collapse supernovae can 
leave a highly magnetised neutron star in their core after their explosion, which is known as a pulsar. The winds 
from these pulsars, known as pulsar wind nebulae, fill the space left by the supernova explosion and accelerate 
electrons and positrons, which re-radiate gamma rays. In more advanced stages of their lives, the diffusion of 
particles around the pulsar can even lead to extended emission over several degrees, known as TeV halos. Our 
galaxy also contains numerous gamma-ray sources arising from binary systems: novae, X-ray binaries and 
even microquasars, which are the stellar-scale analogues of the jetted active galactic nuclei.

Static images, such as those presented in [](#fig:MWL_SkyMap) and [](#fig:MWL_Crab), are particularly useful for 
astronomical sources that are periodic or constant on human timescales. For such sources, observations at 
different wavelengths made at different times can be combined a posteriori without altering the physical picture. 
However, this does not apply to persistent variable sources, such as a jetted active galactic nucleus, the 
flux of which varies erratically on timescales ranging from decades to minutes, nor to transient sources, such as 
gamma-ray 
bursts and novae, which appear and disappear within seconds to days after explosions. 

Fortunately, since the early 
2020s, we have had access to a network of multi-wavelength observatories covering nearly 22 orders of magnitude in 
energy, from a few tens of MHz to energies on the order of PeV, including some with spectroscopic or polarimetric 
capabilities. Simultaneous observation campaigns are scheduled and 
bursts can be followed up thanks to alerts transmitted worldwide within minutes. These alerts are also issued by 
multi-messenger facilities, which have been crucial since the mid-2010s as we will discuss in the next lesson.


#### Relativistic beaming 

The most variable sources known to date often display (or are inferred to host) jets of plasmas.

The existence of emission zones with a bulk velocity (relative to the central compact object) approaching the speed 
of light can be illustrated by the apparent motion of plasma region (often called "blobs") in such 
astrophysical jets.  The apparent velocity of such plasma blobs can exceed the speed of light, an effect that 
can be explained by purely geometrical arguments based on classical physics, as [](#exo:superluminal) illustrates.

:::{exercise} Superluminal motion
:label: exo:superluminal

The blob of plasma imaged in radio waves, farthest to the right in [](#fig:superluminal), appears to travel a distance 
of ${\sim}\,30\,$ light-years over a period of ${\sim}\,7\,$ years.

1. Give an expression of the apparent speed as a function of the physical speed of the plasma blob along the jet in the observer's frame and of the angle between the jet and the line of sight.

2. Deduce a constraint on the Lorentz factor of the plasma blob in the observer's frame.


:::{figure}  ../../images/3c279_320.jpg
:name: fig:superluminal
:align: center
:width: 60%

Radio emission from the jet of the active galactic nucleus 3C 279. From this [page](http://user.astro.columbia.edu/~jules/UN2002/superluminal.html).

:::


:::{solution} exo:superluminal
:class: dropdown

1. Following the notations in [figure %s](#fig:superluminal_sol), the apparent velocity, $v_\mathrm{app}$, of the 
   plasma blob is given by

$$
\begin{align}
v_\mathrm{app} &= \frac{L}{t_2-t_1} \\
			 &= \frac{L}{t_{i,2}-t_{i,1} - \frac{d_1-d_2}{c}} \\
 			 &= \frac{H\sin\theta}{H/v - H\cos\theta/c} \\
 			 &= \frac{v\sin\theta}{1 - \frac{v}{c}\cos\theta},
\end{align}
$$
where $v$ is the physical speed of the plasma blob along the jet in the observer's frame.

2. Using $\beta = \frac{v}{c}$ and $t = \tan(\theta/2)$, together with standard trigonometry gives:
$$
v_\mathrm{app} = \frac{2t\beta }{1+t^2 - (1-t^2)\beta}
$$
So that after a bit of algebra, an apparent speed that is equal to a fraction $k$ of the speed of light reads
$$
v_\mathrm{app} = kc  \Leftrightarrow \Big[(1+\beta)t - \beta/k\Big]^2 = (\beta/k - 1/\Gamma) \times (\beta/k + 1/\Gamma),
$$
where $\Gamma = 1/\sqrt{1-\beta^2}$ is the Lorentz factor of the plasma blob.

The right-hand-side equation has a solution if and only if $\beta/k - 1/\Gamma \geq 0$ i.e. $k \leq \Gamma\beta$. As 
$k = v_\mathrm{app}/c$ and $\beta < 1$, one gets $\Gamma > v_\mathrm{app}/c$ i.e. a Lorentz factor larger than $4$ 
for the jet of the active galactic nucleus 3C 279.

:::{figure}  ../../images/superluminal_calc.png
:name: fig:superluminal_sol
:align: center
:width: 30%

Schematic modeling of the radio knot.
:::

The relativistic motion of the plasma blobs in jetted astrophysical sources results in anisotropic emission. The 
motion also increases the energy of the photons and the intensity of the radiation as the region moves towards the observer. 
The textbook derivation of this relativistic Doppler effect is based on velocity transformations. Alternatively, we 
use here a more straightforward approach based on the transformation of the energy of an emitted photon. 

Assume an isotropic emission of energy $E'$ in the frame that is comoving with the emitting region, with 
corresponding four-momentum $[E' , p_x'c, p_y'c, p_z'c]$. The observer receives photons of energy $E$ in the lab 
frame along the $x$ direction, so the observed four-momentum is $[E, p_xc = E, p_yc = 0, p_zc = 0]$. We can go from 
one frame to the other via a Lorentz-boost $(\Gamma, \Gamma \vec{\beta})$ of the emitting region and a rotation by an 
angle $\theta$ from the direction of motion, i.e.

$$
 \begin{bmatrix} E' \\ p_x'c \\ p_y'c \\ p_z'c \end{bmatrix}
 =
  \begin{bmatrix}
   \Gamma & - \Gamma \beta & & \\
   - \Gamma \beta & \Gamma & & \\
    & & 1 & \\
    & &   & 1 \\
   \end{bmatrix}
 \begin{bmatrix}
   1 & & & \\
     & \cos \theta & -\sin \theta & \\
     & \sin \theta & \cos \theta &  \\
    & &   & 1 \\
   \end{bmatrix}   
   \begin{bmatrix} E \\ E \\ 0 \\ 0 \end{bmatrix}
$$

The first space-like component reads $p_x'c = \Gamma E(\cos\theta-\beta)$. Photons emitted in the forward direction 
$p_x'>0$ thus reach the observer within a cone defined by $\cos\theta > \beta$. In the ultra-relativistic limit, 
this inequality reads $1-\theta^2/2 > 1 - 1/(2\Gamma^2)$, which defines a cone of half-opening angle
$\theta < 1 /\Gamma$. This corresponds to a half-opening angle
$\theta_\mathrm{max} = \frac{1}{\Gamma} \approx 6^\circ \times \big( \frac{\Gamma}{10} \big)^{-1}$.

The time-like component equation reads $E' = \Gamma E (1-\beta\cos\theta)$. Thus, in the observer's frame, the 
energy is enhanced by a Doppler factor $\delta = E / E'$ i.e.
$$
\delta = \frac{1}{\Gamma(1-\beta\cos\theta)}.
$$
This increase in energy $E=h\nu$ corresponds to an increase in frequency and therefore to a shortening of the 
observed time scales by a factor $\delta$. In the ultra-relativistic limit and for a jet nearly aligned with the 
line of site (blazar-like source), this correspond to an energy enhancement or a time shortening by a factor
$\delta \approx \frac{1}{\Gamma\big(1-[1-1/(2\Gamma^2)]\big)} \approx 2 \Gamma$ that is $\delta \approx 10 \times \big( \frac{\Gamma}{5} \big)$.

The specific intensity of the source, i.e. its brightness, is also enhanced. As $I_\nu/\nu^3$ is Lorentz invariant, 
the specific intensity is enhanced by a factor $\delta^3$ and the bolometric intensity,
$I = \int_0^{+\infty} I_\nu \dd \nu$, is enhanced by a factor $\delta^4 \approx 10,000 \times \big( \frac{\Gamma}{5} \big)^4$.


:::{exercise} Opacity of GRB jets
:label: exo:grb_opacity

Two shells are emitted from the central engine with a time delay $\Delta t_\mathrm{var}$ in the observer's frame. 
For simplicity, we assume that the first shell moves at $v_1 = \beta c$ and the second at $v_2 = c$.

1. Give an expression of the distance $r$ from the central engine (observer's frame) at which the shells collide as 
   a function of $\Delta t_\mathrm{var}$ and of the Lorentz factor of the first shell.

In the frame moving at four-velocity $(\Gamma, \Gamma\vec{\beta})$ towards the observer, the emission region is 
modeled as a spherical region of luminosity $L'$ and size $\Delta r' = c \Delta t_\mathrm{var}'$ filled (for 
simplicity) with a monochromatic photon field at $h\nu' = m_e c^2 \approx 511\,$keV.

The pair-production mechanism results in an optical depth of the medium, $\tau$, for photons. An optical depth is the 
product of a distance, a target density and a cross section. 

2. Give an expression of the optical depth for pair production as a function of the observed luminosity $L$ and 
   variability timescale $\Delta t_\mathrm{var}$, assuming a cross section $\sigma_{\gamma\gamma} \approx \sigma_T/5 \approx 0.1\,$barn.

The fraction of photons that escape interactions is $\exp(-\tau)$. Therefore, for photons to escape, the optical depth 
should not be too large ($\tau<1$, corresponding to an "optically-thin" medium).

The prompt emission of a short GRB shows an observed luminosity $L = 10^{44}\,$W and a duration $\Delta t_\mathrm{var} = 10\,$ms.

3. Give a constraint (expression and numerical value) on the Lorentz factor of the first shell and on the distance 
   from the central engine at which the internal shock between the two shells occurs.

:::{figure}  ../../images/GRB_scenario_DESY.jpg
:name: fig:grb_desy
:align: center
:width: 80%

Schematic view of the shocks between shells internal to the jet of a gamma-ray burst. From this [page](https://www.desy.de/news/news_search/index_eng.html?openDirectAnchor=760&two_columns=1&printversion=1). Exercise adapted from F. Rieger's lesson at this [page](https://www.mpi-hd.mpg.de/personalhomes/frieger/HEA4.pdf).

:::

:::{solution} exo:grb_opacity
:class: dropdown

1. Each shell reaches a radius $r_i = v_i(t-t_i)$, with $i=1,2$ and $t_2-t_1 = \Delta t_\mathrm{var}$. The internal 
   shock occurs at a distance $r=r_1=r_2$ and time $t = t_1 + r/v_1 = t_2 + r/v_2$. Then, $\Delta t_\mathrm{var} = r\times(1/v_1 - 1/v_2)$, i.e.
\begin{align}
r &= \Delta t_\mathrm{var} \frac{v_1v_2}{v_2-v_1}\\
  &= c\Delta t_\mathrm{var}\frac{\beta}{1-\beta}\\
  &\approx 2\Gamma^2 c\Delta t_\mathrm{var} \mathrm{\ for\ } \Gamma\gg 1.
\end{align} 

2. The optical depth is the product of a distance, a target density and a cross section. This pure number that 
   quantifies    the probability of interaction is Lorentz invariant. We can calculate its value in the isotropic 
   emission frame: $\tau_{\gamma\gamma} = \tau_{\gamma\gamma}' = n' \Delta r' \sigma_{\gamma\gamma}$, where the 
   distance is $\Delta r'= c \Delta t_\mathrm{var}'$ (causality argument) and where target photon density is $n' = \frac{\varepsilon}{h\nu'} = \frac{1}{h\nu'} \frac{4\pi}{c}I' = \frac{1}{h\nu'} \frac{4\pi}{c} \frac{L'}{4\pi (\Delta r')^2}$. This yields an optical depth:
\begin{align}
\tau_{\gamma\gamma} &= \frac{L'\sigma_{\gamma\gamma}}{h\nu' c^2 \Delta t_\mathrm{var}'}\\
 										&= \frac{L\sigma_{\gamma\gamma}/c^2}{\delta^5 m_e c^2 \Delta t_\mathrm{var}}, \mathrm{\ where\ }\delta \approx 2\Gamma \mathrm{\ is\ the\ Doppler\ factor}
\end{align}

3. The region is partly transparent to photons for $\tau_{\gamma\gamma} < 1$, i.e. for
\begin{align}
\delta &> \Big( \frac{L\sigma_{\gamma\gamma}/c^2}{m_e c^2 \Delta t_\mathrm{var}} \Big)^\frac{1}{5}\\
&> \Big( \frac{10^{44}\times 0.1\times 10^{-28}/(3\times 10^8))^2}{0.5 \times 10^6 \times 1.6 \times 10^{-19} \times 10^{-2}} \Big)^\frac{1}{5}\\
&\gtrsim 400, 
\end{align}
which corresponds to $\Gamma \gtrsim 200$ in the ultrarelativistic limit.

Injecting this lower bound on the Lorentz factor into the solution to question 1 yields $r \gtrsim 2 \times 10^{11}\,$m i.e. about 1 A.U.

:::


:::{tip}
**Notions from this chapter**

_Galactic and extragalactic sources_
- Can I cite one class of Galactic sources of gamma-rays?
- Can I cite one class of extragalactic sources of gamma-rays?
:::


:::{tip}
**Calculations / demonstrations**

_Intensity and energy density_
- What is the relation between these two quantities?

_Doppler factor: $\delta = \frac{1}{\Gamma(1-\beta\cos\theta)}$_
- What are $\delta$, $\Gamma$, $\beta$ and $\theta$?
- How are the energy of a photon, time between arrival of two photons and intensity (or luminosity) of a photon field affected by Doppler boosting?

_Optical depth: $\tau = n \sigma r$_
- What are $\tau$, $n$, $\sigma$, $r$ and their units? 
- What does $\tau \ll 1$ and $\tau \gg 1$ mean? 

:::
