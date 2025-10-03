import asyncio
import requests
from playwright.async_api import async_playwright
import os

# Telegram bot token ve chat ID (GitHub Secrets üzerinden alınacak)
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

URL = "https://www.izko.org.tr/Home/GuncelKur"

def send_telegram_message(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram token/chat id eksik. Mesaj gönderilemiyor.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    resp = requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text})
    if resp.status_code != 200:
        print("Telegram gönderme hatası:", resp.text)

async def fetch_prices():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        await page.goto(URL, wait_until="networkidle")
        await page.wait_for_selector("table")

        rows = await page.query_selector_all("table tr")
        prices = {}
        for row in rows:
            cols = await row.query_selector_all("td")
            if len(cols) >= 2:
                key = (await cols[0].inner_text()).strip()
                value = (await cols[1].inner_text()).strip()
                prices[key] = value

        await browser.close()
        return prices

async def main():
    prices = await fetch_prices()
    if prices:
        msg = "📊 Güncel Kur Bilgileri:\n"
        for k, v in prices.items():
            msg += f"{k}: {v}\n"
        print(msg)
        send_telegram_message(msg)
    else:
        print("⚠️ Veri çekilemedi.")

if __name__ == "__main__":
    asyncio.run(main())
