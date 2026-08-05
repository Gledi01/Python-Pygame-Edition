# ============================================================
# 03. Tombol Interaktif + Keluar dengan Rapi
# Materi: Membuat tombol yang bisa diklik + best practice keluar
# ============================================================

import pygame
import sys

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Tombol Interaktif - Tutorial Pygame")

HITAM  = (0, 0, 0)
PUTIH  = (255, 255, 255)
MERAH  = (220, 50, 50)
HIJAU  = (50, 180, 50)
BIRU   = (50, 120, 220)
ABU    = (100, 100, 100)
ABU_TUA = (60, 60, 60)

font = pygame.font.SysFont("Arial", 32)
font_judul = pygame.font.SysFont("Arial", 48)

# ============================================================
# FUNGSI MEMBUAT TOMBOL
# ============================================================
def buat_tombol(teks, x, y, lebar, tinggi, warna_normal, warna_hover, mouse_pos, mouse_klik):
    """
    Menggambar tombol dan mengembalikan True jika diklik
    """
    # Cek apakah mouse di atas tombol
    hover = (x <= mouse_pos[0] <= x + lebar and
             y <= mouse_pos[1] <= y + tinggi)

    # Pilih warna
    warna = warna_hover if hover else warna_normal

    # Gambar tombol
    pygame.draw.rect(layar, warna, (x, y, lebar, tinggi), border_radius=10)
    pygame.draw.rect(layar, PUTIH, (x, y, lebar, tinggi), 2, border_radius=10)

    # Teks di tengah tombol
    teks_surface = font.render(teks, True, PUTIH)
    teks_rect = teks_surface.get_rect(center=(x + lebar // 2, y + tinggi // 2))
    layar.blit(teks_surface, teks_rect)

    # Jika hover + klik kiri
    if hover and mouse_klik:
        return True
    return False


clock = pygame.time.Clock()
berjalan = True
pesan = "Klik salah satu tombol di bawah"

while berjalan:
    # Ambil status mouse sekali di awal frame
    mouse_pos = pygame.mouse.get_pos()
    mouse_klik = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_klik = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            berjalan = False

    layar.fill(HITAM)

    # Judul
    judul = font_judul.render("Menu Tombol", True, PUTIH)
    layar.blit(judul, (280, 80))

    # Pesan status
    status = font.render(pesan, True, (200, 200, 100))
    layar.blit(status, (200, 160))

    # ============================================================
    # TOMBOL-TOMBOL
    # ============================================================
    if buat_tombol("Mainkan", 300, 250, 200, 60, HIJAU, (80, 220, 80), mouse_pos, mouse_klik):
        pesan = "Tombol MAINKAN ditekan! 🎮"

    if buat_tombol("Pengaturan", 300, 330, 200, 60, BIRU, (80, 160, 255), mouse_pos, mouse_klik):
        pesan = "Tombol PENGATURAN ditekan! ⚙️"

    if buat_tombol("Keluar", 300, 410, 200, 60, MERAH, (255, 80, 80), mouse_pos, mouse_klik):
        pesan = "Keluar dari program..."
        berjalan = False

    # Petunjuk
    petunjuk = font.render("ESC juga bisa untuk keluar", True, ABU)
    layar.blit(petunjuk, (250, 520))

    pygame.display.flip()
    clock.tick(60)

# ============================================================
# CARA KELUAR YANG BENAR
# pygame.quit() membersihkan resource pygame
# sys.exit() menghentikan program Python sepenuhnya
# ============================================================
pygame.quit()
sys.exit()
