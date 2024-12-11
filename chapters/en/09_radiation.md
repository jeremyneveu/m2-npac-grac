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
the main losses for each species and account for the relative energy throughput per particles as well as for the 
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
#:class: dropdown

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
interactions their environment and on their way to Earth, 
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
energies when the nuclei can be seen as a superposition of independent nucleons. In the nucleus rest frame, $\mathcal
{R}'$, different nuclear/hadronic processes should be considered depending on the target photon energy (see {cite}`2006JCAP...09..005A`):  
- _Giant dipole resonance_ for $\epsilon_\gamma' \approx 10-20\,\text{MeV}$, i.e. a collective nuclear mode in which 
  the 
  neutrons and protons oscillate in antiphase. The giant dipole resonance can lead, in the final state, to 
  the release of $n$, $p$, $2n$, $2p$, $np$, $\alpha$; 
- _Quasi-deuteron process_ for $\epsilon_\gamma' \approx 30\,\text{MeV}$, i.e. the interaction of the photon with a pair of 
  nucleons that can be released by the parent nucleus.
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
\epsilon_\gamma & = \frac{m_p \epsilon'_\gamma}{4E_p} \text{, for a head-on collision}
\end{align}


The relevant wavelength for the photon is
\begin{align}
\lambda_\gamma &= \frac{hc}{\epsilon_\gamma}\\
            &= 1.2\,\mu\text{m}\times \left(\frac{\epsilon_\gamma}{1\,\text{eV}}\right)^{-1}\\
            &= 4.8\,\mu\text{m}\times \frac{E_p}{m_pc^2} \left(\frac{\epsilon'_\gamma}{1\,\text{eV}}\right)^{-1}\\
            &= 480\,\mu\text{m}\times \left(\frac{E_p}{1\,\text{EeV}}\right) \left(\frac{\epsilon'_\gamma}{10\,\text
{MeV}} \right)^{-1}
\end{align}

A useful tip in the numerical application lies in noting that $hc = 2\pi\times \hbar c \approx 2\pi\times 197\,\text
{MeV}\,\text{fm} \approx 1.2\,\text{GeV}\,\text{fm} = 1.2\,\text{eV}\,\mu\text{m}$.

For an energy per nucleon $E_p = 1\,\text{EeV}$, a photon of the CMB with a wavelength of $480\,\mu\text{m}$ is seen 
as a $10\,\text{MeV}$ gamma rays in the rest frame of the nucleus, resulting in an interaction through the giant-
dipole-resonance channel. For the same energy per nucleon, the photons relevant to baryon resonance are $\frac{150\,
\text{MeV}}{10\,\text{MeV}} = 15$ times more energetic. They have 15 times smaller wavelengths, around $30\,
\mu\text{m}$, that is they are photons of the CIB.
:::

#### Photo-production of pions and pairs

The main interactions of a nucleon in a photon field:
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

In the nucleon's rest frame the threshold for pair and pion production are about $1\,\text{MeV}$ and $140\,\text{MeV}
$, respectively. The energy loss-length, $\lambda = \langle (\frac{1}{E}\frac{\dd dE}{\dd X})^{-1} \rangle$, depends on 
the 
product of the cross section and of the inelasticity (energy-loss fraction) of the reaction. This product, which is 
nearly constant at energies larger than a few times the threshold energy, is two orders of magnitude larger for pion 
production than for pair production, so that the former dominates over the latter at the highest energies.

The various loss processes relevant for the propagation of ultra-high energy cosmic rays on cosmological scales are 
illustrated in [](fig:UHECR-loss).

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

1. Compute the threshold energy for the photo-production of pions $p+\gamma \rightarrow p+\pi_0$ in a target photon 
   field at $\lambda_\gamma = 1\,\text{mm}$, which is close to the peak of the CMB.  

2. Compute the threshold energy for the pair-production in $\gamma\gamma$ interaction $\gamma+\gamma \rightarrow 
   e^+ + e^-$ in a target photon field at $\lambda_\gamma = 1\,\mu\text{m}$, which is close to the peak of the COB.  

:::


:::{solution} exo:threshold_energies
#:class: dropdown

As a refresher, two properties of the invariant mass are used when computing a threshold energy. First, the norm of 
the four-momentum is conserved in the reaction, i.e. it is the same in the initial and final states. Second, this 
norm is Lorentz invariant, which allows us to compute it in the rest frame for the final state rather than in the 
lab frame. The threshold energy is by definition such as the particles in the final state are produced at rest in 
the center-of-mass frame. In the following calculation, we adopt the convention $c=1$ for simplicity.

1. The conservation of the invariant mass for the reaction $p+\gamma \rightarrow p+\pi_0$ gives:
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

A particle of energy $E$, mass $m$ and charge $Ze$ emits synchrotron radiation in magnetic field $B$. Average over the 
pitch 
angle $\theta$, such as $\cos\theta = \frac{\vec{\beta}\cdot\vec{B}}{\beta B}$, the synchrotron energy loss reads 
(see e.g. chapter~14 of {cite}`jackson_classical_1999`):
$$
\left.-\frac{\dd E}{\dd t}\right|_\text{sync} = \frac{4}{3} \sigma c u_B \beta^2 \gamma^2, 
$$
with $(\gamma, \gamma\vec{\beta})$ the four-momentum of the particle and
\begin{align}
\sigma &= \frac{8\pi}{3} \left[ \frac{(Ze)^2}{ 4\pi\epsilon_0 mc^2} \right]^2\\
&= \sigma_\text{T} \times Z^4 \times \left( \frac{m}{ m_e} \right)^{-2}.
\end{align}

In the ultra-relativistic limit, $\beta \approx 1$ adopted hereafter, the synchrotron loss rate is thus
$$
t_\text{sync}^{-1} = \frac{4}{3} \frac{\sigma c u_B}{mc^2} \times \frac{E}{mc^2}.
$$

Note that the synchrotron loss rate increases with energy and that, for a fixed Lorentz boost $\gamma = E/mc^2$, the 
rate goes as $1/m^3$. If the loss rate becomes dominant with respect to 
the acceleration rate, the maximum energy is limited by the losses (so-called synchrotron burn-off limit).

The synchrotron radiation is emitted as photons over a range of frequencies, $\nu$. The power emitted by a single 
electron per frequency unit reads
$$
P_\nu(\nu) = \frac{4}{3} \sigma c u_B \beta^2 \gamma^2 \times \frac{1}{\nu_\text{c}}f\left( \frac{\nu}{\nu_\text{c}} 
\right),
$$
where $\int \frac{\dd \nu}{\nu_\text{c}}f\left( \frac{\nu}{\nu_\text{c}}\right)=1$ so that $P(\nu) \equiv \int \dd 
\nu\, 
P_\nu(\nu) =  \left.-\frac{\dd E}{\dd t}\right|_\text{sync}$, and where the critical frequency, averaged over the 
pitch angle, is $\nu_\text{c} = \frac{3}{16} \frac{ZeB}{m} \gamma^2$.

The peak of the photon spectrum is at $E_\text{peak} = \alpha h\nu_\text{c}$, where $\alpha \approx 0.3$ corresponds 
to the maximum of $f(x)$. Using the value of the nuclear magneton, $\mu_N = \frac{e\hbar}{2m_p} \approx \pi \times 10^
{-14}\,\text{MeV\,T}^{-1}$, one finds:
\begin{align}
E_\text{peak} & = \frac{3\alpha}{16} \frac{e\hbar}{2m_p} \times 4\pi \times B\gamma^2 \times \left(\frac{m}{m_p}
\right)^{-1} \left(\frac{Z}{1}\right)\\
& = \frac{3\pi\alpha}{4} \mu_N \times B\gamma^2 \times \left(\frac{m}{m_p}\right)^{-1} \left(\frac{Z}{1}
\right)\\
& \approx \frac{3\pi^2\times0.3}{4}\times 10^{-14} \times 10^{-4} \times 10^{18} \text{\,MeV} \times \left(\frac{B}{1\,
\text{G}}\right) \left(\frac{\gamma}{10^9}\right)^2 \left(\frac{m}{m_p}\right)^{-1} \left(\frac{Z}{1}\right)\\
& \approx 2.2\text{\,MeV} \times \left(\frac{B}{1\,\text{G}}\right)  \left(\frac{\gamma}{10^9}\right)^2  
\left(\frac{m}{m_p}\right)^{-1} \left(\frac{Z}{1}\right)
\end{align}

Synchrotron emission from ultra-high energy protons at $10^{18}\,$eV in a magnetic field of $1\,\text{G}$ can thus 
end up as photons in the MeV range. This process has sometimes been invoked to explain the gamma-ray emission from 
the jetted active galactic nuclei. In the next section, we will look at alternative leptonic mechanisms.