---
short_title: Type Ia supernovae
authors:
  - jneveu
keywords: supernovae, Hubble diagram, $H_0$
---

Type Ia supernovae
===================

There are two types of cosmological measurement: distance measurements, which map the expansion history of the Universe, and structure growth measurements, which describe the evolution of the Universe's large-scale structures. The former are simple data that ultimately amount to measuring the evolution of the Hubble parameter $H(z)$. Two methods are used. The first method, which has been used historically, uses standard candles, via type Ia supernovae. If we know that a category of astrophysical objects all have the same intrinsic luminosity, then if this object appears faint, it is located far away and we can deduce its distance from its apparent luminosity. The second method uses a standard rule, i.e. an invariant characteristic length that can be measured throughout the history of the Universe. If this length appears smaller than it is today at a certain redshift $z$, then knowing that it must not have evolved (or knowing how it evolved), we can find out its distance. This method is used in baryonic acoustic oscillations and the measurement of the angular power spectrum of the cosmic microwave background. The principle behind these two methods is illustrated [](#fig:candles).

:::{figure} ../../images/chandelles.jpg
:name: fig:chandelles
:align: center
:width: 80%

Principle of the measurement of the expansion of the Universe using standard candles (type Ia supernovae) and a standard rule (average distance between galaxies, derived from the average distance between overdensities of the cosmic microwave background).
:::


Principle of the standard candle method
-----------------------------------

The standard candle method is based on measuring the luminous fluxes from stars of identical intrinsic luminosity. To measure the speed of expansion of the Universe, we need luminosity distances associated with redshifts and thus construct a Hubble-Lemaître diagram. 

The <wiki:Apparent_magnitude> is a logarithmic scale that measures the luminosity of an object observed from Earth. It is based on the measurement of a luminous flux $\Phi_{0}$ acquired with a telescope equipped with a photosensitive sensor ($\gamma$/s/m$^2$) or a bolometer (W/m$^2$), compared with a reference flux $\Phi_{\rm ref}$ which sets the scale. Historically, the scale was based on a standard star, Vega in the constellation Lyra. To tie in with the 6 categories of magnitudes defined in ancient times, the apparent magnitude of a star is defined by :
\begin{equation}
m = -2.5\log_{10} \left[\frac{\Phi_{0}}{\Phi_{\rm ref}} \right] 
\end{equation}
The absolute magnitude is the flux we would receive from this source at a distance of $10,\parsec$ :
\begin{equation}
M = -2.5\log_{10} \left[\frac{L}{4\pi (10\,\parsec)^2\Phi_{\rm ref}} \right] 
\end{equation}

:::{note} Magnitudes

The classification of the brightness of stars into magnitudes comes from Antiquity, and therefore from visual observation. Between stars of magnitude 0 and 5, there is a ratio of one hundred to one hundred in luminous flux, the fainter magnitude stars being the brighter. The flux is therefore divided by a factor of 2.5 between each magnitude.
:::

In an ideal world, it would be enough to measure the $\Phi_{0}^{(i)}$ fluxes of a collection of $N$ standard candles at $z_i$ redshifts and compare them to obtain a relationship between luminosity distance and redshift. The apparent magnitude $m_i$ of a standard candle at redshift $z_i$ is related to the expansion rate $H(z)$ via the luminosity distance:
\begin{align*}\label{eq:utopia}
m_i & = -2.5\log_{10} \left[\frac{ \Phi_{0}^{(i)}}{\Phi_{\rm ref}}\right] \\
& = -2.5 \log_{10}\left[ \frac{L}{4\pi D_L^2(z_i) \Phi_{\rm ref}}\right] \\
& = 5 \log_{10}\left[ \frac{D_L(z_i)}{10\,\parsec}\right] + M
\end{align*}
The quantity :
\begin{equation}
\mu = 5 \log_{10} \left[ \frac{D_L(z_i)}{10\,\parsec}\right] = 5 \log_{10} \left[\frac{(1+z)}{10\,\parsec} \int_0^z \frac{\dd z}{H(z)} \right] \text{ si } k=0
\end{equation}
This is the decrease in luminosity in magnitude related to the distance from the star. If a standard candle is 2 times further away then it appears 4 times less bright and its distance modulus increases by 1.5 magnitudes. By measuring the fluxes, we can estimate the relative distances between standard candles.

The most important point to note in this formula is that the cosmological expansion speed $H(z)$ is inscribed in the shape of the $\mu(z)$ curve, and not in its normalisation (which can therefore be a free parameter of the model). Standard candles can be used to measure the expansion properties of the Universe, but it is not necessary to know their absolute luminosity $L$! But if we do know their absolute luminosity $L$, then we can establish a scale of absolute distances and the normalisation of the Hubble diagram gives access to the value of $H_0$ ([](#fig:distmod)).

:::{figure} #distmod
:name: fig:distmod
:align: center
:width: 70%

Distance modulus as a function of redshift for three cosmological models. A change in the parameters $\Omega_i^0$ modifies the shape of the curve while the parameter $H_0$ modifies its normalisation.
:::





Hubble diagram of supernovae
-----------------------------------

To establish a Hubble diagram at cosmological distances, we need sources of identical luminosity that are visible at very great distances. Galaxies are too variable in size and intrinsic luminosity to play this role. However, supernovae are stellar explosions whose luminosity is commensurate with that of a galaxy, so they are visible from a great distance.

### Type Ia supernovae

Supernovae are classified into two types: gravitational and thermonuclear. Gravitational supernovae are the best known: they are the result of the explosion of a massive star (more than 8 times the mass of the Sun) at the end of its life, leaving a dense, cold stellar core: a neutron star, or even a black hole in extreme cases. Type I supernovae have no hydrogen lines in their spectrum, while Type II supernovae do. Among Type I supernovae, those containing silicon are Type Ia, followed by Ib and Ic.

Stars with a mass of less than $8\,M_\odot$ end their lives as red giants. At the end of the helium burn, the outer layers are dispersed into the interstellar medium in the form of planetary nebulae (without necessarily producing an intense explosion), leaving the stellar core bare. The collapse of the core is halted by the degeneracy pressure of the electrons (rather than neutrons as in neutron stars) and its low mass (typically $0.5\,M_\odot$). Its surface temperature remains very high for a long time (around $10\,000\,\kelvin$), hence its name of white dwarf. It is composed mainly of carbon and oxygen, the helium and hydrogen having been expelled into space. The typical radius of such an object is a few thousand kilometres (like a terrestrial planet). 
 
:::{figure} ../../images/Type_Ia_Supernova_When_a_White_Dwarf_Steals_Material_from_Companion.mp4

This animation shows the explosion of a white dwarf, the extremely dense remnant of a star that can no longer burn nuclear fuel in its core. In this Type Ia supernova, the white dwarf's gravity steals matter from a nearby stellar companion. When the white dwarf reaches a mass estimated at 1.4 times the current mass of the Sun, it can no longer support its own weight and explodes. Credit: NASA/JPL-Caltech
:::


According to a study by the Very Large Telescope, around 75% of massive stars are {cite:p}`Sana2012` binary systems. In some cases, a white dwarf can be gravitationally linked to another star, which, if it is close enough, can see its outer layers sucked in by the white dwarf's gravity. When the white dwarf has accumulated too much matter from its neighbour and approaches the Chandrasekhar mass ($1.4\,M_\odot$), it becomes unstable. The pressure and temperature conditions at the core of the white dwarf allow carbon fusion to reignite. The white dwarf is unable to expand due to the degenerating pressure and thus cool down, so the reaction ignites into a thermonuclear flame that vaporises the star in a few seconds, enriching the interstellar medium with intermediate mass elements (oxygen, calcium, magnesium, silicon, sulphur) and elements from the iron family (nickel, cobalt). However, this explosion scenario remains only a hypothesis, as there is as yet no evidence for it. Other scenarios exist, such as the merger of two white dwarfs {cite:p}`Nomoto2013`.

SNe Ia draw their energy from the decay of iron-group elements that were produced during the explosion <doi:10.1086/150102>. The main radioactive element formed is $^{56}_{28}\text{Ni}$ :
\begin{equation}
2\ ^{12}_{\ 6}\mathrm{C} + 2\ ^{16}_{\ 8}\mathrm{O} \rightarrow ^{56}_{28}\mathrm{Ni}
\end{equation}
The nickel isotope $^{56}_{28}\text{Ni}$ then decays to $^{56}_{27}\text{Co}$ with a half-life of 6.1 days, which in turn decays to stable iron $^{56}_{26}\text{Fe}$ with a half-life of 77.3 days: 
\begin{equation}
^{56}_{28}\mathrm{Ni} \rightarrow ^{56}_{27}\mathrm{Co} \rightarrow ^{56}_{26}\mathrm{Fe}
\end{equation}
The total luminosity is estimated at $10^{10}\,L_\odot$, i.e. about that of a galaxy (see photographs [](#fig:sn) and [](#fig:sn2)). These objects are therefore a priori visible at cosmological distances. Since the explosion occurs systematically at the same stellar mass, roughly the same amount of material is ejected into space and emits the same amount of light. What's more, since the composition of white dwarfs is very standard, the composition of the emitting material is the same. So they all have more or less the same intrinsic total luminosity. However, they are also transient events: the duration of a supernova is a few tens of days. To catch a supernova, you need to look up at the right place at the right time.


Type Ia supernovae (SNe Ia) were the first cosmological probes to measure the expansion of the Universe over long distances, and to discover its accelerated expansion {cite:p}`Riess1998; Perlmutter1999`. The Nobel Prize in Physics was awarded in 2011 to Saul Perlmutter, Brian Schmidt and Adam Riess for this major discovery. 

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


:::{iframe} https://www.youtube.com/embed/350HR7Z8OYw?si=luHEY7x1g1TQDKvd
:width: 100%

This is a real footage of the type Ia supernova explosion. The supernova, SN 2015F, occurred in NGC 2442 galaxy in early March, 2015, at a distance about 80 million light years away from the earth. Daily cadence images from Feb. 2015 through Oct. 2015, were combined to create the movie. Images were taken with a robotic 17-inch telescope in Australia. Our analysis suggests that this explosion was possibly caused by the interaction between a white dwarf star and a main sequence star with a size of 0.1 - 1.0 times the sun.
:::

A Type Ia supernovae remains visible for around 40 days in the visible sky. To recognise its type, you need to observe it in several colours and, if possible, acquire its spectrum. A sequence of spectra acquired from a type Ia supernova is shown [](#fig:spectresIa).

:::{figure} ../../images/timeseries.pdf
:name: fig:spectresIa
:align: center
:width: 70%

Spectro-temporal series of SN2011fe measured by the SNfactory {cite:p}`Pereira2013` survey. The names of the main components of the spectrum are shown at the top of the figure.
:::


:::{figure} ../../images/lc.pdf
:name: fig:lightcurves
:align: center
:width: 70%

Light curves synthesised SN~2011fe using the UBVRI$_\mathrm{SNf}$ {cite:p}`Pereira2013` filter set. Filled and open symbols correspond to photometric and non-photometric nights respectively. The results of a simultaneous SALT2 fit of UBVR$_\mathrm{SNf}$ in the range of in the phase interval $-\,16 < t < +\,25$~d are represented by solid lines, with the corresponding residuals (SALT2 - SNf) on the lower panel. The shaded areas represent the error of the SALT2 model. The break in the time axis corresponds to the difference of $\sim 50$ days in the follow-up during which SN~2011fe was not visible at night from Hawaii. Note the change in scale of the extended time axis covering the late observations.
:::

In practice, we do not have spectral sequences as precise as the one shown [](#fig:spectraIa) for each supernova detected, as this costs too much observing time on the world's largest telescopes equipped with spectrographs. Only the SNFactory survey has dedicated a spectrograph to the systematic spectral study of supernovae. As a general rule, if possible, a spectrum of the supernova is acquired only at its maximum luminosity (because this is easier) in order to check that it is indeed a type Ia (identification spectrum), with a spectrograph that does not need to have high resolution to identify the main lines of the thermonuclear explosion. Later, a spectrum of the host galaxy is taken to measure its redshift precisely if it is not already known, with a higher resolution spectrograph (redshift spectrum).

The main information available on a type Ia supernovae is therefore its light curve, i.e. the temporal sequence of luminous fluxes, measured by a telescope with different band-pass filters fitted to the telescope's camera [](#fig:lightcurves). 

:::{note} Photometric systems

```{figure} ../../images/photometric_systems.png
:name: fig:photsyst
:align: center
:width: 70%

Band-pass filters for different photometric systems {cite:p}`Bessell2005`.

```

Astrophysical and cosmological photometric surveys are interested in measuring the colour of objects in order to gain access to their physical properties. To do this, telescopes are equipped with band-pass filters, the shapes and positions of which depend on the technologies used and the needs of the survey.

A standard photometric system is defined by a list of standard magnitudes and colours measured at specific bandwidths for a set of stars well distributed across the sky. The observed magnitudes are corrected for the attenuation of the Earth's atmosphere away from the zenith, and the data is then normally extrapolated to zero air mass (outside the atmosphere). 

The UBV system is one of the oldest and most widely used standard photoelectric photometric systems <doi:10.1086/145697>. The B-band was designed to approximate the raw photographic magnitude (minus UV), while the V-band was designed to approximate the visual magnitude system. The photometric systems of the modern SDSS and LSST surveys use instead interference filters called ugrizy in the visible and near infrared.

:::


It is therefore necessary to define an instant at which to compare the brightness of standard candles and a reference filter. For practical reasons, the magnitudes at maximum emission are used as a reference. For historical reasons, the Johnson B band is used as the reference filter. The magnitude of the maximum luminosity of a Type Ia supernovae observed in B-band is therefore used as the standard candle, or at least one that can be standardised.

### Rest frame magnitude

The luminous fluxes $\Phi$ expressed in ($\gamma$/s/m$^2$) or (W/m$^2$) are said to be bolometric [^bolo] because they are integrated over the whole spectrum. Unfortunately, the ability to measure this quantity depends on the sensor used. In the visible and infrared, sensors are based on the photoelectric effect, so they are transparent above a certain wavelength, so the fluxes measured cannot be bolometric. 

In addition, a great deal of information can be derived from measuring the colour of an object, such as the type of supernova: to do this, you need to observe it through different filters and compare the fluxes. 

We introduce the spectral energy density of a star $S_\lambda(\lambda)$ expressed [^Sfreq] in W/m$^2$/nm. The luminous fluxes are observed by telescopes equipped with filters having different bandwidths. Let's denote $T_b(\lambda)$ the transmission of the instrument in the $b$ band. The measured flux is then:
\begin{equation}
\Phi_{0,b} = \int \frac{\dd \lambda}{hc/\lambda} S_\lambda(\lambda) T_b(\lambda) \text{ in $\gamma$/m$^2$/s}
\end{equation}
where $\lambda$ is the observed wavelength. The definition of apparent magnitude in the $b$ band then becomes :
\begin{equation}
m_b = -2.5 \log_{10} \left[ \frac{ \int \lambda \dd \lambda S_\lambda(\lambda) T_b(\lambda) }{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_b(\lambda)}\right]
\end{equation}
where $S_{\mathrm{ref}}(\lambda)$ is the spectral flux density of the reference source (Vega for example). The absolute magnitude in band $b$ is the magnitude of the star in band $b$ if it were observed in its reference frame at rest at $10\,\parsec$ :
\begin{equation}
M_b = -2.5\log_{10} \left[\frac{1}{4\pi (10\,\parsec)^2} \frac{ \int \lambda \dd \lambda L_\lambda(\lambda) T_b(\lambda)}{ \int \lambda \dd \lambda \Phi_{\mathrm{ref}}(\lambda)T_b(\lambda) } \right] 
\end{equation}
where $L_\lambda$ is the spectral luminosity (in W/nm). 

Let $B(\lambda)$ be the transmission of the B band (in the Johnson UBV photometric system). Then we pose:
\begin{equation}
m_B^* = -2.5 \log_{10} \left[ \frac{\int \lambda \dd \lambda S_{\lambda}(\lambda) B(\lambda) }{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) B(\lambda)}\right]
\end{equation}
The absolute magnitude in band $B$ is :
\begin{equation}
M_B = -2.5\log_{10} \left[\frac{1}{4\pi (10\,\parsec)^2} \frac{\int \lambda \dd \lambda L_\lambda(\lambda) B(\lambda)}{\int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) B(\lambda)}   \right] 
\end{equation}
 
However, not all telescopes are equipped with a B filter. Furthermore, and this is the main reason, the emission maximum shifts in wavelength with the redshift, so the B filter would have to be redshifted to capture the same part of the spectrum ([](#fig:snIaB)). Since we only want to compare the effect of distance in order to map $D_L(z)$, these wavelength shift effects must be removed in order to standardise and compare the observed flux at maximum emission. Historically, for type Ia supernovae, cosmologists have established apparent magnitudes in B band _in the rest frame_. The magnitude $m_B^*$ is therefore the apparent magnitude in the B-band reference frame at rest, _as if there were no expansion but only a distance effect_.

The standard candle is the maximum emission of type Ia supernovae in the $B$ band as if it were observed in the reference frame at rest.


:::{figure} ../../images/snIa_restframeB.png
:name: fig:snIaB
:align: center
:width: 100%

Apparent magnitude in $B$ band for supernovae at different redshifts: they correspond to the integral of the spectral density of the supernova at its maximum in the redshifted $B$ band.
:::

As it is not possible to make an observation in the supernova's rest frame of reference, this magnitude $m_B^*$ must be obtained by calculation from observations in any b-bands and a spectrophotometric model of the supernova.

### Spectrophotometric model

The spectrophotometric model is the spectral density as a function of time $S_\lambda(\lambda, t)$, determined from the data (the collection of light curves and spectra available). Let's assume that we are able to obtain it, after training on the data, as with the SALT2 {cite:p}`Guy2007` model. How can we transform the observed apparent magnitudes into B-band magnitudes in the rest frame?

First of all, we need to study the effect of redshift on spectral densities.
The flux $\Phi_{0}$ and the intrinsic luminosity $L$ (in W) of a star at redshift $z$ can be written as :
\begin{equation}\label{eq:boloPhiL}
\Phi_{0} = \frac{L}{4\pi D_L^2(z)}
\end{equation}
where $D_L(z)$ is the luminosity distance. All photons received in a narrow logarithmic frequency range centred on the observed wavelength $\lambda_0$ were emitted in an equally narrow centred wavelength range centred on $\lambda_E = \lambda_0 / (1+z)$. Equation [](#eq:boloPhiL) thus relates the spectral flux densities to the spectral luminosities in the presence of a $z$ {cite:p}`Condon2018` redshift:
\begin{align}
\dd \lambda_0 S_\lambda(\lambda_0) & = \frac{\dd \lambda_E L_\lambda(\lambda_E)}{4 \pi D_L^2 (z)} = \frac{\dd \lambda_0}{1+z}\frac{ L_\lambda(\lambda_0/(1+z))}{4 \pi D_L^2 (z)} \notag \\ 
& \Rightarrow S_\lambda(\lambda_0) =\frac{L_\lambda(\lambda_0/(1+z))}{4 \pi (1+z) D_L^2 (z)} 
\end{align}
This relationship gives the link between the spectral flux density observed at $\lambda_0$ and the spectral luminosity density emitted at $\lambda_E$.

Now let's look at how we can transform the observed magnitudes into $m_B^*$ magnitudes, using the definition of apparent magnitude in b-band:
\begin{align*}
m_b & = -2.5 \log_{10} \left[ \frac{ \int \lambda \dd \lambda S_\lambda(\lambda) T_b(\lambda) }{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_b(\lambda)}\right] \\
& = -2.5 \log_{10} \left[\frac{1}{4 \pi (1+z) D_L^2 (z)} \frac{ \int \lambda \dd \lambda L_\lambda(\lambda/(1+z)) T_b(\lambda) }{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_b(\lambda)}\right]
\end{align*}
Let $K_{bB}$ be the _$K$-correction_ in $b$ bands and $B$ {cite:p}`hogg2002k` :
\begin{align*}
K_{bB} & = -2.5\log_{10} \left[\frac{1}{(1+z)} \frac{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) B(\lambda)}{ \int \lambda \dd \lambda S_{\mathrm{ref}}(\lambda) T_b(\lambda)}  \frac{ \int \lambda \dd \lambda L_\lambda(\lambda/(1+z)) T_b(\lambda) }{ \int \lambda \dd \lambda L_\lambda(\lambda) B(\lambda)}\right]
\end{align*}
So the apparent magnitude can be broken down into three terms:
\begin{align*}
m_b & = M_B + \mu(z) + K_{bB}(z) 
\end{align*}
and the magnitude $m_B^*$ is calculated from the observations $m_b$ and the calculated $K$-correction:
$$ \boxed{m_B^* = m_b - K_{bB}}$$
The $K$-correction represents the correction in magnitude that would be required if we were to observe the star in its rest frame and with a different filter. After applying the $K$-correction, the Hubble diagram is simply modelled by :
\begin{equation}
\boxed{m_B^*(z) = m_b - K_{bB}(z) = M_B + \mu(z)}
\end{equation}
an equation very similar to [](#eq:utopia). The left-hand side represents the magnitudes acquired by the telescope and transformed into the $B$ band at rest and at maximum. The right-hand side represents the cosmological explanatory model. For SNe Ia, $M_B = -19.08 \pm 0.03$ {cite:p}`Betoule2014`. We can therefore see that the distance dependence is entirely contained in the distance modulus $\mu(z)$, but note that there is an additional redshift dependence in the $K$-correction that must be modelled correctly to avoid introducing bias into the Hubble diagram. 

Unfortunately, the $K$-correction depends on a number of ingredients that we need to know in order to calculate it:
- the redshift $z$, to be inferred from a spectrum;
- the spectral density $S_\lambda$ of the supernova, to be constructed by a spectrophotometric model fitted to the measured spectral sequences (as in [](#fig:spectresIa)) such as SALT2 {cite:p}`Guy2007`;
- the reference spectral density $S_{\mathrm{ref}}(\lambda)$, to be established by measurement (<doi:10.1086/153547>, <doi:10.48550/arXiv.2411.03256>) or stellar atmosphere modelling <doi:10.1086/677655>;
- the transmission of the telescope filters $T_b$, or even the atmospheric transmission of the location $T_{\mathrm{atm}}(\lambda)$.

To obtain a measurement of the dark energy state parameter $w_{DE}$ to the percent, each of these ingredients must therefore be established to better than the percent. Today, the dominant uncertainties in the measurement of $w_{DE}$ by type Ia supernovae are the systematic uncertainties in photometric calibration, i.e. knowledge of the bandwidth of the instrument filters and knowledge of the reference fluxes {cite:p}`Betoule2013,Scolnic2018` .

#### Standardisation

After $K$-correction, we can compare the $m_B^*$ magnitudes with a cosmological model. Using the JLA data from the SuperNova Legacy Survey, we obtain the Hubble diagram [](#fig:hubblemb).

:::{figure} #hubbleDiagramMb
:name: fig:hubblemb
:align: center
:width: 70%

Hubble diagram of the 740 SNeIa from the SNLS survey, compared to a $\Lambda$CDM model with $\Omega_m^0 = 0.3$ and $\Omega_\Lambda^0=0.7$.
:::

Around the diagram, we observe that the residuals on the Hubble diagram have a dispersion of $0.4\,$mag, greater than the measurement errors. If we plot these residuals as a function of the colour $c=B-V$ or the normalised duration $x_1$ of the supernova, we see that they are correlated ([](#fig:hubbleRes)). 

:::{list-table} Residuals in the Hubble diagram coloured as a function of the normalised duration $x_1$ (left) or the colour $c=B-V$ (right).
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

So there is a variability in supernovae that has not been taken into account in our spectrophotometric model until now.

We observe that the longer the light curve lasts, the brighter it is at its maximum (the *brighter-slower* rule). In addition, the bluer the SNIa, the brighter they are too (*brighter-bluer* rule). There is also an environmental effect that links the brightness of the supernova to the mass of the host galaxy.

:::{figure} ../../images/courbes_de_lumiere_x1c.png
:name: fig:curbes_de_lumiere_x1c
:align: center
:width: 60%

SNe Ia light curves from the SNLS JLA dataset coloured as a function of $x_1$ or $c$ {cite:p}`nicola2022`.
:::


Light flux is related to nickel production and decay $^{56}$Ni. The two relationships presented above can thus be explained qualitatively: the more $^{56}$Ni the SNIa produces, the brighter it will be and the more blue-emitting FeII and CoII ions it will contain, but also the more opaque it will be (so the emission of photons by diffusion will be delayed, so the SNIa will shine longer) {cite:p}`Kasen2007`.

SNe Ia are therefore not so standard, because their light curves depend on the amount of $^{56}$Ni available at the origin. Nevertheless, without correcting for this intrinsic dispersion, the teams of the Supernova Cosmology Project (SCP) led by Saul Perlmutter and the High-z Supernova Search Team led by Brian Schmidt have been able to demonstrate the existence of an accelerated expansion {cite:p}`Riess1998; Perlmutter1999`. This dispersion is a problem for improving measurements of the expansion of the Universe at the percentage level. Nevertheless, it can be described empirically by two linear relations for $x_1$ and $c$ with coefficients $\alpha$ and $\beta$ respectively. For the mass of the host, we adjust a parameter $\delta M_{host}$ increasing the magnitude for supernovae located in galaxies of mass greater than $10^{10}\,M_\odot$.

These three empirical relationships add three additional parameters $\alpha$, $\beta$ and $\Delta M_{host}$ to be fitted to the data:
\begin{equation}
\boxed{m_{B,corr}^* = M_B + \mu -\alpha x_1 + \beta c + \Delta M_{host}}
\end{equation}
but after that the dispersion in the Hubble diagram is reduced to $0.15\,$mag which increases the precision of the constraints on the expansion of the Universe.


:::{figure} ../../images/HD_jla.pdf
:name: fig:HD
:align: center
:width: 70%

Hubble diagram of supernovae in the JLA catalogue. The black curve represents a $\Lambda$CDM model fitted to the data. A model without dark energy would appear significantly below the curve described by the data ($-0.6\,$mag at $z=1$).
:::

:::{note} Origin of $\delta M_{host}$

Indeed, it seems that massive galaxies contain much more metal and that supernovae can appear brighter in them than in light galaxies (see the discussion in section 5.5 of reference {cite:p}`Sullivan2010`). As suggested by reference {cite:p}`Sullivan2010`, we divide the data into two batches according to the mass of the host galaxy. 
:::



### Calibrations

:::{figure} ../../images/strategy1.png
:name: fig:SNCalib
:align: center
:width: 70%

Strategies for calibrating the luminous flux of tertiary stars (secondary stars are not shown). The redshifted $B$ band is represented by a thick blue line on the spectra of SNe Ia. 
:::

### State of the art





Local measurement of $H_0$ (draft)
------------------------

The $\mu$ distance module makes it possible to measure the relative distance between SNe Ia, which provides crucial information about dark energy, as we will see in the section ? However, the absolute distance of SNe Ia cannot be obtained by this method, because the luminosity distance depends on the value of $H_0$. Consequently, there is a degeneracy between the luminosity of the SNe Ia and $H_0$ when estimating $M_B$. To break this degeneracy, the cosmic distance scale is used. This method involves a series of overlapping distance measurements using various astronomical objects and techniques, as illustrated in Figure 1.17 of Riess et al. (2022). By anchoring the distances of SNe Ia to distances measured independently by the cosmic distance scale, we can disentangle the absolute magnitude of SNe Ia from that of H0. In what follows, we will discuss the various stages of this distance scale.

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