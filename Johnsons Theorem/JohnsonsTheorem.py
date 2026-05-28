import numpy as np
import matplotlib.pyplot as plt

def get_circumcircle(p1, p2, p3):
    d = 2 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
    ux = ((p1[0]**2 + p1[1]**2) * (p2[1] - p3[1]) + (p2[0]**2 + p2[1]**2) * (p3[1] - p1[1]) + (p3[0]**2 + p3[1]**2) * (p1[1] - p2[1])) / d
    uy = ((p1[0]**2 + p1[1]**2) * (p3[0] - p2[0]) + (p2[0]**2 + p2[1]**2) * (p1[0] - p3[0]) + (p3[0]**2 + p3[1]**2) * (p2[0] - p1[0])) / d
    center = np.array([ux, uy])
    radius = np.linalg.norm(center - p1)
    return center, radius

R = 10.0
H = np.array([0.0, 0.0])

base_angle = np.pi / 2 
theta = np.array([base_angle, base_angle + 2*np.pi/3, base_angle + 4*np.pi/3])

O1 = np.array([R * np.cos(theta[0]), R * np.sin(theta[0])])
O2 = np.array([R * np.cos(theta[1]), R * np.sin(theta[1])])
O3 = np.array([R * np.cos(theta[2]), R * np.sin(theta[2])])

A = O1 + O2
B = O2 + O3
C = O1 + O3

O4, R4 = get_circumcircle(A, B, C)

fig, ax = plt.subplots(figsize=(10, 10))

fig.canvas.manager.set_window_title("Johnson's Theorem")

ax.add_patch(plt.Circle(O1, R, color='blue', fill=False, linewidth=1.5, label='C1'))
ax.add_patch(plt.Circle(O2, R, color='green', fill=False, linewidth=1.5, label='C2'))
ax.add_patch(plt.Circle(O3, R, color='red', fill=False, linewidth=1.5, label='C3'))
ax.add_patch(plt.Circle(O4, R4, color='purple', fill=False, linewidth=2, linestyle='--', label='C4 (Circumcircle)'))

ax.plot(*H, 'ko', markersize=8, label='H (Common Point)')
ax.plot(*A, 'co', markersize=6, label='A (Intersection 1-2)')
ax.plot(*B, 'mo', markersize=6, label='B (Intersection 2-3)')
ax.plot(*C, 'yo', markersize=6, label='C (Intersection 1-3)')
ax.plot(*O4, 'x', color='purple', markersize=8, label='O4 (Center of C4)')

ax.set_aspect('equal')
ax.set_xlim(-4*R, 4*R)
ax.set_ylim(-4*R, 4*R)
ax.legend(loc='upper right')
ax.grid(True, linestyle=':', alpha=0.7)

plt.title(f"Johnson's Theorem Verification\nInitial Radius = {R:.4f} | C4 Radius = {R4:.4f}")

plt.subplots_adjust(bottom=0.08)
plt.figtext(0.5, 0.02, "Johnson's Theorem - IG: WAACLIB", ha="center", fontsize=12, fontweight='bold', color='black')

plt.savefig("johnsons_theorem_output.png", dpi=300, bbox_inches='tight')

plt.show()

print(f"R_initial : {R}")
print(f"R_johnson : {R4}")
print(f"Delta     : {abs(R - R4):.2e}")