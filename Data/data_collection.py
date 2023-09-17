import json, csv
import pandas as pd
from news_parser import News_parser

data = [json.loads(line) for line in open(r'Data\News_Category_Dataset_v3.json', 'r', encoding='utf-8')]

categories = {0: [], # спорт
            1: [], # технологии
            2: [], # финансы
            3: [], # Политика
            4: [], # Шоубиз
            5: [], # Fashion
            6: [], # Крипта
            7: [], # Путешествия
            8: [], # Образование
            9: [] # Развлечения
            } # Общее

for elem in data:
    if elem['category'] == 'SPORTS':
        categories[0].append(elem['short_description']) # спорт
    if elem['category'] == 'TECH' or elem['category'] == 'SCIENCE':
        categories[1].append(elem['short_description']) # технологии
    if elem['category'] == 'MONEY' or elem['category'] == 'BUSINESS':
        categories[2].append(elem['short_description']) # финансы
    if elem['category'] == 'POLITICS' or elem['category'] == 'WORLD NEWS':
        categories[3].append(elem['short_description']) # Политика
    
    if elem['category'] == 'STYLE & BEAUTY' or elem['category'] == 'STYLE':
        categories[5].append(elem['short_description']) # Fashion
    
    if elem['category'] == 'TRAVEL':
        categories[7].append(elem['short_description']) # Путешествия
    if elem['category'] == 'EDUCATION':
        categories[8].append(elem['short_description']) # Образование
    if elem['category'] == 'ENTERTAINMENT':
        categories[9].append(elem['short_description']) # Развлечения


cripto_data = pd.read_csv(r'Data\cryptonews.csv')
categories[6] = list(cripto_data['text']) # Крипта

Parser = News_parser()
for key_num in range(10):
    categories[key_num].extend(Parser.parse_news(key_num)) # Дополняем каждую категорию из тг

with open(r"Data\Data.csv", mode="w", encoding='utf-8', newline='') as w_file:
    writer = csv.writer(w_file, delimiter=',')

    for key, value in categories.items():
        for el in value:
            if type(el) == type('qwd') and len(el) > 1:
                writer.writerow([el, key])

data = pd.read_csv(r"Data\Data.csv", encoding='utf-8')
data = data.sample(frac=1)

total_len = data.shape[0]
train_data = data[:total_len-30000]
valid_data = data[total_len-30000:total_len-15000]
test_data  = data[total_len-15000:]

train_data.columns =['text', 'label']
valid_data.columns =['text', 'label']
test_data.columns =['text', 'label']

train_data.to_csv(r"Data\train.csv", sep=',')
valid_data.to_csv(r"Data\valid.csv", sep=',')
test_data.to_csv(r"Data\test.csv", sep=',')