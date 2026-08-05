# ============================================================
# 02. Membuat Objek / Class Sederhana
# Materi: Class untuk objek game (dasar OOP untuk game)
# ============================================================

import pygame

pygame.init()

LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Objek Sederhana (Class) - Tutorial Pygame")

HITAM  = (0, 0, 0)
PUTIH  = (255, 255, 255)
MERAH  = (255, 80, 80)
HIJAU  = (50, 200, 50)
BIRU   = (50, 120, 255)
KUNING = (255, 220, 50)

# ============================================================
# CLASS PLAYER
# Class = cetakan / blueprint untuk membuat objek
# ============================================================
class Player:
    def __init__(self, x, y, warna):
        """Constructor: dipanggil saat objek dibuat"""
        self.x = x
        self.y = y
        self.lebar = 50
        self.tinggi = 50
        self.warna = warna
        self.kecepatan = 5

    def gerak(self, tombol):
        """Update posisi berdasarkan input keyboard"""
        if tombol[pygame.K_LEFT] or tombol[pygame.K_a]:
            self.x -= self.kecepatan
        if tombol[pygame.K_RIGHT] or tombol[pygame.K_d]:
            self.x += self.kecepatan
        if tombol[pygame.K_UP] or tombol[pygame.K_w]:
            self.y -= self.kecepatan
        if tombol[pygame.K_DOWN] or tombol[pygame.K_s]:
            self.y += self.kecepatan

        # Batasi di dalam layar
        self.x = max(0, min(LEBAR - self.lebar, self.x))
        self.y = max(0, min(TINGGI - self.tinggi, self.y))

    def gambar(self, layar):
        """Gambar objek ke layar"""
        pygame.draw.rect(layar, self.warna, (self.x, self.y, self.lebar, self.tinggi), border_radius=8)
        # Mata sederhana
        pygame.draw.circle(layar, PUTIH, (self.x + 15, self.y + 18), 6)
        pygame.draw.circle(layar, PUTIH, (self.x + 35, self.y + 18), 6)
        pygame.draw.circle(layar, HITAM, (self.x + 15, self.y + 18), 3)
        pygame.draw.circle(layar, HITAM, (self.x + 35, self.y + 18), 3)

    def get_rect(self):
        """Mengembalikan Rect untuk deteksi tabrakan nanti"""
        return pygame.Rect(self.x, self.y, self.lebar, self.tinggi)


# ============================================================
# CLASS ENEMY (musuh sederhana)
# ============================================================
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lebar = 40
        self.tinggi = 40
        self.warna = MERAH
        self.arah = 1  # 1 = kanan, -1 = kiri
        self.kecepatan = 3

    def update(self):
        """Gerakan otomatis bolak-balik"""
        self.x += self.kecepatan * self.arah
        if self.x <= 0 or self.x >= LEBAR - self.lebar:
            self.arah *= -1  # balik arah

    def gambar(self, layar):
        pygame.draw.rect(layar, self.warna, (self.x, self.y, self.lebar, self.tinggi), border_radius=5)
        # "Mata jahat"
        pygame.draw.circle(layar, KUNING, (self.x + 12, self.y + 15), 5)
        pygame.draw.circle(layar, KUNING, (self.x + 28, self.y + 15), 5)


# Buat objek dari class
player = Player(100, 300, BIRU)
enemy1 = Enemy(400, 100)
enemy2 = Enemy(200, 450)

font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()
berjalan = True

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

    tombol = pygame.key.get_pressed()

    # Update
    player.gerak(tombol)
    enemy1.update()
    enemy2.update()

    # Gambar
    layar.fill((20, 20, 40))

    player.gambar(layar)
    enemy1.gambar(layar)
    enemy2.gambar(layar)

    # Info
    info = font.render("Gerakkan Player (biru) dengan WASD / Arrow", True, PUTIH)
    layar.blit(info, (150, 20))
    info2 = font.render("Musuh (merah) bergerak otomatis", True, MERAH)
    layar.blit(info2, (200, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program selesai!")
