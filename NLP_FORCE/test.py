import emoji

import re

cat_name = {
            'Блоги.txt': '#блог',
            'Новости и СМИ.txt': '#Новости',
            'Развлечения и юмор.txt': '#Юмор',
            'Технологии.txt': '#Технологии',
            'Экономика.txt': '#Экономика',
            'Бизнес и стартапы.txt': '#Стартап',
            'Криптовалюты.txt': '#Криптовалюта',
            'Путешествия.txt': '#Путешествия',
            'Маркетинг, PR, реклама.txt': '#Маркетинг',
            'Психология.txt': '#Психология',
            'Дизайн.txt': '#Дизайн',
            'Политика.txt': '#Политика',
            'Искусство.txt': '#Искусство',
            'Право.txt': '#Право',
            'Образование и познавательное.txt': '#Образование',
            'Спорт.txt': '#Спорт',
            'Мода и красота.txt': '#Мода',
            'Здоровье и медицина.txt': '#Здоровье #медицина',
            'Картинки и фото.txt': '#фото',
            'Софт и приложения.txt': '#программирование',
            'Видео и фильмы.txt': '#фильмы',
            'Музыка.txt': '#Музыка',
            'Игры.txt': '#Игры',
            'Еда и кулинария.txt': '#Еда #Кулинария',
            'Цитаты.txt': '#Цитаты',
            'Рукоделие.txt': '#Рукоделие',
            'Финансы.txt': '#Финансы',
            'Шоубиз.txt': '#Шоубиз'
            }


def remove_smileys(text):
    pattern = r'[\U0001F600-\U0001F64F\u263A-\u26FF\u2700-\u27BF]+'
    text_without_smileys = emoji.replace_emoji(text)
    text_without_smileys_and_space = re.sub(' \.', '', text_without_smileys)
    
    return text_without_smileys_and_space


for key, value in cat_name.items():
    news = [] 

    with open(f'NLP_FORCE\ForTrain2\{key}', mode='r', encoding='utf-8') as file:
       news_with_smileys = file.readlines()

       for new in news_with_smileys:
           news.append(remove_smileys(new))

    with open(f'NLP_FORCE\ForTrain3\{key}', mode='w', encoding='utf-8') as file:
        file.writelines(news)    
    