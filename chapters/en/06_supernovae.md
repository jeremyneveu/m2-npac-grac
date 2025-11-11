---
short_title: Type Ia supernovae
authors:
  - jneveu
keywords: supernovae, Hubble diagram, $H_0$
---

Type Ia supernovae
===================

There are two types of cosmological measurements: distance measurements, which map the expansion history of the Universe, and structure growth measurements, which describe the evolution of the Universe's large-scale structures. The former are simple data that ultimately amount to measuring the evolution of the Hubble parameter $H(z)$. Two methods are used. The first method, which has been used historically, uses standard candles, via Type Ia supernovae. If we know that a category of astrophysical objects all have the same intrinsic luminosity, then if this object appears faint, it is located far away and we can deduce its distance from its apparent luminosity. The second method uses a standard ruler, i.e., an invariant characteristic length that can be measured throughout the history of the Universe. If this length appears smaller than it is today at a certain redshift $z$, then knowing that it must not have evolved (or knowing how it evolved), we can find out its distance. This method is used in baryonic acoustic oscillations and the measurement of the angular power spectrum of the cosmic microwave background. The principle behind these two methods is illustrated in [](#fig:candles).

:::{figure} ../../images/chandelles.jpg
:name: fig:candles
:align: center
:width: 80%

Principle of the measurement of the expansion of the Universe using standard candles (Type Ia supernovae) and a standard ruler (average distance between galaxies, derived from the average distance between overdensities of the cosmic microwave background).
:::


Principle of the standard candle method
---------------------------------------

The standard candle method is based on measuring the luminous fluxes from stars of identical intrinsic luminosity. To measure the speed of expansion of the Universe, we need luminosity distances associated with redshifts and thus construct a Hubble-Lemaître diagram. 

The <wiki:Apparent_magnitude> is a logarithmic scale that measures the luminosity of an object observed from Earth. It is based on the measurement of a luminous flux $\Phi_{0}$ acquired with a telescope equipped with a photosensitive sensor ($\gamma$/s/m$^2$) or a bolometer (W/m$^2$), compared with a reference flux $\Phi_{\rm ref}$ which sets the scale. Historically, the scale was based on a standard star, Vega in the constellation Lyra. To tie in with the 6 categories of magnitudes defined in ancient times, the apparent magnitude of a star is defined by:
\begin{equation}
m = -2.5\log_{10} \left[\frac{\Phi_{0}}{\Phi_{\rm ref}} \right] 
\end{equation}
The absolute magnitude is the flux we would receive from this source at a distance of $10\,\parsec$:
\begin{equation}
M = -2.5\log_{10} \left[\frac{L}{4\pi (10\,\parsec)^2\Phi_{\rm ref}} \right] 
\end{equation}

:::{note} Magnitudes

The classification of the brightness of stars into magnitudes comes from Antiquity, and therefore from visual observation. Between stars of magnitude 0 and 5, there is a ratio of one hundred to one in luminous flux, the higher magnitude stars being the fainter. The flux is therefore divided by a factor of 2.5 between each magnitude.
:::

In an ideal world, it would be enough to measure the $\Phi_{0}^{(i)}$ fluxes of a collection of $N$ standard candles at $z_i$ redshifts and compare them to obtain a relationship between luminosity distance and redshift. The apparent magnitude $m_i$ of a standard candle at redshift $z_i$ is related to the expansion rate $H(z)$ via the luminosity distance:
\begin{align*}\label{eq:utopia}
m_i & = -2.5\log_{10} \left[\frac{ \Phi_{0}^{(i)}}{\Phi_{\rm ref}}\right] \\
& = -2.5 \log_{10}\left[ \frac{L}{4\pi D_L^2(z_i) \Phi_{\rm ref}}\right] \\
& = 5 \log_{10}\left[ \frac{D_L(z_i)}{10\,\parsec}\right] + M
\end{align*}
The quantity:
\begin{equation}
\mu = 5 \log_{10} \left[ \frac{D_L(z_i)}{10\,\parsec}\right] = 5 \log_{10} \left[\frac{(1+z)}{10\,\parsec} \int_0^z \frac{\dd z}{H(z)} \right] \text{ if } k=0
\end{equation}
is the decrease in luminosity in magnitude linked to the distance of the star. If a standard candle is 2 times further away, then it appears 4 times less bright and its distance modulus increases by 1.5 magnitudes. By measuring the fluxes, we can thus estimate the relative distances between the standard candles.

The most important point to note in this formula is that the cosmological expansion speed $H(z)$ is inscribed in the shape of the $\mu(z)$ curve, and not in its normalization. The normalization of the curve depends notably on $L$ and $H_0$. The standard candles method thus allows us to measure the evolution of the expansion of the Universe, without having to know their absolute luminosity $L$! On the other hand, if we know their absolute luminosity $L$, then we can establish a scale of absolute distances and the normalization of the Hubble diagram gives access to the value of $H_0$ ([](#fig:distmod)).

:::{figure} #distmod
:name: fig:distmod
:align: center
:width: 70%

Distance modulus as a function of redshift for three cosmological models. A change in the parameters $\Omega_i^0$ modifies the shape of the curve while the parameter $H_0$ modifies its normalization.
:::


Hubble diagram of supernovae
-----------------------------

To establish a Hubble diagram at cosmological distances, we need sources of identical luminosities that are visible at very great distances. Galaxies are of varying sizes and therefore intrinsic luminosities too variable to play this role. However, Type Ia supernovae are stellar explosions whose luminosity is commensurate with that of a galaxy. They can therefore be visible from far away but only for a certain time.

### Type Ia supernovae

Supernovae are classified into two types: gravitational or thermonuclear. The former are the best known: they correspond to the explosion of a massive star (more than 8 times the mass of the Sun) at the end of its life, leaving a dense and cold stellar core: a neutron star, or even a black hole in extreme cases. Type I supernovae are those that do not present hydrogen lines in their spectrum, while Type II supernovae contain them. Among Type I supernovae, those containing silicon are Type Ia, then the others Ib or Ic.

Stars with a mass less than $8\,M_\odot$ end their lives as red giants. At the end of helium burning, the outer layers are dispersed into the interstellar medium as planetary nebulae (without necessarily producing an intense explosion), leaving the stellar core bare. The collapse of the core is stopped because of the degeneracy pressure of electrons (and not neutrons as for neutron stars) and its low mass (typically $0.5\,M_\odot$). Its surface temperature remains very high for a long time (about $10\,000\,\kelvin$), hence its name of white dwarf. It is essentially composed of carbon and oxygen, the helium and hydrogen having been expelled into space. The typical radius of such an object is a few thousand kilometers (like a terrestrial planet). 
 
:::{figure} ../../images/Type_Ia_Supernova_When_a_White_Dwarf_Steals_Material_from_Companion.mp4

This animation shows the explosion of a white dwarf, the extremely dense remnant of a star that can no longer burn nuclear fuel in its core. In this Type Ia supernova, the white dwarf's gravity steals matter from a nearby stellar companion. When the white dwarf reaches a mass estimated at 1.4 times the current mass of the Sun, it can no longer support its own weight and explodes. Credit: NASA/JPL-Caltech
:::


According to a study by the Very Large Telescope, about 75% of massive stars live in binary systems {cite:p}`Sana2012`. In some cases, a white dwarf can therefore be gravitationally bound to another star which, if it is sufficiently close, can see its outer layers sucked in by the gravity of the white dwarf. When the white dwarf has accumulated too much matter coming from its neighbor and approaches the Chandrasekhar mass ($1.4\,M_\odot$), it becomes unstable. The pressure and temperature conditions at the core of the white dwarf allow the reignition of carbon fusion. The white dwarf cannot expand and cool because of the degeneracy pressure of electrons, independent of temperature (quantum effect). The reaction runs away into a thermonuclear flame that vaporizes the star in a few seconds. The explosion enriches the interstellar medium with intermediate mass elements (oxygen, calcium, magnesium, silicon, sulfur) and elements from the iron family (nickel, cobalt). However, this explosion scenario remains only a hypothesis insofar as no proof yet exists. Other scenarios exist such as the merger of two white dwarfs {cite:p}`Nomoto2013`.

SNe Ia draw their energy from the disintegration of iron-group elements that were produced during the explosion <doi:10.1086/150102>. The main radioactive element formed is $^{56}_{28}\text{Ni}$:
\begin{equation}
2\ ^{12}_{\ 6}\mathrm{C} + 2\ ^{16}_{\ 8}\mathrm{O} \rightarrow ^{56}_{28}\mathrm{Ni}
\end{equation}
since it is a simple stoichiometric combination of carbon and oxygen atoms, the most abundant atoms of a white dwarf. The nickel isotope $^{56}_{28}\text{Ni}$ then disintegrates into $^{56}_{27}\text{Co}$ with a half-life of 6.1 days, which itself disintegrates into stable iron $^{56}_{26}\text{Fe}$ with a half-life of 77.3 days: 
\begin{equation}
^{56}_{28}\mathrm{Ni} \rightarrow ^{56}_{27}\mathrm{Co} \rightarrow ^{56}_{26}\mathrm{Fe}
\end{equation}
The total luminosity is estimated at $10^{10}\,L_\odot$, i.e., about that of a galaxy (see photographs [](#fig:sn) and [](#fig:sn2)). These are therefore objects a priori visible at cosmological distances. Since the explosion occurs systematically at the same stellar mass, roughly the same amount of material is ejected into space and emits the same amount of light. Moreover, since the composition of white dwarfs is very standard, the composition of the emitting matter is the same. They therefore all have roughly the same intrinsic total luminosity. However, they are also transient events: the duration of a supernova is a few tens of days. To capture one, you therefore need to look at the sky in the right place and at the right time.


Type Ia supernovae (SNe Ia) are the first cosmological probes that made it possible to measure the expansion of the Universe over cosmological distances, and discover its accelerated expansion {cite:p}`Riess1998; Perlmutter1999`. The Nobel Prize in Physics was awarded in 2011 to Saul Perlmutter, Brian Schmidt and Adam Riess for this major discovery. 

:::{figure} ../../images/SN1994D.jpg
:name: fig:sn
:align: center
:width: 60%

The supernova SN 1994D (the bright white dot in the bottom left of the image), in the spiral galaxy NGC4526.
:::

:::{figure} ../../images/sn2023_ixf_ugri_gimp_leg.png
:name: fig:sn2
:align: center
:width: 60%

The supernova sn2023ixf discovered by the ZTF survey and photographed by the StarDICE telescope (Newton, diameter $40\,$cm) in 4 $ugri$ filters on 25 May 2023.
:::




### Spectral sequences and light curves



A Type Ia supernova remains visible for about 40 days in the visible sky. To recognize its type, it must be observed in several colors and if possible acquire its spectrum. A sequence of spectra acquired on a Type Ia supernova is presented in [](#fig:spectresIa).


:::{iframe} https://www.youtube.com/embed/350HR7Z8OYw?si=luHEY7x1g1TQDKvd
:width: 100%

Series of images of a Type Ia supernova explosion. The supernova, SN 2015F, occurred in galaxy NGC 2442 in early March 2015, at a distance of about 80 million light-years from Earth. Daily images from February 2015 to October 2015 were combined to create this film. Images were taken with a 17-inch robotic telescope in Australia. 
:::

:::{figure} ../../images/timeseries.png
:name: fig:spectresIa
:align: center
:width: 70%

Spectro-temporal series of SN2011fe measured by the SNfactory survey {cite:p}`Pereira2013`. The names of the main components of the spectrum are indicated in the upper part of the figure.
:::


:::{figure} ../../images/lc.png
:name: fig:courbeslumiere
:align: center
:width: 70%

Light curves synthesized SN2011fe using the UBVRI$_\mathrm{SNf}$ filter set {cite:p}`Pereira2013`. Filled and open symbols correspond to photometric and non-photometric nights respectively. The results of a simultaneous SALT2 fit of UBVR$_\mathrm{SNf}$ in the range in the phase interval $-\,16 < t < +\,25$ days are represented by solid lines, with the corresponding residuals (SALT2 - SNf) on the lower panel. The shaded areas represent the error of the SALT2 model. The break in the time axis corresponds to the gap of $\sim 50$ days in the follow-up during which SN2011fe was not visible during the night from Hawaii. Note the change in scale of the extended time axis covering the late observations.
:::

In practice, we do not have spectral sequences as precise as the one presented in [](#fig:spectresIa) for each detected supernova, because this costs too much observation time on the world's largest telescopes equipped with spectrographs. Only the SNFactory survey has dedicated a spectrograph to the systematic spectral study of supernovae. As a general rule, if possible, only one spectrum of the supernova is acquired around its maximum luminosity (because it is easier) in order to verify that it is indeed a Type Ia (identification spectrum), with a spectrograph that does not need to have high resolution to identify the main lines of the thermonuclear explosion. Later, a spectrum of the host galaxy is taken to measure its redshift precisely if it is not already known, with a higher resolution spectrograph (redshift spectrum).

The main information available on a Type Ia supernova is therefore its light curve, i.e., the temporal sequence of luminous fluxes, measured by a telescope with different band-pass filters equipping the telescope's camera [](#fig:courbeslumiere). 


It is therefore necessary to define an instant to compare the brightness of standard candles and a reference filter. For practical reasons, we use the magnitudes at maximum emission as a reference. For historical reasons, we use the Johnson B band as a reference filter. **The magnitude of the maximum luminosity of a Type Ia supernova observed in B band is therefore used as a standard candle, or at least standardizable.**


:::{note} Photometric systems
:class: dropdown

```{figure} ../../images/photometric_systems.png
:name: fig:photsyst
:align: center
:width: 70%

Band-pass filters for different photometric systems {cite:p}`Bessell2005`.

```

Astrophysical and cosmological surveys in photometry are interested in measuring the color of objects to access their physical properties. For this, telescopes are equipped with band-pass filters, whose shapes and positions depend on the technologies used and the needs of the survey.

A standard photometric system is defined by a list of standard magnitudes and colors measured at specific bandwidths for a set of stars well distributed across the sky. The observed magnitudes are corrected to account for the attenuation of Earth's atmosphere away from the zenith, and the data are then normally extrapolated to zero air mass (outside the atmosphere). 

The UBV system is one of the oldest and most widely used standard photoelectric photometric systems <doi:10.1086/145697>. The B band was designed to approximate the raw photographic magnitude (minus UV), while the V band was designed to approximate the visual magnitude system. The photometric systems of modern SDSS and LSST surveys instead use interference filters named ugrizy in the visible and near infrared.

:::


### Rest frame magnitude

The luminous fluxes $\Phi$ expressed in ($\gamma$/s/m$^2$) or (W/m$^2$) are called bolometric[^bolo] because they are integrated over the entire spectrum. Unfortunately, the ability to measure this quantity depends on the sensor used. In the visible and infrared, sensors are based on the photoelectric effect so they are transparent above a certain wavelength. In the visible and infrared, measured fluxes cannot be bolometric. 

Moreover, much information can be derived from measuring the color of an object, such as the type of supernova: for this it must be observed through different band-pass filters and compare the fluxes. 

We introduce the spectral energy density of a star $S_\lambda(\lambda)$ expressed[^Sfreq] in W/m$^2$/nm. Let us note $T_f(\lambda)$ the transmission of the instrument equipped with a filter $f$. The measured flux is then:
\begin{equation}
\Phi_{0,f} = \int \frac{\dd \lambda}{hc/\lambda} S_\lambda(\lambda) T_f(\lambda) \text{\ \ \   in $\gamma$/m$^2$/s}
\end{equation}
where $\lambda$ is the wavelength of incident photons. Then the definition of apparent magnitude for a filter $f$ becomes:
\begin{equation}
m_f = -2.5 \log_{10} \left[ \frac{ \int \lambda \dd \lambda S_\lambda(\lambda) T_f(\lambda) }{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_f(\lambda)}\right]
\end{equation}
with $S_{\mathrm{ref}}(\lambda)$ the spectral flux density of the reference source (Vega for example). The absolute magnitude in filter $f$ is the magnitude of the star in filter $f$ if observed in its rest frame at $10\,\parsec$:
\begin{equation}
M_f = -2.5\log_{10} \left[\frac{1}{4\pi (10\,\parsec)^2} \frac{ \int \lambda \dd \lambda L_\lambda(\lambda) T_f(\lambda)}{ \int \lambda \dd \lambda \Phi_{\mathrm{ref}}(\lambda)T_f(\lambda) } \right] 
\end{equation}
with $L_\lambda$ the spectral luminosity (in W/nm). 

We note $B(\lambda)$ the transmission of filter B in the Johnson UBV photometric system (see box). Then we define:
\begin{equation}
m_B^* = -2.5 \log_{10} \left[ \frac{ \int \lambda \dd \lambda S_\lambda(\lambda) B(\lambda) }{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) B(\lambda)}\right]
\end{equation}
The absolute magnitude in band $B$ is:
\begin{equation}
M_B = -2.5\log_{10} \left[\frac{1}{4\pi (10\,\parsec)^2} \frac{ \int \lambda \dd \lambda L_\lambda(\lambda) B(\lambda)}{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) B(\lambda)}   \right] 
\end{equation}
 
However, not all telescopes are equipped with a B filter. Moreover, and this is the main reason, the emission maximum shifts in wavelength with the redshift so it would be necessary to redshift the B filter to capture the same portion of spectrum ([](#fig:snIaB)). Since we want to compare only the effect of distance to map $D_L(z)$, these wavelength shift effects must nevertheless be removed to standardize and compare the observed flux at maximum emission. Historically, for Type Ia supernovae, cosmologists establish apparent magnitudes in B band _in the supernova's rest frame_. The magnitude $m_B^*$ is therefore the apparent magnitude in the rest frame in B band, _as if there were no expansion but only a distance effect_.

**The standard candle is the maximum emission of Type Ia supernovae in band $B$ as if observed in its rest frame.**


:::{figure} ../../images/snIa_restframeB.png
:name: fig:snIaB
:align: center
:width: 100%

Apparent magnitudes in band $B$ for supernovae at different redshifts: they correspond to the integral of the supernova's spectral density at its maximum in the redshifted $B$ band.
:::

Since it is not possible to make an observation in the supernova's rest frame, this magnitude $m_B^*$ must be calculated from observations in arbitrary filters $f$ and a _spectrophotometric_ model of the supernova.

### Spectrophotometric model

The spectrophotometric model will be the data of the spectral density as a function of time $S_\lambda(\lambda, t)$, determined on the data (the collection of light curves and spectra available). Suppose we are able to obtain it, after training on the data, as with the SALT2 model {cite:p}`Guy2007`. How can we transform the observed apparent magnitudes $m_f$ into B band magnitudes in the rest frame $m_B^*$?

First, we must study the effect of redshift on spectral densities.
The flux $\Phi_{0}$ and the intrinsic luminosity $L$ (in W) of a star located at redshift $z$ are related by:
\begin{equation}\label{eq:boloPhiL}
\Phi_{0} = \frac{L}{4\pi D_L^2(z)}
\end{equation}
with $D_L(z)$ the luminosity distance. All photons received in a narrow logarithmic frequency range centered on the observed wavelength $\lambda_0$ have been emitted in an equally narrow wavelength range also centered on $\lambda_E = \lambda_0 / (1+z)$. Equation [](#eq:boloPhiL) thus relates the spectral flux densities to the spectral luminosities in the presence of a redshift $z$ {cite:p}`Condon2018`:
\begin{align}
\dd \lambda_0 S_\lambda(\lambda_0) & =  \frac{\dd \lambda_E L_\lambda(\lambda_E)}{4 \pi D_L^2 (z)} =  \frac{\dd \lambda_0}{1+z}\frac{ L_\lambda(\lambda_0/(1+z))}{4 \pi D_L^2 (z)} \notag \\ 
& \Rightarrow S_\lambda(\lambda_0) =\frac{L_\lambda(\lambda_0/(1+z))}{4 \pi (1+z) D_L^2 (z)} 
\end{align}
This relation gives the link between the spectral flux density observed at $\lambda_0$ and the spectral luminosity density emitted at $\lambda_E$.

Now, let us search how to transform the observed magnitudes $m_f$ into magnitudes $m_B^*$, from the definition of apparent magnitude in band $f$:
\begin{align*}
m_f & = -2.5 \log_{10} \left[ \frac{\int \lambda \dd \lambda S_\lambda(\lambda) T_f(\lambda) }{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_f(\lambda)}\right] \\
& = -2.5 \log_{10} \left[\frac{1}{4 \pi (1+z) D_L^2 (z)} \frac{\int \lambda \dd \lambda L_\lambda(\lambda/(1+z)) T_f(\lambda) }{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_f(\lambda)}\right]
\end{align*}
Let us define $K_{fB}$ the _$K$-correction_ in bands $f$ and $B$ {cite:p}`hogg2002k`:
\begin{align*}
K_{fB} &  = -2.5\log_{10} \left[\frac{1}{(1+z)} \frac{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) B(\lambda)}{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_f(\lambda)}  \frac{\int \lambda \dd \lambda L_\lambda(\lambda/(1+z)) T_f(\lambda) }{\int \lambda \dd \lambda L_\lambda(\lambda) B(\lambda)}\right]
\end{align*}
Then the apparent magnitude can be decomposed into three terms:
\begin{align*}
m_f &  = M_B + \mu(z) + K_{fB}(z) 
\end{align*}
and the magnitude $m_B^*$ is calculated from the observations $m_f$ and the calculated $K$-correction:
$$ \boxed{m_B^* = m_f - K_{fB}}$$
The $K$-correction represents the magnitude correction that must be applied if we observed the star in its rest frame and with another filter. After applying the $K$-correction, the Hubble diagram is simply modeled by:
\begin{equation}
\boxed{m_B^*(z) = m_f - K_{fB}(z) = M_B + \mu(z)}
\end{equation}
an equation very similar to [](#eq:utopia). The left member represents the magnitudes acquired by the telescope and transformed into B band at rest and at maximum. The right member represents the explanatory cosmological model. For SNe Ia, $M_B = -19.08 \pm 0.03$ {cite:p}`Betoule2014`. We can see that the distance dependence is entirely contained in the distance modulus $\mu(z)$, but notice that there is an additional redshift dependence in the $K$-correction. It is therefore necessary to know how to correctly model $K_{fB}(z)$ so as not to introduce redshift bias in the Hubble diagram. 

Unfortunately, the $K$-correction depends on a certain number of ingredients that must therefore be known beforehand to calculate it:
- the redshift $z$, to be inferred from a spectrum;
- the spectral density $S_\lambda$ of the supernova, to be constructed by a spectrophotometric model fitted to the measured spectral sequences (as in [](#fig:spectresIa)) like SALT2 {cite:p}`Guy2007`;
- the reference spectral density $S_{\mathrm{ref}}(\lambda)$, to be established by measurement (<doi:10.1086/153547>, <doi:10.48550/arXiv.2411.03256>) or stellar atmosphere modeling <doi:10.1086/677655>;
- the transmission of the telescope filters $T_f$, or even the atmospheric transmission of the site $T_{\mathrm{atm}}(\lambda)$.

To obtain a measurement of the dark energy equation of state parameter $w_{DE}$ at the percent level, each of these ingredients must therefore be established to better than the percent. Today, the dominant uncertainties on the measurement of $w_{DE}$ by Type Ia supernovae are the systematic uncertainties of photometric calibration, i.e., knowledge of the bandwidth of instrument filters as well as knowledge of reference fluxes {cite:p}`Betoule2013,Scolnic2018`.

#### Standardization

After $K$-correction, we can compare the magnitudes $m_B^*$ to a cosmological model. With the JLA data from the SuperNova Legacy Survey, we obtain the Hubble diagram [](#fig:hubblemb).

:::{figure} #hubbleDiagramMb
:name: fig:hubblemb
:align: center
:width: 70%

Hubble diagram of the 740 SNeIa from the SNLS survey, compared to a $\Lambda$CDM model with $\Omega_m^0 = 0.3$ and $\Omega_\Lambda^0=0.7$.
:::

Around the diagram, we observe that the residuals to the Hubble diagram have a dispersion of $0.4\,$mag, greater than the measurement errors. If we plot these residuals as a function of the color $c=B-V$ or the normalized duration $x_1$ of the supernova, we see that they are correlated ([](#fig:hubbleRes)). 

:::{list-table} Residuals to the Hubble diagram colored as a function of the normalized duration $x_1$ (left) or the color $c=B-V$ (right).
:header-rows: 0
:name: fig:hubbleRes

* - :::{image} #hubbleResX1
    :alt: x1
    :width: 95%
    :align: center
    :::
  - :::{image} #hubbleResC
    :alt: color
    :width: 100%
    :align: center
    :::
:::

There is therefore a variability of supernovae that has not been taken into account in our spectrophotometric model so far.

We observe that the longer the light curve lasts in time, the brighter it is at its maximum (*brighter-slower* rule). Moreover, the bluer the SNIa are, the brighter they are as well (*brighter-bluer* rule). There is also an environment effect that links the brightness of the supernova and the mass of the host galaxy.

:::{figure} ../../images/courbes_de_lumiere_x1c.png
:name: fig:courbes_de_lumiere_x1c
:align: center
:width: 60%

Light curves of SNe Ia from the JLA dataset of the SNLS survey colored as a function of $x_1$ or $c$ {cite:p}`nicola2022`.
:::


The light flux is linked to the production and decay of nickel $^{56}$Ni. The two relations presented above can thus be explained qualitatively: the more $^{56}$Ni the SNIa produces, the brighter it will be and the more it will contain FeII and CoII ions emitting in the blue, but also the more it will be opaque (so the emission of photons by scattering will be delayed, so the SNIa will shine longer) {cite:p}`Kasen2007`.

SNe Ia are therefore not so standard, because their light curves depend on the amount of $^{56}$Ni available at the origin. Nevertheless, without correcting this intrinsic dispersion, the teams of the Supernova Cosmology Project (SCP) led by Saul Perlmutter and the High-z Supernova Search Team led by Brian Schmidt were able to demonstrate the existence of an accelerated expansion {cite:p}`Riess1998; Perlmutter1999`. This dispersion is problematic for improving measurements of the expansion of the Universe at the percent level. Nevertheless, it can be described empirically by two linear relations for $x_1$ and $c$ with coefficients $\alpha$ and $\beta$ respectively. For the host mass, we adjust a parameter $\Delta M_{host}$ increasing the magnitude for supernovae located in galaxies of mass greater than $10^{10}\,M_\odot$.

These three empirical relations add three additional parameters $\alpha$, $\beta$ and $\Delta M_{host}$ to also fit on the data <doi:10.1086/307883>:
\begin{equation}
\boxed{m_{B,corr}^* = M_B + \mu -\alpha x_1 + \beta c +  \Delta M_{host}}
\end{equation}
After this standardization, the dispersion in the Hubble diagram is reduced to $0.15\,$mag which increases the precision on cosmological parameters.


:::{figure} ../../images/HD_jla.png
:name: fig:HD
:align: center
:width: 70%

Hubble diagram of supernovae from the JLA catalog. The black curve represents a $\Lambda$CDM model fitted to the data. A model without dark energy would appear significantly below the curve described by the data ($-0.6\,$mag at $z=1$).
:::

:::{note} Origin of $\Delta M_{host}$

Indeed, it seems that massive galaxies contain much more metals and that supernovae can appear brighter there than in light galaxies (see the discussion section 5.5 of reference {cite:p}`Sullivan2010`). As suggested by reference {cite:p}`Sullivan2010`, we divide the data into two batches according to the mass of the host galaxy. 
:::




### Calibrations

:::{figure} ../../images/strategy1.png
:name: fig:SNCalib
:align: center
:width: 70%

Strategies for calibrating the measurement of the luminous flux of tertiary stars (secondary stars are not represented). The redshifted $B$ band is represented by a thick blue line on the spectra of SNe Ia. 
:::

### State of the art









Local measurement of $H_0$
---------------------------

TODO: See, read and study https://arxiv.org/abs/2311.07552 

The distance modulus $\mu(z)$ allows us to measure the relative distance between SNe Ia, which provides crucial information on dark energy. However, the absolute distance of SNe Ia cannot be obtained by this method: there is a degeneracy between the luminosity of SNe Ia $L$ and $H_0$ during estimation. To break this degeneracy, the cosmic distance ladder is used. This method involves a series of overlapping distance measurements using various astronomical objects and techniques, as illustrated in figure 12 of {cite:t}`Riess2022`. By anchoring the distances of SNe Ia to distances measured independently by the cosmic distance ladder, we can disentangle the absolute magnitude of SNe Ia from that of H0. In what follows, we will discuss the different steps of this distance ladder.

:::{figure} ../../images/distance_ladder.png
:name: fig:distance_ladder
:align: center
:width: 100%

Astrophysical distance ladder {cite:p}`Riess2022`. Measurements of orbital parameters in the Solar System allow calibrating the measurement of stellar distances by the parallax method. The distance of certain Cepheid stars is measured by parallax which allows establishing a relation between the flux of cepheids, their period of luminosity and their distance (lower square). The distance obtained by the luminosity of Cepheids in nearby galaxies allows calibrating the intrinsic luminosity of SNe Ia exploding in a galaxy containing Cepheids (intermediate square). Once the intrinsic luminosity of SNe Ia is known, measuring the slope of the distance-redshift relation for distant supernovae (but not too distant) allows access to $H_0$.
:::

### Parallax measurement

When a foreground star is observed from two opposite positions, A and B, on Earth's orbit around the Sun, it appears to move relative to the background star field toward positions A' and B'. This apparent shift is called parallax. The distance between Earth and the Sun is defined as an astronomical unit (AU), i.e., the average between the two semi-axes of Earth's elliptical orbit. With this distance, and by measuring the apparent displacement of the star's position, we can calculate by trigonometry the distance between the observer and the star. This phenomenon is known as parallax. Parallax measurements made by Gaia reach a precision of 0.04 arcsec <doi:10.1051/0004-6361/201832964>. This method constitutes the first rung of the cosmic distance ladder.

###  Cepheids


Cepheids are a type of star that pulsates radially, undergoing regular variations in diameter and temperature. These pulsations result in luminosity changes with a well-defined and stable period and amplitude. They were discovered by Henrietta Swan Leavitt {cite:p}`Leavitt1907`, who highlighted the correlation between the star's diameter and temperature.

:::{figure} ../../images/leavitt_cepheids.png
:name: fig:leavitt_cepheids
:align: center
:width: 70%

Relation between the magnitude of the minima (lower curve) and maxima (upper curve) of Cepheid light curves as a function of the logarithm of their pulsation period, according to {cite:t}`Leavitt1912`.
:::

The magnitude of the maxima or minima of a Cepheid's light curve is proportional to the logarithm of its pulsation period. This law is known as Leavitt's law, and figure 2 of {cite:t}`Leavitt1912`, illustrates this relation ([](#fig:leavitt_cepheids)).

By observing Cepheids close enough to use the parallax method for distance estimation, we can calibrate the absolute magnitude of Cepheids, and therefore their intrinsic period-luminosity relation. Due to the stability of their period-luminosity function, this calibration can then be applied to all Cepheids, allowing us to measure their luminosity distance in other galaxies where the parallax method is not feasible. Therefore, Cepheids serve as the first standard candle in the cosmic distance ladder, allowing us to determine the distance of other galaxies, as shown in the central graph of [](#fig:distance_ladder).




:::{note} NGC4258 maser

Galaxy NGC4258 contains water molecule masers, the equivalent of lasers but with microwaves, observable in radio astronomy. Masers are molecular gas clouds distributed in a rotating accretion disk and excited by the central black hole of this galaxy. Following the emission line at $22\,$GHz over several months allowed measuring the acceleration in the accretion disk as a function of angular distance from the center {cite:p}`Greenhill1995`. Knowing the acceleration, velocity and assuming the orbit is Keplerian, we can deduce the physical distance between the masers and the center of rotation. Associated with their apparent angular distances, we finally deduce the distance of NGC4258: $(7.60 \pm 0.17 \pm 0.15)\,$Mpc (<doi:10.1038/22972>,  <doi:10.1088/0004-637X/775/1/13>). The observation of 443 Cepheids in NGC4258 then allows refining the calibration of their period-luminosity relation {cite:p}`Riess2022` and increasing the precision on $H_0$.

:::


### Type Ia supernovae

Once the period-luminosity function of Cepheids is calibrated, this calibration is transferred to SNe Ia. To estimate the distance of a galaxy using a Cepheid, it must be resolved relative to other luminous sources in the galaxy and its photometry must be performed ([](#fig:cepheids_shoes)). By measuring its pulsation period, we deduce its intrinsic luminosity and therefore the distance of the host galaxy. 


:::{figure} ../../images/cepheids_shoes.png
:name: fig:cepheids_shoes
:align: center
:width: 70%

Identification of Cepheids (red dots) in 18 galaxies where SNe Ia were observed as well as in the maser NGC4258, by the SHOES survey of the Hubble Space Telescope (from {cite:t}`Riess2022`).
:::

Next, observing an SN Ia in the same galaxy allows knowing its intrinsic luminosity since the distance is known via the Cepheid. {cite:t}`Riess2022` reports the observation of 42 SNe Ia in 37 calibrated hosts. These SNe Ia are represented in the central square of [](#fig:distance_ladder), allowing calibration of the absolute magnitude of SNe Ia. Finally, the upper square plots a Hubble diagram of SNe Ia, which is directly linked to the geometric distance estimation by the parallax method. 

With this sample, {cite:t}`Riess2022` reports a measurement of $H_0$ of $73.04 \pm 1.04\,$km/s/Mpc, in tension at more than $5\sigma$ with the extrapolation of measurements from {cite:t}`Planck2018`. There is therefore a disagreement between measurements made on the CMB (young universe, distant) and measurements made with SNe Ia (recent universe, local). Multiple sources of systematic errors have been investigated but so far none of them seem to resolve the tension. Alternative independent measurement methods are also being implemented to decide between SNe Ia proponents and CMB proponents, such as for example the use of neutron star mergers observed in optical and gravitational waves. Also, new physics models are in competition to reconcile the young universe and the recent universe ($H_0$-Olympics: <doi:10.1016/j.physrep.2022.07.001>). 




:::{important} To remember

- Type Ia supernovae are thermonuclear stellar explosions having very similar intrinsic luminosities, as important as an entire galaxy. However, they only last about forty days.

- The apparent magnitude in B band calculated in the supernova's rest frame is the standard flux allowing comparison of Type Ia supernovae among themselves and establishing a distance-redshift relation (Hubble-Lemaître diagram).

- The calculation involves knowing well the bandpasses of the observation instrument in order not to introduce bias on distance measurements.

- SNe Ia are standardizable by three empirical relations involving their color, their duration and the mass of the host galaxy.

- The measurement of $H_0$ by SNe Ia is calibrated on local distance measurements, in particular on the period-luminosity relation of Cepheids.

::: 


:::{seealso}  To go further

- Effect of redshift on astrophysical measurements: {cite:t}`Condon2018`

- On the history of the first Hubble diagram: https://arxiv.org/abs/2311.07552

- On the $H_0$ tension: {cite:t}`Riess2022` and <doi:10.1016/j.physrep.2022.07.001>

:::




[^bolo]: A bolometric sensor is capable of absorbing photons and measuring their energy regardless of their wavelength (for example by measuring the heating of a material). In contrast, a photonic sensor based on the photoelectric effect becomes transparent at long wavelengths, when the photon energy falls below the electron emission threshold.

[^Sfreq]: Or in frequency $S_\nu(\nu)$ expressed in W/m$^2$/Hz.

### Measuring parallax

When a foreground star is observed from two opposite positions, A and B, in the Earth's orbit around the Sun, it appears to move relative to the background field of stars towards positions A‘ and B’. This apparent shift is called parallax. The distance between the Earth and the Sun is defined as an astronomical unit (AU), i.e. the average between the two half-axes of the Earth's elliptical orbit. Using this distance, and by measuring the apparent displacement of the star's position, we can trigonometrically calculate the distance between the observer and the star. This phenomenon is known as parallax. The parallax measurements made by Gaia reach an accuracy of 0.04 marcsec (Luri et al., 2018). This method constitutes the first rung of the cosmic distance scale.

### Cepheids

Cepheids are a type of star that pulses radially, undergoing regular variations in diameter and temperature. These pulsations result in changes in luminosity with a well-defined and stable period and amplitude. They were discovered by Henrietta Swan Leavitt (Leavitt, 1908), who demonstrated the correlation between the star's diameter and temperature.

The luminosity of a cepheid and its pulsation period. This law is known as Leavitt's law, and Figure 1.16 from Leavitt and Pickering, 1912, illustrates this relationship.
By observing the Cepheids close enough to use the parallax method for distance estimation, we can calibrate the absolute magnitude of the Cepheids, and hence their period-luminosity function. Because of the stability of their period-luminosity function, this calibration can then be applied to all Cepheids, allowing us to measure their luminosity distance in other galaxies where the parallax method is not feasible. As a result, Cepheids serve as the first standard candle in the cosmic distance scale, allowing us to determine the distance to other galaxies, as shown in the graph at bottom left of Figure 1.17.



### Type Ia supernovae

Once the period-luminosity function of Cepheids has been calibrated, we want to transfer this calibration to SNe Ia. To estimate the distance to a galaxy using a Cepheid, the Cepheid must be resolved with respect to the other light sources in the galaxy, and its photometry must be carried out. By measuring its period of variation, we can deduce its intrinsic luminosity, and therefore the distance to the host galaxy. 

Then, by observing an SN Ia in the same galaxy, we can determine its intrinsic luminosity, since the distance is known via the cepheid. Riess et al, 2022 observed 42 SNe Ia in 37 calibrated hosts. These SNe Ia are represented in the middle graph of Figure 1.17, which makes it possible to calibrate the absolute magnitude of the SNe Ia. Finally, the top-right plot shows a Hubble diagram of the SNe Ia, which is directly related to the estimation of the geometric distance using the parallax method. With this sample, Riess et al. 2022 obtained a measurement of $H_0$ of $73.04 \pm 1,04\,$km/s/Mpc.



[^bolo]: A bolometric sensor is capable of absorbing photons and measuring their energy regardless of their wavelength (for example by measuring the heating of a material). In contrast, a photonic sensor based on the photoelectric effect becomes transparent at long wavelengths, when the energy of the photon falls below the emission threshold of an electron.

[^Sfreq]: Or frequency $S_\nu(\nu)$ expressed in W/m$^2$/Hz.