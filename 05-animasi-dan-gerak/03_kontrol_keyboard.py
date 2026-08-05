# ============================================================
# 03. Kontrol Karakter dengan Keyboard + Gravity Sederhana
# Materi: Gerakan kiri-kanan + lompat
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Kontrol Karakter + Lompat - Tutorial Pygame")

HITAM  = (0, 0, 0)
PUTIH  = (255, 255, 255)
BIRU   = (50, 150, 255)
HIJAU  = (50, 180, 50)
COKLAT = (139, 90, 43)
KUNING = (255, 220, 50)

# ============================================================
# DATA PLAYER
# ============================================================
player_x = 100
player_y = 400
player_lebar = 40
player_tinggi = 50
kecepatan = 6
velocity_y = 0          # kecepatan vertikal
gravity = 0.6           # gravitasi
lompat_power = -12      # kekuatan lompat (negatif = ke atas)
di_tanah = False

# Lantai
lantai_y = 500

font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()
berjalan = True

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

        # Lompat hanya saat di tanah
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and di_tanah:
                velocity_y = lompat_power
                di_tanah = False

    # ============================================================
    # INPUT HORIZONTAL
    # ============================================================
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT] or tombol[pygame.K_a]:
        player_x -= kecepatan
    if tombol[pygame.K_RIGHT] or tombol[pygame.K_d]:
        player_x += kecepatan

    # Batasi horizontal
    player_x = max(0, min(LEBAR - player_lebar, player_x))

    # ============================================================
    # GRAVITASI & LOMPAT
    # ============================================================
    velocity_y += gravity          # tarik ke bawah terus
    player_y += velocity_y

    # Cek apakah menyentuh lantai
    if player_y + player_tinggi >= lantai_y:
        player_y = lantai_y - player_tinggi
        velocity_y = 0
        di_tanah = True

    # Gambar
    layar.fill((30, 30, 60))

    # Lantai
    pygame.draw.rect(layar, COKLAT, (0, lantai_y, LEBAR, TINGGI - lantai_y))
    pygame.draw.rect(layar, HIJAU, (0, lantai_y, LEBAR, 15))  # rumput

    # Player
    pygame.draw.rect(layar, BIRU, (player_x, player_y, player_lebar, player_tinggi), border_radius=6)
    # Mata
    pygame.draw.circle(layar, PUTIH, (player_x + 12, player_y + 15), 5)
    pygame.draw.circle(layar, PUTIH, (player_x + 28, player_y + 15), 5)
    pygame.draw.circle(layar, HITAM, (player_x + 12, player_y + 15), 2)
    pygame.draw.circle(layar, HITAM, (player_x + 28, player_y + 15), 2)

    # Info
    status = "Di TANAH" if di_tanah else "Di UDARA"
    teks = font.render(f"Status: {status} | Velocity Y: {velocity_y:.1f}", True, KUNING)
    layar.blit(teks, (20, 20))
    teks2 = font.render("A/D atau ←/→ = gerak | SPACE = lompat", True, PUTIH)
    layar.blit(teks2, (20, 55))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
