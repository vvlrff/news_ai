from Clussifier.bert_classifier import  BertClassifier
import pandas as pd

class Clussifier():
    def __init__(self):
        self.clussifier = BertClassifier(model_path='LaBSE_5.pt', tokenizer_path='cointegrated/LaBSE-en-ru')

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
        
    def parse_xlsx(self, path):
        data = pd.read_excel(path, names=['text', 'channel_id'])  
        return data['text'].tolist()
    
    def crate_xlsx(self, dictionary):
        df = pd.DataFrame(dictionary)
        df = df.transpose()
        df.to_excel("output.xlsx") 

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
            answer[el_cat]['Количество без дубликтов'] += 1
            answer[el_cat]['Сообщения'].append(element)

        return answer
    

if __name__ == '__main__':
    test = Clussifier()
    test.crate_xlsx(test.main(test.parse_xlsx('test_data.xlsx')))

