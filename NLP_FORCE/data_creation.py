import os, csv
import pandas as pd
from sklearn.model_selection import train_test_split

path = r"NLP_FORCE\ForTrain4"
dir_list = os.listdir(path)
print(len(dir_list))

cat_name = {
            'Блоги.txt': 0,
            'Новости и СМИ.txt': 1,
            'Развлечения и юмор.txt': 2,
            'Технологии.txt': 3,
            'Экономика.txt': 4,
            'Бизнес и стартапы.txt': 5,
            'Криптовалюты.txt': 6,
            'Путешествия.txt': 7,
            'Маркетинг, PR, реклама.txt': 8,
            'Психология.txt': 9,
            'Дизайн.txt': 10,
            'Политика.txt': 11,
            'Искусство.txt': 12,
            'Право.txt': 13,
            'Образование и познавательное.txt': 14,
            'Спорт.txt': 15,
            'Мода и красота.txt': 16,
            'Здоровье и медицина.txt': 17,
            'Картинки и фото.txt': 18,
            'Софт и приложения.txt': 19,
            'Видео и фильмы.txt': 20,
            'Музыка.txt': 21,
            'Игры.txt': 22,
            'Еда и кулинария.txt': 23,
            'Цитаты.txt': 24,
            'Рукоделие.txt': 25,
            'Финансы.txt': 26,
            'Шоубиз.txt': 27
            }

with open(r"NLP_FORCE\ForTrain4\Data_GPT.csv", mode="w", encoding='utf-8', newline='') as w_file:
    writer = csv.writer(w_file, delimiter='\t')
    for file_name in dir_list:
        cat = cat_name[file_name]
        with open(f'NLP_FORCE\ForTrain4\{file_name}', encoding='utf-8') as current_file:
            data = current_file.readlines()
            for news_article in data:
                writer.writerow([news_article, cat])

data = pd.read_csv(r"NLP_FORCE\ForTrain4\Data_GPT.csv", encoding='utf-8', on_bad_lines='skip', sep='\t')
data.columns =['text', 'label']

print(data.shape)

Х = data['text']
y = data['label']

X_train, X_rem, y_train, y_rem = train_test_split(Х ,y, train_size=0.8)
X_valid, X_test, y_valid, y_test = train_test_split(X_rem, y_rem, test_size=0.5)

train_data = pd.concat([X_train, y_train], axis=1)
valid_data = pd.concat([X_valid, y_valid], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

train_data.columns =['text', 'label']
valid_data.columns =['text', 'label']
test_data.columns =['text', 'label']

train_data.to_csv(r"NLP_FORCE\train.csv", sep='\t')
valid_data.to_csv(r"NLP_FORCE\valid.csv", sep='\t')
test_data.to_csv(r"NLP_FORCE\test.csv", sep='\t')