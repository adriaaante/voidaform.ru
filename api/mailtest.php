<?php
/**
 * ВРЕМЕННЫЙ файл: разовая проверка, что почта на домене принимает письма
 * и пересылает их на рабочий ящик. Отправляет одно письмо на info@voidaform.ru
 * и удаляет сам себя. Адрес получателя жёстко зашит, доступ по ключу.
 * После проверки файл убирается из репозитория.
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

if (($_GET['key'] ?? '') !== 'd93d9e766b6ac4eeab99b5a3') {
    http_response_code(403);
    echo json_encode(['ok' => false, 'error' => 'forbidden']);
    exit;
}

$to = 'info@voidaform.ru';
$stamp = date('d.m.Y H:i:s');
$subject = 'Проверка почты voidaform.ru — ' . $stamp;
$body = "Это тестовое письмо для проверки ящика info@voidaform.ru.\n\n"
    . "Если вы читаете его на рабочей почте, значит приём писем и пересылка\n"
    . "настроены верно.\n\n"
    . "Отправлено с хостинга: {$stamp}\n";

$headers = implode("\r\n", [
    'From: Void & Form <noreply@voidaform.ru>',
    'Reply-To: noreply@voidaform.ru',
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'X-Mailer: PHP/' . phpversion(),
]);

$sent = mail($to, $subject, $body, $headers);

echo json_encode([
    'ok' => $sent,
    'to' => $to,
    'subject' => $subject,
    'php' => phpversion(),
    'mail_function' => function_exists('mail'),
], JSON_UNESCAPED_UNICODE);

// одноразовый файл — убираем сразу после срабатывания
@unlink(__FILE__);
