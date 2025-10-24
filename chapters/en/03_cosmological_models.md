---
short_title: Cosmological models
authors:
  - jneveu
keywords: cosmological models, EdS model, mechanical analogy
---

Cosmological models
====================

Simple models
-------------

Now that we have a model to describe the dynamics of the Universe, let's calculate its evolution in a few simple cases for practice.

### Flat universe, matter only

Let's start with the case of a flat Universe containing only non-relativistic matter. This is the so-called _Einstein-de Sitter_ model. It is the simplest one could think of in 1930. The first Friedmann equation is written:
\begin{equation*}
& 3 \frac{\dot{a}^2}{a^2} = 8\pi \GN \rho_m = 8 \pi \GN \rho_m^0 \left(\frac{a_0}{a}\right)^{3} 
& \Leftrightarrow (\dot a)^2 = 8 \pi \GN \rho_m^0 a_0^3 / 3 a = H_0^2 \Omega_m^0 \frac{a_0^3}{a}
\end{equation*}
Before integrating this differential equation, let us remember that the energy density parameters are linked by a closure relation [](#eq:omega_sum). Consequently, in a flat Universe with only matter, we have $\Omega_m^0=1$. Let's now integrate the differential equation between $0$ and an arbitrary scale factor $a$:
\begin{equation*} 
\int_0^{a}\sqrt{\frac{a'}{a_0}} \frac{\dd a'}{a_0} = \int_0^t H_0  \dd t' \Rightarrow \frac{2}{3}\left(\frac{a(t)}{a_0}\right)^{3/2} = H_0  t
\end{equation*}
$$
\label{eq:a_matiere_only}
\Rightarrow \frac{a(t)}{a_0} = \left( \frac{3}{2}H_0  t\right)^{2/3}$$
with at the beginning of the Universe $t=0$ when $a=0$. We have thus obtained a direct relation between the scale factor and the age of the Universe.

### Flat universe, radiation only

By similar reasoning, we show that for a flat Universe dominated by radiation we have a different evolution of the scale factor:
$$
\label{eq:a_rad_only}
\frac{a(t)}{a_0} = \left( 2 H_0  t\right)^{1/2}
$$

### Empty universe (Milne)

Suppose that the Universe is empty, or at least with a total energy density much lower than the critical density. Then the Universe must be curved since in this case:
$$\Omega_k^0 = 1 - \Omega_m^0  - \Omega_r^0  - \Omega_\Lambda^0 \approx 1$$
This Universe is therefore hyperbolic[^ksign]. The first Friedmann equation is written:
$$
\frac{\dot{a}^2}{a^2}   = H_0^2 \Omega_k^0 \frac{a_0^2}{a^2} = H_0^2 \frac{a_0^2}{a^2}
$$
then:
$$ 
\dot a = \sqrt{a_0^2 H_0^2} = a_0 H_0
$$
Integration therefore gives a Universe expanding at constant velocity:
$$\label{eq:a_empty}
a(t) = a_0 H_0 t$$

:::{important}

The Hubble constant $H_0$ appears in the three previous Universe models. The expansion rate of the Universe today is not a prediction of the models but external data, when integrating Friedmann's differential equations.
:::

Multi-component models
----------------------

Modern cosmology was born with General Relativity. Since the writing of these equations, scientists have begun to mathematically describe the universe as a physical system. Many models have been proposed to describe the different histories of the universe.

### Eddington-Lemaître model (1927)

:::{exercise} Lemaître model
:label: exo:lemaitre

Friedmann and Lemaître were the first cosmologists to independently propose non-static universe models with arbitrary curvatures. Friedmann's equations have been extensively studied in this course, but Lemaître was the first to propose the idea that the Universe developed from a primeval atom. His model is based on a universe composed only of cold matter, with a cosmological constant and arbitrary spatial curvature (no radiation).

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
\begin{equation}\label{eq:lemaitre}
\frac{\dot{a}^2}{a^2} = H_0^2\left[\Omega_m^0 \left(\frac{a_0}{a}\right)^{3} + \Omega_\Lambda^0 + \Omega_k^0 \left(\frac{a_0}{a}\right)^{2}\right] \Leftrightarrow \dot{a}^2 = H_0^2\left[\Omega_m^0 \frac{a_0^3}{a} + \Omega_\Lambda^0 a^2 + \Omega_k^0 a_0^2 \right]
\end{equation}
At $t\approx 0$, the Universe was extremely small so the matter term dominates:
\begin{equation}
\dot a^2 \approx H_0^2\left[\Omega_m^0 \frac{a_0^3}{a}\right] \Leftrightarrow \sqrt{\frac{a}{a_0}}\frac{\dot{a}}{a_0}= H_0 \sqrt{\Omega_m^0} \Leftrightarrow \frac{a(t)}{a_0} = \left(\frac{3}{2}H_0\sqrt{\Omega_m^0}t\right)^{2/3}
\end{equation}

2. Then, after a certain time, $a$ becomes large and the cosmological constant term dominates:
\begin{equation}
\dot{a}^2 \approx H_0^2\left(\Omega_\Lambda^0 a^2\right) \Leftrightarrow \dot{a}= H_0 \sqrt{\Omega_\Lambda^0} a(t) \Rightarrow a(t) \propto e^{H_0\sqrt{\Omega_\Lambda^0}t}
\end{equation}

3. By differentiating equation [](#eq:lemaitre), we find that:
\begin{equation}
2\dot{a}\ddot{a} = H_0^2\left[ -\dot{a}\Omega_m^0 \frac{a_0^3 }{a^{2}} + 2 \dot{a} a \Omega_\Lambda^0 \right] \Leftrightarrow \frac{\ddot{a}}{a_0} = \frac{H_0^2}{2}\left[2 \Omega_\Lambda^0 \left(\frac{a}{a_0}\right) - \Omega_m^0\left(\frac{a_0}{a}\right)^2\right]
\end{equation}
When $a$ is small, we find that $\ddot{a}$ is negative and the expansion decelerates. However, when $a$ is large, $\ddot{a}>0$ and the expansion of the universe accelerates. The transition occurs at:
\begin{equation}
\ddot{a}=0 \Leftrightarrow 0=\frac{H_0^2}{2}\left[2 \Omega_\Lambda^0 \frac{a_*}{a_0} - \frac{\Omega_m^0a_0^2}{a_*^2}\right] \Leftrightarrow \frac{a_*}{a_0} = \left( \frac{\Omega_m^0}{2\Omega_\Lambda^0}\right)^{1/3}
\end{equation}
For the $\Lambda$CDM model with $\Omega_m^0\approx 0.3$ and $\Omega_\Lambda^0\approx 0.7$, we have $a_*/a_0 \approx 0.6$ hence a transition redshift at $z\approx 0.67$.
:::

### $\Lambda$CDM

The expansion of the Universe is today well described by the flat $\Lambda$CDM model ($\Omega_k^0=0$). The proportions of each of these components are today evaluated at {cite}`Planck2018`:
$$\Omega_\Lambda^0 = 0.685,\quad \Omega_m^0=0.315$$
Concerning cold matter, this can be separated into two contributions: dark matter $\Omega_{c}^0=0.264$ and baryonic matter[^baryons] $\Omega_b^0=0.049$.

Mechanical analogy
------------------

:::{exercise} Mechanical analogy
:label: exo:analogmeca

1. Write the first Friedmann equation as follows:
\begin{equation}
\frac{1}{2}\Omega_k^0 = f(\Omega_i^0,a)
\end{equation}
Interpret this equation by analogy with the mechanical energy conservation equation of a massive body following one-dimensional motion, and describe the role of each "potential energy" term.

2. Derive this equation with respect to time and make the analogy with Newton's law applied to a massive body in one-dimensional motion. Again analyze the role of each "force" term.

In what follows, we neglect the radiation component. Plot the potential energy terms as a function of the scale factor $a$ and describe the fate of the following universes.

3. Spherical model ($k=+1$) with $\Lambda=4\pi \GN \rho_m / c^2$ (show that Einstein's static model is a special case of this model and that it is unstable).

4. Matter-only models with different signs of curvature (the Einstein-de Sitter model corresponds to the case of flat curvature).

5. $\Lambda$CDM models with different signs for the cosmological constant and arbitrary curvatures (calculate the transition scale factor $a_*$ between deceleration and acceleration of expansion).

:::

:::{solution} exo:analogmeca
:class: dropdown

1. In terms of $\Omega_i^0$, the first Friedmann equation is written:
\begin{equation}
H^2 = \left(\frac{\dot{a}}{a}\right)^2 = H_0^2 \left( \frac{\Omega_m^0}{a^3} + \frac{\Omega_r^0}{a^4} + \Omega_\Lambda^0 + \frac{\Omega_k^0}{a^2} \right)
\end{equation}
which gives
\begin{equation}
\frac{1}{2}\Omega_k^0 = \frac{1}{2}\frac{\dot{a}^2}{H_0^2} - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{2}\frac{\Omega_r^0}{a^2} - \frac{1}{2}\Omega_\Lambda^0 a^2
\end{equation}

This last equation resembles the mechanical energy conservation equation for a massive body following one-dimensional motion. Let's make the analogy:
- $\frac{1}{2}\Omega_k^0$ is constant with $a$ can be identified as the conserved mechanical energy of the massive body
- $\frac{1}{2}\frac{\dot{a}^2}{H_0^2}$ represents the kinetic energy of the massive body.
- $- \frac{1}{2}\frac{\Omega_m^0}{a}$ resembles a gravitational potential centered around $a=0$.
- $ -\frac{1}{2}\frac{\Omega_r^0}{a^2}$ is another type of attractive potential.
- $- \frac{1}{2}\Omega_\Lambda^0 a^2$ is an inverted harmonic potential (repulsive) centered around $a=0$.

2. \begin{equation}
\frac{\ddot{a}}{H_0^2} = - \frac{1}{2}\frac{\Omega_m^0}{a^2 } -\frac{\Omega_r^0}{a^3 } + \Omega_\Lambda^0 a
\end{equation}
This equation resembles Newton's law applied to a massive body in one-dimensional motion. Let's make the analogy:
- $\frac{\ddot{a}}{H_0^2}$ acceleration of the massive body
- $- \frac{1}{2}\frac{\Omega_m^0}{a^2 }$ gravitational force (attractive)
- $+ \Omega_\Lambda^0 a$ repulsive elastic force

Let's define:
\begin{equation}
V_{\rm eff}(a) = - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{2}\Omega_\Lambda^0 a^2
\end{equation}

3. In this universe model, we have $\Omega_\Lambda^0 = \Omega_m^0 / 2$ and:
\begin{equation}
V_{\rm eff}(a) = - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{4}\Omega_m^0 a^2
\end{equation}
\begin{equation}
\frac{\dd V_{\rm eff} }{\dd a}= 0 \Rightarrow \left(\frac{1}{a^2}-a\right)\Omega_m^0 = 0 \Rightarrow a=1\text{ (today)}
\end{equation}
At $a=1$ or $t=0$, the first Friedmann equation gives:
\begin{equation}
1 = \Omega_m^0 + \Omega_\Lambda^0 + \Omega_k^0 \Rightarrow \Omega_k^0 = 1 - \frac{3}{2}\Omega_m^0
\end{equation}
The model is spherical so $\Omega_k^0 = -k c^2 / H_0^2 < 0$ with $k=+1$ which implies that $\Omega_m^0 > 2/3$. In Einstein's Universe, $\Omega_m^0=1$.

```{figure} #E-spherical
:width: 60%
:align: center
:label:fig:einstein

Potential energies in the case of a spherical universe with $\Omega_m^0=1$.
```

According to figure [](#fig:einstein), Einstein's solution at $a=a_0$ is unstable.

4.  
```{list-table} Potential energies in the case of matter-only models with different curvatures: (top left), $\Omega_m^0=1.5\Rightarrow k=+1$ (top right), $\Omega_m^0=0.5\Rightarrow k=-1$ (bottom)
:header-rows: 1
:name: fig:analogmeca

* - $\Omega_m^0=1\Rightarrow k=0$
  - $\Omega_m^0=1.5\Rightarrow k=+1$
  - $\Omega_m^0=0.5\Rightarrow k=-1$

* - :::{image} #EdS-Om1
    :alt: galaxies
    :width: 100%
    :align: center
    
    :::
  - :::{image} #EdS-Om15
    :alt: light
    :width: 100%
    :align: center
    
  - :::{image} #EdS-Om05
    :alt: light
    :width: 100%
    :align: center
```

In these models, the curvature is again given by:
\begin{equation}
1 = \Omega_m^0 + \Omega_k^0 \Rightarrow \Omega_k^0 = 1 -\Omega_m^0 \Rightarrow 
\left\lbrace\begin{array}{ll}
k=+1 & \text{ if } \Omega_m^0 > 1\\
k=0 & \text{ if } \Omega_m^0 = 1 \\
k=-1 & \text{ if } \Omega_m^0 < 1 
\end{array}\right.
\end{equation}

By analyzing the three plots in figure [](#fig:analogmeca), we can say that a spherical universe composed only of matter will necessarily collapse at some point, regardless of its initial conditions (necessity for Einstein to add the cosmological constant). A flat expanding universe extends indefinitely and asymptotically stops its expansion at $t\rightarrow \infty$. A hyperbolic expanding universe also extends to infinity.

5. The transition scale factor is given by: 
\begin{equation}
\frac{d V_{\rm eff} }{da}= 0 \rightarrow a_* = \left(\frac{\Omega_m^0}{2 \Omega_\Lambda^0}\right)^{1/3}
\end{equation}

```{list-table} Potential energies in the case of $\Lambda$CDM models with different parameters
:header-rows: 0
:name: fig:analogmeca-LCDM

* - $\Omega_m^0=0.3, \Omega_\Lambda^0=0.7$
  - $\Omega_m^0=0.3, \Omega_\Lambda^0=1.5$

* - :::{image} #LCDM-Om03OL07
    :width: 100%
    :align: center
    
    :::
  - :::{image} #LCDM-Om03OL15
    :width: 100%
    :align: center

* - $\Omega_m^0=0.3, \Omega_\Lambda^0=0.5$
  - $\Omega_m^0=0.3, \Omega_\Lambda^0=-0.7$

* - :::{image} #LCDM-Om03OL05
    :width: 100%
    :align: center
    
    :::
  - :::{image} #LCDM-Om03OL-07
    :width: 100%
    :align: center
    
```

Depending on the parameter values, the transition scale occurs in the future or in the past. If the cosmological constant is positive, expanding universes have decelerated expansion and, after the transition scale, accelerated expansion. If the cosmological constant is negative, the universe must collapse after some time.

Why is the Universe therefore expanding today? This depends entirely on initial conditions, so in particular because the universe was born from a Big Bang. And why was there a Big Bang? One can let one's imagination run free: brane collisions, God, pan-dimensional mice... but the answer is not (yet) given by physical sciences.

:::

Evolution of cosmological parameters
------------------------------------

:::{figure} #omegas
:width: 100%
:align: center
:label: fig:omegas

Evolution of cosmological parameters.
:::

:::{important} Key points

- The integration of the first Friedmann equation by injecting the evolution properties of different fluids allows us to obtain the evolution of the scale factor as a function of time.

- Whether with relativistic matter, non-relativistic matter or for an empty Universe, we obtain functions that increase with time since we measure $H_0>0$, thus scenarios of expanding universes.

- Writing the first Friedmann equation in the form of an equation analogous to energy conservation in classical mechanics provides intuition about the evolution of a Universe as a function of the different components present. Among other things, non-relativistic matter restrains expansion through its attractive gravitational effect, while a positive cosmological constant leads to an acceleration of expansion in the future.

:::

:::{seealso} To go further

- Other historical cosmological models: <wiki:Einstein%27s_static_universe>, <wiki:De_Sitter_universe>

- Standard model of cosmology $\Lambda$CDM: <wiki:Lambda-CDM_model>

:::

[^ksign]: The sign of $k$ is the inverse of the sign of $\Omega_k^0$.
[^baryons]: Baryonic matter is ordinary matter composed of protons and neutrons.
[^Mach]: In theoretical physics, particularly in discussions of gravitational theories, Mach's principle is the name given by Einstein to an imprecise hypothesis often attributed to physicist and philosopher Ernst Mach. The idea is that local inertial frames are determined by the large-scale distribution of matter.
