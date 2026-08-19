# Prompt Riset Produk Viral (Struktur Field n8n) — General Purpose

Adaptasi dari struktur field yang dipakai di workflow konten (brand_niche/target_audience/post_tone/
image_style/creatomate_template_id/telegram_chat_id) menjadi versi untuk **riset produk paling viral di
media sosial & marketplace**. Niche dibiarkan general-purpose — diisi manual tiap kali dipakai, bukan
di-hardcode ke satu brand.

## 1. Field input (Set/Edit Fields node, sebelum AI Agent node)

| Field | Tipe | Contoh isi |
|---|---|---|
| `product_niche` | String | `ISI_NICHE_PRODUK_ANDA` (mis. "skincare lokal", "gadget rumah tangga", "aksesori kopi") |
| `target_audience` | String | `ISI_TARGET_AUDIENCE_ANDA` (mis. "wanita 20-35 tahun di kota besar Indonesia") |
| `target_marketplace` | String | `TikTok Shop, Shopee, Tokopedia, Instagram Shopping` |
| `viral_criteria` | String | `pertumbuhan penjualan cepat, banyak UGC/hashtag, direview micro-influencer, masuk trending marketplace` |
| `creatomate_template_id` | String | `ISI_ID_TEMPLATE_ANDA` |
| `telegram_chat_id` | String | `ISI_CHAT_ID_TELEGRAM_ANDA` |

Empat field pertama jadi variabel yang disuntik ke prompt AI Agent (lihat bawah); dua field terakhir
dipakai node-node setelah AI Agent (generate visual promo di Creatomate, kirim notifikasi ke Telegram).

## 2. Prompt untuk AI Agent node

**Wajib pakai AI Agent node yang tersambung ke tool pencarian web** (SerpAPI, Browse, HTTP Request ke
API marketplace, dll) — bukan LLM node biasa tanpa tool. Data "lagi viral" berubah tiap hari dan tidak
mungkin diketahui akurat dari pengetahuan model saja.

```
Kamu adalah AI Agent riset tren e-commerce. Tugasmu: menemukan produk yang SAAT INI paling viral di
media sosial dan marketplace, sesuai niche yang diberikan.

AT URAN WAJIB:
- Pakai tool pencarian yang tersedia untuk SETIAP klaim tren — jangan mengarang nama produk, angka,
  atau statistik dari ingatan. Pengetahuanmu punya batas waktu, dan data viral berubah tiap hari.
- Kalau hasil pencarian tidak cukup meyakinkan untuk niche ini, katakan terus terang "data tidak
  cukup ditemukan" — jangan memaksakan jawaban supaya terlihat lengkap.
- Prioritaskan sumber: halaman trending/best-seller TikTok Shop, Shopee, Tokopedia; hashtag challenge
  terkait produk di TikTok/Instagram; pemberitaan media soal produk viral. Catat tanggal data diambil.

INPUT:
- Niche produk: {{ $json.product_niche }}
- Target audiens: {{ $json.target_audience }}
- Marketplace yang dicari: {{ $json.target_marketplace }}
- Kriteria "viral": {{ $json.viral_criteria }}

TUGAS:
1. Cari 5-8 produk yang menunjukkan tanda-tanda viral sesuai kriteria, dalam niche & marketplace yang
   ditentukan.
2. Untuk tiap produk, kumpulkan: nama produk, marketplace/platform ditemukan, bukti tren konkret
   (mis. jumlah video terkait, lonjakan penjualan, pertumbuhan hashtag), kenapa relevan buat target
   audiens, sumber (URL/nama akun), dan tanggal data diambil.
3. Urutkan dari sinyal viral paling kuat ke paling lemah.
4. Untuk 3 produk teratas, tulis 1 ide angle konten singkat yang relevan dengan niche & target
   audiens (bukan generik "buat video review").

OUTPUT — HARUS JSON valid, tanpa teks lain di luar JSON:
{
  "generated_at": "YYYY-MM-DD",
  "niche": "...",
  "products": [
    {
      "rank": 1,
      "product_name": "...",
      "marketplace": "...",
      "viral_evidence": "...",
      "why_relevant": "...",
      "content_angle_idea": "...",
      "source_url": "...",
      "data_as_of": "YYYY-MM-DD"
    }
  ],
  "note_if_insufficient_data": "..."
}
```

## 3. Alur setelah AI Agent (saran wiring n8n)

```
[Edit Fields: 6 field di atas]
        ↓
[AI Agent node + tool pencarian web]  ← prompt di section 2
        ↓
[Parse JSON output]
        ↓
   ┌────┴─────┐
   ↓          ↓
[Creatomate]  [Telegram]
render visual  kirim ringkasan
promo produk   top 3 produk +
teratas pakai  angle konten ke
creatomate_    telegram_chat_id
template_id
```

- **Node Creatomate**: pakai `creatomate_template_id` sebagai template, isi variabel template dengan
  `product_name` + `content_angle_idea` dari produk rank 1 (atau loop untuk top 3).
- **Node Telegram**: kirim pesan terformat ke `telegram_chat_id` berisi ringkasan produk (nama,
  marketplace, kenapa viral, angle konten) — supaya tim bisa langsung review sebelum produksi konten.

## Catatan penting

- **Tool pencarian wajib aktif.** Tanpa akses browsing/search real-time, AI Agent akan cenderung
  mengarang nama produk yang "terdengar masuk akal" tapi tidak benar-benar sedang viral — ini
  fabrikasi data, bukan riset. Uji dulu tool pencariannya sebelum menyambungkan ke Creatomate/Telegram
  supaya tim tidak memproduksi konten berdasarkan data palsu.
- **Isi `product_niche` sebelum tiap run** — field ini sengaja dikosongkan (general-purpose), bukan
  di-hardcode ke satu brand/niche tertentu.
- Kalau nanti mau dipakai khusus untuk niche kopi/coffee shop (mis. AL's Coffee & Eatery / Tricarya
  Coffee Roastery mencari produk aksesori kopi yang lagi viral), tinggal isi `product_niche` dengan
  "aksesori & merchandise kopi" dan `target_marketplace`/`target_audience` disesuaikan — struktur
  prompt-nya tidak perlu diubah.
