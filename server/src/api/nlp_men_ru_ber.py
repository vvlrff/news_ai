from .bert_classifier import BertClassifier
import pandas as pd
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
import os



folder_path_to_test = os.getcwd() + r'\src\api\INPUT_\test_data.xlsx'
folder_path_to_test_answer = os.getcwd() + r'\src\api\INPUT_\answer.xlsx'
folder_path_to_test_answer_CHECK = os.getcwd() + r'\src\api\INPUT_\NaturaLP_ANSWER_FOR_CHECKING.xlsx'

folder_path_model = os.getcwd() + r'\src\api\weights\RuBERT_NaturaLP.pt'  # путь к папке, в которую нужно сохранить файл
folder_path_figure = os.getcwd() + r'\src\api\figure_nlp'

class Clussifier():
    def __init__(self):
        self.clussifier = BertClassifier(model_path=folder_path_model, tokenizer_path='cointegrated/rubert-tiny')
        # self.clussifier = BertClassifier(model_path=r'NLP_FORCE\LaBSE_NaturaLP.pt', tokenizer_path='cointegrated/LaBSE-en-ru')
        
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

        idshki = []

        df = pd.DataFrame(list_data)
        df.columns = ['id', 'Новостное сообщение', 'Категория']

        with pd.ExcelWriter(folder_path_to_test_answer_CHECK, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='NaturaLP')
            sheet = writer.sheets['NaturaLP']
            sheet.set_column('C:C', 150)
            sheet.set_column('D:D', 25)
    
    def crate_xlsx(self, dictionary):
        df = pd.DataFrame(dictionary)
        df = df.transpose().reset_index()
        df.rename(columns={'index':'Название категории'}, inplace=True)
        df = df[['Название категории', 'counts', 'counts_not_dubl', 'count_dublic']]

        with pd.ExcelWriter(folder_path_to_test_answer, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Статистика')
            sheet = writer.sheets['Статистика']
            sheet.set_column('B:E', 30)

            df_for_plot1 = df[df['counts'] > 0] 
            
            plt.pie(df_for_plot1['counts'], labels=df_for_plot1['Название категории'], radius=1.0)
            plt.title('counts сообщений по категориям')
            plt.savefig(folder_path_figure+'\pie1.jpeg', dpi=200, bbox_inches='tight')
            sheet.insert_image('H2', folder_path_figure+'\pie1.jpeg')
            plt.close()

            df_for_plot2 = df[df['counts_not_dubl'] > 0] 

            plt.pie(df_for_plot2['counts_not_dubl'], labels=df_for_plot2['Название категории'], radius=1.0)
            plt.title('Количество сообщений без дубликатов по категориям')
            plt.savefig(folder_path_figure+'\pie2.jpeg', dpi=200, bbox_inches='tight')
            sheet.insert_image('H25', folder_path_figure+'\pie2.jpeg')
            plt.close()

            df_for_plot3 = df[df['count_dublic'] > 0] 

            plt.pie(df_for_plot3['count_dublic'], labels=df_for_plot3['Название категории'], radius=1.0)
            plt.title('Количество дубликатов по категориям')
            plt.savefig(folder_path_figure+'\pie3.jpeg', dpi=200, bbox_inches='tight')
            sheet.insert_image('H48', folder_path_figure+'\pie3.jpeg')
            plt.close()

            for key, value in dictionary.items():
                idshki = []
                for el in value['msg без дубликтов']:
                    idshki.append(self.collector[el])
                new_df = pd.DataFrame(list(zip(idshki, value['msg без дубликтов'])), columns =['ID канала', 'msg без дубликтов'])
                new_df.to_excel(writer, sheet_name=key)
                sheet = writer.sheets[key]
                sheet.set_column('B:B', 15)
                sheet.set_column('C:C', 150)
    
    def drop_dublikates(self, target, param):
        cleaned_target = set(target)
        list_from_set = list(cleaned_target)
        for i in range(len(list_from_set)-1):
            for j in range(i+1, len(list_from_set)):
                if fuzz.token_set_ratio(list_from_set[i], list_from_set[j]) > param:
                    if len(list_from_set[i]) >= len(list_from_set[j]):
                        cleaned_target.discard(list_from_set[j])
                    else:
                        cleaned_target.discard(list_from_set[i])
                    print(list_from_set[j], list_from_set[i])

        return list(cleaned_target)
    

    def main(self, target):
        answer_for_cheking = []
        answer = {
                'Блоги': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Новости и СМИ': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Развлечения и юмор': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Технологии': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Экономика': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Бизнес и стартапы': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Криптовалюты': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Путешествия': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Маркетинг, PR, реклама': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Психология': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Дизайн': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Политика': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Искусство': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Право': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Образование и познавательное': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Спорт': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Мода и красота': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Здоровье и медицина': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Картинки и фото': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Софт и приложения': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Видео и фильмы': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Музыка': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Игры': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Еда и кулинария': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Цитаты': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Рукоделие': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Финансы': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Шоубиз': {'counts': 0, 'counts_not_dubl': 0, 'msg': []},
                'Другое': {'counts': 0, 'counts_not_dubl': 0, 'msg': []}
                }

        for element in target:
            el_cat = self.cat_name[self.clussifier.predict(element)]
            answer[el_cat]['counts'] += 1
            answer[el_cat]['msg'].append(element)
            answer_for_cheking.append([element, el_cat])

        for value in answer.values():
            value['msg без дубликтов'] = self.drop_dublikates(value['msg'], param=80)
            value['counts_not_dubl'] = len(value['msg без дубликтов'])
            value['count_dublic'] = value['counts'] - value['counts_not_dubl']

        # print(answer)
        self.crate_xlsx(answer)
        self.crate_xlsx_for_cheking(answer_for_cheking)
        return answer
    
if __name__ == '__main__':
    test = Clussifier()
    test.main(test.parse_xlsx(folder_path_to_test))

