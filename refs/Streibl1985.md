# Three-dimensional imaging by a microscope

N. Streibl 

Physikalisches Institut, Erwin-Rommel-Strasse 1, 8520 Erlangen, Federal Republic of Germany 

Received August 2, 1984; accepted September 26, 1984 

In transmission microscopy, many objects are three dimensional, that is, they are thicker than the depth of focus of the imaging system. The three-dimensional (3-D) image-intensity distribution consists of a series of two-dimensional images (optical slices) with different parts of the object in focus. First, we deal with the fundamental limitations of 3-D imaging with classical optical systems. Second, a transfer theory of 3-D image formation is derived that relates the 3-D object (complex index of refraction) to the 3-D image intensity distribution in first-order Born approximation. This theory applies to weak objects that do not scatter much light. Since, in a microscope, the illumination is neither coherent nor completely incoherent, a theory for partially coherent light is needed, but in this case the object phase distribution and the absorptive parts of the object play different roles. Finally, some experimental results are presented. 

## 1. INTRODUCTION

An experienced observer is often able to determine the shape of a microscopic three-dimensional (3-D) object by focusing through the object; this means that he looks sequentially at a series of two-dimensional (2-D) images with different parts of the object in focus. However, this technique of optical slicing has the disadvantage that each slice is obstructed by out-of-focus noise, which enters each image from adjacent slices. Our aim in this paper is to present a theory of 3-D image formation that explains the limitations of 3-D imaging. 

In Section 2, an intuitive explanation of the main limitations of 3-D imaging is given: By considering volume gratings as elementary objects, it is shown that both the aperture of the imaging system and the spatial coherence of the illumination determine the 3-D resolving power of a microscope. For a more-quantitative analysis, in Section 3 we investigate the propagation of partially coherent light through a 3-D object. The object is assumed to be weak in order to permit a first-order Born approximation. Then, in Section 4, we derive a relation between the 3-D image-intensity distribution (produced by a telecentric imaging system) and the phase distribution and the absorptive parts of the 3-D object. The 3-D image formation is described by two optical transfer functions (OTF's), one for phase and one for absorption. In Section 5, the dependence of the OTF's on the coherence of illumination is studied. The 3-D OTF's emphasize the low frequencies strongly, and they eliminate certain parts of the 3-D spatial-frequency domain completely. Finally, in Section 6, some experiments with a microscope and subsequent 3-D image processing are shown. 

In certain respects, this paper is the continuation of the work on 3-D OTF theory performed by Mertz $^{1}$ and Frieden, $^{2}$ although these authors dealt with incoherently self-luminescent objects. For coherently transilluminated objects, the basic theory was derived by Wolf, $^{3}$ and, for ultrasonic tomography, by Mueller et al. $^{4}$ Experiments on 3-D data acquisition from scattered-field data were done by many people, for example, in ultrasonic tomography, $^{4}$ by Fercher et al. $^{5}$ for coherent fields, by Zinser et al. and Zinser $^{6}$ with an optical slicing technique and linear filtering, and by Häusler and Körner $^{7}$ with an optical slicing technique and nonlinear processing. 

## 2. FUNDAMENTAL LIMITATIONS

In the last century, Abbe $^{8}$ developed the theory of the resolving power of the microscope for 2-D structures. His pioneering idea was to consider planar gratings as elementary objects. Such an elementary grating is imaged by the microscope if at least the first diffraction order passes through the pupil of the objective; otherwise, the diffraction limit is exceeded, and the spatial frequency of the elementary grating is not transmitted by the imaging system. 

Now we will investigate 3-D imaging with an analogous idea: A 3-D Fourier transformation decomposes any 3-D object into elementary volume gratings. According to the laws of Bragg diffraction, an illuminating beam is diffracted by such a volume grating only if the wavelength and the direction of the beam match the 3-D spatial frequency of the volume grating. The diffracted light takes part in the process of image formation only if it fits through the pupil of the imaging system (Abbe's condition). In order to study the roles that are played by Bragg's condition, by Abbe's condition, by the spatial coherence of illumination, and by the pupil size, we consider the simplified imaging system shown in Fig. 1. We begin with an elementary object, a volume grating with the 3-D spatial frequency $\rho_0 = (\mu_0, \eta_0)$ , where $\mu_0 = (\nu_x, \nu_y)$ denotes the lateral part and $\eta_0$ the longitudinal part (along the optical axis) of the 3-D spatial frequency. Let the object be illuminated by a beam with the wave vector $\rho_s = [\mu_s, (\lambda^{-2} - \mu_s^2)^{1/2}]$ , which emerges from an individual source point at $\mu = \mu_s$ . Then $\rho_s$ will interact with all those object frequencies $\rho_0$ that are compatible with the Bragg condition 

$$
\rho_ {D} = \rho_ {s} + \rho_ {0},\tag{1}
$$

where $\pmb{\rho}_{D} = [\pmb{\mu}_{D}, (\lambda^{-2} - \pmb{\mu}_{D}^{2})^{1/2}]$ denotes the wave vector of the diffracted light. 

The diffracted light participates in image formation only if it passes the pupil with the radius $\rho_{P}$ : 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/266a45e3af8966c780876bf4299e00b38e191dfc5c9ee34fac74ab62cd1e3471.jpg)



Fig. 1. 3-D imaging of a partially coherently transilluminated object by a telecentric system.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/f97f6560fc1412af7e8bda868424f39a39f6a7226dd6e79024e35488a2e859c9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/c4c2cf8c607efab19104d452169361578303e3060e9a990d390f861ff10a2294.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/2caa9c97eee2a7d6afcdd42ceac5b1c6797c16ad845211afcd003471a020888d.jpg)



Fig. 2. Shape of the 3-D aperture depends on the size of the illuminating source $\rho_{s}$ compared with the size of the pupil of the imaging system $\rho_{p}$ .


$$
| \mu_ {D} | = | \mu_ {s} + \mu_ {0} | \leq \rho_ {p}.\tag{2}
$$

The illuminating beam comes from a finite source with the radius $\rho_{s}$ : 

$$
\left| \mu_ {s} \right| \leq \rho_ {s}.\tag{3}
$$

Thus we find Abbe's lateral diffraction limit: 

$$
\left| \mu_ {0} \right| = \left| \mu_ {D} - \mu_ {s} \right| \leq \rho_ {s} + \rho_ {p}.\tag{4}
$$

Furthermore, there is also a longitudinal diffraction limit that emerges from the Bragg condition [Eq. (1)]: 

$$
\eta_ {0} = [ \lambda^ {- 2} - (\mu_ {0} + \mu_ {s}) ^ {2} ] ^ {1 / 2} - (\lambda^ {- 2} - \mu_ {s} ^ {2}) ^ {1 / 2}.\tag{5}
$$

For a given lateral object frequency $\mu_{0}$ and for given pupil and source radii, only certain longitudinal frequencies $\eta_{0}$ are accessible for Eq. (5). The sets of accessible 3-D spatial frequencies are shown in Fig. 2 for different radii of the source (different spatial coherence of illumination). Only those 3-D spatial frequencies that are contained within the filled areas in Fig. 2 get a chance to be imaged by our imaging system (of course, for rotationally symmetric pupils and sources, the plots in Fig. 2 must be rotated around the $\eta_{0}$ axis if one is to visualize the 3-D case). Therefore these filled areas act as 3-D apertures: they are the ultimate limit for 3-D data acquisition by optical slicing. For a more complete transfer of object data, more-sophisticated techniques, such as optical tomography, have to be developed. Figure 2 shows that for 3-D imaging the illumination of the object should be partially coherent in order to increase the chance for Bragg diffraction (many angles of incidence). In the coherent limit $\rho_{s} \rightarrow 0$ only a cross section of the object spectrum with the Ewald sphere is transmitted, as was shown by Wolf. $^{3}$ Partially coherent illumination increases the size of the 3-D aperture so that we are able to collect more information about the object. That the 3-D aperture acts as a fundamental limitation for 3-D intensity distributions was recognized by Lohmann. $^{9}$ 

It has been assumed implicitly within this section that the light is diffracted only once within the object. If secondary diffraction cannot be neglected, then the situation becomes complicated: The object diffracts several times, and therefore the object can enter the theory in a nonlinear fashion. In this paper, we assume only first-order interactions with the object, which leads in Section 3 to a first-order Born approximation. 

## 3. BORN APPROXIMATION FOR PARTIALLY COHERENT LIGHT

The object is described by its 3-D distribution of the index of refraction $n(\mathbf{r})$ , which is a complex-valued function for absorbing objects. If the object is slowly varying compared with the wavelength $\lambda$ of the quasi-monochromatic illumination, then the light amplitude $u(\mathbf{r})$ fulfills approximately a scalar Helmholtz equation: 

$$
[ \nabla^ {2} + n ^ {2} (\mathbf {r}) k ^ {2} ] u (\mathbf {r}) = 0.\tag{6}
$$

Equivalently, the object may be described by its scattering potential $V(\mathbf{r})$ , which is evidently zero outside the object: 

$$
V (\mathbf {r}) = k ^ {2} (1 - n ^ {2} (\mathbf {r})),\tag{7}
$$

$$
(\nabla^ {2} + k ^ {2}) u (\mathbf {r}) = V (\mathbf {r}) u (\mathbf {r}).\tag{8}
$$

A quasi-monochromatic partially coherent field is described by the mutual-intensity function $J(\mathbf{r}_{1};\mathbf{r}_{2})$ that is defined $^{10}$ as the expected value over the wild fluctuations of the field, which decrease the degree of coherence: 

$$
J (\mathbf {r} _ {1}; \mathbf {r} _ {2}) = \langle u (\mathbf {r} _ {1}) u ^ {*} (\mathbf {r} _ {2}) \rangle .\tag{9}
$$

By insertion of this definition into wave Eq. (8), we find two simultaneous differential equations for $J(\mathbf{r}_{1}; \mathbf{r}_{2})$ : 

$$
(\nabla_ {1} ^ {2} + k ^ {2}) J (\mathbf {r} _ {1}; \mathbf {r} _ {2}) = V (\mathbf {r} _ {1}) J (\mathbf {r} _ {1}; \mathbf {r} _ {2}),\tag{10a}
$$

$$
(\nabla_ {2} ^ {2} + k ^ {2}) J (\mathbf {r} _ {1}; \mathbf {r} _ {2}) = V ^ {*} (\mathbf {r} _ {2}) J (\mathbf {r} _ {1}; \mathbf {r} _ {2}),\tag{10b}
$$

where $\nabla_{j}$ denotes differentiations with respect to $r_{j}$ with j = 1, 2. If there is no object ( $V \equiv 0$ ), then we observe only the known illuminating mutual intensity $J_{\mathrm{IN}}(\mathbf{r}_{1}; \mathbf{r}_{2})$ : 

$$
(\nabla_ {j} ^ {2} + k ^ {2}) J _ {\mathrm{IN}} (\mathbf {r} _ {1}; \mathbf {r} _ {2}) = 0 \quad j = 1, 2.\tag{10c}
$$

The next step in the standard procedure for deriving the Born approximation is the formal solution of Eqs. (10) by an integral equation. To this end, we need the Green function $G(\mathbf{r})$ of the Helmholtz equation: 

$$
(\nabla^ {2} + k ^ {2}) G (\mathbf {r} - \mathbf {r} ^ {\prime}) = \delta (\mathbf {r} - \mathbf {r} ^ {\prime}).\tag{11}
$$

It is well known that the Green function is a spherical wave emerging from the point $r = r'$ . By applying the operators $(\nabla_{j}^{2} + k^{2}), j = 1, 2$ and by using Eqs. (10) and (11), one can easily verify that the mutual intensity obeys the following integral equation: 

$$
\begin{array}{r l} & J (\mathbf {r} _ {1}; \mathbf {r} _ {2}) = J _ {\mathrm{IN}} (\mathbf {r} _ {1}; \mathbf {r} _ {2}) \\ & \quad + \iint [ G (\mathbf {r} _ {1} - \mathbf {r} _ {1 ^ {\prime}}) V (\mathbf {r} _ {1 ^ {\prime}}) \delta (\mathbf {r} _ {2} - \mathbf {r} _ {2 ^ {\prime}}) \\ & \quad + \delta (\mathbf {r} _ {1} - \mathbf {r} _ {1 ^ {\prime}}) G ^ {*} (\mathbf {r} _ {2} - \mathbf {r} _ {2 ^ {\prime}}) V ^ {*} (\mathbf {r} _ {2 ^ {\prime}}) \\ & \quad - G (\mathbf {r} _ {1} - \mathbf {r} _ {1 ^ {\prime}}) V (\mathbf {r} _ {1 ^ {\prime}}) G ^ {*} (\mathbf {r} _ {2} - \mathbf {r} _ {2 ^ {\prime}}) V ^ {*} (\mathbf {r} _ {2 ^ {\prime}}) ] \\ & \quad \times J (\mathbf {r} _ {1 ^ {\prime}}; \mathbf {r} _ {2 ^ {\prime}}) \mathrm{d} ^ {3} r _ {1 ^ {\prime}} \mathrm{d} ^ {3} r _ {2 ^ {\prime}}. \end{array}\tag{12}
$$

This integral equation is linear in the mutual intensity J; however, the object enters in a bilinear form. The central idea of the Born approximation is to solve the implicit Eq. (12) iteratively by successive substitutions. $^{11}$ The fixed-point theorem of Banach $^{11}$ teaches us that this method converges for a weak object, that is, if $V(\mathbf{r}) \ll 1$ . Within this paper, we assume that the first-order approximation is sufficiently good and that the bilinear term can be neglected: 

$$
\begin{array}{r l} & J (\mathbf {r} _ {1}; \mathbf {r} _ {2}) = J _ {\mathrm{IN}} (\mathbf {r} _ {1}; \mathbf {r} _ {2}) \\ & \qquad + \iint [ G (\mathbf {r} _ {1} - \mathbf {r} _ {1 ^ {\prime}}) V (\mathbf {r} _ {1 ^ {\prime}}) \delta (\mathbf {r} _ {2} - \mathbf {r} _ {2 ^ {\prime}}) \\ & \qquad + \delta (\mathbf {r} _ {1} - \mathbf {r} _ {1 ^ {\prime}}) G ^ {*} (\mathbf {r} _ {2} - \mathbf {r} _ {2 ^ {\prime}}) V ^ {*} (\mathbf {r} _ {2 ^ {\prime}}) ] \\ & \qquad \times J _ {I N} (\mathbf {r} _ {1 ^ {\prime}}; \mathbf {r} _ {2 ^ {\prime}}) d ^ {3} r _ {1 ^ {\prime}} d ^ {3} r _ {2 ^ {\prime}}. \end{array}\tag{13}
$$

This approximation means that the illuminating light is diffracted only once within the object and, moreover, that we observe behind the object only undiffracted light and the interference of the once-diffracted with undiffracted light. 

## 4. 3-D IMAGE FORMATION

In this section, the relation between the object and the 3-D intensity distribution $E_{\mathrm{IMG}}(\mathbf{x},z)$ produced by a telecentric imaging system (Fig. 1) is derived (the 3-D space and the 3-D frequency coordinates are again split into a lateral part and a longitudinal part along the optical axis). The strategy of calculation is the following: First we use the van Cittert-Zernike theorem to obtain from the source at $z = -6f$ the illuminating mutual intensity at the object $J_{\mathrm{IN}}(\mathbf{x}_1,z_1;\mathbf{x}_2,z_2)$ ; then the Born approximation [Eq. (13)] yields the propagating mutual intensity $J(\mathbf{x}_1,z_1;\mathbf{x}_2,z_2)$ . We consider only those field components that propagate in forward (+z) direction. Because the light field is then completely specified by the mutual intensity within one individual plane, we evaluate $J$ only just behind the object, that is, $J_{\mathrm{OBJ}}(\mathbf{x}_1;\mathbf{x}_2) = J(\mathbf{x}_1,z_1 = -4f;\mathbf{x}_2,z_2 = -4f)$ . The well-known formalism of Fourier optics tells us which mutual intensity $J_{\mathrm{IMG}}(\mathbf{x}_1;\mathbf{x}_2)$ is transmitted through the system into the plane $z = 0$ . Finally, this boundary condition determines the 3-D intensity distribution. 

The van Cittert–Zernike theorem combined with the propagation laws for the mutual intensity $^{12}$ yields the illuminating mutual intensity 

$$
\begin{array}{r l} J _ {\mathrm{IN}} (\mathbf {x} _ {1}, z _ {1}; \mathbf {x} _ {2}, z _ {2}) = & \int \tilde {S} (\boldsymbol {\mu}) \exp \{2 \pi i [ (z _ {1} - z _ {2}) \\ & \times (\lambda^ {- 2} - \boldsymbol {\mu} ^ {2}) ^ {1 / 2} + (\mathbf {x} _ {1} - \mathbf {x} _ {2}) \boldsymbol {\mu} ] \} \mathrm{d} ^ {2} \boldsymbol {\mu}, \end{array}\tag{14}
$$

where $\tilde{S}(\boldsymbol{\mu})$ denotes the incoherent source intensity at z = -6f. When we insert this into the Born approximation [Eq. (13)], integrals of the following type occur: 

$$
H = \int G (\mathbf {r} _ {1} - \mathbf {r} _ {1 ^ {\prime}}) V (\mathbf {r} _ {1 ^ {\prime}}) J _ {\mathrm{IN}} (\mathbf {r} _ {1 ^ {\prime}}; \mathbf {r} _ {2}) \mathrm{d} ^ {3} r _ {1}.\tag{15}
$$

The Green function $G(\mathbf{r})$ is a spherical wave that has the following angular spectrum representation (lateral Fourier transform): 

$$
\tilde {G} (\boldsymbol {\mu}, z) = \frac {1}{4 \pi i (\lambda^ {- 2} - \boldsymbol {\mu} ^ {2}) ^ {1 / 2}} \exp [ 2 \pi i | z | (\lambda^ {- 2} - \boldsymbol {\mu} ^ {2}) ^ {1 / 2} ].\tag{16}
$$

Thus we arrive at a lengthy integral: 

$$
\begin{array}{l} H = \int V (\mathbf {x} _ {1} ^ {\prime}, z _ {1} ^ {\prime}) \frac {\tilde {S} (\boldsymbol {\mu} _ {2})}{4 \pi i (\lambda^ {- 2} - \boldsymbol {\mu} _ {1} ^ {2}) ^ {1 / 2}} \exp \left\{2 \pi i \left[ (z _ {1} ^ {\prime} - z _ {2}) \right. \right. \\ \times (\lambda^ {- 2} - \mu_ {2} ^ {2}) ^ {1 / 2} - (\mathbf {x} _ {1} ^ {\prime} - \mathbf {x} _ {2}) \boldsymbol {\mu} _ {2} \\ + | z _ {1} - z _ {1} ^ {\prime} | (\lambda^ {- 2} - \boldsymbol {\mu} _ {1} ^ {2}) ^ {1 / 2} \\ + (\mathbf {x} _ {1} - \mathbf {x} _ {1} ^ {\prime}) \boldsymbol {\mu} _ {1} ] \rbrace d ^ {2} \mu_ {1} d ^ {2} \mu_ {2} d ^ {2} x _ {1} ^ {\prime} d z _ {1} ^ {\prime}. \end{array} \tag {1}\tag{17}
$$

We assume the object to be finite, so that $V(\mathbf{x}_{1}^{\prime}, z_{1}^{\prime}) \equiv 0$ for $z_{1}^{\prime} \geq -4f$ . Moreover, our imaging system accepts only those light waves that travel into the right half-space $z \geq -4f$ . Therefore we neglect reflection within the object, and we take only those components of the integral that fulfill $|z_{1} - z_{1}| = z_{1} - z_{1}^{\prime} \geq 0$ . Finally, we remember that we are interested only in the mutual intensity within the plane $z_{1} = z_{2} = -4f$ , and we drop unimportant phase factors. Then we find that 

$$
\begin{array}{l} H = \int \frac {\tilde {S} (\boldsymbol {\mu} _ {2})}{4 \pi i (\lambda^ {- 2} - \boldsymbol {\mu} _ {1} ^ {2}) ^ {1 / 2}} \exp [ 2 \pi i (\mathbf {x} _ {1} \cdot \boldsymbol {\mu} _ {1} - \mathbf {x} _ {2} \cdot \boldsymbol {\mu} _ {2}) ] \\ \times \int V (\mathbf {x} _ {1} ^ {\prime}, \mathbf {z} _ {1} ^ {\prime}) \exp \{- 2 \pi i [ \mathbf {x} _ {1} ^ {\prime} \cdot (\boldsymbol {\mu} _ {1} - \boldsymbol {\mu} _ {2}) \\ + z _ {1} ^ {\prime} (\lambda^ {- 2} - \boldsymbol {\mu} _ {1} ^ {2}) ^ {1 / 2} - (\lambda^ {- 2} - \boldsymbol {\mu} _ {2} ^ {2}) ^ {1 / 2} ] \} \\ \times d ^ {2} x _ {1} ^ {\prime} d z _ {1} ^ {\prime} d ^ {2} \mu_ {1} d ^ {2} \mu_ {2}. \end{array}\tag{18}
$$

The inner integral (over $x_{1}^{\prime}, z_{1}^{\prime}$ ) is a Fourier component of the object. The outer integral is also a Fourier integral. Hence, after the calculation of the conjugated term of the Born approximation, we find the following (lateral) spectrum of the mutual intensity just behind the object: 

$$
\begin{array}{r l} \tilde {J} _ {\mathrm{OBJ}} (\boldsymbol {\mu} _ {1}; \boldsymbol {\mu} _ {2}) & = \tilde {S} (\boldsymbol {\mu} _ {1}) \delta (\boldsymbol {\mu} _ {1} - \boldsymbol {\mu} _ {2}) + \frac {\tilde {S} (\boldsymbol {\mu} _ {2})}{4 \pi i (\lambda^ {- 2} - \boldsymbol {\mu} _ {1} ^ {2}) ^ {1 / 2}} \\ & \times \overline {{V}} [ \boldsymbol {\mu} _ {1} - \boldsymbol {\mu} _ {2}, (\lambda^ {- 2} - \boldsymbol {\mu} _ {1} ^ {2}) ^ {1 / 2} - (\lambda^ {- 2} - \boldsymbol {\mu} _ {2} ^ {2}) ^ {1 / 2} ] \\ & - \frac {\tilde {S} (\boldsymbol {\mu} _ {1})}{4 \pi i (\lambda^ {- 2} - \boldsymbol {\mu} _ {2} ^ {2}) ^ {1 / 2}} \overline {{V}} ^ {*} (\boldsymbol {\mu} _ {2} - \boldsymbol {\mu} _ {1}), \\ & (\lambda^ {- 2} - \boldsymbol {\mu} _ {2} ^ {2}) ^ {1 / 2} - (\lambda^ {- 2} - \boldsymbol {\mu} _ {1} ^ {2}) ^ {1 / 2}, \end{array} \tag {19}
$$

where $\overline{V}(\boldsymbol{\mu},\eta)$ denotes the 3-D Fourier spectrum of the scattering potential of the object. We decompose the scattering potential $V(\mathbf{r})$ into its real and imaginary parts P and A, which correspond to phase and absorption, respectively: 

$$
V (\mathbf {x}, z) = P (\mathbf {x}, z) + i A (\mathbf {x}, z).\tag{20}
$$

Furthermore, the square roots are Taylor expanded, which means that a paraxial approximation is adopted (this is not necessary, but it is simpler). Then we see that absorption and phase play considerably different roles: 

$$
\begin{array}{r l} & {\tilde {J} _ {\mathrm{OBJ}} (\mu_ {1}; \mu_ {2}) = \tilde {S} (\mu_ {1}) \delta (\mu_ {1} - \mu_ {2})} \\ & {+ \frac {\lambda}{4 \pi i} [ \tilde {S} (\mu_ {2}) - \tilde {S} (\mu_ {1}) ] \overline {{P}} \bigg [ \mu_ {1} - \mu_ {2}, \frac {\lambda}{2} (\mu_ {2} ^ {2} - \mu_ {1} ^ {2}) \bigg ]} \\ & {+ \frac {\lambda}{4 \pi} [ \tilde {S} (\mu_ {2}) + \tilde {S} (\mu_ {1}) ] \tilde {A} \bigg [ \mu_ {1} - \mu_ {2}, \frac {\lambda}{2} (\mu_ {2} ^ {2} - \mu_ {1} ^ {2}) \bigg ].} \end{array}\tag{21}
$$

The mutual intensity $J_{\mathrm{IMG}}(\mathbf{x}_{1}; \mathbf{x}_{2})$ behind the imaging system is determined by multiplication of the spectrum $\tilde{J}_{OBJ}$ with the pupil function $^{10}$ : 

$$
\tilde {J} _ {\mathrm{IMG}} (\mu_ {1}; \mu_ {2}) = \tilde {p} (\mu_ {1}) \tilde {J} _ {\mathrm{OBJ}} (\mu_ {1}; \mu_ {2}) \tilde {p} ^ {*} (\mu_ {2}).\tag{22}
$$

The observed intensity is the diagonal part of the mutual intensity $E_{\mathrm{IMG}}(\mathbf{x}, z) = J_{\mathrm{IMG}}(\mathbf{x}, z; \mathbf{x}, z)$ . It is shown in Ref. 12 that the 3-D spectrum of the image intensity can be calculated by using the following projection law: 

$$
\begin{array}{r l} \overline {{E}} _ {\mathrm{IMG}} (\boldsymbol {\mu}, \eta) = & \int \tilde {J} _ {\mathrm{IMG}} (\boldsymbol {\mu} ^ {\prime} + 1 / _ {2} \boldsymbol {\mu}; \boldsymbol {\mu} ^ {\prime} - 1 / _ {2} \boldsymbol {\mu}) \\ & \times \delta (\eta + \lambda \boldsymbol {\mu} \cdot \boldsymbol {\mu} ^ {\prime}) \mathrm{d} ^ {2} \boldsymbol {\mu} ^ {\prime}. \end{array}\tag{23}
$$

By using Eqs. (21)-(23), we arrive at the main result of this paper: The image spectrum is given by 

$$
\begin{array}{r l} \overline {{E}} _ {\mathrm{IMG}} (\boldsymbol {\mu}, \eta) = & B \delta (\boldsymbol {\mu}, \eta) + \overline {{P}} (\boldsymbol {\mu}, \eta) \overline {{T}} _ {p} (\boldsymbol {\mu}, \eta) \\ & + \overline {{A}} (\boldsymbol {\mu}, \eta) \overline {{T}} _ {A} (\boldsymbol {\mu}, \eta), \end{array}\tag{24}
$$

where B is the bias of light that did not interact with the object: 

$$
B = \int \tilde {S} (\boldsymbol {\mu} ^ {\prime}) | \tilde {p} (\boldsymbol {\mu} ^ {\prime}) | ^ {2} \mathrm{d} ^ {2} \boldsymbol {\mu} ^ {\prime}.\tag{25}
$$

The information about the absorption and the phase structure of the object is transmitted by two different optical transfer functions (OTF's): 

$$
\begin{array}{r l} & {\overline {{T}} _ {A} (\pmb {\mu}, \eta) = \frac {\lambda}{4 \pi} \int \tilde {p} (\pmb {\mu} ^ {\prime} + \frac {1}{2} \pmb {\mu}) [ \tilde {S} (\pmb {\mu} ^ {\prime} + \frac {1}{2} \pmb {\mu})} \\ & {\quad + \left. \tilde {S} (\pmb {\mu} ^ {\prime} - \frac {1}{2} \pmb {\mu}) \right] \tilde {p} ^ {*} (\pmb {\mu} ^ {\prime} - \frac {1}{2} \pmb {\mu}) \delta (\eta + \lambda \pmb {\mu} \cdot \pmb {\mu} ^ {\prime}) \mathrm{d} ^ {2} \mu^ {\prime},} \end{array}\tag{26}
$$

$$
\begin{array}{r l} \overline {{{T}}} _ {p} (\boldsymbol {\mu}, \eta) & = \frac {i \lambda}{4 \pi} \int \tilde {p} (\boldsymbol {\mu} ^ {\prime} + 1 / _ {2} \boldsymbol {\mu}) [ \tilde {S} (\boldsymbol {\mu} ^ {\prime} + 1 / _ {2} \boldsymbol {\mu}) \\ & - \left. \tilde {S} (\boldsymbol {\mu} ^ {\prime} - 1 / _ {2} \boldsymbol {\mu}) \right] \tilde {p} ^ {*} (\boldsymbol {\mu} ^ {\prime} - 1 / _ {2} \boldsymbol {\mu})   \delta (\eta + \lambda \boldsymbol {\mu} \cdot \boldsymbol {\mu} ^ {\prime}) d ^ {2} \boldsymbol {\mu} ^ {\prime}. \end{array} \tag {27}\tag{27}
$$

These functions are investigated in more detail in Section 5. For completeness, it should be mentioned that the Fourier counterpart of Eq. (24) contains the convolutions of the absorptive parts and the phase structure of the object with the (real-valued) 3-D point spread functions $T_{A}$ and $T_{p}$ : 

$$
E _ {\mathrm{IMG}} (\mathbf {r}) = B + P (\mathbf {r}) * * * T _ {p} (\mathbf {r}) + A (\mathbf {r}) * * * T _ {A} (\mathbf {r}).\tag{28}
$$

This section ends with a (maybe puzzling) remark about linearity: Although Eq. (28) looks like a linear relation between the object and the image intensity, one has to be careful; the splitting of the scattering potential V into an absorptive and a phase part, A and P, respectively, involves both V and $V^{*}$ . However, in the strict sense, complex conjugation is a nonlinear operation. This fact will have consequences in the results reported in Section 5. 

## 5. EVALUATION OF THE 3-D OTF'S

In Refs. 12 and 13, it was shown how to evaluate 3-D OTF's similar to those of Eqs. (26) and (27), including a geometrical optical approximation. $^{13}$ In this section, we show as examples several OTF's for a diffraction-limited imaging system in order to understand the influence of the source size (coherence of illumination) on the 3-D image. We assume a rotationally symmetric, disk-shaped pupil and a similar source: 

$$
\tilde {p} (\boldsymbol {\mu}) = \left\{ \begin{array}{l l} 1 & \text {if} | \boldsymbol {\mu} | <   \rho_ {p} \\ 0 & \text {otherwise} \end{array} \right.,\tag{29}
$$

$$
\tilde {S} (\boldsymbol {\mu}) = \left\{ \begin{array}{l l} 1 & \text { if } | \boldsymbol {\mu} | <   \rho_ {S} \\ 0 & \text { otherwise } \end{array} \right..\tag{30}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/688e78dd2be77cb5a048411709ec322ae12e8454aea5f14f19d19a1dfea97911.jpg)



Fig. 3. 3-D OTF's for the absorptive parts and for the phase distribution for different radii of the source $\rho_{s}$ and the pupil $\rho_{p}:\mathrm{a},\mathrm{b},\rho_{s} / \rho_{p}$ $= 0.1$ almost coherent; c, d, $\rho_{s} / \rho_{p} = 0.72$ partially coherent; e, f, $\rho_{s} / \rho_{p}$ $= 0.95$ still partially coherent but approaching incoherent illumination $(\rho_s / \rho_p\gg 2)$ .


Figure 3 shows central cross sections through the 3-D OTF's with the singularity at the origin removed. Of course, the OTF's have cylindrical symmetry with respect to the $\eta$ axis. The regions of support of these OTF's are given by the 3-D apertures (from Section 2), which are repeated symmetrically at the negative frequencies. The reason for this repetition is that the Fourier spectra of the real-valued functions $A, P$ , and $E_{\mathrm{IMG}}$ have Hermitian symmetry; as was mentioned above, the relation between $V$ and $E_{\mathrm{IMG}}$ is not linear in a strict sense. Nevertheless, we see that only certain spatial frequencies (namely, those of the object within the 3-D aperture) are transmitted by the imaging system. The coherent system transmits only a cross section of the object spectrum with the Ewald sphere. When the source size is increased, the support of the 3-D OTF's is increased. The OTF $\overline{T}_A$ associated with the absorptive part of the object always has a strong low-pass character, that is, the high frequencies are damped during transmission. This damping and the longitudinal band limitation are the reasons for the out-of-focus noise in data cubes that was obtained by optical slicing. Both branches of the absorptive OTF's join in a singularity at $(\mu, \eta) = 0$ . This means that an object must have a lateral structure (nonzero $\mu$ ); otherwise, the image tells us nothing about the object. Moreover, this form of the OTF guarantees energy conservation: The planar energy (intensity averaged over one image slice) is independent of $z^{9,12}$ . The purely imaginary phase OTF $\overline{T}_P$ also consists of two branches, and, again, the high spatial frequencies are damped within the region of support. Furthermore, there is a phase flip of $\pi$ at $\eta = 0$ ; the physical reason for the phase flip is that we are allowed to measure not an absolute phase but only local relative changes within the phase structure. 

For some simple pupil functions and source distributions such as disks, the OTF's [Eqs. (26) and (27)] can be evaluated analytically, as was shown for similar cases in Ref. 12. For completeness we give the results corresponding to Fig. 3 without the lengthy (but elementary) derivation: 

$$
\begin{array}{r l} & {\overline {{T}} _ {A} (\rho , \eta) = \frac {1}{2 \pi \rho} \operatorname{Re} \left\{\left[ \frac {1}{2} (\rho_ {p} ^ {2} + \rho_ {S} ^ {2}) \right. \right.} \\ & {\qquad \left. - \frac {1}{4} \rho^ {2} - \left(\frac {\eta}{\lambda \rho}\right) ^ {2} - \left| \frac {\eta}{\lambda} - \frac {1}{2} (\rho_ {p} ^ {2} - \rho_ {S} ^ {2}) \right| \right] ^ {1 / 2},} \\ & {\qquad + \left[ \frac {1}{2} (\rho_ {p} ^ {2} + \rho_ {S} ^ {2}) - \frac {1}{4} \rho^ {2} - \left(\frac {\eta}{\lambda \rho}\right) ^ {2} \right.} \end{array}
$$

$$
\left. \left. - \left| \frac {\eta}{\lambda} + \frac {1}{2} \left(\rho_ {p} ^ {2} - \rho_ {S} ^ {2}\right) \right| \right] ^ {1 / 2} \right\}.\tag{31}
$$

$$
\overline {{T}} _ {p} (\rho , \eta) = \frac {i}{2 \pi \rho} \operatorname{Re} [ (\dots) ^ {1 / 2} - (\dots) ^ {1 / 2} ],\tag{32}
$$

where $\rho = |\mu|$ denotes the radial lateral frequency, the square roots in Eq. (32) are the same as in Eq. (31), and it was assumed that $\rho_{s} \leq \rho_{p}$ . The formulas are valid in paraxial approximation. 

## 6. EXPERIMENTAL RESULTS

In the following experiments, the 3-D data set was obtained by digitally recording successive image slices $E_{\mathrm{IMG}}(\mathbf{x}, z_{n})$ , $z_{n} = z_{0} + n\delta z$ . $\delta z$ should be the Rayleigh depth of focus, which corresponds to the inverse longitudinal width of the 3-D aperture. $^{13}$ Figure 4 shows several sections through this data cube. The section shown in Fig. 4c looks somewhat unconventional, since it is parallel to the optical axis. 

Figure 5 shows a central cross section through the 3-D Fourier spectrum of the image. It was calculated digitally by a 3-D fast-Fourier transform (FFT). The form of the 3-D aperture is clearly visible, and there is a good agreement with the theory. Since all the 3-D OTF's are low-pass filters within their region of support, it is logical to perform 3-D signal processing in order to improve the higher frequencies. However, there are two difficulties: First, the data sets are incomplete (limited region of support) and, second, the absorptive structure and the phase structure are intertwined. Hence there is no linear filter that performs a perfect restoration. If the object is not a purely absorptive object or a pure 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/2b8207fac1c8f655dfe517e3b3ad89aaa4bf23f2aa212aa52471bc974051abd2.jpg)



Fig. 4. Sections through a 3-D data cube (256 × 256 × 50 volume elements) recorded with a microscope (objective Pl100/1.32) and a digital TV-frame store with a sampling rate of δx = 0.1 μm, δy = 0.07 μm, δz = 0.5 μm. The object consists of Urothel cells with clearly visible kernels. a, Lateral section z = 20δz; b, lateral section z = 30δz; c, longitudinal section y = 80δy.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/32c1909ed84ce32bc9eca148c803e9d7c5edd6737377fc605fef8cab8daa282c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/dd0b6a416374d348560a55897970c7e9cc2693dfa4c658b3c33256ed97fe8d9a.jpg)



Fig. 5. Central cross section through the real part of the 3-D Fourier spectrum of a microscopic image ( $128 \times 128 \times 32$ volume elements obtained by FFT). The border of the doughnut-shaped 3-D aperture is visible. The bipolar signal is shown in a bias (gray background).


phase structure, it is moreover not clear what to compensate for, the absorptive OTF $\overline{T}_{A}$ or the phase OTF $\overline{T}_{P}$ . Nevertheless, a global high-pass filtering yields considerable improvements of the 3-D images. $^{6}$ Because of the excessive computer-time requirements for 3-D FFT's, we implemented a 3-D filter in the space domain. The filter is high pass, which compensates approximately for the damping of the high frequencies of the 3-D OTF's. The filter consists of a 3-D Laplacian (easy to implement because of its small kernel), followed by a 2-D low-pass filter with the kernel 1/r (obtained by standard techniques). The transfer function of the filter is given by 

$$
\overline {{{F}}} (\rho , \eta) \sim \frac {1}{\rho} (\rho^ {2} + \eta^ {2}).\tag{33}
$$

Figure 6 shows the comparison between the low-pass OTF $\overline{T}_{A}$ for equal source and pupil size $\rho_{s} = \rho_{p}$ and the filtered version $\overline{F} \cdot \overline{T}_{A}$ . We see an enhancement of the high frequencies. A further enhancement is not reasonable, since the noise also is amplified by the filter. 

Figure 7 shows some slices through the data cube of Fig. 4 after 3-D filtering. Obviously, we have more contrast and a somewhat improved resolution, such as that in Ref. 6. Nevertheless, we should not forget that absorptive and phase structure are not separated, so that it is difficult to give any quantitative interpretation of the images. Important special cases for 3-D filtering are pure amplitude and pure phase objects; then there is a unique relationship between the 3-D image and the amplitude and phase structure, because $P \equiv 0$ or $A \equiv 0$ . In the general case, we can circumvent the problem by recording two data sets with different pupil functions, for example, a bright-field image and a phase-contrast image. Since the associated 3-D OTF's are different, it should be possible to solve for the amplitude A and the phase P. Nevertheless, no linear 3-D filtering can solve the problem of the fundamental incompleteness of the data because of the frequency cutoff by the 3-D aperture. 


Fig. 6. Comparison between a, the OTF of the absorptive part ( $\rho_{s} = \rho_{p}$ ) and b, its product with the 3-D filter [Eq. (33)].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/03ad1b729fa9c6fe27fdf22f682aa865eb5be6abb55504d6719430c5488920ee.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/45887b14-254e-4d82-ba84-e65b63b06fef/c91a995ce914ec51116c09d39b6d48715b56a2a6c5ee09648cedc8c3fb27a4c0.jpg)



Fig. 7. Result of the approximate deconvolution of the object of Fig. 4 with the 3-D filter [Eq. (33)]: a, lateral section $z = 20\delta z$ ; b, lateral section $z = 30\delta z$ .


## 7. SUMMARY

In first-order Born approximation, the 3-D image formation in partially coherent light is described by two optical transfer functions, one for the phase distribution and one for the absorptive parts of the object. The 3-D OTF's have in common that they are of limited support. Their region of support can be derived from the 3-D aperture. The 3-D aperture is the fundamental diffraction limitation that results from the finite size of the illuminating source and the pupil of the imaging system. The 3-D aperture ultimately limits the 3-D resolving power of the imaging system, as the 2-D aperture does in 2-D imaging (Abbe's theory). Within the 3-D aperture, the 3-D OTF's have a low-pass character, that is, they damp high frequencies. This is the reason for out-of-focus noise. The higher the degree of coherence of the illumination, the worse the out-of-focus noise. In particular, the coarse structures of the object creep through large distances in the z direction. Hence the depth of focus depends on the lateral frequency and on the coherence of illumination. We proposed a 3-D post-processing method for enhancing the higher frequencies that can be simply implemented in the space domain (no need for a 3-D FFT) and that improves 3-D images. 

## ACKNOWLEDGMENT

The author is greatly indebted to A. W. Lohmann for his encouragement and many helpful discussions. 

## REFERENCES



1. L. Mertz, Transformations in Optics (Wiley, New York, 1965), p. 101. 





2. R. Frieden, "Optical transfer of the three-dimensional object," J. Opt. Soc. Am. 57, 56–66 (1967). 





3. E. Wolf, "Three-dimensional structure determination of semi-transparent objects from holographic data," Opt. Commun. 1, 153-156 (1969). 





4. R. K. Mueller, M. Kaveh, and G. Wade, "Reconstructive tomography and applications to ultrasonics," Proc. IEEE 67, 567–587 (1979). 





5. A. F. Fercher, H. Bartelt, H. Becker, and E. Wiltschko, "Image formation by inversion of scattered field data, experiments," Appl. Opt. 18, 2427-2439 (1976). 





6. G. Zinser, A. Ehrhardt, and J. Bille, "Erzeugung und Rekonstruktion dreidimensionaler lichtmikroskopischer Bilder," presented at Fifth Deutsche Arbeitsgemeinschaft Mustererkennung Symposium, Karlsruhe, Germany, 1983; G. Zinser, "Erzeugung und Analyse digitaler lichtmikroshopischer Bilder histologischer Präparate bie hoher Ortsauflösung," dissertation (University of Heidelberg, Heidelberg, Federal Republic of Germany, 1982). 





7. G. Häusler and E. Körner, "Simple focusing criterion," Appl. Opt. 23, 2468-2469 (1984); "Acquisition and use of three-dimensional object information in image processing," presented at the Thirteenth Meeting of the International Commission for Optics, Sapporo, Japan, 1984. 





8. E. Abbe, "Beiträge zur Theorie des Mikroskops und der mikroskopischen Wahrnehmung," Arch. Mikrosk. Anat. Entwicklungsmech. 9, 413–459 (1873). 





9. A. W. Lohmann: "Three-dimensional properties of wavefields," Optik 51, 105-117 (1978). 





10. M. Born and E. Wolf, Principles of Optics (Pergamon, London, 1968). 





11. R. B. Rall, Computational Solutions of Nonlinear Operator Equations (Wiley, New York, 1969). 





12. N. Streibl, "Fundamental restrictions for 3-D light distributions," Optik 66, 341-354 (1984). 





13. N. Streibl, "Depth transfer by an imaging system," Opt. Acta (to be published). 

