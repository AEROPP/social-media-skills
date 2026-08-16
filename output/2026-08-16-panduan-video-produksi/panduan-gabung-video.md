# Panduan Menggabungkan Gambar + Narasi + Musik Jadi Video (9:16)

Panduan produksi untuk menyatukan 3 aset yang sudah dibuat jadi video pendek siap upload:

1. **Gambar** — hasil generate dari `output/2026-08-16-prompt-gambar-ai/125-prompt-chatgpt-image.md` (5 gambar per variasi, rasio 9:16, teks sudah ter-render di gambar)
2. **Narasi** — hasil generate voice dari `output/2026-08-16-narasi-ai-voice/25-narasi-ai-voice.md` (1 file audio per variasi)
3. **Musik** — latar musik royalty-free sesuai mood tiap format (lihat pemilihan di bawah)

**Beda dengan pipeline utama di `SKILL.md`:** pipeline utama repo ini pakai footage video CC0 asli.
Alur di panduan ini pakai **gambar diam + AI voice**, jadi outputnya video gaya "slideshow bernarasi"
(Ken Burns/pan-zoom), bukan footage bergerak. Karena gambar & suaranya AI-generated, video hasil
panduan ini **wajib diberi label AI-generated content** saat upload — lihat bagian Kepatuhan di bawah.

---

## Alat yang dipakai

| Kebutuhan | Tool | Kenapa |
|---|---|---|
| Assembly gambar+audio+musik jadi video | **CapCut** (gratis, tanpa watermark) | Sudah jadi rekomendasi utama di `references/tools-produksi.md`, punya fitur "Auto Ken Burns" untuk foto diam, auto-caption, dan music library bawaan |
| Musik latar tambahan (opsional, di luar library CapCut) | **YouTube Audio Library** / **Uppbeat** (free tier) | Royalty-free, aman dipakai komersial, kategori mood lengkap |

Kalau nanti naik skala dan assembly manual di CapCut mulai berat, evaluasi Pictory/InVideo AI seperti
disebut di `references/tools-produksi.md` — keduanya juga bisa terima input gambar + audio custom.

---

## Langkah 1 — Siapkan file per variasi

Untuk tiap variasi (mis. Judul 1 / V1), kumpulkan dalam satu folder:
```
judul1-v1/
├── slide1.png ... slide5.png     (dari prompt gambar, urutkan sesuai nomor)
└── narasi.mp3                     (hasil generate ElevenLabs dari naskah V1)
```
Beri nama file berurutan (`slide1.png`, `slide2.png`, dst.) supaya gampang di-drag ke timeline sesuai
urutan hook → isi → isi → isi → CTA.

## Langkah 2 — Generate audio narasi

1. Buka ElevenLabs, buat/gunakan 1 voice tersimpan per narator (Pak Bahri, Kak Nur, Adit) — jangan
   pilih voice acak tiap kali, biar suara konsisten antar video (lihat `references/tools-produksi.md`).
2. Tempel naskah narasi 1 variasi penuh (5 baris + jeda) dari `25-narasi-ai-voice.md` ke ElevenLabs.
3. Kalau tool-nya mendukung SSML, ganti `(jeda)` → `<break time="500ms" />` dan `(jeda panjang)` →
   `<break time="1200ms" />` supaya jeda antar poin lebih presisi dan mudah disinkronkan ke gambar.
4. Export sebagai satu file audio utuh (`narasi.mp3`) per variasi — bukan 5 file terpisah, supaya lebih
   mudah di-drop sebagai satu track di CapCut.

## Langkah 3 — Susun timeline di CapCut

1. **Import** kelima gambar + file audio narasi ke media panel CapCut.
2. **Drag audio narasi** ke track audio utama dulu — ini jadi acuan panjang total video.
3. **Drag kelima gambar** ke track video secara berurutan (slide1 → slide5), sejajarkan di atas track
   audio.
4. **Tentukan durasi tiap gambar** dengan dengar audio narasi dan tandai waktu tiap kalimat berganti
   (biasanya di titik `(jeda)`), lalu potong/perpanjang tiap klip gambar supaya transisinya jatuh
   tepat saat narasi pindah ke poin berikutnya. Contoh alokasi untuk video ~18 detik (Judul 1/V1):

   | Slide | Narasi | Perkiraan durasi |
   |---|---|---|
   | 1 (hook) | "Kopi Sumatra sama dengan kopi luwak? Big no." | 0:00–0:03 |
   | 2 | "Banyak yang salah kaprah..." | 0:03–0:07 |
   | 3 | "Faktanya, 99% kopi Sumatra..." | 0:07–0:11 |
   | 4 | "Proses inilah yang bikin rasanya earthy..." | 0:11–0:15 |
   | 5 (CTA) | "Follow biar kamu nggak salah kaprah..." | 0:15–0:18 |

   Sesuaikan angka ini ke kecepatan bicara voice yang kamu pakai — jangan asumsikan sama persis, selalu
   cocokkan sambil dengar audio asli.
5. **Aktifkan "Auto Ken Burns"** (atau animasi pan/zoom manual) di tiap klip gambar supaya foto diam
   terasa hidup, bukan statis kaku. Arah pan boleh bervariasi antar slide (zoom-in di hook, pan
   horizontal di isi) biar tidak monoton.
6. **Transisi antar slide**: pakai cut sederhana atau crossfade singkat (0.2–0.3 detik) — hindari
   transisi flashy yang mengganggu keterbacaan teks di gambar.

## Langkah 4 — Tambahkan musik latar

1. Pilih musik sesuai mood format:
   - **Mitos vs fakta / fakta cepat / versus** (Judul 1, 2, 3, 5 V1-V4): musik upbeat ringan, tempo
     sedang, tanpa lirik (kategori "corporate/inspiring" di library musik).
   - **ASMR/satisfying** (Judul 4 V1 & V5): musik ambient/lo-fi minimal beat, volume sangat rendah —
     prioritaskan suara asli tuangan/tarikan kopi kalau ada rekaman aslinya, musik hanya pelengkap.
   - **Reflektif/emosional** (Judul 5 V3 & V5): musik acoustic/piano pelan, hindari musik ceria yang
     kontras dengan nada cerita.
2. **Drop musik ke track terpisah di bawah narasi**, lalu turunkan volumenya jadi **-15 sampai -20 dB**
   relatif terhadap narasi — musik harus terdengar tapi tidak menutupi suara narator.
3. **Fade in** musik di 0.5 detik pertama dan **fade out** di 0.5–1 detik terakhir supaya tidak
   terpotong kasar.
4. Kalau CapCut minta atribusi untuk lagu tertentu dari library-nya, cek ketentuan lisensinya dulu
   sebelum upload — sebagian lagu di library gratis tetap butuh kredit di caption.

## Langkah 5 — Caption/teks tambahan (opsional tapi disarankan)

Teks utama sudah ter-render di tiap gambar (dari prompt gambar AI), jadi caption burned-in dari CapCut
**tidak wajib**. Tapi tetap disarankan menyalakan **auto-caption dari audio** dengan ukuran font kecil
di posisi berbeda dari teks utama gambar (mis. teks gambar di tengah, auto-caption kecil di bawah) —
ini membantu penonton yang menonton tanpa suara sekaligus menegaskan isi untuk aksesibilitas.

## Langkah 6 — Export

- Rasio: **9:16**, resolusi **1080×1920**, minimal 30fps.
- Durasi total mengikuti panjang narasi (target keseluruhan **15–30 detik** sesuai
  `references/platform-guidelines.md`).
- Format: **MP4 (H.264)**.
- Cek preview penuh sekali lagi: pastikan transisi gambar pas dengan jeda narasi, musik tidak
  menenggelamkan suara, dan teks di gambar tetap terbaca penuh (tidak terpotong crop/transisi).

---

## Kepatuhan sebelum upload

- **Wajib nyalakan label "AI-generated content"** (TikTok) / toggle **"Altered or synthetic content"**
  (YouTube Shorts) — video ini pakai gambar AI dan voice AI, beda dari pipeline utama footage nyata di
  `SKILL.md`. Lihat detail di `references/platform-guidelines.md`.
- Isi metadata upload (caption, hashtag, jadwal) memakai `templates/metadata-template.md`, dan catat di
  kolom "Sumber footage/aset" bahwa gambar & audio dihasilkan AI (bukan CC0), untuk kebutuhan audit
  internal.
- Review manusia tetap wajib sebelum publish tiap video, terutama cek hasil render teks di gambar
  (kadang AI image generation salah eja) dan kejelasan pengucapan AI voice.

## Checklist cepat per video

- [ ] 5 gambar sudah di-generate & di-cek teksnya benar (tidak typo/terpotong)
- [ ] Audio narasi sudah di-generate dengan voice narator yang konsisten
- [ ] Timeline tersusun, durasi tiap slide sinkron dengan jeda narasi
- [ ] Ken Burns/animasi pan-zoom aktif di semua slide
- [ ] Musik latar terpasang, volume di-duck di bawah narasi, fade in/out halus
- [ ] Auto-caption dari audio aktif (opsional tapi disarankan)
- [ ] Export 9:16, 1080×1920, MP4
- [ ] Label AI-generated content dinyalakan sebelum upload
- [ ] Metadata & jadwal upload sudah diisi sesuai template
