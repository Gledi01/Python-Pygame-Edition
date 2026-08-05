# ============================================================
# 02. Mengganti Warna Latar
# Materi: Memahami warna RGB dan mengisi latar belakang
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Warna Latar - Tutorial Pygame")

# ============================================================
# WARNA RGB
# RGB = Red (Merah), Green (Hijau), Blue (Biru)
# Setiap nilai dari 0 sampai 255
# ============================================================
HITAM   = (0, 0, 0)
PUTIH   = (255, 255, 255)
MERAH   = (255, 0, 0)
HIJAU   = (0, 255, 0)
BIRU    = (0, 0, 255)
KUNING  = (255, 255, 0)
UNGU    = (128, 0, 128)
ORANGE  = (255, 165, 0)
CYAN    = (0, 255, 255)
ABU     = (128, 128, 128)

# Coba ganti warna di bawah ini!
warna_latar = BIRU   # Ganti ke MERAH, HIJAU, KUNING, dll

berjalan = True

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

    # Isi seluruh layar dengan warna yang dipilih
    layar.fill(warna_latar)

    pygame.display.flip()

pygame.quit()
print("Program selesai!")
