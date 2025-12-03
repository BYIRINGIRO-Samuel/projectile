import numpy as np
import matplotlib.pyplot as plt

v0 = 25.0
t_total = 3.0
x_target = 45.0
g = 9.8

cos_alpha = x_target / (v0 * t_total)
alpha = np.arccos(cos_alpha)

v0x = v0 * np.cos(alpha)
v0y = v0 * np.sin(alpha)

t = np.linspace(0, t_total, 300)

x = v0x * t
y = v0y * t - 0.5 * g * t**2

plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion of Water Stream")
plt.grid(True)
plt.show()
