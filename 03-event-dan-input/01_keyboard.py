# ============================================================
# 01. Input Keyboard
# Materi: Mendeteksi tombol yang ditekan
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Input Keyboard - Tutorial Pygame")

HITAM = (0, 0, 0)
PUTIH = (255, 255, 255)
HIJAU = (50, 220, 50)
MERAH = (255, 80, 80)
BIRU  = (80, 150, 255)

font = pygame.font.SysFont("Arial", 36)
font_kecil = pygame.font.SysFont("Arial", 24)

# Posisi kotak yang bisa digeser dengan keyboard
x = 350
y = 250
kecepatan = 5

clock = pygame.time.Clock()
berjalan = True

tombol_terakhir = "Belum ada"

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

        # ============================================================
        # KEYDOWN = tombol baru saja ditekan (sekali)
        # ============================================================
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                tombol_terakhir = "KIRI (← / A)"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                tombol_terakhir = "KANAN (→ / D)"
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                tombol_terakhir = "ATAS (↑ / W)"
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                tombol_terakhir = "BAWAH (↓ / S)"
            elif event.key == pygame.K_SPACE:
                tombol_terakhir = "SPACE"
            elif event.key == pygame.K_ESCAPE:
                berjalan = False

    # ============================================================
    # get_pressed() = cek tombol yang SEDANG ditahan (terus-menerus)
    # Cocok untuk gerakan karakter
    # ============================================================
    tombol = pygame.key.get_pressed()

    if tombol[pygame.K_LEFT] or tombol[pygame.K_a]:
        x -= kecepatan
    if tombol[pygame.K_RIGHT] or tombol[pygame.K_d]:
        x += kecepatan
    if tombol[pygame.K_UP] or tombol[pygame.K_w]:
        y -= kecepatan
    if tombol[pygame.K_DOWN] or tombol[pygame.K_s]:
        y += kecepatan

    # Batasi supaya kotak tidak keluar layar
    x = max(0, min(LEBAR - 50, x))
    y = max(0, min(TINGGI - 50, y))

    # Gambar
    layar.fill(HITAM)

    # Kotak yang bergerak
    pygame.draw.rect(layar, BIRU, (x, y, 50, 50))

    # Info
    judul = font.render("Gerakkan kotak dengan WASD / Arrow", True, PUTIH)
    layar.blit(judul, (150, 30))

    info = font_kecil.render(f"Tombol terakhir: {tombol_terakhir}", True, HIJAU)
    layar.blit(info, (50, 100))

    posisi = font_kecil.render(f"Posisi: x={x}, y={y}", True, MERAH)
    layar.blit(posisi, (50, 140))

    petunjuk = font_kecil.render("ESC = Keluar", True, (150, 150, 150))
    layar.blit(petunjuk, (50, 550))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
