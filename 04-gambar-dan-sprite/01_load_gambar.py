# ============================================================
# 01. Membuat & Menampilkan "Gambar" (Surface)
# Materi: Surface, membuat gambar sendiri, dan blit
# Catatan: Karena belum ada file gambar, kita buat Surface sendiri
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Surface & Gambar - Tutorial Pygame")

HITAM  = (0, 0, 0)
PUTIH  = (255, 255, 255)
MERAH  = (255, 80, 80)
HIJAU  = (50, 200, 50)
BIRU   = (50, 120, 255)
KUNING = (255, 220, 50)
ORANGE = (255, 150, 30)

font = pygame.font.SysFont("Arial", 24)

# ============================================================
# MEMBUAT SURFACE (kanvas gambar)
# Surface adalah "kertas" tempat kita menggambar
# ============================================================

# 1. Surface kosong berwarna solid
surface_merah = pygame.Surface((100, 100))
surface_merah.fill(MERAH)

# 2. Surface dengan bentuk di dalamnya
surface_bola = pygame.Surface((80, 80), pygame.SRCALPHA)  # SRCALPHA = support transparan
pygame.draw.circle(surface_bola, HIJAU, (40, 40), 35)
pygame.draw.circle(surface_bola, PUTIH, (40, 40), 35, 3)

# 3. Surface "player" sederhana (persegi + mata)
surface_player = pygame.Surface((60, 60), pygame.SRCALPHA)
pygame.draw.rect(surface_player, BIRU, (0, 0, 60, 60), border_radius=10)
pygame.draw.circle(surface_player, PUTIH, (20, 25), 8)   # mata kiri
pygame.draw.circle(surface_player, PUTIH, (40, 25), 8)   # mata kanan
pygame.draw.circle(surface_player, HITAM, (20, 25), 4)   # pupil
pygame.draw.circle(surface_player, HITAM, (40, 25), 4)
pygame.draw.arc(surface_player, PUTIH, (15, 30, 30, 25), 3.14, 0, 3)  # senyum

# 4. Surface bintang
surface_bintang = pygame.Surface((70, 70), pygame.SRCALPHA)
titik = [(35, 5), (42, 25), (65, 25), (47, 40), (55, 60),
         (35, 48), (15, 60), (23, 40), (5, 25), (28, 25)]
pygame.draw.polygon(surface_bintang, KUNING, titik)

clock = pygame.time.Clock()
berjalan = True

# Posisi untuk digeser
player_x = 100
player_y = 300

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

    # Gerakkan player dengan keyboard
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT]:
        player_x -= 4
    if tombol[pygame.K_RIGHT]:
        player_x += 4
    if tombol[pygame.K_UP]:
        player_y -= 4
    if tombol[pygame.K_DOWN]:
        player_y += 4

    layar.fill((30, 30, 50))  # biru gelap

    # ============================================================
    # BLIT = menempelkan Surface ke layar
    # layar.blit(surface, (x, y))
    # ============================================================
    layar.blit(surface_merah, (50, 50))
    layar.blit(surface_bola, (200, 60))
    layar.blit(surface_bintang, (350, 50))
    layar.blit(surface_player, (player_x, player_y))

    # Label
    layar.blit(font.render("Surface Merah", True, PUTIH), (40, 160))
    layar.blit(font.render("Bola", True, PUTIH), (210, 160))
    layar.blit(font.render("Bintang", True, PUTIH), (350, 160))
    layar.blit(font.render("Player (gerak dengan Arrow)", True, PUTIH), (player_x - 40, player_y + 70))

    info = font.render("Ini adalah cara dasar membuat & menampilkan gambar", True, ORANGE)
    layar.blit(info, (100, 500))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
