import sys
import pygame

# 1. Inisialisasi Pygame
pygame.init()
pygame.mixer.init()  # Inisialisasi modul audio untuk suara/musik

# 2. Pengaturan Layar (Window)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Contoh Load PNG dan Audio di Pygame")

# 3. Pengaturan Warna dan Waktu
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

# ==========================================
# 4. LOAD GAMBAR PNG & AUDIO
# ==========================================

try:
  # Load gambar PNG dengan alpha channel (transparansi) menggunakan convert_alpha()
  player_image = pygame.image.load("player.png").convert_alpha()

  # Mengubah ukuran gambar jika diperlukan (misal: 64x64 piksel)
  player_image = pygame.transform.scale(player_image, (64, 64))

  # Load musik latar belakang (biasanya format OGG atau MP3 untuk file besar)
  pygame.mixer.music.load("background.ogg")
  pygame.mixer.music.set_volume(
      0.5
  )  # Mengatur volume musik (0.0 sampai 1.0)

  # Load efek suara (biasanya format WAV untuk durasi pendek)
  jump_sound = pygame.mixer.Sound("jump.wav")
  jump_sound.set_volume(0.8)  # Mengatur volume efek suara

except pygame.error as e:
  print(
      "Gagal memuat asset! Pastikan file player.png, background.ogg, dan"
      " jump.wav tersedia."
  )
  print(f"Error: {e}")
  pygame.quit()
  sys.exit()

# Posisi awal karakter di layar
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Memulai pemutaran musik latar secara berulang (-1 artinya loop terus-menerus)
pygame.mixer.music.play(-1)

# ==========================================
# 5. GAME LOOP UTAMA
# ==========================================
running = True
while running:
  # --- Event Handling (Input Pengguna) ---
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # Deteksi tombol keyboard ditekan
    elif event.type == pygame.KEYDOWN:
      # Contoh: Tekan tombol Spasi untuk memutar efek suara lompat
      if event.key == pygame.K_SPACE:
        jump_sound.play()

  # --- Kontrol Pergerakan Karakter ---
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    player_x -= player_speed
  if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    player_x += player_speed
  if keys[pygame.K_UP] or keys[pygame.K_w]:
    player_y -= player_speed
  if keys[pygame.K_DOWN] or keys[pygame.K_s]:
    player_y += player_speed

  # --- Render / Menggambar ke Layar ---
  # 1. Bersihkan layar dengan warna putih (atau warna latar belakang lain)
  screen.fill(WHITE)

  # 2. Gambar aset PNG ke posisi (player_x, player_y)
  screen.blit(player_image, (player_x, player_y))

  # 3. Perbarui tampilan layar
  pygame.display.flip()

  # --- Batasi Frame Rate (FPS) ---
  clock.tick(60)

# 6. Keluar dari Pygame dengan bersih
pygame.quit()
sys.exit()
