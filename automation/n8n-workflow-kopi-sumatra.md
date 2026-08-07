# Rancangan Otomasi n8n — Kopi Sumatra Content Pipeline (Real-Footage)

Dokumen ini merancang alur otomasi dari "generate batch harian" sampai "upload ke TikTok & YouTube
Shorts", memakai **footage nyata berlisensi** (bukan AI text-to-video). Skeleton workflow yang bisa
diimpor ke n8n ada di `workflow-kopi-sumatra.json` (satu folder ini) — semua node yang butuh API
eksternal sengaja **dinonaktifkan (disabled)** dan diberi sticky note karena belum ada kredensial/
keputusan sumber footage dari pengguna. Jangan aktifkan node tersebut sebelum langkah "Yang harus
disiapkan dulu" di bawah selesai.

## Baca ini dulu: batasan nyata sebelum berharap "100 video/hari full-otomatis"

Sumber footage yang dipakai sekarang adalah **CC0/Public Domain (Pexels & Pixabay)**, jadi tidak ada
batas unduhan bulanan atau batas tayang per video seperti Shutterstock — dua kendala itu tidak
berlaku di setup ini. Yang tetap berlaku:

1. **Rate limit API Pexels/Pixabay.** Gratis, tapi ada batas request/jam per API key. Di skala
   100 video/hari (±200-300 pencarian/hari) umumnya masih di bawah limit, tapi node pencarian tetap
   perlu retry/backoff dan idealnya menyertakan atribusi ke Pexels/fotografer untuk melonggarkan
   limit kalau dibutuhkan.
2. **Wikimedia Commons/rilisan pemerintah (kalau dipakai sesekali untuk klip spesifik Sumatra)**
   punya lisensi bervariasi per file (CC0/CC-BY/CC-BY-SA) — **jangan otomasi pengambilan dari sumber
   ini**, tetap perlu dicek manual satu per satu sebelum masuk katalog (lihat
   `skills/kopi-sumatra-content/references/sumber-footage-berlisensi.md`).
3. **Kuota API upload TikTok/YouTube tetap berlaku**, tidak berubah oleh sumber footage:
   - **YouTube Data API v3**: kuota default 10.000 unit/hari, `videos.insert` menghabiskan ~1.600
     unit → hanya ±6 upload/hari lewat API tanpa quota increase request.
   - **TikTok Content Posting API**: butuh app review; sebelum lolos, hanya boleh posting
     draft/private ke akun test.

**Implikasi**: fase awal realistisnya berhenti di "generate skrip + shot list + cocokkan footage +
render/edit", sedangkan **upload final tetap manual** lewat TikTok Studio & YouTube Studio sampai
kuota/akses API di atas benar-benar disetujui.

## Arsitektur

```mermaid
flowchart TD
    A[Schedule Trigger - tiap hari 05:00 WIB] --> B[Code: Generate 100 Kombinasi<br/>Pilar x Format x Kategori Footage x Narator]
    B --> C[Loop Over Items - rate limit]
    C --> D[Cari/Cocokkan Footage ke Perpustakaan Internal]
    D --> E{Klip cocok sudah ada?}
    E -- Belum --> F[HTTP Request: Cari Footage Baru<br/>DISABLED - Pexels/Pixabay API]
    E -- Sudah --> G[Generate Voiceover TTS]
    F --> G
    G --> H[Stitch Klip and Overlay Grafis and Caption<br/>DISABLED - butuh servis edit]
    H --> I{Kuota/akses API upload tersedia?}
    I -- Belum --> J[Simpan ke Storage and Log untuk upload manual]
    I -- Sudah --> K[HTTP Request: Upload TikTok<br/>DISABLED]
    I -- Sudah --> L[HTTP Request: Upload YouTube Shorts<br/>DISABLED]
    K --> M[Log Episode + Sumber Footage + Lisensi]
    L --> M
    J --> M
```

## Detail tiap tahap

1. **Schedule Trigger** — jalan sekali sehari (mis. 05:00 WIB) supaya cocokkan footage & edit sempat
   selesai sebelum jadwal upload pertama jam 06:00.

2. **Code: Generate 100 Kombinasi** — port JavaScript dari logika rotasi di
   `skills/kopi-sumatra-content/scripts/generate_batch.py` (pilar × format × kategori-footage ×
   narator, rotasi berbasis tanggal), menghasilkan hook/beat/CTA + shot list berisi **kata kunci
   pencarian footage** (bukan prompt AI).

3. **Loop Over Items (rate limit)** — proses satu video per iterasi.

4. **Cari/Cocokkan Footage ke Perpustakaan Internal** — cek dulu apakah kata kunci shot cocok dengan
   klip yang sudah dimiliki (mis. lookup ke Google Sheet/Airtable berisi katalog footage internal
   dengan tag kata kunci). Ini langkah kunci supaya **tidak** membeli klip baru tiap video.

5. **Cari Footage Baru (kalau belum ada yang cocok)** — panggil Pexels API atau Pixabay API (gratis,
   perlu API key) memakai kata kunci dari shot list. Hasil baru ini ditambahkan ke katalog
   perpustakaan internal supaya bisa dipakai ulang video-video berikutnya, bukan dicari ulang tiap
   kali.

6. **Generate Voiceover (TTS)** — panggil API text-to-speech (mis. ElevenLabs) dari naskah
   hook/beat/CTA. Biaya kecil per video (lihat `automation/estimasi-biaya-produksi.md`).

7. **Stitch Klip + Overlay + Caption** — n8n sendiri tidak punya kemampuan native edit video; butuh
   layanan eksternal (Shotstack, Creatomate, atau microservice ffmpeg sendiri) untuk menyambung
   2-3 klip B-roll + voiceover + caption burned-in + **overlay grafis/data** (wajib, lihat catatan
   reused-content di `references/platform-guidelines.md`).

8. **Cabang kuota**: selama akses upload API belum disetujui, video hasil disimpan ke storage
   (Google Drive/S3) dan dicatat di spreadsheet supaya tim bisa upload manual dengan metadata yang
   sudah disiapkan otomatis (lihat `templates/metadata-template.md`).

9. **Log Episode** — catat setiap episode (index, pilar, format, kategori footage, narator, ID klip
   yang dipakai + sumbernya (Pexels/Pixabay/Wikimedia), status upload, link video) ke Google
   Sheet/Airtable — berguna untuk audit atribusi kalau suatu saat dibutuhkan.

## Yang harus disiapkan dulu sebelum node API diaktifkan

- [ ] Bangun katalog awal perpustakaan footage dari Pexels & Pixabay (lihat
      `skills/kopi-sumatra-content/references/sumber-footage-berlisensi.md`) — cukup untuk mulai,
      upgrade ke Shutterstock/footage sendiri belakangan kalau dibutuhkan.
- [ ] Siapkan spreadsheet/database katalog footage (kata kunci, sumber, link asal, tanggal pakai
      terakhir) untuk lookup di node "Cari/Cocokkan Footage ke Perpustakaan Internal".
- [ ] Daftar API key Pexels & Pixabay (gratis).
- [ ] Pilih & daftar API TTS (ElevenLabs atau alternatif) + API key.
- [ ] Pilih layanan stitching/video-editing (atau bangun microservice ffmpeg sendiri).
- [ ] Daftarkan aplikasi TikTok for Developers, lalui app review, siapkan OAuth per akun TikTok.
- [ ] Daftarkan project Google Cloud, aktifkan YouTube Data API v3, siapkan OAuth, dan ajukan
      quota increase kalau target benar-benar >6 upload/hari lewat API.
- [ ] Siapkan storage (Drive/S3) + spreadsheet log untuk fase transisi sebelum upload API aktif.

Setelah semua ini siap dan pengguna mengonfirmasi kredensialnya, workflow di `workflow-kopi-sumatra.json`
bisa diimpor ke n8n dan node-node yang relevan tinggal diaktifkan + diisi kredensialnya satu per satu.
