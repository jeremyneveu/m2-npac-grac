---
short_title: []
authors:
  - jbiteau
keywords: []
---

Jetted and non-jetted astroparticle sources in the universe
=============================================


Multi-messenger emissions on cosmic scales
--------------------------------

### Energy density, surface brightness, flux density and luminosity

An observable directly related to the energy density of an isotropic photon field is the sky surface brightness, from which all the foregrounds have been subtracted. Following the notation of {cite}`1986rpa..book.....R`, the bolometric surface brightness or bolometric intensity, $I$, is defined as the energy passing through a surface $\dd A$ during a time $\dd t$ and from a solid angle $\dd \Omega$:
$$
\dd E = I \dd A \dd t \dd \Omega,
$$
with $[I] = \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}$.

The radiative energy density, $\varepsilon$, in a volume $\dd V = c \dd t \dd A$ is such as $dE = \varepsilon \dd V$, so that the average intensity integrated over the sphere is
$$
I = \frac{c}{4\pi} \varepsilon
$$ 

:::{important}
The specific intensity, $I_\nu$, is the derivative of the bolometric intensity, $I$:

$$
I = \int \dd \nu\ I_{\nu}, \quad \mathrm{with\ } [I_{\nu}] =  \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{Hz}^{-1}
$$

Specific intensity is often represented in the form $\nu I_\nu$ as a function of $\ln \nu$, since the integral under the curve then gives the bolometric intensity:
$$\int \dd \ln \nu\ \nu I_{\nu} = \int \dd \nu\ I_{\nu} = I$$

Radio-to-optical astronomers often plot $\nu I_\nu$, while X-ray and higher-energy astronomers often consider $E^2 J(E) = \nu I_\nu$, where both are in units of power per unit area per unit solid angle. 

Similarly, the specific flux density from a point source, denoted as $S_\nu$ or $F_\nu$ with $[F_\nu] = \mathrm{W}\,\mathrm{m}^{-2}$, is represented as $\nu F_\nu = E^2 \frac{\dd N}{\dd E}$, where $\left[\frac{\dd N}{\dd E}\right] = \mathrm{m}^{-2}\,\mathrm{s}^{-1}\,\mathrm{eV}^{-1}$. The specific and bolometric luminosity are estimated from the flux and distance as $L_\nu = 4\pi D_L^2 F_\nu$ and $L = 4\pi D_L^2 F$.

The net flux received from a region covering a solid angle $\dd \Omega$ at zenith angle $\theta$ can be computed from the surface brightness of that region as
$$
F = \int \dd\Omega\ I \cos \theta 
$$ 

Note that if $I$ is isotropic, the net flux is zero as the energy crossing the surface $\dd A$ in the $+\vec{n}$ direction is the opposite of that from $-\vec{n}$ direction.


:::

:::{note}
The literature sometimes uses the notation $I_{\mathrm{dex}}$ with $[I_{\mathrm{dex}}] = \mathrm{W}\,\mathrm{m}^{-2}\,\mathrm{sr}^{-1}\,\mathrm{dex}^{-1}$. With this notation, 
$$\int \dd \log_{10} \nu\ I_{\mathrm{dex}} = \int \dd \nu\ I_{\nu} = I$$
Note that $I_\mathrm{dex}$ differs by a factor $\nu \ln 10$ from $I_{\nu}$
:::

Following again {cite}`1986rpa..book.....R`, the energy density in a field of particles with momentum between $p$ and $p + \dd p$ depends on the number of particles per phase volume, $\dd \mathcal{N}/\dd^3 x \dd^3 p$ as

$$
\varepsilon_\nu \dd \nu = h\nu  \frac{\dd \mathcal{N}}{\dd^3 x \dd^3 p} 4\pi p^2 \dd p
$$

$\dd \mathcal{N}/\dd^3 x \dd^3 p$ is invariant under a Lorentz transformation. Indeed $\dd \mathcal{N}$ is countable and thus invariant. Under a boost $(\beta, \gamma)$ along the x-axis from the coomving frame (K') towards the observer's frame (K), one finds $\dd x = \gamma^{-1} \dd x'$ (length contraction) and $\dd p_x = \gamma (\dd p_{x'} + \beta \dd E') = \gamma \dd p_{x}'$ for particles with fixed energy (total momentum fixed between $p$ and $p + \dd p$). Thus $\dd^3 x \dd^3 p$ is invariant, *quod erat demonstrandum*.
 
 
One finds
$$
I_\nu \dd \nu = \frac{h}{c} (h\nu)^3  \frac{\dd \mathcal{N}}{\dd^3 x \dd^3 p} \dd \nu
$$

so that 

$$
I_\nu / \nu^3 \equiv \mathrm{Lorentz\ invariant}
$$


### The spectrum of the universe


:::{figure}  ../../images/The_Fitted_MM_EGAL_Background_2023.png
:name: fig:mm_spectrum
:align: center
:width: 100%

The multi-messenger extragalactic spectrum. Adapted from this [page](https://zenodo.org/records/7842239).
:::

The broadband emission from all galaxy populations is responsible for the spectrum of the universe shown in [](#fig:mm_spectrum). In particular, electromagnetic radiations include the cosmic radio background (CRB) from both active and star-forming galaxies, the cosmic infrared and optical backgrounds (CIB and COB) mostly from nucleosynthesis and dust emission, the cosmic X-ray background (CXB) from active galaxies and the cosmic gamma-ray background (CGB) from jetted active galaxies. The differential measurements of these cosmic backgrounds are of fundamental value: they reflect our knowledge of the distribution of light emitted by star formation, accretion and ejection integrated since the formation of the first astrophysical sources. Although these emissions are only a negligible part of the cosmic energy inventory, they provide us with a cosmological consistency test that is essential for understanding the content and evolution of the post-recombination universe  {cite:p}`2004ApJ...616..643F`. 

These measurements also quantify the degree of darkness of the night sky once the foregrounds are subtracted. It is the history of their emission that provides the solution to the Olbers paradox and the present intensity of these backgrounds that determines the darkness (or rather grayness) of the night sky. We can understand the extragalactic backgrounds at all electromagnetic wavelengths, the so-called extragalactic background light, using synthetic models of galaxy populations. Some unknowns in the extraglactic background light, including tensions between measurements, are nonetheless still the subject of active research. Light emission is fundamentally the result of decay, heating and acceleration of matter. We will explore in the following lessons the knowledge established with photons, in particular through multi-wavelength observations of gamma-ray sources, and to which extent this multi-wavelength knowledge allows us to understand extragalactic backgrounds observed today with other messengers, in particular the extragalactic neutrino background (ENB) between $30\,$TeV and $3\,$PeV and the extragalactic cosmic-ray background (ECRB) between $200\,$PeV and $200\,$EeV.



:::{exercise} Energy densities in the Milky Way
:label: exo:milky_way

The Galaxy can be seen as a disc of bolometric luminosity $(1.5-2.0) \times 10^{10} \ L_\odot$, approximated by a cylinder of diameter $2R=25\,$kpc and height $h=300\,$pc. Its bulge, with a bolometric luminosity $0.5 \times 10^{10} \ L_\odot$, can be approximated as a bar or spheroid of diameter $3\,$kpc. The bolometric luminosity of the Sun is $L_\odot = 3.8 \times 10^{26}\,$W. 


1. Calculate the energy density of the photon field in the disc in eV$\,$m$^{-3}$.

2. The magnetic field of the Milky Way is inferred to range in $1-10\,\mu$G that is $(1-10)\times 10^{-10}\,$T. Estimate the magnetic energy density in the Milky Way.

3. From the local cosmic-ray spectrum presented in [](#fig:cr_spectrum), estimate the energy density of cosmic rays in the Milky Way.

:::{figure}  ../../images/The_CR_Spectrum_2023.png
:name: fig:cr_spectrum
:align: center
:width: 60%

The local cosmic-ray spectrum. Components from the Milky Way dominate the brightness of the sky at least up to the knee structure at $E \approx 3\,$PeV. From this [page](https://zenodo.org/records/7948212).
:::


:::{solution} exo:milky_way
:class: dropdown

1. We assume the photon field to be isotropic in the disc of Milky Way. Then, we can estimate the photon density as:

$$
\begin{align}
\varepsilon_\mathrm{O-IR} &= \frac{4\pi}{c} I_\mathrm{O-IR} \nonumber \\
		 &= \frac{4\pi}{c} \frac{F_\mathrm{O-IR}}{\int \dd \Omega \cos \theta}
\end{align}
$$

where $F_\mathrm{O-IR}$ is the net flux emitted from one side of the disc and $\int \dd \Omega \cos \theta = 2\pi \int_0^1 \cos \theta \dd  \cos \theta = \pi$. The total flux emitted by the two sides of the disc is $2F_\mathrm{O-IR} = \frac{L_\mathrm{O-IR}}{\pi R^2}$, so that

$$
\begin{align}
\varepsilon_\mathrm{O-IR} &= \frac{4\pi}{c} I_\mathrm{O-IR} \\
		 &= \frac{2}{c} \frac{L_\mathrm{O-IR}}{\pi R^2}
 		 &= \frac{2}{c} \frac{L_\mathrm{O-IR}}{\pi R^2}
 		 &\approx (0.5-0.7) \times 10^{6} \,\mathrm{eV\,m}^{-3},
\end{align}
$$

i.e. two-to-three times the energy density of the CMB.

2. 
$$
\begin{align}
\varepsilon_B & = \frac{B^2}{2\mu_0} \\
 & \approx \frac{(1-100) \cdot 10^{-20} \times 6.2 \cdot 10^{18}}{2 \times 4\pi \times 10^{-7}} \,\mathrm{eV\,m}^{-3} \\
 & \approx (0.02-2) \times 10^{6} \,\mathrm{eV\,m}^{-3},
\end{align}
$$

3. The local cosmic-ray intensity can be approximated as $J(E) = J_0 \left(\frac{E}{E_0} \right)^{-p} = 2 \times 10^4\, \mathrm{GeV^{-1}}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}\,\mathrm{sr}^{-1}\times \left(\frac{E}{1\,\mathrm{GeV}} \right)^{-2.7}$.

Considering the cosmic-ray velocity to be near the speed of light (which is wrong near $1\,$GeV), the energy density of cosmic rays in the Milky Way above $E_0 = 1\,\mathrm{GeV} \approx m_p c^2$ can be approximated by

$$
\begin{align}
\varepsilon_\mathrm{CR} &= \frac{4\pi}{c} \int_{E_0} \dd E\ E J(E) \\
			 &= \frac{4\pi}{c} \frac{E_0^2 J_0}{p-2} \\
 			 &\approx 1.2 \times 10^{6} \,\mathrm{eV\,m}^{-3}
\end{align}
$$


Interestingly, the three components are close to equipartition.
:::



### The spectrum, composition and arrival directions of cosmic rays



:::{figure}  ../../images/CR_observables_2020PhR...872....1B.png
:name: fig:cr_observables
:align: center
:width: 60%

Simplified view of the cosmic-ray observables. The local cosmic-ray spectrum is scaled to a power $E^{2.7}$ in panel (a) to enhance the features. The mean logarithmic of cosmic-rays is shown in panel (b). Note that $\ln A_\mathrm{H} = 0$, $\ln A_\mathrm{C} \approx 2.5$ and $\ln A_\mathrm{Fe} \approx 4$. The dipole amplitude and right-ascension are displayed in panels (c) and (d), which also includes the right ascension of the Galactic Center. Adapted from {cite}`2020PhR...872....1B`.
:::



:::{note} Spherical coordinates for the observer

:::{figure}  ../../images/equatorial_coordinates.png
:name: fig:eq_coordinates
:align: center
:width: 100%

Schematic view of equatorial coordinates: right ascension (R.A. or $\alpha$) and declination (Dec or $\delta$). Adapted from this [page](https://lco.global/spacebook/sky/equatorial-coordinate-system).
:::

:::{figure}  ../../images/dipole_TeV.png
:name: fig:cr_TeV_dipole
:align: center
:width: 100%

The cosmic-ray relative flux, $\frac{\phi(\vec n)}{\phi_\mathrm{iso}}-1$ at energies above ${\sim}\,10 \,$TeV in equatorial coordinates, smoothed on a $5^\circ$ angular scale. Adapted by {cite}`2020PhR...872....1B` from {cite}`2017PrPNP..94..184A`.
:::


:::{figure}  ../../images/dipole_EeV.jpeg
:name: fig:cr_EeV_dipole
:align: center
:width: 90%

The cosmic-ray flux at energies above ${\sim}\,10 \,$EeV in equatorial coordinates, smoothed on a $45^\circ$ angular scale. The Galactic plane and center are shown as a dashed black and white line and a white circle, respectively. The supergalactic plane is shown as a dotted line. From {cite}`2022icrc.confE.375T`.
:::

:::{figure}  ../../images/uhecr_skymap_40EeV.png
:name: fig:cr_EeV_excess
:align: center
:width: 90%

The cosmic-ray flux at energies above ${\sim}\,40 \,$EeV in equatorial coordinates, smoothed on a $25^\circ$ angular scale. The Galactic plane and center are shown as a dashed orange line and an orange star, respectively. The supergalactic plane is shown as a gray line.
From {cite}`PierreAuger:2023mvf`.
:::


Candidate sources for cosmic-ray production
----------------------------------

### Known gamma-ray emitters with and without jets


:::{figure}  ../../images/Fermi_5_year_scaled.jpg
:name: fig:lat_skymap
:align: center
:width: 100%

Skymap in Galactic coordinates of the excess of gamma-rays with energies above $1\,$GeV from 5 years of observations with Fermi-LAT. From this [page](https://svs.gsfc.nasa.gov/11342).
:::

#### Bestiary of sources

Main populations of extragalactic sources: jetted active galactic nuclei (blazars and radio galaxies), gamma-ray bursts (long and short), starburst galaxies.

Emission on Galactic scale: Fermi / eROSITA bubbles

Galactic sources: supernova remnant (core-collapse, thermonuclear), pulsar wind nebula, pulsar, TeV halo; nova, X-ray binaries, microquasars


#### Relativistic beaming 

The existence of emission zones with a bulk velocity (relative to the central compact object) approaching the speed of light can be illustrated by the apparent superluminal motion of plasma blobs in astrophysical jets. This apparent velocity exceeding the speed of light is an effect that can be explained by purely geometrical arguments based on classical physics, as the following exercise illustrates.

:::{exercise} Superluminal motion
:label: exo:superluminal

The blob of plasma imaged in radio waves, farthest to the right in the figure below, appears to travel a distance of ${\sim}\,30\,$ light-years over a period of ${\sim}\,7\,$ years.

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

1. Following the notations in [figure %s](fig:superluminal_sol), the apparent velocity, $v_\mathrm{app}$, of the plasma blob is given by

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
v_\mathrm{app} &= \frac{2t\beta }{1+t^2 - (1-t^2)\beta}
$$
So that after a bit of algebra, an apparent speed that is equal to a fraction $k$ of the speed of light reads
$$
v_\mathrm{app} = kc  \Leftrightarrow \Big[(1+\beta)t - \beta/k\Big]^2 = (\beta/k - 1/\Gamma) \times (\beta/k + 1/\Gamma),
$$
where $\Gamma = 1/\sqrt{1-\beta^2}$ is the Lorentz factor of the plasma blob.

The right-hand-side equation as a solution if and only if $\beta/k - 1/\Gamma \geq 0$ i.e. $k \leq \Gamma\beta$. As $k = v_\mathrm{app}/c$ and $\beta < 1$, one gets $\Gamma > v_\mathrm{app}/c$ i.e. a Lorentz factor larger than $4$ for the jet of the active galactic nucleus 3C 279.

:::{figure}  ../../images/superluminal_calc.png
:name: fig:superluminal_sol
:align: center
:width: 30%

Schematic modeling of the radio knot.
:::

The relativistic motion of the plasma blob in jetted astrophysical sources results in anisotropic emission. The motion also increases the energy of the photons and the intensity of the radiation as the region moves towards the observer. 
The textbook derivation of this relativistic Doppler effect is based on velocity transformations. Alternatively, we use here a more straightforward approach based on the transformation of the energy of an emitted photon. 

Assume an isotropic emission of energy $E'$ in the frame that is comoving with the emitting region, with corresponding four-momentum $[E' , p_x'c, p_y'c, p_z'c]$. The observer receives photons of energy $E$ in the lab frame along the $x$ direction, so the observed four-momentum is $[E, p_xc = E, p_yc = 0, p_zc = 0]$. We can get from one frame to the other by a Lorentz-boost $(\Gamma, \Gamma \vec{\beta})$ of the emitting region and a rotation by an angle $\theta$ from the direction of motion, i.e.

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

The first space-like component reads $p_x'c = \Gamma E(\cos\theta-\beta)$. Photons emitted in the forward direction $p_x'>0$ thus reach the observer within a cone defined by $\cos\theta > \beta$. In the ultra-relativistic limit, this inequality reads $1-\theta^2/2 > 1 - 1/(2\Gamma^2)$, which defines a cone of half-opening angle $\theta < 1 /\Gamma$. This corresponds to a half-opening angle $\theta_\mathrm{max} \approx 3^\circ \times \big( \frac{\Gamma}{5} \big)^{-1}$.

The time-like component equation reads $E' = \Gamma E (1-\beta\cos\theta)$. Thus, in the observer's frame, the energy is enhanced by a Doppler factor $\delta = E / E'$ i.e.
$$
\delta = \frac{1}{\Gamma(1-\beta\cos\theta)}.
$$
This increase in energy $E=h\nu$ corresponds to an increase in frequency and therefore to a shortening of the observed time scales by a factor $\delta$. In the ultra-relativistic limit and for a jet nearly aligned with the line of site (blazar-like source), this correspond to an energy enhancement or a time shortening by a factor $\delta \approx \frac{1}{\Gamma\big(1-[1-1/(2\Gamma^2)]\big)} \approx 2 \Gamma$ that is $\delta \approx 10 \times \big( \frac{\Gamma}{5} \big)$.

The specific intensity of the source, i.e. its brightness, is also enhanced. As $I_\nu/\nu^3$ is Lorentz invariant, the specific intensity is enhanced by a factor $\delta^3$ and the bolometric intensity, $I = \int_0^{+\infty} I_\nu \dd \nu$, is enhanced by a factor $\delta^4 \approx 10,000 \times \big( \frac{\Gamma}{5} \big)^4$.


:::{exercise} Opacity of GRB jets
:label: exo:grb_opacity

Two shells are emitted from the central engine with a time delay $\Delta t_\mathrm{var}$ in the observer's frame. For simplicity, we assume that the first shell moves at $v_1 = \beta c$ and the second at $v_2 = c$.

1. Give an expression of the distance $r$ from the central engine (observer's frame) at which the shells collide as a function of $\Delta t_\mathrm{var}$ and the Lorentz factor of the first shell.

In the frame moving at four-velocity $(\Gamma, \Gamma\vec{\beta})$ towards the observer, the emission region is modeled as a spherical region of luminosity $L'$ and size $\Delta r' = c \Delta t_\mathrm{var}'$ filled (for simplicity) with a monochromatic photon field at $h\nu' = m_e c^2 \approx 511\,$keV.

2. Give an expression of the optical depth for pair production as a function of the observed luminosity $L$ and variability timescale $\Delta t_\mathrm{var}$, assuming a cross section $\sigma_{\gamma\gamma} \approx \sigma_T/5 \approx 0.1\,$barn.

The prompt emission of a short GRB shows an observed luminosity $L = 10^{44}\,$W and a duration $\Delta t_\mathrm{var} = 10\,$ms.

3. Give a constraint (expression and numerical value) on the the Lorentz factor of the first shell and on the distance from the central engine at which the internal shock between the two shells occurs.

:::{figure}  ../../images/GRB_scenario_DESY.jpg
:name: fig:superluminal_sol
:align: center
:width: 80%

Schematic view of the shocks between shells internal to the jet of a gamma-ray burst. From this [page](https://www.desy.de/news/news_search/index_eng.html?openDirectAnchor=760&two_columns=1&printversion=1). Exercise adapted from F. Rieger's lesson at this [page](https://www.mpi-hd.mpg.de/personalhomes/frieger/HEA4.pdf).

:::

:::{solution} exo:grb_opacity
:class: dropdown

1. Each shell reaches a radius $r_i = v_i(t-t_i)$, with $i=1,2$ and $t_2-t_1 = \Delta t_\mathrm{var}$. The internal shock occurs at a distance $r=r_1=r_2$ and time $t = t_1 + r/v_1 = t_2 + r/v_2$. Then, $\Delta t_\mathrm{var} = r\times(1/v_1 - 1/v_2)$, i.e.
\begin{align}
r &= \Delta t_\mathrm{var} \frac{v_1v_2}{v_2-v_1}\\
  &= c\Delta t_\mathrm{var}\frac{\beta}{1-\beta}\\
  &\approx 2\Gamma^2 c\Delta t_\mathrm{var} \mathrm{\ for\ } \Gamma\gg 1.
\end{align} 

2. The optical depth is the product of a distance, a target density and a cross section. This pure number that quantifies the probability of interaction is Lorentz invariant. We can calculate its value in the isotropic emission frame: $\tau_{\gamma\gamma} = \tau_{\gamma\gamma}' = n' \Delta r' \sigma_{\gamma\gamma}$, where the distance is $\Delta r'= c \Delta t_\mathrm{var}'$ (causality argument) and where target photon density is $n' = \frac{\varepsilon}{h\nu'} = \frac{1}{h\nu'} \frac{4\pi}{c}I' = \frac{1}{h\nu'} \frac{4\pi}{c} \frac{L'}{4\pi (\Delta r')^2}$. This yields an optical depth:
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


### Maximum energy: the Hillas criterion


A necessary condition for accelerating particles up to a given maximum energy is that their astrophysical source is large enough, or magnetised enough, to confine them for at least one radius of gyration. This relatively simple criterion, attributed to Michael Hillas, is used to classify astrophysical accelerators in a so-called Hillas diagram, as shown in [figure %s](fig:cr_hillas).

:::{figure}  ../../images/CR_Hillas.jpeg
:name: fig:cr_hillas
:align: center
:width: 60%

Magnetic field in Gauss vs size in km of candidate cosmic-ray sources. The Hillas limit, which provides the minimum magnetic field at a fixed size needed to accelerate cosmic rays to a given magnetic rigidity, is shown in blue for protons at the knee energy and in brown for protons at the ankle energy. Adapted from {cite}`2020PhR...872....1B`.
:::

The gyro-radius, $r_\mathrm{g}$, of a particle of four-velocity $(\gamma, \gamma\vec{\beta})$ derives from the equation of motion $\frac{\dd}{\dd t}\big(\gamma m \vec{v} \big) = Ze \vec{v}\times \vec{B}$, where $m$ and $Z$ are the mass and charge of the particle. As the magnetic field does no work, $\gamma m$ is constant so that the particle moves along an helicoidal trajectory characterized by $\gamma m \frac{v_\perp^2}{r_\mathrm{g}} = Z e B v_\perp$, where $p_\perp = \gamma m v_\perp$ is the momentum in the plane perpendicular to the $B$ field. Thus

$$
\begin{align}
r_\mathrm{g} &= \frac{p_\perp}{Z e B}\\
&= \frac{R}{Bc}\\
&= 1.1\,\mathrm{pc} \times \Big(\frac{R}{10^{15}\,\mathrm{V}}\Big) \times \Big(\frac{B}{1\,\mu\mathrm{G}}\Big)^{-1},
\end{align}
$$
where $R = \frac{p_\perp c}{Z e} \approx \frac{E}{Z e}$ is the magnetic rigidity in volts.


The Hillas criterion states that accelerating a particle up to a given rigidity $R$ within a region of size $L$ is only possible if $r_\mathrm{g}<r$, which imposes $R < r B c$. Accounting for relativistic bulk motion of the emitting region $(\Gamma, \Gamma\vec{\beta})$, the relativistic Hillas criterion on the observed rigidity reads


$$
\begin{align}
R_\mathrm{obs} < \Gamma \beta r' B' c\\\
&< 9 \times 10^{15}\,\mathrm{V} \times \Big(\frac{r'}{1\,\,\mathrm{pc}}\Big) \times \Big(\frac{B}{1\,\mu\mathrm{G}}\Big)^{-1}, \mathrm{\ or}\\
&< 9 \times 10^{18}\,\mathrm{V} \times \Big(\frac{r'}{1\,\,\mathrm{pc}}\Big) \times \Big(\frac{B}{1\,\mathrm{mG}}\Big)^{-1}
\end{align}
$$

The classes of Galactic sources satisfying this condition up to the magnetic rigidity corresponding to the knee and second knee of the cosmic-ray spectrum, i.e. a proton energy of $\approx 3 \times 10^{15}\,\mathrm{eV}$ and an energy of $\approx 10^{17}\,\mathrm{eV}$ for fully ionized iron are shown in [figure %s](fig:cr_hillas). Extragalactic sources are also shown and can be compared to the Hillas criterion up to the ankle and cut-off of the cosmic-ray spectrum, i.e. for maximum proton energy of $\approx 5 \times 10^{18}\,\mathrm{eV}$ and iron energy of $\approx 10^{20}\,\mathrm{eV}$.

### Cosmic-ray production rate

Cosmic-ray accelerators must not only be able to achieve a given maximum rigidity, but must also be sufficiently luminous that their cumulative emission reproduces the observed intensity, $I_\mathrm{CR} = \frac{c}{4\pi} \varepsilon_\mathrm{CR}$.

A particularly useful quantity for studying the origin of Galactic cosmic rays is the energy production rate:
$w_\mathrm{GCR} = \varepsilon_\mathrm{GCR}({>}\,1\,\mathrm{GeV})/\tau_\mathrm{esc}$, where $\varepsilon_\mathrm{GCR}({>}\,1\,\mathrm{GeV})\approx 1.2 \times 10^6\,\mathrm{eV\,m}^{-3} \approx 6 \times 10^{45}\,\mathrm{J\,kpc}^{-3}$ was determined in [exercise %s](exo:milky_way) and where $\tau_\mathrm{esc} \gtrsim 15\,$Myr is the residence time of cosmic rays in the Galaxy. This residence time is estimated from so called cosmic-ray clocks (see e.g. {cite}`2014arXiv1407.5223L`), e.g. through the ratio between $^{10}$Be ($t_{1/2} = 1.4\,$Myr) and its stable isotope $^{9}$Be, both formed by the fragmentation of carbon and oxygen nuclei confined in the Milky Way.

If we model the Milky Way as a disk with diameter $2r_\mathrm{MW} = 25\,$kpc and height $h_\mathrm{MW} = 0.3\,$kpc, then the energy production rate of Galactic cosmic rays integrated over the volume of the Milky Way yields the cumulative luminosity of the cosmic-ray sources:
\begin{align}
\sum_{\mathrm{src} \in \mathrm{MW}} L_\mathrm{src}(> 1\,\mathrm{GeV}) &= w_\mathrm{GCR} \times \pi r_\mathrm{MW}^2 h_\mathrm{MW}\\
&\lesssim 2 \times 10^{33}\,\mathrm{W}.
\end{align}

The kinetic energy of a core-collapse supernova can be estimated to 
\begin{align}
T_\mathrm{CC} &= \frac{1}{2}M_\mathrm{ejecta} v_\mathrm{shock}^2 \\
&\approx 10^{44}\,\mathrm{J} \times \Big( \frac{M_\mathrm{ejecta}}{10\,M_\odot} \Big) \times \Big( \frac{v_\mathrm{shock}}{3\times 10^3 \,\mathrm{km\,s}^{-1}} \Big)^2
\end{align}
and their explosion rate in the Milky-Way is estimated as $\lambda_\mathrm{CC} = (1.6 \pm 0.5)\times 10^{-2}\,\mathrm{yr}^{-1}$ ({cite}`2021NewA...8301498R`).

If core-collapse supernovae are responsible for accelerating the majority of cosmic rays to energies greater than 1 GeV, then the efficiency of the conversion of kinetic energy into cosmic rays, $\eta_\mathrm{GCR}$, should satisfy the relation
\begin{align}
\eta_\mathrm{GCR} &= \frac{\sum_{\mathrm{src} \in \mathrm{MW}} L_\mathrm{src}(> 1\,\mathrm{GeV})}{T_\mathrm{CC}\lambda_\mathrm{CC} } \\
&\lesssim 2\%,
\end{align}
a reasonnable constraint suggesting that core-collapse supernovae may be responsible for accelerating the bulk of Galactic cosmic rays.


