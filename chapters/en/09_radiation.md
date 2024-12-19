---
short_title: Radiative processes
authors:
  - jbiteau
keywords: radiation
---

Radiative processes
=============================================


General considerations
--------------------------------

Radiative processes are crucial to the study of cosmic-ray acceleration for two reasons.
1. As energy losses, they limit the maximum energy reached by astrophysical accelerators (cf. diffusion-loss equation [](08_acceleration.md#eq_FokkerPlanck));
2. As a mechanism for producing neutral secondary particles (neutrinos, gamma-rays, neutrons) that can more easily 
   escape the magnetized regions where cosmic-ray electrons, protons and nuclei are accelerated.

Stable neutral secondary particles (neutrinos, gamma-rays) are not deflected by intervening magnetic fields 
(in the interstellar medium, the galactic halo, the cosmic web) and thus trace the direction of the astrophysical 
accelerators more 
robustly than the primary charged particles. 

Different loss mechanisms should be considered depending on whether the cosmic ray interacts with ambient protons 
(and helium nuclei), photons, or magnetic fields. For a given cosmic-ray species (e.g. electrons), the comparison of 
loss time scales, $\left[ \frac{1}{p} \frac{\dd p}{\dd t}\right]^{-1}$, or loss lengths, $\left[ \frac{1}{p} \frac{\dd p}{\dd x}\right]^{-1}$, allows us 
to identify the main channels of secondary-radiation production and to model them in detail as a function of energy. 

As the losses accumulate following $\dot p_\text{loss} = \sum_{i \in \text{processes}} \dot p_i$, the overall loss 
timescale is

$$
\begin{align}
t_\text{loss} &= \frac{p}{\dot p_\text{loss}} \\
& = \frac{p}{\sum_{i \in \text{processes}} \dot p_i} \\
& = \frac{1}{\sum_{i \in \text{processes}} t_i^{-1}}. 
\end{align}
$$
As expected, the fastest losses (i.e. the ones with the shortest $t_i$) dominate the fate of the primary particle.

When multiple cosmic-ray species are present (e.g. co-acceleration of electrons and protons), we have to identify 
the main losses for each species and account for the relative energy throughput per particle as well as for the 
number of particles per primary species. Radiative processes are divided in two main categories, hadronic and 
leptonic, depending on the nature of the primary ($p$ or $^{A}_{Z}X$ versus $e^-$ or $e^+$).

Hadronic processes
--------------------------------

### Spallation and $p$-$p$ processes

The baryonic composition of the interstellar medium and of the cosmic web is dominated by hydrogen (about half 
molecular, H$_2$, and half atomic, as neutral HI or ionized HII in the Milky Way) and helium (about $10\,\%$ in 
number, that is $40\,\%$ in mass in the Milky Way, see {cite}`1990ASSL..161...39B`).

In dense environments, such as molecular clouds near supernova remnants and the circum nuclear medium of starburst 
galaxies, proton-proton ($p$-$p$) and spallation processes can be dominant (see e.g. timescales in {cite}`2023PhRvD.107h3009C`). 
Nearly all intermediate-mass nuclei such as Li-Be-B, are produced by spallation. Leaving such nuclei 
aside, the throughput of $p$-$p$ and spallation processes is dominated by neutrons and protons, which in turns 
mainly interact through:
\begin{align}
n+p &\rightarrow p+p+\pi^-\\
p+p &\rightarrow p+p+\pi^0\\
p+p &\rightarrow p+n+\pi^+
\end{align}

:::{note}
It is fair to ask whether the cross sections of the hadronic processes we study are well known, especially for 
cosmic rays whose energy per nucleon is of the order of $E/A = 10^{18}\,$eV. The interaction of a proton at $E = 1\,
\text{EeV}$ with a hydrogen nucleus at rest, of energy $m_p c^2$, corresponds in the centre of mass to an energy 
per proton 
of $\sqrt{E m_p c^2/2} \approx 20\,\text{TeV}$. In practice, this is very close to the energy scale of human-made 
accelerators 
such as the LHC.
:::

The three types of pions are produced in a ``democratic'' fashion by $p$-$p$ interactions, so that the average 
number of charged pion per neutral pion produced in these interactions is
\begin{align}
&K_\pi \equiv \frac{N_{\pi^\pm}}{N_{\pi^0}}\\
\text{with } &K_\pi(p-p) \approx 2
\end{align}

The subsequent decay of pions leads to the production of neutral secondaries:
\begin{align}
\pi^0 &\rightarrow \gamma \gamma\\
\pi^+ &\rightarrow \mu^+ + \nu_\mu \rightarrow e^+ + \nu_e + \bar\nu_\mu + \nu_\mu\\
\pi^- &\rightarrow \mu^- + \bar\nu_\mu \rightarrow e^- + \bar\nu_e + \nu_\mu + \bar\nu_\mu\\
\end{align}

Although neutrinos are produced in proportion $(\nu_e : \nu_\mu : \nu_\tau)|_\text{source} = (1 : 2 : 0)$, 
detection is expected in proportion $(\nu_e : \nu_\mu : \nu_\tau)|_\oplus = (1 : 1 : 1)$ due to neutrino oscillations.

:::{exercise} Neutrino and gamma-ray fluxes from an optically thin medium
:label: exo:neutrino_gamma_thin_medium

Given a ratio of charged to neutral pions $K_\pi$, compare the number flux and energy flux of gamma rays and 
neutrinos from a region transparent to these neutral secondaries. 

_Note:_ Because electrons and neutrinos have a negligible mass with respect to pions, one can safely assume that 
each of them carries a fourth of the energy of their parent charged pion.

:::

:::{solution} exo:neutrino_gamma_thin_medium
:class: dropdown

The interaction of a proton leads to the production of charged and neutral pions with branching ratios of $K_\pi/
(K_\pi+1)$ and $1/(K_\pi+1)$, respectively. This yields a number of neutrinos $N_\nu = \int\dd E_\nu \frac{\dd N_\nu}
{\dd E_\nu} = 3 N_{\pi^\pm} \propto 3  N_p K_\pi$ at energy $E_\nu = E_\pi /4 $ and of gamma rays $N_\gamma = 
\int\dd E_\gamma \frac{\dd N_\gamma}{\dd E_\gamma}= 2 N_{\pi^0} \propto 2 N_p $ at energy $E_\gamma = E_\pi /2 $.

The gamma-ray and neutrino number flux thus follow the relation:
$$
\int\dd E_\gamma \frac{\dd N_\gamma}{\dd E_\gamma} = \frac{2}{3K_\pi} \int\dd E_\nu \frac{\dd N_\nu}{\dd E_\nu}  
$$

The gamma-ray energy flux is $\int\dd E_\gamma \frac{\dd N_\gamma}{\dd E_\gamma}E_\gamma \propto 2N_p\frac{E_\pi}{2}
$ and the neutrino energy flux is $\int\dd E_\nu \frac{\dd N_\nu}{\dd E_\nu}E_\nu \propto 3K_\pi N_p\frac{E_\pi}{4}$,
from which we get
$$
\int\dd E_\gamma \frac{\dd N_\gamma}{\dd E_\gamma}E_\gamma = \frac{4}{3K_\pi}\int\dd E_\nu \frac{\dd N_\nu}{\dd 
E_\nu}E_\nu
$$

For $p$-$p$ interactions, $K_\pi \approx 2$ so that neutrinos are three times more numerous than gamma rays. 
Although individually the neutrinos are twice less energetic than gamma rays, they carry as a population a power $1.
5$  times larger than the gamma rays. 
:::

The relative energy loss of the primary nucleon is called the inelasticity of the reaction, $\kappa$. The average 
inelasticity per pion is thus defined as $\langle E_\pi \rangle = \kappa_\pi E_p$, with $\kappa_\pi \approx 20\,\%$ 
for $p$-$p$ interactions (also valid for $p$-$\gamma$ interactions discussed in the following, see {cite}`2018PrPNP.102...73A`).
This means that a population of $10\,\text{PeV}$ protons will produce on average $2\,\text{PeV}$ pions, which will decay in 
$1\,\text{PeV}$ gamma rays and $500\,\text{TeV}$ neutrinos. Note that while the neutrinos are likely to escape 
interactions in their environment and on their way to Earth, 
the  $1\,\text{PeV}$ gamma rays could easily interact along their path with lower-energy photons to produce pairs of 
electrons and positrons (see section dedicated to leptonic processes). While neutrinos and gamma-rays are expected 
to be produced in about equal proportion by hadronic processes, they are not necessarily expected to arrive at Earth in such 
proportions!  

### Photo-erosion and $p$-$\gamma$ processes

#### Photo-erosion

The photo-erosion process, also called photo-disintegration, describes the interaction of a nucleus with a 
photon:
$$
^{A}_{Z}X + \gamma \rightarrow ^{A-a-b}_{Z-b}Y + an + bp, 
$$
with $(a,b) \in \mathbb{N}^2$.

The Lorentz boost per nucleon is roughly conserved in such interactions. This is particularly true at the highest 
energies when the nuclei can be seen as a superposition of independent nucleons. 

In the nucleus rest frame, $\mathcal {R}'$, different nuclear/hadronic processes should be considered depending on 
the target photon energy (see {cite}`2006JCAP...09..005A`):  
- _Giant dipole resonance_ for $\epsilon_\gamma' \approx 10-20\,\text{MeV}$, i.e. a collective nuclear mode in which 
  the neutrons and protons oscillate in antiphase. The giant dipole resonance can lead, in the final state, to 
  the release of $n$, $p$, $2n$, $2p$, $np$, $\alpha$; 
- _Quasi-deuteron process_ for $\epsilon_\gamma' \approx 30\,\text{MeV}$, i.e. the interaction of the photon with a pair of 
  nucleons that can be released by the parent nucleus;
- _Baryon resonance_ for $\epsilon_\gamma' \gtrsim 150\,\text{MeV}$, i.e. the interaction of the photon with single 
  nucleons. This process is similar to the $p$-$\gamma$ and $n$-$\gamma$ processes discussed in the following 
  subsection. 

:::{note}
Because of the Lorentz boost of the nucleus, the target photons relevant to these process are the microwave 
and infrared photon fields in the radiation field of the cosmic accelerator or on cosmic scales (CMB and CIB). Indeed, 
for a primary nucleus of energy $E_{X} = A E_{p}$, the Lorentz-invariance of the four-momentum norm applied to the 
initial state, e.g. $p+\gamma$, leads to (adopting the convention $c=1$): 
\begin{align}
(E_p + \epsilon_\gamma)^2 - (\vec{p_p}+ \vec{p_\gamma})^2 &= (m_p + \epsilon_\gamma')^2 - (\vec{0}+ \vec{p_\gamma'})^2 \\
m_p^2 + 2E_p\epsilon_\gamma(1-\cos\theta) &= m_p^2 + 2m_p \epsilon_\gamma'\\ 
\epsilon_\gamma & = \frac{m_p \epsilon'_\gamma}{2E_p} \text{, for a head-on collision}
\end{align}


The relevant wavelength for the photon is
\begin{align}
\lambda_\gamma &= \frac{hc}{\epsilon_\gamma}\\
            &= 1.2\,\mu\text{m}\times \left(\frac{\epsilon_\gamma}{1\,\text{eV}}\right)^{-1}\\
            &= 2.4\,\mu\text{m}\times \frac{E_p}{m_pc^2} \left(\frac{\epsilon'_\gamma}{1\,\text{eV}}\right)^{-1}\\
            &= 240\,\mu\text{m}\times \left(\frac{E_p}{1\,\text{EeV}}\right) \left(\frac{\epsilon'_\gamma}{10\,\text
{MeV}} \right)^{-1}
\end{align}

A useful tip in the numerical application lies in noting that $hc = 2\pi\times \hbar c \approx 2\pi\times 197\,\text
{MeV}\,\text{fm} \approx 1.2\,\text{GeV}\,\text{fm} = 1.2\,\text{eV}\,\mu\text{m}$.

For an energy per nucleon $E_p = 2\,\text{EeV}$, a photon of the CMB with a wavelength of $480\,\mu\text{m}$ is seen 
as a $10\,\text{MeV}$ gamma rays in the rest frame of the nucleus, resulting in an interaction through the giant-
dipole-resonance channel. For the same energy per nucleon, the photons relevant to baryon resonance are $\frac{150\,
\text{MeV}}{10\,\text{MeV}} = 15$ times more energetic. They have 15 times smaller wavelengths, around $30\,
\mu\text{m}$, that is they are photons of the CIB.
:::

#### Photo-production of pions and pairs

The main interactions of a nucleon in a photon field are:
- the photo-production of pairs: 
  - $p+\gamma \rightarrow p + e^+ + e^-$
  - $n+\gamma \rightarrow n + e^+ + e^-$
- the photo-production of pions:
  - $p + \gamma \rightarrow p + \pi^0$ and $p + \gamma \rightarrow n + \pi^+$
  - $n + \gamma \rightarrow n + \pi^0$ and $n + \gamma \rightarrow p + \pi^-$

Note that the three pions are not produced in a ``democratic'' fashion in $p$-$\gamma$ processes, rather:
\begin{align}
&K_\pi \equiv \frac{N_{\pi^\pm}}{N_{\pi^0}}\\
\text{with } &K_\pi(p-\gamma) \approx 1
\end{align}

In the nucleon's rest frame, the threshold for pair and pion production are about $1\,\text{MeV}$ and $140\,\text{MeV}
$, respectively. The energy loss-length, $\lambda = \langle (\frac{1}{E}\frac{\dd dE}{\dd X})^{-1} \rangle$, depends on 
the 
product of the cross section and of the inelasticity (energy-loss fraction) of the reaction. This product, which is 
nearly constant at energies larger than a few times the threshold energy, is two orders of magnitude larger for pion 
production than for pair production, so that the former dominates over the latter at the highest energies.

The various loss processes relevant for the propagation of ultra-high energy cosmic rays on cosmological scales are 
illustrated in [](fig:UHECR_loss).

:::{figure}  ../../images/UHECR-mfp.png
:name: fig:UHECR_loss
:align: center
:width: 100%

Energy loss length of ultra-high-energy cosmic rays as a function of energy. Different nuclei are illustrated in 
different colors. The relevant processes are shown with different line styles.
:::

At the lowest energies, below $1\,\text{EeV}$, the losses are dominated by the 
so-called adiabatic cooling, which is driven by the expansion of the universe, indeed:
\begin{align}
t_\text{adiab} &= \left|\frac{1}{E}\frac{\dd E}{\dd t} \right|^{-1}\\
&= \left|\frac{1}{E}\frac{\dd E}{\dd z}\frac{\dd z}{\dd t} \right|^{-1}\\
&= \left|-\frac{(1+z)H(z)}{(1+z)}\right|^{-1}\\
&= 1/H(z)
\end{align}


:::{exercise} Threshold for photo-production of pions and for $\gamma\gamma$ pair production
:label: exo:threshold_energies

The photo-production pion and the production of $e^+e^-$ pairs are the dominant interaction channels for 
cosmic rays and gamma rays propagating on cosmological scales. 

1. Compute the threshold energy for the photo-production of pions, $p+\gamma \rightarrow p+\pi^0$, in a target photon 
   field at $\lambda_\gamma = 1\,\text{mm}$, which is close to the peak of the CMB.  

2. Compute the threshold energy for pair-production, $\gamma\gamma$ interaction $\gamma+\gamma \rightarrow 
   e^+ + e^-$, in a target photon field at $\lambda_\gamma = 1\,\mu\text{m}$, which is close to the peak of the COB.  

:::


:::{solution} exo:threshold_energies
:class: dropdown

As a refresher, two properties of the invariant mass are used when computing a threshold energy. First, the norm of 
the four-momentum is conserved in the reaction, i.e. it is the same in the initial and final states. Second, this 
norm is Lorentz invariant, which allows us to compute it in the rest frame for the final state rather than in the 
lab frame. The threshold energy is by definition such as the particles in the final state are produced at rest in 
the center-of-mass frame. In the following calculation, we adopt the convention $c=1$ for simplicity.

1. The conservation of the invariant mass for the reaction $p+\gamma \rightarrow p+\pi^0$ gives:
\begin{align}
(E_p+E_\gamma)^2 - (\vec{p_p}+\vec{p_\gamma})^2 &= (m_p + m_\pi)^2\\
m_p^2 + 2E_p E_\gamma(1-\cos\theta) &= m_p^2 + 2m_p m_\pi + m_\pi^2\\
E_p &\approx \frac{2m_p m_\pi}{2E_\gamma(1-\cos\theta)}\\
E_p &\gtrsim \frac{2m_p m_\pi}{4E_\gamma}
\end{align}
That is:
\begin{align}
E_{p,\text{ th}} &\approx \frac{m_p m_\pi}{2}\times \frac{\lambda_\gamma}{hc}\\
&\approx \frac{0.94\,\text{GeV}\times 140 \times 10^6\,\text{eV}\times 10^{3}}{2\times 1.2\,\text{eV} } \times \left
   (\frac
   {\lambda_\gamma}{1\,\text{mm}}\right)\\
&\approx 55\,\text{EeV} \times \left (\frac {\lambda_\gamma}{1\,\text{mm}}\right)
\end{align}

2. Similarly, for  $\gamma+\gamma \rightarrow e^+ + e^-$
\begin{align}
(E_\gamma+\epsilon)^2 - (\vec{p_\gamma}+\vec{p_\epsilon})^2 &= (2m_e)^2\\
2E_\gamma\epsilon(1-\cos\theta) &= 4m_e^2\\
E_\gamma &= \frac{4m_e^2}{2\epsilon(1-\cos\theta)}\\
E_\gamma &\geq \frac{4m_e^2}{4\epsilon}
\end{align}
That is:
\begin{align}
E_{\gamma,\text{ th}} &= m_e^2\times \frac{\lambda_\gamma}{hc}\\
&\approx \frac{0.511^2\,\text{MeV}^2}{1.2\,\text{eV} } \times 
   \left(\frac {\lambda_\gamma}{1\,\mu\text{m}}\right)\\
&\approx 220\,\text{GeV} \times \left(\frac {\lambda_\gamma}{1\,\mu\text{m}}\right)
\end{align}
:::

### Proton synchrotron

A particle of energy $E$, mass $m$ and charge $Ze$ emits synchrotron radiation in a magnetic field $B$. Averaged over 
the 
pitch 
angle $\theta$, such as $\cos\theta = \frac{\vec{\beta}\cdot\vec{B}}{\beta B}$, the synchrotron energy loss reads 
(see e.g. chapter 14 of {cite}`jackson_classical_1999`):
$$
\label{eq:sync_loss}
\left.-\frac{\dd E}{\dd t}\right|_\text{sync} = \frac{4}{3} \sigma c u_B \beta^2 \gamma^2, 
$$
with $(\gamma, \gamma\vec{\beta})$ the four-momentum of the particle and
\begin{align}
\sigma &= \frac{8\pi}{3} \left[ \frac{(Ze)^2}{ 4\pi\epsilon_0 mc^2} \right]^2\\
&= \sigma_\text{T} \times Z^4 \times \left( \frac{m}{ m_e} \right)^{-2}.
\end{align}

In the ultra-relativistic limit, $\beta \approx 1$ adopted hereafter, the synchrotron loss rate is thus
\begin{align}
t_\text{sync}^{-1} &= \left.-\frac{1}{E}\frac{\dd E}{\dd t}\right|_\text{sync}\\
&= \frac{4}{3} \frac{\sigma c u_B}{mc^2} \times \frac{E}{mc^2}.
\end{align}

Note that the synchrotron loss rate increases with energy and that, for a fixed Lorentz boost $\gamma = E/mc^2$, the 
rate goes as $1/m^3$. If the loss rate becomes dominant with respect to 
the acceleration rate, the maximum energy is limited by the losses (so-called synchrotron burn-off limit).

The synchrotron radiation is emitted as photons over a range of frequencies, $\nu$. The power emitted by a single 
proton per frequency unit reads
$$
\label{sync_power}
\left.P_\nu(\nu,\gamma)\right|_\text{sync} = \frac{4}{3} \sigma c u_B \beta^2 \gamma^2 \times f_\text{sync}\left( \frac{\nu}{\nu_\text{c}} 
\right),
$$
where $\int \dd \nu\,f_\text{sync}\left( \frac{\nu}{\nu_\text{c}}\right)=1$ so that $\left.P(\gamma)\right|_\text{sync} \equiv \int \dd 
\nu\, 
\left.P_\nu(\nu,\gamma)\right|_\text{sync} =  \left.-\frac{\dd E}{\dd t}\right|_\text{sync}$, and where the critical frequency, averaged over 
the 
pitch angle, is $\nu_\text{c} = \frac{3}{16} \frac{ZeB}{m} \gamma^2$.

The peak of the photon spectrum is at $E_\text{peak} = \alpha h\nu_\text{c}$, where $\alpha \approx 0.3$ corresponds 
to the maximum of $f_\text{sync}(x)$.[^1] Using the value of the nuclear magneton, $\mu_N = \frac{e\hbar}{2m_p} \approx \pi 
\times 10^
{-14}\,\text{MeV\,T}^{-1}$, one finds:
\begin{align}
\label{Epeak_sync}
E_\text{peak} & = \frac{3\pi\alpha}{4} \mu_N \times B\gamma^2 \times \left(\frac{m}{m_p}\right)^{-1} \left(\frac{Z}{1}
\right)\\
& \approx \frac{3\pi^2\times0.3}{4}\times 10^{-14} \times 10^{-4} \times 10^{18} \text{\,MeV} \times \left(\frac{B}{1\,
\text{G}}\right) \left(\frac{\gamma}{10^9}\right)^2 \left(\frac{m}{m_p}\right)^{-1} \left(\frac{Z}{1}\right)\\
& \approx 2.2\text{\,MeV} \times \left(\frac{B}{1\,\text{G}}\right)  \left(\frac{\gamma}{10^9}\right)^2  
\left(\frac{m}{m_p}\right)^{-1} \left(\frac{Z}{1}\right)
\end{align}

[^1]: The exact form of the function $f$, which depends on the survival function of the 
modified Bessel function of order $5/3$, is not necessary for the development of the argument. For more details, see 
{cite}`1986rpa..book.....R`.

Synchrotron emission from ultra-high energy protons at $10^{18}\,$eV in a magnetic field of $1\,\text{G}$ can thus 
end up as photons in the MeV range. This process has sometimes been invoked to explain the gamma-ray emission from 
the jetted active galactic nuclei. In the next section, we will look at alternative leptonic mechanisms.

Leptonic processes
--------------------------------

### Electron synchrotron

For a given Lorentz boost, the synchrotron losses $\left.-\frac{\dd E}{\dd t}\right|_\text{sync}$ go as $m^{-2}$ 
so that the emission from electrons can be sizeable with respect to that of protons. In what follows, we mostly 
discuss electrons but synchrotron could also be expected e.g. from positrons if there are no electrons around. 
Otherwise, the positrons and electrons annihilate resulting, for particles nearly at rest, in a $511\,\text{keV}$ 
emission that is observed e.g. along the Galactic ridge. 

Equation [](Epeak_sync) can be used to determine the peak energy of the emission from e.g. $500\,\text{GeV}$ 
electrons in a $1\,\text{mG}$ field:
\begin{align}
\label{Epeak_sync_e}
\left.E_\text{peak}\right|_\text{sync} & \approx 2.2\text{\,MeV} \times \times 10^{-3} \times \times 10^{-6} \times 
1836 \times \left
(\frac{B}
{1\,\text{mG}}\right)  \left(\frac {\gamma}{10^6}\right)^2\\
& \approx 4\text{\,eV} \times \left(\frac{B}{1\,\text{mG}}\right)  \left(\frac {\gamma}{10^6}\right)^2
\end{align}
So, in a mG field, $0.5\,\text{TeV}$ electrons radiate in the UV, while $5\,\text{TeV}$ electrons radiate in X-rays 
at  $0.4\,\text{keV}$.
Synchrotron radiation from electrons thus explains the emission from radio to optical wavelengths 
(sometimes up to X-rays) of most non-thermal sources.

We can take the calculation one step further and determine the expected spectrum for the synchrotron emission (a 
similar derivation can of course be made for protons). Consider a number density of electrons, $n_e$, following a 
power law of energy or Lorentz boost $\gamma$, i.e. 
$$
\label{eq:pwl_e}
n_e(\gamma) = n_0 \gamma^{-s},
$$
with e.g. $s \approx 2$ for diffusive shock acceleration. 

The synchrotron luminosity of such electrons filling a spherical region of radius $R$ that is optically thin 
(transparent) to its own emission reads:
$$
\left.L_\nu\right|_\text{sync} = \frac{4}{3}\pi R^3 \int \dd \gamma\, n_e(\gamma) \left.P_\nu(\nu, \gamma)\right|_\text{sync},
$$
where $P_\nu$ is the power emitted by a single electron, as defined in Equation [](sync_power).

To simplify the problem, we assume that the distribution function of emission as a function of photon frequency is 
sharply peaked around $\alpha\nu_c = \gamma^2 \nu_\text{ref}$, where $\nu_\text{ref} = \frac{3\alpha}{16} \frac
{eB}{m_e} $ does not depend on the electron Lorentz boost. The assumption of a sharply peaked function is called 
the delta approximation:
$$
f_\text{sync}(\nu/\nu_c) \approx \delta(\nu - \gamma^2 \nu_\text{ref}).
$$

Then, considering only the ultra-relativistic electrons ($\beta \approx 1$):
\begin{align}
\left.L_\nu\right|_\text{sync} &= \frac{4}{3}\pi R^3 \times \frac{4}{3}\sigma_\text{T}c u_B \times \int \dd \gamma\, n_e
(\gamma) \gamma^2 \delta(\nu - \gamma^2 \nu_\text{ref})\\
&= \frac{4}{3}\pi R^3 \times \frac{4}{3}\sigma_\text{T}c u_B \times \int \dd \gamma\, 
\frac{\gamma}{2\nu_\text{ref}} n_e(\gamma) \times 2\gamma \nu_\text{ref}\, \delta(\nu - \gamma^2 \nu_\text{ref})\\
&= \frac{4}{3}\pi R^3 \times \frac{4}{3}\sigma_\text{T}c u_B \times \int \dd \gamma\, 
\frac{\gamma}{2\nu_\text{ref}} n_e(\gamma) \times \delta\left(\gamma- \sqrt{\frac{\nu}{\nu_\text{ref}}}\right),   
\text{as } \delta(f(x))f'(x) = \delta(x)  \\
&= \frac{4}{3}\pi R^3 \times \frac{2}{3}\sigma_\text{T}c \times \frac{u_B}{\nu_\text{ref}} \times \sqrt{\frac{\nu}
{\nu_\text{ref}}} n_e\left(   
\sqrt{\frac{\nu}{\nu_\text{ref}}} \right)\\
&= \frac{4}{3}\pi R^3n_0 \times \frac{2}{3}\sigma_\text{T}c \times \frac{u_B}{\nu_\text{ref}} \times \left(\frac{\nu}
{\nu_\text{ref}}\right)^{-(s-1)/2}.
\end{align}

For a flat energy spectrum of electrons with $s=2$, neglecting the redshift of the photons, the energy spectrum of 
synchrotron photons goes as:
\begin{align}
\label{eq:sync_spec}
E_\gamma^2 \frac{\dd N}{\dd E_\gamma} &= \frac{\nu L_{\nu}}{4\pi D_L^2}\\
&\propto n_0 R^3 \times \frac{u_B}{\nu_\text{ref}} \times \nu^{1-(s-1)/2}\\
&\propto n_0 R^3 \times B \times \nu^{0.5}\\
&\propto n_0 R^3 \times B \times E_\gamma^{0.5},
\end{align}
i.e. a differential photon spectrum following a power-law, $\frac{\dd N}{\dd E_\gamma} \propto E_\gamma^{-1.5}$, from 
$\gamma_\text{min}
^2 \nu_\text{ref} \propto \gamma_\text{min}^2 B$ to $\gamma_\text{max}^2 \nu_\text{ref} \propto \gamma_\text{max}^2 
B$.

The observed range of frequencies covered by the photons can provide constraints on the range of Lorentz boosts 
covered by the electrons, provided the magnetic field, and the observed flux normalisation constrains the 
product of the magnetic field with the number of electrons in the emitting region.  

### Inverse Compton

The inverse Compton process, which is symmetrical to the Compton process, consists of the scattering of an energetic 
electron onto a photon, resulting in an energy gain for the photon:
$$
e^-_1 + \gamma_1 \rightarrow e^-_2 + \gamma_2, 
$$
where the initial photon and electron have energies $E_{\gamma_1} = h\nu_1$ and $E_{e_1} = \gamma m_e c^2$ in the 
observer's frame. 

There are two regimes to be considered for this scattering in the rest frame $\mathcal{R}'$ of the electron (see 
Chapter 9.3 in {cite}`2011hea..book.....L`):
- Thomson regime: $h\nu_1' \approx \gamma h\nu \ll m_ec^2$. In the Thomson regime, the cross section is independent 
  of the photon energy, $\sigma \approx \sigma_\text{T}$, and the outgoing photon has an energy $h\nu_2' =h\nu_1'$ 
  with an opposite momentum.  Back in the observer frame, the energy of the outgoing photon is $h\nu_2 \approx 
  \gamma  h\nu_2 \approx \gamma^2 h\nu_2$, which result in a net gain of energy by a factor $\propto 
  \gamma^2$.[^2]
- Klein-Nishina regime: $h\nu_1' \gtrsim m_ec^2$. In the Klein-Nishina regime, the recoil of the electron 
  cannot be neglected and the  cross section is  suppressed as $\sigma \propto (h\nu_1')^{-1}$. The conservation of 
  energy in the observer's frame tells us that the energy gain of the photon is at most  $h\nu_2 - h\nu_1 = 
  (\gamma-1)m_e c^2$, that is a gain $\propto \gamma$ for an   ultrarelativistic electron.
[^2]: Averaging over the angular configurations, one finds $h\nu_2 = \frac{4}{3} (\gamma\beta)^2 
  h\nu_2$.   

The inverse-Compton energy loss of an electron in an isotropic radiation field of energy density $u_\text{rad}$ reads:
$$
\left.P(\gamma)\right|_\text{IC} =  \left.-\frac{\dd E}{\dd t}\right|_\text{IC} = \frac{4}{3} \sigma c u_\text{rad} \beta^2 
\gamma^2, 
$$

Note that synchrotron radiation can be viewed as the inverse-Compton scattering of virtual photons associated to the 
magnetic field (so-called method of virtual quanta). This is the fundamental reason behind the similarity of the 
inverse-Compton and synchrotron energy loss in Equation [](eq:sync_loss). We can then write
$$
\boxed{\frac{\left.P(\gamma)\right|_\text{IC\ \ \ }}{\left.P(\gamma)\right|_\text{sync}} = \frac{u_\text{rad}}
{u_{B\ \ }}}.
$$

Similarly to synchrotron radiation, the power emitted by a single electron per unit photon frequency can be written:
$$
\label{IC_power}
\left.P_\nu(\nu,\gamma)\right|_\text{IC} = \frac{4}{3} \sigma c \beta^2 \gamma^2 \int \dd \nu_1 \frac{\dd u_\text
{rad}}{\dd \nu_1} \times f_\text{IC} \left(\frac{\nu}{\gamma^2\nu_1}\right),
$$
where $\int \dd \nu f_\text{IC} \left(\frac{\nu}{\gamma^2\nu_1}\right) = 1$.

The inverse-Compton luminosity of ultrarelativistic ($\beta \approx 1$) electrons filling an optically-thin 
spherical region of radius $R$ is: 
\begin{align}
\left.L_\nu\right|_\text{IC} &= \frac{4}{3}\pi R^3 \int \dd \gamma\, n_e(\gamma) \left.P_\nu(\nu, \gamma)
\right|_\text{IC}\\
 &= \frac{4}{3}\pi R^3 \times \int \dd \gamma\, \frac{4}{3} \sigma c n_e(\gamma)   \gamma^2 \int \dd \nu_1 
\frac{\dd u_\text
{rad}}{\dd \nu_1} \times f_\text{IC} \left(\frac{\nu}{\gamma^2\nu_1}\right)
\end{align}

In the Thomson regime, the function $f_\text{IC}(x)$ peaks around $x\approx2$. The delta approximation can be roughly 
adopted so that 
$$
f_\text{IC}(\nu/\gamma^2\nu_1) \approx \delta(\nu - 2\gamma^2 \nu_1).
$$

Then, the inverse-Compton luminosity of the source reads:
\begin{align}
\label{eq:Lic}
\left.L_\nu\right|_\text{IC} &= \frac{4}{3}\pi R^3 \times \frac{4}{3} \sigma_\text{T} c \times \int \dd \gamma\,
n_e
(\gamma) \gamma^2 \int \dd \nu_1 \frac{\dd u_\text
{rad}}{\dd \nu_1}(\nu_1) \times \delta(\nu - 2\gamma^2 \nu_1)\\
&= \frac{4}{3}\pi R^3 \times \frac{4}{3} \sigma_\text{T} c \times \int \dd \gamma\, \frac{1}{2} n_e (\gamma) \int \dd 
\nu_1 \frac{\dd u_\text{rad}}{\dd \nu_1}(\nu_1) \times  2\gamma^2 \delta(\nu - 2\gamma^2 \nu_1)\\
&= \frac{4}{3}\pi R^3 \times \frac{4}{3} \sigma_\text{T} c \times \int \dd \gamma\, \frac{1}{2} n_e (\gamma) \int \dd 
\nu_1 \frac{\dd u_\text{rad}}{\dd \nu_1}(\nu_1) \times  \delta(\nu_1 - \frac{\nu}{2\gamma^2})\\
&= \frac{4}{3}\pi R^3 \times \frac{2}{3} \sigma_\text{T} c \times \int \dd \gamma\, n_e (\gamma) \times \frac{\dd 
u_\text{rad}}{\dd \nu_1}\left(\frac{\nu}{2\gamma^2}\right).
\end{align}

The radiation field can have different origins depending on the environment. We speak of external inverse Compton 
when the photon field does not come directly from the electron population. For example, it can be an 
optical/infrared photon field from the environment of the compact object (e.g. accretion disk) or a diffuse photon 
field such as the CMB  for an extended emission region. 

A special case, found in many non-thermal sources, is when the scattered photon field comes from the electrons 
themselves, namely their synchrotron emission. This is known as the synchrotron self-Compton (SSC) model. The energy 
density in the spherical region of radius  $R$ is related to the synchrotron luminosity of this region by the 
relation (see e.g. Section 6 in {cite}`2013LNP...873.....G`):
$$
\label{eq:tcross}
\frac{4}{3}\pi R^3 \frac{\dd u_\text{rad}}{\dd \nu_1} \dd \nu_1 = t_\text{cross} \times \left.L_{\nu_1}\right|_\text
{sync} \dd \nu_1, 
$$
where $t_\text{cross} = \frac{3}{4}\frac{R}{c}$ is the average crossing time of the photons through the spherical 
region. 

Using Equations [](eq:Lic) and [](eq:tcross), the SSC losses can then be written as:
\begin{align}
\left.L_\nu\right|_\text{SSC} &= \frac{\sigma_\text{T} R}{2}  \times \int \dd \gamma\,  
n_e (\gamma) \times \left.L_{\nu_1}\right|_\text{sync}\left(\frac{\nu}{2\gamma^2}\right).
\end{align}

The SSC luminosity of an electron population of density $n_0$ and Lorentz factor $\bar \gamma$ is simply its 
synchrotron luminosity scaled by a factor $n_0 \sigma_\text{T} R/2$ and shifted to frequencies larger by a factor of 
$2 {\bar \gamma}^2$. The same conclusion can be reached for a power-law distribution of the Lorentz boost of 
the electrons as in Equation [](eq:pwl_e):

\begin{align}
\left.L_\nu\right|_\text{SSC} &= \frac{\sigma_\text{T} R}{2} \times \frac{4}{3}\pi R^3 n_0\times  \frac{2}{3}
\sigma_\text{T}c \times \frac{u_B}{\nu_\text{ref}}   \times \int \dd \gamma\,  
n_0 \gamma^{-s} \times \left(\frac{\nu}{2\gamma^2\nu_\text{ref}}\right)^{-(s-1)/2}\\
 &= \frac{\sigma_\text{T}^2 c R}{3} \times \frac{4}{3}\pi R^3n_0 \times  \frac{u_B}{\nu_\text{ref}} \times  \left(\frac
{\nu}{2\nu_\text{ref}}\right)^{-(s-1)/2}
\times \int \dd \gamma\, n_0 \gamma^{-1}\\
&=\frac{4}{3}\pi R^3 \times n_0^2 \ln\left( \frac{\gamma_\text{max}}{\gamma_\text{min}}\right) \times \frac{\sigma_\text
{T}^2 c R}{3} \times \frac{u_B}{\nu_\text{ref}} \times  \left(\frac{\nu}{2\nu_\text{ref}}\right)^{-(s-1)/2}.
\end{align}

The SSC spectrum has the same photon index as the synchrotron spectrum. As we have shown in  Equation [](eq:sync_spec),
the frequency range covered by the synchrotron photons goes from 
$\gamma_\text{min}^2 \nu_\text{ref}$ to $\gamma_\text{max}^2 \nu_\text{ref}$, where $\nu_\text{ref} \propto B$. The 
frequency range covered by the SSC photons should then go from $2\gamma_\text{min}^4 \nu_\text{ref}$ to $2\gamma_\text
{max}^4 \nu_\text{ref}$, when we neglect the Klein-Nishina effect. Note though that for $\gamma_\text{max} h\nu_1 
\gtrsim m_e c^2$, which is verified e.g. for $\gamma_\text{max}=10^6$ and $h\nu_1 = \left.E_\text{peak}\right|_\text
{sync}  \approx 4\text{\,eV} 
\times \left(\frac{B}{1\,\text{mG}}\right)  \left(\frac {\gamma}{10^6}\right)^2$, the scattering occurs in the 
Klein-Nishina regime so that the SSC peak emission can reach an energy of $\left.E_\text{peak}\right|_\text{SSC} 
\approx 
\gamma_\text{max} m_e c^2 \approx 0.5 \text{\,TeV}$.

Irrespective of the scattering regime, the ratio of the amplitude of the SSC and synchrotron peaks provides 
constraints on the product of the density of the region of its size, while the peak energies (or better their ratio 
in the Thomson regime) constrain the maximum Lorentz factor of the electrons.

### Bremsstrahlung

The Bremsstrahlung emission, i.e. the radiation of an electron in the electromagnetic field of a 
nucleus, is relevant in an astrophysical context when the density of matter (neutral or ionised hydrogen/helium) is 
sufficiently high, as for the $p-p$ process. Through Bremsstrahlung emission, the electron can lose a substantial 
fraction of its kinetic energy $T=(\gamma-1)m_e c^2$. For a Maxwellian electron velocity distribution with $\beta\ll1$ 
and $T \approx \frac{1}{2}m_e(\beta c)^2$, we speak of thermal Bremsstrahlung or free-free emission, as the electron 
is  not bound to the nucleus with which it interacts in either the initial or final states.[^3] Thermal 
Bremsstrahlung  emission is found, for example, in the warm-hot plasma of galaxy clusters and explains their X-ray 
continuum radiation up to $\frac{1}{2}m_e(\beta c)^2 = 2.5\,\text{keV}\times \left(\frac{\beta}{0.1}\right)^2$. 

[^3]: The opposite term, bound-bound radiation, is used for the emission of spectral lines by partially ionised atoms.

Non-thermal Bremsstrahlung is found in the interstellar medium, particularly in molecular clouds  close to supernova 
remnants. This non-thermal radiation explains some of the gamma-ray emission from molecular clouds up to energies of  $(\gamma-1)m_e c^2 
\approx 0.5\,\text{TeV}\times \left(\frac{\gamma}{10^6}\right)$, in addition  to the emission processes discussed 
above.

The energy loss of an electron through Bremsstrahlung depends on the radiation length of the electrons in the medium, 
$X_0$ in $\text{g}\,\text{cm}^{-2}$, so that:
$$
\label{eq:brem_loss}
\left.-\frac{\dd E}{\dd t}\right|_\text{Brem} = \frac{n m_p c}{X_0} \times \gamma m_e c^2, 
$$
where $n m_p$ is the mass density of protons.

The Bremsstrahlung loss rate, $-\left.\frac{1}{E}\frac{\dd E}{\dd t}\right|_\text{Brem}$, 
is independent of the electron energy, contrarily to synchrotron and inverse Compton loss rates which go as 
$\propto E$. As all electrons are affected by Bremsstrahlung in the same manner, the photon index of the 
Bremsstrahlung spectrum is the same as the electron index. 

A comparison of the various emission mechanisms invoked in a lepto-hadronic model for the emission of a supernova 
remnant interacting with a molecular cloud are shown in [](fig:sed_SN1006). The energy flux of the 
synchrotron and external inverse-Compton components goes as $E_\gamma^2 \frac{\dd N_\gamma}{\dd E_\gamma} \propto 
E_\gamma^{0.5}$. We can thus infer that electrons are injected in the model with a slope of $s \approx 2$. This 
confirmed by the Bremsstrahlung component, which is flat ($E_\gamma^2 \frac{\dd N_\gamma}{\dd E_\gamma} \propto 
E_\gamma^0$ i.e. $\frac{\dd N_\gamma}{\dd E_\gamma} \propto E_\gamma^{-2}$) between ${\sim}\,1\,\text{MeV}$ and
${\sim}\,1\,\text{TeV}$. Finally, while the leptonic emission fully explains the synchrotron peak from radio to X rays, 
hadronic emission is included to model the high-energy component. This hadronic emission from the $p-p$ process results 
in $\pi^0$ decay, with a flat spectrum from ${\sim}\,100\,\text{MeV}$ to ${\sim}\,1\,\text{TeV}$ corresponding to 
the proton index $s \approx 2$.[^4] Note the characteristic feature of the pion bump, with a sharp break close to 
half the pion mass at ${\sim}\,70\,\text{MeV}$. This break has now been observed in the several bright supernova 
remnants interacting with molecular clouds in the energy range covered by the Fermi-LAT satellite, demonstrating the 
co-acceleration of protons and electrons in these environments.

[^4]: For an energy-independent inelasticity, the pions and the photons have the same index as the protons, 
following the same argument as for Bremsstrahlung emission.

:::{figure}  ../../images/sed_mixed_SN1006.png
:name: fig:sed_SN1006
:align: center
:width: 100%

Spectral energy distribution, i.e. energy flux as a function of photon energy from 
radio wavelengths to TeV gamma rays, of the supernova remnant SN 1006 interacting with a molecular cloud. The 
radiation processes are indicated with lines of different colors and styles, as indicated in the figure. _Extracted 
from {cite}`2010A&A...516A..62A`._
:::


:::{exercise} Synchrotron emission from X-ray filaments in Tycho’s SNR
:label: exo:tycho

X-ray observations have uncovered very thin filaments at the shock front of several young supernova remnants (SNR). 
The thickness of the filaments is a few percent of the SNR radius, and the emission is thought to be synchrotron 
emission of very-high-energy electrons.

1. Give the numerical value of the energy of electrons radiating synchrotron photons at a peak energy $h\nu = 2\,\text
   {keV}$ in a magnetic field $B = 1\,\text{nT} = 10\,\mu\text{G}$.

2. What is the synchrotron cooling timescale, $t_\text{sync}$, of these electrons? What distance would the electrons 
   travel if they had a ballistic trajectory?

3. Assuming that the diffusion of the electrons follows the Bohm limit, $D = \frac{pc}{3eB}$, give the expression 
   and the numerical value of the diffusion length after a time $t_\text{sync}$.

   _Note: we recall the value of the Bohr magneton, $\mu_\text{B} = \frac{e \hbar}{2m_e} \approx 5.8\times 10^{-11}\,
   \text{MeV}\,\text{T}^{-1}$._

4. Tycho's SNR is at a distance $d = 2.4\,\text{kpc}$. Its filaments have an observed thickness of $\theta = 2.5\, \text
   {arcseconds}$. Assuming that the thickness of the filaments is equal to the diffusion length of the electrons, 
   give the expression and the numerical value of the magnetic field at the shock.

_Exercise adapted from R. Terrier's lessons._

:::

:::{solution} exo:tycho
:class: dropdown

1. We have seen that the peak synchrotron energy depends linearly on the magnetic field and quadratically on the 
   electron Lorentz boost. Inverting Equation [](Epeak_sync_e) to find the electron Lorentz boost, one gets:
   \begin{align}
\gamma &\approx 10^6 \times \left( \frac{h\nu}{4\,\text{eV}} \right)^{1/2} \left( \frac{B}{1\,\text{mG}} \right)^
   {-1/2}\\
 &\approx 10^6 \times \sqrt{500} \times \sqrt{100}  \times \left( \frac{h\nu}{2\,\text{keV}} \right)^{1/2} \left( \frac{B}
   {10\,\mu\text{G}} \right)^{-1/2}\\
&\approx 2 \times 10^8  \times \left( \frac{h\nu}{2\,\text{keV}} \right)^{1/2} 
   \left( \frac{B}
   {10\,\mu\text{G}} \right)^{-1/2}
   \end{align}
   This corresponds to an electron energy of $E_e = \gamma m_e c^2 \approx  100\,\text{TeV}$.
2. The synchrotron cooling timescale of an electron is
   \begin{align}
t_\text{sync} &= \left[\left.-\frac{1}{E} \frac{\dd E}{\dd t}\right|_\text{sync} \right]^{-1} \\
&= \frac{3}{4} \frac{m_e c^2}{\sigma_\text{T} c u_B} \times \left(\frac{E}{m_e c^2}\right)^{-1}
   \end{align}
   Noting that $u_B = \frac{B^2}{2\mu_0} = 2.5\,\text{MeV\,m}^{-3} \times \left(\frac{B}{10\,\mu\text{G}} \right)^2$,
   we get
   \begin{align}
t_\text{sync} &= \frac{3 \times 0.5}{4 \times 0.67 \cdot 10^{-28} \times 3 \cdot 10^8 \times 2.5 \times 2 \times 
   10^8}\,\text{s}  \times \left
   (\frac{B}{10\,\mu\text{G}} \right)^{-2} \left(\frac{\gamma}{2 \times 10^8}\right)^{-1}\\
& = 1.2\,\text{kyr}  \times \left
   (\frac{B}{10\,\mu\text{G}} \right)^{-2} \left(\frac{\gamma}{2 \times 10^8}\right)^{-1}
   \end{align}
   i.e. 
   \begin{align} 
c t_\text{sync} &= 0.31 \times 1.2\,\text{kpc}  \times \left(\frac{B}{10\,\mu\text{G}} \right)^{-2} \left(\frac{\gamma}{2 \times 10^8}\right)^{-1}\\
&= 370\,\text{pc}  \times \left(\frac{B}{10\,\mu\text{G}} \right)^{-2} \left(\frac{\gamma}{2 \times 10^8}\right)^{-1}
   \end{align}
3. At time $t = t_\text{sync}$, the diffusion length of the electrons goes as
   \begin{align}
r_\text{diff} &= \sqrt{4Dt_\text{sync}}\\
 &= \sqrt{\frac{4pc}{3eB}t_\text{sync}}\\
&\approx \sqrt{\frac{2 \gamma}{3B} \frac{\hbar c}{\mu_\text{B}} ct_\text{sync}}\\
&\approx \sqrt{\frac{2\times 2 \cdot 10^8}{3 \times 10^{-9}} \frac{197 \times 10^{-15}}{5.8 \cdot 10^{-11} \times 3.
   1 \cdot 10^{16}} \times 370}\,\text{pc} \times \left(\frac{B}{10\,\mu\text{G}} \right)^{-3/2}\\
&\approx \sqrt{\frac{6 \times 3.7 \times 10^{-3}}{9.3 \times 5.8 \times 10^{-4}}}\,\text{pc} \times \left(\frac{B}
   {10\,\mu\text{G}} \right)^{-3/2}\\
&\approx 2\,\text{pc} \times \left(\frac{B}{10\,\mu\text{G}} \right)^{-3/2}\\
   \end{align}
4. The observed thickness of the filaments is $R = d \tan \theta \approx 2.4\,\text{kpc} \times \frac{2.5}{3600} 
   \times \frac{\pi}{180} \approx 30\,\text{mpc}$. If the observed size of the filaments is limited by diffusion, 
   $r_\text{diff} =R$, we get a magnetic field
   \begin{align}
B &= 10\,\mu\text{G} \times \left(\frac{R}{2\,\text{pc}}\right)^{-2/3}\\
  &= 10\,\mu\text{G} \times \left(\frac{2}{0.03}\right)^{2/3} \times \left(\frac{R}{30\,\text{mpc}}\right)^
   {-2/3}\\
&= 160\,\mu\text{G} \times \left(\frac{R}{30\,\text{mpc}}\right)^{-2/3}\\
   \end{align}
This is indeed the order of magnitude of the magnetic field inferred in such environments.
:::


:::{tip}
**Notions from this chapter**

_Hadronic losses_
- Through which processes do protons and nuclei lose energy in astrophysical environments?
- What are the secondary particles produced in these processes?
- 
_Leptonic losses_
- Through which processes do electrons lose energy in astrophysical environments?
- In which energy range do these electrons radiate away their energy?
- What is the link between the photon index and the electron index for these processes?

:::


:::{tip}
**Calculations / demonstrations**

_Pion production: $\int\dd E_\gamma \frac{\dd N_\gamma}{\dd E_\gamma}E_\gamma = \frac{4}{3K_\pi}\int\dd E_\nu \frac{\dd N_\nu}{\dd 
E_\nu}E_\nu$_
- What are $E_\gamma$, $E_\nu$ and $K_\pi$? 
- What is the value of $K_\pi$ for the $p-p$ and $p-\gamma$ processes? 
- Can I prove this relation?
- This relation is valid in an "optically thin" medium, what does that mean?

_Synchrotron and inverse-Compton emission of electrons:  $P = \frac{4}{3}\sigma c u (\gamma\beta)^2$_
- What are $P$, $\gamma$, $\beta$, $\sigma$ and $u$? 
- Which of these quantities differ for synchrotron and inverse-Compton losses? 
- What can I learn from the ratio of inverse-Compton and synchrotron emission of an astrophysical source?

:::