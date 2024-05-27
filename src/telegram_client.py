import os
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
from datetime import datetime
from dateutil import tz

class TelegramScraper:
    def __init__(self, api_id, api_hash, phone, username, start_date, end_date, group_url):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone
        self.username = username
        self.start_date = datetime.fromisoformat(start_date).replace(tzinfo=tz.UTC)
        self.end_date = datetime.fromisoformat(end_date).replace(tzinfo=tz.UTC)
        self.group_url = group_url
        self.client = TelegramClient(self.username, self.api_id, self.api_hash)

    async def start(self):
        await self.client.connect()
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone)
            try:
                await self.client.sign_in(self.phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                await self.client.sign_in(password=input('Password: '))

    async def get_group_entity(self):
        return await self.client.get_entity(self.group_url)

    async def fetch_messages(self, group, max_messages=1000):
        offset_id = 0
        limit = 100
        all_messages = []
        total_messages = 0

        while total_messages < max_messages:
            history = await self.client(GetHistoryRequest(
                peer=group,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))

            if not history.messages:
                break

            messages = history.messages
            for message in messages:
                if self.start_date <= message.date.astimezone(tz.UTC) <= self.end_date:
                    all_messages.append(message)
                    total_messages += 1
                    if total_messages >= max_messages:
                        break

            offset_id = messages[-1].id

        return all_messages
