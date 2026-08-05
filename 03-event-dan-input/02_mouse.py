# ============================================================
# 02. Input Mouse
# Materi: Posisi mouse, klik kiri/kanan, dan hover
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Input Mouse - Tutorial Pygame")

HITAM  = (0, 0, 0)
PUTIH  = (255, 255, 255)
MERAH  = (255, 80, 80)
HIJAU  = (50, 220, 50)
BIRU   = (80, 150, 255)
KUNING = (255, 220, 50)
ABU    = (80, 80, 80)

font = pygame.font.SysFont("Arial", 28)
font_kecil = pygame.font.SysFont("Arial", 22)

# Kotak target
kotak_x = 300
kotak_y = 200
kotak_lebar = 200
kotak_tinggi = 150

# Status
klik_kiri = False
klik_kanan = False
pesan = "Gerakkan mouse dan klik!"

clock = pygame.time.Clock()
berjalan = True

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

        # ============================================================
        # MOUSEBUTTONDOWN = tombol mouse ditekan
        # event.button: 1 = kiri, 2 = tengah, 3 = kanan
        # ============================================================
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Klik kiri
                klik_kiri = True
                pesan = "Klik KIRI terdeteksi!"
            elif event.button == 3:  # Klik kanan
                klik_kanan = True
                pesan = "Klik KANAN terdeteksi!"

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                klik_kiri = False
            elif event.button == 3:
                klik_kanan = False

    # ============================================================
    # Ambil posisi mouse saat ini
    # mouse_pos = (x, y)
    # ============================================================
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Cek apakah mouse di dalam kotak (hover)
    di_dalam_kotak = (kotak_x <= mouse_x <= kotak_x + kotak_lebar and
                      kotak_y <= mouse_y <= kotak_y + kotak_tinggi)

    # Warna kotak berubah kalau di-hover
    if di_dalam_kotak:
        warna_kotak = HIJAU
        if klik_kiri:
            warna_kotak = KUNING
    else:
        warna_kotak = BIRU

    # Gambar
    layar.fill(HITAM)

    # Kotak
    pygame.draw.rect(layar, warna_kotak, (kotak_x, kotak_y, kotak_lebar, kotak_tinggi))
    pygame.draw.rect(layar, PUTIH, (kotak_x, kotak_y, kotak_lebar, kotak_tinggi), 3)

    # Crosshair di posisi mouse
    pygame.draw.line(layar, MERAH, (mouse_x - 15, mouse_y), (mouse_x + 15, mouse_y), 2)
    pygame.draw.line(layar, MERAH, (mouse_x, mouse_y - 15), (mouse_x, mouse_y + 15), 2)
    pygame.draw.circle(layar, MERAH, (mouse_x, mouse_y), 8, 2)

    # Info
    judul = font.render("Deteksi Mouse", True, PUTIH)
    layar.blit(judul, (300, 30))

    pos_teks = font_kecil.render(f"Posisi Mouse: ({mouse_x}, {mouse_y})", True, PUTIH)
    layar.blit(pos_teks, (50, 450))

    hover_teks = font_kecil.render(f"Di dalam kotak: {'YA' if di_dalam_kotak else 'TIDAK'}", True, HIJAU if di_dalam_kotak else ABU)
    layar.blit(hover_teks, (50, 490))

    pesan_teks = font_kecil.render(pesan, True, KUNING)
    layar.blit(pesan_teks, (50, 530))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
