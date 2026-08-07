# Social Media Skills

Repo ini berisi Claude Skills untuk produksi konten media sosial. Skill pertama:
**`kopi-sumatra-content`** — seri edukasi kopi Sumatra (dari kebun sampai ke penikmat kopi) untuk
TikTok Studio & YouTube Shorts, memakai **footage nyata berlisensi** (bukan AI-generated), dirancang
untuk skala sampai 100 video pendek per hari.

> Catatan: pipeline ini awalnya dirancang memakai AI text-to-video bergaya anime, lalu dipindah ke
> real-footage berlisensi karena AI-generation jauh lebih mahal di skala tinggi, sedangkan
> clip video YouTube orang lain tanpa izin melanggar hak cipta & ToS. Lihat
> `skills/kopi-sumatra-content/references/sumber-footage-berlisensi.md` untuk alasan & sumber legal.

## Struktur repo

```
social-media-skills/
├── skills/
│   └── kopi-sumatra-content/     Skill utama: SKILL.md + referensi riset & sumber footage, template
│                                  skrip/shot-list/metadata, dan generator batch harian
├── output/
│   └── 2026-08-07/                Contoh batch 100 video concept (JSON + CSV) hasil generator
└── automation/
    ├── n8n-workflow-kopi-sumatra.md      Rancangan otomasi + batasan nyata (lisensi, kuota upload)
    ├── workflow-kopi-sumatra.json        Skeleton workflow n8n yang bisa diimpor (node API dinonaktifkan)
    └── estimasi-biaya-produksi.md        Perhitungan biaya produksi per video/hari/bulan
```

## Mulai dari mana

1. Baca `skills/kopi-sumatra-content/SKILL.md` untuk alur kerja lengkap.
2. Jalankan generator untuk membuat batch harian baru:
   ```
   python skills/kopi-sumatra-content/scripts/generate_batch.py --date YYYY-MM-DD --count 100 \
     --out-dir output/YYYY-MM-DD
   ```
3. Sunting hasilnya (skrip, shot list kata kunci footage, metadata) sesuai panduan di `references/`
   dan `templates/`, lalu cocokkan tiap shot ke footage berlisensi nyata sebelum diedit/diupload.
4. Kalau ingin mengotomasi generate → sourcing footage → upload, baca dulu
   `automation/n8n-workflow-kopi-sumatra.md` — ada batasan lisensi footage & kuota API TikTok/YouTube
   yang penting dipahami sebelum menargetkan otomasi penuh 100 upload/hari.
5. Untuk perkiraan biaya, lihat `automation/estimasi-biaya-produksi.md`.

## Contoh hasil hari pertama

`output/2026-08-07/batch.csv` dan `batch.json` berisi 100 konsep video (pilar, format, kategori
footage, narator, hook, isi, CTA, caption on-screen, shot list kata kunci pencarian footage,
caption/hashtag TikTok, judul/deskripsi YouTube Shorts) — hasil generator, siap disunting dan
dicocokkan ke footage nyata sebelum produksi.
