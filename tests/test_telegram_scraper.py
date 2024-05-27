import sys
import os
from datetime import datetime
from dateutil import tz
import pytest

# Adicione o caminho do diretório src ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from telegram_client import TelegramScraper
from config import Config

@pytest.fixture
def scraper():
    return TelegramScraper(
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        phone=Config.PHONE_NUMBER,
        username=Config.USERNAME,
        start_date=Config.START_DATE,
        end_date=Config.END_DATE,
        group_url=Config.GROUP_URL
    )

def test_init(scraper):
    assert scraper is not None
    assert scraper.start_date is not None
    assert scraper.end_date is not None

@pytest.mark.asyncio
async def test_start(scraper):
    await scraper.start()
    assert scraper.client.is_user_authorized()

@pytest.mark.asyncio
async def test_get_group_entity(scraper):
    await scraper.start()
    group = await scraper.get_group_entity()
    assert group is not None

@pytest.mark.asyncio
async def test_fetch_messages(scraper):
    await scraper.start()
    group = await scraper.get_group_entity()
    messages = await scraper.fetch_messages(group, max_messages=10)
    assert len(messages) > 0
    assert all(scraper.start_date <= message.date.astimezone(tz.UTC) <= scraper.end_date for message in messages)
