# Panduan Gaya Visual (Anime/Cartoon) untuk Text-to-Video

Tujuan: semua video terasa satu semesta visual yang sama meski dibuat terpisah-pisah oleh AI text-to-video,
dan karakter host tetap dikenali penonton dari video ke video.

## Gaya Global (masukkan di setiap prompt)

> 2D anime style, hand-drawn look inspired by Studio Ghibli warmth, clean lineart, soft cel-shading,
> warm earthy color palette (terracotta, moss green, warm brown, cream), gentle natural lighting,
> painterly background, no on-screen text, no watermark, no logo.

- **Palet warna** konsisten dengan tema kopi: coklat tanah, hijau daun kopi, terracotta atap seng,
  krem/kertas untuk highlight.
- **Negative prompt** (kalau tool mendukung): `distorted hands, extra fingers, blurry face, text artifacts,
  logo, watermark, realistic photo, 3D render`.
- Hindari elemen yang menyerupai merek/logo kopi nyata, atau wajah figur publik nyata.

## Character Sheet (jaga konsistensi lintas video)

### Pak Bahri (petani veteran)
- Pria ~55 tahun, kulit sawo matang, kumis tipis beruban, mengenakan topi anyaman bambu, kemeja flanel
  lengan digulung, sarung terselip di pinggang, membawa keranjang panen anyaman.
- Ekspresi tenang, gestur pelan dan meyakinkan.

### Kak Nur (Q Grader / roaster)
- Wanita ~28 tahun, rambut diikat kuncir tinggi, kacamata bulat, mengenakan apron denim di atas kaos
  polos, sering memegang cangkir cupping atau termometer roasting.
- Ekspresi fokus, gestur presisi/rapi.

### Adit (content explorer)
- Pria muda ~20 tahun, rambut pendek berantakan, jaket denim oversized, membawa "kamera" bergaya
  anime (efek genggam/POV), ekspresi antusias & penasaran.

Simpan deskripsi ini persis (atau referensi gambar karakter jika tool text-to-video mendukung
image-to-video/reference image) di setiap prompt yang memakai host tersebut, supaya wajah & pakaian
tidak berubah-ubah antar video.

## Setting Sheet

- **Kebun Gayo**: dataran tinggi berkabut, barisan pohon kopi di bawah naungan lamtoro, tanah vulkanik
  gelap, matahari pagi lembut menembus kabut.
- **Kebun Lintong**: perbukitan hijau, siluet Danau Toba & rumah adat Batak beratap tanduk kerbau di
  kejauhan, langit cerah.
- **Rumah Giling/Roastery Mandailing**: bangunan kayu semi-terbuka, mesin pulper/huller kayu-besi manual,
  karung goni bertumpuk, drum roasting kecil dengan api di bawahnya, asap tipis aromatik.

## Struktur Prompt per Shot

Tool text-to-video umumnya menghasilkan klip pendek (~4–10 detik). Video 15–45 detik = 2–5 klip yang
disambung saat editing, ditambah voiceover/narasi dan teks caption saat post-produksi (bukan di dalam
video AI itu sendiri). Gunakan `templates/prompt-video-template.md` untuk menulis setiap shot dengan
elemen: [gaya global] + [karakter] + [setting] + [aksi spesifik shot ini] + [gerakan kamera] + [mood/pencahayaan].

Contoh gerakan kamera yang berguna: *establishing wide shot*, *slow push-in*, *close-up on hands*,
*pan left following character*, *slow motion detail shot*.

## Kepatuhan Label Konten AI

Karena seluruh video dibuat dengan AI generative, **wajib** menyalakan/menyertakan label konten
AI-generated/synthetic yang disediakan TikTok dan YouTube saat upload (lihat
`references/platform-guidelines.md`). Ini bukan opsional — merupakan kebijakan platform untuk konten
sintetis yang menampilkan orang/tempat/kejadian yang tampak realistis, dan gaya anime/cartoon tidak
menghilangkan kewajiban ini di sebagian besar kasus (cek toggle "AI-generated content" saat upload).
