# ============================================================
# 03. Eksperimen Warna RGB
# Materi: Memahami cara kerja warna RGB dengan interaktif
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Eksperimen RGB - Tutorial Pygame")

# Nilai awal RGB
r = 100
g = 150
b = 200

font = pygame.font.SysFont("Arial", 28)
font_kecil = pygame.font.SysFont("Arial", 20)

clock = pygame.time.Clock()
berjalan = True

print("Kontrol:")
print("  R/F = naik/turun nilai Red")
print("  G/V = naik/turun nilai Green")
print("  B/N = naik/turun nilai Blue")
print("  SPACE = reset")

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

        # Tekan tombol keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                r = min(255, r + 10)
            if event.key == pygame.K_f:
                r = max(0, r - 10)
            if event.key == pygame.K_g:
                g = min(255, g + 10)
            if event.key == pygame.K_v:
                g = max(0, g - 10)
            if event.key == pygame.K_b:
                b = min(255, b + 10)
            if event.key == pygame.K_n:
                b = max(0, b - 10)
            if event.key == pygame.K_SPACE:
                r, g, b = 100, 150, 200

    # Isi layar dengan warna hasil kombinasi RGB
    layar.fill((r, g, b))

    # Tampilkan nilai RGB
    info = font.render(f"R = {r}   G = {g}   B = {b}", True, (255, 255, 255))
    # Biar teks kelihatan, kasih background gelap di belakangnya
    pygame.draw.rect(layar, (0, 0, 0), (40, 40, 400, 50))
    layar.blit(info, (50, 50))

    # Petunjuk
    petunjuk1 = font_kecil.render("R/F = Red | G/V = Green | B/N = Blue | SPACE = Reset", True, (255, 255, 255))
    pygame.draw.rect(layar, (0, 0, 0), (40, 520, 720, 40))
    layar.blit(petunjuk1, (50, 530))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
