---
short_title: The expanding Universe
authors:
  - jneveu
keywords: cosmological distances, scale factor, dark energy
---

The expanding Universe
======================

In the previous chapter, through simple geometrical considerations, we managed to write the form of the metric solution to Einstein's equation for a homogeneous and isotropic Universe. From an unknown tensor with 10 components (since the metric is a symmetric tensor), through symmetry arguments we arrived at the FLRW metric which contains only one unknown function of time $a(t)$. To now describe the dynamics of the Universe, and not just its geometry, we need to solve Einstein's equation in order to understand how the matter and energy content acts on the expansion of the Universe via the scale factor $a(t)$.


The energy-momentum tensor
----------------------------

### Definition in Special Relativity

For a set of $N$ particles, interacting or not with each other or with the outside, the four-momentum density $p^\mu$ of this set is defined by {cite:p}`Weinberg1972`[p. 43]:
$$
\sum_n p_n^{\mu}c\ \delta^{(3)}(\vec x - \vec x_n(t)) = T^{\mu 0}(t, \vec x) 
$$
where $\vec x_n(t)$ and $p_n^{\mu}(t)=(E_n/c, \vec p_n)$ are the positions and four-momenta of particle $n$ at time $t$. The volume current[^vecj] of momentum through a surface with normal $\vec e_i$ is:
$$
\sum_n p_n^{\mu} \frac{\dd x_n^i(t)}{\dd t} \delta^{(3)}(\vec x - \vec x_n(t)) = T^{\mu i}(t, \vec x)
$$
These two definitions can be combined to obtain a tensor with two indices:
$$
T^{\mu \nu}(t, \vec x) = \sum_n p_n^{\mu} \frac{\dd x_n^\nu(t)}{\dd t} \delta^{(3)}(\vec x - \vec x_n(t))
$$
with $x_n^0(t)=ct$. In the reference frame where this set of particles is at rest, the energy of a massive particle is $E_n= \gamma_n m^2 c^2$ (with $\gamma_n$ its Lorentz factor) and its momentum is $\vec p_n c = \gamma_n m \vec v_n c$: we then demonstrate that $p_n^\mu c = E_n (\dd x_n^\mu /c \dd t)$[^pcphoton]. Hence the expression of the energy-momentum tensor as a symmetric tensor in special relativity:
$$
T^{\mu \nu}(t, \vec x) = c^2 \sum_n \frac{p_n^{\mu} p_n^{\nu}}{E_n} \delta^{(3)}(\vec x - \vec x_n(t))\label{eq:TmunuGaz}
$$

:::{figure} ../../images/tmunu_def.svg

The energy-momentum tensor represents the volume currents of four-momenta $p^\mu$ and the energy density $\epsilon$ in a local volume of space-time. If the physical system studied in this local volume is subject to no working force other than gravitation, then we have the conservation equation $T^{\mu\nu}_{\;\;\;;\mu}=0$.
:::

The energy-momentum tensor $T^{\mu\nu}$ of Einstein's equation describes the energy density and volume fluxes of momentum in relativistic mechanics. It is a second-order tensor, constructed from the 4-momentum vector, which takes the following form:
\begin{equation}
T^{\mu\nu}=\begin{pmatrix} 
T^{00}= \text{energy density}\,\,\,\,
& T^{01}= \text{energy/c flux through }x_1\,\,\,\,\,
& T^{02}=\text{energy/c flux through }x_2\,\,\,\,\,
& T^{03}=\text{energy/c flux through }x_3
\\ T^{10}=c\times \text{density of }p_1,\,\,\,\,\,\,
& T^{11}= \text{flux of }p_1\text{ through }x_1\,\,\,\,\,\,\,
& T^{12}= \text{flux of }p_1\text{ through }x_2\,\,\,\,\,\,\,
& T^{13}= \text{flux of }p_1\text{ through }x_3
\\ T^{20}= c\times\text{density of }p_2\,\,\,\,\,\,\,\,
& T^{21}= \text{flux of }p_2\text{ through }x_1\,\,\,\,\,\,\,
& T^{22}= \text{flux of }p_2\text{ through }x_2\,\,\,\,\,\,\,
& T^{31}= \text{flux of }p_2\text{ through }x_3
\\ T^{30}= c\times\text{density of }p_3\,\,\,\,\,\,\,\,
& T^{31}= \text{flux of }p_3\text{ through }x_1\,\,\,\,\,\,\,
& T^{32}= \text{flux of }p_3\text{ through }x_2\,\,\,\,\,\,\,\,
& T^{33}= \text{flux of }p_3\text{ through }x_3
\end{pmatrix}
\label{stress-energy-tensor-meaning}
\end{equation}
If the physical system studied in this local volume is not subject to any working force other than gravitation, then we have the conservation equation $T^{\mu\nu}_{\;\;\;;\mu}=0$, a set of four equations representing the local conservation equation for energy and momentum. 

A few remarks on the components of this tensor:
 * $T^{00}$ is the local $\epsilon$ energy density, generally the dominant component of the energy-momentum tensor;
* $T^{ii}$ represent the flux of momentum through a surface, and hence the kinetic pressure $P$ exerted by the physical system in the $\vec e_i$ direction;
* $T^{ij},\ i \neq j$ represent volumic momentum flows orthogonally to displacements, i.e. viscosity or shear phenomena.

:::{note} Energy-momentum tensor in Special Relativity
:class: dropdown

For a set of $N$ particles, the quadri-impulse density $p^\mu$ is defined by {cite:p}`Weinberg1972`[p. 43]:
$$
T^{\mu 0}(t, \vec x) = \sum_n p_n^{\mu}c \delta^{(3)}(\vec x - \vec x_n(t))
$$
where $x_n(t)$ and $p_n^{\mu}(t)=(E_n/c, \vec p_n)$ are the positions and quadri-impulses of particle $n$ at time $t$. The momentum flux through a surface of normal $\vec e_i$ is :
$$
T^{\mu i}(t, \vec x) = \sum_n p_n^{\mu} \frac{\dd x_n^i(t)}{\dd t} \delta^{(3)}(\vec x - \vec x_n(t))
$$
These two definitions can be combined to obtain :
$$
T^{\mu \nu}(t, \vec x) = \sum_n p_n^{\mu} \frac{\dd x_n^\nu(t)}{\dd t} \delta^{(3)}(\vec x - \vec x_n(t))
$$
with $x_n^0(t)=ct$. Since the energy of a massive particle is $E=\sqrt{m^2\gamma^2 \vec v^2 c^2 + m^2 c^4}$ and that of a zero-mass particle is $E=\vert \vec p \vert c$, then we show that $p_n^\mu c = E_n (\dd x_n^\mu /c \dd t)$. Hence the energy-momentum tensor is written as a symmetrical tensor:
$$
T^{\mu \nu}(t, \vec x) = c^2 \sum_n \frac{p_n^{\mu} p_n^{\nu}}{E_n} \delta^{(3)}(\vec x - \vec x_n(t))\label{eq:TmunuGaz}
 $$

:::

Now, in our hypothesis of a Universe of maximum symmetry, let's first recall that we can define a cosmic, universal time, using the physical evolution of the Universe as a clock (matter density, CMB temperature...). The hypersurfaces of space-time parametrized by this universal time are then themselves subspaces of maximum symmetry. The $\mathcal{T}$ tensors representing the cosmological observables of such maximally symmetric subspaces must then be of _form invariant_, i.e. they remain the same functions of the spatial coordinates at a date $t$ whatever the chosen coordinate system: if we go from a $x^\rho$ system to $x'^\rho$, we must have $\mathcal{T}'_{\mu\nu\ldots}(x'^\rho) = \mathcal{T}_{\mu\nu\ldots}(x'^\rho)$. Intuitively, if $\mathcal{T}$ is the energy-momentum tensor, this means, among other things, that the energy density must be identical at all points for any choice of coordinate system {cite:p}`Weinberg1972`[p. 409]. We can then demonstrate an important property concerning the form that the tensors of these subspaces {cite:p}`Weinberg1972`[p. 392] must take.

:::{important} Structure of form-invariant tensors
A form-invariant tensor in a space of maximum symmetry :
- is position-independent if it is a scalar,
- is zero if it's a vector,
- is proportional to the metric tensor if it's a second-order tensor.
:::

:::{tip} Demonstration for a scalar tensor {cite:p}`Weinberg1972`[p. 392]
:class: dropdown

If $\mathcal{T}^{\mu\nu\ldots}$ transforms like a tensor and is form invariant, then :
$$
\label{eq:form_invariant}
\mathcal{T}_{\mu\nu\ldots}(x^\rho) =
\frac{\partial x'^\lambda}{\partial x^\mu}\frac{\partial x'^\sigma}{\partial x^\nu}\cdots \mathcal{T}'_{\lambda\sigma\ldots}(x'^\rho) = \frac{\partial x'^\lambda}{\partial x^\mu}\frac{\partial x'^\sigma}{\partial x^\nu}\cdots \mathcal{T}_{\lambda}{\sigma\ldots}(x'^\rho)
$$
For a scalar tensor $\mathcal{S}(x^\mu)$ :
$$
\label{eq:scalar_form_invariant}
\mathcal{S}(x^\rho) = \mathcal{S}(x'^\rho)
$$
Let be an infinitesimal spatial transformation:
$$x'^\rho = x^\rho + \epsilon \xi^\rho(x),\quad \vert\epsilon\vert \ll 1$$
then equation [](#eq:scalar_form_invariant) becomes to first order :
$$
0 = \xi^\lambda(x) \frac{\partial \mathcal{S}(x)}{\partial x^\lambda}
$$
Since $\mathcal{S}$ is maximally symmetrical, we're allowed to choose any non-zero $\xi^\lambda$ transformation, so :
$$
\frac{\partial \mathcal{S}(x)}{\partial x^\lambda} = 0
$$
so $\mathcal{S}$ of invariant form is not a function of space coordinates.

:::

Therefore, mathematically we can introduce $\epsilon(t)$ and $P(t)$ two functions of time such that the energy-momentum tensor simplifies into :
$$ \begin{align}
T^{00} & = \epsilon(t) &\quad \text{(scalar)} \\
T^{i0} & = T^{0i} = 0 & \quad \text{(vector)} \\
T^{ij} & = P(t) \gamma^{ij}& \quad \text{(second-order tensor)}
\end{align} $$

More elegantly, we can introduce the quadri-vector $U^\mu$ defined by :
$$ U^0 = 1, \quad U^i = 0 $$
and obtain a compact expression for the energy-momentum tensor of a homogeneous, isotropic Universe:
\begin{equation}
\label{eq:def-Tmunu2}
T^{\mu\nu} = (\epsilon + P) U^\mu U^\nu + P g^{\mu\nu}
\end{equation}
Using the FLRW metric, solution of a homogeneous and isotropic universe as well, the energy-momentum tensor is written :
\begin{equation}
\label{eq:def-Tmunu}
T^{\mu\nu} = (\epsilon + P) U^\mu U^\nu + P g^{\mu\nu} = 
\begin{pmatrix}
-\epsilon g^{00} & 0 & 0 & 0 \\
0 & P g^{11} & 0 & 0 \\
0 & 0 & P g^{22} & 0 \\
0 & 0 & 0 & P g^{33}  \\ 
\end{pmatrix} 
\end{equation}

In a Cartesian basis and flat space, the energy-momentum tensor takes the simple form:
\begin{equation}
\label{eq:tmunu_fluid}
T^{mu\nu} =  
\begin{pmatrix}
\epsilon & 0 & 0 & 0 \\
0 & P/a^2(t) & 0 & 0 \\
0 & 0 & P/a^2(t) & 0 \\
0 & 0 & 0 & P/a^2(t) \\
\end{pmatrix}.
\end{equation}

How should we interpret these mathematical considerations? Firstly, if we compare equation [](#eq:def-Tmunu) with [](#stress-energy-tensor-meaning) then we identify $\epsilon$ with energy density and $P$ with kinetic pressure (flow of momentum across a surface)[^epsP]. Next, the energy-momentum tensor $T^{\mu\nu}$ is identified with that of a <wiki:perfect_fluid>. This means that in a homogeneous, isotropic Universe, matter can be described as a continuous medium, whose evolution can be described without taking into account viscosity and thermal conduction effects. _The thermodynamic evolution of the Universe is therefore adiabatic._ Finally, $U^\mu$ is then identified with the comobile quadri-velocity of the fluid, so the fact that $U^i = 0$ shows that the physical system under study is at rest in the comobile coordinates, as expected. 


:::{note} Energy-momentum tensor of a perfect fluid {cite:p}`Weinberg1972`[p. 48]
:class: dropdown

Let's study a perfect fluid, i.e. a set of particles whose mean free path is small compared with the distances at which it is studied, and without viscosity. Given the definition of an energy-momentum tensor, in the $\mathcal{R}'$ frame of reference where the perfect fluid is at rest, we can write:
$$ T'^{ij} = P \delta^{ij}, \quad T'^{i0} = T'^{0i} = 0, \quad T'^{00} = \rho c^2 $$
where $\rho$ is explicitly the fluid's own _massic_ density and $P$ its kinetic pressure (i.e. a flow of momentum across a surface). In another reference frame, that of a flow observer for example, this energy-momentum tensor is rewritten:
$$ T^{\mu\nu} = \Lambda^{\mu}_{\;\alpha} \Lambda^{\nu}_{\;\beta} T^{\alpha\beta} $$
with $\Lambda^\mu_{\;\alpha}$ the Lorentz transformation defined by equation [](#eq:lorentz2). More explicitly:
$$ T^{ij} = P \delta^{ij} + (P + \rho c^2) \frac{v^i v^j}{c^2- v^2}, \quad T^{i0} = (P + \rho c^2) \frac{c v ^i}{c^2 - v^2}, \quad T^{00} = \frac{\rho c^4 + P v^2}{c^2 - v^2} $$

Let's define the quadri-velocity in comobile coordinates as follows:
$$ \vec U = \frac{ \dd \vec x }{c \dd \tau} = \frac{ \vec v / c }{ \sqrt{1-v^2}}, \quad U^0 = \frac{ \dd t }{ \dd \tau} = \frac{1 }{ \sqrt{1-v^2}}, \quad U^\mu U^\mu = -c^2 $$
then the tensor is written:
$$ T^{\mu\nu} = (\rho c^2 + P) U^\mu U^\nu + P \eta^{\mu\nu}$$

Equation [](#eq:def-Tmunu) therefore corresponds well to the definition of an energy-momentum tensor for a perfect fluid in the relativistic framework.

Note that in a flat space-time, the conservation of the energy-momentum tensor of a perfect fluid allows us to recover the Navier-Stokes equation without viscosity or external forces, and the conservation of matter equation. For simplicity's sake, let's return to the case of an incompressible fluid, so $\dd \rho / \dd t = 0$ and non-relativistic, so $P / \rho c^2 \propto (v/c)^2 \ll 1$. Then:
$$ 0 = \frac{\partial T^{\mu\nu}}{\partial x^\nu} \Rightarrow
\left\lbrace\begin{align*}
& \mu = i:\ & 0 = & \vec\nabla P + \rho \frac{\partial \vec v}{\partial t} + \rho (\vec v \cdot \vec\nabla)(\vec v)\\
\mu = 0:\ & 0 = & \rho \vec \nabla \vec v + \frac{\partial \rho}{\partial t} 
\end{align*}\right.
$$

:::


Friedmann equations
---------------------------

Solving Einstein's equation [](#eq:einstein2) involves finding a solution metric, given the distribution of matter and energy encoded in $T^{\mu\nu}$. Assuming the principles of homogeneity and isotropy for this tensor, the metric is the Friedmann-Lemaître-Robertson-Walker (FLRW) metric, using the usual set of spherical comobile coordinates $(ct, \sigma, \theta, \phi)$:
$$
\begin{aligned}\label{eq:flrw}
\displaystyle g_{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & \dfrac{a^2(t)}{1-k\sigma^2} & 0 & 0 \\
0 & 0 & a^2(t)\sigma^2 & 0 \\
0 & 0 & 0 & a^2(t) \sigma^2 \sin^2 \theta \\
\end{pmatrix},\end{aligned}
$$ 
where $a(t)$ is an unknown function. The scale parameter $a(t)$ can be obtained by solving the Einstein equation knowing the content of the Universe's energy-momentum tensor $T^{\mu\nu}$ and the value of $k$. For the FLRW metric, its inverse is simply:
$$
g^{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & \dfrac{1-k\sigma^2}{a^2(t)} & 0 & 0 \\ 
0 & 0 & \dfrac{1}{a^2(t)\sigma^2} & 0 \\
0 & 0 & 0 & \dfrac{1}{a^2(t) \sigma^2 \sin^2 \theta}   \\ 
\end{pmatrix}.
$$

Using the FLRW metric [](#eq:flrw), let's calculate the following affine connection from equation [](#eq:connexion):
$$
\begin{aligned}
\Gamma^1_{\ 01} & = \frac{1}{2} g^{1 \mu} \left( \partial_0 g_{1\mu} + \partial_1 g_{0 \mu} - \partial_\mu g_{01} \right) \\
& = \frac{1}{2} g^{1 1} \left(\frac{\partial g_{11}}{c\partial t} + \partial_\sigma g_{01} - 0 \right) \text{ because }\forall \mu \neq 1, g^{1\mu}=0\\
& = \frac{1}{2} \frac{1-k\sigma^2}{a^2} \left( \frac{2 \dot{a} a}{c(1-k\sigma^2)} + 0 \right) \\
& = \frac{\dot a}{ca} = \frac{H}{c}.
\end{aligned}
$$

In the same way, we obtain the other affine connections, then the Riemann and Ricci tensors. In the end, the Einstein tensor is diagonal and is worth: 
$$
\begin{aligned}
G_{00} & = - 3 \left( \frac{\dot{a}^2}{c^2 a^2}+ \frac{k}{a^2} \right), \\
G_{ij} & = \frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{c^2 a^2}g_{ij} \text{ for } i=j\neq 0.
\end{aligned}
$$
From Einstein's equation [](#eq:einstein2) and the energy-momentum tensor [](#eq:tmunu_fluid), we obtain for the coordinate $00$ and for the spatial coordinates $ij$: 
$$
\begin{aligned}
G_{\mu\nu}-\Lambda g_{\mu\nu} & = -8\pi \GN T_{\mu\nu}/c^4 \\
\Leftrightarrow & \left\lbrace
\begin{array}{rl}
    \text{00: } & \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{c^2 k}{a^2} \right) = 8\pi \GN \rho + c^2 \Lambda} \\
    ij\text{: } & \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{a^2} = - \frac{8\pi \GN}{c^2 } P + c^2 \Lambda }
\end{array}
\right.\end{aligned}
$$ 
These are the two Friedmann equations. Here they are expressed in terms of the Hubble parameter
$H=\dot{a}/a$ : 
$$
\label{eq:friedmann}
\left\lbrace
\begin{array}{rl}
    \text{00: } & \displaystyle{H^2 = \frac{8\pi \GN \rho}{3} + \frac{c^2 \Lambda}{3} - \frac{c^2 k}{a^2}}\\
    ij\text{: } & \displaystyle{2\dot{H} + 3H^2 = - \frac{8\pi \GN}{c^2 } P + c^2 \Lambda - \frac{c^2 k}{a^2}}
\end{array}
\right.
$$
The first Friedmann equation explicitly relates the evolution of the scale factor $a(t)$ to the energy content of the Universe. Moreover, by subtracting these two equations and combining the result with the time derivative of the first, we can obtain the energy conservation equation that would also be obtained directly by calculating $T^{\mu\nu}_{\;\;\;;\mu}=0$ in the FLRW metric: 
$$
\label{eq:conservation_energie}
\boxed{\dot{\epsilon} = -3 H( \epsilon + P )}
$$

:::{exercise}
:label: exo:friedmann

In this exercise, we use the FLRW metric in cartesian coordinates, and the corresponding stress energy tensor for a perfect fluid:
\begin{equation}
g_{\mu\nu} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & a^2(t) & 0 & 0 \\
0 & 0& a^2(t) & 0 \\
0 & 0& 0& a^2(t)  \\
\end{pmatrix}\qquad 
T_{\mu\nu}=\begin{pmatrix} \rho c^2 & 0 & 0 & 0 \\ 0 &a^2 P & 0 & 0 \\ 0&0&a^2 P &0 \\ 0&0&0&a^2 P \end{pmatrix}
\label{stress-energy-cosmo-tensor}
\end{equation}
We recall the following formula for the Christoffel and Riemann tensors:
\begin{align}
\Gamma^\kappa_{\ \mu\nu} &= \frac{1}{2}g^{\kappa\lambda}\left( g_{\mu\lambda,\nu}+g_{\lambda\nu,\mu}-g_{\mu\nu,\lambda} \right) \\
R^{\mu}_{\ \nu\alpha\beta} &= -\Gamma^\mu_{\ \nu\beta,\alpha} + \Gamma^\mu_{\ \nu\alpha,\beta} - \Gamma^\lambda_{\ \nu\beta}\Gamma^\mu_{\ \lambda\alpha} + \Gamma^\lambda_{\ \nu\alpha}\Gamma^\mu_{\ \lambda\beta} \\
R_{\mu\nu}& = R^\rho_{\ \mu\rho\nu} = -\Gamma^\rho_{\ \mu\nu,\rho} + \Gamma^\rho_{\ \mu\rho,\nu} - \Gamma^\rho_{\ \rho\lambda}\Gamma^\lambda_{\ \mu\nu} + \Gamma^\rho_{\ \nu\lambda}\Gamma^\lambda_{\ \mu\rho} \\
R &= g^{\mu\nu}R_{\mu\nu}
\end{align}
with $_{,\mu}$ the derivative $\partial / \partial x^\mu$.


1. Show that $\Gamma^0_{\ ij} = \dot{a}a/c \delta_{ij}$ and $\Gamma^j_{\ 0i}=\dot{a}/(ac)\delta^j_i$, with the latin index standing for the spatial coordinates $i=1,2,3$. The other Christoffel symbols are null.
2. Show that $R_{00}=3\ddot{a}/(ac^2)$ and $R_{ij}=-(\ddot{a}a+2\dot{a}^2)\delta_{ij}/c^2$.
3. Show that $R=-6\left(\ddot{a}/a+(\dot{a}/a)^2\right)/c^2$ and finally that $G_{\mu\nu}=R_{\mu\nu}-g_{\mu\nu}R/2$ is:
\begin{equation}
G_{\mu\nu}={1 \over c^2}\begin{pmatrix} 3{\dot{a}^2\over a^2} & 0 & 0 & 0 \\ 0 &-2\ddot{a}a-\dot{a}^2 & 0 & 0 \\ 0&0& -2\ddot{a}a-\dot{a}^2 &0 \\ 0&0&0&-2\ddot{a}a-\dot{a}^2  \end{pmatrix}
\label{Einstein-cosmo-tensor}
\end{equation}
4. Write the two Friedmann equations in term of the Hubble parameter $H=\dot{a}/a$ instead of $a$.
5. From the two Friedmann equations, find the energy conservation equation law $\dot{\rho} c^2 = -3 H(\rho c^2 + P)$.

:::{solution} exo:friedmann
:class: dropdown

1. Let's compute the Christoffel symbols:
\begin{align}
\Gamma^{0}_{\mu\nu} & = \frac{1}{2}g^{0\lambda}\left( g_{\mu\lambda,\nu}+g_{\lambda\nu,\mu}-g_{\mu\nu,\lambda} \right) \\
 & = \frac{1}{2}g^{00}\left( g_{\mu 0,\nu}+g_{0\nu,\mu}-g_{\mu\nu,0} \right) \\
  & = \frac{1}{2}g^{00}\left( g_{0 0,\nu}+g_{00,\mu}-g_{\mu\nu,0} \right) \\
  & = \frac{1}{2}(-1)\times\left( 0+ 0 -g_{\mu\nu,0} \right) \\
  & = \frac{1}{2}g_{\mu\nu,0}
\end{align}
We find:
\begin{equation}
\Gamma^{0}_{ij} =  -\frac{1}{2}g_{ij,0} =   -\frac{1}{2}\frac{\partial (-a^2(t))}{c\partial t} \delta_{ij}= \frac{\dot{a}a}{c} \delta_{ij}
\end{equation}
with $\delta_{ij}$ the Kronecker symbol such that $\delta_{ij}=1$ only if $j=i$. It is a number (not a matrix). Then:
\begin{align}
\Gamma^{j}_{0i} & = \frac{1}{2}g^{j\lambda}\left( g_{0\lambda,i}+g_{\lambda i,0}-g_{0i,\lambda} \right) \\
 & = \frac{1}{2}g^{jk}\left( g_{0k,i}+g_{ki,0}-g_{0i,k} \right) \\
  & = \frac{1}{2}g^{jk}\left( 0+g_{ki,0}-0 \right) \\
  & = \frac{1}{2}g^{jk}\times\left( \frac{-2a\dot{a}}{c}\delta_{ik} \right)  \\
  & = g^{jk}\times\left( +\frac{\dot{a}}{ac}g_{ik} \right)  \\
  & = \frac{\dot{a}}{ac}\delta^j_i
\end{align}
with $\delta^j_i$ the identity matrix ($\delta^i_i = 3$, but $\delta_{ii}=1$).

2. Now the Ricci tensors :
\begin{align}
R_{00} & = -\Gamma^\rho_{\ 00,\rho} + \Gamma^\rho_{\ 0\rho,0} - \Gamma^\rho_{\ \rho\lambda}\Gamma^\lambda_{\ 00} + \Gamma^\rho_{\ 0\lambda}\Gamma^\lambda_{\ 0\rho} \\
& = 0 + \Gamma^\rho_{\ 0\rho,0} + 0 + \Gamma^\rho_{\ 0\lambda}\Gamma^\lambda_{\ 0\rho} \\
& =  + \Gamma^i_{\ 0i,0} + 0 + \Gamma^i_{\ 0j}\Gamma^j_{\ 0i} \\
& = 3\frac{\ddot{a}a-\dot{a}^2}{a^2 c^2} +  \left(\frac{\dot{a}}{ac}\right)^2 \delta^i_j \delta^j_i\\
& = 3\frac{\ddot{a}a-\dot{a}^2}{a^2 c^2} + 3 \left(\frac{\dot{a}}{ac}\right)^2\\
& = 3 \frac{\ddot{a}}{ac^2}
\end{align}
\begin{align}
R_{ij} & = -\Gamma^\rho_{\ ij,\rho} + \Gamma^\rho_{\ i\rho,j} - \Gamma^\rho_{\ \rho\lambda}\Gamma^\lambda_{\ ij} + \Gamma^\rho_{\ i\lambda}\Gamma^\lambda_{\ j\rho} \\
& = -\Gamma^0_{\ ij,0} + 0 -\Gamma^k_{\ k0}\Gamma^0_{\ ij}+\Gamma^0_{\ ik}\Gamma^k_{\ j0} + \Gamma^k_{\ i0} \Gamma^0_{\ jk} \\
& = -\frac{\ddot{a}a+\dot{a}^2}{c^2}\delta_{ij} -\frac{\dot{a}}{ac}\frac{\dot{a}a}{c}\delta^k_k \delta_{ij} +  \frac{\dot{a}}{ac}\frac{\dot{a}a}{c} \delta_{ik}\delta^k_j +  \frac{\dot{a}}{ac}\frac{\dot{a}a}{c} \delta_{jk}\delta^k_i\\
& = -\frac{\ddot{a}a+\dot{a}^2}{c^2}\delta_{ij} -3\frac{\dot{a}}{ac}\frac{\dot{a}a}{c} \delta_{ij} + 2 \frac{\dot{a}}{ac}\frac{\dot{a}a}{c} \delta_{ij}\\
& = -\frac{a^2}{c^2}\left(\frac{\ddot{a}}{a}+2\frac{\dot{a}^2}{a^2}\right)\delta_{ij}
\end{align}
with $\delta_{ik}\delta^k_j=\delta_{ij}$ and $\delta^k_k=3$.

3. Now the Einstein tensor :
From the Einstein equation $G_{\mu\nu} - \Lambda g_{\mu\nu} = -8\pi G T_{\mu\nu}/c^4$ write the Friedmann equations:
\begin{equation} \left\lbrace
\begin{array}{l}
   \displaystyle{3 \left( \frac{\dot{a}^2}{a^2}+ \frac{c^2k}{a^2} \right) = 8\pi \GN \rho + c^2 \Lambda} \\
    \displaystyle{\frac{2\ddot{a}a + \dot{a}^2 + c^2 k}{a^2} = - 8\pi \GN P/c^2 + c^2 \Lambda }
\end{array}
\right.
\end{equation}
(here we admit the Friedmann equations with an arbitrary curvature $k$).

\begin{align}
R &= g^{\mu\nu}R_{\mu\nu} \\
& = g^{00}R_{00} + g^{ij}R_{ij}\\
& = -1\times\left( 3 \frac{\ddot{a}}{ac^2}\right) -  g^{ij}\delta_{ij} \frac{a^2}{c^2}\left(\frac{\ddot{a}}{a}+2\frac{\dot{a}^2}{a^2}\right) \\
& = -1\times\left( - 3 \frac{\ddot{a}}{ac^2}\right)  -\frac{\delta^i_i}{a^2} \frac{a^2}{c^2}\left(\frac{\ddot{a}}{a}+2\frac{\dot{a}^2}{a^2}\right) \\
& = -6 \left(\frac{\ddot{a}}{ac^2} + \frac{\dot{a}^2}{a^2c^2}\right) \\
\end{align}
with $g^{ij}=\delta^{ij}/a^2$ and $\delta^i_i=3$.
\begin{align}
G_{00} &= R_{00}-g_{00}R/2 \\
& = 3 \frac{\ddot{a}}{ac^2} - \frac{6}{2}\left(\frac{\ddot{a}}{ac^2} + \frac{\dot{a}^2}{a^2c^2}\right) \\
& =- 3 \frac{\dot{a}^2}{a^2c^2} 
\end{align}
\begin{align}
G_{ij} &= R_{ij}-g_{ij}R/2 \\
& =-\frac{a^2}{c^2}\left(\frac{\ddot{a}}{a}+2\frac{\dot{a}^2}{a^2}\right)\delta_{ij} -(a^2\delta_{ij})\times \frac{-6}{2}\left(\frac{\ddot{a}}{ac^2} + \frac{\dot{a}^2}{a^2c^2}\right) \\
& = a^2\left(2\frac{\ddot{a}}{ac^2}+ \frac{\dot{a}^2}{a^2c^2}\right) \delta_{ij}
\end{align}
Using the definition of $ T_{\mu\nu}$, we obtain directly the two Friedmann equations:
\begin{equation}
G_{\mu\nu} - \Lambda g_{\mu\nu}  = -\frac{8\pi \GN}{c^4}T_{\mu\nu}
\end{equation}
\begin{align}
\label{Friedmann1}
3{\dot{a}^2 \over a^2}&=& 8 \pi \GN \rho + c^2 \Lambda\\
2{\ddot{a} \over a} + {\dot{a}^2 \over a^2}& =& - {8 \pi \GN \over c^2}P + c^2 \Lambda
\label{align}
\end{align}

4. Using $H=\dot a / a$:
\begin{equation} \left\lbrace
\begin{array}{l}
   \displaystyle{3 H^2+ \frac{3kc^2}{a^2} = 8\pi \GN \rho + c^2\Lambda} \\
    \displaystyle{2\dot{H} + 3H^2 + \frac{c^2k}{a^2} = - 8\pi \GN P/c^2 + c^2\Lambda }
\end{array}
\right.
\end{equation}
using $\ddot{a}/a=\dot{H}+H^2$. 

5. And finally the energy-momentum tensor conservation:
\begin{align}
8\pi G \dot{\rho} & = 6\dot{H}H - \frac{6c^2 k \dot{a}}{a^3} \\
& = 3H \left[-8\pi \GN P / c^2 + c^2 \Lambda - 3 H^2 - \frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi \GN P / c^2 -8 \pi \GN \rho + 2\frac{kc^2}{a^2}\right] - 6 H \frac{kc^2}{a^2} \\
& = 3H \left[-8\pi \GN P / c^2 -8 \pi \GN \rho \right]
\end{align}
and $\dot{\rho} c^2 = -3 H(\rho c^2 + P)$. 
This is the same result as in the $T^{\beta \alpha}_{\,\,\,\,\,\,;\alpha}=0$ computation (as expected).


:::

:::{exercise} Evolution of entropy
:label: exo:expansion_isentropique

From the first principle of thermodynamics and equation [](#eq:conservation_energie), find that the expansion of the Universe is isentropic.

:::

:::{solution} exo:expansion_isentropique
:class: dropdown

$$\dd U = T \dd S - P \dd V $$
$$U = a^3 \epsilon, \quad V = a^3$$
$$ \dd(a^3 \epsilon) = - P \dd (a^3) + T \dd S \Rightarrow 3 \dot{a} a^2 \epsilon + a^3 \dot{\epsilon} = - 3 P \dot{a} a^2  + T \frac{\dd S}{\dd t}\Rightarrow \dot{\epsilon} = -3\frac{\dot{a}}{a}(P+\epsilon) +T \frac{\dd S}{\dd t} $$
Therefore 
$$\frac{\dd S}{\dd t} = 0$$
and the expansion is isentropic. This is expected given that for a homogeneous and isotropic Universe the energy-momentum tensor is that of a perfect fluid therefore without viscosity or heat transfer. The evolution is therefore adiabatic ($\delta Q=0$).
:::




Cosmological inventory
-----------------------

The energy-momentum tensor includes non-relativistic and relativistic matter. Relativistic matter is generally called radiation because today the photon radiation from the CMB is largely dominant in this component. 

### Matter

Non-relativistic matter exerts no pressure so 
$$P_m=0,$$
then: 
$$
\label{eq:conservation_energie_matiere}
\dot{\rho}_m = -3 H\rho_m \Rightarrow \rho_m = \rho_m^0 \left(\frac{a_0}{a}\right)^{3}.
$$
This last relation indeed translates the fact that if a box of side $a$ containing a certain quantity of matter sees the length of its sides double, then the matter density is indeed divided by $2^3$. 

### Photons and neutrinos



:::{exercise} Entropy evolution
:label: exo:expansion_isentropique

From the first principle of thermodynamics and equation [](#eq:conservation_energie), find that the expansion of the Universe is isentropic.

:::

:::{solution} exo:expansion_isentropique
:class: dropdown

$$\dd U = T \dd S - P \dd V $$
$$U = a^3 \epsilon, \quad V = a^3$$
$$ \dd(a^3 \epsilon) 
= - P \dd (a^3) + T \dd S \Rightarrow 3 \dot{a} a^2 \epsilon + a^3 \dot{\epsilon} = - 3 P \dot{a} a^2 + T \frac{\dd S}{\dd t}\Rightarrow \dot{\epsilon} 
= -3\frac{\dot{a}}{a}(P+\epsilon) +T \frac{\dd S}{\dd t} $$
So 
$$ \frac{\dd S}{\dd t} = 0$$
and the expansion is isentropic. 
This is to be expected, given that for a homogeneous, isotropic Universe, the energy-momentum tensor is that of a perfect fluid, i.e. without viscosity or heat transfer. Evolution is therefore adiabatic ($\delta Q=0$).
:::




Cosmological inventory
-----------------------

The energy-momentum tensor includes non-relativistic and relativistic matter. Relativistic matter is generally referred to as radiation, since CMB photon radiation now dominates this component. 

### Matter

Non-relativistic matter exerts no pressure, so 
$$P_m=0,$$
then : 
$$
\label{eq:conservation_energie_matiere}
\dot{\rho}_m = -3 H\rho_m \Rightarrow \rho_m = \rho_m^0 \left(\frac{a_0}{a}\right)^{3}.
$$
This last relationship reflects the fact that if a box of side $a$ containing a certain quantity of matter sees the length of its sides doubled, then the density of matter is indeed divided by $2^3$. 

### Photons and neutrinos

For relativistic matter (photons, neutrinos), 
$$P_r = \frac{1}{3} \epsilon_r,$$
therefore:
$$
\label{eq:conservation_energie_radiation}
\dot{\epsilon}_r = -4 H\epsilon_r \Rightarrow \epsilon_r = \epsilon_r^0 \left(\frac{a_0}{a}\right)^{4}.
$$ 
The reasoning with a cubic box of side $a$ also applies here, but if all lengths double, then the wavelength of the radiation also doubles, so its energy is divided by 2. We indeed find a decrease in radiation energy density scaling as $2^4$.


:::{note} Equation of state of a perfect gas

For a perfect gas, we recall that the equation of state is:
$$ P = \rho_n k_B T $$
with $T$ its temperature, $\rho_n$ the particle density and $k_B$ the Boltzmann constant.
If it is at low temperature (i.e. non-relativistic) then we have $\epsilon \approx m c^2 \rho_n$ and we want $P / \epsilon = k_B T \ll 1/3$ namely:
$$ T \ll m c^2 / 3 k_B $$
For a hydrogen gas, $T \ll 10^{12}\,$K. So we see that matter as we know it is non-relativistic today and even well before the CMB.

:::


:::{note} Non-interaction hypothesis
:class: dropdown

We used equation [](#eq:conservation_energie) to deduce that non-relativistic matter has a density that evolves as $a^{-3}$ while relativistic matter evolves as $a^{-4}$. The attentive reader may have noticed that the density and pressure in equation [](#eq:conservation_energie) are however the sum of relativistic and non-relativistic densities and pressures. In a Universe possessing these two components, are equations [](#eq:conservation_energie_matiere) and [](#eq:conservation_energie_radiation) still valid?

Equation [](#eq:conservation_energie) can be derived from thermodynamic reasoning which may be useful here. Since the expansion of the Universe is adiabatic, the entropy variation linked to expansion is zero so $\dd S = 0$. The first principle of thermodynamics on a volume $V$ of Universe gives:
$$\label{eq:conservation_energie_thermo}
\dd U = -P \dd V + T \dd S \Leftrightarrow \dd \left(\epsilon_m V + \epsilon_r V  \right) = -\frac{1}{3}\epsilon_r \dd V$$
If the two components do not interact with each other, then this last equation can be split into its two components, like two independent thermodynamic systems:
$$\dd \left(\epsilon_m V\right) = 0, \quad \dd \left(\epsilon_r V  \right) = -\frac{1}{3}\epsilon_r \dd V$$
If they interacted, this would not be true. From these two equations, we deduce again equations [](#eq:conservation_energie_matiere) and [](#eq:conservation_energie_radiation).

:::




### Cosmological constant

In Friedmann equations [](#eq:friedmann), it is possible to interpret the cosmological constant $\Lambda$ and curvature $k$ in terms of energy densities in the same way as the energy density $\rho$ of the energy-momentum tensor. 

The energy density associated with the cosmological constant is sometimes called dark energy density, due to the strange properties associated with it:
$$\epsilon_\Lambda(t) = \rho_\Lambda c^2 =  \frac{c^4 \Lambda}{8\pi \GN} = \text{ constant }.$$ 
We see that the energy density associated with the cosmological constant being constant in time, it has a very singular behavior: whatever the size of the Universe, there is always as much energy per unit volume. It is therefore not diluted like any ordinary energy when the Universe expands. Moreover, thanks to the second Friedmann equation, we see that the pressure associated with the cosmological constant would be:
$$P_\Lambda = - \epsilon_\Lambda,$$
namely a negative pressure! In ordinary physics, one of the rare phenomena involving negative pressures is cavitation (<wiki:Pressure#Negative_pressures>). By setting $\epsilon_{\mathrm{tot}}=\epsilon + \epsilon_\Lambda$ (and $P_{\mathrm{tot}}=P + P_\Lambda$) then combining the two Friedmann equations [](#eq:friedmann) to eliminate the curvature term, we obtain:
2\dot{H} + 2H^2 = \frac{2\ddot{a}}{a} = -\frac{8\pi \GN}{3}\left( \epsilon _{\mathrm{tot}} + 3P_{\mathrm{tot}}\right).
\end{equation}
We observe that the expansion of the Universe accelerates ($\ddot{a}>0$) if $P_{\mathrm{tot}}<-\epsilon_{\mathrm{tot}}/3$. Since the Universe consists essentially of non-relativistic matter and radiation, the previous condition becomes equivalent to:
$$
\ddot{a} > 0 \Leftrightarrow \epsilon_\Lambda > \epsilon_r + \epsilon_m/2$$
In conclusion, if the cosmological constant dominates the energy content of the Universe, then it generates such negative pressure that the Universe enters _accelerated expansion_.

:::{note} What unit for $\Lambda$?

Since $\epsilon_\Lambda$ is an energy density, we deduce that $\Lambda$ has the dimension of the inverse of the square of a length. To summarize,
$$
\label{eq:dimensions}
\left[a\right] = \mathsf{L},\quad \left[\rho \right] = \mathsf{M}\cdot \mathsf{L}^{-3}, \quad \left[\epsilon \right] = \left[p \right] = \mathsf{M}\cdot \mathsf{L}^{-1} \cdot \mathsf{T}^{-2}\quad \left[\Lambda \right] = \mathsf{L}^{-2} $$
$$
\left[ g_{\mu\nu} \right] = [1,\mathsf{L}^{2},\mathsf{L}^{2},\mathsf{L}^{2}] $$
:::


### Curvature

The energy density associated with curvature energy is identified as: 
$$
\epsilon_k(t) =\rho_k(t) c^2 = - \frac{3 c^4 k  }{8\pi \GN a^2(t)}.$$
Similarly, its effect in terms of pressure is:
$$P_k = \frac{c^4 k}{8\pi \GN a^2(t)}.$$


Cosmological parameters
2\dot{H} + 2H^2 = \frac{2\ddot{a}}{a} = -\frac{8\pi \GN}{3}\left( \epsilon _{\mathrm{tot}} + 3P_{\mathrm{tot}}\right).
\end{equation}
We see that the expansion of the Universe accelerates ($\ddot{a}>0$) if $P_{\mathrm{tot}}<-\epsilon_{\mathrm{tot}}/3$. Since the Universe consists essentially of non-relativistic matter and radiation, the previous condition becomes equivalent to :
$$
\ddot{a} > 0 \Leftrightarrow \epsilon_\Lambda > \epsilon_r + \epsilon_m/2$$.
In conclusion, if the cosmological constant dominates the energy content of the Universe, then it generates such negative pressure that the Universe enters _accelerated expansion_.

:::{note} What unit for $\Lambda$?

Since $\epsilon_\Lambda$ is an energy density, we deduce that $\Lambda$ has the dimension of the inverse square of a length. To summarize,
$$
\label{eq:dimensions}
\left[a\right] = \mathsf{L},\quad \left[\rho \right] = \mathsf{M}\cdot \mathsf{L}^{-3}, \quad \left[\epsilon \right] = \left[p \right] = \mathsf{M}\cdot \mathsf{L}^{-1} \cdot \mathsf{T}^{-2}\quad \left[\Lambda \right] = \mathsf{L}^{-2} $$
$$
\left[ g_{\mu\nu} \right] = [1,\mathsf{L}^{2},\mathsf{L}^{2},\mathsf{L}^{2}] $$
:::



### Curvature

The energy density associated with curvature energy can be identified as : 
$$
\epsilon_k(t) =\rho_k(t) c^2 = - \frac{3 c^4 k }{8\pi \GN a^2(t)}.$$
Similarly, its effect in terms of pressure is :
$$P_k = \frac{c^4 k}{8\pi \GN a^2(t)}.$$


Cosmological parameters
----------------------------

### Equation-of-state parameters

The equation of state $w$ associated with a component of the Universe is defined by the ratio of its pressure to its energy density:
$$
\label{eq:def-w}
\boxed{w=P/\epsilon}
$$

- Non-relativistic cold matter exerts no pressure on its external environment
    from which $P_m=0$ hence $w_m=0$.

- Relativistic matter, on the other hand, exerts a pressure on its medium
    relativistic matter exerts a pressure on its environment of $P_r = \epsilon_r / 3 $, hence $w_r=1/3$.

- For the cosmological constant, we have $P_\Lambda = - \epsilon_\Lambda$, so its equation of state is
    constant and negative $w_\Lambda = -1$.

- Curvature assimilated to a perfect fluid would have an equation-of-state parameter $w_k=1/3$.


### Energy density parameters

We can define a critical density, corresponding to the density we should have in a homogeneous, isotropic, expanding universe with zero spatial curvature (cf equation [](#eq:friedmann)): 
$$
\rho_c(t) = \frac{3H^2(t)}{8\pi \GN}.$$ 
It's also convenient to define its current value:
$$
\rho_{c}^0 = \frac{3H^2_0}{8\pi \GN} = 1.1 \times 10^{-29} \left( \frac{H_0}{75\text{ km/s/Mpc}}\right)^2\text{ g/cm}^3 \approx 6 \text{ protons/m}^3.
$$
where $H_0$ is the Hubble constant.

The density parameters (dimensionless) are defined by normalizing the energy densities by the critical density, i.e. :
$$
\Omega_m(t) = \frac{\rho_m(t)}{\rho_c(t)},\quad \Omega_\Lambda(t) = \frac{c^2 \Lambda}{3H^2(t)}, \quad \Omega_k(t) = -\frac{c^2 k}{a^2(t)H^2(t)}
$$
$$
\Omega_m^0 = \frac{\rho_m^0}{\rho_c^0},\quad \Omega_\Lambda^0 = \frac{c^2 \Lambda}{3H^2_0}, \quad \Omega_k^0 = -\frac{c^2 k}{a_0^2 H^2_0}.
$$
The first Friedmann equation is then simply written:
$$
\label{eq:omega_sum}
1 = \Omega_m(t) + \Omega_r(t) + \Omega_\Lambda(t) + \Omega_k(t)
$$

:::{math}
:label: eq:friedmann2
\bar H^2 (t) \equiv \frac{H^2(t)}{H_0^2} = \Omega_m^0 \left(\frac{a_0}{a(t)}\right)^{3} + \Omega_r^0 \left(\frac{a_0}{a(t)}\right)^{4} + \Omega_\Lambda^0 + \Omega_k^0 \left(\frac{a_0}{a(t)}\right)^{2}.
:::
This model of the Universe, linking the prediction of its expansion $\bar H(z)$ to its contents of cosmological constant, matter and radiation, is called the $\Lambda$CDM model ($\Lambda$ for the cosmological constant and CDM for *Cold Dark Matter*) in the case $k=0$ (flat Universe). This is the standard model of cosmology.


### Dark energy modeling

What is the true nature of dark energy? Is it the manifestation of vacuum energy? A second fundamental constant of gravitation? Or a new fifth force? The manifestation of additional spatial dimensions? These questions about the nature of dark energy do not have answers at the moment, but since the discovery of accelerated expansion in 1998 {cite:p}`Riess1998,Perlmutter1999` new cosmological surveys are underway to precisely measure the equation of state of dark energy $w_{DE}$: as long as we measure $w_{DE} = w_\Lambda=-1$ then the acceleration of expansion can be explained with a single parameter which is the value of $\Lambda$. If measurements deviate significantly from $-1$, then more complex models will have to be tested.

This is why today, in addition to the standard $\Lambda$CDM model, cosmologists test empirical models that seek deviations from the standard model:
- Flat $w$CDM: flat Universe model with free parameters $\Omega_m^0$, $\Omega_r^0$ and $w_{DE}$;
- $w$CDM: arbitrary curvature model with free parameters $\Omega_m^0$, $\Omega_r^0$, $\Omega_\Lambda^0$ and $w_{DE}$;
- $w_0w_a$CDM: model where the equation-of-state parameter of dark energy is given by two free parameters:
$$
w_{DE}(a) = w_0 + \left(1 - \frac{a}{a_0}\right)w_a$$

The major challenge for current and future cosmological surveys is to measure $w_a$, in order to measure variations in the acceleration of the expansion of the Universe.


Cosmological distances
------------------------

Cosmology is an observational science. We must infer the properties of the Universe without being able to move or redo the Big Bang experiment, but only from our observations. Cosmological parameters are linked to the expansion rate of the Universe $H(z)$. Therefore to be able to estimate them we must be capable of measuring $H(z)$. This expansion rate is present in the proper and comoving distances defined [Sec. {number}](#distance-propre-et-distance-comoving), but these are not measurable. 

:::{warning}

Neither proper distance nor comoving distance are measurable because they assume we can overcome the expansion of the Universe. However, in cosmology, we want to measure distances and their evolution to deduce the behavior of $a(t)$ and therefore the behavior of the Universe's content. Traditionally, cosmology uses photons as messengers coming from the most distant galaxies. Observation of luminous objects can lead us to determine distances according to at least two of their aspects: their luminosity and their apparent size. We can thus define two distances based on observation of luminous fluxes $\Phi$ and angular sizes $\delta$:
$$
\Phi = \frac{L}{4\pi D_L^2}, \qquad \delta = \frac{l}{D_A}
$$
where $L$ is the intrinsic luminosity of an object (in watts) and $l$ a physical size (in meters).

:::


### Hubble distance

With the parameters $c$ and $H_0$, it is possible to construct a quantity homogeneous to a length. This typical distance in cosmology is called the *Hubble distance* and is worth:
$$
D_H = \frac{c}{H_0} = 3000\,\text{Mpc/}h
$$
where $h$ is usually defined by:
$$
H_0 = 100\,h\,\text{km/s/Mpc}
$$
So for $h=0.7$, we find $D_H \approx 4.3 \,\text{Gpc} \approx 14 \,\text{Gly}$. This value will appear for all (non-comoving) distances defined below.
So for $h=0.7$, we find $D_H \approx 4.3 \,\text{Gpc} \approx 14 \,\text{Gly}$. This value will appear for all (non-comoving) distances defined below.


### Luminosity distance 

In a static, flat space, the apparent luminosity of a source at rest at distance $D_L$ would be $L_E/4\pi D_L^2$. We therefore propose to define the luminosity distance of a source $D_L(z)$ in cosmology as:
$$
\Phi_0 \equiv \frac{L_E}{4 \pi D_L^2(z)}
$$
Let's consider a source located in $\sigma_E$, emitting $\delta N_E$ photons of mean frequency $\nu_E$ at time $t_E$ during $\delta t_E$ (refer again to the [](#fig:distances_croquis)). Its luminosity is :
$$
L_E = h\nu_E \frac{\delta N_E }{\delta t_E}.$$ 
So the flux density received by an observer with a telescope of aperture size $A$ is : 
$$
\Phi_0 = h \nu_0\frac{\delta N_0 }{A \delta t_0}.$$ 
The surface over which the emitted flux is distributed at time $t_0$ is:
$$
S = \int_0^{2\pi} \int_0^\pi \sqrt{-g} \dd\theta \dd\phi = \int_0^{2\pi} \int_0^\pi a^2(t_0)\sigma^2(t_0)\sin\theta \dd\theta \dd\phi = 4 \pi a^2_0 \sigma^2_E.
$$
with $\sigma(t_0)=\sigma_E$.
The number of emitted photons $\delta N_E$ intercepted by the collecting surface of size $A$ is therefore :
$$
\delta N_0 = \delta N_E \frac{A}{4 \pi a^2_0 \sigma^2_E}.$$
From the equation
[](#eq:redshift2), we have:
$$\nu_E = \nu_0 a_0/a(t_E) = \nu_0 (1+z)$$
and also:
$$\delta t_E = \delta t_0/(1+z).$$
Hence the received flux:
$$\Phi_0 = h \nu_0\frac{\delta N_0 }{A \delta t_0 } = h \nu_0  \frac{\delta N_E}{4 \pi a^2_0 \sigma^2_E \delta t_0 } = \frac{L_E}{4 \pi a^2_0 \sigma^2_E(1+z)^2}.$$

We deduce the expression for the luminosity distance in a curved, expanding universe, a function of cosmological parameters and redshift:
$$
\Rightarrow D_L(z) = a_0 \sigma_E (1+z) = a_0 (1+z)
\left\lbrace
\begin{array}{cl}
    \sin \chi(z) & \text{ si } k=+1 \\
    \chi(z) & \text{ si } k=0 \\
    \text{sh } \chi(z) & \text{ si } k=-1 
\end{array}
\right. 
$$


Today, the scale factor $a_0$ is not accessible via Friedmann's equations, which only give the expansion rate. However, it can be expressed as a function of cosmological parameters and $H_0$:
\begin{equation}
\Omega_k^0 = - \frac{kc^2}{H_0^2 a_0^2} \Rightarrow a_0 = \left\lbrace\begin{array}{l}
    \displaystyle{\frac{c}{H_0\sqrt{-\Omega_k^0}}}  \text{ if } k=+1 \\
    \text{indeterminate but usually worth } 1 \text{ if } k=0 \\
    \displaystyle{\frac{c}{H_0\sqrt{\Omega_k^0}}}  \text{ if } k=-1 
\end{array}
\right.
\end{equation}
Thus:
\begin{equation}
\displaystyle{\chi(z) = \left\lbrace\begin{array}{cl}
    \displaystyle{H_0\sqrt{-\Omega_k^0}\int_0^z\frac{dz}{H(z)}}  & \text{ if } k=+1 \\\
    \displaystyle{\frac{1}{a_0}\int_0^z\frac{cdz}{H(z)}} & \text{ if } k=0 \\\\
    \displaystyle{H_0\sqrt{\Omega_k^0}\int_0^z\frac{dz}{H(z)} } & \text{ if } k=-1 
\end{array}
\right.}
\end{equation}

$$
D_L(z) = (1+z) \left\lbrace
\begin{array}{cl}
    \displaystyle \frac{c}{H_0 \sqrt{-\Omega_k^0}} \sin\left[ H_0 \sqrt{-\Omega_k^0} \int_0^z \frac{\dd z}{H(z)} \right] & \text{ if } k=+1 \\
    \displaystyle \int_0^z \frac{c\dd z}{H(z)} & \text{ if } k=0 \\
    \displaystyle \frac{c}{H_0 \sqrt{\Omega_k^0}} \sh\left[ H_0 \sqrt{\Omega_k^0} \int_0^z \frac{\dd z}{H(z)} \right] & \text{ if } k=-1 \
\end{array}
\right. 
.$$

We have thus obtained a link between a distance measurement obtained by measuring the $\Phi_0$ flux of a star, and a cosmological model based on parameters to be determined. By measuring the fluxes of objects of known intrinsic luminosity $L_E$, cosmological parameters can be estimated.

### Angular distances


:::{figure} ../../images/angular_distance.svg
:name: fig:angular_distance
:align: center
:width: 100%

Angular distance of an object of transverse physical size $l$.
:::


The last important distance in cosmology is the angular distance of an object $D_A(z)$. In a static, flat space, the apparent angle $\delta$ of an object of physical size $l$ at rest at distance $D_A$ would be $l/D_A$. We therefore propose to define the angular distance $D_A(z)$ in cosmology as:
$$
\delta = \frac{l}{D_A(z)}
$$

How is this distance modelled in the FLRW metric? Let's consider an object of transverse physical size $l$ located in $\sigma=\sigma_E,t=t_E$ and observed today in $\sigma=0,t=t_0$. 

In physical space, the angle $\delta$ is the same as in comobile space (we pass from one to the other by a homothety), but also the same at reception and transmission. The angle under which the object is seen is therefore, in all cases, and for any curvature (see [](#fig:projection_polaire)) : 
$$
\delta = \frac{l}{a_E \sigma_E} = \frac{l (a_0/a_E)}{a_0 \sigma_E} = \frac{l_c}{\sigma_E}
$$
with $l_c = l / a_E$ the comoving size of the object at emission $t_E$. We propose to define the comoving angular distance or comoving transverse distance simply as:
$$d_A(z) = \frac{l_c}{\delta} = \sigma_E = \left\lbrace\begin{array}{cl}
    \sin \chi(z) & \text{ if } k=+1 \\
    \chi(z) & \text{ if } k=0 \\
    \sinh \chi(z) & \text{ if } k=-1 
\end{array}
\right.
$$
We can also deduce the expression for the angular distance in a curved, expanding universe, as a function of cosmological parameters and redshift:
$$
\Rightarrow D_A(z) \equiv\frac{l}{\delta} = a(t_E) \sigma_E=\frac{a_0 \sigma_E}{1+z} = \frac{a_0}{1+z}d_A(z)=\frac{D_L(z)}{(1+z)^2}$$
$$D_A(z) = \frac{a_0}{1+z} \left\lbrace\begin{array}{cl}
    \sin \chi(z) & \text{ if } k=+1 \\
    \chi(z) & \text{ if } k=0 \\
    \sinh \chi(z) & \text{ if } k=-1 
\end{array}
\right.$$

$$D_A(z) = \frac{1}{1+z} \left\lbrace
\begin{array}{cl}
    \displaystyle \dfrac{c}{H_0 \sqrt{-\Omega_k^0}} \sin\left[ H_0 \sqrt{-\Omega_k^0} \int_0^z \dfrac{\dd z}{H(z)} \right] & \text{ if } k=+1 \\
    \displaystyle \int_0^z \dfrac{c \dd z}{H(z)} & \text{ if } k=0 \\
    \displaystyle \dfrac{c}{H_0 \sqrt{\Omega_k^0}} \sh\left[ H_0 \sqrt{\Omega_k^0} \int_0^z \dfrac{\dd z}{H(z)} \right] & \text{ if } k=-1 \\
\end{array}
\right. 
$$
From exercise [](#exo:sphere-comoving), we can see that the use of $\sigma$ instead of $\chi$ is well suited to the three types of Universe curvatures in these distance definitions.

:::{note} Hubble-Lemaître law

At low redshift $z\ll 1$, we find Hubble-Lemaître's law for all three curvatures:
$$D_L(z) \approx \frac{cz}{H_0} \approx D_A(z)$$
with $cz$ the apparent speed of recession relative to the Earth.

:::


:::{important} Measurements of cosmological parameters

In the framework of a flat Universe, angular measurements performed by the _Planck_ satellite on the cosmic microwave background, combined with flux measurements of type Ia supernovae, and angular distances of baryon acoustic oscillations allow to infer the matter and dark energy content for a flat universe today ([](doi:10.1051/0004-6361/201833910)):
$$
\label{eq:omegas_planck}
\Omega_m^0 = 0.3111 \pm 0.0056, \quad \Omega_\Lambda^0 = 0.6889 \pm 0.0056
$$

If curvature is a free parameter of the model (we speak of an extension to the standard $\Lambda$CDM model), we measure:
$$
\Omega_k^0 = 0.0007\pm 0.0037
$$
which is compatible with a strictly flat universe[^flat], or curved but with a very large radius of curvature since $\Omega_k^0 \approx k/a_0^2$.

If we propose a two-parameter model for dark energy, we obtain ([](doi:10.1051/0004-6361/201833910)):
$$
w_0 = −0.957 \pm 0.080, \quad w_a = −0.29^{+0.32}_{ −0.26}
$$ 

:::



:::{exercise} Orders of magnitude
:label: exo:densities

Transform the values in equation [](#eq:omegas_planck) into mass density and energy density.

:::


:::{solution} exo:densities
:class: dropdown

Suppose that density of the dark energy as cosmological constant is equal to the present critical density, $\rho_\Lambda=\rho_c$. What is then the total amount of dark energy inside the Solar System? Compare this number with $M_\odot c^2$.

$$\rho_c\approx 10^{-29}\,\text{g/cm}^3$$
$$R\approx 50\,\text{A.U.}$$
$$1\,\text{A.U.} \approx 1.5\times 10^{11}\,\text{m}; E_{DE}S.S./c^2 ≃ 0.2 \cdot 10^{14}\, \text{kg}; M_⊙ ≃ 2 \cdot 10^{30}\, \text{kg}; E_{DE}S.S./M_⊙c^2 ≃ 10^{-17}.$$

Transform Lambda into a length: Length = $\sqrt{1/\Lambda}$ = ....

:::




:::{important} Key points

- The Cosmological Principle implies that matter must be described as a perfect fluid, and therefore that its transformations are adiabatic.

- The evolution of the Universe as a function of its matter content and geometry is encoded in the Friedmann equations
\begin{equation*}
\left\lbrace
\begin{array}{l}
    \displaystyle{H^2 = \frac{8\pi \GN \rho}{3} + \frac{c^2 \Lambda}{3} - \frac{c^2 k}{a^2}},\\
    \displaystyle{2\dot{H} + 3H^2 = - \frac{8\pi \GN}{c^2 } P + c^2 \Lambda - \frac{c^2 k}{a^2}}.
\end{array}
\right.
\end{equation*}

- These two equations contain the conservation equation for the energy-momentum tensor
\begin{equation*}
\dot{\epsilon} = -3 H(\epsilon + P). 
\end{equation*}

- We define the equation-of-state parameter for a component $X$ of the Universe as the ratio of its pressure and energy density $w_X = P_X/\epsilon_X$. Its density parameter is $\Omega_X = \rho_X / \rho_c$ with $\rho_c = 3H^2/8\pi\GN$ the critical density.

- The luminosity and angular distances relate physical observables (luminous fluxes and angles) to the intrinsic properties of the observed object and to integral distances of $1/H(a)$.

::: 


:::{seealso}  To go further

- Demonstration of the structure of form-invariant tensors: {cite:t}`Weinberg1972`[p. 392]

- Relativistic hydrodynamics: <wiki:Fluid_solution>

- Imperfect (viscous) fluids: {cite:t}`Weinberg1972`[p. 53], {cite:t}`Weinberg1971Fluids`, {cite:t}`LandauFluids`

:::




[^vecj]: In electromagnetism, the amount of charge passing through a surface $\dd \vec S$ during a duration $\dd t$ is $\dd q = e n (\vec v \dd t)\cdot \dd \vec S$ with $n$ the particle density: we then define the volume current of charge by $\vec j = e n \vec v$. The definition of volume current for four-momentum (instead of electric charge) is identical.

[^pcphoton]: For a massless particle, we have directly $E_n = \vert \vec p_n \vert c$.

[^epsP]: The choice of notations for these mathematical functions was not made by chance...

[^flat]: We will _stricto sensu_ never be able to measure that the Universe is flat ($k=0$), but that measurements are compatible with the hypothesis of a flat universe.