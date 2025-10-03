# Altın Kur Telegram Bot

Bu bot, her gün sabah 09:00 Türkiye saatiyle **IZKO altın fiyatlarını** Telegram üzerinden gönderir.

## Kurulum

1. GitHub’da yeni bir repo oluştur: `altin-kur-bot`
2. Bu repo’ya `kur_bot.py` ve `.github/workflows/schedule.yml` dosyalarını ekle.
3. GitHub Settings → Secrets → Actions’a gir:
   - `TELEGRAM_BOT_TOKEN` → Bot tokenını buraya ekle
   - `TELEGRAM_CHAT_ID` → Telegram chat ID’nizi buraya ekle
4. Commit ve push et.

## Çalışma Zamanlaması

- Her gün saat **09:00 Türkiye saati** (UTC+3) otomatik çalışır.
- İstersen manuel olarak da “Run workflow” ile tetikleyebilirsin.
