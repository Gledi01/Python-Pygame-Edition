# ============================================================
# 01. Menggambar Bentuk Dasar
# Materi: Persegi, lingkaran, garis, dan ellipse
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Bentuk Dasar - Tutorial Pygame")

# Warna
HITAM  = (0, 0, 0)
PUTIH  = (255, 255, 255)
MERAH  = (255, 50, 50)
HIJAU  = (50, 200, 50)
BIRU   = (50, 100, 255)
KUNING = (255, 220, 0)
UNGU   = (180, 50, 200)

clock = pygame.time.Clock()
berjalan = True

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

    # Bersihkan layar
    layar.fill(HITAM)

    # ============================================================
    # 1. PERSEGI / RECTANGLE
    # pygame.draw.rect(layar, warna, (x, y, lebar, tinggi), ketebalan)
    # ketebalan = 0 berarti diisi penuh (solid)
    # ============================================================
    pygame.draw.rect(layar, MERAH, (50, 50, 150, 100), 0)   # solid
    pygame.draw.rect(layar, PUTIH, (50, 50, 150, 100), 3)   # border putih

    # ============================================================
    # 2. LINGKARAN / CIRCLE
    # pygame.draw.circle(layar, warna, (x_tengah, y_tengah), radius, ketebalan)
    # ============================================================
    pygame.draw.circle(layar, HIJAU, (350, 100), 60, 0)     # solid
    pygame.draw.circle(layar, PUTIH, (350, 100), 60, 4)     # border

    # ============================================================
    # 3. ELLIPSE (lonjong)
    # pygame.draw.ellipse(layar, warna, (x, y, lebar, tinggi), ketebalan)
    # ============================================================
    pygame.draw.ellipse(layar, BIRU, (500, 40, 200, 120), 0)

    # ============================================================
    # 4. GARIS / LINE
    # pygame.draw.line(layar, warna, (x1, y1), (x2, y2), ketebalan)
    # ============================================================
    pygame.draw.line(layar, KUNING, (50, 200), (750, 200), 5)
    pygame.draw.line(layar, UNGU, (50, 250), (400, 400), 3)
    pygame.draw.line(layar, PUTIH, (400, 400), (750, 250), 3)

    # ============================================================
    # 5. POLYGON (banyak sisi)
    # pygame.draw.polygon(layar, warna, [(x1,y1), (x2,y2), ...], ketebalan)
    # ============================================================
    titik_segitiga = [(200, 450), (100, 550), (300, 550)]
    pygame.draw.polygon(layar, MERAH, titik_segitiga, 0)

    titik_bintang = [(500, 400), (530, 480), (620, 480), (550, 530),
                     (580, 610), (500, 560), (420, 610), (450, 530),
                     (380, 480), (470, 480)]
    pygame.draw.polygon(layar, KUNING, titik_bintang, 0)

    # Update layar
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
