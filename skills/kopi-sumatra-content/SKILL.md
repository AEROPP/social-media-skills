---
name: kopi-sumatra-content
description: >
  Membuat konten edukasi kopi Sumatra skala tinggi (puluhan hingga 100 video pendek per hari)
  untuk TikTok Studio dan YouTube Shorts, dari riset (penanaman, panen, giling basah, roasting,
  brewing, budaya) menjadi skrip video, prompt AI text-to-video bergaya anime/cartoon, dan metadata
  upload siap pakai. Gunakan skill ini setiap kali pengguna minta batch skrip/konten kopi Sumatra
  harian, minta ide video edukasi kopi dalam jumlah besar, minta prompt video AI bergaya
  anime/cartoon untuk topik kopi, atau minta jadwal/metadata upload TikTok & YouTube Shorts untuk
  seri konten kopi — bahkan jika mereka hanya menyebut "bikin video kopi" atau "konten edukasi kopi"
  tanpa menyebut nama skill ini secara eksplisit.
---

# Kopi Sumatra Content — Skill Produksi Konten Edukasi Kopi Skala Tinggi

## Kapan memakai skill ini

Setiap kali diminta membuat/memperluas seri video pendek edukasi kopi Sumatra (dari kebun ke cangkir),
menghasilkan batch skrip harian, menulis prompt text-to-video bergaya anime/cartoon untuk topik kopi,
atau menyiapkan metadata upload TikTok Studio / YouTube Shorts untuk seri ini.

## Kenapa dibutuhkan sistem, bukan ditulis manual

100 video/hari tidak bisa ditulis satu-satu secara manual dan tetap konsisten. Skill ini memakai sistem
rotasi kombinatorial (**Pilar × Format × Setting × Host**, 900 kombinasi total) supaya setiap video
punya sudut berbeda, tetap dalam satu identitas visual/naratif yang sama, dan tidak berulang persis
selama berhari-hari. Baca `references/content-pillars.md` untuk detail sistem ini sebelum menulis
apa pun — semua langkah di bawah bergantung padanya.

## Alur kerja

1. **Riset dulu.** Baca `references/riset-kopi-sumatra.md` untuk fakta dasar (geografi, proses giling
   basah khas Sumatra, roasting, brewing, budaya). Kalau pengguna minta angka/statistik terkini
   (harga, volume ekspor), ingatkan bahwa itu perlu dicek ke sumber terbaru — jangan mengarang angka.

2. **Tentukan tanggal & jumlah batch.** Jalankan generator untuk mendapat kerangka hari itu:
   ```
   python skills/kopi-sumatra-content/scripts/generate_batch.py --date YYYY-MM-DD --count 100 \
     --out-dir output/YYYY-MM-DD
   ```
   Ini menghasilkan `batch.json` dan `batch.csv` berisi kombinasi pilar/format/setting/host untuk
   setiap video, lengkap dengan draft hook, beat isi, CTA, prompt video per shot, dan metadata
   TikTok/YouTube — semuanya sudah terisi otomatis dari bank fakta di `references/`.

3. **Sunting, jangan asal terima mentah-mentah.** Output generator adalah kerangka/first draft yang
   solid secara struktur, tapi baca ulang tiap baris: gabungkan kalimat yang kaku, variasikan
   penyampaian antar video bertetangga (supaya tidak terasa robotic kalau ditonton berurutan), dan
   sesuaikan nada bicara dengan `voice` masing-masing host (lihat `content-pillars.md`).

4. **Lengkapi visual dengan panduan gaya.** Saat menuliskan/menyempurnakan prompt video, ikuti
   `references/gaya-visual-anime.md` untuk deskripsi karakter dan setting yang konsisten —
   jangan parafrase ulang deskripsi karakter tiap kali, salin persis supaya wajah/pakaian host
   tidak berubah-ubah antar video. Format prompt per shot mengikuti
   `templates/prompt-video-template.md`.

5. **Siapkan metadata upload** memakai `templates/metadata-template.md` dan patuhi ketentuan platform
   di `references/platform-guidelines.md` — termasuk **wajib menyalakan label konten AI-generated**
   di TikTok maupun YouTube untuk semua video di seri ini, dan menyebar jadwal upload sepanjang hari
   (bukan sekaligus).

6. **Kalau diminta otomasi penuh** (generate → video AI → upload otomatis), rujuk
   `automation/n8n-workflow-kopi-sumatra.md` di root repo untuk rancangan workflow n8n-nya. Jangan
   asumsikan kredensial API AI video-gen atau TikTok/YouTube sudah tersedia — tanyakan dulu ke
   pengguna sebelum mencoba menyambungkan API sungguhan.

## Struktur skill ini

```
kopi-sumatra-content/
├── SKILL.md                          (file ini)
├── references/
│   ├── riset-kopi-sumatra.md         fakta dasar kopi Sumatra (kebun -> cangkir)
│   ├── content-pillars.md            sistem rotasi Pilar x Format x Setting x Host
│   ├── gaya-visual-anime.md          panduan gaya visual & character/setting sheet
│   └── platform-guidelines.md        aturan TikTok Studio & YouTube Shorts
├── templates/
│   ├── skrip-template.md             format skrip per video
│   ├── prompt-video-template.md      format prompt text-to-video per shot
│   └── metadata-template.md          format caption/judul/hashtag/jadwal upload
└── scripts/
    └── generate_batch.py             generator batch harian (rotasi kombinatorial)
```

## Batasan yang perlu diingat

- Skill ini menghasilkan **skrip, prompt, dan metadata** — bukan file video jadi. Video AI perlu
  dibuat lewat tool text-to-video pilihan pengguna (di luar skill ini), lalu disambung/di-edit.
- Jangan buat klaim kesehatan/medis tentang kopi, dan hati-hati dengan topik kopi luwak (isu
  kesejahteraan hewan) — lihat bagian "Sensitivitas & Kepatuhan Konten" di
  `references/riset-kopi-sumatra.md`.
- Upload sungguhan ke TikTok/YouTube (baik manual maupun via automation) tetap butuh review manusia
  sebelum publish, terutama di awal seri.
