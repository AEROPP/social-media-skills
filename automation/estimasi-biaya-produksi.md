# Estimasi Biaya Produksi — Kopi Sumatra Content (100 video/hari, Real-Footage)

Perhitungan ini sudah diperbarui mengikuti pivot dari AI text-to-video ke **real-footage berlisensi**
(lihat `skills/kopi-sumatra-content/references/sumber-footage-berlisensi.md`). Struktur biayanya beda
secara mendasar: footage boleh dipakai ulang di banyak video (lisensi royalty-free), jadi biayanya
**investasi perpustakaan di muka + biaya kecil per video (voiceover & editing)** — bukan biaya
video-gen yang terus bertambah linear seperti pendekatan AI sebelumnya.

**Harga di bawah hasil pencarian web per Agustus 2026** dan bisa berubah — cek ulang harga resmi
sebelum commit budget besar, terutama untuk lisensi Shutterstock Enhanced (harganya tidak dipublikasikan
pasti, perlu cek langsung saat checkout/hubungi sales).

## 1. Biaya investasi perpustakaan footage (satu kali / periodik, bukan per video)

| Jalur | Estimasi biaya | Catatan |
|---|---|---|
| **A. Full CC0** (Pexels/Pixabay) | **$0** | Cukup untuk validasi awal format konten; footage generik, kurang spesifik "Sumatra". |
| **B. Campuran CC0 + Shutterstock** | **≈ $500-1.500** (satu kali, lalu refresh berkala) | Mis. 60 klip CC0 gratis + 40-90 klip Shutterstock (on-demand $8.32-9.95/klip, atau subscription $119/bulan untuk 20 klip/bulan selama 2-4 bulan lalu berhenti berlangganan). |
| **C. Syuting/komisi sendiri** | **≈ Rp 3-6 juta (~$190-380) sekali syuting** | Sewa videografer lokal Aceh/Sumut 1-2 hari, hasil bisa dipecah puluhan-ratusan klip B-roll otentik, **dimiliki penuh** (tidak ada batas lisensi/views). Nilai terbaik jangka panjang. |

**Rekomendasi jalur**: mulai dari **A (gratis)** untuk uji format & validasi engagement 2-4 minggu
pertama, lalu investasi ke **C (syuting sendiri)** begitu channel terbukti dapat traksi — ini
menghasilkan aset tak terbatas tanpa batas lisensi, lebih murah dalam jangka panjang dibanding terus
berlangganan stock, dan visualnya lebih otentik (benar-benar Gayo/Lintong/Mandailing, bukan stok
generik).

## 2. Biaya berjalan per video (tidak tergantung sumber footage, karena footage dipakai ulang)

| Komponen | Estimasi/video | Catatan |
|---|---|---|
| Voiceover (ElevenLabs, ~300 karakter/video) | **$0.02-0.03** | Flash/Turbo $0.05/1.000 karakter atau Multilingual v2 $0.10/1.000 karakter. |
| Stitching/edit (Shotstack/Creatomate, video ~0.5 menit) | **$0.10-0.20** | Menyambung 2-3 klip B-roll + voiceover + caption burned-in + overlay grafis (wajib untuk kepatuhan reused-content, lihat `references/platform-guidelines.md`). |
| **Total per video** | **≈ $0.12-0.23** | Jauh lebih murah dari tier AI Menengah/Premium sebelumnya, dan sedikit lebih murah atau setara tier AI Budget (Runway Turbo $0.28/video). |

## 3. Biaya harian & bulanan (100 video/hari, 3.000 video/bulan)

| | Estimasi |
|---|---|
| Per hari (100 video, voiceover+stitch saja) | $12-23 |
| Per bulan (3.000 video) | $360-690 |
| + Refresh perpustakaan footage berkala | +$150-300/bulan (opsional, biar visual tidak itu-itu saja) |

## 4. Biaya pendukung tetap (sama seperti sebelumnya, tidak berubah oleh pivot ini)

| Komponen | Estimasi | Catatan |
|---|---|---|
| Otomasi n8n | $0-29 | Self-host ≈ $0, atau n8n Cloud Starter ~$26. 100 video/hari lewat 1 trigger harian jauh di bawah kuota eksekusi tier termurah. |
| Storage video | $10-15 | Untuk ±3.000 file video/bulan sebelum diupload/dihapus. |
| Review manusia (QA + cek lisensi sebelum publish) | ~$360 | Placeholder: 1 reviewer paruh waktu ~2 jam/hari @ ~$6/jam — **sesuaikan dengan tarif nyata**. Review sekarang juga mengecek kecocokan lisensi footage, bukan cuma cek fakta. |
| **Total pendukung** | **≈ $370-400/bulan** | |

## 5. Total estimasi bulanan (all-in, 3.000 video/bulan)

| | Estimasi |
|---|---|
| Biaya berjalan (voiceover+stitch+refresh) | $510-990 |
| Pendukung tetap | ~$385 |
| **Total/bulan (setelah perpustakaan awal jadi)** | **≈ $900-1.375/bulan** |
| **Biaya per video (all-in, ongoing)** | **≈ $0.30-0.46** |
| **+ Investasi awal perpustakaan (sekali)** | $0 (jalur A) / $500-1.500 (jalur B) / ~$190-380 (jalur C) |

Kurs kasar (cek kurs hari ini sebelum dipakai resmi, asumsi Rp 16.000/USD): total bulanan ongoing
≈ **Rp 14,4-22 juta/bulan**, investasi awal ≈ **Rp 0-24 juta** tergantung jalur.

## 6. Perbandingan dengan pendekatan AI text-to-video (versi sebelumnya)

| | AI Budget (Runway Turbo) | AI Menengah (Kling) | AI Premium (Runway 4.5) | **Real-Footage (pivot ini)** |
|---|---|---|---|---|
| Per video (ongoing) | $0.28 | $1.52 | $2.79 | **$0.12-0.23** |
| Per bulan (ongoing) | $1.225 | $4.945 | $8.755 | **$900-1.375** |

**Kejujuran soal angka ini**: real-footage kira-kira **setara atau sedikit lebih murah** dibanding
tier AI paling murah (Runway Turbo), tapi **jauh lebih murah** dari tier AI Menengah/Premium. Yang
membuat real-footage tetap layak dipilih bukan cuma soal lebih murah, tapi:
- Tidak ada risiko glitch/distorsi wajah/inkonsistensi karakter khas AI-generated video.
- Tidak wajib label AI-generated content (kecuali voiceover-nya sangat realistis).
- Investasi jalur C (syuting sendiri) makin lama makin murah karena footage jadi aset milik sendiri.

Trade-off-nya: real-footage butuh **kedisiplinan lisensi** (catat sumber tiap klip, pantau batas
500.000 views untuk klip Shutterstock Standard, penuhi syarat "nilai tambah asli" biar tidak kena
kebijakan reused-content) — overhead administratif yang tidak ada di pendekatan AI.

## 7. Yang TIDAK termasuk di angka di atas

- **Kuota/API upload TikTok & YouTube**: gratis secara nominal, tapi ada batasan teknis nyata (kuota
  YouTube Data API default ~6 upload/hari, TikTok Content Posting API butuh app review) — lihat
  `n8n-workflow-kopi-sumatra.md`.
- **Upgrade ke Shutterstock Enhanced License** untuk klip di video yang mendekati/viral melewati
  500.000 views — harga add-on ini tidak dipublikasikan pasti, cek langsung ke Shutterstock.
- **Lisensi musik/audio latar** di luar yang disediakan gratis oleh TikTok/YouTube.
- **Biaya syuting lanjutan** (jalur C) kalau ingin menambah variasi lokasi/musim secara berkala.

## 8. Cara menghitung ulang untuk asumsi berbeda

```
Biaya ongoing/video = biaya voiceover + biaya stitching (footage marginal ≈ $0 kalau reusable)
Biaya per hari       = jumlah video/hari x biaya ongoing/video
Biaya per bulan      = biaya per hari x jumlah hari upload/bulan + refresh perpustakaan berkala
```

## Sumber harga (Agustus 2026)

- [Shutterstock Pricing 2026 — Tekpon](https://tekpon.com/software/shutterstock/pricing/) — subscription video $59-119/bulan (5-20 klip)
- [Photutorial — Shutterstock cost](https://photutorial.com/shutterstock-pricing-explained/) — on-demand $8.32-9.95/klip
- [Shutterstock license comparison](https://www.shutterstock.com/royalty-free/video-license-comparison) — Standard: 500.000 views cap, indemnifikasi $10.000; Enhanced: indemnifikasi $250.000
- [ElevenLabs API Pricing](https://elevenlabs.io/pricing/api) — $0.05-$0.10 per 1.000 karakter
- [Shotstack vs Creatomate 2026 — Wireflow](https://www.wireflow.ai/blog/creatomate-vs-shotstack) — $0.10-$0.40/menit
- [n8n Pricing 2026 — openhosst](https://openhosst.com/blog/n8n-cloud-pricing) — Starter €24/mo, 2.500 eksekusi
- [YouTube Reused Content Policy 2026 — vidIQ](https://vidiq.com/blog/post/youtube-reused-content-policy-guide/)
