# ============================================================
# 01. Jendela Kosong Pygame
# Materi: Membuat jendela game yang paling sederhana
# ============================================================

# Import library pygame
# pygame adalah library untuk membuat game 2D di Python
import pygame

# Inisialisasi pygame
# Harus dipanggil dulu sebelum pakai fungsi-fungsi pygame
pygame.init()

# Tentukan ukuran jendela (lebar, tinggi) dalam pixel
LEBAR = 800
TINGGI = 600

# Buat jendela game
# set_mode() membuat layar / window
layar = pygame.display.set_mode((LEBAR, TINGGI))

# Kasih judul di jendela
pygame.display.set_caption("Jendela Pertama - Tutorial Pygame")

# Variable untuk kontrol loop game
# True = game masih jalan, False = game berhenti
berjalan = True

# ============================================================
# GAME LOOP (loop utama)
# Semua game punya loop ini. Di sini semua proses terjadi.
# ============================================================
while berjalan:
    # Cek semua event (kejadian) yang terjadi
    # Misalnya: klik mouse, tekan keyboard, tutup jendela
    for event in pygame.event.get():
        # Jika user klik tombol close (X) di jendela
        if event.type == pygame.QUIT:
            berjalan = False  # Stop loop

    # Isi layar dengan warna hitam (RGB: 0, 0, 0)
    # RGB = Red, Green, Blue (nilai 0-255)
    layar.fill((0, 0, 0))

    # Update tampilan layar
    # Tanpa ini, perubahan di layar tidak terlihat
    pygame.display.flip()

# Keluar dari pygame dengan rapi
pygame.quit()
print("Program selesai. Terima kasih!")
