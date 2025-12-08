import numpy as np
import matplotlib.pyplot as plt
import random
N = 100000
x, y = 0, 0
x_list, y_list = [], []
print("Lütfen bekleyin.")

for i in range(N):
    r = random.random()
    if r < 0.01:
        x, y =  0, 0.16 * y
    elif r < 0.86:
        x_new = 0.85 * x + 0.04 * y
        y_new = -0.04 * x + 0.85 * y + 1.6
        x, y = x_new, y_new
    elif r < 0.93:
        x_new = 0.2 * x - 0.26 * y
        y_new = 0.23 * x + 0.22 * y + 1.6
        x, y = x_new, y_new
    else:
        x_new = -0.15 * x + 0.28 * y
        y_new = 0.26 * x + 0.24 * y + 0.44
        x, y = x_new, y_new
        
    x_list.append(x)
    y_list.append(y)
fig = plt.figure(figsize=(10, 14), facecolor='black')
ax = fig.add_axes([0.05, 0.2, 0.9, 0.75])
ax.set_facecolor('black')
ax.scatter(x_list, y_list, s=0.2, c='#2ecc71', marker='.')

ax.axis('off')
plt.figtext(0.5, 0.14, "BARNSLEY FERN - IG:WAACLIB", 
            ha="center", color="white", fontsize=20, fontname="Arial", fontweight="bold")

plt.figtext(0.5, 0.09, r"$x_{n+1} = a x_n + b y_n + e$", 
            ha="center", color="#dddddd", fontsize=16)
print("Eğrelti otu oluşturuldu. Görsel açılıyor...")
plt.savefig("Barnsley_Fern_Poster.png", dpi=300, facecolor='black')
plt.show()