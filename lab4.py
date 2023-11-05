from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

im = Image.open('jesien.jpg')
im.save("diff.png")

im2 = Image.open('diff.png')
def statystyki(im2):
    s = stat.Stat(im2)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe
# MUSISZ PODAC 2 ZDJECIA Z 3B, KTORE TRZEBA WRZUCIC NA IMAGECHOPS DIFF - POTEM WGRAC JE DO FUNKCJI.
statystyki(dif1)

hist = dif1.histogram()
p = 0
print(hist[p])
print(hist[256 + p])
print(hist[2*256 + p])

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()

rysuj_histogram_RGB(dif1)

statystyki(dif2)

hist = dif2.histogram()
p = 0
print(hist[p])
print(hist[256 + p])
print(hist[2*256 + p])


###ZAD2 A I B
im = Image.open('obraz.jpg')
im.save('obraz1.jpg')
im1 = Image.open('obraz1.jpg')
im1.save('obraz2.jpg')
im2 = Image.open('obraz2.jpg')
im2.save('obraz3.jpg')
im3 = Image.open('obraz3.jpg')
im3.save('obraz4.jpg')
im4 = Image.open('obraz4.jpg')
im4.save('obraz5.jpg')
im5 = Image.open('obraz5.jpg')

#ZAD2 C - Oceń różnice między obrazem i obraz5.jpg

#ZAD2 D - Oceń różnice między obraz4.jpg i obraz5.jpg

#ZAD2 E Jak kolejne zapisywanie obrazu odbiega od oryginału


