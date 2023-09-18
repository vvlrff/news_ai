from bert_classifier import BertClassifier
import pandas as pd
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz

class Clussifier():
    def __init__(self):
        self.clussifier = BertClassifier(model_path=r'NLP_FORCE\LaBSE_5.pt', tokenizer_path='cointegrated/LaBSE-en-ru')

        self.cat_name = {0: 'Спорт',
                        1: 'Технологии',
                        2: 'Финансы',
                        3: 'Политика',
                        4: 'Шоубизнес',
                        5: 'Мода',
                        6: 'Криптовалюта',
                        7: 'Путешествия',
                        8: 'Образование',
                        9: 'Развлечения',
                        10: 'Общее'}
        
        self.collector = None
        
    def parse_xlsx(self, path):
        data = pd.read_excel(path, names=['text', 'channel_id'])  
        texts = data['text'].tolist()
        indexes = data['channel_id'].tolist()
        self.collector = dict(zip(texts, indexes))
        return texts
    
    def crate_xlsx(self, dictionary):
        df = pd.DataFrame(dictionary)
        df = df.transpose().reset_index()
        df.rename(columns={'index':'Название категории'}, inplace=True )
        df = df[['Название категории', 'Общее количество', 'Количество без дубликтов']]

        with pd.ExcelWriter(r'NLP_FORCE\NaturaLP_ANSWER.xlsx', engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Статистика')
            sheet = writer.sheets['Статистика']
            sheet.set_column('B:D', 30)

            plt.pie(df['Количество без дубликтов'], labels=df['Название категории'], radius=1.0)
            plt.title('Количество сообщений без дубликатов по категориям')
            plt.savefig(r'NLP_FORCE\pie2.jpeg', dpi=200, bbox_inches='tight')
            sheet.insert_image('F22', r'NLP_FORCE\pie2.jpeg')
            plt.close()

            plt.pie(df['Общее количество'], labels=df['Название категории'], radius=1.0)
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
                sheet.set_column('D:E', 300)
    
    def drop_dublikates(self, target, param):
        cleaned_target = set(target)

        for i in range(len(target)-1):
            for j in range(i+1, len(target)):
                if fuzz.WRatio(target[i], target[j]) > param:
                    if len(target[i]) >= len(target[j]):
                        cleaned_target.discard(target[j])
                    else:
                        cleaned_target.discard(target[i])

        return list(cleaned_target)
    

    def main(self, target):
        answer = {'Спорт': {'Общее количество': 0, 'Количество без дубликтов': 0, 'Сообщения': []},
                  'Технологии': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []},
                  'Финансы': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []},
                  'Политика': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []},
                  'Шоубизнес': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []},
                  'Мода': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []},
                  'Криптовалюта': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []},
                  'Путешествия': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []},
                  'Образование': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []},
                  'Развлечения': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []},
                  'Общее': {'Общее количество': 0, 'Количество без дубликтов': 0,'Сообщения': []}}

        for element in target:
            el_cat = self.cat_name[self.clussifier.predict(element)]
            answer[el_cat]['Общее количество'] += 1
            answer[el_cat]['Сообщения'].append(element)

        for value in answer.values():
            value['Сообщения без дубликтов'] = self.drop_dublikates(value['Сообщения'], param=80)
            value['Количество без дубликтов'] = len(value['Сообщения без дубликтов'])

        print(answer)
        self.crate_xlsx(answer)
        return answer
    
if __name__ == '__main__':
    test = Clussifier()
    test.crate_xlsx(test.main(test.parse_xlsx(r'NLP_FORCE\test_data.xlsx')))

