# ============================================================
# 02. Menulis Teks di Layar
# Materi: Font, render teks, dan menampilkan teks
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Teks di Pygame - Tutorial")

HITAM  = (0, 0, 0)
PUTIH  = (255, 255, 255)
MERAH  = (255, 80, 80)
HIJAU  = (80, 220, 80)
BIRU   = (80, 150, 255)
KUNING = (255, 220, 50)

# ============================================================
# MEMBUAT FONT
# SysFont("nama_font", ukuran)
# Nama font umum: Arial, Comic Sans MS, Courier New, dll
# ============================================================
font_besar  = pygame.font.SysFont("Arial", 48)
font_sedang = pygame.font.SysFont("Arial", 32)
font_kecil  = pygame.font.SysFont("Arial", 20)
font_tebal  = pygame.font.SysFont("Arial", 36, bold=True)

clock = pygame.time.Clock()
berjalan = True

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

    layar.fill(HITAM)

    # ============================================================
    # CARA MENAMPILKAN TEKS
    # 1. Render teks menjadi Surface (gambar)
    #    font.render("teks", anti_alias, warna)
    #    anti_alias = True supaya teks halus
    # 2. Blit (tempel) Surface ke layar
    #    layar.blit(surface_teks, (x, y))
    # ============================================================

    # Judul
    judul = font_besar.render("Belajar Teks di Pygame!", True, KUNING)
    layar.blit(judul, (180, 50))

    # Teks biasa
    teks1 = font_sedang.render("Ini adalah teks ukuran sedang", True, PUTIH)
    layar.blit(teks1, (100, 150))

    teks2 = font_kecil.render("Ini teks kecil - cocok untuk skor atau info", True, HIJAU)
    layar.blit(teks2, (100, 200))

    teks3 = font_tebal.render("Teks TEBAL untuk penekanan", True, MERAH)
    layar.blit(teks3, (100, 250))

    # Teks dengan warna berbeda
    teks4 = font_sedang.render("Merah", True, MERAH)
    teks5 = font_sedang.render("Hijau", True, HIJAU)
    teks6 = font_sedang.render("Biru", True, BIRU)
    layar.blit(teks4, (100, 350))
    layar.blit(teks5, (250, 350))
    layar.blit(teks6, (400, 350))

    # Petunjuk
    petunjuk = font_kecil.render("Tekan tombol X di pojok untuk keluar", True, (150, 150, 150))
    layar.blit(petunjuk, (220, 550))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
