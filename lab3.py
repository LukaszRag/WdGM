from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

#ZAD 1
im1 = Image.open('obraz.jpg')
print("tryb", im1.mode)
print("format", im1.format)
print("rozmiar", im1.size)
h, w = im1.size
im1


#ZAD 2A
T = np.array(im1)
print("typ danych tablicy obrazu: ", T.dtype)
print("rozmiar elementu tablicy obrazu: ", T.itemsize)
print("rozmiar tablicy obrazu: ", T.shape)
#tablica kanału r
t_r = T[:, :, 0]
print("typ danych tablicy kanału r: ", t_r.dtype)
print("rozmiar elemntu tablicy kanału r: ",t_r.itemsize)
print("rozmiar tablicy kanału r: ",t_r.shape)
im_r = Image.fromarray(t_r) # obraz w odcieniuach szarości kanału r
print("tryb kanału r: ", im_r.mode)
#tablica kanału g
t_g = T[:, :, 1]
im_g = Image.fromarray(t_g) # obraz w odcieniuach szarości kanału g
#tablica kanału b
t_b = T[:, :, 2]
im_b = Image.fromarray(t_b) # obraz w odcieniuach szarości kanału b

#ZAD 2B
im2 = Image.merge('RGB', (im_r, im_g, im_b))
diff_im = ImageChops.difference(im1, im2)

#ZAD 2C
plt.figure(figsize=(32, 16))
plt.subplot(1,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im1)
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(im2, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
plt.show()

#ZAD 3 (A-B-C)
r, g, b = im1.split()
print("tryb kanału r: ", r.mode)
print("tryb kanału g: ", g.mode)
print("tryb kanału b: ", b.mode)
plt.figure(figsize=(32, 16))
plt.subplot(1,3,1)
plt.imshow(r, "gray")
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(g)
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(b)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('im3.png')
plt.savefig('im3.jpg')
plt.show()

diff_im3 = ImageChops.difference(im)
plt.figure(figsize=(32, 16))
plt.subplot(1,1,1)
plt.imshow(diff_im3, "gray")
plt.axis('off')
plt.savefig('fig2.png')
plt.show()