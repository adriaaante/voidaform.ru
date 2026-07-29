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

  <link rel="preload" href="../assets/fonts/montserrat-cyrillic.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="../assets/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>
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
      <a class="logo" href="../" aria-label="Void &amp; Form — на главную">
        <svg class="logo__mark" viewBox="-3 -3 206 206" aria-hidden="true">
          <path d="M0 100V0h200v100a100 100 0 0 1-200 0Z" fill="none" stroke="currentColor" stroke-width="5.4"/>
        </svg>
        <span class="logo__text">Void &amp; Form</span>
      </a>
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
      <div class="container">
        <div style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:28px">
          <h2 class="section-title reveal" style="max-width:12em">Хотите так же — но по-своему?</h2>
          <a class="btn reveal" href="../index.html#contacts">Обсудить проект</a>
        </div>
        <nav class="project-nav" aria-label="Другие проекты">
          <a href="{prev_slug}.html">← {prev_name}</a>
          <a href="{next_slug}.html">{next_name} →</a>
        </nav>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container">
      <div class="footer__top">
        <a class="footer__logo" href="../" aria-label="Void &amp; Form — на главную">
          <svg viewBox="-1.5 -1.5 291 203" aria-hidden="true">
            <g fill="none" stroke="currentColor" stroke-width="2.7">
              <path d="M44 70V0h200v70"/>
              <path d="M48.606 130A100 100 0 0 0 239.394 130"/>
              <rect x="0" y="70" width="288" height="60"/>
            </g>
            <text x="144" y="112.8" text-anchor="middle" textLength="234.7" lengthAdjust="spacingAndGlyphs"
                  font-family="Montserrat, Helvetica, Arial, sans-serif" font-size="36.6" font-weight="500" fill="currentColor">VOID &amp; FORM</text>
          </svg>
        </a>
        <nav class="footer__nav" aria-label="Навигация в подвале">
          <a href="../index.html#projects">Проекты</a>
          <a href="../index.html#services">Услуги</a>
          <a href="../index.html#process">Процесс</a>
          <a href="../index.html#contacts">Контакты</a>
          <a href="../privacy.html">Политика конфиденциальности</a>
        </nav>
        <div class="footer__contact">
          <a class="footer__phone" href="tel:+79876543210">+7 (987) 654-32-10</a>
          <span>Москва и Московская область</span>
        </div>
      </div>
      <div class="footer__bottom">
      <span>© 2026 Void &amp; Form · Авторское дизайн-бюро</span>
      <a href="https://futureflow.ru" target="_blank" rel="noopener" aria-label="Сделано в FutureFlow"
   style="display:inline-flex;align-items:center;gap:8px;color:inherit;text-decoration:none;font:600 12.5px/1 system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif">
  <svg width="20" height="20" viewBox="0 0 32 32" fill="none" stroke="url(#ffGrad)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <defs><linearGradient id="ffGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c8dcf4"/><stop offset=".5" stop-color="#fff"/><stop offset="1" stop-color="#f5a623"/></linearGradient></defs>
    <rect x="8" y="8" width="16" height="16" rx="2.5"/>
    <path d="M12 8V4M16 8V4M20 8V4 M12 28V24M16 28V24M20 28V24 M8 12H4M8 16H4M8 20H4 M28 12H24M28 16H24M28 20H24"/>
  </svg>
  <span>Сделано в&nbsp;<span style="font-weight:700;background:linear-gradient(90deg,#c8dcf4,#fff 50%,#f5a623);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent">FutureFlow</span></span>
</a>
      </div>
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
