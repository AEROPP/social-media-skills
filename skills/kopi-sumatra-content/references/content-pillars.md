# Sistem Pilar Konten & Rotasi (untuk skala 100 video/hari)

Membuat 100 video *benar-benar unik* dari nol setiap hari tidak realistis kalau ditulis manual satu-satu.
Solusinya: sistem kombinatorial — **Pilar (topik) × Format (bentuk penyampaian) × Kategori Footage
(lokasi visual) × Narator (gaya suara)**. Setiap kombinasi menghasilkan sudut video yang berbeda
meski topik dasarnya sama, dan jumlah kombinasi jauh lebih besar dari 100/hari sehingga video tidak
berulang persis selama berhari-hari.

Karena videonya sekarang **real-footage berlisensi/reusable** (lihat
`references/sumber-footage-berlisensi.md`), footage boleh dipakai ulang di banyak video — yang bikin
tiap video tetap terasa beda adalah kombinasi naskah/fakta/sudut cerita di bawah ini, bukan selalu
footage baru.

`scripts/generate_batch.py` mengimplementasikan rotasi ini secara deterministik (berbasis tanggal) supaya
setiap hari dapat batch baru tanpa duplikat, dan seluruh kombinasi (900 total) baru berulang setelah
~9 hari — pada saat itu pun kombinasi fakta yang dipilih tiap pilar juga dirotasi.

## Pilar (10) — "apa yang dijelaskan"

| id | Nama | Contoh sudut |
|---|---|---|
| `asal_usul` | Asal-usul & Geografi | Kenapa Gayo, Lintong, Mandheling punya rasa beda padahal satu pulau |
| `penanaman` | Penanaman & Perawatan | Butuh 3-4 tahun sebelum panen pertama |
| `panen` | Panen (Petik Merah) | Kenapa petani harus panen manual, bukan diborong |
| `giling_basah` | Proses Giling Basah (ciri khas Sumatra) | Rahasia biji hijau kebiruan khas Sumatra |
| `sortasi_fermentasi` | Sortasi & Fermentasi | Bagaimana biji cacat disortir jadi grade 1 |
| `roasting` | Proses Roasting | Kenapa Sumatra sering di-roast medium-dark |
| `brewing` | Metode Seduh | Kopi saring/tarik khas Aceh vs french press |
| `cita_rasa` | Karakter Rasa & Cupping | Kenapa rasanya earthy bukan asam |
| `budaya` | Budaya Ngopi & Petani | Warung kopi sebagai pusat sosial Aceh |
| `mitos_fakta` | Mitos vs Fakta | "Kopi Sumatra = kopi luwak"? Salah! |

Bank fakta per pilar ada di `references/riset-kopi-sumatra.md` dan dipakai `generate_batch.py` untuk
mengisi hook/body otomatis.

## Format (10) — "bagaimana disampaikan"

| id | Nama | Struktur singkat |
|---|---|---|
| `hook_fakta_cepat` | Fakta Cepat | Hook mengejutkan → 1 fakta → CTA (15-20s) |
| `pov_kunjungan` | POV Kunjungan Kebun | Kamera POV jalan-jalan di kebun/kilang, host narasi |
| `day_in_life` | Day in the Life | Ikuti rutinitas host dari pagi ke sore |
| `tutorial_mini` | Tutorial Mini | Langkah 1-2-3 cara melakukan sesuatu |
| `mitos_vs_fakta` | Mitos vs Fakta | Klaim populer → dibantah/dikonfirmasi dengan fakta |
| `versus` | Perbandingan | A vs B (mis. giling basah vs washed) side-by-side |
| `asmr_proses` | ASMR Proses | Fokus visual+suara proses (giling, sangrai, tuang) minim dialog |
| `sejarah_singkat` | Sejarah Singkat | Asal-usul/latar belakang topik dalam garis waktu singkat |
| `tanya_jawab` | Tanya Jawab Interaktif | Host lempar pertanyaan ke penonton, jawab di akhir |
| `behind_the_scenes` | Di Balik Layar | Sisi "belum banyak orang tahu" dari sebuah proses |

## Kategori Footage (3) — jenis lokasi/visual yang dicari di perpustakaan footage

1. **Kebun dataran tinggi** (mewakili Gayo/Lintong) — kabut pagi, barisan pohon kopi di bawah naungan,
   tangan memetik ceri merah, tanah vulkanik.
2. **Rumah giling & roastery** (mewakili proses pascapanen Mandailing) — mesin pulper/huller manual,
   karung goni, drum roasting, sortasi biji.
3. **Warung kopi & brewing** — kopi saring/tarik khas Aceh, cupping table, suasana warung kopi sebagai
   ruang sosial.

Kategori ini dipakai sebagai kata kunci pencarian ke perpustakaan footage/stock (lihat
`templates/shot-list-footage-template.md`), bukan lagi deskripsi visual untuk prompt AI.

## Narator (3) — gaya suara voiceover, bukan karakter tampil di kamera

Karena videonya real-footage (B-roll), "host" di sini adalah **gaya bicara narator** untuk voiceover —
tidak perlu difilmkan kecuali memang ingin menambahkan on-camera host asli suatu saat nanti.

1. **Pak Bahri** — suara tenang & bersahaja, seperti berbagi cerita ke tetangga; cocok untuk pilar
   penanaman/panen/giling basah/budaya.
2. **Kak Nur** — suara energik & presisi, seperti menjelaskan ke calon roaster; cocok untuk pilar
   roasting/brewing/cita rasa/sortasi.
3. **Adit** — suara penasaran & antusias, sering melempar pertanyaan balik ke penonton; cocok untuk
   pilar asal-usul/mitos-fakta dan format tanya jawab.

## Cara kerja rotasi

`generate_batch.py --date YYYY-MM-DD --count 100` menghasilkan 100 baris
`(pilar, format, kategori footage, narator)` unik untuk tanggal itu, diambil dari total 10×10×3×3 = 900
kombinasi, tanpa mengulang kombinasi yang sama dalam satu siklus ±9 hari. Setiap baris lalu diisi teks
(hook, beat isi, CTA) dari bank fakta pilar terkait + gaya bicara narator, plus kata kunci shot list
footage dan metadata siap pakai.

Gunakan output generator sebagai **kerangka/first draft** — tetap baca ulang dan sunting sebelum publish,
terutama untuk memastikan variasi kalimat tidak terasa robotic kalau ditonton berurutan.
