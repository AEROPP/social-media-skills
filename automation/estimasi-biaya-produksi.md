# Estimasi Biaya Produksi — Kopi Sumatra Content (100 video/hari)

Perhitungan ini berbasis desain generator di `skills/kopi-sumatra-content/scripts/generate_batch.py`:
tiap video terdiri dari 1 shot establishing + 1-2 shot isi (rata-rata **~16 detik klip AI mentah per
video** sebelum di-trim jadi video final 15-45 detik), plus voiceover singkat dan proses penyambungan
klip (stitching).

**Harga di bawah hasil pencarian web per Agustus 2026** dan berubah cepat di industri AI video — cek
ulang harga resmi provider sebelum commit budget besar, terutama untuk kontrak/pembelian kredit dalam
jumlah besar.

## 1. Komponen biaya per video

| Komponen | Budget | Menengah | Premium |
|---|---|---|---|
| AI text-to-video | Runway Gen-4 Turbo, $0.01/detik | Kling Standard (via fal.ai), $0.084/detik | Runway Gen-4.5 / Kling 3.0, ~$0.16/detik (rata-rata) |
| → Biaya video-gen (~16 detik/video) | **$0.16** | **$1.34** | **$2.56** |
| Voiceover (ElevenLabs, ~300 karakter/video) | Flash/Turbo $0.05/1.000 karakter → **$0.02** | Multilingual v2 $0.10/1.000 karakter → **$0.03** | Multilingual v2 → **$0.03** |
| Stitching/edit klip (Shotstack/Creatomate, video ~0.5 menit) | Paket langganan $0.20/menit → **$0.10** | rata-rata **$0.15** | Pay-as-you-go $0.40/menit → **$0.20** |
| **Total per video** | **≈ $0.28** | **≈ $1.52** | **≈ $2.79** |

## 2. Biaya harian & bulanan (100 video/hari, 30 hari/bulan = 3.000 video/bulan)

| | Budget | Menengah | Premium |
|---|---|---|---|
| Per hari (100 video) | $28 | $152 | $279 |
| Per bulan (3.000 video) | $840 | $4.560 | $8.370 |

## 3. Biaya pendukung tetap (per bulan, tidak tergantung tier)

| Komponen | Estimasi | Catatan |
|---|---|---|
| Otomasi n8n | $0-29 | Self-host di VPS kecil ≈ $0 (pakai VPS yang sudah ada) atau n8n Cloud Starter €24 (~$26) kalau mau dikelola. 100 video/hari via 1 trigger harian ≈ 30 eksekusi/bulan — jauh di bawah kuota, jadi tier termurah cukup. |
| Storage video (Drive/S3) | $10-15 | Untuk ±3.000 file video/bulan sebelum diupload/dihapus. |
| Review manusia (QA sebelum publish) | ~$360 | Asumsi placeholder: 1 reviewer paruh waktu, ~2 jam/hari @ ~$6/jam. **Sesuaikan dengan tarif tenaga kerja sebenarnya** — ini variabel paling tidak pasti di perhitungan ini. |
| **Total biaya pendukung** | **≈ $370-400/bulan** | |

## 4. Total estimasi bulanan (all-in, 3.000 video/bulan)

| | Budget | Menengah | Premium |
|---|---|---|---|
| Produksi (video-gen+TTS+stitch) | $840 | $4.560 | $8.370 |
| Pendukung tetap | ~$385 | ~$385 | ~$385 |
| **Total/bulan** | **≈ $1.225** | **≈ $4.945** | **≈ $8.755** |
| **Biaya per video (all-in)** | **≈ $0.41** | **≈ $1.65** | **≈ $2.92** |

Kurs kasar (cek kurs hari ini sebelum dipakai resmi, asumsi Rp 16.000/USD):

| | Budget | Menengah | Premium |
|---|---|---|---|
| Per video | ≈ Rp 6.560 | ≈ Rp 26.400 | ≈ Rp 46.720 |
| Per bulan | ≈ Rp 19,6 juta | ≈ Rp 79,1 juta | ≈ Rp 140,1 juta |

## 5. Yang TIDAK termasuk di angka di atas

- **Kuota/API upload TikTok & YouTube**: gratis secara nominal, tapi ada batasan teknis nyata
  (kuota YouTube Data API default ~6 upload/hari, TikTok Content Posting API butuh app review) —
  lihat `n8n-workflow-kopi-sumatra.md`. Kalau upload tetap manual lewat TikTok Studio/YouTube Studio,
  biaya ini $0 tapi butuh waktu tenaga manusia tambahan untuk upload 100x/hari.
- **Riset & penulisan skrip**: ditangani skill ini (generator + review manusia/AI assistant),
  marginal cost mendekati nol di luar waktu review pada poin 3.
- **Biaya revisi ulang** kalau hasil video AI gagal/glitch dan perlu di-generate ulang — di dunia nyata
  biasanya ada tingkat kegagalan/reject 10-30% terutama untuk konsistensi karakter di text-to-video,
  yang bisa menambah 10-30% ke baris "video-gen" di atas. Belum dihitung di tabel karena sangat
  tergantung provider & seberapa ketat character sheet diikuti.
- **Lisensi musik/audio latar** kalau dipakai di luar dari yang disediakan gratis oleh TikTok/YouTube.

## 6. Cara menghitung ulang untuk asumsi berbeda

```
Biaya video-gen/video = (rata-rata detik klip AI per video) x (harga per detik provider)
Biaya per hari         = jumlah video/hari x total biaya per video
Biaya per bulan         = biaya per hari x jumlah hari upload/bulan
```

Ganti "rata-rata detik klip AI per video" kalau desain shot diubah (mis. lebih sedikit shot atau
shot lebih pendek akan menurunkan biaya linear), dan ganti harga per detik sesuai provider yang
akhirnya dipilih.

## Sumber harga (Agustus 2026)

- [Runway ML Pricing 2026](https://saascrmreview.com/runway-ml-pricing/) — Gen-4 Turbo $0.01/s, Gen-4.5 $0.12/s
- [Kling API Pricing 2026 — costbench](https://costbench.com/software/ai-media-apis/kling-api/) — $0.084-$0.168/s
- [AI Video Generation API Pricing May 2026 — Crazyrouter](https://crazyrouter.com/en/blog/ai-video-generation-api-pricing-may-2026-comparison)
- [Luma AI Pricing 2026 — eesel AI](https://www.eesel.ai/blog/luma-ai-pricing) — ~$0.60/klip 5 detik 720p
- [ElevenLabs API Pricing](https://elevenlabs.io/pricing/api) — $0.05-$0.10 per 1.000 karakter
- [Shotstack vs Creatomate 2026 — Wireflow](https://www.wireflow.ai/blog/creatomate-vs-shotstack) — $0.10-$0.40/menit
- [n8n Pricing 2026 — openhosst](https://openhosst.com/blog/n8n-cloud-pricing) — Starter €24/mo, 2.500 eksekusi
