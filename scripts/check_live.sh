#!/usr/bin/env bash
# Проверка живого сайта voidaform.ru: главная и обработчик заявок.
# Запускается после выкладки и по расписанию (health.yml); выход с ошибкой —
# сигнал написать владельцу.
set -u
SITE="https://voidaform.ru"
fail=0
err() { echo "::error::$1"; echo "- $1" >> "${PROBLEMS_FILE:-/dev/null}"; fail=1; }

code=$(curl -s -o /dev/null -w '%{http_code}' -m 20 "$SITE/")
[ "$code" = 200 ] || err "главная отвечает $code"

r=$(curl -sS -m 20 -H "Origin: $SITE" -A "Mozilla/5.0 (site-check)" "$SITE/api/lead.php?token=1" 2>&1)
echo "$r" | grep -q '"ok":true' || err "форма заявок не работает (lead.php: ${r:0:120})"

[ $fail = 0 ] && echo "voidaform.ru: всё работает"
exit $fail
