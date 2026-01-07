import os
import subprocess

# --- KONFIGURASI ---
output_folder = "assets"  # Folder hasil akan disimpan di sini
# -------------------

# Buat folder output jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Ambil lokasi folder saat ini
current_path = os.getcwd()
files = [f for f in os.listdir(current_path) if f.endswith((".mp4", ".MOV", ".mkv"))]

print(f"Ditemukan {len(files)} video. Memulai proses...\n")

for filename in files:
    # 1. Bersihkan Nama File (Ganti Spasi dengan _)
    clean_name = filename.replace(" ", "_")
    
    input_path = os.path.join(current_path, filename)
    output_path = os.path.join(output_folder, clean_name)

    print(f"Processing: {filename} -> {clean_name}...")

    # 2. Perintah FFmpeg
    # -c:v libx264 : Gunakan codec H.264 (Wajib untuk web)
    # -preset fast : Convert cepat (gunakan 'medium' atau 'slow' untuk kompresi lebih baik tapi lama)
    # -crf 23      : Kualitas (makin kecil makin bagus, standar web 23-28)
    # -movflags +faststart : AGAR VIDEO BISA BUFFERING (Penting untuk web!)
    # -an          : Hapus audio (Opsional, hapus '# ' di baris cmd jika ingin ada suara)
    
    cmd = [
        "ffmpeg", "-i", input_path,
        "-c:v", "libx264",
        "-preset", "fast", 
        "-crf", "23",
        "-c:a", "aac",        # Audio codec (biarkan ada suara)
        "-movflags", "+faststart",
        "-y",                 # Overwrite jika ada file sama
        output_path
    ]

    # Jalankan perintah tanpa memunculkan window baru
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

print(f"\n✅ SELESAI! Cek folder '{output_folder}'.")