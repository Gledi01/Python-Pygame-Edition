# ============================================================
# GAME DRAG & DROP - Puzzle Sederhana
# Materi akhir: Gabungan semua yang sudah dipelajari
# 
# Cara main:
# - Klik dan tahan kotak berwarna, lalu geser ke target yang sesuai
# - Jika warna cocok, kotak "nempel" dan skor bertambah
# - Selesaikan semua untuk menang!
# ============================================================

import pygame
import sys

pygame.init()

# ============================================================
# KONSTANTA
# ============================================================
LEBAR = 900
TINGGI = 650
FPS = 60

# Warna
HITAM     = (20, 20, 30)
PUTIH     = (255, 255, 255)
ABU       = (80, 80, 100)
ABU_MUDA  = (140, 140, 160)
MERAH     = (230, 70, 70)
HIJAU     = (50, 200, 100)
BIRU      = (60, 130, 255)
KUNING    = (255, 210, 50)
UNGU      = (180, 80, 220)
ORANGE    = (255, 150, 40)
CYAN      = (50, 220, 220)

# ============================================================
# CLASS KOTAK (yang bisa di-drag)
# ============================================================
class Kotak:
    def __init__(self, x, y, ukuran, warna, nama_warna):
        self.x = x
        self.y = y
        self.ukuran = ukuran
        self.warna = warna
        self.nama_warna = nama_warna
        self.dragging = False          # sedang digeser?
        self.offset_x = 0              # selisih posisi mouse dengan pojok kotak
        self.offset_y = 0
        self.terpasang = False         # sudah dipasang di target?
        self.x_awal = x                # posisi awal (untuk reset)
        self.y_awal = y

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.ukuran, self.ukuran)

    def mulai_drag(self, mouse_x, mouse_y):
        """Mulai menggeser kotak"""
        if not self.terpasang:
            self.dragging = True
            self.offset_x = self.x - mouse_x
            self.offset_y = self.y - mouse_y

    def update_drag(self, mouse_x, mouse_y):
        """Update posisi saat digeser"""
        if self.dragging:
            self.x = mouse_x + self.offset_x
            self.y = mouse_y + self.offset_y

    def lepas(self):
        """Lepas mouse"""
        self.dragging = False

    def reset(self):
        """Kembalikan ke posisi awal"""
        self.x = self.x_awal
        self.y = self.y_awal
        self.terpasang = False
        self.dragging = False

    def gambar(self, layar, font):
        # Shadow biar kelihatan 3D
        if not self.terpasang:
            pygame.draw.rect(layar, (0, 0, 0), 
                           (self.x + 4, self.y + 4, self.ukuran, self.ukuran), 
                           border_radius=12)

        # Kotak utama
        pygame.draw.rect(layar, self.warna, 
                        (self.x, self.y, self.ukuran, self.ukuran), 
                        border_radius=12)

        # Border
        border_warna = PUTIH if self.dragging else (255, 255, 255, 100)
        pygame.draw.rect(layar, PUTIH, 
                        (self.x, self.y, self.ukuran, self.ukuran), 
                        3, border_radius=12)

        # Nama warna di tengah
        teks = font.render(self.nama_warna, True, PUTIH)
        teks_rect = teks.get_rect(center=(self.x + self.ukuran // 2, 
                                          self.y + self.ukuran // 2))
        layar.blit(teks, teks_rect)


# ============================================================
# CLASS TARGET (tempat drop)
# ============================================================
class Target:
    def __init__(self, x, y, ukuran, warna, nama_warna):
        self.x = x
        self.y = y
        self.ukuran = ukuran
        self.warna = warna
        self.nama_warna = nama_warna
        self.terisi = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.ukuran, self.ukuran)

    def cocok(self, kotak):
        """Cek apakah kotak ini cocok dengan target"""
        return self.nama_warna == kotak.nama_warna and not self.terisi

    def gambar(self, layar, font):
        # Kotak target (outline saja)
        if self.terisi:
            # Sudah terisi → tampil solid transparan
            s = pygame.Surface((self.ukuran, self.ukuran), pygame.SRCALPHA)
            s.fill((*self.warna, 80))
            layar.blit(s, (self.x, self.y))
            pygame.draw.rect(layar, self.warna, 
                           (self.x, self.y, self.ukuran, self.ukuran), 
                           4, border_radius=12)
        else:
            # Belum terisi → dashed look (outline tebal)
            pygame.draw.rect(layar, self.warna, 
                           (self.x, self.y, self.ukuran, self.ukuran), 
                           4, border_radius=12)
            # Isi semi transparan gelap
            s = pygame.Surface((self.ukuran - 8, self.ukuran - 8), pygame.SRCALPHA)
            s.fill((0, 0, 0, 60))
            layar.blit(s, (self.x + 4, self.y + 4))

        # Label
        teks = font.render(self.nama_warna, True, self.warna)
        teks_rect = teks.get_rect(center=(self.x + self.ukuran // 2, 
                                          self.y + self.ukuran + 20))
        layar.blit(teks, teks_rect)


# ============================================================
# SETUP GAME
# ============================================================
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("🎮 Game Drag & Drop - Tutorial Pygame RPL")

clock = pygame.time.Clock()
font_judul = pygame.font.SysFont("Arial", 40, bold=True)
font_normal = pygame.font.SysFont("Arial", 22)
font_kecil = pygame.font.SysFont("Arial", 18)
font_kotak = pygame.font.SysFont("Arial", 16, bold=True)

# Buat kotak-kotak yang bisa digeser (posisi bawah)
ukuran_kotak = 90
kotak_list = [
    Kotak(80,  480, ukuran_kotak, MERAH,  "Merah"),
    Kotak(200, 480, ukuran_kotak, HIJAU,  "Hijau"),
    Kotak(320, 480, ukuran_kotak, BIRU,   "Biru"),
    Kotak(440, 480, ukuran_kotak, KUNING, "Kuning"),
    Kotak(560, 480, ukuran_kotak, UNGU,   "Ungu"),
]

# Buat target (posisi atas) - urutan diacak supaya lebih menantang
target_list = [
    Target(100, 120, ukuran_kotak, BIRU,   "Biru"),
    Target(250, 120, ukuran_kotak, KUNING, "Kuning"),
    Target(400, 120, ukuran_kotak, MERAH,  "Merah"),
    Target(550, 120, ukuran_kotak, UNGU,   "Ungu"),
    Target(700, 120, ukuran_kotak, HIJAU,  "Hijau"),
]

# Game state
skor = 0
total = len(kotak_list)
pesan = "Geser kotak ke target yang warnanya sama!"
pesan_warna = KUNING
menang = False
kotak_aktif = None   # kotak yang sedang di-drag

# ============================================================
# FUNGSI BANTUAN
# ============================================================
def cek_drop(kotak):
    """Cek apakah kotak di-drop di atas target yang cocok"""
    global skor, pesan, pesan_warna, menang

    for target in target_list:
        if target.get_rect().colliderect(kotak.get_rect()):
            if target.cocok(kotak):
                # BENAR!
                kotak.x = target.x
                kotak.y = target.y
                kotak.terpasang = True
                target.terisi = True
                skor += 1
                pesan = f"Benar! {kotak.nama_warna} cocok! 🎉"
                pesan_warna = HIJAU

                if skor >= total:
                    menang = True
                    pesan = "SELAMAT! Semua berhasil dipasang! 🏆"
                    pesan_warna = KUNING
                return True
            else:
                # SALAH warna
                pesan = f"Salah! Itu target {target.nama_warna}, bukan {kotak.nama_warna}"
                pesan_warna = MERAH
                return False
    return False


def reset_game():
    """Reset semua ke awal"""
    global skor, pesan, pesan_warna, menang, kotak_aktif
    skor = 0
    menang = False
    pesan = "Geser kotak ke target yang warnanya sama!"
    pesan_warna = KUNING
    kotak_aktif = None
    for k in kotak_list:
        k.reset()
    for t in target_list:
        t.terisi = False


# ============================================================
# GAME LOOP
# ============================================================
berjalan = True

while berjalan:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                berjalan = False
            if event.key == pygame.K_r:
                reset_game()

        # ============================================================
        # MOUSE DOWN → mulai drag
        # ============================================================
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not menang:
                # Cek dari kotak paling atas (supaya yang overlap bisa dipilih)
                for kotak in reversed(kotak_list):
                    if kotak.get_rect().collidepoint(mouse_x, mouse_y) and not kotak.terpasang:
                        kotak.mulai_drag(mouse_x, mouse_y)
                        kotak_aktif = kotak
                        # Pindahkan ke akhir list supaya digambar di paling atas
                        kotak_list.remove(kotak)
                        kotak_list.append(kotak)
                        break

        # ============================================================
        # MOUSE UP → lepas & cek drop
        # ============================================================
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if kotak_aktif:
                kotak_aktif.lepas()
                berhasil = cek_drop(kotak_aktif)
                if not berhasil and not kotak_aktif.terpasang:
                    # Kembali ke posisi awal kalau salah / tidak di target
                    kotak_aktif.x = kotak_aktif.x_awal
                    kotak_aktif.y = kotak_aktif.y_awal
                    if "Salah" not in pesan:
                        pesan = "Lepas di atas target yang sesuai warnanya"
                        pesan_warna = ORANGE
                kotak_aktif = None

    # Update posisi kotak yang sedang di-drag
    if kotak_aktif and kotak_aktif.dragging:
        kotak_aktif.update_drag(mouse_x, mouse_y)

    # ============================================================
    # DRAW
    # ============================================================
    layar.fill(HITAM)

    # Judul
    judul = font_judul.render("Drag & Drop Puzzle", True, PUTIH)
    layar.blit(judul, (LEBAR // 2 - judul.get_width() // 2, 20))

    # Skor
    skor_teks = font_normal.render(f"Skor: {skor} / {total}", True, CYAN)
    layar.blit(skor_teks, (30, 30))

    # Pesan
    pesan_teks = font_normal.render(pesan, True, pesan_warna)
    layar.blit(pesan_teks, (LEBAR // 2 - pesan_teks.get_width() // 2, 70))

    # Gambar target dulu (di belakang)
    for target in target_list:
        target.gambar(layar, font_kecil)

    # Label area
    label_target = font_kecil.render("▼ TARGET (drop di sini) ▼", True, ABU_MUDA)
    layar.blit(label_target, (LEBAR // 2 - label_target.get_width() // 2, 95))

    label_kotak = font_kecil.render("▲ KOTAK (geser dari sini) ▲", True, ABU_MUDA)
    layar.blit(label_kotak, (LEBAR // 2 - label_kotak.get_width() // 2, 450))

    # Gambar kotak
    for kotak in kotak_list:
        kotak.gambar(layar, font_kotak)

    # Petunjuk
    if not menang:
        petunjuk = font_kecil.render("Klik & tahan kotak, lalu geser ke target → R = Reset → ESC = Keluar", True, ABU)
        layar.blit(petunjuk, (LEBAR // 2 - petunjuk.get_width() // 2, 610))
    else:
        # Tampilan menang
        overlay = pygame.Surface((LEBAR, TINGGI), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        layar.blit(overlay, (0, 0))

        menang_teks = font_judul.render("🎉 KAMU MENANG! 🎉", True, KUNING)
        layar.blit(menang_teks, (LEBAR // 2 - menang_teks.get_width() // 2, 280))

        reset_teks = font_normal.render("Tekan R untuk main lagi", True, PUTIH)
        layar.blit(reset_teks, (LEBAR // 2 - reset_teks.get_width() // 2, 350))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
