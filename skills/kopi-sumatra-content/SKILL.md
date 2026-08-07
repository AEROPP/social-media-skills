---
name: kopi-sumatra-content
description: >
  Membuat konten edukasi kopi Sumatra skala tinggi (puluhan hingga 100 video pendek per hari)
  untuk TikTok Studio dan YouTube Shorts, dari riset (penanaman, panen, giling basah, roasting,
  brewing, budaya) menjadi skrip video, shot list footage nyata berlisensi (bukan AI-generated),
  dan metadata upload siap pakai. Gunakan skill ini setiap kali pengguna minta batch skrip/konten
  kopi Sumatra harian, minta ide video edukasi kopi dalam jumlah besar, minta bantuan clipping/
  sourcing footage kopi dari stock berlisensi, atau minta jadwal/metadata upload TikTok & YouTube
  Shorts untuk seri konten kopi — bahkan jika mereka hanya menyebut "bikin video kopi" atau
  "konten edukasi kopi" tanpa menyebut nama skill ini secara eksplisit.
---

# Kopi Sumatra Content — Skill Produksi Konten Edukasi Kopi Skala Tinggi

## Kapan memakai skill ini

Setiap kali diminta membuat/memperluas seri video pendek edukasi kopi Sumatra (dari kebun ke cangkir),
menghasilkan batch skrip harian, mencari/mencocokkan footage B-roll berlisensi untuk topik kopi, atau
menyiapkan metadata upload TikTok Studio / YouTube Shorts untuk seri ini.

**Videonya real-footage berlisensi, bukan AI-generated.** Awalnya pipeline ini dirancang untuk
AI text-to-video bergaya anime, tapi berpindah ke footage nyata (stock berlisensi/CC0/syuting sendiri)
karena AI-generated video terus-menerus jauh lebih mahal di skala 100/hari, sementara clipping video
YouTube orang lain tanpa izin adalah pelanggaran hak cipta & ToS — jangan pernah menyarankan itu.
Lihat `references/sumber-footage-berlisensi.md` untuk detail sumber yang legal.

## Skala saat ini: 10 video/hari (pilot), menuju 100/hari

Operasional dimulai dari **10 video/hari** untuk validasi format sebelum naik ke target 100/hari.
Di skala 10/hari, jumlahnya cukup kecil untuk **disunting manual satu per satu** — termasuk mengoreksi
narator yang kurang cocok dengan pilar (lihat peta keahlian di `content-pillars.md`) dan membedakan
sudut cerita kalau ada pilar yang kebetulan muncul lebih dari sekali dalam sehari. Lihat contoh lengkap
yang sudah disunting di `output/2026-08-07-pilot-10/produksi-10-video.md`. Begitu formatnya terbukti
(retention/engagement bagus di TikTok/YouTube Studio setelah beberapa minggu), naikkan `--count` secara
bertahap — di skala 100/hari, koreksi manual per video sudah tidak realistis lagi, jadi sistem rotasi
otomatis dan overlay grafis generik yang menjaga variasi (lihat `content-pillars.md`).

## Kenapa dibutuhkan sistem rotasi, bukan ditulis manual dari nol

Skill ini memakai sistem rotasi kombinatorial (**Pilar × Format × Kategori Footage × Narator**, 900
kombinasi total) supaya setiap video punya sudut cerita berbeda meski sebagian footage-nya dipakai
ulang. Baca `references/content-pillars.md` untuk detail sistem ini sebelum menulis apa pun — semua
langkah di bawah bergantung padanya.

## Alur kerja

1. **Riset dulu.** Baca `references/riset-kopi-sumatra.md` untuk fakta dasar (geografi, proses giling
   basah khas Sumatra, roasting, brewing, budaya). Kalau pengguna minta angka/statistik terkini
   (harga, volume ekspor, harga lisensi footage terbaru), ingatkan bahwa itu perlu dicek ke sumber
   terbaru — jangan mengarang angka.

2. **Tentukan tanggal & jumlah batch.** Jalankan generator untuk mendapat kerangka hari itu (mulai
   dari `--count 10` di fase pilot):
   ```
   python skills/kopi-sumatra-content/scripts/generate_batch.py --date YYYY-MM-DD --count 10 \
     --out-dir output/YYYY-MM-DD
   ```
   Ini menghasilkan `batch.json` dan `batch.csv` berisi kombinasi pilar/format/kategori-footage/
   narator untuk setiap video, lengkap dengan draft hook, beat isi, CTA, **shot list berisi kata
   kunci pencarian footage** (bukan prompt AI), dan metadata TikTok/YouTube.

3. **Sunting, jangan asal terima mentah-mentah.** Output generator adalah kerangka/first draft yang
   solid secara struktur, tapi baca ulang tiap baris: gabungkan kalimat yang kaku, variasikan
   penyampaian antar video bertetangga (supaya tidak terasa robotic kalau ditonton berurutan), dan
   sesuaikan nada bicara dengan `voice` masing-masing narator (lihat `content-pillars.md`).

4. **Cocokkan shot list ke footage nyata.** Untuk tiap baris di shot list, cari/cocokkan klip dari
   perpustakaan footage berlisensi yang sudah dimiliki, atau sumber baru sesuai
   `references/sumber-footage-berlisensi.md`. Catat sumber & jenis lisensi tiap klip memakai
   `templates/shot-list-footage-template.md` — jangan pernah pakai footage tanpa lisensi yang jelas.

5. **Tambahkan nilai asli, bukan cuma footage + caption.** Setiap video wajib punya minimal satu
   elemen nilai tambah (overlay grafis/data, insight/analisis di narasi, framing edukatif khas) —
   ini bukan sekadar estetika, tapi syarat supaya tidak kena kebijakan "reused content" YouTube/TikTok
   yang bisa membatasi jangkauan atau monetisasi. Lihat bagian terkait di
   `references/platform-guidelines.md`.

6. **Siapkan metadata upload** memakai `templates/metadata-template.md` dan patuhi ketentuan platform
   di `references/platform-guidelines.md`, termasuk menyebar jadwal upload sepanjang hari (bukan
   sekaligus) dan mencatat sumber footage di metadata internal untuk audit.

7. **Kalau diminta otomasi penuh** (sourcing footage → render/edit → upload otomatis), rujuk
   `automation/n8n-workflow-kopi-sumatra.md` di root repo untuk rancangan workflow n8n-nya. Jangan
   asumsikan kredensial API stock-footage atau TikTok/YouTube sudah tersedia — tanyakan dulu ke
   pengguna sebelum mencoba menyambungkan API sungguhan.

## Struktur skill ini

```
kopi-sumatra-content/
├── SKILL.md                              (file ini)
├── references/
│   ├── riset-kopi-sumatra.md             fakta dasar kopi Sumatra (kebun -> cangkir)
│   ├── content-pillars.md                sistem rotasi Pilar x Format x Kategori Footage x Narator
│   ├── sumber-footage-berlisensi.md      sumber footage legal & strategi perpustakaan reusable
│   └── platform-guidelines.md            aturan TikTok Studio & YouTube Shorts + reused-content policy
├── templates/
│   ├── skrip-template.md                 format skrip per video (narasi + shot + overlay)
│   ├── shot-list-footage-template.md     format shot list & pencatatan sumber/lisensi footage
│   └── metadata-template.md              format caption/judul/hashtag/jadwal upload
└── scripts/
    └── generate_batch.py                 generator batch harian (rotasi kombinatorial)
```

## Batasan yang perlu diingat

- Skill ini menghasilkan **skrip, shot list, dan metadata** — bukan file video jadi. Footage nyata
  perlu dicocokkan/diunduh dari sumber berlisensi lalu diedit/disambung (di luar skill ini).
- **Jangan pernah menyarankan mengunduh/clip video YouTube orang lain tanpa lisensi** untuk diupload
  ulang — itu pelanggaran hak cipta & ToS YouTube, terlepas dari seberapa banyak diedit ulang.
- Jangan buat klaim kesehatan/medis tentang kopi, dan hati-hati dengan topik kopi luwak (isu
  kesejahteraan hewan) — lihat bagian "Sensitivitas & Kepatuhan Konten" di
  `references/riset-kopi-sumatra.md`.
- Upload sungguhan ke TikTok/YouTube (baik manual maupun via automation) tetap butuh review manusia
  sebelum publish, terutama di awal seri.
