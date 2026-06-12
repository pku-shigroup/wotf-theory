#!/usr/bin/env python3
"""
Visualize the two Ewald caps from the PGT theory derivation (pgt_theory.tex).

The intensity-spectrum cross term  Ĩ_{i-s}  decomposes into two spherical
caps in k-space, each a delta-shell on the Ewald sphere:

  Cap 1 (→ -k_inc):  upper hemisphere,  shifted by -k_inc,  carries  F̃(k)
  Cap 2 (z-rev):      lower hemisphere,  shifted by +k_inc,  carries  F̃*(-k)

Run with the ic-pgt-algorithm venv:
    /home/zhangkai/phd/ic-pgt/ic-pgt-algorithm/.venv/bin/python visualize_caps.py
"""

# Hello from sshfs
import numpy as np
import matplotlib.pyplot as plt

# ── Physical parameters (normalised) ───────────────────────────────────────
km = 1.0                             # wavenumber in medium  k_m = 2π n_m / λ
theta_inc = np.deg2rad(25)           # incident angle from the z-axis

# Incident wave vector: |k_inc| = km
k_inc = np.array([0.0, 0.0, km])     # axial incidence (simplest case)
# For oblique incidence, uncomment:
# k_inc = np.array([km * np.sin(theta_inc), 0.0, km * np.cos(theta_inc)])

assert np.allclose(np.linalg.norm(k_inc), km), "|k_inc| must equal km"


# ── Geometry helpers ───────────────────────────────────────────────────────
def upper_hemi(km, n=80):
    """Upper Ewald hemisphere  k_z = +√(km² - k_x² - k_y²)."""
    phi = np.linspace(0, 2 * np.pi, n)
    r = np.linspace(0, km, n)
    phi, r = np.meshgrid(phi, r)
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    z = np.sqrt(np.maximum(km**2 - x**2 - y**2, 0))
    return x, y, z


def lower_hemi(km, n=80):
    """Lower Ewald hemisphere  k_z = -√(km² - k_x² - k_y²)."""
    x, y, z = upper_hemi(km, n)
    return x, y, -z


def shift_surf(x, y, z, vec):
    """Translate surface by vector vec."""
    return x + vec[0], y + vec[1], z + vec[2]


# ── Generate all surfaces ──────────────────────────────────────────────────
xu, yu, zu = upper_hemi(km)           # upper hemi (origin-centred)
xl, yl, zl = lower_hemi(km)           # lower hemi

# Cap 1: upper hemi shifted by  −k_inc
x1, y1, z1 = shift_surf(xu, yu, zu, -k_inc)

# Cap 2: lower hemi shifted by  +k_inc   (the "z-reversed" cap)
x2, y2, z2 = shift_surf(xl, yl, zl, +k_inc)

# Ewald-sphere wireframe (for reference)
phi_w, theta_w = np.meshgrid(
    np.linspace(0, 2 * np.pi, 80),
    np.linspace(0, np.pi, 40),
)
x_ew = km * np.sin(theta_w) * np.cos(phi_w)
y_ew = km * np.sin(theta_w) * np.sin(phi_w)
z_ew = km * np.cos(theta_w)


# ═══════════════════════════════════════════════════════════════════════════
# Figure 1 – 3D overview
# ═══════════════════════════════════════════════════════════════════════════
fig1 = plt.figure(figsize=(14, 6))

# — left: 3D —
ax3d = fig1.add_subplot(1, 2, 1, projection='3d')
ax3d.plot_wireframe(x_ew, y_ew, z_ew, color='gray', alpha=0.12,
                    linewidth=0.3)
ax3d.plot_surface(x1, y1, z1, color='#e74c3c', alpha=0.65, edgecolor='none')
ax3d.plot_surface(x2, y2, z2, color='#3498db', alpha=0.65, edgecolor='none')
ax3d.quiver(0, 0, 0, k_inc[0], k_inc[1], k_inc[2],
            color='green', linewidth=3, arrow_length_ratio=0.15)
ax3d.scatter([0], [0], [0], c='k', s=30)
ax3d.set(xlabel=r'$k_x$', ylabel=r'$k_y$', zlabel=r'$k_z$',
         xlim=(-1.6*km, 1.6*km), ylim=(-1.6*km, 1.6*km), zlim=(-1.6*km, 1.6*km))
ax3d.set_box_aspect((1, 1, 1))
ax3d.set_title('3D view')
ax3d.legend([
    plt.Line2D([0],[0], color='#e74c3c', lw=6, alpha=0.7),
    plt.Line2D([0],[0], color='#3498db', lw=6, alpha=0.7),
    plt.Line2D([0],[0], color='green', lw=2),
], [r'Cap 1 $\to -k_{\rm inc}$', r'Cap 2 (z-rev) $\to +k_{\rm inc}$',
    r'$k_{\rm inc}$'], loc='upper left', fontsize=8)

# — right: 2D cross-section at k_y = 0 —
ax2d = fig1.add_subplot(1, 2, 2)
k_rho = np.linspace(-1.8 * km, 1.8 * km, 600)

# Ewald sphere cross-section
m_ew = np.abs(k_rho) <= km
ax2d.plot(k_rho[m_ew],  np.sqrt(km**2 - k_rho[m_ew]**2),  'gray', lw=0.7, alpha=0.5)
ax2d.plot(k_rho[m_ew], -np.sqrt(km**2 - k_rho[m_ew]**2),  'gray', lw=0.7, alpha=0.5)

# Cap 1: k_z = -k_inc_z + √(km² - (k_ρ + k_inc_x)²)
m1 = np.abs(k_rho + k_inc[0]) <= km
kz1 = np.full_like(k_rho, np.nan)
kz1[m1] = -k_inc[2] + np.sqrt(km**2 - (k_rho[m1] + k_inc[0])**2)
ax2d.plot(k_rho, kz1, '#e74c3c', lw=2)

# Cap 2: k_z = +k_inc_z - √(km² - (k_ρ - k_inc_x)²)
m2 = np.abs(k_rho - k_inc[0]) <= km
kz2 = np.full_like(k_rho, np.nan)
kz2[m2] = k_inc[2] - np.sqrt(km**2 - (k_rho[m2] - k_inc[0])**2)
ax2d.plot(k_rho, kz2, '#3498db', lw=2)

# Annotations
ax2d.annotate(r'$k_{\rm inc}$', xy=(k_inc[0], k_inc[2]),
              xytext=(k_inc[0]+0.15, k_inc[2]+0.15),
              arrowprops=dict(arrowstyle='->', color='green', lw=1.5),
              fontsize=10, color='green')
ax2d.scatter([0], [0], c='k', s=25, zorder=5)
ax2d.axhline(0, color='k', lw=0.5); ax2d.axvline(0, color='k', lw=0.5)
ax2d.set(xlabel=r'$k_\rho = \sqrt{k_x^2+k_y^2}$  (or $k_x$ at $k_y=0$)',
         ylabel=r'$k_z$', xlim=(-1.6*km, 1.6*km), ylim=(-1.6*km, 1.6*km),
         title=r'$(k_\rho, k_z)$ slice')
ax2d.set_aspect('equal'); ax2d.grid(alpha=0.3)
ax2d.legend([r'Cap 1 $[-k_{\rm inc}]$: $+\widetilde{F}(\mathbf{k})$',
             r'Cap 2 (z-rev) $[+k_{\rm inc}]$: $-\widetilde{F}^*(-\mathbf{k})$'],
            fontsize=7.5, loc='lower right')

fig1.tight_layout()
fig1.savefig('/home/zhangkai/phd/ic-pgt/pgt-theory/ewald_caps_overview.png',
             dpi=150, bbox_inches='tight')
print('[1/3] ewald_caps_overview.png'):

# ═══════════════════════════════════════════════════════════════════════════
# Figure 2 – Decomposed step-by-step
# ═══════════════════════════════════════════════════════════════════════════
fig2, axes = plt.subplots(1, 3, figsize=(15, 4.8))

for ax in axes:
    # Ewald reference
    ax.plot(k_rho[m_ew],  np.sqrt(km**2 - k_rho[m_ew]**2),  'gray', lw=0.6, alpha=0.4)
    ax.plot(k_rho[m_ew], -np.sqrt(km**2 - k_rho[m_ew]**2),  'gray', lw=0.6, alpha=0.4)
    ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
    ax.set(xlabel=r'$k_\rho$', xlim=(-1.5*km, 1.5*km), ylim=(-1.5*km, 1.5*km))
    ax.set_aspect('equal'); ax.grid(alpha=0.25)

# — panel 0: Ewald sphere —
axes[0].fill_between(k_rho[m_ew], 0, np.sqrt(km**2 - k_rho[m_ew]**2),
                     alpha=0.12, color='gray')
axes[0].plot(k_rho[m_ew], np.sqrt(km**2 - k_rho[m_ew]**2), 'k', lw=1.8)
axes[0].set_title('Ewald sphere  $|k|=k_m$')
axes[0].set_ylabel(r'$k_z$')

# — panel 1: Cap 1 —
axes[1].fill_between(k_rho, -1.5*km, kz1, alpha=0.12, color='#e74c3c')
axes[1].plot(k_rho, kz1, '#e74c3c', lw=2)
axes[1].annotate(r'$-k_{\rm inc}$', xy=(-k_inc[0], -k_inc[2]),
                 fontsize=9, color='#c0392b',
                 xytext=(-k_inc[0]-0.3, -k_inc[2]+0.1),
                 arrowprops=dict(arrowstyle='->', color='#c0392b'))
axes[1].set_title(r'Cap 1: upper hemi $\to -k_{\rm inc}$  [$+\widetilde{F}$]')

# — panel 2: Cap 2 —
axes[2].fill_between(k_rho, kz2, 1.5*km, alpha=0.12, color='#3498db')
axes[2].plot(k_rho, kz2, '#3498db', lw=2)
axes[2].annotate(r'$+k_{\rm inc}$', xy=(k_inc[0], k_inc[2]),
                 fontsize=9, color='#2980b9',
                 xytext=(k_inc[0]+0.12, k_inc[2]+0.3),
                 arrowprops=dict(arrowstyle='->', color='#2980b9'))
axes[2].set_title(r'Cap 2: lower hemi $\to +k_{\rm inc}$  [$-\widetilde{F}^*$]')

fig2.tight_layout()
fig2.savefig('/home/zhangkai/phd/ic-pgt/pgt-theory/ewald_caps_decomposed.png',
             dpi=150, bbox_inches='tight')
print('[2/3] ewald_caps_decomposed.png')


# ═══════════════════════════════════════════════════════════════════════════
# Figure 3 – 3D oblique incidence (richer geometry)
# ═══════════════════════════════════════════════════════════════════════════
k_inc_obl = np.array([km * np.sin(theta_inc), 0.0, km * np.cos(theta_inc)])
x1o, y1o, z1o = shift_surf(xu, yu, zu, -k_inc_obl)
x2o, y2o, z2o = shift_surf(xl, yl, zl, +k_inc_obl)

fig3 = plt.figure(figsize=(10, 8))
ax3 = fig3.add_subplot(1, 1, 1, projection='3d')
ax3.plot_wireframe(x_ew, y_ew, z_ew, color='gray', alpha=0.10, linewidth=0.3)
ax3.plot_surface(x1o, y1o, z1o, color='#e74c3c', alpha=0.55, edgecolor='none')
ax3.plot_surface(x2o, y2o, z2o, color='#3498db', alpha=0.55, edgecolor='none')
ax3.quiver(0, 0, 0, k_inc_obl[0], k_inc_obl[1], k_inc_obl[2],
           color='green', linewidth=3, arrow_length_ratio=0.12)
# drop-shadows on the k_x-k_y plane
for cx, cy, cz, cc in [(x1o, y1o, z1o, '#e74c3c'), (x2o, y2o, z2o, '#3498db')]:
    ax3.plot_surface(cx, cy, np.full_like(cz, -1.6*km),
                     color=cc, alpha=0.1, edgecolor='none')
ax3.scatter([0], [0], [0], c='k', s=25)
ax3.set(xlabel=r'$k_x$', ylabel=r'$k_y$', zlabel=r'$k_z$',
        xlim=(-1.6*km, 1.6*km), ylim=(-1.6*km, 1.6*km), zlim=(-1.6*km, 1.6*km),
        title=fr'Oblique incidence  $\theta={np.rad2deg(theta_inc):.0f}^\circ$')
ax3.set_box_aspect((1, 1, 1))

fig3.tight_layout()
fig3.savefig('/home/zhangkai/phd/ic-pgt/pgt-theory/ewald_caps_oblique.png',
             dpi=150, bbox_inches='tight')
print('[3/3] ewald_caps_oblique.png')
print('\nDone — 3 figures saved to pgt-theory/')
