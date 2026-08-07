# Social Media Skills

Repo ini berisi Claude Skills untuk produksi konten media sosial. Skill pertama:
**`kopi-sumatra-content`** — seri edukasi kopi Sumatra (dari kebun sampai ke penikmat kopi) untuk
TikTok Studio & YouTube Shorts, memakai AI text-to-video bergaya anime/cartoon, dirancang untuk
skala sampai 100 video pendek per hari.

## Struktur repo

```
social-media-skills/
├── skills/
│   └── kopi-sumatra-content/     Skill utama: SKILL.md + referensi riset, template skrip/prompt/
│                                  metadata, dan generator batch harian
├── output/
│   └── 2026-08-07/                Contoh batch 100 video concept (JSON + CSV) hasil generator
└── automation/
    ├── n8n-workflow-kopi-sumatra.md   Rancangan otomasi + batasan nyata (kuota YouTube, review TikTok)
    └── workflow-kopi-sumatra.json     Skeleton workflow n8n yang bisa diimpor (node API dinonaktifkan)
```

## Mulai dari mana

1. Baca `skills/kopi-sumatra-content/SKILL.md` untuk alur kerja lengkap.
2. Jalankan generator untuk membuat batch harian baru:
   ```
   python skills/kopi-sumatra-content/scripts/generate_batch.py --date YYYY-MM-DD --count 100 \
     --out-dir output/YYYY-MM-DD
   ```
3. Sunting hasilnya (skrip, prompt video, metadata) sesuai panduan di `references/` dan `templates/`
   sebelum dipakai untuk render video AI / upload.
4. Kalau ingin mengotomasi generate → render → upload, baca dulu
   `automation/n8n-workflow-kopi-sumatra.md` — ada batasan kuota API TikTok/YouTube yang penting
   dipahami sebelum menargetkan otomasi penuh 100 upload/hari.

## Contoh hasil hari pertama

`output/2026-08-07/batch.csv` dan `batch.json` berisi 100 konsep video (pilar, format, setting,
host, hook, isi, CTA, caption on-screen, prompt video per shot, caption/hashtag TikTok, judul/deskripsi
YouTube Shorts) — hasil generator, siap disunting sebelum produksi.
