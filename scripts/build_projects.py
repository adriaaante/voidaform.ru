#!/usr/bin/env python3
"""Генерирует страницы проектов projects/*.html из данных PROJECTS.

Запуск из корня репозитория:  python3 scripts/build_projects.py
Источник данных — реальные дизайн-проекты из PDF-альбомов заказчика
(Google Drive, папка «Примеры работ»). Изображения лежат в assets/img/{slug}-*.jpg.
"""

import html
import pathlib

SITE = "https://voidaform.ru"

PROJECTS = [
    {
        "slug": "grafit",
        "name": "Графит",
        "type": "Квартира",
        "facts": [
            ("Тип", "Квартира"),
            ("Площадь", "47,6 м²"),
            ("Локация", "Москва, ЦАО, ЖК RedSide"),
            ("Год", "2019"),
        ],
        "area": "47,6 м²",
        "tag": "ЖК RedSide",
        "short": "Графит, олива и латунь: собранный интерьер в центре Москвы",
        "seo": "Дизайн-проект квартиры 47,6 м² в ЖК RedSide (Москва, Пресненский район): графитовая кухня, оливковые акценты, латунь, мрамор.",
        "text": [
            "Компактная квартира в ЖК RedSide на Пресне — пример того, как на 47 метрах разместить всё необходимое и не потерять воздух.",
            "Основа палитры — глубокий графит и серо-зелёные стены с классическими молдингами. Оливковый бархат, латунные светильники и тёмный мрамор кухни добавляют плотности, а светлый паркет «ёлочкой» удерживает баланс.",
            "Каждая зона продумана до сантиметра: барная стойка вместо громоздкого стола, гардеробная со стеклянными фасадами, санузел в камне с чёрной сантехникой.",
        ],
        "gallery": [
            ("grafit-1.jpg", True,  "Гостиная с угловым диваном и обеденной зоной — дизайн-проект квартиры 47,6 м² в ЖК RedSide"),
            ("grafit-2.jpg", True,  "Кухня с графитовым островом, барной стойкой и мраморным фартуком — проект «Графит»"),
            ("grafit-3.jpg", True,  "Столовая зона с овальным столом и стульями в оливковом бархате — проект «Графит»"),
            ("grafit-4.jpg", True,  "Спальня с оливковыми стенами и подвесными светильниками — проект «Графит»"),
            ("grafit-5.jpg", False, "Санузел в сером камне с чёрной сантехникой — проект «Графит»"),
            ("grafit-6.jpg", False, "Гардеробная со стеклянными фасадами и подсветкой — проект «Графит»"),
        ],
        "cover_alt": "Кухня с латунными деталями и барными стульями в оливковом бархате — дизайн-проект квартиры 47,6 м², ЖК RedSide",
    },
    {
        "slug": "akvarel",
        "name": "Акварель",
        "type": "Квартира",
        "facts": [
            ("Тип", "Четырёхкомнатная квартира"),
            ("Состав", "4 комнаты · 2 санузла"),
            ("Локация", "Москва, ЦАО, ЖК RedSide"),
            ("Год", "2019"),
        ],
        "area": "4 комнаты",
        "tag": "ЖК RedSide",
        "short": "Светлая семейная квартира: зелень, пудра и графичные перегородки",
        "seo": "Дизайн-проект четырёхкомнатной семейной квартиры в ЖК RedSide: светлая палитра, зелёные и пудровые акценты, стеклянные перегородки, детские комнаты.",
        "text": [
            "Четырёхкомнатная квартира для семьи с детьми: каждому — своя комната и свой характер, при этом дом звучит как единое целое.",
            "Общие зоны собраны на светлой основе: серый диван, паркет «ёлочкой», графичные стеклянные перегородки в чёрном профиле отделяют кухню, не отнимая света. Акценты — глубокий зелёный и латунь.",
            "Детские получили собственные палитры — пудрово-розовую и спокойную с деревом и спортивным уголком. Ванные — терраццо, оливковый потолок и цветные раковины: у каждой комнаты своя интонация.",
        ],
        "gallery": [
            ("akvarel-1.jpg", True,  "Гостиная с серым диваном и стеклянной перегородкой в чёрном профиле — четырёхкомнатная квартира в ЖК RedSide"),
            ("akvarel-2.jpg", True,  "Кухня с зелёными фасадами и островом за стеклянной перегородкой — проект «Акварель»"),
            ("akvarel-3.jpg", True,  "Столовая зона у окна с панорамным видом — проект «Акварель»"),
            ("akvarel-4.jpg", True,  "Спальня со светло-серой кроватью и зелёными шторами — проект «Акварель»"),
            ("akvarel-5.jpg", False, "Ванная с отделкой терраццо и цветными раковинами — проект «Акварель»"),
            ("akvarel-6.jpg", False, "Детская комната в пудрово-розовой гамме — проект «Акварель»"),
        ],
        "cover_alt": "Прихожая с круглым зеркалом и зелёной акцентной стеной — дизайн-проект четырёхкомнатной квартиры, ЖК RedSide",
    },
    {
        "slug": "glubina",
        "name": "Глубина",
        "type": "Квартира",
        "facts": [
            ("Тип", "Квартира"),
            ("Площадь", "159,6 м²"),
            ("Локация", "Москва, ЦАО, ЖК RedSide"),
            ("Год", "2019"),
        ],
        "area": "159,6 м²",
        "tag": "ЖК RedSide",
        "short": "Большая квартира в тёмных тонах: синий бархат, дерево, камин",
        "seo": "Дизайн-проект квартиры 159,6 м² в ЖК RedSide (ул. Сергея Макеева): тёмное дерево, синий бархат, мраморная кухня, камин, детская.",
        "text": [
            "Почти 160 метров на улице Сергея Макеева — простор, который позволил выстроить полноценные сценарии: парадная столовая, гостиная с камином, приватное крыло со спальнями.",
            "Характер задают глубокие тона: тёмное дерево, чёрный мрамор кухни, синий бархат кресел и штор. Хрустальная люстра над столом и латунная фурнитура добавляют парадности без пафоса.",
            "В приватной части — спокойная спальня с гардеробной, детская в голубой гамме с домиком-кроватью и библиотека с подсветкой, ведущая по коридору, как нить.",
        ],
        "gallery": [
            ("glubina-1.jpg", True,  "Гостиная с камином, серым диваном и креслами в синем бархате — квартира 159,6 м² в ЖК RedSide"),
            ("glubina-2.jpg", True,  "Парадная столовая с хрустальной люстрой и стульями в синем бархате — проект «Глубина»"),
            ("glubina-3.jpg", True,  "Кухня с чёрным мраморным островом и тёмными фасадами — проект «Глубина»"),
            ("glubina-4.jpg", True,  "Спальня в тёмном дереве с латунной люстрой — проект «Глубина»"),
            ("glubina-5.jpg", False, "Ванная с чёрными раковинами из мрамора и латунными светильниками — проект «Глубина»"),
            ("glubina-6.jpg", False, "Библиотека с подсветкой в коридоре — проект «Глубина»"),
        ],
        "cover_alt": "Коридор с книжными стеллажами и линейной подсветкой — дизайн-проект квартиры 159,6 м², ЖК RedSide",
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Проект «{name}» — {type_lc} {area} | Дизайн-бюро Void &amp; Form</title>
  <meta name="description" content="{seo} Дизайн-бюро Void & Form, Москва.">
  <link rel="canonical" href="{site}/projects/{slug}.html">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Void & Form">
  <meta property="og:locale" content="ru_RU">
  <meta property="og:title" content="Проект «{name}» — {type_lc} {area}">
  <meta property="og:description" content="{seo}">
  <meta property="og:url" content="{site}/projects/{slug}.html">
  <meta property="og:image" content="{site}/assets/img/{slug}-1.jpg">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" href="../favicon.svg" type="image/svg+xml">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Manrope:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Главная", "item": "{site}/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Проекты", "item": "{site}/#projects" }},
      {{ "@type": "ListItem", "position": 3, "name": "«{name}»", "item": "{site}/projects/{slug}.html" }}
    ]
  }}
  </script>
</head>
<body>

  <header class="header is-scrolled" id="header">
    <div class="container header__in">
      <a class="logo" href="../">Void <span>&amp;</span> Form</a>
      <nav class="nav" id="nav" aria-label="Основная навигация">
        <a href="../index.html#projects">Проекты</a>
        <a href="../index.html#about">Философия</a>
        <a href="../index.html#services">Услуги</a>
        <a href="../index.html#process">Процесс</a>
        <a href="../index.html#contacts">Контакты</a>
      </nav>
      <a class="header__phone" href="tel:+79876543210">+7 (987) 654-32-10</a>
      <button class="burger" id="burger" aria-label="Открыть меню" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <main>
    <section class="project-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Хлебные крошки">
          <a href="../">Главная</a><span>/</span><a href="../index.html#projects">Проекты</a><span>/</span><span>«{name}»</span>
        </nav>
        <h1>«{name}»</h1>
        <div class="project-facts">
{facts}
        </div>
      </div>
    </section>

    <section class="container" style="padding-bottom: clamp(48px, 7vw, 90px)">
      <div class="project-gallery">
{gallery}
      </div>
    </section>

    <section class="container">
      <div class="project-about reveal">
        <span class="section-label">О проекте</span>
        <h2 class="section-title" style="font-size: clamp(26px, 3vw, 38px)">{short}</h2>
{paragraphs}
      </div>
    </section>

    <section class="section section--soft">
      <div class="container" style="text-align:center">
        <h2 class="section-title reveal" style="margin: 0 auto 28px">Хотите так же — но по-своему?</h2>
        <a class="btn reveal" href="../index.html#contacts">Обсудить проект</a>
        <nav class="project-nav container" aria-label="Другие проекты">
          <a href="{prev_slug}.html">← «{prev_name}»</a>
          <a href="{next_slug}.html">«{next_name}» →</a>
        </nav>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer__in">
      <a class="logo" href="../">Void <span>&amp;</span> Form</a>
      <nav class="footer__nav" aria-label="Навигация в подвале">
        <a href="../index.html#projects">Проекты</a>
        <a href="../index.html#services">Услуги</a>
        <a href="../index.html#contacts">Контакты</a>
        <a href="../privacy.html">Политика конфиденциальности</a>
      </nav>
      <span>© 2026 Void &amp; Form · Авторское дизайн-бюро</span>
    </div>
  </footer>

  <div class="lightbox" id="lightbox" role="dialog" aria-label="Просмотр фотографии">
    <img src="" alt="">
  </div>

  <script src="../js/main.js" defer></script>
</body>
</html>
"""


def main() -> None:
    root = pathlib.Path(__file__).resolve().parent.parent
    out_dir = root / "projects"
    out_dir.mkdir(exist_ok=True)

    for i, p in enumerate(PROJECTS):
        prev_p = PROJECTS[i - 1]
        next_p = PROJECTS[(i + 1) % len(PROJECTS)]
        paragraphs = "\n".join(
            "        <p>{}</p>".format(html.escape(t)) for t in p["text"]
        )
        facts = "\n".join(
            '          <div class="fact"><div class="fact__label">{}</div>'
            '<div class="fact__value">{}</div></div>'.format(html.escape(k), html.escape(v))
            for k, v in p["facts"]
        )
        gallery_rows = []
        for idx, (img, wide, alt) in enumerate(p["gallery"]):
            cls = ' class="is-wide reveal"' if wide else ' class="reveal"'
            lazy = "" if idx == 0 else ' loading="lazy"'
            gallery_rows.append(
                '        <figure{cls}><img src="../assets/img/{img}" alt="{alt}"{lazy}></figure>'.format(
                    cls=cls, img=img, alt=html.escape(alt, quote=True), lazy=lazy
                )
            )
        page = TEMPLATE.format(
            site=SITE,
            slug=p["slug"],
            name=p["name"],
            type_lc=p["type"].lower(),
            area=p["area"],
            short=p["short"],
            seo=p["seo"],
            facts=facts,
            gallery="\n".join(gallery_rows),
            paragraphs=paragraphs,
            prev_slug=prev_p["slug"],
            prev_name=prev_p["name"],
            next_slug=next_p["slug"],
            next_name=next_p["name"],
        )
        (out_dir / (p["slug"] + ".html")).write_text(page, encoding="utf-8")
        print("written:", out_dir / (p["slug"] + ".html"))


if __name__ == "__main__":
    main()
