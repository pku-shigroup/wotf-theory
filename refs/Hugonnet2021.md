# Optimizing illumination in three-dimensional deconvolution microscopy for accurate refractive index tomography

HERVE HUGONNET,<sup>1,2</sup> MOOSUNG LEE,<sup>1,2</sup> AND YONGKEUN PARK<sup>1,2,3,\*</sup>

<sup>1</sup>Department of Physics, Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Republic of Korea

<sup>2</sup>KAIST Institute for Health Science and Technology, KAIST, Daejeon, Republic of Korea <sup>3</sup>Tomocube Inc., Daejeon, Republic of Korea <sup>\*</sup>yk.park@kaist.ac.kr

Abstract: In light transmission microscopy, axial scanning does not directly provide tomographic reconstruction of specimen. Phase deconvolution microscopy can convert a raw intensity image stack into a refractive index tomogram, the intrinsic sample contrast which can be exploited for quantitative morphological analysis. However, this technique is limited by reconstruction artifacts due to unoptimized optical conditions, which leads to a sparse and non-uniform optical transfer function. Here, we propose an optimization method based on simulated annealing to systematically obtain optimal illumination schemes that enable artifact-free deconvolution. The proposed method showed precise tomographic reconstruction of unlabeled biological samples.

© 2021 Optical Society of America under the terms of the OSA Open Access Publishing Agreement

## 1. Introduction

Light transmission microscopy has been an indispensable imaging tool for visualizing threedimensional (3D) structures of microscopic samples [1]. Because most microscopic specimens such as biological cells are translucent, a major challenge in light microscopy has been to improve image contrast. A key idea has been to encode the intensity with the phase variations of the light due to the sample’s inhomogeneous refractive index (RI) distribution [2,3]. Phase contrast microscopy [4], dark-field microscopy, and diferential interference contrast microscopy [5] are widely used methods to achieve this goal by modulating incoherently transmitted light. However, with these methods, it is dificult to directly relate the intensity contrast with the sample RI in a quantitative manner. Since RI can provide essential information about the protein concentrations [6] and lipid compositions [7] in biological cells as well as specific chemical information about soft matter particles, direct 3D RI imaging is highly desirable.

3D RI imaging, or optical difraction tomography (ODT), can be categorized into two classes. The first is conventional ODT that is implemented by illuminating the sample with coherent plane waves at various incidence angles, retrieving the complex light field transmitted through the sample, and reconstructing a sample RI map using the Fourier difraction theorem [8]. Although the reconstruction accuracy of ODT has been drastically improved using the multiple scattering models [9–13], the use of coherent light and interferometry makes the setup susceptible to the fundamental coherent and mechanical noise. Methods using only the intensity of light transmitted at various angle through the sample have also been developed [14–16] but require a computationally costly iterative reconstruction scheme and often introduce reconstruction artifacts. The second is ODT based on 3D incoherent imaging that does not rely on a coherent source or interferometry, but can retrieve the RI distribution by modulating a Köhler illumination intensity in the pupil plane and deconvolving the raw image stack by the corresponding point spread function (PSF) [17]. This phase deconvolution microscopy can be easily combined with other complementary imaging modalities [18]; moreover, it is mechanically more stable and less sensitive to speckle noise.

A major challenge of 3D phase deconvolution microscopy is to mitigate inaccurate RI quantification and reconstruction artifacts after deconvolution. Both problems mostly arise from the use of unoptimized PSFs for 3D imaging. If the modulation of the pupil plane intensity is not optimal, the resultant PSF may not sample the spatial frequencies of the sample in an isotropic manner. Moreover, unoptimized pupil apodizations can be sensitive to misalignment errors, which may induce reconstruction artifacts due to optical setup imperfections. Several previous studies have reported the importance of finding an optimal illumination scheme in phase deconvolution microscopy [19,20], but they were limited to two dimensions. Previous studies employed various illumination schemes, such as uniform illumination up to a certain numerical aperture (partially coherent (PC) ODT) [17], illumination using half of the pupil aperture in four directions (diferential phase contrast (DPC) ODT) [21], ring [22] and Gaussian-shaped [23] illumination, to achieve 3D phase deconvolution microscopy; however, the complexity of the 3D imaging problem has not yet led to the discovery of optimal illumination schemes for 3D RI imaging.

Here, we propose plural eficient patterns for self-interfering ODT (PEPSI-ODT) and optimized illumination patterns for robust 3D phase deconvolution microscopy. Using the simulated annealing algorithm [24], we optimized the pupil plane illumination intensity, resulting in a homogeneous sampling of the 3D RI spatial frequencies. We compared the reconstruction performance of PEPSI-ODT with other ODT methods. The results showed that our method provides RI images of colloidal microspheres and HEK293T cells with minimal artifacts and is in good agreement with conventional coherent ODT.

## 2. Deconvolution phase microscopy

## 2.1. Principle

PEPSI-ODT is a type of phase deconvolution microscopy, in which the sample is illuminated by Kohler illumination with various optimized apodizations while being axially scanned (Fig. 1(a)). The pupil intensity distribution can be controlled by a spatial light modulator or a light emitting device (LED) array in the Fourier plane [21]. Focal scanning can be implemented by axially moving the sample [21], objective lens, or using remote focusing schemes [25,26]. The raw image stacks of the light transmitted through the sample exhibit diferent intensity distributions depending upon the pupil apodizations and the sample RI (Fig. 1(b)). Phase deconvolution microscopy enables recovery of the intrinsic RI contrast of the sample by deconvolving the raw data with theoretically estimated PSFs (Fig. 1(c)).

The theory of phase deconvolution microscopy is based on the linearization of light scattering. Earlier theory relied upon the Born approximation [17] but could not accurately explain the experimental reconstruction accuracy, since RI reconstructed under the Born approximation typically shows underestimation and morphological artifacts in most biological samples [27]. To better explain the RI reconstruction accuracy, we used the Rytov approximation [28], a later scattering model based on the slowly varying phase assumption.

Starting from the elastic light scattering theory based on the Rytov approximation, the field $E _ { o u t }$ transmitted through a sample illuminated by a plane wave, $E _ { i n } = e x p [ \mathrm { i } \ \mathbf { k _ { i n } } { \cdot } \mathbf { r } ]$ , is $U ^ { s } = E _ { i n } \cdot l n ( E _ { o u t } / E _ { i n } )$ . From the Taylor expansion of the relative transmitted intensity $I _ { o u t } / I _ { i n } =$ $| E _ { o u t } / E _ { i n } | ^ { 2 } = e x p ( 2 { \cdot } \mathrm { R e } [ U ^ { s } / E _ { i n } ] )$ , the light intensity transmitted through sample $I _ { o u t }$ is

$$
I _ {o u t} = I _ {i n} [ 1 + 2 \cdot R e (U ^ {s} / E _ {i n}) ] + O [ R e (U ^ {s} / E _ {i n}) ^ {2} ],\tag{1}
$$

![](images/10a8887de1eff52b16c05aa7bfce619f3cf837170c08a5de58905f3fbed4c45a.jpg)  
Fig. 1. Principle of the proposed technique: (a) The illumination apodization is changed while a sample is axially scanned. (b) Intensity transmitted through the sample is measured for diferent apodization. (c) Reconstructed RI tomogram after deconvolution.

in which the high-order terms can be omitted for slowly varying RI samples [28]. We aim to relate the transmitted intensity to the sample RI using the Fourier difraction theorem [29]

$$
\widetilde {F} (\mathbf {k} - \mathbf {k _ {i n}}) \delta (k _ {z} - \sqrt {k ^ {2} - k _ {x} ^ {2} - k _ {y} ^ {2}}) = - i k _ {z} \widetilde {U} ^ {s} (\mathbf {k})\tag{2}
$$

where $\mathbf { k } = ( k _ { x } , \ k _ { y } , \ k _ { z } ) , \ | \mathbf { k _ { i n } } | = k = 2 \pi n _ { m } / \lambda$ (wave number); $n _ { m }$ is the medium RI; $F ( x , y , z ) =$ $\begin{array} { r } { \frac { 1 } { 4 \pi } k ^ { 2 } ( n ^ { 2 } ( x , y , z ) / \bar { n } _ { m } ^ { 2 } - 1 ) } \end{array}$ is the scattering potential; n is the 3D RI map, and tilde denotes the 3D <sup>π</sup>Fourier transform. The Dirac delta function indicates that the scattered field is projected onto the Ewald sphere. If we define $S = I _ { o u t } / I _ { i n } - 1$ , its Fourier transform is expressed using Eqs. (1) and (2) as

$$
\begin{array}{r} \widetilde {S} (\mathbf {k}) = \frac {i}{k _ {z} + k _ {i , z}} \widetilde {F} (\mathbf {k}) \delta \left(k _ {z} + k _ {i, z} - \sqrt {k ^ {2} - k _ {x} ^ {\prime 2} - k _ {y} ^ {\prime 2}}\right) \\ - \frac {i}{k _ {z} - k _ {i , z}} \widetilde {F} ^ {*} (- \mathbf {k}) \delta \left(k _ {z} - k _ {i, z} + \sqrt {k ^ {2} - k _ {x} ^ {\prime 2} - k _ {y} ^ {\prime 2}}\right), \end{array}\tag{3}
$$

where $\mathbf { k } ^ { ' } = \mathbf { k } + \mathbf { k } _ { \mathbf { i n } }$ . The scattering potential can be split into its real and imaginary parts, $F = F _ { r e a l } + i F _ { i m a g } ,$ , with $F _ { r e a l }$ and $F _ { i m a g }$ being real and imaginary parts, respectively. Exploiting $\widetilde f ( \mathbf { k } ) = [ \widetilde f ( - \mathbf { k } ) ] ^ { * }$ for real-valued $f ( x )$ , we obtain

$$
\widetilde {S} (\mathbf {k}) = \widetilde {F} _ {i m a g} (\mathbf {k}) \widetilde {H} _ {A} (\mathbf {k}; \mathbf {k} _ {\mathbf {i} n}) + \widetilde {F} _ {r e a l} (\mathbf {k}) \widetilde {H} _ {P} (\mathbf {k}; \mathbf {k} _ {\mathbf {i} n}),\tag{4}
$$

where the amplitude and phase transfer functions, $\overline { { H } } _ { A } ( \mathbf { k } )$ and $\overline { { H } } _ { P } ( \mathbf { k } )$ , respectively, are defined a

$$
\left\{ \begin{array}{l} \widetilde {H} _ {A} (\mathbf {k}; \mathbf {k} _ {\mathbf {i} n}) = - \frac {1}{k _ {z} + k _ {i , z}} \delta \left(k _ {z} + k _ {i, z} - \sqrt {k ^ {2} - k _ {x} ^ {\prime 2} - k _ {y} ^ {\prime 2}}\right) - \frac {1}{k _ {z} - k _ {i , z}} \delta \left(k _ {z} - k _ {i, z} + \sqrt {k ^ {2} - k _ {x} ^ {\prime 2} - k _ {y} ^ {\prime 2}}\right) \\ \widetilde {H} _ {P} (\mathbf {k}; \mathbf {k} _ {\mathbf {i} n}) = \frac {i}{k _ {z} + k _ {i , z}} \delta \left(k _ {z} + k _ {i, z} - \sqrt {k ^ {2} - k _ {x} ^ {\prime 2} - k _ {y} ^ {\prime 2}}\right) - \frac {i}{k _ {z} - k _ {i , z}} \delta \left(k _ {z} - k _ {i, z} + \sqrt {k ^ {2} - k _ {x} ^ {\prime 2} - k _ {y} ^ {\prime 2}}\right) \end{array} \right.\tag{5}
$$

The shapes of $\overline { { H } } _ { A } ( \mathbf { k } )$ and $\overline { { H } } _ { P } ( \mathbf { k } )$ )indicate the odd and even properties along the $k _ { z }$ axis, respectively. The form of Eq. (4) still holds true when Kohler illumination is used because the transmitted intensity for diferent angled illumination sums up incoherently. I $\dot { \bar { \rho } } ( k _ { i , x } , k _ { i , y } )$ is the normalized illumination intensity at the pupil plane, the transfer functions are expressed as [17]

$$
\left\{ \begin{array}{l l} \widetilde {H} _ {A} (\mathbf {k}) = \int \rho (k _ {i, x}, k _ {i, y}) \widetilde {H} _ {A} (\mathbf {k}; \mathbf {k} _ {\mathbf {i} n}) d k _ {i, x} d k _ {i, y} \\ \widetilde {H} _ {P} (\mathbf {k}) = \int \rho (k _ {i, x}, k _ {i, y}) \widetilde {H} _ {P} (\mathbf {k}; \mathbf {k} _ {\mathbf {i} n}) d k _ {i, x} d k _ {i, y} \end{array} \right..\tag{6}
$$

To reconstruct the complex RI values, at least two measurements with diferent pupil apodizations are needed. The RI reconstruction for multiple incoherent illuminations can then be expressed as solving the linear problem at each spatial frequency

$$
\mathbf {y} = \left( \begin{array}{c} \widetilde {S} _ {1} \\ \widetilde {S} _ {2} \\ \dots \end{array} \right) = \left[ \begin{array}{c c} \widetilde {H} _ {A 1} & \widetilde {H} _ {P 1} \\ \widetilde {H} _ {A 2} & \widetilde {H} _ {P 2} \\ \dots & \dots \end{array} \right] \binom{\widetilde {F} _ {i m a g}}{\widetilde {F} _ {r e a l}} = \mathbf {A} x.\tag{7}
$$

The pseudoinverse of the matrix then leads to deconvolution and RI reconstructions. To avoid excessive noise during the deconvolution, we used a Tikhonov regularization with cost function $| \mathbf { A } x - \mathbf { y } | _ { 2 } ^ { 2 } + \alpha | \mathbf { x } | _ { 2 } ^ { 2 }$ , where is the regularization parameter. Its analytic solution that minimizes the cost function is $\mathbf { x } = ( \mathbf { A } \mathbf { A } ^ { T } + \alpha \mathbf { I } ) ^ { - 1 } \mathbf { A } ^ { T } \mathbf { y } [ 3 0 ]$ . It should be noted that when the immersion medium did not match the mounting medium refractive index, we rescaled the axial magnification of the raw data before deconvolution [31].

## 2.2. Optimization process

We maximized the deconvolution performance by maximizing the signal-to-noise ratio within the sampling range of deconvolution (Fig. 2). In particular, we assumed that a raw image stack exhibits a uniform Gaussian white noise owing to shot noise [32,33] and computed the noise standard deviation within the bandwidth of the transfer functions. Since we are mainly interested in RI reconstructions, we only focused on improving the signal-to-noise ratios of the phase transfer functions. To do so, we first define the optical transfer function (OTF) density (OTFD) as the inverse of the noise standard deviation amplification occurring during the reconstruction process without regularization at a given spatial frequency.

$$
\mathrm{OTFD} (\mathbf {k}) = \left(\sum_ {j = 1} ^ {N} (\widetilde {H} _ {j P} ^ {- 1}) (\mathbf {k}) ^ {2}\right) ^ {- \frac {1}{2}},\tag{8}
$$

where $N$ is the number of diferent illuminations (Fig. 2(a)). In PEPSI-ODT, the illumination is set to minimize the following cost function (Fig. 2(b)):

$$
c = \frac {\sum_ {\mathbf {k}} | \nabla_ {\mathbf {k}} \mathrm{OTFD} (\mathbf {k}) |}{\left(\sum_ {\mathbf {k}} | \mathrm{OTFD} (\mathbf {k}) |\right) ^ {1 + \beta}}.\tag{9}
$$

The parameter $\beta$ is used to give more importance to signal strength and can be adjusted to <sup>β</sup>balance the signal strength and spatial frequency coverage. If $\beta$ is close to zero, the cost function favors uniformity over signal strength. We used a value of 0.1 for $\beta ,$ which is a good compromise between the signal strength and OTFD uniformity.

Because minimizing the cost function is a non-convex problem, we carried out the optimization using the simulated annealing algorithm [24] (Fig. 2(c)). The illumination pupil intensity was expressed using a linear sum of Zernike polynomials. We limited the used orders to the sixth to avoid rapid change in the pattern intensity, which could decrease the pattern’s susceptibility to misalignment. Additionally, increasing the order did not significantly improve the optimization result (Fig. S2).

![](images/3147d30ca6885e6edff96b6d0aaaeac8c168649065ff339428da36aae04e8ba9.jpg)  
Fig. 2. Optimization process. (a) The optical transfer function density is computed, (b) then the cost function is computed. (c) The pattern is semi randomly accepted using the cost function diference and the acceptance function $F _ { i } ( x )$ . Then a new pattern is created by random perturbation of the last accepted pattern.

The optimization process using simulated annealing consists of random perturbations of the patterns at each step and keeping the newly created patterns with a random probability depending on the change in the cost function. Specifically, we defined the acceptance function $F _ { i } ( \mathbf { x } )$ at the i-th iteration. Its value is true if $a ^ { - x / b ^ { \prime } }$ exceeds a random value ranging from 0 to 1, where a and b were set to 1.22 and 1.0017, respectively. The exponential decay was slowly reduced until a suitable pattern was found.

![](images/cba2fc4595c60849ad5d15f691eac89227370abdd6c3ba4e7b61f8b1867d0419.jpg)  
Fig. 3. Principle of data acquisition, illumination design and refractive index reconstruction. (a) Optical setup. BS: beam-splitter; L: lens; M: mirror; SLM: spatial light modulator; OB: objective lens (b) Intensity displayed on the SLM. (c) Optical transfer function and (d) optical transfer function density.

The optimization can be carried out for diferent numbers of illuminations and reconstruction configurations. In general, at least three diferent apodizations are required to enable uniform coverage of all spatial frequencies; however, using more illuminations greatly increases the signal-to-noise ratio. Indeed, using more apodizations enables each illumination to reduce its support in the pupil plane, which reduces overlapping of the positive and negative terms from Eq. (5) when computing the phase transfer function. The number of required apodizations can be reduced when imaging objects with purely real RIs. However, this assumption can lead to reconstruction artifacts when imaging biological samples [26].

In the experiments, we used four apodizations to retrieve the complex RI because this configuration provides the best strength and uniformity. The optimized patterns, OTF and OTFD for this configuration are shown in Figs. 3(b)–(d). Optimizations for other configurations are shown in Figs. S1 (a)–(b). In addition, the uniformity and strength of the OTFD for each configuration and previous DPC- and PC-ODT illumination schemes are quantified using the mean and coeficient of variation of the OTFD. PEPSI-ODT has a significantly more uniform coverage compared with previous methods at a similar signal strength. The repetition of the optimization procedure with diferent random seeds provided similar results except for pattern rotation, suggesting the successful convergence to the optimal solutions (Fig. S2).

## 3. Results

## 3.1. Experimental setup

A schematic of the incoherent imaging system is shown in Fig. 2(a). The illumination part was composed of Köhler illumination implemented using an LED (M470L2, Thorlabs) followed by a spatial light modulator (X10468-01, Hamamatsu) which modulated the intensity in the pupil plane. The light transmitted through the sample using two objective lenses (LUMFLN60XW NA=1.1, Olympus) was then refocused using a remote focusing scheme composed of an objective lens (UPLSAPO60XW NA=1.2, Olympus) and a mirror mounted on a piezo stage (LPS710E/M, Thorlabs) and projected on the camera (LT425M-WOCG, Lumenera Inc.). Remote focusing enables fast aberration-free acquisition of focus stacks without disrupting the sample [25]. To compare diferent ODT modalities, the setup was integrated with a coherent ODT imaging modality using beam splitters. The coherent ODT setup and reconstruction process are described in [34].

## 3.2. Experiment

To evaluate the imaging performance of PEPSI-ODT, we compared it with diferent illumination schemes in deconvolution phase microscopy and coherent ODT (Fig. 4(a)). For comparison purposes, we selected two of the most used illumination schemes: DPC ODT and PC-ODT. While PEPSI-ODT uses four optimized pupil intensity patterns, DPC-ODT uses four half circles in the four cardinal directions [21]. Phase deconvolution microscopy using a single low-pass-filtered pupil is also possible using PC-ODT [17], but it requires prior information about the sample and sacrifices the spatial resolution. It should be noted that, unlike phase deconvolution microscopy, coherent ODT does not modulate the pupil intensity but records the transmitted complex field under illumination at diferent angles of incidence.

First, we compared the OTFD of the diferent imaging modalities (Fig. 4(b)). An ideal ground truth was set to a uniform distribution within the theoretical bandwidth range. The OTFD of coherent ODT sparsely filled the bandwidth range; thus, sparse angular scanning may have underestimated the sample RI. However, the PEPSI-ODT smoothly filled the bandwidth range owing to Kohler illumination. Moreover, the OTFD of PEPSI-ODT exhibited a significantly more uniform distribution compared with the DPC- and PC-ODT methods. These comparisons indicated the success of OTFD optimization in our method.

![](images/bafeab169cfb66420b5c78177f5bd6bb7b9e3c9a6608e32f0d448e1f4362ce03.jpg)  
Fig. 4. Comparison of PEPSI-ODT with DPC-ODT, PC-ODT and coherent ODT under the Rytov approximation in (a) bead and (b) HEK293T cells. (c) OTF density for deconvolution phase microscopy and the support for the ground truth and coherent ODT. (d) Pupil apodization for each method.

Secondly, we compared the reconstruction performance of the diferent methods using a reference sample (Fig. 4(c)). We imaged and reconstructed a 3D RI tomogram of a 10-µmdiameter polystyrene microsphere suspended in an index-matching oil (Cargille, series A, nominal RI = 1.57). A ground truth was established by numerically convolving a 10-µm-diameter polystyrene microsphere with an ideal transfer function. Coherent ODT with 373 angular projections provided an RI tomogram in close agreement with the ground truth. Importantly, PEPSI-ODT with four diferent illuminations also provided a similar reconstruction result, albeit with axial shrinkage artifact due to the high RI of the sample medium [31] and slight underestimation. Notably, the reconstruction artifacts were minimal compared with DPC-ODT and PC-ODT, which exhibited directional fringes and axial rings, respectively. The significant diference in the reconstruction performance reminds of the importance of using optimal illumination in phase deconvolution microscopy.

Finally, we applied the proposed method to 3D RI live-cell imaging (Fig. 4(d)). We imaged an aggregate of four HEK293T cells using the diferent ODT imaging schemes. Because the imaged cells contained microscopic sub-organelles inside their bodies, successful deconvolution over a high spatial frequency range was important. The reconstructed results showed the high fidelity of PEPSI-ODT, which was consistent with coherent ODT. On the other hand, the anisotropic OTFDs of DPC- and PC-ODT caused severe reconstruction errors, suggesting that optimal illumination schemes are important for phase deconvolution microscopy in biological applications.

## 4. Conclusions

We proposed a new method to choose the illumination scheme in deconvolution phase microscopy. PEPSI-ODT removes reconstruction artifacts by enabling uniform sampling of all spatial frequencies. Our method is flexible and can obtain an optimal illumination scheme depending on several criteria: signal strength, spatial frequency coverage, and sensitivity to misalignment.

We compared the reconstruction results to other illumination schemes as well as coherent optical difraction tomography. PEPSI-ODT achieved imaging results that are comparable to coherent optical difraction tomography with a simpler optical setup while avoiding imaging artifacts present in other deconvolution phase microscopy schemes. Therefore, our method can be considered as a more practical alternative to conventional ODT.

Although we have used a SLM to generate designated illumination patterns for this study, the proposed approach can also be implemented with alternative pattern generation methods, including a LED array, a digital micromirror device, or a rotation of patterned filters [35,36].

The reconstruction performance of the proposed method can be further improved by several technical improvements. For example, halo artifacts and lower axial resolution are inherent limitations in 3D transmission microscopy. These can be numerically mitigated by novel denoising and deblurring algorithms based on non-negativity constraints, total variation (Fig. S3) [37], or Hessian minimization [38]. Furthermore, the optimal choice of hardware can boost the imaging speed to an order of a few volumes per second.

The simplicity of the optical setup combined with the focal stack image acquisition scheme makes this method particularly attractive for combination with fluorescence imaging systems. In addition, the use of incoherent light reduces speckle noise, which might be useful when imaging thick specimens [34].

Funding. Tomocube; KAIST (Up program); National Research Foundation of Korea (2015R1A3A2066550, 2017M3C1A3013923, 2018K000396).

Disclosures. M.L and Y.P. have financial interests in Tomocube Inc., a company that commercializes optical difraction tomography and quantitative phase-imaging instruments, and is one of the sponsors of the work.

## References

1. D. J. Stephens and V. J. Allan, “Light microscopy techniques for live cell imaging,” Science 300(5616), 82–86 (2003).

2. Y. Park, C. Depeursinge, and G. Popescu, “Quantitative phase imaging in biomedicine,” Nat. Photonics 12(10), 578–589 (2018).

3. D. Kim, S. Lee, M. Lee, J. Oh, S.-A. Yang, and Y. Park, “Refractive index as an intrinsic imaging contrast for 3-D label-free live cell imaging,” BioRxiv, 106328 (2017).

4. F. Zernike, “How I Discovered Phase Contrast,” Science 121(3141), 345–349 (1955).

5. S. F. Hughes, “Interference microscope,” (1948/08/03/ 1948)

6. R. Barer, K. F. Ross, and S. Tkaczyk, “Refractometry of living cells,” Nature 171(4356), 720–724 (1953).

7. K. Kim, S. Lee, J. Yoon, J. Heo, C. Choi, and Y. Park, “Three-dimensional label-free imaging and quantification of lipid droplets in live hepatocytes,” Sci. Rep. 6(1), 36815 (2016).

8. E. Wolf, “Three-dimensional structure determination of semi-transparent objects from holographic data,” Opt. Commun. 1(4), 153–156 (1969).

9. M. Chen, D. Ren, H.-Y. Liu, S. Chowdhury, and L. Waller, “Multi-layer Born multiple-scattering model for 3D phase microscopy,” Optica 7(5), 394–403 (2020).

10. H. Liu, D. Liu, H. Mansour, P. T. Boufounos, L. Waller, and U. S. Kamilov, “SEAGLE: Sparsity-Driven Image Reconstruction Under Multiple Scattering,” IEEE Trans. Comput. Imaging 4(1), 73–86 (2018).

11. S. Fan, S. Smith-Dryden, J. Zhao, S. Gausmann, A. Schülzgen, G. Li, and B. E. A. Saleh, “Optical Fiber Refractive Index Profiling by Iterative Optical Difraction Tomography,” J. Lightwave Technol. 36(24), 5754–5763 (2018).

12. J. Lim, A. B. Ayoub, E. E. Antoine, and D. Psaltis, “High-fidelity optical difraction tomography of multiple scattering samples,” Light: Sci. Appl. 8(1), 82 (2019).

13. T. Pham, E. Soubies, A. Ayoub, J. Lim, D. Psaltis, and M. Unser, “Three-Dimensional Optical Difraction Tomography With Lippmann-Schwinger Model,” IEEE Trans. Comput. Imaging 6, 727–738 (2020).

14. R. Horstmeyer, J. Chung, X. Ou, G. Zheng, and C. Yang, “Difraction tomography with Fourier ptychography,” Optica 3(8), 827–835 (2016).

15. S. Chowdhury, M. Chen, R. Eckert, D. Ren, F. Wu, N. Repina, and L. Waller, “High-resolution 3D refractive index microscopy of multiple-scattering samples from intensity images,” Optica 6(9), 1211–1219 (2019).

16. C. Zuo, J. Sun, J. Li, A. Asundi, and Q. Chen, “Wide-field high-resolution 3D microscopy with Fourier ptychographic difraction tomography,” Opt. Lasers Eng. 128, 106003 (2020).

17. N. Streibl, “Three-dimensional imaging by a microscope,” J. Opt. Soc. Am. A 2(2), 121 (1985).

18. A. Descloux, K. S. Grußmayer, E. Bostan, T. Lukes, A. Bouwens, A. Sharipov, S. Geissbuehler, A. L. Mahul-Mellier, H. A. Lashuel, M. Leutenegger, and T. Lasser, “Combined multi-plane phase retrieval and super-resolution optical fluctuation imaging for 4D cell microscopy,” Nat. Photonics 12(3), 165–172 (2018).

19. Y. Fan, J. Sun, Q. Chen, X. Pan, L. Tian, and C. Zuo, “Optimal illumination scheme for isotropic quantitative diferential phase contrast microscopy,” Photonics Res. 7(8), 890–904 (2019).

20. H.-H. Chen, Y.-Z. Lin, and Y. Luo, “Isotropic diferential phase contrast microscopy for quantitative phase bio-imaging,” J. Biophotonics 11(8), e201700364 (2018).

21. M. Chen, L. Tian, and L. Waller, “3D diferential phase contrast microscopy,” Biomed. Opt. Express 7(10), 3940–3950 (2016).

22. J. Li, Q. Chen, J. Sun, J. Zhang, J. Ding, and C. Zuo, “Three-dimensional tomographic microscopy technique with multi-frequency combination with partially coherent illuminations,” Biomed. Opt. Express 9(6), 2526–2542 (2018).

23. J. A. Rodrigo, J. M. Soto, and T. Alieva, “Fast label-free optical difraction tomography compatible with conventional wide-field microscopes,” in Optical Methods for Inspection, Characterization, and Imaging of Biomaterials IV, (International Society for Optics and Photonics, 2019), 1106016.

24. S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, “Optimization by Simulated Annealing,” Science 220(4598), 671–680 (1983).

25. E. J. Botcherby, M. J. Booth, R. Juškaitis, and T. Wilson, “Real-time extended depth of field microscopy,” Opt. Express 16(26), 21843–21848 (2008).

26. J. M. Soto, J. A. Rodrigo, and T. Alieva, “Label-free quantitative 3D tomographic imaging for partially coherent light microscopy,” Opt. Express 25(14), 15699 (2017).

27. K. Kim, J. Yoon, S. Shin, S. Lee, S.-A. Yang, and Y. Park, “Optical difraction tomography techniques for the study of cell pathophysiology,” JBPE, 020201-020201-020201-020216 (2016).

28. M. H. Jenkins and T. K. Gaylord, “Three-dimensional quantitative phase imaging via tomographic deconvolution phase microscopy,” Appl. Opt. 54(31), 9213–9227 (2015).

29. M. Born and E. Wolf, Principles of Optics: Electromagnetic Theory of Propagation, Interference and Difraction of Light, 7 ed. (Cambridge University Press, Cambridge, 1999).

30. M. Foster, “An Application of the Wiener-Kolmogorov Smoothing Theory to Matrix Inversion,” J. Soc. Ind. Appl. Math. 9(3), 387–392 (1961).

31. T. H. Besseling, J. Jose, and A. V. Blaaderen, “Methods to calibrate and scale axial distances in confocal microscopy as a function of refractive index,” J. Microsc. 257(2), 142–150 (2015).

32. A. Papoulis, “High density shot noise and gaussianity,” J. Appl. Probability 8(1), 118–127 (1971).

33. V. Z. Marmarelis, “Appendix II: Gaussian White Noise,” Nonlinear Dynamic Modeling of Physiological Systems, 499–501 (2004).

34. H. Hugonnet, Y. W. Kim, M. Lee, S. Shin, R. H. Hruban, S.-M. Hong, and Y. Park, “Multiscale label-free volumetric holographic histopathology of thick-tissue slides with subcellular resolution,” bioRxiv, 2020.2007.2015.205633 (2020).

35. L. Tian, J. Wang, and L. Waller, “3D diferential phase-contrast microscopy with computational illumination using an LED array,” Opt. Lett. 39(5), 1326–1329 (2014).

36. S. Shin, K. Kim, J. Yoon, and Y. Park, “Active illumination using a digital micromirror device for quantitative phase imaging,” Opt. Lett. 40(22), 5407–5410 (2015).

37. A. Beck and M. Teboulle, “Fast Gradient-Based Algorithms for Constrained Total Variation Image Denoising and Deblurring Problems,” IEEE Trans. on Image Process. 18(11), 2419–2434 (2009).

38. S. Lefkimmiatis, J. P. Ward, and M. Unser, “Hessian Schatten-Norm Regularization for Linear Inverse Problems,” IEEE Trans. on Image Process. 22(5), 1873–1888 (2013).