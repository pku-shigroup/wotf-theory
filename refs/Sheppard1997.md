# Vectorial pupil functions and vectorial transfer functions

C. J. R. Sheppard*, K. G. Larkin** 

Department of Physical Optics, School of Physics, University of Sydney, Australia 

Vectorial pupil functions and vectorial transfer functions. The concept of the vectorial form of the pupil function in high aperture imaging is introduced. Both two- and three-dimensional imaging are considered. This leads further to the concept of a vectorial optical transfer function (OTF), which can be used to describe imaging in two or three dimensions in high aperture systems. In this paper the full vectorial OTF is calculated for a 0.95 numerical aperture (NA) system and is shown to be significantly different from the scalar OTF. The most surprising difference is the occurrence of negative values at certain spatial frequencies. The fast and accurate calculation of vectorial OTF for 2-D imaging is achieved using the Fast Fourier transforms found in conventional image processing software. 

Vektorielle Pupillenfunktionen und vektorielle Transferfunktionen. Es wird ein Konzept für die vektorielle Form der Pupillenfunktion in Abbildungssystemen mit hoher numerischer Apertur eingeführt. Es werden zwei- und dreidimensionale Abbildungen betrachtet. Dies führt zudem zum Konzept der vektoriellen optischen Transferfunktionen (OTF), das zur Beschreibung der Abbildung in zwei und drei Dimensionen bei hoher numerischer Apertur (NA) verwendet werden kann. In dieser Arbeit wird die vollständige OTF für eine numerische Apertur von 0,95 berechnet. Diese weicht stark von der skalaren OTF ab. Am meisten überrascht, daß bei gewissen räumlichen Frequenzen negative Werte auftreten. Die schnelle und genaue Berechnung der vektoriellen OTF für 2-D-Abbildung kann wie in der konventionellen Bildverarbeitung mittels der Fast-Fourier-Transformation durchgeführt werden. 

## 1 Introduction

Two dimensional optical imaging theory is usually based upon the simple concept of a space invariant point spread function (PSF) which relates the object to an image; an image which is merely the scaled (or magnified) object which has been “blurred” by a linear convolution with the PSF. Both coherent and and incoherent imaging can be modelled by a suitable choice of either an amplitude PSF or an intensity PSF. If the object, image and PSF are represented by their spatial frequency components (via the Fourier transform) then the “real space” convolution operation corresponds to a “frequency space” multiplication by the optical transfer function (OTF). The OTF is the Fourier transform of the PSF. In many situations it is convenient to consider optical system response in terms of the OTF because an overall system response can be represented as a product of intermediate OTFs. 

In the last decade, or so, the concept of a 3-D PSF and a corresponding 3-D OTF has been very useful in the analysis of imaging in optical microscopy (especially confocal microscopy) and tomography. High resolution microscopes must operate with large values of the numerical aperture (usually called "high NA") and consequently cannot use the usual paraxial approximations encountered in most elementary imaging theory. Better approximations for high NA systems have been developed, but they are scalar in nature. However, the vector nature of electromagnetic radiation begins to cause significant deviations from scalar predictions in high NA systems. Often such considerations have been ignored or avoided because the vector theory was considered too difficult. In fact at high apertures the vectorial effects become dominant over other high aperture effects, incorporation of which into a scalar theory results in an overemphasis of differences as compared with low angle theory. In this paper we show how some simple concepts can be developed to represent the full vectorial nature of optical imaging. 

## 2 The two-dimensional vectorial pupil function

According to the theory of Richards and Wolf [1], in the Debye approximation (i.e. for very large values of Fresnel number), the monochromatic electric field in the focal region of an optical system of high numerical aperture illuminated with plane polarized radiation is given by 

$$
E (\boldsymbol {r}) = - \frac {i k}{2 \pi f} \iint e (m, n) \exp \left\{i k (\boldsymbol {m} \cdot \boldsymbol {r}) \right\} \frac {\mathrm{d} m \mathrm{d} n}{s}\tag{1}
$$

where e is the electrical field over the Gaussian reference sphere, r is a position vector 

$$
\boldsymbol {r} = x \boldsymbol {i} + y \boldsymbol {j} + z \boldsymbol {k}\tag{2}
$$

(3) 

in the focal region; $m, n, s$ are direction cosines of a point on the Gaussian references sphere such that 

$$
\boldsymbol {m} = m \boldsymbol {i} + n \boldsymbol {j} + s \boldsymbol {k}
$$

f is the radius of the reference sphere and the wave number $k = 2\pi/\lambda$ . Comparing this expression with the scalar Debye expression, we can recognize e/s as a vectorial pupil function $P_{e}$ . 

The magnetic field $H(r)$ can be written in a similar way in terms of the magnetic vectorial pupil function $P_{m} = h/s$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/6654103784066c8eb753aa386230594a4f35940112e7de074b6123230a3f47f9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/41271241490ed4dd30f7b224e4016c323416be35d4b07c1b7b1e81808712a79a.jpg)


Introducing the cylindrical direction cosine 

$$
l = + \sqrt {(m ^ {2} + n ^ {2})}\tag{4}
$$

for an optical system illuminated by a plane-polarized wave, the vectorial pupil function has the following components [1-3] 

$$
\begin{array}{l} P _ {e x} = a (l) \left(\frac {m ^ {2} \sqrt {1 - l ^ {2}} + n ^ {2}}{l ^ {2}}\right) = a (l) \left(1 - \frac {m ^ {2}}{1 + s}\right) \\ P _ {e y} = - a (l) \frac {(1 - \sqrt {1 - l ^ {2}})}{l ^ {2}} m n = - a (l) \frac {m n}{1 + s} \\ P _ {e z} = - a (l) m \\ P _ {m x} = - a (l) \frac {(1 - \sqrt {1 - l ^ {2}})}{l ^ {2}} m n = - a (l) \frac {m n}{1 + s} \\ P _ {m y} = a (l) \frac {(m ^ {2} + n ^ {2} \sqrt {1 - l ^ {2}})}{l ^ {2}} = a (l) \left(1 - \frac {n ^ {2}}{1 + s}\right) \\ P _ {m z} = - a (l) n. \end{array}\tag{5}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/cacd03ea45d6f7ea03ea6a90b638aaade17bd933a65f4c7aafca7189d58f79af.jpg)



Fig. 1.
Components of the electric vectorial pupil function for systems satisfying the sine condition.


Here $a(l)$ is the apodization function, which for an aberration-free system which satisfies the sine condition is 

$$
a (l) = (1 - l ^ {2}) ^ {- 1 / 4} = s ^ {- 1 / 2}\tag{6}
$$

and for an aberration-free system satisfying the Herschel condition (a uniform angular distribution) is 

$$
a (l) = (1 - l ^ {2}) ^ {- 1 / 2} = s ^ {- 1}.\tag{7}
$$

In general 

$$
P _ {e x} ^ {2} + P _ {e y} ^ {2} + P _ {e z} ^ {2} = P _ {m x} ^ {2} + P _ {m y} ^ {2} + P _ {m z} ^ {2} = a ^ {2} (l)\tag{8}
$$

i.e. independent of the meridional angle. 

The three components of the electric vectorial pupil function are illustrated in fig. 1. Near to the axis it is polarized in the x direction, and the behaviour can be described by a scalar pupil function. It can be seen from eq. 5 that the magnetic vectorial pupil function is the same as the electric one, but rotated by $\pi/2$ . 

We can also investigate other apodization functions [4]. For example for a paraboloidal mirror we have 

$$
a (l) = \frac {2}{(1 + \sqrt {1 - l ^ {2}}) \sqrt {1 - l ^ {2}}} = \frac {2}{(1 + s) s}\tag{9}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/ad28761d6f7c5dba4ef3fd2f40072f36cb7a8125f7fae0bf477bac9959b24b4e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/6a513ed818c0e551177364f242eb238cfb726508b822e155de65180fcd59aa50.jpg)


whereas the apodization 

$$
a (l) = \frac {(1 + \sqrt {1 - l ^ {2}})}{2 \sqrt {1 - l ^ {2}}} = \frac {1 + s}{2 s}\tag{10}
$$

we call the mixed-dipole case: it corresponds to the far field of crossed electric and magnetic dipoles (oriented along the x and y axes). This apodization has been shown to maximize the electric energy density at the focus [5] in symmetric optical systems with plane polarised input. The vectorial pupil function components for the mixed-dipole apodization are shown in fig. 2. 

In all of these cases except for the sine condition, the direction cosine s, equal to $(1 - l^{2})^{1/2}$ , can be positive or negative, with the negative sign corresponding to plane wave components incident on the focus with angles of incidence subtended at the axis greater than $\pi/2$ . In these cases there is a singularity at the origin of direction cosines m, n. The polarization for small m, n is also now not plane-polarized. This corresponds to the dark central spot which occurs at the focus for focusing by an annular toroidal mirror [6] (a surface of revolution generated by a circular arc rotating about the optical axis). In the case of the sine condition, the apodization $a(l)$ is not defined for s < 0. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/fff3ee28e0fad0b3950097f91aead7092ffb081f8489b004227ef20d41315707.jpg)



Fig. 2.
Components of the electric pupil functions for angles greater than $\pi/2$ satisfying the Herschel condition.


A common feature of the components shown in figs. 1, and 2 is the occurrence of a singularity at l = 1. Such a singularity occurs in the scalar case also. Physically the singularity represents the dominance of marginal rays for 2-D imaging in very high NA optical systems. A number of additional features appearing in figs. 1 and 2 are worth noting. Firstly, the symmetries of the x, y, and z components. The x component is symmetric about both the m and n axes. The y component is antisymmetrical about both m and n axes but symmetrical about the two diagonals (m = n and m = -n). The z component is symmetrical about the n axis and antisymmetric about the m axis. These symmetries have a direct correspondence to the PSF symmetries via the Fourier transform. Secondly, both x and y components can be considered to have deviations from high NA scalar theory which are second order with respect to the co-ordinates, that is to say either $m^{2}$ or mn. In contrast, the z component exhibits a linear deviation (-m). This is an indication that the major redistribution of energy in many high NA systems is into the z component of polarization [7]. 

## 3 The three-dimensional vectorial pupil function

In scalar optics we can define a three-dimension (3-D) pupil function equal (apart from a constant multiplier) to the 3-D Fourier transform of the amplitude in the focal region [8, 9]. In the same way we can introduce the 3-D vectorial pupil function $Q_e(m')$ defined by 

$$
Q _ {e} (m ^ {\prime}) = \text { const. } \times \iiint E (r) \exp \left\{- i k (m ^ {\prime} \cdot r) \right\} d r.\tag{11}
$$

The function $Q_{e}(m')$ is split into two counter-propagating parts in two hemispheres for convenience. 

$$
Q _ {e} (m ^ {\prime}) = P _ {e +} \left(m ^ {\prime}, n ^ {\prime}\right) \delta \left(s ^ {\prime} - s\right) + P _ {e -} \left(m ^ {\prime}, n ^ {\prime}\right) \delta \left(s ^ {\prime} + s\right).\tag{12}
$$

Where the $e+$ and $e-$ subscripts refer to the upper and lower hemispheres respectively. But 

$$
m ^ {2} + n ^ {2} + s ^ {2} = l ^ {2} + s ^ {2} = 1\tag{13}
$$

so that 

$$
\begin{array}{r l} Q _ {e} (m ^ {\prime}) & = P _ {e +} (m ^ {\prime}, n ^ {\prime}) \delta (s ^ {\prime} - \sqrt {1 - l ^ {2}}) \\ & \quad + P _ {e -} (m ^ {\prime}, n ^ {\prime}) \delta (s ^ {\prime} + \sqrt {1 - l ^ {2}}). \end{array}\tag{14}
$$

Simple rules for the manipulation of line and surface delta functions can be found in the recent book by Bracewell [10]. The vectorial pupil function is non-zero only on the surface of a sphere centred on the origin. The vector is tangential to the sphere for propagation in an isotropic medium, thus limiting the degrees of freedom of the three electric field components. The polarization of the 3-D vectorial pupil function for plane-polarized illumination is shown in fig. 3. This polarization is the same as that in the far-field of crossed electric and magnetic dipoles placed at the focus [5]. The two-dimensional pupil function $P_e(m,n)$ is the projection of the three-dimensional pupil function in the s direction 

$$
\begin{array}{l} \boldsymbol {P} _ {e +} (m, n ^ {\prime}) = \int_ {0} ^ {\infty} Q (m ^ {\prime}, n ^ {\prime}) d s ^ {\prime} \\ \boldsymbol {P} _ {e -} (m ^ {\prime}, n ^ {\prime}) = \int_ {\infty} ^ {0} Q (m ^ {\prime}, n ^ {\prime}) d s ^ {\prime} \\ \boldsymbol {P} _ {e \pm} (m ^ {\prime}, n ^ {\prime}) = \int_ {\infty} ^ {\infty} P _ {e \pm} (m ^ {\prime}, n ^ {\prime}) \delta (s ^ {\prime} \mp \sqrt {1 - l ^ {2}}) d s ^ {\prime}. \end{array}\tag{15}
$$

Figure 4 shows a perspective representation of the cap of a sphere corresponding to the pupil function of a 0.95 NA optical system. The negative values of s are indicative of wave propagation in the positive z direction. The $\{m, n, s\}$ axes have been scaled by $\lambda^{-1}$ factor so that the implied scales ranges over $\pm\lambda^{-1}$ . For a system satisfying the Herschel condition, the angular illumination is constant, but the apodization function $a(l)$ (a function of transverse direction cosines) varies as 1/s. The 3-D transfer function is a uniformly weighted cap of a sphere. In the practical quasi-monochromatic case the sphere has a small but finite thickness as a result of the wavelength spread [11]. Thus the projection of the sphere in the axial direction, which gives the 2-D pupil function, is not uniform as a result of the variation in the cross-section of the spherical shell. A similar behaviour occurs for the other apodizations: for the sine condition the 3-D transfer function is weighted as $\cos^{1/2}\theta$ , where $\theta$ is the angle subtended at the origin, which falls off with distance from the axis. The 2-D pupil, given by the projection, however, increases with distance from the axis [12]. From eq. (11) the field in the focal region is given by the 3-D Fourier transform of the 3-D pupil function. McCutchen [8] has described how the amplitude in any plane through the focus is, by the projection-slice theorem, given by the 2-D Fourier transform of the projection of the 3-D pupil function in the direction of the normal to the plane. In particular the amplitude in a meridional plane is given by the 2-D Fourier transform of the projection of the three-dimensional pupil function in a transverse direction. As software is readily available for efficiently performing 2-D Fourier transforms using the Fast Fourier Transform (FFT) algorithm, this provides a useful method for calculating the field in the focal region. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/33bd0f1e41b64e4b382e1022fe69357ed8ef807792c00164b7e25b374787da5d.jpg)



Fig. 3. The polarization of the 3-D vectorial pupil function for plane polarized illumination.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/de52c9a17608608d4fcb45a5d8ec6d63f63d7a86ac5a56a78c917fd9e3ccac01.jpg)



Fig. 4. A perspective representation of the cap of a sphere corresponding to the pupil function of a 0.95 NA optical system. The negative values of s are indicative of wave propagation in the positive z direction. The $\{m, n, s\}$ axes have been scaled by a $\lambda^{-1}$ factor so that the implied scales range over $\pm\lambda^{-1}$ .


## 4 The vectorial coherent transfer function

In scalar optics, for a coherent optical system in which the object is illuminated by a plane wave, the amplitude PSF is multiplied by a complex exponential factor. This phase has the effect that the 3-D coherent transfer function (CTF), given by the 3-D Fourier transform of the amplitude point spread function, is equal to the 3-D pupil function shifted so that it is a spherical shell through the origin, rather than centred on the origin [13–15]. The same applies for the vectorial case. The 3-D pupil function is shifted in the direction of the illumination, so that for a transmission system the region where the vectorial pupil function is almost plane-polarized intersects the origin (point C in fig. 3), whereas in reflection the discontinuity is at the origin. The vectorial coherent transfer function defined here is a vector quantity. It contains information about imaging for different illumination polarizations, and for different polarization properties of the object. 

## 5 The three-dimensional vectorial optical transfer function

The three-dimensional vectorial optical transfer function is defined analogously with the scalar OTF: it is simply the (suitably normalised) 3-D Fourier transform of the intensity in the focal region [16]. In a system with high NA the vectorial OTF is very different from the traditional scalar OTF, as we shall see presently. Using the well known relation between the modulus square of a function (the electric field in this case) and its FT which is an autocorrelation we find that the overall vectorial OTF is also a scalar function. This can be represented mathematically as follows: the intensity related to the electric field is given by the scalar product with complex conjugation 

$$
I (\boldsymbol {r}) = | \boldsymbol {q} (\boldsymbol {r}) | ^ {2} = \boldsymbol {q} (\boldsymbol {r}) \cdot \boldsymbol {q} ^ {*} (\boldsymbol {r}).\tag{16}
$$

So the Fourier transform is the OTF 

$$
\tilde {I} (m) = Q (m) \otimes_ {3} Q ^ {*} (m)\tag{17}
$$

where the $\otimes_{3}$ sign indicates 3-D convolution. Note that convolution with a reversed and conjugated function is a correlation. A more detailed development of the 3-D (scalar) OTF can be found in the recent book by Gu [17]. The 3-D correlation is easily split into its 3 component parts, just as the intensity has 3 cartesian components. 

$$
\boldsymbol {q} (\boldsymbol {r}) \cdot \boldsymbol {q} ^ {*} (\boldsymbol {r}) = q _ {x} ^ {2} + q _ {y} ^ {2} + q _ {z} ^ {2}\tag{18}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/23df7d24fbfced791d055bd316ce0c9795a5cb58f3fc34575bf5345da2a1892d.jpg)



Fig. 5. A representation of the 3-D OTF of a 0.95 NA optical system. Only the half of the OTF for n > 0 has been shown in an attempt to clarify some details of the spatial distribution. The shape is often described as a “donut” with a cusp in the s = 0 rim region. The volume defined within the mesh is the region of support for the 3-D OTF; the actual values in this region depend upon the particular pupil function distribution.


and 

$$
\begin{array}{r l} & Q (m) \otimes_ {3} Q ^ {*} (m) \\ & \equiv Q _ {x} \otimes_ {3} Q _ {x} ^ {*} + Q _ {y} \otimes_ {3} Q _ {y} ^ {*} + Q _ {z} \otimes_ {3} Q _ {z} ^ {*}. \end{array}\tag{19}
$$

Although the overall OTF is rather difficult to calculate analytically (we are not aware of an analytic solution for the vectorial form, but the high angle scalar OTF has been calculated by Sheppard et al. [11]) it is almost trivial to calculate using the FFT in 3-D. The 3-D OTF is a very different function from the 3-D pupil function. Readers unfamiliar with 3-D imaging theory may find some of the 3-D visualisation difficult at first. A representation of the 3-D OTF of a 0.95 NA optical system is displayed in fig. 5. Only the half of the OTF for n > 0 has been shown in an attempt to clarify some details of the spatial distribution. The shape is often described as a “donut” with a cusp in the s = 0 rim region. Figure 5 only shows the region of support for the 3-D OTF; the actual values in this region depend crucially upon the pupil function distribution. One final feature to note is the so called “missing cone” in the m = n = 0 region. It is, perhaps, informative to look now at the corresponding vectorial 2-D OFTs. These can also be simply calculated using the projection-slice theorem applied to a 2-D slice in the focal plane (transverse intensity distribution). The problem reduces to a 2-D autocorrelation of the vector pupil projections because of the special property of the pupil function (i.e. its existence only on a spherical shell). Consider the intensity in the focal plane, $I_{t}(x, y)$ 

$$
\begin{array}{l} I (\boldsymbol {r}) = I (x, y, z) \\ I _ {t} (x, y) = I (x, y, 0) = | \boldsymbol {q} (x, y, 0) | ^ {2}. \end{array}\tag{20}
$$

Then the 2-D FT of this intensity is the 2-D vectorial OTF, which in turn is the projection of the 3-D vectorial OTF: 

Slice 

$$
I _ {t} (x, y) = I (x, y, 0)\tag{21}
$$

Projection 

$$
\tilde {I} _ {t} (m, n) = \int_ {- \infty} ^ {\infty} \tilde {I} (m, n, s) d s\tag{22}
$$

Correlation 

$$
\tilde {I} (m) = \int_ {- \infty} ^ {\infty} Q (m ^ {\prime}) \cdot Q ^ {*} (m ^ {\prime} + m) d m.\tag{23}
$$

But from equation (11) we have a function existing only on a sphere, so, we can write 

$$
\begin{array}{l} \widetilde {I} (m) = \int_ {- \infty} ^ {\infty} \left\{\boldsymbol {P} (m ^ {\prime}, n ^ {\prime}) \delta (s ^ {\prime} - s _ {0}) \right\} \\ \cdot \left\{\boldsymbol {P} ^ {*} (m ^ {\prime} - m, n ^ {\prime} - n) \delta (s ^ {\prime} - s - s _ {0}) \right\} d m d n d s. \end{array}\tag{24}
$$

The projection then simplifies to 

$$
\begin{array}{r l} \tilde {I} _ {t} (m, n) & = \int_ {- \infty} ^ {\infty} P (m ^ {\prime}, n ^ {\prime}) \cdot P ^ {*} (m ^ {\prime} - m, n ^ {\prime} - n) \mathrm{dmdn} \\ & = P (m, n) \otimes_ {2} P ^ {*} (- m, n). \end{array} \tag{25}
$$

In summary; the projection of the 3D OTF can be obtained from the 2D autocorrelation of the projected pupil function. This is very convenient for 2D calculations and is used implicitly in conventional 2D imaging theory. We can now evaluate the vectorial OTF for a typical optical system and compare it to the result of high NA scalar theory. We have concentrated on the transverse intensity and transverse 2-D OTF in this paper as it is easier to compare our results with other, well known, results. In practice the axial section OTFs are also very simple to calculate. 

Fig. 6 shows a contour/density plot of the well known scalar OTF for transverse incoherent imaging. The distribution is known as a Chinese that function. Note, however, that in this case we are looking at a very high NA, 0.95 in fact, which corresponds to an aperture semi-angle of $72^{\circ}$ . The horizontal (m) and vertical (n) spatial frequency axes extend to a value of $\pm2$ , which corresponds to the maximum frequency attainable with an idealized system of NA = 1.0. Note that we have assumed an apodization corresponding to the Herschel condition in this example because it can be expected to have more pronounced vector effects at high NA. 

Fig. 7 shows the x-component derived from the full vectorial analysis for a 0.95 Herschel lens. The input polarisation is assumed to be in the x direction which in turn corresponds to horizontal spatial frequencies (m). An unexpected feature is the central elongation in the horizontal (m) direction and peripheral elongation in the perpendicular (n) direction. Figure 8 shows the Y vector components of the OTF. It contains positive and negative regions, with a central positive zone. The background grey level represents zero in this figure so there are 4 negative regions (shown as black) and 5 positive regions (shown as lighter grey). The overall effect of this component is small as it only represents about 2.9% of overall 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/7e9d73c32022e5fcd63fbedb100106becbfd50137c41d3161d3860cedf0b0d75.jpg)



Fig. 6. A countour/density plot of the well known scalar OTF for transferse incoherent imaging. The distribution is known as a Chinese hat function.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/0d3bfc34c6ed5ec5191e3672ef070dd743c96f6b3739644f6bd007701c7f6ee9.jpg)



Fig. 7. The x-component derived from the full vectorial analysis for a 0.95 Herschel lens. The input polarization is assumed to be in the x direction which in turn corresponds to horizontal spatial frequencies (m). An unexpected feature is the central elongation in the horizontal (m) direction and peripheral elongation in the perpendicular (n) direction.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/6c2467332066f93c5feb86085cdc808a0730943101e4140ad0cdc9709d4b0f84.jpg)



Fig. 8. The y vector components of the OTF. It contains both positive and negative regions, with a central positive zone. The background grey level represents zero in this figure so there are 4 negative regions (shown as black) and 5 positive regions (shown a lighter grey). The overall effect of this components is small as it only represents about 2.9% of overall OTF.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/5e19f88175cdee785bc409668f69281eff8a1720fddd0c2d6e6e9ecf422861b4.jpg)



Fig. 10. The total (x plus y plus z) OTF which is clearly very different from the simple high NA scalar approximation in Fig. 6. Careful inspection of this OTF reveals negative regions on the left and right of peak (shown as the darkest shade). This is rather surprising as it means that there is a contrast reversal for a range of transverse spatial frequencies.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/64a262fc7509683036c679c0f054f2136d17d5f4ffdf09beaef27a604fe31215.jpg)



Fig. 9. The z component of OTF. Again there are positive and negative regions, but this time with two-fold symmetry not four-fould. The midgrey background again represents zero. The contribution of this components to the total OTF is much more significant with almost 30% at the peak.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/5438cef6339f6a8d76dcfe01dd3e3f3fa56214803c2483b9c68a5200ba9c355a.jpg)



Fig. 11. The difference between the high NA scalar theory and high NA vectorial theory. The very different frequency responses in the m direction are primarily due to the z component of the vectorial OTF.


OTF. A recent paper by Flagello [7] remarked upon the small overall contribution of the Y component to imaging in high NA lithographic systems. Fig. 9 shows the Z component of OTF. Again there are positive and negative regions, but this time two-fold symmetry not fourfold. The mid-grey background again represent zero. The contribution of this component to the total OTF is much more significant with almost 30% at the peak. Fig. 10 shows the total (X plus Y plus Z)) OTF which is clearly very different to the simple high NA scalar approximation in fig. 6. Careful inspection of this OTF reveals negative regions on the left and right of peak (shown as the darkest shade). This is rather surprising as it means that there is a contrast reversal for a range of transverse spatial frequencies. Similar calculations for a 0.95 NA system satisfying the sine condition also show this contrast reversal. This is an important and unexpected result. One obvious consequence is that conventional image deconvolution techniques will be seriously in error if they use the scalar approximation to the OTF instead of the full vectorial form. The most extreme negative value is 4.3% of the OTF peak value. Even in the aplanatic case the extreme negative is 3.9% of peak. Fig. 11 illustrates the difference between the high NA scalar theory and high NA vectorial theory. The very different frequency responses in the m direction are primarily due to the z component of the vectorial OTF. 

This paper is just an introduction to the concept of vectorial pupil functions and vectorial transfer function. We realize that much of this is implicit in the detailed vector theory of focusing of EM waves. However, the transfer/pupil functions have an important role in the linear systems approach to imaging in optical system and can be usefully interpreted in a full 3-D theory which is in many ways simpler than the 2-D theory. One obvious factor is that the 3-D theory does not require the ubiquitous quadratic phase factor in many calculations. This phase factor is implicit in the geometric form (spherical cap) of the pupil functions and is easily extended to the high NA situation in which quadratic phase must tend towards the more correct spherical phase. One final observation regarding the calculation of the vectorial OTFs is that the data in each figures was generated in just a few seconds using a 2-D FFT program initially developed for image processing on a personal computer. The final OTF resolution is $145 \times 145$ pixels at 8 bit quantization. The calculation procedure is as follows: Firstly, the 2-D projections of the vector pupil function are generated from the simple algebraic forms in equation (5). Secondly, pupil projections are precisely autocorrelated, cross-correlated or convolved (as required) using FFT procedures. Finally the various components are added together to give the overall vectorial OTF. There is the additional option to Fourier transform the vectorial OTF to find a chosen 2-D slice of the focal region intensity. 

## 6 Analogues of the optical transfer function

In the scalar optics the OTF is the Fourier transform of the intensity PSF. The 2-D OTF is thus the 2-D Fourier transform of the 2-D intensity PSF, while the 3-D OTF is the 3-D Fourier transform of the 3-D intensity PSF [13]. These can be considered as autocorrelations of the pupil functions. For a self-luminous object, usually the image is detected by a device which is sensitive to electric energy density. Thus the relevant PSF is the time-averaged electric energy density in the focused distribution. The OTF is then scalar autocorrelation of the vectorial pupil function. Similarly for fluorescence imaging, the object is excited by the incident electric energy. It is also possible to define a vectorial OTF, given by the vector correlations of the vectorial pupil functions. Such a concept can be used to describe the distribution of the Poynting vector $S = E \times H$ . As a final illustration of the power of the vectorial OTF concept, we have shown the transverse component of the vectorial OTF for the Poynting vector in fig. 12. The exact details of the calculation can be omitted for brevity but only involve three 2-D cross-correlations. The axial components looks very much like fig. 5 and have not been shown here. The most obvious feature is the strong fourfold symmetry and this can be expected to the strongly indicative of the local transverse power flow in the focal plane. This is an area for further research. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-06/92bcc930-037c-45ef-8707-57900d8f4941/9d7272a5b5a8f80470d6e37f98ac472538c339fb5dd560abce6427c91e75bb46.jpg)



Fig. 12. The transverse component of the vectorial OTF for the Poynting vector $S = E \times H$ . The most obvious feature is the strong fourfold symmetry and this can be expected to be strongly indicative of the local transverse power flow in the focal plane.


## 7 Discussion

The vectorial form of the 2-D and 3-D pupil functions for high-aperture systems has been introduced. In analogy to scalar theory this leads to the concept of the coherent and optical transfer functions for coherent and incoherent systems respectively. In the case of the vectorial OTF we have shown that it can be very different from the scalar OTF as NAs typically found in optical microscopy and optical lithography. Fortunately the vectorial OTF is easy to calculate using widely available FFT software applied for each of the vector components in turn. One surprising results of this work is that the vectorial OTF has been shown to have negative values at certain spatial frequencies. A small departure from the radial symmetry of the scalar OTF was expected, but contrast reversal was not. 

In practice the generalisation of the coherent transfer function and optical transfer function to the vectorial case must be considered in conjunction with interaction with the object. For example, in the Born approximation, the object is regarded as an assembly of scattering points, each of which scatters as an electric dipole. Thus the directionality of the dipole radiation should be incorporated into an imaging theory. On the other hand, a small hole in a perfectly conducting sheet may be considered to behave as a magnetic dipole. In a similar way, the theory of fluorescence imaging may be analysed by due consideration of dipole orientation. For a general strongly scattering object it is not in fact possible to treat the polarization properties of imaging in terms of a transfer function description. These aspects are being considered, but in the meantime the concept of a transfer function can be seen to be useful for appreciation of the relative optical performance of various focusing systems. 

## Acknowledgements

The authors acknowledge the support of the Australian Research Council and the Science Foundation for Physics in the University of Sydney. 

## References



[1] B. Richards, E. Wolf: Electromagnetic diffraction in optical systems. II Structure of the image field in an aplanatic system. Proc. Royal Soc. Lond. A 235 (1959) 358–379. 





[2] M. Mansuripur: Distribution of light at and near the focus of high-numerical-aperture objectives. J. Opt. Soc. Am. A 3 (1986) 2986-2093. 





[3] M. Mansuripur: Certain computational aspects of vector diffraction problems. J. Opt. Soc. Am. A 6 (1989) 786–805. 





[4] C. J. R. Sheppard, M. Gu: Imaging by a high aperture optical system. J. Mod. Opt. 40 (1993) 1631–1651. 





[5] C. J. R. Sheppard, K. G. Larkin: Optimal concentration of electromagnetic radiation. J. Mod. Opt. 41 (1994) 1495–1505. 





[6] C. J. R. Sheppard: Electromagnetic field in the focal region of wide-angular annular lens and mirror systems. IEE J. Microw. Opt. Acoust. 2 (1978) 136–166. 





[7] D. G. Flagello, T. Milster, A. E. Rosenbluth: Theory of high-NA imaging in homogeneous thin films. J. Opt. Soc. Am. A 13 (1996). 





[8] C. W. McCutchen: Generalized aperture and the three-dimensional diffraction image. J. Opt. Soc. Am. A 54 (1964). 





[9] C. J. R. Sheppard and C. J. Cogswell: Three-dimensional image formation in confocal microscopy. J. Microsc. 159 (1960) 179–194 (1990). 





[10] R. N. Bracewell: Two-Dimensional Imaging. Prentice Hall, Englewood Cliffs, New Jersey 1995. 





[11] C. J. R. Sheppard, M. Gu, Y. Kawata, S. Kawata: Three-Dimensional transfer functions for high aperture systems. J. Opt. Soc. Am. A 11 (1994) 593–598. 





[12] R. Barakat, D. Lev: Transfer function and total illuminance of high numerical aperture systems obeying the sine condition. J. Opt. Soc. Am. 53 (1963) 324–332. 





[13] E. Wolf: Three-dimensional structure determination of semi-transparent objects from holographic data. Opt. Commun. 1 (1969) 153 - 156. 





[14] M. Kaveh, M. Soumekh: Computer-Assisted Diffraction Tomography. In: H. Stark (ed.): Image recovery: theory and application. pp. 369–413. Academic Press, Orlando 1987. 





[15] C. J. R. Sheppard: General considerations of diffraction theory of 3-D imaging. Eur. J. Cell Biology 48, (Suppl. 25) (1989) 29–32. 





[16] B. R. Frieden: Optical transfer of the three-dimensional object. J. Opt. Soc. Am. A 57 (1967) 56–66. 





[17] M. Gu: Principles of three-dimensional imaging in confocal microscopes. World Scientific, Singapore 1996. 

