import json, csv
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

        self.searching_period = datetime.now() - timedelta(days=5)

    def parse_news(self):

        for key in self.channels:
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
                            # if message.date.timestamp() > self.last_date_ru:
                            if message.date.timestamp() > self.searching_period.timestamp():

                                text = message.text

                                if text is None or message.text == '':
                                    continue

                                self.row_info.append([text, key])
                            
                            else:
                                break
                    except:
                        pass

        return self.row_info
    
    def write_to_csv(self, all_data):
        with open(r"Data\train.csv", mode="w", encoding='utf-8', newline='') as w_file:
            writer = csv.writer(w_file, delimiter=',')
            writer.writerows(all_data)


if __name__ == '__main__':
    test = News_parser()
    all_data = test.parse_news()
    test.write_to_csv(all_data)
    # print(test.row_info)
