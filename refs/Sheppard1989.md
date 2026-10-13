# Three-dimensional imaging in a microscope

C. J. R. Sheppard and X. Q. Mao 

Department of Engineering Science, Oxford University, Parks Road, Oxford OX1 3PJ, UK 

Received June 10, 1987; accepted March 3, 1989 

Three-dimensional imaging in transmission and incident light microscopes is considered. Two-point resolution and images of lines and planes are discussed. The transfer functions for partially coherent systems are developed. 

## 1. INTRODUCTION

It is well known from geometrical optics that a three-dimensional image is formed from a thick object. Diffraction theory of three-dimensional imaging has also been presented for coherent $^{1,2}$ and incoherent systems. $^{3}$ Streibl $^{4}$ considered imaging in a microscope of transmission geometry, based on the first Born approximation, that is, neglecting multiple scattering and depletion of the incident beam. Condenser apertures of various sizes were considered, but the treatment was restricted to the imaging of weak objects, such that the interference of diffracted light with diffracted light was neglected. The spatial-frequency cutoff in three-dimensional imaging, for transmission and reflection systems of high numerical aperture, has also been discussed. $^{5,6}$ 

Here we investigate imaging according to the paraxial (small-aperture) approximation for transmitted-light and incident-light systems. Although the object is assumed to be weakly scattering so that the first Born approximation is valid, we nevertheless retain the second-order (bilinear) terms, arising from the interference of diffracted light with diffracted light, in the image intensity. One reason for doing this is to investigate the differences between conventional and confocal systems; the latter will be considered in a forthcoming paper. Retaining the second-order terms is necessary because for weakly scattering objects, such that second-order terms are negligible, imaging is identical in transmission-mode conventional and confocal systems. We show below that some of the results are not limited in applicability to weakly scattering objects. 

## 2. THREE-DIMENSIONAL IMAGING

We define optical coordinates $(v_{0}, w_{0}, u_{0})$ and $(v, w, u)$ for the object and image regions: 

$$
\begin{array}{r l} & v _ {0} = k x _ {0} \sin \alpha_ {1}, \qquad v = k x \sin \alpha , \\ & w _ {0} = k y _ {0} \sin \alpha_ {1}, \qquad w = k y \sin \alpha , \\ & u _ {0} = 4 k z _ {0} \sin^ {2} (\alpha_ {1} / 2), \qquad u = 4 k z \sin^ {2} (\alpha / 2), \end{array}\tag{1}
$$

where $\sin\alpha$ is the numerical aperture, k is $2\pi/\lambda$ , and $x_{0}$ , x, etc. are distances in object and image space. The given expression for u is a better approximation than the usual one $^{7}$ for higher values of $\alpha$ . Consider a system with critical illumination (Fig. 1), with lenses with pupils $P_{1,2}(\xi, \eta)$ , the coordinates $(\xi, \eta)$ being normalized such that the ray $\xi^2 + \eta^2 = 1$ intersects the edge of the objective pupil. The point-spread functions of the lenses thus are given by $^{1}$ 

$$
\begin{array}{c} h _ {1} (\mathbf {v} _ {0}) = \int \int P _ {1} (\xi_ {1}, \eta_ {1}) \exp \left\{j u \left[ \frac {1}{4 \sin^ {2} (\alpha / 2)} - \frac {1}{2} \left(\xi_ {1} ^ {2} + \eta_ {1} ^ {2}\right) \right] \right\} \\ \times \exp [ - j (\xi_ {1} v _ {0} + \eta_ {1} w _ {0}) ] d \xi_ {1} d \eta_ {1}, \tag{2a} \end{array}
$$

$$
\begin{array}{r} h _ {2} (\mathbf {v}) = \int \int P _ {2} (\xi_ {2}, \eta_ {2}) \exp \left\{j u \left[ \frac {1}{4 \sin^ {2} (\alpha / 2)} - \frac {1}{2} (\xi_ {2} ^ {2} + \eta_ {2} ^ {2}) \right] \right\} \\ \times \exp [ - j (\xi_ {2} v + \eta_ {2} w) ] d \xi_ {1} d \eta_ {1}, \end{array} \tag {2b}
$$

where v represents the vector whose components are v, w, and u, respectively. In the case of incident light, the sign of u in Eq. (2b) should be changed. 

Assume that the three-dimensional object may be characterized by a scattering distribution $^{2}$ $t(\mathbf{v}_{0})$ , representing the scattering per unit volume, which is related to the refractive index n by 

$$
t (\mathbf {v} _ {0}) = j k ^ {2} [ 1 - n ^ {2} (\mathbf {v} _ {0}) ].\tag{3}
$$

Both n and t are in general complex, and the j accounts for the fact that in a lossless medium the scattered wave is in phase quadrature to the direct wave. We assume that the first Born approximation holds. We neglect the unscattered radiation, which is a valid assumption both for dark-field and for incident-light microscopy because no direct (unscattered) radiation contributes to the image. For transmission microscopy in bright field, however, we must make an appropriate choice for $t(\mathbf{v}_{0})$ to allow for the direct radiation. We return to this point below. The image intensity can be summed over the elemental slices that constitute the object because the first Born approximation means that the principle of superposition is valid. Furthermore it must be integrated over the incoherent source of intensity distribution $S(\mathbf{v}_{1})$ , giving 

$$
\begin{array}{r l r} & & {I (\mathbf {v}) = \int \int S (\mathbf {v} _ {1}) \left| \int h _ {1} (\mathbf {v} _ {0} - \mathbf {v} _ {1}) t (\mathbf {v} _ {0}) h _ {2} (\mathbf {v} - \mathbf {v} _ {0}) \mathrm{d} \mathbf {v} _ {0} \right| ^ {2} \mathrm{d} x _ {1} \mathrm{d} y _ {1}} \\ & & {= \int \int g (\mathbf {v} _ {0} ^ {\prime} - \mathbf {v} _ {0}) t (\mathbf {v} _ {0}) t ^ {*} (\mathbf {v} _ {0} ^ {\prime}) h _ {2} (\mathbf {v} - \mathbf {v} _ {0}) h _ {2} ^ {*} (\mathbf {v} - \mathbf {v} _ {0} ^ {\prime}) \mathrm{d} \mathbf {v} _ {0} \mathrm{d} \mathbf {v} _ {0} ^ {\prime},} \end{array}\tag{4}
$$

in which $g(\mathbf{v}_0' - \mathbf{v}_0)$ is the mutual intensity function given by 

Source 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/1f15c65d3311dae1ba84150bb422faf81e8ff35098e6cb99202c22da53aa5f51.jpg)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/6b057453dbb57a28c278bdc8df36f7f7378a0c57c4f3e880481e986e930bbe10.jpg)

$$
g (\mathbf {v} _ {0} ^ {\prime} - \mathbf {v} _ {0}) = \int \int h _ {1} (\mathbf {v} _ {0} - \mathbf {v} _ {1}) h _ {1} ^ {*} (\mathbf {v} _ {0} ^ {\prime} - \mathbf {v} _ {1}) S (\mathbf {v} _ {1}) d x _ {1} d y _ {1}.\tag{5}
$$

We see that, for an infinite and uniform source on the plane $(x, y, z)$ , 

$$
\begin{array}{l} g \left(\mathbf {v} _ {0} ^ {\prime} - \mathbf {v} _ {0}\right) = \int \int \left| P _ {1} \left(\xi_ {1}, \eta_ {1}\right) \right| ^ {2} \exp \{- j \left[ \xi_ {1} \left(v _ {0} - v _ {0} ^ {\prime}\right) \right. \\ \left. + \eta_ {1} \left(w _ {0} - w _ {0} ^ {\prime}\right) \right] \} \exp \left\{j \left(u _ {0} - u _ {0} ^ {\prime}\right) \left[ \frac {1}{4 \sin^ {2} \left(\alpha_ {1} / 2\right)} \right. \right. \\ \left. - \frac {1}{2} \left(\xi_ {1} ^ {2} + \eta_ {1} ^ {2}\right) \right] \Bigg \} d \xi_ {1} d \eta_ {1}. \end{array} \tag {6}
$$

If the diameter of the condenser pupil is small and the illumination is provided by a plane wave, then g reduces to a constant phase variation along the axis, which for the transmission geometry cancels with those of $h_{2}$ , and illumination is coherent for both the lateral and the axial directions. If, on the other hand, the diameter of the condenser pupil is large compared with that of the objective pupil, the degree of coherence is small in both the lateral and the axial directions. Equation (4) may be used conveniently to calculate the images of single points, lines, or planes or pairs of points, lines, or planes distributed in three dimensions. 

Fig. 1. Geometry of the optical system in (a) transmission and (b) incident light. 

## 3. TWO AXIAL POINTS

For the case of two axial point scatterers suspended in space and separated by a normalized distance 2a, we have, for the transmission geometry, 

$$
\begin{array}{r l} I (u) & = | h _ {2} (u - a) | ^ {2} + | h _ {2} (u + a) | ^ {2} \\ & \quad + 2 \operatorname{Re} [ g (2 a) h _ {2} (u + a) h _ {2} ^ {*} (u - a) ]. \end{array}\tag{7}
$$

We consider the case of circular pupils free from aberrations. Note that this example is an ideal case, as, of course, it is impossible to have two point scatterers with no unscattered radiation in a bright-field transmission system, but nevertheless it illustrates some important features. Furthermore it is precisely analogous to the two-dimensional case in which the Rayleigh criterion for two-point resolution, which applies strictly for two bright points in a dark background, is used to predict resolution in a semitransparent object. The spread functions for the lenses have axial variations: 

$$
g (u) = \exp \left\{j \frac {u}{4} \left[ \cot^ {2} \frac {\alpha}{2} + (1 - s ^ {2}) \right] \right\} \left[ \frac {\sin \left(s ^ {2} u / 4\right)}{s u ^ {2} / 4} \right],\tag{8}
$$

$$
h _ {2} (u) = \exp \biggl (j \frac {u}{4} \cot^ {2} \frac {\alpha}{2} \biggr) \biggl [ \frac {\sin (u / 4)}{u / 4} \biggr ],\tag{9}
$$

in which 

$$
s = \sin (\alpha_ {1} / _ {2}) / \sin (\alpha / 2),\tag{10}
$$

so that the intensity is 

$$
\begin{array}{r l} I (u) & = \left[ \frac {\sin (u - a) / 4}{(u - a) / 4} \right] ^ {2} + \left[ \frac {\sin (u + a) / 4}{(u + a) / 4} \right] ^ {2} + 2 \cos \left[ \frac {a (s ^ {2} - 1)}{2} \right] \\ & \times \frac {\sin (s ^ {2} a / 2)}{s ^ {2} a / 2} \left\{\frac {\sin [ (u + a) / 4 ]}{(u + a) / 4} \right\} \left\{\frac {\sin [ (u - a) / 4 ]}{(u - a) / 4} \right\}, \end{array} \tag {11}
$$

with 

$$
a = 4 \Delta k \sin^ {2} (\alpha / 2),\tag{12}
$$

in which $\Delta$ is the absolute distance between the two points.
The third term of Eq. (10) vanishes for $s^{2}a \rightarrow \infty$ . In this case resolution is the same as for incoherent imaging. 

For a value of $a$ of $2\pi$ , the image of one point is situated on the first zero of the image of the other. This corresponds to Rayleigh resolution, although in this case the ratio of the intensity midway between the points to that at the point is $8/\pi^2 = 0.811$ rather than 0.735, the ratio for lateral resolution [Eq. (3)]. This may be taken as the definition of resolution in the axial direction. For this separation the third term also vanishes for $s = 0$ , so that the coherent image is the same as the incoherent image. This is also true for all integer values of $s^2$ , so that the intensity midway between the points is $8/\pi^2$ and the two-point resolution is the same for coherent, full ( $s = 1$ ), or incoherent illumination. The images are identical only for this particular spacing, however. For closer spacing the coherent system gives a poorer image than the incoherent one, whereas for slightly greater spacing the coherent system gives a better image. 

For the case of incident light [Fig. 1(b)] the behavior is more complicated. Now the point-spread function for the objective $h_{2}(u)$ is different from Eq. (9) and is given by 

$$
h _ {2} (u) = \exp \left(- j \frac {u}{4} \cot^ {2} \frac {\alpha}{2}\right) \left[ \frac {\sin (u / 4)}{u / 4} \right],\tag{13}
$$

and the axial intensity is 

$$
\begin{array}{l} I (u) = \left\{\frac {\sin [ (u - a) / 4 ]}{(u - a) / 4} \right\} ^ {2} + \left\{\frac {\sin [ (u + a) / 4 ]}{(u + a) / 4} \right\} ^ {2} \\ \qquad + 2 \cos \left\{\left[ \cot^ {2} \frac {\alpha}{2} \frac {(1 - s ^ {2})}{2} \right] a \right\} \frac {\sin (s ^ {2} a / 2)}{s ^ {2} a / 2} \\ \qquad \times \left\{\frac {\sin [ (u - a) / 4 ]}{(u - a) / 4} \right\} \left\{\frac {\sin [ (u + a) / 4 ]}{(u + a) / 4} \right\}. \end{array}\tag{14}
$$

The resolution for $s^{2}a \rightarrow \infty$ is the same as for the transmission case, but for finite values of s the third term depends critically on the spacing because of interference effects. 

## 4. AN AXIAL LINE

The image of an axial line scatterer (assumed to be long compared with the spread function of the system) in transmission may be calculated from Eq. (4) by putting 

$$
t (\mathbf {v} _ {0}) = \delta (v _ {0}) \delta (w _ {0}).\tag{15}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/5283f041cc12cba71975a49e5a7c618090c2763b5c7376d37a1490ff18decfc3.jpg)

Fig. 2. Image of an axial line in a transmission system. $s \geq 1$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/3cd48d1fc1dd9942aa30782f8e4ea1f78535f4a507ad9f18e573f4ce5129a156.jpg)

Fig. 3. Image of an axial line in an incident light system, $s = \cot(\alpha/2)$ . 

Substituting for g and $h_{2}$ from Eqs. (6) and (2), and integrating over $u_{0}$ and $u_{0}'$ , we obtain 

$$
\begin{array}{l} I (\mathbf {v}) = \int \int \left\{\int \int P _ {2} \left(\xi_ {2}, \eta_ {2}\right) \exp \left[ - j \left(\xi_ {2} v + \eta_ {2} w\right) \right. \right. \\ \left. - \frac {1}{2} j u \left(\xi_ {2} ^ {2} + \eta_ {2} ^ {2}\right) \right] \delta \left(\xi_ {1} ^ {2} + n _ {1} ^ {2} - \xi_ {2} ^ {2} - \eta_ {2} ^ {2}\right) d \xi_ {2} d \eta_ {2} \Bigg \} \\ \times \left\{\int \int P _ {2} ^ {*} \left(\xi_ {2} ^ {\prime}, \eta_ {2} ^ {\prime}\right) \exp \left[ - j \left(\xi_ {2} ^ {\prime} v + \eta_ {2} ^ {\prime} w\right) \right. \right. \\ \left. - \frac {1}{2} j u \left(\xi_ {2} ^ {\prime 2} + \eta_ {2} ^ {\prime 2}\right) \right] \delta \left(\xi_ {1} ^ {2} + \eta_ {1} ^ {2} - \xi_ {1} ^ {\prime 2} - \eta_ {1} ^ {\prime 2}\right) d \xi_ {2} ^ {\prime} d \eta_ {2} ^ {\prime} \Bigg \} \\ \times | P _ {1} (\xi_ {1}, \eta_ {1}) | ^ {2} d \xi_ {1} d \eta_ {1}. \end{array} \tag {16}
$$

For circularly symmetrical systems we thus obtain 

$$
I (\rho) = \int \int | P _ {1} (\xi) | ^ {2} | P _ {2} (\xi) | ^ {2} J _ {0} ^ {2} (\xi \rho) \xi \mathrm{d} \xi ,\tag{17}
$$

in which $J_0$ is a zero-order Bessel function and $\rho = (v^2 + w^2)^{1/2}$ . For a coherent system, $|P_1(\xi)|^2 = \delta(\xi)$ , there is no transverse variation in intensity, but for $s \geq 1$ we have 

$$
I (\rho) = \int_ {0} ^ {1} J _ {0} ^ {2} (\xi \rho) \xi \mathrm{d} \xi = \frac {1}{2} \left[ J _ {0} ^ {2} (\rho) + J _ {2} ^ {2} (\rho) \right],\tag{18}
$$

which is shown in Fig. 2. This expression is the same as that derived for a purely incoherent system. 

Again the incident-light system gives different results because of the different phase distributions of the illumination, so that we now have, for circular symmetry, 

$$
I (\rho) = \int_ {0} ^ {\infty} \left| P _ {1} \left[ \left(\frac {1}{\sin^ {2} (\alpha / 2)} - \xi^ {2}\right) ^ {1 / 2} \right] \right| ^ {2} | P _ {2} (\xi) | ^ {2} J _ {0} ^ {2} (\xi \rho) \xi \mathrm{d} \xi .\tag{19}
$$

Because the maximum value of $\xi$ is 1, Eq. (19) is equal to 0, which means that there is no image unless $s \geq \cot(\alpha/2)$ . For $s = \cot(\alpha/2) > 1$ the intensity distribution in the image is 

$$
I (\rho) = J _ {0} ^ {2} (\rho),\tag{20}
$$

which is shown in Fig. 3. 

## 5. THREE-DIMENSIONAL TRANSFER FUNCTION IN TRANSMISSION

Equation (4) is symmetrical with respect to the three coordinates. We now introduce the three-dimensional object spectrum 

$$
t (\mathbf {v} _ {0}) = \int T (\mathbf {m}) \mathrm{exp} (j \mathbf {m} \cdot \mathbf {v} _ {0}) \mathrm{d} \mathbf {m},\tag{21}
$$

which gives, for the image intensity, 

$$
I (\mathbf {v}) = \int \int C (\mathbf {m}; \mathbf {m} ^ {\prime}) T (\mathbf {m}) T ^ {*} (\mathbf {m} ^ {\prime}) \exp [ j (\mathbf {m} - \mathbf {m} ^ {\prime}) \cdot \mathbf {v} ] d \mathbf {m} d \mathbf {m} ^ {\prime},\tag{22}
$$

in which $C(\mathbf{m}; \mathbf{m}')$ is a six-dimensional partially coherent transfer function (transmission cross coefficient) given by 

$$
\begin{array}{l} C (\mathbf {m}; \mathbf {m} ^ {\prime}) = \int \int | P _ {1} (\xi , \eta) | ^ {2} P _ {2} (\xi - m, \eta - n) P _ {2} ^ {*} (\xi - m ^ {\prime}, \eta - n ^ {\prime}) \\ \times \delta [ r - m \xi - n \eta + ^ {1 / 2} (m ^ {2} + n ^ {2}) ] \delta [ r ^ {\prime} - m ^ {\prime} \xi - n ^ {\prime} \eta \\ + ^ {1 / 2} (m ^ {\prime 2} + n ^ {\prime 2}) ] d \xi d \eta , \end{array} \tag {23}
$$

in which the two delta functions represent lines in the $(\xi, \eta)$ plane, and hence the transfer function is appreciable only if the condition 

$$
m ^ {\prime} n = n ^ {\prime} m\tag{24}
$$

is satisfied, in which case we lose no generality by taking $n = n' = 0$ . Introducing 

$$
\xi^ {\prime} = \xi - ^ {1} / _ {2} (m + m ^ {\prime}),\tag{25}
$$

we obtain 

$$
\begin{array}{r l} C (m, 0, r; m ^ {\prime}, 0, r ^ {\prime}) & = \int \int \left| P _ {1} \bigg [ \xi^ {\prime} + \frac {1}{2} (m + m ^ {\prime}), \eta \bigg ] \right| ^ {2} \\ & \times P _ {2} [ \xi^ {\prime} - ^ {1} / _ {2} (m - m ^ {\prime}), \eta ] P _ {2} ^ {*} [ \xi^ {\prime} + ^ {1} / _ {2} (m - m ^ {\prime}), \eta ] \\ & \times \delta (r - \xi^ {\prime} m - ^ {1} / _ {2} m m ^ {\prime}) \delta (r ^ {\prime} - m ^ {\prime} \xi^ {\prime} - ^ {1} / _ {2} m m ^ {\prime}) \mathrm{d} \xi^ {\prime} \mathrm{d} \eta , \end{array}\tag{26}
$$

which is zero unless 

$$
\xi^ {\prime} = \frac {r}{m} + \frac {m ^ {\prime}}{2} = \frac {r ^ {\prime}}{m ^ {\prime}} + \frac {m}{2}.\tag{27}
$$

This condition is satisfied if $m = m'$ and $r = r'$ or if $m' = r' = 0$ (or if $m' = r'$ assume other values). We can thus write 

$$
\begin{array}{l} C (m, 0, r; m ^ {\prime}, 0, r ^ {\prime}) = \frac {1}{m m ^ {\prime}} \delta \left[ \frac {r}{m} - \frac {r ^ {\prime}}{m ^ {\prime}} - \frac {1}{2} (m - m ^ {\prime}) \right] \\ \times \int \int \left| P _ {1} \left[ \xi^ {\prime} + \frac {1}{2} (m + m ^ {\prime}), \eta \right] \right| ^ {2} P _ {2} \left[ \xi^ {\prime} - \frac {1}{2} (m - m ^ {\prime}), \eta \right] \\ \times P _ {2} ^ {*} \left[ \xi^ {\prime} + \frac {1}{2} (m - m ^ {\prime}), \eta \right] \delta \left[ \xi^ {\prime} - \left(\frac {r - r ^ {\prime}}{m - m ^ {\prime}}\right) \right] d \xi^ {\prime} d \eta . \end{array} \tag{28}
$$

From Eq. (23) we obtain the transfer function for various special cases. For $m = n = m' = n' = 0$ , we obtain 

$$
C (0, 0, r; 0, 0, r ^ {\prime}) = \pi s ^ {2} \delta (r) \delta (r ^ {\prime}), \quad s \leq 1,\tag{29}
$$

so that no image is formed from an object with structure only in the axial direction. For $r = r' = 0$ , we obtain 

$$
\begin{array}{l} C (m, 0, 0; m ^ {\prime}, 0, 0) \\ = \left\{ \begin{array}{l l} \frac {2}{m m ^ {\prime}} \delta (m - m ^ {\prime}) \mathrm{Re} \bigg [ s ^ {2} - \bigg (\frac {m}{2} \bigg) ^ {2} \bigg ] ^ {1 / 2} & s \leq 1 \\ \frac {2}{m m ^ {\prime}} \delta (m - m ^ {\prime}) \mathrm{Re} \bigg [ 1 - \bigg (\frac {m}{2} \bigg) ^ {2} \bigg ] ^ {1 / 2} & s > 1 \end{array} \right. \end{array}\tag{30}
$$

and 

$$
C (m, 0, 0; 0, 0, 0) = \left\{ \begin{array}{l l} \frac {2}{m} \operatorname{Re} \left(s ^ {2} - \frac {m ^ {2}}{4}\right) ^ {1 / 2} & s \leq 1 \\ \frac {2}{m} \operatorname{Re} \left(1 - \frac {m ^ {2}}{4}\right) ^ {1 / 2} & s > 1 \end{array} . \right.\tag{31}
$$

For the case of a small condenser pupil the system can be described in terms of a coherent transfer function, 

$$
C (\mathbf {m}; \mathbf {m} ^ {\prime}) = c (\mathbf {m}) c (\mathbf {m} ^ {\prime})
$$

and 

$$
c (\mathbf {m}) = P _ {2} (- m, - n) \delta [ r + ^ {1 / 2} (m ^ {2} + n ^ {2}) ],\tag{32}
$$

which is shown in Fig. 4. For n = 0 the cutoff frequency in the x direction is m = 1, whereas that in the z direction is r = 1/2. The absolute spatial-frequency cutoffs are thus given by 

$$
\Lambda_ {x} = (\sin \alpha) / \lambda , \quad \Lambda_ {z} = 2 \sin^ {2} (\alpha / 2) / \lambda ,\tag{33}
$$

which are compared as functions of numerical aperture in Fig. 5. As $\alpha \rightarrow \pi/2$ , the spatial-frequency cutoffs in the three dimensions thus approach the same value. 

For a larger condenser pupil the partially coherent transfer function in transmission reduces to 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/f38fa68d7b2a31c7027d36419553a9a65f031590930d49d7456b95a333cfc77b.jpg)

(a)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/bcd010bbb03f5b8ca46c4e359150722c25585edb799516ba83d78b162b40d382.jpg)

(b)

Fig. 4. Coherent transfer function for a transmission system with a small condenser pupil: normalized spatial frequencies.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/3be81a1226a2ef828aff99d94883ea97f428bce02b33a89fe334b649762422ca.jpg)

(a)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/4f09efe22932f4b9724211aa540c7278674b7a239d15a8169520f482308bf2b4.jpg)

(b)

Fig. 5. Coherent transfer function for a transmission system with small condenser pupil: absolute spatial frequencies.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/44df11500ba007e63fc6fb18f5113129cdceb8f770fcc1ea1ca041fa015be03f.jpg)

(a)

(b)

Fig. 6. Transfer function $H(m - m', 0, r - r')$ for a transmission system with a large condenser.

$$
\begin{array}{l} C (m, 0, r; m ^ {\prime}, 0, r ^ {\prime}) \\ = \frac {1}{m m ^ {\prime}} \delta \left[ \frac {r}{m} - \frac {r ^ {\prime}}{m ^ {\prime}} + \frac {1}{2} (m - m ^ {\prime}) \right] \int \int P _ {2} \left[ \xi^ {\prime} - \frac {1}{2} (m - m ^ {\prime}), \eta \right] \\ \times P _ {2} ^ {*} \left[ \xi^ {\prime} + \frac {1}{2} (m - m ^ {\prime}), \eta \right] \delta \left[ \xi^ {\prime} - \left(\frac {r - r ^ {\prime}}{m - m ^ {\prime}}\right) \right] d \xi^ {\prime} d \eta \\ = \frac {1}{m m ^ {\prime}} \delta \left[ \frac {r}{m} - \frac {r ^ {\prime}}{m ^ {\prime}} - \frac {1}{2} (m - m ^ {\prime}) \right] H (m - m ^ {\prime}, 0, r - r ^ {\prime}), \end{array} \tag {34}
$$

with, for a circular objective pupil, 

$$
H (m, 0, r) = \operatorname{Re} \left\{\left[ 1 - \left(\frac {r}{m} + \frac {m}{2}\right) ^ {2} \right] ^ {1 / 2} \right\},\tag{36}
$$

in which Re denotes the real part of its argument. 

The function $H(m,0,r)$ has the same form as the incoherent transfer function described by Frieden and is shown in Fig. 6. Notice, however, the important result that imaging is not purely incoherent because of the condition described by Eq. (27), which ensures that $C(\mathbf{m};\mathbf{m}^{\prime})$ is not a function of only $m-m^{\prime}, n-n^{\prime}$ , and $r-r^{\prime}$ , as can be seen from Eq. (35), in which the delta function expresses the characteristics. 

## 6. WEAK-OBJECT TRANSFER FUNCTION IN TRANSMISSION

Imaging for a finite condenser is partially coherent. We now consider imaging of an object for which the scattered light is weak in intensity compared with the unscattered light. The effective object, comprising both unscattered and scattered radiation, may be expressed as 

$$
t (\mathbf {v} _ {0}) = \delta (u _ {0}) + t _ {1} (\mathbf {v} _ {0}),\tag{37}
$$

in which the modulus of $t_{1}$ is small. Neglecting second-order terms, we obtain 

$$
\begin{array}{r l} I (\mathbf {v}) = \int \int C (0, 0, r; 0, 0, r ^ {\prime}) \mathrm{d} r \mathrm{d} r ^ {\prime} \\ & + \int \int C (\mathbf {m}; 0, 0, r ^ {\prime}) T _ {1} (\mathbf {m}) \exp (j \mathbf {m} \cdot \mathbf {v}) \mathrm{d} \mathbf {m} \mathrm{d} r ^ {\prime} \\ & + \int \int C (0, 0, r; \mathbf {m} ^ {\prime}) T _ {1} ^ {*} (\mathbf {m} ^ {\prime}) \exp (- j \mathbf {m} ^ {\prime} \cdot \mathbf {v}) \mathrm{d} \mathbf {m} ^ {\prime} \mathrm{d} r, \end{array}\tag{38}
$$

which may be written as 

$$
\begin{array}{l} I (\mathbf {v}) = C _ {D} (\mathbf {0}; \mathbf {0}) + \int C _ {W} (\mathbf {m}; \mathbf {0}) T _ {1} (\mathbf {m}) \exp (j \mathbf {m} \cdot \mathbf {v}) \mathrm{d} \mathbf {m} \\ \qquad + \int C _ {W} (\mathbf {0}, \mathbf {m}) T _ {1} ^ {*} (\mathbf {m}) \exp (- j \mathbf {m} ^ {\prime} \cdot \mathbf {v} ^ {\prime}) \mathrm{d} \mathbf {m} ^ {\prime}. \end{array}\tag{39}
$$

However, we know from the condition that the intensity is real: 

$$
C (\mathbf {m}; \mathbf {m} ^ {\prime}) = C ^ {*} (\mathbf {m} ^ {\prime}; \mathbf {m}).\tag{40}
$$

Splitting the object Fourier transform into the Fourier transform of the real part of $t_{1}$ , which represents the absorptive variations, and that of the imaginary part, which represents the phase variation, we obtain 

$$
T _ {1} (\mathbf {m}) = T _ {1 r} (\mathbf {m}) + i T _ {1 i} (\mathbf {m}).\tag{41}
$$

We have that $T_{1r}(\mathbf{m})$ is Hermitian and $iT_{1r}(\mathbf{m})$ is anti-Hermitian, and thus we obtain 

$$
\begin{array}{r l} I (\mathbf {v}) = C _ {D} (\mathbf {0}; \mathbf {0}) + \int \int [ C _ {A} (\mathbf {m}; \mathbf {0}) T _ {1 r} (m) \\ & + C _ {P} (\mathbf {m}; \mathbf {0}) T _ {1 i} (m) ] \exp (j \mathbf {m} \cdot \mathbf {v}) d \mathbf {m} \end{array}\tag{42}
$$

for the image intensity, in which 

$$
\begin{array}{l} C _ {A} (\mathbf {m}; \mathbf {0}) = C _ {W} (\mathbf {m}; \mathbf {0}) + C _ {W} ^ {*} (- \mathbf {m}; \mathbf {0}), \\ C _ {P} (\mathbf {m}; \mathbf {0}) = C _ {W} (\mathbf {m}; \mathbf {0}) - C _ {W} ^ {*} (- \mathbf {m}; \mathbf {0}) \end{array}\tag{43}
$$

are the weak-object transfer functions and are the same as those described by Streibl. $^{4}$ The functions $C_{A}(\mathbf{m};\mathbf{0})$ and $C_{P}(\mathbf{m};\mathbf{0})$ are called the absorptive and the phase transfer functions, respectively. The values of $C_{W}(\mathbf{m};\mathbf{0})$ or $C_{W}(\mathbf{0};\mathbf{m})$ can be calculated from Eq. (23). We obtain 

$$
\begin{array}{r l} C _ {W} (\mathbf {m}; \mathbf {0}) & = \int \int | P _ {1} (\xi , \eta) | ^ {2} (\xi - m, \eta - n) P _ {2} ^ {*} (\xi , \eta) \\ & \quad \times \delta [ r - m \xi - n \eta + ^ {1 / 2} (m ^ {2} + n ^ {2}) ] \mathrm{d} \xi \mathrm{d} \eta \\ & = \frac {2}{\rho} \operatorname{Re} \left\{\left[ \frac {1}{2} (1 + s ^ {2}) - \frac {\rho^ {2}}{4} - \frac {r ^ {2}}{\rho^ {2}} \right. \right. \\ & \quad \left. - \left| r - \frac {1}{2} (1 - s ^ {2}) \right| \right] ^ {1 / 2} \Bigg \}, \end{array}\tag{44}
$$

in which $\rho = (m^{2} + n^{2})^{1/2}, s \leq 1$ , and s is the relative radius of the condenser pupil. The function $C_{W}(\mathbf{m}; \mathbf{0})$ has the same form as that of the weak-object transfer function described by Streibl. The transfer function $C_{W}(\mathbf{m}; \mathbf{0})$ can be shown from Eq. (37) to be bound by the following conditions: 

for $r \leq -1/2(1 - s^2)$ , 

$$
r \geq^ {1} / _ {2} (\rho - 1) ^ {2} - ^ {1} / _ {2},\tag{45a}
$$

$$
r \leq^ {1} / _ {2} (\rho + 1) ^ {2} - ^ {1} / _ {2};\tag{45b}
$$

for $r \geq -1/2(1 - s^2)$ , 

$$
r \geq - \frac {1}{2} (\rho + s) ^ {2} + \frac {s ^ {2}}{2},\tag{45c}
$$

$$
r \leq - \frac {1}{2} (\rho + s) ^ {2} + \frac {s ^ {2}}{2}.\tag{45d}
$$

These conditions represent four parabolas, as shown in Fig. 7. 

For the special case in which $r = 0$ , we have, for $s \leq 1$ , 

$$
C _ {W} (m, n, 0; \mathbf {0}) = \frac {2}{\rho} \operatorname{Re} (s ^ {2} - \rho^ {2} / 4) ^ {1 / 2},\tag{46}
$$

representing the transfer function for thick structures with variations in only the transverse directions. 

From Eqs. (43) and (44), we can see that for s < 1 the phase transfer function $C_{P}(\mathbf{m}; \mathbf{0})$ is not equal to zero, so that a phase object can be imaged. 

For s > 1 the transfer function has the same form as for s = 1 and is independent of s so that only the absorptive part of the object is imaged. 

Also from Eq. (23) we have 

$$
C _ {D} (\mathbf {0}; \mathbf {0}) = \int \int | P _ {1} (\xi , \eta) | ^ {2} | P _ {2} (\xi , \eta) | ^ {2} \mathrm{d} \xi \mathrm{d} \eta ,\tag{47}
$$

which is $\pi$ for values of $s$ greater that unity. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/983702f5cd4b67a06cbd42266579f3d0e07569ecd623b99fe525bd4d766e792d.jpg)

/// c(m;0)≠0

Fig. 7. Cutoff for the transmission weak-object transfer function. Curves (a), (b), (c), and (d) correspond to Eqs. (45a), (45b), (45c), and (45d), respectively. 

## 7. THREE-DIMENSIONAL TRANSFER FUNCTION IN INCIDENT LIGHT

For the incident-light geometry the phase of the illumination is changed so that from Eqs. (2) and (4) we obtain the transfer function 

$$
\begin{array}{l} \mathbf {C} (\mathbf {m}; \mathbf {m} ^ {\prime}) = \int \int | P _ {1} (\xi , \eta) | ^ {2} P _ {2} (\xi - m, \eta - n) \\ \times P _ {2} ^ {*} (\xi - m ^ {\prime}, \eta - n ^ {\prime}) \delta \left[ r + \frac {1}{2 \sin^ {2} (\alpha / 2)} - (\xi^ {2} + \eta^ {2}) \right. \\ \left. + m \xi + n \eta - \frac {\dot {m} ^ {\prime 2} + n ^ {\prime 2}}{2} \right] \delta \left[ r ^ {\prime} + \frac {1}{2 \sin^ {2} (\alpha / 2)} \right. \\ \left. - (\xi^ {2} + \eta^ {2}) + m ^ {\prime} \xi + n ^ {\prime} \eta - \frac {m ^ {\prime 2} + n ^ {\prime 2}}{2} \right] d \xi d \eta , \end{array}\tag{48}
$$

in which the two delta functions represent two rings. When $m' = m$ the two rings coincide, and this case corresponds to that of specular reflection as described in Section 9 below. The signal resulting from this component is strong, but it results not in an image but instead in an unchanging background. When $m' \neq m$ the two rings cross each other, and the signal is weak, but it varies, thereby forming a diffraction image. There are other special cases, which are also discussed in Section 8. 

For the particular case in which $m = m' = n = n' = 0$ , from Eq. (48) we have 

$$
C (0, 0, r; 0, 0, r ^ {\prime}) = \dot {\pi} \delta (r _ {\alpha} - r _ {\alpha} ^ {\prime}),\tag{49}
$$

in which 

$$
r _ {\alpha} = r + \frac {1}{2 \sin^ {2} (\alpha / 2)}\tag{50}
$$

and 

$$
r _ {\alpha} \leq \left\{ \begin{array}{l l} s ^ {2} & \quad s \leq 1 \\ 1 & \quad s > 1 \end{array} . \right.\tag{51}
$$

From Eq. (22) we see that no image is formed from an object consisting only of variations in the axial direction. 

For a small condenser pupil the transfer function is 

$$
C (\mathbf {m}; \mathbf {m} ^ {\prime}) = c (\mathbf {m}) c (\mathbf {m} ^ {\prime}),\tag{52}
$$

and for a circularly symmetrical pupil it is 

$$
c (\mathbf {m}) = P (- m, - n) \delta \left[ r + \frac {1}{2 \sin^ {2} (\alpha / 2)} - \frac {m ^ {2} + n ^ {2}}{2} \right],\tag{53}
$$

which is different from Eq. (32), as is shown in Fig. 8(a). Its passband in the axial direction is 

$$
- \frac {1}{2} \cot^ {2} \frac {\alpha}{2} \geq r \geq - \frac {1}{2 \sin^ {2} (\alpha / 2)}.\tag{54}
$$

We see that the transfer function is offset by an amount dependent on the numerical aperture. For $\alpha\to\pi/2$ , r lies in the range between -1 and -1/2. This offset of the transfer function is analogous to the behavior that takes place in coherent imaging with oblique illumination; that is, imaging of axial structure has a differential contrast component. 

For a large condenser pupil we obtain 

$$
\begin{array}{r l} C (\mathbf {m}; m ^ {\prime}) & = \int \int P _ {2} (\xi - m, \eta - n) P _ {2} ^ {*} (\xi - m ^ {\prime}, \eta - n ^ {\prime}) \\ & \quad \times \delta \bigg [ r + \frac {1}{2 \sin^ {2} (\alpha / 2)} - (\xi^ {2} + \eta^ {2}) \\ & \quad + m \xi + n \eta - \frac {m ^ {\prime 2} + n ^ {2}}{2} \bigg ] \\ & \quad \times \delta \bigg [ r ^ {\prime} + \frac {1}{2 \sin^ {2} (\alpha / 2)} - (\xi^ {2} + \eta^ {2}) \\ & \quad + m ^ {\prime} \xi + n ^ {\prime} \eta - \frac {m ^ {\prime 2} + n ^ {\prime 2}}{2} \bigg ] d \xi d \eta \\ & = \int \int P _ {2} (\xi - m, \eta - n) P _ {2} ^ {*} (\xi - m ^ {\prime}, \eta - n ^ {\prime}) \\ & \quad \times \delta \bigg [ r _ {\alpha} - (\xi^ {2} + \eta^ {2}) + m \xi + n \eta - \frac {m ^ {2} + n ^ {2}}{2} \bigg ] \\ & \quad \times \delta \bigg [ r _ {\alpha} ^ {\prime} - (\xi^ {2} + \eta^ {2}) + m ^ {\prime} \xi + n ^ {\prime} \eta \\ & \quad - \frac {m ^ {\prime 2} + n ^ {\prime 2}}{2} \bigg ] d \xi d \eta . \end{array}\tag{55}
$$

Introducing 

$$
\xi^ {\prime} = \xi - m\tag{56}
$$

and 

$$
\eta^ {\prime} = \eta - n,\tag{57}
$$

we obtain 

$$
\begin{array}{l} C (\mathbf {m}; \mathbf {m}) = \int \int P _ {2} \left(\xi^ {\prime}, \eta\right) P _ {2} ^ {*} \left[ \xi^ {\prime} + \left(m - m ^ {\prime}\right), \eta^ {\prime} + \left(n - n ^ {\prime}\right) \right] \\ \times \delta \left\{r _ {\alpha} - \left[ \left(\xi^ {\prime} + \frac {m}{2}\right) ^ {2} + \left(\eta^ {\prime} + \frac {n}{2}\right) ^ {2} \right] - \frac {m ^ {2} + n ^ {2}}{4} \right\} \\ \times \delta \left[ (r - r ^ {\prime}) + (m - m ^ {\prime}) \xi^ {\prime} + (n - n ^ {\prime}) \eta^ {\prime} \right. \\ + \frac {(m - m ^ {\prime}) ^ {2} + (n - n ^ {\prime}) ^ {2}}{2} ] d \xi^ {\prime} d \eta^ {\prime}. \end{array} \tag {58}
$$

The two delta functions imply that the region of integration is defined by the crossing points between one ring and one straight line, which must be inside the overlapping area of the two pupils. Calculating the integral by the method used by Streibl, $^{4}$ we obtain the transfer function for $n' = n = 0$ : 

$$
\begin{array}{r l} C (m, 0, r; m ^ {\prime}, 0, r ^ {\prime}) & = \frac {1}{| m - m ^ {\prime} |} \operatorname{Re} \left\{\left[ \frac {m r _ {\alpha} - m ^ {\prime} r _ {\alpha} ^ {\prime}}{m - m ^ {\prime}} \right. \right. \\ & \quad \left. \left. - \left(\frac {r - r ^ {\prime}}{m - m ^ {\prime}}\right) ^ {2} - \frac {m ^ {\prime 2} + m ^ {2}}{4} \right] ^ {- 1 / 2} \right\}, \end{array}\tag{59}
$$

in which the conditions 

$$
r _ {\alpha} + \frac {m (r - r ^ {\prime})}{m - m ^ {\prime}} - \frac {m m ^ {\prime}}{2} \leq 1\tag{60}
$$

$$
r _ {\alpha} ^ {\prime} + \frac {m ^ {\prime} (r - r ^ {\prime})}{m - m ^ {\prime}} - \frac {m m ^ {\prime}}{2} \leq 1\tag{61}
$$

are satisfied. Note the important result that the transfer function $C(\mathbf{m}; \mathbf{m}')$ in incident light is also not a function of only $m - m'$ , $n - n'$ , and $r - r'$ . 

## 8. WEAK-OBJECT TRANSFER FUNCTION IN INCIDENT LIGHT

For a finite condenser, as in transmission, imaging is partially coherent. When $(m, n)$ or $(m', n')$ equal zero and r or $r'$ takes the lowest absolute value, then $C(\mathbf{m}; 0, 0, r_{0}')$ or $C(0, 0, r_{0}; \mathbf{m}')$ can be calculated from Eq. (48). Putting $m' = n' = 0$ , we obtain 

$$
\begin{array}{l} C (m, n, r; 0, 0, r ^ {\prime}) = \int \int | P _ {1} (\xi , \eta) | ^ {2} P _ {2} (\xi - m, \eta - n) P _ {2} ^ {*} (\xi , \eta) \\ \times \delta \left[ r ^ {\prime} + \frac {1}{2 \sin^ {2} (\alpha / 2)} - \left(\xi^ {2} + \eta^ {2}\right) \right] \\ \times \delta \left[ r + \frac {1}{2 \sin^ {2} (\alpha / 2)} - \left(\xi^ {2} + \eta^ {2}\right) \right. \\ \left. + m \xi + n \eta - \frac {m ^ {2} + n ^ {2}}{2} \right] d \xi d \eta . \end{array} \tag {62}
$$

and 

Because the maximum of $(\xi^2 + \eta^2)$ is $1/2(1 + s^2 - |s^2 - 1|)$ , $r'$ (or $r$ ) lies within the following range: 

$$
- \frac {1}{2 \sin^ {2} (\alpha / 2)} \leq r ^ {\prime} \leq - \frac {1}{2 \sin^ {2} (\alpha / 2)} + \frac {1}{2} (1 + s ^ {2} - | s ^ {2} - 1 |),\tag{63}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/f2425110d96eb271d4bfe37e42fbd3a7b7128a5b4f0a7a6d0073f740036476f1.jpg)

a) $S = 0$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/c82c6dd10164aad1f1b895d3381aed977b34f1021cc18745a55493ba97ec94d2.jpg)

b) S=0.5

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-05/51d80b03-370c-47f1-92d1-483939cbf971/51f35fb7d7cfff12a340817febe26eee1789b2652586e114f3922d19f9cfb643.jpg)

c) S=1

Fig. 8. Transfer function $C(m, n, r; 0, 0, r_{0})$ for an incident-light system.

which means that $r'$ cannot be equal to zero, so there is no first-order image in the axial direction, and thus an object with only zero frequency in the axial direction, such as that described by Eq. (15), cannot be imaged for $s \leq 1$ . The lowest value of $r'$ (for $m' = n' = 0$ ) is given by 

$$
r ^ {\prime} = r _ {0} ^ {\prime} = - \frac {1}{2 \sin^ {2} (\alpha / 2)} + \frac {1}{2} (1 + s ^ {2} - | s ^ {2} - 1 |).\tag{64}
$$

In many objects the spectrum decreases with spatial frequency, and for some classes of object we may assume that the dominant contribution is thus from $r' = r_{0}$ . From Eq. (62) we then obtain the transfer function, 

$$
\begin{array}{r l} C (m, n, r; 0, 0, [ s b: r: 0 ] ^ {\prime}) & = \frac {1}{\rho} \operatorname{Re} \left\{\left[ \frac {1}{2} (1 + s ^ {2}) - \frac {\rho^ {2}}{4} - \frac {r _ {\beta} ^ {2}}{\rho^ {2}} - \left| r _ {\beta} - \frac {1}{2} (1 - s ^ {2}) \right| \right] ^ {1 / 2} \right\}, \\ & r _ {\beta} \leq \frac {1 - s ^ {2}}{2}, \end{array} \tag {65}
$$

for which $r_{\beta} = r - r_0'$ and $s \leq 1$ . The value of $C(m, n, r; 0, 0, r_0')$ for $s > 1$ is the same as that for $s = 1$ . The region in which $C(m, n, r; 0, 0, r_0)$ has the value shown in Fig. 8. 

We must emphasize the importance of the case in which $r_{\beta} = -\frac{1}{2}\rho[\rho - \sqrt{2}(1 + s^{2})]$ . In this case the transfer function tends to infinity, and the corresponding signal can form a diffraction image. This corresponds to the touching of the two rings represented by the two delta functions in Eq. (62). In the other cases, except that in which m = n = 0, the signal can form a diffraction image, but the image is relatively weak. 

Consider now the imaging of an object in which the dominant contribution is from $r = r_{0}$ . Neglecting higher-order terms in $(m, n)$ or $(m', n')$ , we obtain the intensity of the image: 

$$
\begin{array}{r l} I (\mathbf {v}) & = \int \int \int C (m, n, r; 0, 0, r _ {0} ^ {\prime}) T (\mathbf {m}) \\ & \quad \times T ^ {*} (0, 0, r _ {0} ^ {\prime}) \exp [ j (m v + n w + r _ {\beta} u ] \mathrm{d} \mathbf {m} \\ & \quad + \int \int \int C (0, 0, r _ {0} ^ {\prime}; m ^ {\prime}, n ^ {\prime}, r ^ {\prime}) T (0, 0, r _ {0} ^ {\prime}) \\ & \quad \times T ^ {*} (\mathbf {m}) e - j (m ^ {\prime} v + n ^ {\prime} w + r _ {\beta} ^ {\prime} (u) \mathrm{d} \mathbf {m} ^ {\prime}. \end{array}\tag{66}
$$

Using the condition that the intensity be real and splitting T into the real and imaginary parts $T_{r}(m)$ and $T_{i}(m)$ , we obtain 

$$
\begin{array}{r l} I (\mathbf {v}) = & \int \int \int C _ {A} (m, n, r; 0, 0, r _ {0} ^ {\prime}) [ T _ {r} (\mathbf {m}) T _ {i} (0, 0, r _ {0} ^ {\prime}) \\ & + T _ {r} (0, 0, r _ {0} ^ {\prime}) T _ {i} (m) ] \exp [ - j (m v + n w + r _ {\beta} u) \mathrm{d} \mathbf {m} \\ & + \int \int \int C _ {P} (m, n, r; 0, 0, r _ {0} ^ {\prime}) [ T _ {i} (m) T _ {r} (0, 0, r _ {0} ^ {\prime}) \\ & + T _ {i} (0, 0, r _ {0} ^ {\prime}) T _ {r} (\mathbf {m}) ] \exp [ - j (m v + n w + r _ {\beta} u) ] \mathrm{d} \mathbf {m}, \end{array}\tag{67}
$$

in which 

$$
\begin{array}{r l} C _ {A} (m, n, r; 0, 0, r _ {0} ^ {\prime}) & = C (m, n, r; 0, 0, r _ {0} ^ {\prime}) \\ & + C ^ {*} (- m, - n, - r; 0, 0, - r _ {0} ^ {\prime}) \end{array}\tag{68}
$$

and 

$$
\begin{array}{r l} C _ {P} (m, n, r; 0, 0, r _ {0} ^ {\prime}) = C (m, n, r; 0, 0, r _ {0} ^ {\prime}) & \\ - C ^ {*} (- m, - n, - r; 0, 0, - r _ {0} ^ {\prime}). \end{array}\tag{69}
$$

From Eq. (67) we can see that in incident light there is no first-order image in t, only a second-order image. In addition the real part and the imaginary part of the object can no longer be imaged separately through the incident-light system. 

## 9. IMAGING OF SLOPING PLANES

Consider an object that consists of a sloping scattering plane; for example, the transmission object 

$$
t (v, w, u) = \delta (v + \gamma u),\tag{70}
$$

for which the Fourier transform is 

$$
T (m, n, r) = \delta (n) \delta (r - m \gamma).\tag{71}
$$

From Eq. (22) the image of the sloping plane is 

$$
\begin{array}{r l} I (\mathbf {v}) = \int \int C (m, 0, m \gamma^ {\prime}; m ^ {\prime}, 0, m ^ {\prime} \gamma) \\ & \times \exp [ j (m - m ^ {\prime}) (\nu + \gamma u) ] \mathrm{d} m \mathrm{d} m ^ {\prime} \end{array}\tag{72}
$$

Substituting Eq. (23) for the transfer function, we obtain 

$$
I (\mathbf {v}) = \int \int \frac {| P _ {1} (\xi , \eta) | ^ {2} | P _ {2} (2 \gamma - \xi , \eta) | ^ {2}}{4 (\gamma - \xi) ^ {2}} \mathrm{d} \xi \mathrm{d} \eta ,\tag{73}
$$

which is a function of $\gamma$ only. Thus the signal depends on the angle of slope of the plane. It is a maximum when the plane includes the optic axis, and it becomes zero when the plane is at such an angle that the scattered rays do not pass through the objective pupil. 

For an incident-light system, however, for a nonzero transfer function, r is necessarily large, so that $\gamma$ is correspondingly large. When integrating over r in Eq. (22) we can therefore assume that m is approximately constant and given by a value 

$$
m _ {0} \simeq - \frac {1}{2 \gamma \sin^ {2} (\alpha / 2)}.\tag{74}
$$

Thus the image of the sloping plane is now given by 

$$
I (\mathbf {v}) = \int \int C (m _ {0}, 0, r; m _ {0} ^ {\prime}, 0, r ^ {\prime}) \exp [ j (r - r ^ {\prime}) u ] \mathrm{d} r \mathrm{d} r ^ {\prime}.\tag{75}
$$

Substituting in for the transfer function from Eq.(48) and integrating in r and $r'$ , we find that 

$$
I (\mathbf {v}) = \int \int | P _ {1} (\xi , \eta) | ^ {2} | P _ {2} (\xi - m _ {0}, \eta) | ^ {2} \mathrm{d} \xi \mathrm{d} \eta .\tag{76}
$$

Again, the signal is independent of position, but this time it reaches a maximum when the plane is perpendicular to the axis. Again, it becomes zero when the scattered rays do not pass through the objective pupil. In both the transmission and the incident-light cases, the only contributions come from the transfer function $C(\mathbf{m}; \mathbf{m})$ , which represents specular reflection. 

## 10. THREE-DIMENSIONAL PUPILS AND TRANSFER FUNCTIONS

The transfer functions can be expressed in a simple form by introducing three-dimensional pupils representing the objective and condenser lenses: 

$$
\pi_ {2} (\pmb {\xi}) = \int h _ {2} (\mathbf {v}) \mathrm{exp} (- j \pmb {\xi} \cdot \mathbf {v}) \mathrm{d} \pmb {\xi},\tag{77}
$$

$$
\pi_ {1} (\boldsymbol {\xi}) = \int g (\mathbf {v}) \exp (- j \boldsymbol {\xi} \cdot \mathbf {v}) d \boldsymbol {\xi}.\tag{78}
$$

We have from Eqs. (2) and (4) 

$$
\pi_ {1} (\xi) = | P _ {1} (\xi , \eta) | ^ {2} \delta \left[ \zeta - \frac {1}{4 \sin^ {2} (\alpha / 2)} + \frac {1}{2} \left(\xi^ {2} + \eta^ {2}\right) \right],\tag{79}
$$

$$
\pi_ {2} (\dot {\xi}) = P _ {2} (\xi , \eta) \delta \Bigg [ \zeta - \frac {1}{4 \sin^ {2} (\alpha / 2)} + \frac {1}{2} (\xi^ {2} + \eta^ {2}) \Bigg ],\tag{80}
$$

and the partially coherent transfer function may be written as 

$$
C (\mathbf {m}; \mathbf {m} ^ {\prime}) = \int \pi_ {1} (\xi) \pi_ {2} (\xi + m) \pi_ {2} ^ {*} (\xi + m ^ {\prime}) \mathrm{d} \xi .\tag{81}
$$

For an incident-light system, $\pi_1(\xi)$ is the same as Eq. (79), but $\pi_2(\xi)$ has the form 

$$
\pi_ {2} (\xi) = P _ {2} (\xi , \eta) \delta \Bigg [ \xi + \frac {1}{4 \sin^ {2} (\alpha / 2)} - \frac {1}{2} (\xi^ {2} + \eta^ {2}) \Bigg ],\tag{82}
$$

and the partially coherent transfer function is still given by Eq. (81). 

In this way the pupil functions and the partially coherent transfer functions have a symmetrical form over three-dimensional coordinates. 

We can now identify the imaging process in terms of the well-known Ewald sphere construction, but, in the paraxial approximation considered here, these spheres are approximated to paraboloids. In the transmission case the three intersecting paraboloids of Eq. (81) are oriented in the same direction. The surfaces $\pi_{1}$ and $\pi_{2}$ intersect in a parabola, and so too do the surfaces $\pi_{1}$ and $\pi_{2}^{*}$ . For the integral of Eq. (81) to be nonzero, these two parabolas must coincide, which corresponds to conditions described by Eqs. (24) and (27) being satisfied. Equation (24) means that the vectors m and $m'$ must be in a plane containing the axis, whereas Eq. (27) requires that m and $m'$ be chords of a parabola with one same endpoint. It is interesting to note that, without the paraxial approximation, the spheres $\pi_{1}$ and $\pi_{2}$ and the spheres $\pi_{1}$ and $\pi_{2}^{*}$ intersect in circles, and these circles can touch but cannot exactly coincide unless $m = m'$ . In this way the results obtained without the paraxial approximation may be quite different from those obtained with it. 

Turning now to the incident-light geometry, the paraboloids $\pi_{1}$ and $\pi_{2}$ (and $\pi_{2}^{*}$ ) face in opposition directions. The paraboloids intersect in ellipses whose projections in the direction of the axis are circles. These circles can coincide, touch, or cross, as discussed in Sections 7 and 8. 

## 11. DISCUSSION

We have derived the three-dimensional partially coherent transfer functions for microscopes, assuming critical illumination and using the paraxial approximation. As for the two-dimensional functions, we would expect the results to be the same for the Köhler illumination system. Both transmission and incident-light systems have been considered, the latter behaving as a dark-field system for axial variations. Neither system can image objects that have no transverse detail. 

The first Born approximation is used here, but the discussion in Section 10 indicated this assumption must be reexamined. The imaging of the partially coherent system was separated into a transfer function, which is a property of only the optical system, and an object spectrum, which is independent of the system. The scattering function for the object is a function of four variables (two direction cosines each for illumination and detection). Provided that an object spectrum, which is a function of three variables, can be derived from the scattering function, the transfer functions derived here are valid also for strongly scattering objects; the effects of multiple scattering affect only the effective object spectrum. This is possible, for example, for an object with variations only in one direction or for a two-dimensional system. 

We can determine the scattering function by methods that are appropriate for the particular form of object, for example, using coupled-wave or coupled-mode theories, neglecting second derivatives or higher-order beams, as may be permissible. $^{8}$ We must exercise some care in applying the first Born approximation. For example, for a dielectric surface a multiple-scattering theory is necessary for prediction of the correct Fresnel coefficients. Reflections from boundaries can also be incorporated directly. 

Finally, we should point out that the three-dimensional approach takes into account the effects of the varying thickness of an object with different angles of illumination. 

The transfer functions presented in this paper are quite complicated, particularly for the incident-light geometry. In a forthcoming paper, in which we consider confocal systems, we shall show that these functions behave in a much simpler manner, as a result of the coherence of these systems. 

## REFERENCES

1. C. W. McCutchen, "Generalized aperture and the three-dimensional diffraction image," J. Opt. Soc. Am. 54, 240-244 (1964). 

2. E. Wolf, "Three-dimensional structure determination of semi-transparent objects from holographic data," Opt. Commun. 1, 153-156 (1969). 

3. B. R. Frieden, "Optical transfer of a three-dimensional object," J. Opt. Soc. Am. 57, 56-66 (1967). 

4. N. Streibl, "Three-dimensional imaging in a microscope," J. Opt. Soc. Am. A 2, 121-127 (1985). 

5. C. J. R. Sheppard, "The spatial frequency cut-off in three-dimensional imaging," Optik 72, 131-133 (1986). 

6. C. J. R. Sheppard, "The spatial frequency cut-off in three-dimensional imaging, II," Optik 74, 128-129 (1986). 

7. C. J. R. Sheppard and H. Matthews, "Imaging in high-aperture optical systems," J. Opt. Soc. Am. A 4, 1354-1360 (1987). 

8. T. K. Gaylord and M. G. Moharam, "Planar dielectric grating diffraction theories," Appl. Phys. B 28, 1-4 (1982). 
