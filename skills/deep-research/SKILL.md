---
name: deep-research
description: >
  Menjalankan riset mendalam otomatis (iterative deep research) tentang topik apa pun, memakai
  tool "Open Deep Research" (agent Node.js/TypeScript, LLM + web search Firecrawl) yang di-vendor
  di `tool/` skill ini, lalu merangkum learnings & sumbernya untuk dipakai memperbarui/mengisi
  file riset seperti `skills/kopi-sumatra-content/references/riset-kopi-sumatra.md` atau riset
  dasar untuk seri konten media sosial baru. Gunakan skill ini setiap kali pengguna minta riset
  mendalam/terkini tentang suatu topik sebelum menulis skrip, minta "cari data/fakta terbaru
  tentang X", minta verifikasi klaim dengan sumber, atau minta menjalankan/menyiapkan tool
  deep-research — bahkan jika mereka tidak menyebut nama skill ini secara eksplisit.
---

# Deep Research — Riset Mendalam Otomatis untuk Materi Konten

## Apa ini

Tool open-source **"Open Deep Research"** (dzhng/deep-research, lisensi MIT) yang di-vendor di
`tool/` skill ini apa adanya. CLI TypeScript ringkas (<500 LoC) yang:

1. Men-generate beberapa SERP query dari topik memakai LLM.
2. Mencari & meng-scrape hasilnya lewat **Firecrawl**.
3. Mengekstrak *learnings* (fakta padat) + pertanyaan lanjutan dari tiap hasil.
4. Merekursi lebih dalam (sesuai parameter `depth`) memakai learnings sebagai konteks baru.
5. Menyusun semua learnings + daftar sumber jadi laporan markdown (`report.md`) atau jawaban
   ringkas (`answer.md`).

Lihat `tool/README.md` untuk dokumentasi upstream lengkap (diagram alur, opsi model lokal/R1, dst).

## Kapan dipakai di repo ini

Sebelum menulis atau memperbarui `references/riset-*.md` di skill konten mana pun (mis.
`kopi-sumatra-content`), atau saat memulai riset dasar untuk seri konten baru, kalau pengguna
butuh fakta/angka **terkini atau spesifik** yang berisiko di luar pengetahuan model dan minta
riset dijalankan otomatis (bukan cuma ditulis dari ingatan model).

Jangan pakai skill ini untuk menulis skrip/shot list/metadata itu sendiri — itu tugas skill
konten yang bersangkutan (mis. `kopi-sumatra-content`). Skill ini cuma menghasilkan **riset
mentah** yang jadi bahan baku.

## Yang WAJIB dicek dulu sebelum menjalankan

- **Butuh API key eksternal berbayar**: Firecrawl (search+scrape) dan OpenAI (`o3-mini`) atau
  Fireworks (DeepSeek R1). Jangan pernah asumsikan pengguna sudah punya — tanyakan dulu, dan
  minta mereka isi sendiri `tool/.env.local` (salin dari `tool/.env.example`). **Jangan pernah
  meminta pengguna menempel API key mereka ke chat**, dan jangan pernah commit `.env.local` atau
  kredensial apa pun ke repo ini.
- Setiap run melakukan panggilan API sungguhan (biaya token LLM + kuota Firecrawl) yang naik cepat
  seiring `breadth`/`depth` (jumlah query kira-kira bercabang `breadth` di tiap level, sampai
  `depth` level). Konfirmasi dulu ke pengguna sebelum menjalankan run dengan breadth/depth besar.
- Butuh Node.js (disarankan versi di `tool/.nvmrc`, 22.x) terpasang di environment yang menjalankan
  tool ini.
- Lihat `references/setup-dan-integrasi.md` untuk detail env var dan alur integrasi hasil riset.

## Cara pakai

1. `cd skills/deep-research/tool && npm install` (sekali saja).
2. Salin `.env.example` ke `.env.local` dan minta pengguna mengisi `FIRECRAWL_KEY` +
   `OPENAI_KEY` (atau `FIREWORKS_KEY` untuk DeepSeek R1) sendiri.
3. Jalankan interaktif: `npm start` — akan menanyakan topik, breadth (default 4), depth
   (default 2), dan mode `report`/`answer`, lalu pertanyaan follow-up untuk memperjelas arah
   riset.
   - Atau non-interaktif lewat API: `npm run api`, lalu `POST /api/research` atau
     `/api/generate-report` dengan body `{ query, breadth, depth }` (lihat `src/api.ts`).
4. Hasilnya tersimpan sebagai `report.md` atau `answer.md` di dalam `tool/`.
5. **Ekstrak manual**, jangan copy-paste mentah: ambil fakta yang relevan dan sumbernya
   (`visitedUrls`/bagian "Sources"), lalu masukkan ke `references/riset-*.md` skill konten yang
   dituju, dengan atribusi sumber. Cross-check klaim penting (angka, statistik, klaim kesehatan)
   ke sumber aslinya sebelum dipakai — keluaran LLM tetap bisa salah meski berbasis hasil scraping
   nyata.

## Batasan

- **Bukan pengganti verifikasi manusia.** Selalu cek ulang sumber untuk klaim sensitif (medis,
  hukum, kesehatan, kesejahteraan hewan) sebelum masuk ke skrip konten — lihat bagian
  "Sensitivitas & Kepatuhan Konten" di `skills/kopi-sumatra-content/references/riset-kopi-sumatra.md`
  sebagai contoh kehati-hatian yang dibutuhkan.
- Tool ini generik (tidak tahu format TikTok/YouTube Shorts) — outputnya riset mentah, bukan
  skrip, shot list, atau metadata upload.
- Kalau tidak ada API key yang tersedia dan pengguna tidak ingin membuatnya, jangan mencoba
  "mengganti" riset otomatis dengan mengarang fakta — tanyakan dulu apakah mau riset manual biasa
  atau ditunda.

## Struktur skill ini

```
deep-research/
├── SKILL.md                          (file ini)
├── references/
│   └── setup-dan-integrasi.md        detail env var, mode CLI vs API, alur integrasi hasil riset
└── tool/                              source asli "Open Deep Research" (vendored, MIT license)
    ├── README.md                      dokumentasi upstream lengkap
    ├── src/                           kode TypeScript (deep-research.ts, providers.ts, dst.)
    ├── package.json / package-lock.json
    └── .env.example                   template env var (isi sendiri, jangan commit .env.local)
```
