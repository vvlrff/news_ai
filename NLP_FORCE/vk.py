import vk_api, re
from fuzzywuzzy import fuzz

vk_session = vk_api.VkApi(token='542ccee1542ccee1542ccee1a657397c855542c542ccee13127ef5f6ed1cb2d9bd69637')

vk = vk_session.get_api()

cat_name = {
            # 'Блоги.txt': '#блог',
            # 'Новости и СМИ.txt': '#Новости',
            # 'Развлечения и юмор.txt': '#Юмор',
            # 'Технологии.txt': '#Технологии',
            # 'Экономика.txt': '#Экономика',
            # 'Бизнес и стартапы.txt': '#Стартап',
            # 'Криптовалюты.txt': '#Криптовалюта',
            # 'Путешествия.txt': '#Путешествия',
            # 'Маркетинг, PR, реклама.txt': '#Маркетинг',
            # 'Психология.txt': '#Психология',
            # 'Дизайн.txt': '#Дизайн',
            # 'Политика.txt': '#Политика',
            # 'Искусство.txt': '#Искусство',
            # 'Право.txt': '#Право',
            # 'Образование и познавательное.txt': '#Образование',
            # 'Спорт.txt': '#Спорт',
            # 'Мода и красота.txt': '#Мода',
            # 'Здоровье и медицина.txt': '#Здоровье #медицина',
            # 'Картинки и фото.txt': '#фото',
            'Софт и приложения.txt': '#программирование',
            # 'Видео и фильмы.txt': '#фильмы',
            # 'Музыка.txt': '#Музыка',
            # 'Игры.txt': '#Игры',
            # 'Еда и кулинария.txt': '#Еда #Кулинария',
            # 'Цитаты.txt': '#Цитаты',
            # 'Рукоделие.txt': '#Рукоделие',
            # 'Финансы.txt': '#Финансы',
            # 'Шоубиз.txt': '#Шоубиз'
            }

def drop_dublikates(target, param):
    cleaned_target = set(target)
    list_from_set = list(cleaned_target)
    for i in range(len(list_from_set)-1):
        for j in range(i+1, len(list_from_set)):
            if fuzz.token_set_ratio(list_from_set[i], list_from_set[j]) > param:
                if len(list_from_set[i]) >= len(list_from_set[j]):
                    cleaned_target.discard(list_from_set[j])
                else:
                    cleaned_target.discard(list_from_set[i])

    return list(cleaned_target)


def remove_links_and_hashtags(text):

    text_without_links = re.sub(r'http\S+|www.\S+', '', text)
    text_without_tags = re.sub(r'#\w+', '', text_without_links)
    text_without_n = re.sub(r'\n', '. ', text_without_tags)
    
    return text_without_n


for key, value in cat_name.items():
    with open(f'NLP_FORCE\ForTrain2\{key}', mode='w', encoding='utf-8') as file:
        if key == 'Картинки и фото.txt':
            min_len = 70
        elif key == 'Цитаты.txt':
            min_len = 40
        else:
            min_len = 120
        total_data = []
        time_now = 1695236288
        while len(total_data) < 1000:
            search_results = vk.newsfeed.search(q=value, count=200, extended=0, end_time = time_now, start_time = time_now - 60 * 60 * 24 * 7)
            current_data_list = []
            for item in search_results['items']:
                if item['text'].count('#') < 6:
                    current_news_len = remove_links_and_hashtags(item['text'])
                    if len(current_news_len) > min_len:
                        current_data_list.append(current_news_len+'\n')
            current_data_list = drop_dublikates(current_data_list, param=80)
            time_now -= 60 * 60 * 24 * 7 - 30
            total_data.extend(current_data_list)

            print(f'{key}: {len(total_data)}')

        file.writelines(total_data)
