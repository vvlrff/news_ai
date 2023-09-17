import json, csv, re
from telethon.sync import TelegramClient
from datetime import timedelta
from datetime import datetime

from params import tg_name, tg_api_id, tg_api_hash, CHANNELS


class News_parser:

    def __init__(self, name=tg_name, api_id=tg_api_id, api_hash=tg_api_hash):
        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash

        self.channels = CHANNELS
        self.row_info = []

        self.searching_period = datetime.now() - timedelta(days=30)

    def remove_links(self, text):
        # Шаблон для поиска ссылок в тексте
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        # Удаление ссылок из текста
        text_without_links = url_pattern.sub('', text)
        return text_without_links

    def parse_news(self, key_num):

        for key in self.channels:
            if key == key_num:
                with TelegramClient(self.name,
                                    self.api_id,
                                    self.api_hash,
                                    device_model = "iPhone 14 Pro Max",
                                    system_version = "14.8.1",
                                    app_version = "8.4",
                                    lang_code = "en",
                                    system_lang_code = "en-US") as client:
                    
                    for index in range(len(self.channels)):
                        try:
                            for message in client.iter_messages(self.channels[key][index]):
                                
                                if message.date.timestamp() > self.searching_period.timestamp():

                                    text = message.text

                                    if text is None or message.text == '':
                                        continue

                                    self.row_info.append(self.remove_links(text))
                                
                                else:
                                    break
                        except:
                            pass

        return self.row_info


# if __name__ == '__main__':
#     test = News_parser()
#     all_data = test.parse_news()
