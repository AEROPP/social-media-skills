#!/usr/bin/env python3
"""Generate a day's batch of Kopi Sumatra short-video concepts.

This produces SCRIPTS and a FOOTAGE SHOT LIST (search keywords) for real, licensed B-roll —
not AI video-generation prompts. See references/sumber-footage-berlisensi.md for why: footage
should come from a reusable licensed library (Shutterstock, CC0 sources, or footage shot on
location), matched against these keywords, not generated synthetically.

Rotates Pilar x Format x Kategori-Footage x Narator (10x10x3x3 = 900 combinations) deterministically
by date so each day gets `count` non-repeating combos, and the full set only cycles back
after ~900/count days (with facts also rotated to keep repeats from feeling identical).

Usage:
    python generate_batch.py --date 2026-08-07 --count 100 --out-dir ../../../output/2026-08-07
"""
import argparse
import csv
import itertools
import json
import random
from datetime import date, datetime
from pathlib import Path

PILLARS = {
    "asal_usul": {
        "name": "Asal-usul & Geografi",
        "facts": [
            "Tiga sentra utama kopi Sumatra: Gayo (Aceh), Lintong, dan Mandailing (Sumatera Utara).",
            "Kopi Gayo ditanam di ketinggian 1.100-1.700 mdpl, salah satu tertinggi di Indonesia.",
            "Nama 'Mandheling' yang terkenal di pasar dunia berasal dari daerah Mandailing, Sumut.",
            "Sebagian besar kopi Sumatra ditanam petani kecil dengan lahan 0,5-2 hektar.",
            "Banyak kebun Sumatra tergabung koperasi untuk sertifikasi organik & Fair Trade.",
            "Sumatra didominasi kopi Arabika di dataran tinggi, bukan Robusta.",
        ],
    },
    "penanaman": {
        "name": "Penanaman & Perawatan",
        "facts": [
            "Butuh 3-4 tahun sejak tanam sebelum pohon kopi berbuah untuk pertama kali.",
            "Pohon kopi ditanam di bawah naungan lamtoro atau sengon agar tidak kena matahari langsung.",
            "Ketinggian dan suhu dingin dataran tinggi memperlambat pematangan ceri kopi.",
            "Pohon kopi yang dirawat baik bisa terus produktif berbuah selama puluhan tahun.",
            "Kebun rakyat Sumatra umumnya semi-organik, pupuk dari kompos & sisa panen sendiri.",
            "Naungan pohon juga membantu menjaga kelembapan tanah di musim kering.",
        ],
    },
    "panen": {
        "name": "Panen (Petik Merah)",
        "facts": [
            "Kopi kualitas terbaik dipanen manual, hanya ceri yang sudah merah matang (petik merah).",
            "Memetik ceri yang belum matang bisa merusak rasa akhir secangkir kopi.",
            "Satu pohon kopi biasanya dipanen bertahap beberapa kali karena kematangan tidak serentak.",
            "Musim panen raya di Sumatra mengikuti pola hujan setempat, beda tiap daerah.",
            "Petani berpengalaman bisa menilai kematangan ceri hanya dari warna dan sedikit tekanan jari.",
            "Panen adalah tahap paling padat karya dalam seluruh rantai produksi kopi.",
        ],
    },
    "giling_basah": {
        "name": "Proses Giling Basah (ciri khas Sumatra)",
        "facts": [
            "Giling basah (wet-hulling) adalah proses pascapanen unik yang cuma umum di Sumatra.",
            "Kulit tanduk yang masih lembap langsung digiling, bukan dikeringkan penuh dulu seperti proses washed biasa.",
            "Proses giling basah membuat biji hijau Sumatra berwarna kebiruan/keabu-abuan yang khas.",
            "Giling basah menghasilkan body kopi yang sangat tebal dan keasaman yang rendah.",
            "Rasa earthy, herbal, dan rempah khas kopi Sumatra berasal dari proses giling basah ini.",
            "Giling basah berkembang sebagai solusi petani menghadapi cuaca tropis yang lembap.",
        ],
    },
    "sortasi_fermentasi": {
        "name": "Sortasi & Fermentasi",
        "facts": [
            "Setelah giling basah, biji kopi disortasi manual untuk membuang biji cacat atau berlubang.",
            "Grading seperti 'Mandheling Grade 1' ditentukan dari jumlah cacat per 300 gram sampel.",
            "Fermentasi semalam sebelum dicuci membantu melepaskan lapisan lendir di kulit tanduk.",
            "Sortasi manual biasanya dikerjakan ibu-ibu di sekitar kebun sebagai sumber penghasilan tambahan.",
            "Biji hitam dan biji pecah adalah dua jenis cacat paling umum yang disortir keluar.",
            "Kualitas sortasi sangat memengaruhi harga jual kopi ke eksportir.",
        ],
    },
    "roasting": {
        "name": "Proses Roasting",
        "facts": [
            "Karena body-nya tebal, kopi Sumatra sering di-roast pada level medium hingga dark.",
            "Roasting level dark membantu menonjolkan rasa earthy dan rempah kopi Sumatra.",
            "Roaster modern mulai eksperimen roast medium/light untuk mengungkap rasa buah tersembunyi.",
            "Suhu dan waktu roasting yang tepat menentukan apakah rasa jadi gosong atau kaya rasa.",
            "First crack dan second crack adalah dua penanda penting dalam proses roasting kopi.",
            "Biji kopi kehilangan berat dan berubah warna drastis selama proses roasting.",
        ],
    },
    "brewing": {
        "name": "Metode Seduh",
        "facts": [
            "French press dan moka pot sangat cocok untuk menonjolkan body tebal kopi Sumatra.",
            "Kopi saring khas Aceh diseduh lalu 'ditarik' bolak-balik antar wadah seperti teh tarik.",
            "Teknik tarik pada kopi Aceh menghasilkan buih dan melarutkan rasa lebih merata.",
            "Pour-over V60 kurang umum untuk kopi Sumatra karena keasamannya yang rendah.",
            "Warung kopi Aceh sering menyajikan kopi saring dengan gula yang sudah dicampur dari awal.",
            "Ukuran gilingan (grind size) sangat memengaruhi rasa akhir dari metode seduh apapun.",
        ],
    },
    "cita_rasa": {
        "name": "Karakter Rasa & Cupping",
        "facts": [
            "Kopi Sumatra dikenal dengan rasa earthy, herbal, dan rempah yang khas.",
            "Body kopi Sumatra sangat tebal, sering digambarkan seperti sirup (syrupy).",
            "Keasaman kopi Sumatra tergolong rendah-sedang dibanding kopi washed dari negara lain.",
            "Sebagian lot kopi Sumatra punya sentuhan rasa cokelat atau karamel yang lembut.",
            "Cupping adalah metode standar industri untuk menilai rasa kopi secara objektif.",
            "After-taste kopi Sumatra biasanya bertahan lama di lidah.",
        ],
    },
    "budaya": {
        "name": "Budaya Ngopi & Petani",
        "facts": [
            "Warung kopi adalah pusat sosial di Aceh, tempat diskusi hingga transaksi bisnis.",
            "Rantai pasok kopi Sumatra: petani, pengepul/koperasi, prosesor, eksportir, lalu kafe.",
            "Perubahan iklim membuat pola musim panen kopi Sumatra makin sulit diprediksi.",
            "Regenerasi petani muda jadi tantangan nyata bagi keberlanjutan kebun kopi Sumatra.",
            "Banyak petani Sumatra mewarisi kebun kopi dari orang tua turun-temurun.",
            "Harga kopi dunia yang fluktuatif berdampak langsung pada pendapatan petani kecil.",
        ],
    },
    "mitos_fakta": {
        "name": "Mitos vs Fakta",
        "facts": [
            "Tidak semua kopi Sumatra adalah kopi luwak - luwak hanya sebagian sangat kecil dari produksi.",
            "Kopi mahal tidak selalu berarti kopi enak - cocok di lidah lebih penting dari harga.",
            "Kopi Sumatra bukan kopi 'paling pahit' - rasa pahit berlebih biasanya tanda over-roast, bukan ciri asal.",
            "Warna biji hijau kebiruan bukan tanda kopi rusak, itu justru ciri khas proses giling basah.",
            "Kafein tidak berkurang karena roast lebih gelap - itu mitos yang sering dipercaya.",
            "Kopi Sumatra organik tidak otomatis berarti tanpa proses sama sekali - tetap melalui giling basah standar.",
        ],
    },
}

ANGLES = {
    # Short topic phrases (no leading capital, no trailing period) used to fill hook templates
    # like "kenapa {topic_lower}?" or "katanya {topic_lower}." — kept separate from `facts`
    # (which are full sentences for body beats) so hooks read naturally.
    "asal_usul": [
        "gayo, lintong, dan mandailing punya rasa kopi yang beda padahal satu pulau",
        "kopi gayo ditanam di dataran setinggi ini",
        "nama mandheling begitu terkenal di pasar dunia",
        "petani kecil mendominasi produksi kopi sumatra",
        "banyak kebun sumatra ikut sertifikasi organik",
        "sumatra lebih banyak arabika daripada robusta",
    ],
    "penanaman": [
        "pohon kopi butuh waktu lama sebelum berbuah",
        "pohon kopi ditanam di bawah naungan pohon lain",
        "dataran tinggi bikin ceri kopi matang lebih lambat",
        "pohon kopi bisa produktif puluhan tahun",
        "kebun kopi sumatra banyak yang semi-organik",
        "naungan pohon menjaga kelembapan tanah",
    ],
    "panen": [
        "petani harus panen manual satu-satu",
        "ceri yang belum merah tidak boleh dipetik",
        "satu pohon kopi dipanen berkali-kali",
        "musim panen tiap daerah di sumatra beda-beda",
        "petani bisa tahu ceri matang cuma dari warna",
        "panen jadi tahap paling padat karya",
    ],
    "giling_basah": [
        "biji kopi sumatra berwarna kebiruan",
        "proses giling basah cuma umum di sumatra",
        "kulit tanduk digiling saat masih basah",
        "kopi sumatra body-nya begitu tebal",
        "rasa earthy kopi sumatra berasal dari prosesnya",
        "petani sumatra mengembangkan giling basah",
    ],
    "sortasi_fermentasi": [
        "biji kopi disortir satu per satu pakai tangan",
        "grade kopi ditentukan dari jumlah biji cacat",
        "kopi difermentasi semalam sebelum dicuci",
        "sortasi manual jadi sumber penghasilan ibu-ibu sekitar kebun",
        "biji hitam harus disortir keluar",
        "sortasi memengaruhi harga jual kopi",
    ],
    "roasting": [
        "kopi sumatra sering di-roast gelap",
        "roasting gelap menonjolkan rasa rempah kopi sumatra",
        "roaster mulai coba roast lebih terang buat kopi sumatra",
        "suhu roasting menentukan rasa akhir kopi",
        "ada istilah first crack dan second crack saat roasting",
        "biji kopi berubah drastis saat di-roast",
    ],
    "brewing": [
        "french press cocok banget buat kopi sumatra",
        "kopi aceh diseduh dengan cara ditarik-tarik",
        "teknik tarik bikin kopi aceh berbuih",
        "v60 jarang dipakai buat kopi sumatra",
        "warung kopi aceh sudah campur gula dari awal",
        "ukuran gilingan memengaruhi rasa kopi",
    ],
    "cita_rasa": [
        "kopi sumatra rasanya earthy bukan asam",
        "body kopi sumatra setebal sirup",
        "keasaman kopi sumatra tergolong rendah",
        "ada kopi sumatra yang rasanya seperti cokelat",
        "cupping dipakai buat menilai rasa kopi secara resmi",
        "after-taste kopi sumatra tahan lama",
    ],
    "budaya": [
        "warung kopi jadi pusat sosial di aceh",
        "rantai kopi sumatra panjang dari petani sampai kafe",
        "perubahan iklim mengubah musim panen kopi",
        "anak muda mulai jarang mau jadi petani kopi",
        "kebun kopi diwariskan turun-temurun",
        "harga kopi dunia memengaruhi petani kecil",
    ],
    "mitos_fakta": [
        "semua kopi sumatra itu kopi luwak",
        "kopi mahal pasti lebih enak",
        "kopi sumatra itu kopi paling pahit",
        "biji kopi kebiruan artinya kopi rusak",
        "roast gelap bikin kafein berkurang",
        "kopi organik berarti tanpa proses sama sekali",
    ],
}

FOOTAGE_KEYWORDS = {
    # English stock-footage search phrases, aligned (same order/offset) with PILLARS[*]["facts"]
    # so the keyword picked for a beat matches the fact being narrated in that beat.
    "asal_usul": [
        "aerial highland coffee plantation Indonesia",
        "coffee farm misty mountains high altitude",
        "small map graphic Sumatra region overlay",
        "smallholder farmer coffee field",
        "coffee farmer cooperative meeting",
        "arabica coffee cherries close up branch",
    ],
    "penanaman": [
        "coffee seedling nursery young plants",
        "coffee trees shade grown canopy",
        "highland fog coffee plantation morning",
        "old coffee tree trunk plantation",
        "organic compost coffee farm soil",
        "shade tree coffee farm sunlight",
    ],
    "panen": [
        "farmer hand picking ripe red coffee cherries",
        "coffee cherries ripe red on branch",
        "harvest basket coffee cherries",
        "coffee farm harvest season rain",
        "close up hand selecting ripe coffee cherry",
        "farmers harvesting coffee manual labor",
    ],
    "giling_basah": [
        "wet coffee parchment beans pile",
        "manual coffee huller machine wood",
        "wet hulling coffee process Indonesia",
        "green coffee beans bluish grey color",
        "coffee pulping machine wet process",
        "coffee mill house rural Indonesia",
    ],
    "sortasi_fermentasi": [
        "hand sorting coffee beans defects table",
        "coffee grading quality control closeup",
        "coffee beans fermentation tank",
        "women sorting coffee beans village",
        "black defective coffee beans closeup",
        "coffee warehouse sacks grading",
    ],
    "roasting": [
        "coffee roasting drum machine smoke",
        "dark roasted coffee beans closeup",
        "coffee roaster monitoring temperature",
        "coffee beans first crack roasting",
        "roasting machine coffee shop interior",
        "coffee beans color change roasting process",
    ],
    "brewing": [
        "french press coffee pouring closeup",
        "traditional Aceh coffee pulled pouring",
        "coffee frothy pour traditional cloth filter",
        "pour over V60 coffee brewing",
        "traditional coffee shop Aceh serving",
        "coffee grinder grinding beans closeup",
    ],
    "cita_rasa": [
        "coffee cupping tasting spoon closeup",
        "thick coffee pour syrupy texture",
        "coffee tasting expression closeup",
        "coffee beans chocolate closeup aroma",
        "cupping session table multiple cups",
        "coffee cup steam closeup aftertaste",
    ],
    "budaya": [
        "traditional coffee shop Aceh interior people",
        "coffee farmer family portrait",
        "coffee plantation landscape climate",
        "young farmer coffee field portrait",
        "old coffee farmer talking legacy",
        "coffee market price board trading",
    ],
    "mitos_fakta": [
        "civet coffee luwak myth graphic",
        "expensive coffee beans premium closeup",
        "coffee cup dark roast pouring",
        "green coffee beans bluish myth closeup",
        "coffee roasting dark beans closeup",
        "organic coffee certification label",
    ],
}

FOOTAGE_CATEGORIES = {
    "kebun_dataran_tinggi": {
        "name": "Kebun dataran tinggi (Gayo/Lintong)",
        "establishing_keywords": "aerial misty highland coffee plantation sunrise Indonesia",
    },
    "giling_roastery": {
        "name": "Rumah giling & roastery (Mandailing)",
        "establishing_keywords": "wooden coffee mill house roastery interior Indonesia",
    },
    "warung_brewing": {
        "name": "Warung kopi & brewing",
        "establishing_keywords": "traditional Indonesian coffee shop interior warm light",
    },
}

FORMATS = {
    "hook_fakta_cepat": {
        "name": "Fakta Cepat",
        "duration": "15-20 detik",
        "beats": 1,
        "hook": "Tau nggak kenapa {topic_lower}?",
        "cta": "Follow biar kamu makin banyak tau fakta kopi Sumatra!",
    },
    "pov_kunjungan": {
        "name": "POV Kunjungan Kebun",
        "duration": "25-35 detik",
        "beats": 2,
        "hook": "POV: kamu baru sampai di {kategori_name} bareng {narator_name}.",
        "cta": "Komentar 'lanjut' kalau mau {narator_name} tunjukin tahap berikutnya!",
    },
    "day_in_life": {
        "name": "Day in the Life",
        "duration": "25-40 detik",
        "beats": 2,
        "hook": "Sehari mengikuti {narator_name} di {kategori_name}.",
        "cta": "Follow buat ikutin keseharian {narator_name} bikin kopi Sumatra tiap hari!",
    },
    "tutorial_mini": {
        "name": "Tutorial Mini",
        "duration": "20-30 detik",
        "beats": 2,
        "hook": "Begini cara {topic_lower}, gampang kok!",
        "cta": "Save video ini biar nggak lupa langkahnya!",
    },
    "mitos_vs_fakta": {
        "name": "Mitos vs Fakta",
        "duration": "20-30 detik",
        "beats": 2,
        "hook": "Katanya {topic_lower}. Beneran gitu?",
        "cta": "Follow biar kamu nggak salah kaprah soal kopi lagi!",
    },
    "versus": {
        "name": "Perbandingan",
        "duration": "25-35 detik",
        "beats": 2,
        "hook": "{kategori_name}: mari kita bandingkan dua sisi soal {topic_lower}.",
        "cta": "Menurut kamu mana yang lebih menarik? Komen di bawah!",
    },
    "asmr_proses": {
        "name": "ASMR Proses",
        "duration": "20-30 detik",
        "beats": 2,
        "hook": "Dengarkan dan lihat prosesnya baik-baik.",
        "cta": "Tenang banget ya prosesnya? Follow buat konten ASMR kopi lainnya!",
    },
    "sejarah_singkat": {
        "name": "Sejarah Singkat",
        "duration": "25-35 detik",
        "beats": 2,
        "hook": "Sejarah singkat kenapa {topic_lower}.",
        "cta": "Mau tau sejarah kopi lainnya? Follow ya!",
    },
    "tanya_jawab": {
        "name": "Tanya Jawab Interaktif",
        "duration": "20-30 detik",
        "beats": 1,
        "hook": "{narator_name} mau tanya: menurut kamu kenapa {topic_lower}?",
        "cta": "Tulis jawabanmu di komentar, nanti dijawab {narator_name} di video berikutnya!",
    },
    "behind_the_scenes": {
        "name": "Di Balik Layar",
        "duration": "25-35 detik",
        "beats": 2,
        "hook": "Ini sisi yang jarang orang lihat dari {topic_lower}.",
        "cta": "Follow buat lihat lebih banyak sisi di balik layar kopi Sumatra!",
    },
}

NARRATORS = {
    "bahri": {
        "name": "Pak Bahri",
        "voice": "tenang dan bersahaja, seperti berbagi cerita ke tetangga",
        "expertise": {"penanaman", "panen", "giling_basah", "sortasi_fermentasi", "budaya"},
    },
    "nur": {
        "name": "Kak Nur",
        "voice": "energik dan presisi, seperti menjelaskan ke calon roaster",
        "expertise": {"roasting", "brewing", "cita_rasa", "sortasi_fermentasi"},
    },
    "adit": {
        "name": "Adit",
        "voice": "penasaran dan antusias, sering bertanya balik ke penonton",
        "expertise": {"asal_usul", "mitos_fakta", "tanya_jawab"},
    },
}


def all_combos():
    return list(
        itertools.product(PILLARS.keys(), FORMATS.keys(), FOOTAGE_CATEGORIES.keys(), NARRATORS.keys())
    )


def combos_for_date(target_date: date, count: int):
    combos = all_combos()
    n = len(combos)
    pass_number = (target_date.toordinal() * count) // n
    rng = random.Random(f"kopi-sumatra-pass-{pass_number}")
    order = combos[:]
    rng.shuffle(order)
    start = (target_date.toordinal() * count) % n
    end = start + count
    if end <= n:
        return order[start:end]
    return order[start:] + order[: end - n]


def pick_facts(pilar_id: str, target_date: date, how_many: int):
    facts = PILLARS[pilar_id]["facts"]
    offset = target_date.toordinal() % len(facts)
    rotated = facts[offset:] + facts[:offset]
    return rotated[:how_many]


def pick_angle(pilar_id: str, target_date: date):
    angles = ANGLES[pilar_id]
    offset = target_date.toordinal() % len(angles)
    return angles[offset]


def pick_footage_keywords(pilar_id: str, target_date: date, how_many: int):
    keywords = FOOTAGE_KEYWORDS[pilar_id]
    offset = target_date.toordinal() % len(keywords)
    rotated = keywords[offset:] + keywords[:offset]
    return rotated[:how_many]


def build_video(pilar_id, format_id, kategori_id, narator_id, target_date, index):
    pilar = PILLARS[pilar_id]
    fmt = FORMATS[format_id]
    kategori = FOOTAGE_CATEGORIES[kategori_id]
    narator = NARRATORS[narator_id]

    beats_needed = fmt["beats"]
    facts = pick_facts(pilar_id, target_date, beats_needed)
    footage_keywords = pick_footage_keywords(pilar_id, target_date, beats_needed)
    topic_lower = pick_angle(pilar_id, target_date)

    hook = fmt["hook"].format(
        topic_lower=topic_lower, kategori_name=kategori["name"], narator_name=narator["name"]
    )
    cta = fmt["cta"].format(
        topic_lower=topic_lower, kategori_name=kategori["name"], narator_name=narator["name"]
    )
    beats = facts

    title = f"{pilar['name']} — {fmt['name']} ({narator['name']} @ {kategori['name']})"
    caption_on_screen = beats[0] if beats else hook

    # Shot list = search keywords to match against the licensed footage library, NOT AI prompts.
    # See references/sumber-footage-berlisensi.md and templates/shot-list-footage-template.md —
    # "source" and "license" must still be filled in by hand once a real clip is picked.
    shot_list = [
        {
            "shot": 1,
            "purpose": "establishing",
            "search_keywords": kategori["establishing_keywords"],
            "source": "",
            "license": "",
        }
    ]
    for i, keyword in enumerate(footage_keywords, start=2):
        shot_list.append(
            {
                "shot": i,
                "purpose": "isi",
                "search_keywords": keyword,
                "source": "",
                "license": "",
            }
        )

    hashtags = f"#kopisumatra #{pilar_id.replace('_','')} #edukasikopi #coffeetok"
    tiktok_caption = f"{hook} Eps {index}/100 🌱☕"
    yt_title = f"{title.split(' — ')[0]} #Shorts"
    yt_description = (
        f"{beats[0] if beats else hook} Eps {index}/100 seri Kopi Sumatra: Dari Kebun ke Cangkir. "
        f"#kopisumatra #edukasikopi #Shorts"
    )

    return {
        "index": index,
        "pilar": pilar_id,
        "pilar_name": pilar["name"],
        "format": format_id,
        "format_name": fmt["name"],
        "kategori_footage": kategori_id,
        "kategori_footage_name": kategori["name"],
        "narator": narator_id,
        "narator_name": narator["name"],
        "durasi_target": fmt["duration"],
        "judul_internal": title,
        "hook": hook,
        "beats": beats,
        "cta": cta,
        "caption_on_screen": caption_on_screen,
        "shot_list": shot_list,
        "tiktok_caption": tiktok_caption,
        "tiktok_hashtags": hashtags,
        "youtube_title": yt_title,
        "youtube_description": yt_description,
    }


def generate(target_date: date, count: int):
    combos = combos_for_date(target_date, count)
    return [
        build_video(pilar_id, format_id, kategori_id, narator_id, target_date, i + 1)
        for i, (pilar_id, format_id, kategori_id, narator_id) in enumerate(combos)
    ]


def write_outputs(videos, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "batch.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)

    csv_path = out_dir / "batch.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "index", "pilar", "format", "kategori_footage", "narator", "durasi_target",
                "judul_internal", "hook", "beats", "cta", "caption_on_screen",
                "footage_search_keywords", "tiktok_caption", "tiktok_hashtags",
                "youtube_title", "youtube_description",
            ]
        )
        for v in videos:
            writer.writerow(
                [
                    v["index"], v["pilar_name"], v["format_name"], v["kategori_footage_name"],
                    v["narator_name"], v["durasi_target"], v["judul_internal"], v["hook"],
                    " | ".join(v["beats"]), v["cta"], v["caption_on_screen"],
                    " | ".join(s["search_keywords"] for s in v["shot_list"]),
                    v["tiktok_caption"], v["tiktok_hashtags"], v["youtube_title"],
                    v["youtube_description"],
                ]
            )

    return json_path, csv_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD")
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--out-dir", default=None, help="Output directory (default: ./output/<date>)")
    args = parser.parse_args()

    target_date = datetime.strptime(args.date, "%Y-%m-%d").date()
    videos = generate(target_date, args.count)

    out_dir = Path(args.out_dir) if args.out_dir else Path("output") / args.date
    json_path, csv_path = write_outputs(videos, out_dir)
    print(f"Generated {len(videos)} video concepts for {args.date}")
    print(f"JSON: {json_path}")
    print(f"CSV:  {csv_path}")


if __name__ == "__main__":
    main()
