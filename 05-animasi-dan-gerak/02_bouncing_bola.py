# ============================================================
# 02. Bola Memantul (Bouncing)
# Materi: Deteksi batas layar dan membalik arah
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Bola Memantul - Tutorial Pygame")

HITAM  = (0, 0, 0)
PUTIH  = (255, 255, 255)
MERAH  = (255, 80, 80)
HIJAU  = (50, 200, 50)
BIRU   = (50, 150, 255)
KUNING = (255, 220, 50)

# ============================================================
# DATA BOLA
# ============================================================
bola_x = 400
bola_y = 300
radius = 25
kecepatan_x = 5
kecepatan_y = 4
warna_bola = BIRU

font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()
berjalan = True

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False
        # Tekan SPACE untuk ubah warna
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Ganti warna secara acak sederhana
            if warna_bola == BIRU:
                warna_bola = MERAH
            elif warna_bola == MERAH:
                warna_bola = HIJAU
            else:
                warna_bola = BIRU

    # ============================================================
    # UPDATE POSISI
    # ============================================================
    bola_x += kecepatan_x
    bola_y += kecepatan_y

    # ============================================================
    # DETEKSI TABRAKAN DENGAN DINDING
    # Jika menyentuh kiri/kanan → balik kecepatan_x
    # Jika menyentuh atas/bawah → balik kecepatan_y
    # ============================================================
    if bola_x - radius <= 0 or bola_x + radius >= LEBAR:
        kecepatan_x = -kecepatan_x  # balik arah horizontal

    if bola_y - radius <= 0 or bola_y + radius >= TINGGI:
        kecepatan_y = -kecepatan_y  # balik arah vertikal

    # Gambar
    layar.fill(HITAM)

    # Bola
    pygame.draw.circle(layar, warna_bola, (bola_x, bola_y), radius)
    pygame.draw.circle(layar, PUTIH, (bola_x, bola_y), radius, 3)

    # Info
    teks = font.render(f"Posisi: ({bola_x}, {bola_y})", True, PUTIH)
    layar.blit(teks, (20, 20))
    teks2 = font.render(f"Kecepatan: ({kecepatan_x}, {kecepatan_y})", True, KUNING)
    layar.blit(teks2, (20, 55))
    teks3 = font.render("SPACE = ganti warna | X = keluar", True, (150, 150, 150))
    layar.blit(teks3, (20, 550))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
