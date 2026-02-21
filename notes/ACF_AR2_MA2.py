import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def acf_ar2(beta1, beta2, k_max=20):
    roots = np.roots([1, -beta1, -beta2])
    r1, r2 = roots[0], roots[1]
    rho1 = beta1 / (1 - beta2)
    A = (rho1 - r2) / (r1 - r2)
    B = 1 - A
    ks = np.arange(k_max + 1)
    rho = A * (r1 ** ks) + B * (r2 ** ks)
    return ks, rho.real

def acf_ma2(phi1, phi2, k_max=20):
    den = 1 + phi1**2 + phi2**2
    rho0 = 1
    rho1 = (phi1 + phi1 * phi2) / den
    rho2 = phi2 / den
    ks = np.arange(k_max + 1)
    rho = np.zeros_like(ks, dtype=float)
    rho[0] = rho0
    rho[1] = rho1
    rho[2] = rho2
    return ks, rho

ar_params = [
    (0.5, 0.3),
    (-0.5, 0.3),
    (0.7, -0.4),
    (-0.6, -0.5)
]

ma_params = [
    (0.5, 0.4),
    (-0.6, 0.3),
    (0.8, -0.5),
    (-0.7, -0.6)
]

with PdfPages("ACF_AR2_MA2.pdf") as pdf:

    fig1, axes = plt.subplots(2, 2, figsize=(10, 8), dpi=300)
    fig1.suptitle("ACF for AR(2) with Different (β₁, β₂) Values", fontsize=14)
    fig1.subplots_adjust(hspace=0.5, wspace=0.4, left=0.1, right=0.95, top=0.9, bottom=0.1)

    for ax, (b1, b2) in zip(axes.flatten(), ar_params):
        ks, rho = acf_ar2(b1, b2)
        ax.plot(ks, rho, marker='o')
        ax.axhline(0, color='black', linewidth=1)
        ax.set_title(f"β₁ = {b1},  β₂ = {b2}", fontsize=11)
        ax.set_xlabel("Lag k")
        ax.set_ylabel("ρ(k)")
        ax.grid(True)


    margin = 0.08

    fig1.add_artist(plt.Line2D([margin, 1-margin], [0.5, 0.5], transform=fig1.transFigure, color='red', linewidth=2))
    fig1.add_artist(plt.Line2D([0.5, 0.5], [margin, 1-margin], transform=fig1.transFigure, color='red', linewidth=2))


    pdf.savefig(fig1)
    plt.close(fig1)

    fig2, axes = plt.subplots(2, 2, figsize=(10, 8), dpi=300)
    fig2.suptitle("ACF for MA(2) with Different (Φ₁, Φ₂) Values", fontsize=14)
    fig2.subplots_adjust(hspace=0.5, wspace=0.4, left=0.1, right=0.95, top=0.9, bottom=0.1)

    for ax, (p1, p2) in zip(axes.flatten(), ma_params):
        ks, rho = acf_ma2(p1, p2)
        ax.stem(ks, rho, basefmt="black")
        ax.set_title(f"Φ₁ = {p1},  Φ₂ = {p2}", fontsize=11)
        ax.set_xlabel("Lag k")
        ax.set_ylabel("ρ(k)")
        ax.grid(True)

    fig2.add_artist(plt.Line2D([margin, 1-margin], [0.5, 0.5], transform=fig2.transFigure, color='red'))
    fig2.add_artist(plt.Line2D([0.5, 0.5], [margin, 1-margin], transform=fig2.transFigure, color='red'))

    pdf.savefig(fig2)
    plt.close(fig2)

print("PDF saved as ACF_AR2_MA2.pdf")
