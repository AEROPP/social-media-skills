# Estimasi Biaya Produksi — Kopi Sumatra Content (100 video/hari, Footage CC0/Public Domain)

Perhitungan ini mengasumsikan **Jalur A: footage 100% CC0/Public Domain** (Pexels, Pixabay, dan
sesekali Wikimedia Commons/rilisan pemerintah untuk klip spesifik) sebagai keputusan sumber footage
saat ini — lihat `skills/kopi-sumatra-content/references/sumber-footage-berlisensi.md`. Tidak ada
biaya lisensi Shutterstock atau syuting sendiri di angka ini; keduanya tetap didokumentasikan sebagai
opsi upgrade nanti kalau dibutuhkan.

**Harga di bawah hasil pencarian web per Agustus 2026** dan bisa berubah — cek ulang harga resmi
(terutama tarif TTS/stitching) sebelum commit budget besar.

## 0. Fase pilot saat ini: 10 video/hari

Skala operasional yang sedang berjalan (lihat `output/2026-08-07-pilot-10/produksi-10-video.md`)
adalah **10 video/hari**, bukan 100. Biaya per video sama saja (footage tetap $0, cuma voiceover +
stitching), tapi totalnya jauh lebih kecil karena volumenya 10x lebih sedikit — dan di skala ini,
kurasi masih dikerjakan manual per video, jadi jam kerjanya juga lebih sedikit dari asumsi 100/hari:

| | Estimasi (10 video/hari, 300 video/bulan) |
|---|---|
| Biaya berjalan (voiceover + stitching) | $1,2-2,3/hari → **$36-69/bulan** |
| Kurasi footage + QA manual (~1-1,5 jam/hari @ ~$6/jam) | **~$180-270/bulan** |
| Storage (±300 file/bulan) | ~$2-3/bulan |
| Otomasi n8n | $0 (di skala ini masih wajar dikerjakan manual tanpa otomasi) |
| **Total/bulan (fase pilot)** | **≈ $220-340/bulan (≈ Rp 3,5-5,4 juta)** |

Semua angka di bagian 1-8 di bawah tetap dihitung untuk **target 100 video/hari** (skenario setelah
pilot terbukti dan siap naik skala) — gunakan sebagai referensi kapan waktunya scale-up masuk akal
secara biaya vs. hasil (retention, follower growth) dari fase pilot ini.

## 1. Biaya footage: $0

Pexels dan Pixabay: gratis untuk pemakaian komersial, tanpa batas jumlah unduhan, tanpa batas
tayang/views, tanpa kewajiban atribusi (walau disarankan), dan API-nya gratis untuk otomasi
pencarian. Satu-satunya "biaya" di sini adalah **waktu kurasi manusia** yang lebih lama dibanding
stock berbayar karena katalog CC0 kurang tertag rapi — sudah dimasukkan ke baris tenaga kerja di
bawah.

## 2. Biaya berjalan per video

| Komponen | Estimasi/video | Catatan |
|---|---|---|
| Footage (Pexels/Pixabay) | **$0** | Reusable tanpa batas, tidak ada biaya per klip maupun per video. |
| Voiceover (ElevenLabs, ~300 karakter/video) | **$0.02-0.03** | Flash/Turbo $0.05/1.000 karakter atau Multilingual v2 $0.10/1.000 karakter. |
| Stitching/edit (Shotstack/Creatomate, video ~0.5 menit) | **$0.10-0.20** | Menyambung 2-3 klip B-roll + voiceover + caption burned-in + overlay grafis (wajib — lihat catatan nilai-tambah di `sumber-footage-berlisensi.md`, makin penting karena footage-nya generik). |
| **Total per video** | **≈ $0.12-0.23** | |

## 3. Biaya harian & bulanan (100 video/hari, 3.000 video/bulan)

| | Estimasi |
|---|---|
| Per hari (100 video) | $12-23 |
| Per bulan (3.000 video) | $360-690 |

## 4. Biaya pendukung tetap

| Komponen | Estimasi | Catatan |
|---|---|---|
| Otomasi n8n | $0-29 | Self-host ≈ $0, atau n8n Cloud Starter ~$26. 100 video/hari lewat 1 trigger harian jauh di bawah kuota eksekusi tier termurah. Pencarian API Pexels/Pixabay gratis, hanya perlu API key. |
| Storage video | $10-15 | Untuk ±3.000 file video/bulan sebelum diupload/dihapus. |
| Kurasi footage + QA sebelum publish | **~$540** | Naik dari asumsi sebelumnya (~2 jam/hari) menjadi **~3 jam/hari @ ~$6/jam**, karena mencocokkan kata kunci shot list ke katalog CC0 yang kurang tertag rapi makan waktu lebih lama dibanding stock berbayar, ditambah cek fakta & cek lisensi/atribusi tiap klip. **Sesuaikan dengan tarif tenaga kerja & efisiensi tim sebenarnya** — ini variabel paling tidak pasti di perhitungan ini. |
| **Total pendukung** | **≈ $550-585/bulan** | |

## 5. Total estimasi bulanan (all-in, 3.000 video/bulan)

| | Estimasi |
|---|---|
| Biaya berjalan (voiceover + stitching) | $360-690 |
| Pendukung tetap (n8n + storage + kurasi/QA) | ~$565 |
| **Total/bulan** | **≈ $925-1.255** |
| **Biaya per video (all-in)** | **≈ $0.31-0.42** |
| **Investasi awal perpustakaan footage** | **$0** (tidak perlu beli apa pun di muka) |

Kurs kasar (cek kurs hari ini sebelum dipakai resmi, asumsi Rp 16.000/USD):

| | Estimasi |
|---|---|
| Per video | ≈ Rp 4.960 - Rp 6.720 |
| Per bulan | ≈ Rp 14,8 juta - Rp 20,1 juta |

## 6. Perbandingan dengan opsi lain (untuk konteks, tidak dipakai saat ini)

| | AI Budget (Runway Turbo) | AI Menengah (Kling) | AI Premium (Runway 4.5) | Real-Footage + Shutterstock | **Real-Footage CC0 (dipakai sekarang)** |
|---|---|---|---|---|---|
| Investasi awal | $0 | $0 | $0 | $500-1.500 | **$0** |
| Per video (ongoing) | $0.28 | $1.52 | $2.79 | $0.12-0.23 | **$0.12-0.23** |
| Per bulan (ongoing) | $1.225 | $4.945 | $8.755 | $900-1.375 | **$925-1.255** |

CC0 dan Shutterstock punya biaya *ongoing* yang mirip (karena keduanya sama-sama cuma bayar
voiceover+stitching per video setelah perpustakaan terbentuk) — **bedanya CC0 tidak butuh investasi
awal sama sekali**, sementara Shutterstock butuh $500-1.500 di muka untuk membangun katalog. Trade-off
CC0: visual lebih generik dan waktu kurasi lebih lama (sudah tercermin di baris tenaga kerja).

## 7. Yang TIDAK termasuk di angka di atas

- **Kuota/API upload TikTok & YouTube**: gratis secara nominal, tapi ada batasan teknis nyata (kuota
  YouTube Data API default ~6 upload/hari, TikTok Content Posting API butuh app review) — lihat
  `n8n-workflow-kopi-sumatra.md`.
- **Rate limit API Pexels/Pixabay**: gratis tapi ada batas request/jam — di skala 100 video/hari
  (±200-300 pencarian/hari) umumnya masih aman, tapi pantau saat mulai scaling; atribusi ke
  Pexels/fotografer bisa melonggarkan limit kalau dibutuhkan.
- **Lisensi musik/audio latar** di luar yang disediakan gratis oleh TikTok/YouTube.
- **Biaya upgrade ke Jalur B/C** kalau nanti footage CC0 dirasa kurang otentik/berulang — lihat
  estimasi di `sumber-footage-berlisensi.md`.

## 8. Cara menghitung ulang untuk asumsi berbeda

```
Biaya ongoing/video = biaya voiceover + biaya stitching (footage = $0 di Jalur A)
Biaya per hari       = jumlah video/hari x biaya ongoing/video
Biaya per bulan      = biaya per hari x jumlah hari upload/bulan + biaya kurasi/QA tenaga kerja
```

## Sumber (Agustus 2026)

- [Pexels License](https://www.pexels.com/license/) — gratis komersial, atribusi tidak wajib, tidak boleh dijual mentah/standalone
- [Pexels API](https://www.pexels.com/api/) — gratis, rate limit dilonggarkan dengan atribusi
- [Pixabay Terms of Service](https://pixabay.com/service/terms/) — gratis komersial, atribusi tidak wajib
- [Pixabay License guide](https://pixabay.com/blog/posts/pixabay-license-what-is-allowed-and-what-is-not-4/)
- [ElevenLabs API Pricing](https://elevenlabs.io/pricing/api) — $0.05-$0.10 per 1.000 karakter
- [Shotstack vs Creatomate 2026 — Wireflow](https://www.wireflow.ai/blog/creatomate-vs-shotstack) — $0.10-$0.40/menit
- [n8n Pricing 2026 — openhosst](https://openhosst.com/blog/n8n-cloud-pricing) — Starter €24/mo, 2.500 eksekusi
- [YouTube Reused Content Policy 2026 — vidIQ](https://vidiq.com/blog/post/youtube-reused-content-policy-guide/)
