# Rekomendasi Tools Produksi (Agustus 2026)

Tiga kategori tool yang dibutuhkan pipeline ini: (1) perakit video otomatis (script + footage +
voiceover jadi 1 video), (2) voiceover/TTS untuk narator, (3) AI text-to-video murni untuk shot
spesifik yang tidak ada di katalog CC0. Harga & fitur di bawah hasil riset per Agustus 2026 — cek
ulang sebelum berlangganan, terutama kuota/limit yang berubah cepat.

## 1. AI Script-to-Video Assembler (kebutuhan utama saat ini)

Ini yang paling relevan untuk pipeline sekarang: mengubah naskah di `produksi-10-video.md` +
footage CC0 + voiceover jadi video jadi, tanpa edit manual satu-satu.

| Tool | Harga | Kelebihan | Catatan untuk pipeline ini |
|---|---|---|---|
| **CapCut** | Gratis, tanpa watermark | Auto-caption AI (edit-able), terintegrasi Sora 2 & Veo 3.1 untuk shot AI sesekali, familiar dipakai kreator Indonesia | **Rekomendasi utama untuk fase pilot 10/hari** — gratis, dan tim editor Indonesia umumnya sudah terbiasa pakai ini |
| **Pictory** | $25/bulan (tahunan), 200 menit video/bulan | Auto-cocokkan tiap bagian naskah ke klip stock, overlay voiceover otomatis | Jatah 200 menit/bulan ≈ pas untuk skala **10 video/hari** (±150 menit/bulan di durasi 25-30 detik/video), tapi kurang untuk 100/hari (butuh ±1.500 menit/bulan → perlu tier lebih tinggi) |
| **InVideo AI** | $28/bulan | Dari prompt/skrip langsung jadi video: cari klip, tambah voiceover+teks+musik+transisi otomatis | Alternatif Pictory, alur kerja mirip |
| **Fliki** | Bervariasi per paket | Kualitas voiceover jadi diferensiator utama, caption stabil kalau naskah direvisi | Punya banyak provider suara dalam satu tempat (Azure, ElevenLabs, dll.) — kalau ingin voiceover+assembly dalam satu tool |

**Rekomendasi bertahap**: pakai **CapCut** (gratis) untuk validasi 10 video/hari sekarang. Kalau mulai
naik skala dan volume kerja manual mulai berat, pindah ke **Pictory/InVideo AI** yang otomatis
mencocokkan naskah ke klip — di titik itu juga saatnya evaluasi apakah 200 menit/bulan Pictory masih
cukup atau perlu naik tier / pindah alat lain untuk 100/hari.

## 2. AI Voiceover / TTS untuk narator (Pak Bahri, Kak Nur, Adit)

| Tool | Harga | Kelebihan | Catatan |
|---|---|---|---|
| **ElevenLabs** (rekomendasi utama) | Gratis 10.000 karakter/bulan (~10 menit audio), paid dari situ | Kualitas Bahasa Indonesia paling natural menurut ulasan 2026, mendukung berbagai aksen daerah, ada voice cloning untuk suara custom | Free tier cukup untuk ±30 video pilot (300 karakter/video); di skala 100/hari perlu paket berbayar — lihat `automation/estimasi-biaya-produksi.md` |
| **Murf AI (Falcon)** | ~$0.01/menit | Skor kualitas tertinggi dibanding ElevenLabs/OpenAI/Cartesia/Deepgram versi mereka, harga sepertiga ElevenLabs | Opsi hemat kalau budget TTS jadi perhatian di skala tinggi |
| **Fliki (multi-provider)** | Bervariasi | Bisa pilih provider suara (Azure, Google, ElevenLabs, dll.) dalam satu dashboard | Praktis kalau assembler & TTS ingin satu tool saja |

**Rekomendasi**: pakai **ElevenLabs** untuk konsistensi 3 suara narator (bikin 1 voice tersimpan per
narator, dipakai ulang tiap video — jangan pilih voice acak tiap kali, biar Pak Bahri/Kak Nur/Adit
selalu terdengar sama). Kalau biaya TTS mulai signifikan di skala 100/hari, evaluasi Murf sebagai
alternatif lebih murah.

## 3. AI Text-to-Video murni (pelengkap, BUKAN sumber utama)

Dipakai hanya untuk shot spesifik yang benar-benar tidak ada padanannya di Pexels/Pixabay (mis. close-up
sangat spesifik "biji kopi hijau kebiruan basah baru digiling") — bukan pengganti footage CC0 secara
keseluruhan (lihat alasan ekonomi & kepatuhan di `sumber-footage-berlisensi.md`).

| Tool | Kekuatan | Kapan dipakai |
|---|---|---|
| **Kling 3.0** | Koherensi naratif multi-shot terbaik, value bagus | Default kalau butuh AI shot — keseimbangan kualitas/harga terbaik |
| **Runway Gen-4.5** | Kualitas & fisika gerakan paling realistis | Kalau satu shot penting banget dan kualitas harus maksimal |
| **Pika 2.5** | Paling cepat & murah, bagus untuk iterasi cepat | Uji coba ide cepat sebelum commit ke render final |
| **Luma Ray3** | Color grading paling sinematik | Shot yang butuh mood visual premium (mis. konten highlight/showcase) |

**Catatan penting**: kalau AI-generated shot dipakai bareng footage CC0 dalam satu video, video itu
otomatis butuh label AI-generated content saat upload (beda dari video full-CC0) — lihat
`references/platform-guidelines.md`. Pakai sesedikit mungkin dan hanya kalau CC0 benar-benar tidak
punya alternatif yang cukup baik.

## Ringkasan stack yang direkomendasikan untuk fase pilot (10 video/hari)

```
Naskah & shot list  → dari generate_batch.py (sudah ada)
Footage             → Pexels/Pixabay (CC0, gratis)
Voiceover narator   → ElevenLabs (1 voice tersimpan per narator)
Assembly + caption  → CapCut (gratis)
AI shot pelengkap   → Kling 3.0 (hanya kalau CC0 benar-benar tidak ada, pay-as-you-go)
```
