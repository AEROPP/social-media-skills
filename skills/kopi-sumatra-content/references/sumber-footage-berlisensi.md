# Sumber Footage Berlisensi (Real-Footage, bukan AI-Generated)

Pipeline ini memakai **footage video nyata** (bukan AI text-to-video) yang diedit/dipotong-potong
(clipping) menjadi video pendek. Karena sumbernya rekaman asli, dua hal wajib dipastikan sebelum
sebuah klip dipakai: **(1) lisensinya legal** dan **(2) videonya tetap punya nilai tambah asli**
supaya tidak kena kebijakan "reused content" TikTok/YouTube. Jangan pernah mengunduh video YouTube
orang lain lalu upload ulang tanpa lisensi — itu pelanggaran hak cipta dan ToS YouTube, terlepas dari
seberapa banyak diedit ulang.

**Keputusan saat ini: pakai jalur CC0/Public Domain (Jalur A) sebagai sumber utama.** $0 biaya
lisensi, tanpa batas tayang, dan cukup untuk memvalidasi format konten. Jalur B (Shutterstock) dan
C (syuting sendiri) tetap didokumentasikan di bagian bawah sebagai upgrade kalau nanti dibutuhkan
visual yang lebih spesifik/otentik.

## Jalur A (aktif): Footage CC0 / Public Domain

| Sumber | Lisensi | Komersial? | Atribusi? | Catatan |
|---|---|---|---|---|
| **Pexels Videos** (+ API) | Pexels License | Ya | Tidak wajib (disarankan) | Tidak boleh dijual mentah/tanpa modifikasi, tidak boleh untuk platform stock saingan, tidak boleh menyiratkan endorsement. API gratis, ada rate limit — attribusi ke Pexels/fotografer bisa melonggarkan limit. |
| **Pixabay Videos** (+ API) | Pixabay Content License | Ya | Tidak wajib | Sama seperti Pexels: tidak boleh dijual ulang mentah/standalone, tidak boleh menyiratkan endorsement. Konten dari sebelum 2019 malah CC0 murni. |
| **Wikimedia Commons** | Bervariasi (CC0, CC-BY, CC-BY-SA) | Tergantung lisensi tiap file | **Wajib untuk CC-BY/CC-BY-SA** | Hati-hati: CC-BY-SA mewajibkan hasil turunan ikut lisensi share-alike yang sama — sebaiknya **hindari** CC-BY-SA untuk konten komersial berulang kecuali sudah paham konsekuensinya. Cek lisensi tiap file satu-satu, jangan asumsikan CC0. |
| **Rilisan dinas pariwisata** (Kemenparekraf, Pemda Aceh/Sumut) | Bervariasi per rilisan | Sering ya, kadang non-komersial saja | Sering diminta | Paling berpotensi punya visual spesifik Sumatra, tapi syarat lisensi harus dicek satu per satu per rilisan — jangan diasumsikan bebas pakai penuh. |

**Cara pakai praktis**: prioritaskan Pexels & Pixabay (lisensi paling jelas, tanpa atribusi wajib,
API gratis untuk otomasi). Pakai Wikimedia Commons/rilisan pemerintah hanya untuk klip yang benar-
benar dibutuhkan spesifik Sumatra dan lisensinya sudah dicek manual + atribusi disiapkan bila perlu.

**Trade-off yang harus diterima**: pilihan visual generik ("dataran tinggi berkabut", "tangan
memetik ceri kopi") — kemungkinan besar bukan benar-benar difilmkan di Gayo/Lintong/Mandailing,
melainkan lokasi kopi lain (Amerika Latin, Afrika, Vietnam, dll.) yang terlihat mirip secara visual.
Ini memengaruhi:
- **Keaslian/kredibilitas visual** — kalau ada penonton yang jeli, footage-nya mungkin dikenali
  bukan dari Sumatra. Mitigasi: jangan klaim "ini benar-benar kebun di Gayo" dalam narasi kalau
  footage-nya generik — fokuskan klaim spesifik pada fakta (yang memang akurat), bukan pada visual.
- **Risiko reused-content lebih tinggi** — footage CC0 dipakai banyak kreator lain juga, jadi
  overlay grafis/data dan narasi orisinal (lihat `references/platform-guidelines.md`) menjadi
  **lebih penting**, bukan pelengkap opsional.
- **Waktu kurasi lebih lama** — katalog CC0 kurang tertag rapi dibanding stock berbayar, jadi
  mencari klip yang benar-benar cocok per shot butuh waktu manual lebih banyak (sudah dihitung di
  estimasi biaya sebagai tambahan jam review).

## Jalur B & C (opsi upgrade nanti, belum dipakai)

### B. Shutterstock (berlisensi, lebih spesifik & berkualitas)
Video subscription $59-119/bulan (5-20 klip/bulan) atau on-demand $8.32-9.95/klip. Standard License
punya batas 500.000 views/video (upgrade ke Enhanced kalau viral). Pertimbangkan ini kalau setelah
beberapa minggu memakai CC0, terasa footage-nya terlalu generik/berulang dan channel sudah punya
traksi yang layak diinvestasikan.

### C. Syuting sendiri / kerja sama resmi (paling otentik jangka panjang)
Sewa videografer lokal Aceh/Sumut (~Rp 3-6 juta sekali syuting) untuk footage yang benar-benar
otentik dan dimiliki penuh, tanpa batas lisensi/views. Opsi terbaik kalau channel sudah terbukti dan
ingin membedakan diri dari kreator lain yang sama-sama pakai stock CC0 generik.

## Insight ekonomi: bangun PERPUSTAKAAN footage, jangan cari ulang tiap video

Footage CC0 tetap perlu dikurasi jadi **perpustakaan internal terorganisir**, bukan dicari ulang
dari nol tiap video:

1. Bangun katalog awal ~100-150 klip B-roll yang mencakup semua kategori footage di
   `content-pillars.md` (kebun berkabut, tangan memetik ceri, mesin giling, drum roasting, seduhan
   kopi, suasana warung kopi, dst) — sekali kurasi, simpan link/file + kata kunci taggingnya.
2. Tandai tiap klip dengan kata kunci pilar/kategori di `templates/shot-list-footage-template.md`
   supaya generator (`generate_batch.py`) bisa mencocokkan shot yang dibutuhkan tiap video dengan
   klip yang sudah dikurasi, alih-alih mencari ulang tiap kali.
3. **Yang membuat 100 video/hari tetap terasa berbeda satu sama lain bukan footage-nya** (boleh
   dipakai ulang berkali-kali, gratis), **melainkan naskah, sudut cerita, dan overlay grafis/data**
   yang berbeda tiap video — inilah kenapa sistem rotasi pilar/format/fakta di `content-pillars.md`
   tetap krusial, dan kenapa nilai tambah asli makin penting saat visualnya generik.
4. Refresh katalog secara berkala (mis. tambah 20-30 klip baru tiap 1-2 bulan dari rilisan
   Pexels/Pixabay terbaru) supaya visual tidak terasa itu-itu saja bagi penonton setia.

Detail angka biaya ada di `automation/estimasi-biaya-produksi.md`.

## Checklist sebelum sebuah klip dipakai

- [ ] Sumber & jenis lisensi dicatat (Pexels / Pixabay / Wikimedia CC-BY / rilisan pemerintah) —
      simpan di log (lihat `templates/shot-list-footage-template.md`).
- [ ] Kalau memakai Wikimedia Commons CC-BY/CC-BY-SA: atribusi disertakan sesuai syarat lisensinya,
      dan CC-BY-SA dihindari kecuali benar-benar diperlukan.
- [ ] Klip tidak dijual mentah/standalone dan tidak menyiratkan endorsement merek/orang tertentu
      (syarat umum Pexels & Pixabay).
- [ ] Video punya nilai tambah asli (narasi/insight/grafis unik) — bukan sekadar footage + caption,
      supaya lolos kebijakan reused-content YouTube & tidak diturunkan jangkauannya di TikTok (lihat
      `references/platform-guidelines.md`). Ini **lebih penting** saat footage-nya CC0 generik.
