# Prompt Riset Produk Viral — Versi Output untuk CapCut Product Video

Adaptasi dari `prompt-riset-produk-viral-n8n.md`, outputnya diarahkan untuk dipakai di fitur
**CapCut Commerce / Product Video** (bikin video promo produk otomatis dari foto produk) alih-alih
Creatomate.

## Catatan penting sebelum pakai (baca dulu)

**CapCut tidak punya API publik untuk render otomatis** seperti Creatomate. Fitur Product Video/Commerce
di CapCut adalah alur **manual di dalam aplikasi**: kamu upload foto produk atau paste link produk
(Shopee/TikTok Shop), pilih template, lalu CapCut yang men-generate video-nya di app — n8n/AI Agent
tidak bisa "memencet tombol" itu langsung. Karena itu, workflow ini didesain sampai tahap **paket siap
pakai** (foto, nama produk, keunggulan produk, naskah hook) yang dikirim ke Telegram, lalu **manusia**
yang membuka CapCut dan menempelkan datanya ke fitur Product Video. Kalau ternyata kamu punya akses ke
CapCut Business API/Open Platform yang mendukung automasi headless, beri tahu saya detailnya dan
langkah render bisa disambung otomatis juga.

## 1. Field input (Set/Edit Fields node, sebelum AI Agent node)

| Field | Tipe | Contoh isi |
|---|---|---|
| `product_niche` | String | `ISI_NICHE_PRODUK_ANDA` |
| `target_audience` | String | `ISI_TARGET_AUDIENCE_ANDA` |
| `target_marketplace` | String | `TikTok Shop, Shopee, Tokopedia, Instagram Shopping` |
| `viral_criteria` | String | `pertumbuhan penjualan cepat, banyak UGC/hashtag, direview micro-influencer, masuk trending marketplace` |
| `capcut_video_style` | String | `ISI_GAYA_VIDEO_ANDA` (mis. "unboxing energik, teks besar, musik upbeat" atau "clean minimal ala review produk") |
| `telegram_chat_id` | String | `ISI_CHAT_ID_TELEGRAM_ANDA` |

`capcut_video_style` menggantikan `creatomate_template_id` — bukan ID template (CapCut tidak dipanggil
via ID API), tapi deskripsi gaya video yang dipakai manusia untuk memilih template CapCut Product Video
yang paling cocok saat proses manual nanti.

## 2. Prompt untuk AI Agent node

Tetap **wajib pakai AI Agent node yang tersambung ke tool pencarian web** — alasan sama seperti versi
sebelumnya: data viral berubah tiap hari, tidak boleh dikarang dari ingatan model.

```
Kamu adalah AI Agent riset tren e-commerce. Tugasmu: menemukan produk yang SAAT INI paling viral di
media sosial dan marketplace, sesuai niche yang diberikan, DAN menyiapkan paket materi siap pakai
untuk dibuatkan video promo di CapCut (fitur Product Video/Commerce).

ATURAN WAJIB:
- Pakai tool pencarian yang tersedia untuk SETIAP klaim tren — jangan mengarang nama produk, angka,
  atau statistik dari ingatan. Pengetahuanmu punya batas waktu, dan data viral berubah tiap hari.
- Kalau hasil pencarian tidak cukup meyakinkan untuk niche ini, katakan terus terang "data tidak
  cukup ditemukan" — jangan memaksakan jawaban supaya terlihat lengkap.
- Prioritaskan sumber: halaman trending/best-seller TikTok Shop, Shopee, Tokopedia; hashtag challenge
  terkait produk di TikTok/Instagram; pemberitaan media soal produk viral. Catat tanggal data diambil.
- Untuk URL gambar produk: HANYA sertakan URL foto yang benar-benar ditemukan lewat pencarian (mis.
  dari listing marketplace resmi). Kalau tidak ketemu URL foto yang valid, kosongkan field-nya —
  JANGAN menaruh URL karangan.

INPUT:
- Niche produk: {{ $json.product_niche }}
- Target audiens: {{ $json.target_audience }}
- Marketplace yang dicari: {{ $json.target_marketplace }}
- Kriteria "viral": {{ $json.viral_criteria }}
- Gaya video CapCut yang diinginkan: {{ $json.capcut_video_style }}

TUGAS:
1. Cari 5-8 produk yang menunjukkan tanda-tanda viral sesuai kriteria, dalam niche & marketplace yang
   ditentukan.
2. Untuk tiap produk, kumpulkan: nama produk, marketplace/platform ditemukan, bukti tren konkret,
   kenapa relevan buat target audiens, URL listing produk (buat cek foto & link beli), dan tanggal
   data diambil.
3. Urutkan dari sinyal viral paling kuat ke paling lemah.
4. Untuk 3 produk teratas, siapkan **paket materi CapCut**:
   - `key_selling_points`: 3-4 poin keunggulan produk singkat (buat teks di video)
   - `hook_script`: 1 kalimat pembuka video yang menarik perhatian 2 detik pertama, sesuai gaya
     video yang diminta ({{ $json.capcut_video_style }})
   - `caption_cta`: 1 kalimat penutup/ajakan beli untuk caption post
   - `suggested_hashtags`: 4-6 hashtag relevan (niche + marketplace + umum)

OUTPUT — HARUS JSON valid, tanpa teks lain di luar JSON:
{
  "generated_at": "YYYY-MM-DD",
  "niche": "...",
  "products": [
    {
      "rank": 1,
      "product_name": "...",
      "marketplace": "...",
      "listing_url": "...",
      "viral_evidence": "...",
      "why_relevant": "...",
      "data_as_of": "YYYY-MM-DD",
      "capcut_package": {
        "key_selling_points": ["...", "...", "..."],
        "hook_script": "...",
        "caption_cta": "...",
        "suggested_hashtags": ["...", "..."]
      }
    }
  ],
  "note_if_insufficient_data": "..."
}
```

## 3. Alur kerja (n8n → Telegram → manual CapCut)

```
[Edit Fields: 6 field di atas]
        ↓
[AI Agent node + tool pencarian web]  ← prompt di section 2
        ↓
[Parse JSON output]
        ↓
[Format pesan Telegram: top 3 produk + capcut_package tiap produk]
        ↓
[Kirim ke telegram_chat_id]
        ↓
   (MANUAL — bukan otomatis)
[Tim buka CapCut → Product Video/Commerce]
[Paste listing_url produk / upload foto produk]
[Tempel hook_script sebagai teks pembuka]
[Tempel key_selling_points sebagai teks isi]
[Pilih template sesuai capcut_video_style]
[Render & download, lalu upload manual ke TikTok/Shopee]
```

## Contoh format pesan Telegram (node "Format Message" sebelum kirim)

```
🔥 PRODUK VIRAL HARI INI — {{ $json.niche }}
Diambil: {{ $json.generated_at }}

#1 {{ $json.products[0].product_name }} ({{ $json.products[0].marketplace }})
Bukti viral: {{ $json.products[0].viral_evidence }}
Kenapa relevan: {{ $json.products[0].why_relevant }}
Link: {{ $json.products[0].listing_url }}

📦 Paket materi CapCut:
Hook: "{{ $json.products[0].capcut_package.hook_script }}"
Poin jual:
- {{ $json.products[0].capcut_package.key_selling_points[0] }}
- {{ $json.products[0].capcut_package.key_selling_points[1] }}
- {{ $json.products[0].capcut_package.key_selling_points[2] }}
CTA: "{{ $json.products[0].capcut_package.caption_cta }}"
Hashtag: {{ $json.products[0].capcut_package.suggested_hashtags.join(' ') }}

👉 Buka CapCut > Product Video, upload foto dari link di atas, tempel materi ini.
```

(Ulangi blok yang sama untuk produk rank #2 dan #3, atau loop pakai node "Split in Batches" kalau mau
tiap produk jadi pesan Telegram terpisah.)

## Catatan tambahan

- Kalau timmu memang butuh render otomatis tanpa sentuh tangan manusia, opsi realistisnya bukan
  CapCut — balik ke versi Creatomate (`prompt-riset-produk-viral-n8n.md`) yang memang didesain untuk
  dipanggil via API dari n8n.
- Field `listing_url` sengaja dipisah dari "URL gambar langsung" karena AI Agent lebih reliable
  menemukan link listing marketplace lewat pencarian dibanding menebak URL file gambar spesifik —
  tim tinggal buka link itu dan screenshot/download foto produknya sendiri untuk diupload ke CapCut.
