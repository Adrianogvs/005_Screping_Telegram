import os
import csv
from telethon.errors import SessionPasswordNeededError
from dotenv import load_dotenv
from datetime import datetime
from tqdm import tqdm
from telegram_client import TelegramScraper
from config import Config
import asyncio

load_dotenv()

async def main():
    scraper = TelegramScraper(
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        phone=Config.PHONE_NUMBER,
        username=Config.USERNAME,
        start_date=Config.START_DATE,
        end_date=Config.END_DATE,
        group_url=Config.GROUP_URL
    )

    await scraper.start()

    group = await scraper.get_group_entity()

    messages = await scraper.fetch_messages(group)  # Aguarda a execução da coroutine

    # Salvar mensagens em um arquivo CSV na pasta 'data'
    csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'messages.csv')
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["date", "sender_id", "message"])
        for message in messages:
            writer.writerow([message.date, message.sender_id, message.message])

    print(f"Total messages fetched: {len(messages)}")
    print(f"Mensagens salvas em: {csv_file_path}")

if __name__ == '__main__':
    asyncio.run(main())
