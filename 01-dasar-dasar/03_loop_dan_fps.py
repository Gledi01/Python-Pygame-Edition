# ============================================================
# 03. Loop Game dan FPS (Frame Per Second)
# Materi: Mengontrol kecepatan game dengan Clock
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Loop & FPS - Tutorial Pygame")

# Warna
HITAM = (0, 0, 0)
PUTIH = (255, 255, 255)
HIJAU = (0, 200, 0)

# ============================================================
# CLOCK
# Digunakan untuk mengatur FPS (berapa kali layar di-update per detik)
# FPS tinggi = gerakan lebih halus, tapi lebih berat
# FPS 60 adalah standar untuk kebanyakan game
# ============================================================
clock = pygame.time.Clock()
FPS = 60

# Font untuk menampilkan teks FPS
font = pygame.font.SysFont("Arial", 30)

berjalan = True

while berjalan:
    # ============================================================
    # 1. HANDLE EVENT
    # ============================================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

    # ============================================================
    # 2. UPDATE LOGIKA (belum ada di contoh ini)
    # ============================================================
    # Di sini nanti kita update posisi objek, skor, dll

    # ============================================================
    # 3. GAMBAR / RENDER
    # ============================================================
    layar.fill(HITAM)

    # Tampilkan teks informasi
    teks = font.render("FPS Target: 60 | Tekan X untuk keluar", True, PUTIH)
    layar.blit(teks, (50, 50))

    teks2 = font.render("Ini adalah struktur dasar Game Loop", True, HIJAU)
    layar.blit(teks2, (50, 100))

    # ============================================================
    # 4. UPDATE LAYAR
    # ============================================================
    pygame.display.flip()

    # ============================================================
    # 5. BATASI FPS
    # clock.tick(FPS) membuat loop berjalan maksimal FPS kali per detik
    # ============================================================
    clock.tick(FPS)

pygame.quit()
print("Program selesai!")
