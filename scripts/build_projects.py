#!/usr/bin/env python3
"""Генерирует страницы проектов projects/*.html из данных PROJECTS.

Запуск из корня репозитория:  python3 scripts/build_projects.py
При замене плейсхолдеров на реальные проекты — обновите PROJECTS и перезапустите.
"""

import html
import pathlib

SITE = "https://voidaform.ru"

PROJECTS = [
    {
        "slug": "tishina",
        "name": "Тишина",
        "type": "Апартаменты",
        "area": "127 м²",
        "duration": "7 месяцев",
        "scope": "Дизайн-проект · Ремонт под ключ · Комплектация",
        "location": "Москва",
        "short": "Светлый минимализм: известняк, кремовые оттенки, мягкий свет",
        "seo": "Дизайн-проект и ремонт апартаментов 127 м² в Москве: светлый минимализм, известняковая штукатурка, кремовая палитра.",
        "text": [
            "Заказчики попросили пространство, в котором можно отдыхать от города: без визуального шума, лишних предметов и ярких акцентов.",
            "Основой палитры стали тёплые оттенки слоновой кости и известняковая штукатурка. Свет — главный материал проекта: полупрозрачный лён на окнах рассеивает солнце, а скрытая подсветка мягко ведёт по квартире вечером.",
            "Скульптурный диван, травертин и дуб — немногие, но точные предметы. Всё остальное — воздух.",
        ],
        "alts": [
            "Светлая минималистичная гостиная с диваном кремового цвета и травертиновым столиком — проект «Тишина»",
            "Гостиная в оттенках слоновой кости с льняными шторами — проект «Тишина», дизайн-бюро Void & Form",
        ],
    },
    {
        "slug": "forma",
        "name": "Форма",
        "type": "Квартира",
        "area": "84 м²",
        "duration": "6 месяцев",
        "scope": "Дизайн-проект · Ремонт под ключ",
        "location": "Москва",
        "short": "Джапанди: светлый дуб, глиняная штукатурка, камень",
        "seo": "Дизайн интерьера квартиры 84 м² в стиле джапанди: светлый дуб, глиняная штукатурка, каменный остров на кухне.",
        "text": [
            "Квартира для пары, которая ценит ритуалы: утренний кофе, ужины с друзьями, тишину вечера. Планировку выстроили вокруг кухни-гостиной.",
            "Джапанди здесь — не стиль, а способ думать: реечный дуб, глиняная штукатурка тёплого серо-бежевого оттенка, каменный остров со скруглёнными углами и бумажный светильник над ним.",
            "Каждый предмет прошёл отбор: если вещь не нужна ежедневно — её в проекте нет.",
        ],
        "alts": [
            "Кухня-гостиная в стиле джапанди с реечной стеной из дуба и каменным островом — проект «Форма»",
            "Интерьер джапанди с глиняной штукатуркой и бумажным светильником — проект «Форма», Void & Form",
        ],
    },
    {
        "slug": "svet",
        "name": "Свет",
        "type": "Пентхаус",
        "area": "156 м²",
        "duration": "9 месяцев",
        "scope": "Дизайн-проект · Авторский надзор · Комплектация",
        "location": "Москва",
        "short": "Панорамный минимализм: травертин, город в дымке",
        "seo": "Дизайн-проект пентхауса 156 м² с панорамными окнами: белый травертин, кремовый модульный диван, вид на Москву.",
        "text": [
            "Главный герой этого пентхауса — вид. Город в дымке за панорамными окнами меняется каждый час, и интерьер не спорит с ним, а служит рамой.",
            "Белый травертин, кремовый модульный диван и полированный бетон потолка создают спокойный фон. Вечером сценарии света превращают гостиную в наблюдательную площадку.",
            "Минимум предметов, максимум простора: пространство дышит на все 156 метров.",
        ],
        "alts": [
            "Гостиная пентхауса с панорамными окнами и видом на город — проект «Свет»",
            "Пентхаус в кремовых тонах с травертиновой стеной на закате — проект «Свет», Void & Form",
        ],
    },
    {
        "slug": "dyhanie",
        "name": "Дыхание",
        "type": "Квартира",
        "area": "68 м²",
        "duration": "5 месяцев",
        "scope": "Дизайн-проект · Ремонт под ключ · Комплектация",
        "location": "Москва",
        "short": "Пастель и лён: камерное пространство для двоих",
        "seo": "Дизайн и ремонт квартиры 68 м²: спальня в пастельных тонах, лаймвош пудрового оттенка, льняной текстиль.",
        "text": [
            "Небольшая квартира для двоих, где главной комнатой стала спальня — место, где начинается и заканчивается день.",
            "Стены покрыты лаймвошем пудрового розово-бежевого оттенка: покрытие живёт вместе со светом, меняя глубину в течение дня. Лён, округлое изголовье, травертиновая тумба — всё мягкое, тактильное, спокойное.",
            "Здесь нет ничего случайного и ничего лишнего — только то, что помогает дышать глубже.",
        ],
        "alts": [
            "Спальня в пастельных пудровых тонах с льняным текстилем — проект «Дыхание»",
            "Минималистичная спальня с округлым изголовьем и травертиновой тумбой — проект «Дыхание», Void & Form",
        ],
    },
    {
        "slug": "gran",
        "name": "Грань",
        "type": "Апартаменты",
        "area": "92 м²",
        "duration": "6 месяцев",
        "scope": "Дизайн-проект · Авторский надзор",
        "location": "Москва",
        "short": "Грейдж и тёмный камень: спокойный контраст",
        "seo": "Дизайн апартаментов 92 м²: палитра грейдж, акцентная стена из тёмного камня, овальный дубовый стол.",
        "text": [
            "Заказчик хотел интерьер «со стержнем» — спокойный, но не безликий. Ответом стала одна точная грань: стена из тёмного природного камня в столовой.",
            "Вокруг неё — тишина грейджа: тёплый серо-бежевый, овальный дубовый стол, скульптурные стулья и линейный свет над столом.",
            "Контраст здесь не кричит — он держит пространство, как хребет держит тело.",
        ],
        "alts": [
            "Столовая с акцентной стеной из тёмного камня и овальным дубовым столом — проект «Грань»",
            "Интерьер в палитре грейдж с тёмным камнем и линейным светильником — проект «Грань», Void & Form",
        ],
    },
    {
        "slug": "bereg",
        "name": "Берег",
        "type": "Квартира",
        "area": "143 м²",
        "duration": "8 месяцев",
        "scope": "Дизайн-проект · Ремонт под ключ · Комплектация",
        "location": "Москва",
        "short": "Песок и лён: кабинет-библиотека, тёплая тишина",
        "seo": "Дизайн-проект квартиры 143 м² с домашним кабинетом-библиотекой: песочные тона, встроенные стеллажи из дуба.",
        "text": [
            "Семья много работает из дома, поэтому сердцем квартиры стал кабинет-библиотека — комната, где хочется думать.",
            "Встроенные дубовые стеллажи с редкими, любимыми предметами, криволинейный стол из светлого дерева, шерстяной ковёр и песочная палитра создают ощущение берега: тепло, ровно, спокойно.",
            "Мягкий боковой свет и глубокие тени делают комнату живой в любое время дня.",
        ],
        "alts": [
            "Домашний кабинет-библиотека с дубовыми стеллажами в песочных тонах — проект «Берег»",
            "Кабинет со светлым криволинейным столом и шерстяным ковром — проект «Берег», Void & Form",
        ],
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

  <link rel="icon" href="/favicon.svg" type="image/svg+xml">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Manrope:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">

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
      <a class="logo" href="/">Void <span>&amp;</span> Form</a>
      <nav class="nav" id="nav" aria-label="Основная навигация">
        <a href="/#projects">Проекты</a>
        <a href="/#about">Философия</a>
        <a href="/#services">Услуги</a>
        <a href="/#process">Процесс</a>
        <a href="/#contacts">Контакты</a>
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
          <a href="/">Главная</a><span>/</span><a href="/#projects">Проекты</a><span>/</span><span>«{name}»</span>
        </nav>
        <h1>«{name}»</h1>
        <div class="project-facts">
          <div class="fact"><div class="fact__label">Тип</div><div class="fact__value">{type}</div></div>
          <div class="fact"><div class="fact__label">Площадь</div><div class="fact__value">{area}</div></div>
          <div class="fact"><div class="fact__label">Срок реализации</div><div class="fact__value">{duration}</div></div>
          <div class="fact"><div class="fact__label">Локация</div><div class="fact__value">{location}</div></div>
        </div>
      </div>
    </section>

    <section class="container" style="padding-bottom: clamp(48px, 7vw, 90px)">
      <div class="project-gallery">
        <figure class="is-wide reveal"><img src="/assets/img/{slug}-1.jpg" alt="{alt1}"></figure>
        <figure class="is-wide reveal"><img src="/assets/img/{slug}-2.jpg" alt="{alt2}" loading="lazy"></figure>
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
        <a class="btn reveal" href="/#contacts">Обсудить проект</a>
        <nav class="project-nav container" aria-label="Другие проекты">
          <a href="/projects/{prev_slug}.html">← «{prev_name}»</a>
          <a href="/projects/{next_slug}.html">«{next_name}» →</a>
        </nav>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer__in">
      <a class="logo" href="/">Void <span>&amp;</span> Form</a>
      <nav class="footer__nav" aria-label="Навигация в подвале">
        <a href="/#projects">Проекты</a>
        <a href="/#services">Услуги</a>
        <a href="/#contacts">Контакты</a>
        <a href="/privacy.html">Политика конфиденциальности</a>
      </nav>
      <span>© 2026 Void &amp; Form · Авторское дизайн-бюро</span>
    </div>
  </footer>

  <div class="lightbox" id="lightbox" role="dialog" aria-label="Просмотр фотографии">
    <img src="" alt="">
  </div>

  <script src="/js/main.js" defer></script>
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
        page = TEMPLATE.format(
            site=SITE,
            slug=p["slug"],
            name=p["name"],
            type=p["type"],
            type_lc=p["type"].lower(),
            area=p["area"],
            duration=p["duration"],
            location=p["location"],
            short=p["short"],
            seo=p["seo"],
            alt1=p["alts"][0],
            alt2=p["alts"][1],
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
