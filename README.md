# Social Media Skills

Repo ini berisi Claude Skills untuk produksi konten media sosial. Skill pertama:
**`kopi-sumatra-content`** — seri edukasi kopi Sumatra (dari kebun sampai ke penikmat kopi) untuk
TikTok Studio & YouTube Shorts, memakai **footage nyata berlisensi CC0** (Pexels/Pixabay, bukan
AI-generated). **Skala operasional saat ini: 10 video/hari (pilot)**, menuju target 100/hari setelah
formatnya terbukti.

> Catatan: pipeline ini awalnya dirancang memakai AI text-to-video bergaya anime, lalu dipindah ke
> real-footage CC0 berlisensi karena AI-generation jauh lebih mahal di skala tinggi, sedangkan
> clip video YouTube orang lain tanpa izin melanggar hak cipta & ToS. Lihat
> `skills/kopi-sumatra-content/references/sumber-footage-berlisensi.md` untuk alasan & sumber legal.

## Struktur repo

```
social-media-skills/
├── skills/
│   └── kopi-sumatra-content/     Skill utama: SKILL.md + referensi riset & sumber footage, template
│                                  skrip/shot-list/metadata, dan generator batch harian
├── output/
│   ├── 2026-08-07-pilot-10/       Produksi harian 10 video/hari (skala aktif saat ini), skrip
│   │                               lengkap siap produksi di produksi-10-video.md
│   └── 2026-08-07/                Contoh batch 100 video concept (JSON + CSV) untuk target ke depan
└── automation/
    ├── n8n-workflow-kopi-sumatra.md      Rancangan otomasi + batasan nyata (lisensi, kuota upload)
    ├── workflow-kopi-sumatra.json        Skeleton workflow n8n yang bisa diimpor (node API dinonaktifkan)
    └── estimasi-biaya-produksi.md        Perhitungan biaya produksi per video/hari/bulan
```

## Mulai dari mana

1. Baca `skills/kopi-sumatra-content/SKILL.md` untuk alur kerja lengkap.
2. Jalankan generator untuk membuat batch harian baru (mulai dari 10/hari):
   ```
   python skills/kopi-sumatra-content/scripts/generate_batch.py --date YYYY-MM-DD --count 10 \
     --out-dir output/YYYY-MM-DD
   ```
3. Sunting hasilnya (skrip, shot list kata kunci footage, metadata) sesuai panduan di `references/`
   dan `templates/` — lihat `output/2026-08-07-pilot-10/produksi-10-video.md` sebagai contoh hasil
   sunting lengkap — lalu cocokkan tiap shot ke footage CC0 nyata sebelum diedit/diupload.
4. Kalau ingin mengotomasi generate → sourcing footage → upload, baca dulu
   `automation/n8n-workflow-kopi-sumatra.md` — ada batasan kuota API TikTok/YouTube yang penting
   dipahami sebelum menargetkan otomasi penuh 100 upload/hari.
5. Untuk perkiraan biaya, lihat `automation/estimasi-biaya-produksi.md`.

## Contoh hasil produksi

- `output/2026-08-07-pilot-10/produksi-10-video.md` — **skrip produksi lengkap 10 video** (hook, isi,
  CTA, shot list footage, overlay, metadata TikTok/YouTube, jadwal upload) untuk skala pilot yang
  sedang berjalan.
- `output/2026-08-07/batch.csv` dan `batch.json` — contoh mentah 100 konsep video hasil generator
  (belum disunting) untuk gambaran skala target ke depan.
