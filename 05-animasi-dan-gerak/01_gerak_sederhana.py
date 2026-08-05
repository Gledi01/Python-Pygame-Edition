# ============================================================
# 01. Gerakan Sederhana
# Materi: Mengubah posisi objek setiap frame
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Gerakan Sederhana - Tutorial Pygame")

HITAM  = (0, 0, 0)
PUTIH  = (255, 255, 255)
BIRU   = (50, 150, 255)
HIJAU  = (50, 200, 50)
KUNING = (255, 220, 50)

# Posisi dan kecepatan bola
bola_x = 100
bola_y = 300
kecepatan_x = 4

font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()
berjalan = True

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

    # ============================================================
    # UPDATE POSISI
    # Setiap frame, posisi ditambah dengan kecepatan
    # ============================================================
    bola_x += kecepatan_x

    # Jika keluar kanan, balik ke kiri
    if bola_x > LEBAR + 30:
        bola_x = -30

    # Gambar
    layar.fill(HITAM)

    # Bola bergerak
    pygame.draw.circle(layar, BIRU, (bola_x, bola_y), 30)
    pygame.draw.circle(layar, PUTIH, (bola_x, bola_y), 30, 3)

    # Garis lantai
    pygame.draw.line(layar, HIJAU, (0, 350), (LEBAR, 350), 2)

    # Info
    teks = font.render(f"Posisi X: {bola_x} | Kecepatan: {kecepatan_x}", True, KUNING)
    layar.blit(teks, (50, 50))
    teks2 = font.render("Bola bergerak terus ke kanan (loop)", True, PUTIH)
    layar.blit(teks2, (50, 90))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
