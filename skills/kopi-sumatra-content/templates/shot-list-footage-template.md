# Template Shot List & Sumber Footage (per video)

Ganti template prompt AI video dengan daftar shot yang dicocokkan ke **perpustakaan footage berlisensi**
yang sudah dimiliki (lihat `references/sumber-footage-berlisensi.md`), atau ke pencarian baru kalau
belum ada klip yang cocok.

```
Judul internal   : [pilar] / [format] / eps [nomor]
Narator (suara)  : [Pak Bahri | Kak Nur | Adit] - gaya bicara saja, tidak tampil di kamera kecuali
                    memang difilmkan sendiri
Durasi target    : [xx] detik

SHOT 1 (establishing, ~4-6 detik)
  Kata kunci pencarian : "[mis. misty highland coffee plantation aerial]"
  Sumber terpilih      : [Pustaka internal #id | Pexels URL | Shutterstock ID]
  Lisensi              : [CC0 | Standard | Enhanced | Milik sendiri]
  Catatan views cap    : [n/a | pantau kalau mendekati 500rb views (Shutterstock Standard)]

SHOT 2 (isi, ~5-6 detik)
  Kata kunci pencarian : [...]
  Sumber terpilih      : [...]
  Lisensi              : [...]

SHOT 3 (isi, opsional, ~5-6 detik)
  Kata kunci pencarian : [...]
  Sumber terpilih      : [...]
  Lisensi              : [...]

Overlay grafis/data (nilai tambah asli, wajib ada minimal 1)
  : [mis. peta kecil animasi lokasi Gayo/Lintong/Mandailing, angka ketinggian mdpl, perbandingan
     giling basah vs washed dalam infografis singkat]

Voiceover script  : lihat templates/skrip-template.md untuk hook/beat/CTA
```

## Contoh terisi (pilar `giling_basah`, format `mitos_vs_fakta`)

```
Judul internal   : Proses Giling Basah / Mitos vs Fakta / Eps 12
Narator (suara)  : Kak Nur
Durasi target    : 25 detik

SHOT 1 (establishing)
  Kata kunci pencarian : "wooden coffee mill house Sumatra worker manual huller"
  Sumber terpilih      : Pustaka internal #RG-014
  Lisensi              : Shutterstock Standard (klip dibeli, sudah dipakai di 6 video lain)
  Catatan views cap    : belum mendekati 500rb akumulasi, aman

SHOT 2 (isi)
  Kata kunci pencarian : "close up wet coffee parchment beans hand"
  Sumber terpilih      : Pustaka internal #RG-021
  Lisensi              : Shutterstock Standard

SHOT 3 (isi)
  Kata kunci pencarian : "green coffee beans bluish grey color sorting"
  Sumber terpilih      : Pexels (CC0)
  Lisensi              : CC0

Overlay grafis/data
  : Perbandingan visual "Giling Basah (Sumatra)" vs "Washed Process (umum)" - 3 poin beda cepat.

Voiceover script  : "Kenapa biji kopi Sumatra warnanya kebiruan? Ternyata bukan rusak..."
```

## Cara kerja dengan generator

`scripts/generate_batch.py` mengisi kolom "Kata kunci pencarian" secara otomatis berdasarkan
pilar+setting yang dirotasi hari itu. Kolom "Sumber terpilih" dan "Lisensi" **diisi manual** setelah
mencocokkan ke perpustakaan footage internal (spreadsheet/folder terpisah) atau mencari klip baru —
generator tidak bisa menebak koleksi footage yang sudah kamu miliki.
