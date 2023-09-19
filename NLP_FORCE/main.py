from bert_classifier import BertClassifier
import pandas as pd
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz

class Clussifier():
    def __init__(self):
        self.clussifier = BertClassifier(model_path=r'NLP_FORCE\RuBERT_NaturaLP.pt', tokenizer_path='cointegrated/rubert-tiny')
        
        self.cat_name = {
                        0: 'Блоги',
                        1: 'Новости и СМИ',
                        2: 'Развлечения и юмор',
                        3: 'Технологии',
                        4: 'Экономика',
                        5: 'Бизнес и стартапы',
                        6: 'Криптовалюты',
                        7: 'Путешествия',
                        8: 'Маркетинг, PR, реклама',
                        9: 'Психология',
                        10: 'Дизайн',
                        11: 'Политика',
                        12: 'Искусство',
                        13: 'Право',
                        14: 'Образование и познавательное',
                        15: 'Спорт',
                        16: 'Мода и красота',
                        17: 'Здоровье и медицина',
                        18: 'Картинки и фото',
                        19: 'Софт и приложения',
                        20: 'Видео и фильмы',
                        21: 'Музыка',
                        22: 'Игры',
                        23: 'Еда и кулинария',
                        24: 'Цитаты',
                        25: 'Рукоделие',
                        26: 'Финансы',
                        27: 'Шоубиз',
                        29: 'Другое'
                        }
        
        self.collector = None
        
    def parse_xlsx(self, path):
        data = pd.read_excel(path, names=['text', 'channel_id'])  
        texts = data['text'].tolist()
        indexes = data['channel_id'].tolist()
        self.collector = dict(zip(texts, indexes))
        return texts
    
    def crate_xlsx_for_cheking(self, list_data):
        for news_article in list_data:
            news_article.insert(0, self.collector[news_article[0]])

        df = pd.DataFrame(list_data)
        df.columns = ['id', 'Новостное сообщение', 'Категория']

        with pd.ExcelWriter(r'NLP_FORCE\NaturaLP_ANSWER_FOR_CHECKING.xlsx', engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='NaturaLP')
            sheet = writer.sheets['NaturaLP']
            sheet.set_column('C:C', 150)
            sheet.set_column('D:D', 25)
    
    def crate_xlsx(self, dictionary):
        df = pd.DataFrame(dictionary)
        df = df.transpose().reset_index()
        df.rename(columns={'index':'Название категории'}, inplace=True)
        df = df[['Название категории', 'Общее количество', 'Количество без дубликтов']]

        with pd.ExcelWriter(r'NLP_FORCE\NaturaLP_ANSWER.xlsx', engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Статистика')
            sheet = writer.sheets['Статистика']
            sheet.set_column('B:D', 30)

            plt.pie(df['Количество без дубликтов'], labels=df['Название категории'], radius=2.0)
            plt.title('Количество сообщений без дубликатов по категориям')
            plt.savefig(r'NLP_FORCE\pie2.jpeg', dpi=200, bbox_inches='tight')
            sheet.insert_image('F52', r'NLP_FORCE\pie2.jpeg')
            plt.close()

            plt.pie(df['Общее количество'], labels=df['Название категории'], radius=2.0)
            plt.title('Общее количество сообщений по категориям')
            plt.savefig(r'NLP_FORCE\pie1.jpeg', dpi=200, bbox_inches='tight')
            sheet.insert_image('F2', r'NLP_FORCE\pie1.jpeg')
            plt.close()

            for key, value in dictionary.items():
                idshki = []
                for el in value['Сообщения без дубликтов']:
                    idshki.append(self.collector[el])
                new_df = pd.DataFrame(list(zip(idshki, value['Сообщения без дубликтов'])), columns =['ID канала', 'Сообщения без дубликтов'])
                new_df.to_excel(writer, sheet_name=key)
                sheet = writer.sheets[key]
                sheet.set_column('B:B', 15)
                sheet.set_column('C:C', 150)
    
    def drop_dublikates(self, target, param):
        cleaned_target = set(target)
        list_from_set = list(cleaned_target)
        for i in range(len(list_from_set)-1):
            for j in range(i+1, len(list_from_set)):
                if fuzz.WRatio(list_from_set[i], list_from_set[j]) > param:
                    if len(list_from_set[i]) >= len(list_from_set[j]):
                        cleaned_target.discard(list_from_set[j])
                    else:
                        cleaned_target.discard(list_from_set[i])

        return list(cleaned_target)
    

    def main(self, target):
        answer_for_cheking = []
        answer = {
                'Блоги': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Новости и СМИ': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Развлечения и юмор': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Технологии': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Экономика': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Бизнес и стартапы': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Криптовалюты': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Путешествия': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Маркетинг, PR, реклама': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Психология': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Дизайн': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Политика': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Искусство': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Право': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Образование и познавательное': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Спорт': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Мода и красота': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Здоровье и медицина': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Картинки и фото': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Софт и приложения': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Видео и фильмы': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Музыка': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Игры': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Еда и кулинария': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Цитаты': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Рукоделие': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Финансы': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Шоубиз': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                'Другое': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []}
                }

        for element in target:
            el_cat = self.cat_name[self.clussifier.predict(element)]
            answer[el_cat]['Общее количество'] += 1
            answer[el_cat]['Сообщения'].append(element)
            answer_for_cheking.append([element, el_cat])

        for value in answer.values():
            value['Сообщения без дубликтов'] = self.drop_dublikates(value['Сообщения'], param=80)
            value['Количество без дубликтов'] = len(value['Сообщения без дубликтов'])

        # print(answer)
        self.crate_xlsx(answer)
        self.crate_xlsx_for_cheking(answer_for_cheking)
        return answer
    
if __name__ == '__main__':
    test = Clussifier()
    test.main(test.parse_xlsx(r'NLP_FORCE\test_data.xlsx'))

