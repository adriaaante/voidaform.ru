# voidaform.ru — сайт дизайн-бюро Void & Form

## Что это
Статический сайт (чистые HTML/CSS/JS, без сборки и зависимостей) авторского
дизайн-бюро Void & Form: дизайн интерьеров и ремонт квартир. Язык — русский.
Референс концепции: bureauslovo.com (минимализм, пастельные тона).
Телефон компании: +7 (987) 654-32-10 (в коде — tel:+79876543210 и wa.me/79876543210).

## Структура проекта
- `index.html` — главная: hero, манифест, проекты, философия, услуги, процесс, FAQ, контакты.
- `projects/*.html` — 6 страниц проектов. **Не редактировать руками** — генерируются
  скриптом `scripts/build_projects.py` (данные проектов внутри скрипта, запуск из корня).
- `css/style.css` — вся стилистика; дизайн-токены в `:root` (палитра, шрифты).
- `js/main.js` — меню, reveal-анимации, лайтбокс, форма (отправка ведёт в WhatsApp).
- `assets/img/*.jpg` — фото интерьеров; `favicon.svg`, `privacy.html`, `sitemap.xml`, `robots.txt`.
- Шрифты: Google Fonts (Cormorant Garamond + Manrope), подключены с preconnect.

## Грабли / важное
- **Все фото проектов — AI-плейсхолдеры** (Higgsfield nano_banana_pro, июль 2026).
  Заказчик обещал PDF с реальными проектами в Google Drive, папка
  «Примеры работ» (id 1fqC5GFI4UaOJb3P2bmhFcwvewpYZsHgO) — на 21.07.2026 была ПУСТА.
  При появлении PDF: извлечь картинки → заменить `assets/img/*` → обновить данные
  в `scripts/build_projects.py` → перегенерировать страницы.
- SEO уже разложено: JSON-LD (ProfessionalService, FAQPage, BreadcrumbList), OG-теги,
  canonical на https://voidaform.ru. При смене домена — менять и в
  `scripts/build_projects.py` (константа SITE), и в index/sitemap/robots.
- Форма заявки серверной части не имеет: submit открывает WhatsApp с текстом заявки.

## Команды
- `python3 scripts/build_projects.py` — перегенерировать страницы проектов.
- Локальный просмотр: `python3 -m http.server 8765` из корня.

## Деплой
Хостинг не настроен. Деплой = выложить содержимое репозитория как есть
(статические файлы) на любой хостинг под доменом voidaform.ru.
