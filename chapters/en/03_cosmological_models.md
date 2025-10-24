---
short_title: Cosmological models
authors:
  - jneveu
keywords: cosmological models, EdS model, mechanical analogy
---

# Cosmological models

## Simple models

In the following exercises, we will use the {term}`flat Universe` approximation ($k=0$), corresponding to the {term}`critical density`, which empirically appears to be a very good approximation.

### Einstein-de Sitter model

:::{exercise} Einstein-de Sitter model
:label: exo:EdeS

We consider a {term}`flat` Universe ($\Omega_k^0=0$) consisting only of matter ($\Omega_m^0=1$, $\Omega_\Lambda^0=\Omega_r^0=0$).

1. Determine the Hubble parameter $H(a)$ as a function of the scale factor $a$ and the current Hubble constant $H_0$.

2. Determine the scale factor $a(t)$ as a function of time, taking $a(t_0)=1$ at time $t_0$ (today), with time measured from the Big Bang.

3. Calculate the age of the Universe $t_0$ as a function of $H_0$ and make a numerical application for $H_0=70$ km/s/Mpc.

4. Determine the deceleration parameter $q_0$. What can you conclude about the current dynamics of the Universe?

:::

:::{solution} exo:EdeS
:class: dropdown

1. The first Friedmann equation gives:
\begin{equation}
H^2 = \left(\frac{\dot{a}}{a}\right)^2 = H_0^2 \left( \frac{\Omega_m^0}{a^3} + \frac{\Omega_r^0}{a^4} + \Omega_\Lambda^0 + \frac{\Omega_k^0}{a^2} \right)
\end{equation}
With $\Omega_m^0=1$ and $\Omega_r^0=\Omega_\Lambda^0=\Omega_k^0=0$:
\begin{equation}
H(a) = \frac{\dot{a}}{a} = \frac{H_0}{a^{3/2}}
\end{equation}

2. We have: $\frac{da}{dt} = a \frac{H_0}{a^{3/2}} = \frac{H_0}{a^{1/2}}$

Which gives: $a^{1/2} da = H_0 dt$

Integrating: $\int_0^a {a'}^{1/2} da' = H_0 \int_0^t dt'$

We get: $\frac{2}{3} a^{3/2} = H_0 t$

Therefore: 
\begin{equation}
a(t) = \left( \frac{3 H_0 t}{2} \right)^{2/3}
\end{equation}

3. At $t=t_0$, we have $a(t_0)=1$, so:
\begin{equation}
1 = \left( \frac{3 H_0 t_0}{2} \right)^{2/3} \Rightarrow t_0 = \frac{2}{3 H_0}
\end{equation}

Numerical application: $t_0 = \frac{2}{3} \times \frac{1}{70 \text{ km/s/Mpc}} = 9.1$ Gyr

4. The deceleration parameter is:
\begin{equation}
q_0 = -\frac{\ddot{a}a}{\dot{a}^2}\bigg|_{t=t_0}
\end{equation}

From the second Friedmann equation:
\begin{equation}
\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}(\rho + 3p/c^2)
\end{equation}

For matter (dust), $p=0$, so:
\begin{equation}
q_0 = \frac{4\pi G \rho_0}{3 H_0^2} = \frac{\Omega_m^0}{2} = \frac{1}{2}
\end{equation}

The Universe is therefore decelerating.

:::

### Radiation model

:::{exercise} Radiation-dominated model
:label: exo:radiation

We consider a flat Universe consisting only of radiation ($\Omega_r^0=1$, $\Omega_m^0=\Omega_\Lambda^0=\Omega_k^0=0$).

1. Determine the scale factor $a(t)$ as a function of time.

2. Calculate the age of the Universe $t_0$ as a function of $H_0$.

3. Compare this result with the Einstein-de Sitter model.

:::

:::{solution} exo:radiation
:class: dropdown

1. The first Friedmann equation gives:
\begin{equation}
H^2 = \frac{H_0^2}{a^4} \Rightarrow \frac{da}{dt} = \frac{H_0}{a}
\end{equation}

Which gives: $a da = H_0 dt$

Integrating: $\int_0^a a' da' = H_0 \int_0^t dt'$

We get: $\frac{a^2}{2} = H_0 t$

Therefore:
\begin{equation}
a(t) = \sqrt{2 H_0 t}
\end{equation}

2. At $t=t_0$, we have $a(t_0)=1$, so:
\begin{equation}
1 = \sqrt{2 H_0 t_0} \Rightarrow t_0 = \frac{1}{2 H_0}
\end{equation}

3. The radiation-dominated universe is younger than the Einstein-de Sitter model:
$t_0^{\text{rad}} = \frac{1}{2 H_0} < t_0^{\text{EdS}} = \frac{2}{3 H_0}$

:::

### Empty Universe

:::{exercise} Empty Universe (Milne model)
:label: exo:empty

We consider a Universe containing no matter or energy ($\Omega_m^0=\Omega_r^0=\Omega_\Lambda^0=0$, $\Omega_k^0=1$).

1. Determine the scale factor $a(t)$ as a function of time.

2. Calculate the age of the Universe $t_0$ as a function of $H_0$.

:::

:::{solution} exo:empty
:class: dropdown

1. The first Friedmann equation gives:
\begin{equation}
H^2 = \frac{H_0^2}{a^2} \Rightarrow \frac{da}{dt} = H_0
\end{equation}

Integrating: $a(t) = H_0 t + C$

With $a(0)=0$, we get $C=0$, so:
\begin{equation}
a(t) = H_0 t
\end{equation}

2. At $t=t_0$, we have $a(t_0)=1$, so:
\begin{equation}
1 = H_0 t_0 \Rightarrow t_0 = \frac{1}{H_0}
\end{equation}

This is the oldest possible universe for a given $H_0$.

:::

:::{important}

The Hubble constant $H_0$ appears in the three previous Universe models. The expansion rate of the Universe today is not a prediction of the models but an external datum, during the integration of the Friedmann differential equations.
:::

## Multi-component models

Modern cosmology was born with General Relativity. Since the writing of these equations, scientists have begun to mathematically describe the universe as a physical system. Many models have been proposed to describe the different histories of the universe.

### Eddington-Lemaître model

:::{exercise} Eddington-Lemaître model  
:label: exo:lemaitre

Friedmann and Lemaître were the first cosmologists to independently propose non-static universe models with arbitrary curvatures. Friedmann equations have been extensively studied in this course, but Lemaître was the first to propose the idea that the Universe developed from a primitive atom. His model is based on a universe composed only of cold matter, with a cosmological constant and arbitrary spatial curvature (no radiation).

1. In such a model, show that, just after a big bang at $t=0$, at the beginning of the universe the scale factor increases as:
\begin{equation}
\frac{a(t)}{a_0} =\left( \frac{3}{2}H_0\sqrt{\Omega_m^0}t\right)^{2/3}
\end{equation}

2. As the universe expands, however, the energy density of matter decreases and the cosmological constant eventually dominates. Show that, for large $t$, the scale factor increases as:
\begin{equation}
a(t) \propto e^{H_0\sqrt{\Omega_\Lambda^0}t}
\end{equation}

3. Calculate $\ddot{a}$ and show that the expansion of the universe first decelerates, then accelerates. Calculate $a_*$ the scale factor at the transition.

:::

:::{solution} exo:lemaitre  
:class: dropdown

1. In the Lemaître matter-only model, the first Friedmann equation is written:
\begin{equation}
\label{eq:lemaitre}
\frac{\dot{a}^2}{a^2} = H_0^2\left[\Omega_m^0 \left(\frac{a_0}{a}\right)^{3} + \Omega_\Lambda^0 + \Omega_k^0 \left(\frac{a_0}{a}\right)^{2}\right] \Leftrightarrow \dot{a}^2 = H_0^2\left[\Omega_m^0 \frac{a_0^3}{a} + \Omega_\Lambda^0 a^2 + \Omega_k^0 a_0^2 \right]
\end{equation}
At $t\approx 0$, the Universe was extremely small so the matter term dominates:
\begin{equation}
\dot a^2 \approx H_0^2\left[\Omega_m^0 \frac{a_0^3}{a}\right] \Leftrightarrow \sqrt{\frac{a}{a_0}}\frac{\dot{a}}{a_0}= H_0 \sqrt{\Omega_m^0} \Leftrightarrow \frac{a(t)}{a_0} = \left(\frac{3}{2}H_0\sqrt{\Omega_m^0}t\right)^{2/3}
\end{equation}

2. Then, after some time, $a$ becomes large and the cosmological constant term dominates:
\begin{equation}
\dot{a}^2 \approx H_0^2\left(\Omega_\Lambda^0 a^2\right) \Leftrightarrow \dot{a}= H_0 \sqrt{\Omega_\Lambda^0} a(t) \Rightarrow a(t) \propto e^{H_0\sqrt{\Omega_\Lambda^0}t}
\end{equation}

3. By deriving equation [](#eq:lemaitre), we find that:
\begin{equation}
2\dot{a}\ddot{a} = H_0^2\left[ -\dot{a}\Omega_m^0 \frac{a_0^3 }{a^{2}} + 2 \dot{a} a \Omega_\Lambda^0 \right] \Leftrightarrow \frac{\ddot{a}}{a_0} = \frac{H_0^2}{2}\left[2 \Omega_\Lambda^0 \left(\frac{a}{a_0}\right) - \Omega_m^0\left(\frac{a_0}{a}\right)^2\right]
\end{equation}
When $a$ is small, we find that $\ddot{a}$ is negative and expansion decelerates. However, when $a$ is large, $\ddot{a}>0$ and the expansion of the universe accelerates. The transition occurs at:
\begin{equation}
\ddot{a}=0 \Leftrightarrow 0=\frac{H_0^2}{2}\left[2 \Omega_\Lambda^0 \frac{a_*}{a_0} - \frac{\Omega_m^0a_0^2}{a_*^2}\right] \Leftrightarrow \frac{a_*}{a_0} = \left( \frac{\Omega_m^0}{2\Omega_\Lambda^0}\right)^{1/3}
\end{equation}
For the $\Lambda$CDM model with $\Omega_m^0\approx 0.3$ and $\Omega_\Lambda^0\approx 0.7$, we have $a_*/a_0 \approx 0.6$ hence a transition redshift at $z\approx 0.67$.
:::

## $\Lambda$CDM model

The expansion of the Universe is now well described by the flat $\Lambda$CDM model ($\Omega_k^0=0$). The proportions of each component are now estimated at {cite}`Planck2018`:
$$\Omega_\Lambda^0 = 0.685,\quad \Omega_m^0 = 0.315$$

Cold matter can be separated into two contributions: dark matter $\Omega_{c}^0=0.264$ and baryonic matter [^baryons] $\Omega_b^0=0.049$.

## Mechanical analogy

:::{exercise} Mechanical analogy
:label: exo:analogmeca

1. Write the first Friedmann equation as follows:
\begin{equation}
\frac{1}{2}\Omega_k^0 = f(\Omega_i^0,a)
\end{equation}
Interpret this equation by analogy with the equation for the conservation of mechanical energy of a massive body in one-dimensional motion, and describe the role of each "potential energy" term.

2. Derive this equation with respect to time and make the analogy with Newton's law applied to a massive body in one-dimensional motion. Analyze again the role of each "force" term.

In what follows, we neglect the radiation component. Plot the potential energy terms as a function of the scale factor $a$ and describe the fate of the following universes.

3. Spherical model ($k=+1$) with $\Lambda=4\pi G \rho_m / c^2$ (show that Einstein's static model is a special case of this model and is unstable).

4. Matter-only models with different signs of curvature (the Einstein-de Sitter model corresponds to the case of flat curvature).

5. $\Lambda$CDM models with different signs for the cosmological constant and arbitrary curvatures (calculate the transition scale factor $a_*$ between expansion deceleration and acceleration).

:::

:::{solution} exo:analogmeca
:class: dropdown

1. In terms of $\Omega_i^0$, the first Friedmann equation is written:
\begin{equation}
H^2 = \left(\frac{\dot{a}}{a}\right)^2 = H_0^2 \left( \frac{\Omega_m^0}{a^3} + \frac{\Omega_r^0}{a^4} + \Omega_\Lambda^0 + \frac{\Omega_k^0}{a^2} \right)
\end{equation}

which gives:
\begin{equation}
\frac{1}{2}\Omega_k^0 = \frac{1}{2}\frac{\dot{a}^2}{H_0^2} - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{2}\frac{\Omega_r^0}{a^2} - \frac{1}{2}\Omega_\Lambda^0 a^2
\end{equation}

This equation resembles the conservation of mechanical energy for a massive body in one-dimensional motion:
- $\frac{1}{2}\Omega_k^0$ (constant) represents the conserved mechanical energy
- $\frac{1}{2}\frac{\dot{a}^2}{H_0^2}$ represents the kinetic energy
- $\frac{1}{2}\frac{\Omega_m^0}{a}$ is a gravitational potential centered at $a=0$ (attractive)
- $\frac{1}{2}\frac{\Omega_r^0}{a^2}$ is another type of attractive potential
- $\frac{1}{2}\Omega_\Lambda^0 a^2$ is an inverted harmonic potential (repulsive) centered at $a=0$

2. Deriving with respect to time:
\begin{equation}
\frac{\ddot{a}}{H_0^2} = - \frac{1}{2}\frac{\Omega_m^0}{a^2 } -\frac{\Omega_r^0}{a^3 } + \Omega_\Lambda^0 a
\end{equation}

This resembles Newton's law $F = ma$:
- $\frac{\ddot{a}}{H_0^2}$ is the acceleration
- $\frac{1}{2}\frac{\Omega_m^0}{a^2 }$ is the gravitational force (attractive)
- $\frac{\Omega_r^0}{a^3 }$ is the radiation pressure force (attractive)
- $\Omega_\Lambda^0 a$ is the dark energy force (repulsive)

3. For a spherical model with $\Lambda=4\pi G \rho_m / c^2$, we have $\Omega_\Lambda^0 = \Omega_m^0 / 2$.

The effective potential is:
\begin{equation}
V_{\rm eff}(a) = - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{4}\Omega_m^0 a^2
\end{equation}

The extremum occurs at:
\begin{equation}
\frac{dV_{\rm eff}}{da} = 0 \Rightarrow \frac{1}{2}\frac{\Omega_m^0}{a^2} - \frac{1}{2}\Omega_m^0 a = 0 \Rightarrow a = 1
\end{equation}

Einstein's solution at $a=1$ is unstable because it's at a maximum of the potential.

4. For matter-only models:
- $k=+1$: Spherical universe that will eventually collapse
- $k=0$: Flat universe that expands forever but asymptotically stops
- $k=-1$: Hyperbolic universe that expands forever

5. For $\Lambda$CDM models, the transition scale factor is:
\begin{equation}
a_* = \left(\frac{\Omega_m^0}{2 \Omega_\Lambda^0}\right)^{1/3}
\end{equation}

- Positive $\Lambda$: Transition from deceleration to acceleration
- Negative $\Lambda$: Universe will eventually collapse

:::

## Age of the Universe

:::{exercise} Age of the Universe
:label: exo:Uage

1. Calculate $a(t)$ and the age of the universe for three different models, assuming $H_0\approx 70\,\text{km/s/Mpc}$:
   - $\Omega_m^0=1, \Omega_\Lambda^0=0, \Omega_r^0 \approx 0$ (flat Einstein-de Sitter model)
   - $\Omega_m^0=\Omega_\Lambda^0\approx 0, \Omega_r^0 \approx 0$ (empty universe)
   - $\Omega_m^0=\Omega_r^0\approx 0, \Omega_\Lambda^0 = 1$ (flat model dominated by vacuum)

   Use $1\,\text{Mpc}=3\times 10^{19}\,\text{km}$.

2. Which universe is the oldest?

   For a $\Lambda$CDM model with $32\%$ matter and $68\%$ dark energy, cosmologists estimate the age of the universe at $13.8\,\text{Gyr}$. This can be compared with the age of the oldest stars: $t_{\text{first stars}} = 11.5\pm 1.3\,\text{Gyr}$ {cite:p}`hobson2006general`.

3. Assume that $H_0\approx 500\,\text{km/s/Mpc}$ as originally estimated by Edwin Hubble. Calculate again the age of the universe for the first case. Conclude.

:::

:::{solution} exo:Uage
:class: dropdown

1. We use the first Friedmann equation:
\begin{equation}
H^2 = H_0^2 \left[ \frac{\Omega_m^0}{a^3}+ \Omega_\Lambda^0+ \frac{(1-\Omega_m^0-\Omega_\Lambda^0)}{a^2}\right]
\end{equation}

**Einstein-de Sitter model** ($\Omega_m^0=1$):
\begin{equation}
\frac{da}{dt} = H_0 a^{-1/2} \Rightarrow a^{3/2} = \frac{3}{2}H_0 t \Rightarrow a(t) = \left( \frac{3}{2}H_0 t\right)^{2/3}
\end{equation}

Age: $t_U = \frac{2}{3H_0} = 9.1\,\text{Gyr}$

**Empty universe** ($\Omega_k^0=1$):
\begin{equation}
\frac{da}{dt} = H_0 \Rightarrow a(t) = H_0 t
\end{equation}

Age: $t_U = \frac{1}{H_0} = 13.6\,\text{Gyr}$

**Vacuum-dominated model** ($\Omega_\Lambda^0=1$):
\begin{equation}
\frac{da}{dt} = H_0 a \Rightarrow a(t) = e^{H_0 t}
\end{equation}

This model has no Big Bang (infinite age).

2. The empty universe is the oldest among finite-age models.

3. With $H_0=500$ km/s/Mpc:
\begin{equation}
t_U = \frac{2}{3H_0} = 1.9\,\text{Gyr}
\end{equation}

This is incompatible with the age of the Earth (~4.5 Gyr), which led to the "age crisis" in early cosmology.

:::

## Evolution of cosmological parameters

:::{figure} #omegas
:width: 100%
:align: center
:label: fig:omegas

Evolution of cosmological parameters.
:::

:::{note} Interactive content
![](#om-slider)
:::

:::{important} Key points

- The integration of the first Friedmann equation by injecting the evolution properties of different fluids allows us to obtain the evolution of the scale factor as a function of time.

- Whether with relativistic matter, non-relativistic matter or for an empty universe, we obtain functions that increase with time since we measure $H_0>0$, thus scenarios of expanding universes.

- Writing the first Friedmann equation in the form of an equation analogous to energy conservation in classical mechanics provides intuition about the evolution of a universe as a function of the different components present. Among other things, non-relativistic matter restrains expansion through its attractive gravitational effect, while a positive cosmological constant leads to an acceleration of expansion in the future.

:::

:::{seealso} To go further

- Other historical cosmological models: <wiki:Einstein%27s_static_universe>, <wiki:De_Sitter_universe>

- Standard model of cosmology $\Lambda$CDM: <wiki:Lambda-CDM_model>

:::

[^ksign]: The sign of $k$ is the inverse of the sign of $\Omega_k^0$.
[^baryons]: Baryonic matter is ordinary matter composed of protons and neutrons.
[^Mach]: In theoretical physics, particularly in discussions of gravitational theories, Mach's principle is the name given by Einstein to an imprecise hypothesis often attributed to physicist and philosopher Ernst Mach. The idea is that local inertial frames are determined by the large-scale distribution of matter.
