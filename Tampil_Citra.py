import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "gambar.jpg"
img = cv2.imread(path)

if img is None:
    print("Gambar tidak ditemukan!")
    exit()


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(gray, cmap='gray')
plt.title("Citra Grayscale")
plt.axis("off")

plt.show()


M, N = gray.shape
print("Resolusi Spasial (M x N):", M, "x", N)


L_teoritis = 256
unique_levels = np.unique(gray)
L_real = len(unique_levels)

print("Tingkat Keabuan Teoritis (8-bit):", L_teoritis)
print("Jumlah tingkat keabuan yang digunakan:", L_real)
