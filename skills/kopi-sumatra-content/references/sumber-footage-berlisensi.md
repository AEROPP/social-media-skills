# Sumber Footage Berlisensi (Real-Footage, bukan AI-Generated)

Pipeline ini memakai **footage video nyata** (bukan AI text-to-video) yang diedit/dipotong-potong
(clipping) menjadi video pendek. Karena sumbernya rekaman asli, dua hal wajib dipastikan sebelum
sebuah klip dipakai: **(1) lisensinya legal** dan **(2) videonya tetap punya nilai tambah asli**
supaya tidak kena kebijakan "reused content" TikTok/YouTube. Jangan pernah mengunduh video YouTube
orang lain lalu upload ulang tanpa lisensi — itu pelanggaran hak cipta dan ToS YouTube, terlepas dari
seberapa banyak diedit ulang.

## Tiga jalur sumber yang legal

### A. Footage bebas lisensi (CC0 / Public Domain) — termurah

- **Pexels Videos, Pixabay Videos** — koleksi video gratis, boleh dipakai komersial tanpa atribusi
  wajib (cek lisensi tepatnya di tiap platform, umumnya CC0-like).
- **Wikimedia Commons** — sebagian video berlisensi CC-BY (butuh atribusi) atau public domain.
- **Rilisan dinas pariwisata** — Kemenparekraf, Dinas Pariwisata Aceh/Sumatera Utara kadang merilis
  video promosi daerah dengan lisensi bebas pakai untuk promosi non-komersial/komersial (cek syarat
  tiap rilisan, sering minta atribusi ke sumber daerah).
- **Kelebihan**: $0, tidak ada batas tayang, bisa dipakai ulang tanpa batas.
- **Kekurangan**: pilihan sangat generik ("kebun kopi" umum, bukan spesifik "kebun Gayo giling basah"),
  kualitas/relevansi bervariasi, dan klip yang sama mungkin dipakai kreator lain juga (kurang unik).

### B. Footage berlisensi (Shutterstock, dsb.) — lebih spesifik & berkualitas

- Video subscription mulai **$59/bulan untuk 5 video/bulan** hingga **$119/bulan untuk 20 video/bulan**
  (jatah tidak bisa ditabung ke bulan berikutnya). Paket on-demand tahunan (5/10/25 klip) juga tersedia.
- Harga on-demand per klip standalone sekitar **$8.32-$9.95/klip** (lebih murah per klip kalau beli
  paket besar/tahunan).
- **Standard License**: royalty-free, boleh dipakai berkali-kali di banyak video (bukan sekali pakai),
  TAPI ada **batas 500.000 tayangan per video** untuk penggunaan di platform seperti YouTube, dan
  proyek broadcast/TV punya batas budget produksi $10.000. Kalau sebuah video berpotensi viral jauh
  di atas 500rb views, klip Standard-nya idealnya di-upgrade ke **Enhanced License** (indemnifikasi
  $250.000, tanpa batas tayang seketat itu).
- **Kelebihan**: pilihan lebih spesifik & kualitas tinggi (drone kebun, close-up giling basah, dll).
- **Kekurangan**: jatah unduhan bulanan kecil dibanding kebutuhan 100 video/hari — lihat strategi
  "bangun perpustakaan footage" di bawah, dan tetap harus memantau video mana yang mendekati 500rb
  views agar lisensinya di-upgrade.

### C. Footage sendiri / kerja sama resmi — paling otentik & sustainable jangka panjang

- Rekam sendiri atau sewa videografer lokal di Aceh/Sumatera Utara untuk syuting sehari di kebun,
  rumah giling, dan warung kopi — hasil beberapa jam syuting bisa dipecah jadi puluhan klip B-roll
  yang **dimiliki penuh** (tidak ada batas lisensi/views sama sekali).
- Kerja sama dengan kreator YouTube/kebun kopi Sumatra yang sudah punya konten — minta izin tertulis
  untuk memakai/me-repurpose sebagian footage mereka (kredit + kompensasi sesuai kesepakatan).
- **Kelebihan**: paling otentik (benar-benar Gayo/Lintong/Mandailing, bukan stok generik), tidak ada
  batas views/lisensi, jadi aset jangka panjang.
- **Kekurangan**: butuh koordinasi lapangan & biaya syuting di muka (bukan biaya per video).

## Insight ekonomi penting: bangun PERPUSTAKAAN footage, jangan beli per video

Lisensi royalty-free (jalur A & B) **boleh dipakai berulang kali di banyak video** — bukan sekali
pakai lalu habis. Artinya strategi paling efisien untuk 100 video/hari **bukan** membeli/mengunduh
klip baru untuk tiap video, melainkan:

1. Bangun perpustakaan awal berisi ~100-150 klip B-roll yang mencakup semua kombinasi
   pilar × setting di `content-pillars.md` (kebun pagi berkabut, tangan memetik ceri, mesin giling
   basah, drum roasting, seduhan kopi tarik Aceh, suasana warung kopi, dst).
2. Tandai tiap klip dengan kata kunci pilar/setting di `templates/shot-list-footage-template.md`
   supaya generator (`generate_batch.py`) bisa mencocokkan shot yang dibutuhkan tiap video dengan
   klip yang sudah dimiliki, alih-alih mencari/beli baru tiap kali.
3. **Yang membuat 100 video/hari tetap terasa berbeda satu sama lain bukan footage-nya** (boleh
   dipakai ulang), **melainkan naskah, sudut cerita, dan overlay grafis/data** yang berbeda tiap
   video — inilah kenapa sistem rotasi pilar/format/fakta di `content-pillars.md` tetap krusial.
4. Refresh perpustakaan secara berkala (mis. tambah 20-30 klip baru tiap 1-2 bulan) supaya visual
   tidak terasa itu-itu saja bagi penonton setia.

Ini mengubah biaya footage dari "biaya per video yang terus bertambah" menjadi **investasi awal +
biaya refresh berkala** — jauh lebih murah dalam jangka panjang dibanding generate ulang tiap video
lewat AI. Detail angka ada di `automation/estimasi-biaya-produksi.md`.

## Checklist sebelum sebuah klip dipakai

- [ ] Sumber & jenis lisensi dicatat (CC0 / Shutterstock Standard / Shutterstock Enhanced / footage
      sendiri) — simpan di log (lihat `templates/shot-list-footage-template.md`).
- [ ] Kalau Shutterstock Standard: video yang memakainya dipantau, upgrade ke Enhanced sebelum
      tayangan mendekati 500.000.
- [ ] Kalau footage berlisensi CC-BY: atribusi disertakan sesuai syarat lisensinya.
- [ ] Video punya nilai tambah asli (narasi/insight/grafis unik) — bukan sekadar footage + caption,
      supaya lolos kebijakan reused-content YouTube & tidak diturunkan jangkauannya di TikTok (lihat
      `references/platform-guidelines.md`).
