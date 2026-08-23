# Setup & Integrasi Deep Research

## Environment variables (`tool/.env.local`)

Salin dari `tool/.env.example`, lalu isi sesuai kebutuhan. Jangan pernah commit file ini.

| Variable              | Wajib?          | Keterangan                                                                 |
|-----------------------|-----------------|-----------------------------------------------------------------------------|
| `FIRECRAWL_KEY`       | Ya              | API key Firecrawl (search + scrape web).                                   |
| `FIRECRAWL_BASE_URL`  | Tidak           | Isi kalau pakai self-hosted Firecrawl, mis. `http://localhost:3002`.        |
| `FIRECRAWL_CONCURRENCY` | Tidak         | Default 2. Naikkan kalau Firecrawl paid/self-hosted supaya run lebih cepat; kalau free tier sering rate-limit, turunkan ke 1. |
| `OPENAI_KEY`          | Ya (kalau tidak pakai Fireworks) | Dipakai model `o3-mini` untuk generate query/learnings/report.  |
| `CONTEXT_SIZE`        | Tidak           | Default 128000 token, batas konteks yang dipakai untuk trimming prompt.     |
| `OPENAI_ENDPOINT` + `CUSTOM_MODEL` | Tidak | Untuk model lokal/OpenAI-compatible lain (Ollama, OpenRouter, dst).      |
| `FIREWORKS_KEY`       | Tidak           | Kalau diisi, otomatis pakai DeepSeek R1 lewat Fireworks, bukan `o3-mini`.   |

## Mode CLI vs API

- **CLI interaktif** (`npm start`): paling cocok untuk sesi riset satu kali yang ditanyakan
  langsung ke pengguna (breadth/depth/follow-up questions dijawab interaktif). Baik dijalankan
  langsung oleh Claude di sesi ini kalau env var sudah siap.
- **Server API** (`npm run api`, default port 3051): cocok kalau riset ini mau dipanggil berulang
  dari skrip lain atau automation n8n di masa depan (lihat `automation/` di root repo). Endpoint:
  - `POST /api/research` → `{ query, depth?, breadth? }` → balikan `{ answer, learnings, visitedUrls }`
  - `POST /api/generate-report` → sama, tapi balikan laporan markdown panjang.

Untuk kebutuhan repo ini (riset topik konten, bukan layanan yang jalan terus), mode CLI biasanya
cukup — jangan nyalakan server API kalau tidak benar-benar dibutuhkan.

## Alur integrasi hasil riset ke skill konten

1. Jalankan deep research untuk topik yang relevan dengan pilar konten (mis. "proses giling basah
   kopi Sumatra", "harga ekspor kopi Sumatra 2026", "isu kesejahteraan hewan kopi luwak").
2. Buka `report.md`/`answer.md` hasilnya, baca bagian "Sources"/`visitedUrls` — verifikasi
   ke sumbernya, bukan sekadar percaya ringkasan LLM-nya.
3. Tulis ulang fakta yang relevan dengan gaya `references/riset-kopi-sumatra.md` (atau file riset
   skill lain yang dituju): ringkas, cantumkan konteks (tahun/sumber kalau angka bisa berubah),
   dan tandai eksplisit kalau suatu angka perlu dicek ulang saat produksi karena bisa sudah usang.
4. Kalau riset menyentuh topik sensitif (kesehatan, hukum, kesejahteraan hewan), pastikan
   penulisan ulangnya konsisten dengan bagian "Sensitivitas & Kepatuhan Konten" pada file riset
   skill terkait — jangan biarkan klaim berisiko dari sumber pihak ketiga masuk begitu saja.
5. Hapus/jangan commit `report.md`/`answer.md` mentah dari `tool/` — itu hasil sementara, bukan
   deliverable. Deliverable-nya adalah suntingan yang sudah masuk ke `references/riset-*.md`.

## Biaya & skala

Jumlah query LLM + request Firecrawl per run kira-kira bertambah tiap level `depth` dengan faktor
`breadth` (lalu breadth mengecil separuh tiap level lebih dalam). Untuk riset topik konten biasa,
`breadth` 3-4 dan `depth` 1-2 biasanya cukup dan murah. Naikkan hanya kalau topiknya luas dan
pengguna sudah tahu implikasi biayanya — selalu konfirmasi dulu untuk run besar, konsisten dengan
prinsip "jangan asumsikan kredensial/biaya API sudah oke" di `automation/n8n-workflow-kopi-sumatra.md`.
