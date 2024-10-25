---
short_title: Cosmological models
authors:
  - jneveu
keywords: cosmological models, EdS model, mechanical analogy
---

Cosmological models
=======================

Simple models
---------------

Now that we have a model to describe the dynamics of the Universe, let's calculate its evolution in a few simple cases for practice.

### Flat Universe, matter only

Let's start with the case of a flat Universe, containing only non-relativistic matter. This is the so-called Einstein-Sitter model. It's the simplest we could think of in 1930. The first Friedmann equation is written:
$$ \begin{align*}
& 3 \frac{\dot{a}^2}{a^2} = 8 \pi \GN \rho_m = 8 \pi \GN \rho_m^0 \left(\frac{a_0}{a}\right)^{3} 
& \Leftrightarrow (\dot a)^2 = 8 \pi \GN \rho_m^0 a_0^3 / 3 a = H_0^2 \Omega_m^0 \frac{a_0^3}{a}
\end{align*}
$$
Before integrating this differential equation, let's remember that the energy density parameters are linked by a closure relation [](#eq:omega_sum). Therefore, in a flat Universe with only matter, we have $\Omega_m^0=1$. Now let's integrate the differential equation:
$$  
\sqrt{\frac{a}{a_0}} \frac{\dd a}{a_0} = H_0 \dd t \Rightarrow \left(\frac{a}{a_0}\right)^{3/2} = \frac{3}{2}H_0 t $$
$$
\label{eq:a_matiere_only}
\Rightarrow \frac{a(t)}{a_0} = \left( \frac{3}{2}H_0 t\right)^{2/3}$$
with at the beginning of the Universe $t=0$ and $a=0$. We have thus obtained a direct relationship between the scale factor and the age of the Universe.

### Flat Universe, radiation only

Using similar reasoning, we show that for a flat Universe dominated by radiation, we have a different evolution of the scale factor:
$$
\label{eq:a_rad_only}
\frac{a(t)}{a_0} = \left( 2 H_0 t\right)^{1/2}
$$

### Empty Universe (Milne)

Let's assume that the Universe is empty, or at least with a total energy density very low compared to the critical density. Then the Universe must be curved, since in this case :
$$\Omega_k^0 = 1 - \Omega_m^0 - \Omega_r^0 - \Omega_\Lambda^0 \approx 1$$.
This Universe is therefore hyperbolic [^ksign]. The first Friedmann equation is written :
$$
\frac{\dot{a}^2}{a^2} = H_0^2 \Omega_k^0 \frac{a_0^2}{a^2}
$$
then :
$$ 
\dot a = \sqrt{a_0^2 H_0^2 \Omega_k^0} = a_0 H_0
$$
Integration gives a Universe expanding at constant speed:
$$\label{eq:a_empty}
a(t) = a_0 H_0 t$$

:::{important}

The Hubble constant $H_0$ appears in all three previous Universe models. The expansion rate of the Universe today is not a prediction of the models but an external datum, during the integration of the Friedmann differential equations.
:::



Historical models
-------------------

Modern cosmology was born of General Relativity. Since the writing of these equations, scientists have begun to describe the universe mathematically as a physical system. Numerous models have been proposed to describe the different histories of the universe. In this chapter, we will review some of them.


### Einstein's first model (1917)

:::{exercise} First cosmological models
:label: exo:einstein_first


Einstein was the first to build a model for the universe as a whole, in 1917. He believed in a static, bounded universe containing only matter.

1. From a modern perspective, using Friedmann's equations (below), show that a static universe containing only matter must have a non-zero cosmological constant $\Lambda=4\pi G \rho_m / c^2$ and must be spherical. Calculate the radius of Einstein's spherical universe $R\equiv a_{\rm Einstein}$.

\begin{equation} \left\lbrace
\begin{array}{l}
   \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{c^2k}{a^2} \right) = 8\pi \GN \rho_m + c^2 \Lambda}  \\ 
    \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{a^2} = - 8\pi \GN \frac{P}{c^2} + c^2 \Lambda }
\end{array}
\right.
\end{equation}

2. Using Friedmann's equations, show that this spherical universe is unstable. Consider a perturbation $\delta R$ of the radius of the universe and $\delta \rho$ of the density of matter to calculate the evolution of the radius.

:::


:::{solution} exo:einstein_first
:class: dropdown

1. For a universe with only non-relativistic matter, $P_m=0$. If it is static, then $\ddot{a}=\dot{a}=0$ and Friedmann's second equation is written :
\begin{equation}
\frac{c^2 k}{a^2}=c^2 \Lambda
\end{equation}
Injecting this equation into the first Friedmann equation gives :
\begin{align}
3 \frac{c^2 k}{a^2} = 8 \pi G \rho_m + c^2 \Lambda & \Leftrightarrow 2 c^2 \Lambda = 8 \pi G \rho_m \
& \Leftrightarrow \Lambda = 4 \pi G \rho_m / c^2 > 0 
\end{align}
So, to obtain a static universe, Einstein had to introduce a non-zero cosmological constant. Moreover, we deduce that $c^2 k / a^2 > 0$ so $k=+1$: the static universe must be spherical. Einstein originally argued that the universe should be bounded using Mach's principle[^Mach], so the solution of a spherical universe seemed satisfactory from this point of view. 

The scale factor can be associated with the radius of the spherical universe. Using the second Friedmann equation, we find that the value of the radius is :
\begin{equation}
R\equiv a_E = \Lambda^{-1/2}
\end{equation}

2. Combining the two Friedmann equations for a universe with cold matter only, we find:
\begin{equation}
\frac{2 \ddot{a}}{a} = - \frac{8\pi G \rho}{3} + \frac{2 c^2 \Lambda}{3}
\end{equation}
Let's consider a perturbation of the radius, $a=\Lambda^{-1/2} + \delta a$, which induces a perturbation of the density of matter on the sphere $\rho_m = \rho_0 + \delta \rho = c^2 \Lambda/4 \pi G + \delta \rho$. This last equation becomes
\begin{align}
2 \frac{\delta \ddot{a}}{a} = - \frac{2 c^2 \Lambda}{3} - \frac{8 \pi G \delta \rho}{3 c^2}+ \frac{2 c^2 \Lambda}{3} 
 = - \frac{8 \pi G \delta \rho}{3 c^2}
\end{align}
Now the quantity of matter is conserved, so we also have :
$$\rho a^3 = cste \Rightarrow \frac{\delta \rho}{\rho} = -3 \frac{\delta a}{a}$$
and :
\begin{equation}
\delta \ddot{a} = 4 \pi G \rho_0 \delta a \Leftrightarrow \delta \ddot{a} - c^2 \Lambda \delta a = 0
\end{equation}
i.e. the perturbation $\delta a$ grows exponentially with time ($\Lambda>0$). The universe is unstable.


:::


### Universe with only one cosmological constant (de Sitter, 1917)

:::{exercise} de Sitter's model
:label: exo:desitter

Shortly after Einstein in 1917, de Sitter published another type of cosmological model. He proposed a flat universe with only a non-zero cosmological constant and no matter inside (or a negligible amount of matter). 
1. Show that such a universe grows exponentially with time. This is the de Sitter universe. 
2. Also find a coordinate system in which it is static. 


:::

:::{solution} exo:desitter
:class: dropdown


1. In a flat universe $k=0$ and the first Friedmann equation gives in Sitter's model :
\begin{equation}
\frac{\dot{a}^2}{a^2} = \frac{c^2 \Lambda}{3} \Leftrightarrow -\sqrt{\frac{3}{c^2 \Lambda}}\frac{\dd a }{\dd t}+a=0
\end{equation}
The solution of this differential equation is
\begin{equation}
a(t) = a_0 e^{sqrt{c^2 \Lambda/3}t}
\end{equation}
The de Sitter universe grows exponentially with time. 

2. To show that a de Sitter universe can be considered a static universe, let's write $T_0 = \sqrt{c^2 \Lambda / 3}$ and change the coordinates $r'(t) = a_0 e^{t/T_0}\sigma$. The FLRW metric then becomes
\begin{equation}
\dd s^2 =- \dd t^2 + a^2 (\dd \sigma^2 + \sigma^2 \dd \theta^2 + \sigma^2 \sin\theta \dd \phi^2) =- \dd t^2 + \left[\left(\dd r' - r' \dd t / T_0\right)^2 + r'^2 \dd \theta^2 + r'^2 \sin\theta \dd \phi^2\right]
\end{equation}
Using the transformation :
\begin{equation}
t = t' + \frac{T_0}{2}\log \left( \frac{r'^2}{T_0^2} - 1 \right) 
\end{equation}
we find :
\begin{equation}
\dd s^2 = \left(1-\frac{r'^2}{T_0^2}\right) \dd t'^2 - \left(1-\frac{r'^2}{T_0^2}\right)^{-1} \dd r'^2 - r'^2 \dd \theta^2 -r'^2 \sin\theta \dd \phi^2 
\end{equation}
Historically, Sitter's model was discovered as a static universe with this coordinate system, whose shape closely resembles Schwarzschild's solution. As soon as the idea of an expanding universe was accepted by the scientific community, Sitter's universe was considered in its dynamical form, as an exponentially expanding universe dominated by the cosmological constant.

:::

### Eddington-Lemaître model (1927)


:::{exercise} Lemaître model
:label: exo:lemaitre

Friedmann and Lemaître were the first cosmologists to independently propose non-static models of universes with arbitrary curvatures. Friedmann's equations have been extensively studied in this course, but Lemaître was the first to propose the idea that the Universe developed from a primitive atom. His model is based on a universe composed entirely of cold matter, with a cosmological constant and arbitrary spatial curvature (no radiation). 

1. In such a model, show that, just after a big bang at $t=0$, at the beginning of the universe the scale factor increases as :
\begin{equation}
\frac{a(t)}{a_0} =\left( \frac{3}{2}H_0\sqrt{\Omega_m^0}t\right)^{2/3}
\end{equation}

2. As the universe expands, however, the energy density of matter decreases and the cosmological constant eventually dominates. Show that, for large $t$, the scale factor increases as :
\begin{equation}
a(t) \propto e^{H_0\sqrt{\Omega_\Lambda^0}t}
\end{equation}

3. Calculate $\ddot{a}$ and show that the expansion of the universe first decelerates, then accelerates. Calculate $a_*$ the scale factor at the transition.

:::

:::{solution} exo:lemaitre
:class: dropdown

1. In the single-matter Lemaître model, the first Friedmann equation is written :
\begin{equation}\label{eq:lemaitre}
\frac{\dot{a}^2}{a^2} = H_0^2\left[\Omega_m^0 \left(\frac{a_0}{a}\right)^{3} + \Omega_\Lambda^0 + \Omega_k^0 \left(\frac{a_0}{a}\right)^{2}\right] \Leftrightarrow \dot{a}^2 = H_0^2\left[\Omega_m^0 \frac{a_0^3}{a} + \Omega_\Lambda^0 a^2 + \Omega_k^0 a_0^2 \right]
\end{equation}
At $t\approx 0$, the Universe was extremely small so the matter term dominates:
\begin{equation}
\dot a^2 \approx H_0^2\left[\Omega_m^0 \frac{a_0^3}{a}\right] \Leftrightarrow \sqrt{\frac{a}{a_0}}\frac{\dot{a}}{a_0}= H_0 \sqrt{\Omega_m^0} \Leftrightarrow \frac{a(t)}{a_0} = \left(\frac{3}{2}H_0\sqrt{\Omega_m^0}t\right)^{2/3}
\end{equation}

2. Then, after some time, $a$ becomes large and the cosmological constant term dominates:
\begin{equation}
\dot{a}^2 \approx H_0^2\left(\Omega_\Lambda^0 a^2\right) \Leftrightarrow \dot{a}= H_0 \sqrt{\Omega_m^0} a(t) \Rightarrow a(t) \propto e^{H_0\sqrt{\Omega_\Lambda^0}t}
\end{equation}

3. Deriving equation [](#eq:lemaitre), we find that :
\begin{equation}
2\dot{a}\ddot{a} = H_0^2\left[-\dot{a}\Omega_m^0 \frac{a_0^3 }{a^{2}} + 2 \dot{a} a \Omega_\Lambda^0 \right] \Leftrightarrow \frac{\ddot{a}}{a_0} = \frac{H_0^2}{2}\left[2 \Omega_\Lambda^0 \left(\frac{a}{a_0}\right) - \Omega_m^0\left(\frac{a_0}{a}\right)^2\right]
\end{equation}
When $a$ is small, we see that $\ddot{a}$ is negative and expansion decelerates. However, when $a$ is large, $\ddot{a}>0$ and the expansion of the universe accelerates. The transition occurs at :
\begin{equation}
\ddot{a}=0 \Leftrightarrow 0=\frac{H_0^2}{2}\left[2 \Omega_\Lambda^0 \frac{a_*}{a_0} - \frac{\Omega_m^0a_0^2}{a_*^2}\right] \Leftrightarrow \frac{a_*}{a_0} = \left( \frac{\Omega_m^0}{2\Omega_\Lambda^0}\right)^{1/3}
\end{equation}
For the $\Lambda$CDM model with $\Omega_m^0\approx 0.3$ and $\Omega_\Lambda^0\approx 0.7$, we have $a_*/a_0 \approx 0.6$ hence a transition redshift to $z\approx 0.67$.
:::


Mechanical analogy
-------------------

:::{exercise} Mechanical analogy
:label: exo:analogmeca

1. Write the first Friedmann equation as follows:
\begin{equation}
\frac{1}{2}\Omega_k^0 = f(\Omega_i^0,a)
\end{equation}
Interpret this equation by analogy with the equation for the conservation of mechanical energy of a massive body in one-dimensional motion, and describe the role of each “potential energy” term.

2. Derive this equation with respect to time and make the analogy with Newton's law applied to a massive body in one-dimensional motion. Analyze again the role of each “force” term.

In what follows, we neglect the radiation component. Plot the potential energy terms as a function of the scale factor $a$ and describe the fate of the following universes.

3. Spherical model ($k=+1$) with $\Lambda=4\pi \GN \rho_m / c^2$ (show that Einstein's static model is a special case of this model and is unstable).

4. Matter-only models with different signs of curvature (the Einstein-de Sitter model corresponds to the case of flat curvature).

5. $\Lambda$CDM models with different signs for the cosmological constant and arbitrary curvatures (calculate the transition scale factor $a_*$ between expansion deceleration and acceleration).

:::


:::{solution} exo:analogmeca
:class: dropdown


1. In terms of $\Omega_i^0$, the first Friedmann equation is written :
\begin{equation}
H^2 = \left(\frac{\dot{a}}{a}\right)^2 = H_0^2 \left( \frac{\Omega_m^0}{a^3} + \frac{\Omega_r^0}{a^4} + \Omega_\Lambda^0 + \frac{\Omega_k^0}{a^2} \right)
\end{equation}
which gives
\begin{equation}
\frac{1}{2}\Omega_k^0 = \frac{1}{2}\frac{\dot{a}^2}{H_0^2} - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{2}\frac{\Omega_r^0}{a^2} - \frac{1}{2}\Omega_\Lambda^0 a^2
\end{equation}

This last equation resembles the equation for the conservation of mechanical energy for a massive body in one-dimensional motion. Let's make the analogy:
- $\frac{1}{2}\Omega_k^0$ is constant with $a$ can be identified as the conserved mechanical energy of the massive body.
- $\frac{1}{2}\frac{\dot{a}^2}{H_0^2}$ represents the kinetic energy of the solid body.
- $\frac{1}{2}\frac{\Omega_m^0}{a}$ resembles a gravitational potential centered around $a=0$.
- $\frac{1}{2}\frac{\Omega_r^0}{a^2}$ is another type of attractive potential.
- $\frac{1}{2}\Omega_\Lambda^0 a^2$ is an inverted harmonic potential (repulsive) centered around $a=0$.

2. \begin{equation}
\frac{ddot{a}}{H_0^2} = - \frac{1}{2}\frac{\Omega_m^0}{a^2 } -\frac{\Omega_r^0}{a^3 } + \Omega_\Lambda^0 a
\end{equation}
This equation resembles Newton's law applied to a massive body in one-dimensional motion. Let's make the analogy:
- $\frac{ddot{a}}{H_0^2}$ acceleration of the solid body
- $\frac{1}{2}\frac{\Omega_m^0}{a^2 }$ gravitational force (attractive)
- $\Omega_\Lambda^0 a$ elastic repulsive force

Let's define :
\begin{equation}
V_{\rm eff}(a) = - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{2}\Omega_\Lambda^0 a^2
\end{equation}

3. In this universe model, we have $\Omega_\Lambda^0 = \Omega_m^0 / 2$ and :
\begin{equation}
V_{\rm eff}(a) = - \frac{1}{2}\frac{\Omega_m^0}{a} - \frac{1}{4}\Omega_m^0 a^2
\end{equation}
\begin{equation}
\frac{\dd V_{\rm eff} }{\dd a}= 0 \Rightarrow \left(\frac{1}{a^2}-a\right)\Omega_m^0 = 0 \Rightarrow a=1\text{ (today)}
\end{equation}
At $a=1$ or $t=0$, the first Friedmann equation gives :
\begin{equation}
1 = \Omega_m^0 + \Omega_\Lambda^0 + \Omega_k^0 \Omega_k^0 = 1 - \frac{3}{2}\Omega_m^0
\end{equation}
The model is spherical so $\Omega_k^0 = -k c^2 / H_0^2 < 0$ with $k=+1$ which implies that $\Omega_m^0 > 2/3$. In Einstein's Universe, $\Omega_m^0=1$.

```{figure}#E-spherical
:width: 60%
:align: center
:label:fig:einstein

Potential energies for a spherical universe with $\Omega_m^0=1$.
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

In these models, curvature is again given by :
\begin{equation}
1 = \Omega_m^0 + \Omega_k^0 \Rightarrow \Omega_k^0 = 1 -\Omega_m^0 \Rightarrow 
\left\lbrace\begin{array}{ll}
k=+1 & \text{ if } \Omega_m^0 > 1\\\\
k=0 & \text{ if } \Omega_m^0 = 1 \\\\
k=-1 & \text{ if } \Omega_m^0 < 1 
\end{array}\right.
\end{equation}

By analyzing the three plots in figure [](#fig:analogmeca), we can say that a spherical universe composed solely of matter will necessarily collapse at some point, whatever its initial conditions (Einstein's need to add the cosmological constant). An expanding flat universe expands indefinitely and asymptotically stops expanding at $t\rightarrow \infty$. An expanding hyperbolic universe also expands to infinity.

5. The transition scale factor is given by : 
\begin{equation}
\frac{d V_{\rm eff} }{da}= 0 \rightarrow a_* = \left(\frac{\Omega_m^0}{2 \Omega_\Lambda^0}\right)^{1/3}
\end{equation}

```{list-table} Potential energies in the case of single-matter models with different curvatures: (top left), $\Omega_m^0=1.5\Rightarrow k=+1$ (top right), $\Omega_m^0=0.5\Rightarrow k=-1$ (bottom)
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

Depending on the parameter values, the transition scale occurs in the future or in the past. If the cosmological constant is positive, expanding universes have a decelerated expansion and, after the transition scale, an accelerated expansion.  If the cosmological constant is negative, the universe must collapse after a certain time.

So why is the Universe expanding today? That depends entirely on the initial conditions, and in particular on whether the universe was born of a Big Bang. And why was there a Big Bang? We can let our imaginations run wild: brane collisions, God, pan-dimensional mice... but the answer is not (yet) given by the physical sciences.

:::




Age of the Universe
------------------

:::{exercise} Age of the Universe
:label: exo:Uage

1. Calculate $a(t)$ and the age of the universe for three different models, assuming $H_0\approx 70\,\text{km/s/Mpc}$ :
- $\Omega_m^0=1, \Omega_\Lambda^0=0, \Omega_r^0 \approx 0$ (flat Einstein-de Sitter model)
- $\Omega_m^0=\Omega_\Lambda^0\approx 0, \Omega_r^0 \approx 0$ (empty universe)
- $\Omega_m^0=\Omega_r^0\approx 0, \Omega_\Lambda^0 = $1$ (flat model dominated by vacuum)

We need $1\,$Mpc$=3\times 10^{19}\,$km.

2. Which universe is the oldest? 

For a $\Lambda$CDM model with $32\%$ matter and $68\%$ dark energy, cosmologists estimate the age of the universe at $13.8\,\text{Gyr}$. This figure can be compared with the age of the oldest stars, which is measured at {cite:p}`hobson2006general`[p. 410] :
\begin{equation}
t_{\text{first stars}} = 11.5\pm 1.3\,\text{Gyr}
\end{equation}
 
3. Now assume that $H_0\approx 500\,$km/s/Mpc as originally estimated by Edwin Hubble. 
Calculate again the age of the universe for the first case, which was the most reasonable model at the time (flat, full of matter...). Conclude.


:::


:::{solution} exo:Uage
:class: dropdown


1. We use the first Friedmann equation :
\begin{equation}
H^2 = \left(\frac{1}{a}\frac{da}{dt}\right)^2 = H_0^2 \left[ \frac{\Omega_m^0}{a^3}+ \Omega_\Lambda^0+ \frac{\left(1-\Omega_m^0-\Omega_\Lambda^0\right)}{a^2}\right].
\end{equation}
because at $a(t_0)=1$ we still have $1=\Omega_k^0 + \Omega_m^0 + \Omega_\Lambda^0$.

- We have $\Omega_m^0=1, \Omega_\Lambda^0=0, \Omega_r^0 \approx 0$ then :
\begin{equation}
\frac{\dd a}{\dd t} = a H_0 \sqrt{\frac{\Omega_m^0}{a^3}+\Omega_\Lambda^0+ \frac{\left(1-\Omega_m^0-\Omega_\Lambda^0\right)}{a^2}} = a H_0 \sqrt{\frac{\Omega_m^0}{a^3}} = H_0 a^{-1/2} 
\end{equation}
With $t=0$ at the Big Bang, 
\begin{equation}
\sqrt{a}\dd a = H_0 \dd t \Rightarrow \int_0^a \sqrt{a'}\dd a' = H_0 \int_0^t \dd t' \Rightarrow \frac{2}{3}a^{3/2} = H_0 t
\end{equation}
We thus obtain :
\begin{equation}
a(t) = \left( \frac{3}{2}H_0 t\right)^{2/3}\quad\text{and}\quad t_U = \frac{2}{3}\frac{1}{H_0} = 9.1\,\text{Gyr} 
\end{equation}
with :
\begin{equation}
\frac{1}{H_0} = \frac{1}{70\,\text{km/s/Mpc}}= 4.3\times 10^{17}\,\text{s} = 13.6\,\text{Gyr} 
\end{equation}

- $\Omega_m^0=\Omega_\Lambda^0\approx 0,\Omega_r^0 \approx 0$ then :
\begin{equation}
\frac{\dd a}{\dd t} = a H_0 \sqrt{\frac{\left(1-\Omega_m^0-\Omega_\Lambda^0\right)}{a^2}} = a H_0 \frac{\sqrt{1}}{a} = H_0 
\end{equation}
With $t=0$ at the Big Bang, 
\begin{equation}
a(t) = H_0 t \Rightarrow t_U = \frac{1}{H_0} = 13.6\,\text{Gyr} 
\end{equation}

- $\Omega_m^0=\Omega_r^0\approx 0, \Omega_\Lambda^0 = 1$ then:
\begin{equation}
\frac{da}{dt} = a H_0 \sqrt{\Omega_\Lambda^0} 
\end{equation}
With $t=t_0$ now, 
\begin{equation}
\frac{\dd a}{a} = H_0 \sqrt{\Omega_\Lambda^0} \dd t \Rightarrow \int_a^{a_0} \frac{\dd a'}{a'} = H_0 \sqrt{\Omega_\Lambda^0} \int_t^{t_0} \dd t' \Rightarrow a(t) = a_0 e^{H_0 \sqrt{\Omega_\Lambda^0} (t- t_0)}
\end{equation}
We have $a(t)\Rightarrow 0$ when $t\rightarrow -\infty$ so the age of the universe is infinite in Sitter's model.

2. Einstein de-Sitter's value is incompatible with measuring the age of the first stars with such a value of $H_0$. However, the $\Lambda$CDM model agrees with the “empty universe” model. However, in the “empty universe”, the assumption that matter plays no role is very strong.

3. 
\begin{equation}
\frac{1}{H_0} = \frac{1}{500\,\text{km/s/Mpc}}= 4.3\times 10^{17}\,\text{s} = 1.9\,\text{Gyr} 
\end{equation}

The first measurement of the Hubble constant was incompatible with measurements of the Earth's age. Early cosmological models were therefore affected by this fact until the measurement of the constant $H_0$ was corrected.

:::


Evolution of cosmological parameters
------------------------------------


:::{figure} #omegas
:width: 100%
:align: center
:label: fig:omegas

Evolution of cosmological parameters.
:::


This will embed the output of a notebook cell

:::{note} Test
![](#om-slider)

:::


[^ksign]: The sign of $k$ is the inverse of the sign of $\Omega_k^0$.
[^Mach]: In theoretical physics, particularly in discussions of gravitational theories, the Mach principle 
is the name given by Einstein to an imprecise hypothesis often attributed to physicist and philosopher Ernst Mach. 
The idea is that local inertial frames are determined by the large-scale distribution of matter.

