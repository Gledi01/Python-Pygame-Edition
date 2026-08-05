# Folder Assets

Di sini kamu bisa taruh file gambar (`.png`, `.jpg`) atau suara (`.wav`, `.ogg`) untuk dipakai di game.

## Cara memakai gambar di Pygame:

```python
gambar = pygame.image.load("assets/nama_file.png")
gambar = pygame.transform.scale(gambar, (lebar, tinggi))  # opsional resize
layar.blit(gambar, (x, y))
```

Untuk tutorial ini, kita buat gambar langsung dengan kode (Surface) supaya tidak perlu file eksternal.
