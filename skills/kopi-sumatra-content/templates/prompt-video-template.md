# Template Prompt Text-to-Video (per shot)

Satu video pendek = 2-5 klip AI (masing-masing ~4-10 detik) yang disambung saat editing. Tulis satu
prompt per shot memakai kerangka ini (isi tiap `[...]` sesuai `references/gaya-visual-anime.md`):

```
[GAYA GLOBAL]
2D anime style, hand-drawn look inspired by Studio Ghibli warmth, clean lineart, soft cel-shading,
warm earthy color palette (terracotta, moss green, warm brown, cream), gentle natural lighting,
painterly background, no on-screen text, no watermark, no logo.

[KARAKTER]
[deskripsi lengkap host dari character sheet, mis. "Pak Bahri, man in his mid-50s, tanned skin,
thin greying moustache, woven bamboo hat, rolled-up flannel shirt, sarong tied at waist, carrying
a woven harvest basket"]

[SETTING]
[deskripsi lengkap setting dari setting sheet, mis. "misty highland coffee farm at sunrise, rows of
coffee trees under shade trees, dark volcanic soil"]

[AKSI SHOT INI]
[aksi spesifik, 1 kalimat, mis. "he gently picks a ripe red coffee cherry and holds it up to the light"]

[KAMERA]
[mis. "slow push-in close-up on his hand and the cherry"]

[MOOD/PENCAHAYAAN]
[mis. "soft golden morning light, light mist in the background"]

[DURASI]
[4-10 detik sesuai batas tool]

Negative prompt: distorted hands, extra fingers, blurry face, text artifacts, logo, watermark,
realistic photo, 3D render.
```

## Contoh terisi (shot 1 dari video "Giling Basah", host Pak Bahri, setting Rumah Giling Mandailing)

```
2D anime style, hand-drawn look inspired by Studio Ghibli warmth, clean lineart, soft cel-shading,
warm earthy color palette (terracotta, moss green, warm brown, cream), gentle natural lighting,
painterly background, no on-screen text, no watermark, no logo.

Pak Bahri, man in his mid-50s, tanned skin, thin greying moustache, woven bamboo hat, rolled-up
flannel shirt, sarong tied at waist.

Semi-open wooden mill house, manual pulper and huller machines, stacked burlap sacks, warm
afternoon light through wooden slats.

He feeds damp parchment coffee beans into a manual huller and turns the hand crank.

Camera: medium shot, slight pan following the crank motion.

Mood: warm, industrious, focused afternoon light with visible dust motes in the air.

Duration: 6 seconds.

Negative prompt: distorted hands, extra fingers, blurry face, text artifacts, logo, watermark,
realistic photo, 3D render.
```

## Tips Produksi

- Simpan deskripsi karakter/setting persis sama (copy-paste) di semua prompt agar konsisten —
  jangan parafrase ulang tiap kali.
- Kalau tool text-to-video mendukung *reference image* atau *character consistency/seed*, gunakan
  fitur itu di atas deskripsi teks untuk hasil lebih stabil.
- Voiceover/narasi dan caption on-screen ditambahkan di tahap **editing**, bukan di dalam prompt
  text-to-video (kebanyakan tool belum reliable untuk lip-sync + teks dalam frame).
