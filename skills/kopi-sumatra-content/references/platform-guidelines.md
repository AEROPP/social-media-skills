# Panduan Platform: TikTok Studio & YouTube Shorts

## TikTok

- **Rasio & durasi**: 9:16 vertikal. Untuk konten edukasi cepat, durasi ideal **15–34 detik** —
  cukup untuk hook + 1 insight + CTA tanpa kehilangan retention.
- **Hook**: harus terjadi di **1–2 detik pertama** (visual atau kalimat pembuka), karena algoritma
  TikTok sangat sensitif terhadap drop-off di awal.
- **Caption on-screen**: sertakan teks/caption terbakar di video (burned-in captions) — banyak
  penonton menonton tanpa suara.
- **Hashtag**: campuran niche + broad, contoh: `#kopisumatra #kopigayo #kopilintong #edukasikopi
  #coffeetok #baristatips #ngopi`. 3–6 hashtag cukup, jangan spam.
- **Series/numbering**: karena ini seri harian, beri penanda episode di judul/caption (mis. "Eps 12/100 —
  Kenapa Biji Kopi Sumatra Berwarna Kebiruan?") untuk mendorong penonton follow demi episode berikutnya.
- **Penjadwalan**: gunakan fitur scheduling TikTok Studio untuk menyebar 100 video sepanjang hari
  (jangan upload 100 sekaligus dalam satu jam — bisa dianggap spam oleh sistem & membanjiri feed followers).
  Sebar interval, misal setiap 10–15 menit dari jam 06.00–22.00.
- **Konten duplikat/template**: TikTok menurunkan jangkauan video yang terlihat seperti template/
  reused content tanpa nilai tambah (lihat bagian "Kebijakan Reused Content" di bawah — ini menggantikan
  kebutuhan label AI karena sumber videonya sekarang footage nyata, bukan AI-generated).
- **Label AI tetap perlu KALAU** memakai voiceover AI (text-to-speech) yang terdengar sangat mirip
  suara manusia asli — sebagian kebijakan TikTok soal audio sintetis realistis masih relevan; cek
  toggle "AI-generated content" khusus untuk komponen audio-nya kalau ragu.

## YouTube Shorts

- **Rasio & durasi**: 9:16, maksimal teknis 3 menit tapi untuk masuk kategori Shorts & rekomendasi
  optimal, usahakan **≤60 detik**.
- **Judul**: sertakan kata kunci pencarian relevan + `#Shorts` di akhir judul atau deskripsi, contoh:
  "Proses Giling Basah Kopi Sumatra yang Jarang Diketahui #Shorts".
- **Deskripsi**: 1-2 kalimat ringkasan + hashtag + (opsional) link ke video panjang/playlist terkait
  jika ada versi long-form dari seri ini.
- **Label AI/synthetic**: karena videonya footage nyata (bukan AI-generated), toggle "Altered or
  synthetic content" umumnya **tidak wajib** untuk bagian visual. Kalau voiceover memakai AI TTS yang
  sangat realistis, tetap baik menyalakan label ini untuk transparansi meski belum selalu diwajibkan
  ketat oleh YouTube untuk audio saja.

## Kebijakan Reused Content — wajib dipahami sebelum publish

Karena strategi produksi sekarang berbasis **footage yang dipakai ulang** dari perpustakaan berlisensi
(lihat `references/sumber-footage-berlisensi.md`), risiko terbesar bukan lagi hak cipta AI, tapi
**kebijakan "reused content"**:

- **YouTube (2026)**: video yang hanya menyambung klip + caption tanpa nilai tambah asli berisiko
  dianggap "reused content" → dibatasi monetisasi/distribusinya. Standar yang dipakai YouTube adalah
  **"replaceability"**: kalau kreator lain bisa dengan mudah mengunduh footage yang sama dan membuat
  ulang video yang setara, kanal berisiko diturunkan. Yang dianggap aman: narasi dengan analisis/insight
  asli, framing edukatif yang jelas berbeda dari sumber, editing yang membangun cerita — bukan sekadar
  klip disambung rapi.
- **TikTok**: konten yang terlihat template/berulang tanpa sudut baru juga cenderung diturunkan
  jangkauannya oleh sistem rekomendasi, meski tidak selalu berupa penalti eksplisit.
- **Implikasi untuk seri ini**: naskah (hook/beat/CTA dari sistem rotasi pilar) dan **overlay
  grafis/data** (lihat `templates/shot-list-footage-template.md`) menjadi elemen pembeda utama yang
  wajib kuat di setiap video — bukan sekadar pelengkap. Jangan pernah publish video yang cuma footage
  + caption generik tanpa narasi/insight.

## Strategi Umum untuk Skala 100 Video/Hari

1. **Bukan 100 ide acak** — pakai sistem rotasi pilar (lihat `content-pillars.md`) supaya tetap
   konsisten sebagai "satu channel edukasi", bukan terasa spam bervariasi tanpa arah.
2. **Quality gate sebelum upload**: walau dibuat sistematis, tetap ada 1 langkah review manusia
   (cek fakta, cek video AI tidak glitch/distorsi wajah, cek caption sudah benar) — terutama penting
   di awal sebelum proses benar-benar diotomasi penuh (lihat `automation/`).
3. **Analitik**: pantau retention & watch-through rate per pilar/format di TikTok Studio & YouTube
   Studio setelah 1-2 minggu; pangkas format yang performanya lemah, perbanyak yang kuat — sistem
   pilar memudahkan analisis ini karena setiap video punya tag pilar/format yang jelas (simpan di
   metadata internal, lihat kolom pada `output/`).
4. **Konsistensi jadwal**: penonton edukasi format seri menyukai kepastian jadwal (mis. selalu mulai
   jam 06.00 WIB) — bantu algoritma & kebiasaan audiens.
