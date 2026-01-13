# %%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# %%
# Parameters
gamma = 42.58e3  # Gyromagnetic ratio for proton (Hz/T)
B0 = 1.5  # Static magnetic field strength (Tesla)
M0 = 1.0  # Initial magnetization magnitude

# Time parameters
dt = 1e-6  # Time step (seconds)
T = 0.1  # Total simulation time (seconds)
t = np.arange(0, T, dt)
N = len(t)

# Initial magnetization vector (after a 90-degree pulse, it's in the transverse plane)
M = np.zeros((N, 3))
M[0, :] = [
    M0,
    0,
    0,
]  # Assume 90 degree pulse puts M on the x-axis for simplicity

# Larmor frequency (angular)
omega0 = 2 * np.pi * gamma * B0  # rad/s

# Bloch equation simulation (simplified, no relaxation)
for i in range(N - 1):
    Mx, My, Mz = M[i, :]
    # dM/dt = gamma * M x B0 (where B0 = [0, 0, B0])
    dMx_dt = omega0 * My
    dMy_dt = -omega0 * Mx
    dMz_dt = 0  # Mz is constant in free precession without relaxation

    # Update magnetization using Euler method
    M[i + 1, 0] = Mx + dMx_dt * dt
    M[i + 1, 1] = My + dMy_dt * dt
    M[i + 1, 2] = Mz + dMz_dt * dt

# Visualization
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# Plot the precession path
ax.plot(M[:, 0], M[:, 1], M[:, 2], label="Precession Path", color="blue")
ax.scatter(
    M[0, 0],
    M[0, 1],
    M[0, 2],
    color="green",
    s=50,
    label="Start (After 90° pulse)",
)
ax.scatter(M[-1, 0], M[-1, 1], M[-1, 2], color="red", s=50, label="End")

# Set plot limits and labels
ax.set_xlim([-M0 * 1.1, M0 * 1.1])
ax.set_ylim([-M0 * 1.1, M0 * 1.1])
ax.set_zlim([-M0 * 1.1, M0 * 1.1])
ax.set_xlabel("Mx")
ax.set_ylabel("My")
ax.set_zlabel("Mz (B0 direction)")
ax.set_title("Proton Precession Simulation (Idealized)")
ax.legend()
ax.grid(True)
plt.show()
