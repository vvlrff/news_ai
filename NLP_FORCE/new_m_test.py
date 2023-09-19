# from bert_classifier import BertClassifier


# classifier = BertClassifier(model_path=r'NLP_FORCE\RuBERT_NaturaLP.pt', tokenizer_path='cointegrated/rubert-tiny')

# print(classifier.predict('Сбербанк на 0,1 процентного пункта увеличил размер первого взноса по ипотеке. Теперь он составляет не меньше 10,1%. Изменение относительно небольшое: например, для кредита на 10 млн рублей придется заплатить на 10 000 рублей больше. Ранее ЦБ ужесточил требования к выдаче ипотеки для банков, а правительство повысило величину первого взноса по ипотечным госпрограммам'))
import os
path = r"C:\Users\Chubu\OneDrive\Рабочий стол\news_ai\NLP_FORCE\ForTrain"
dir_list = os.listdir(path)
print(len(dir_list))

for file_name in dir_list:
    with open(f'NLP_FORCE\ForTrain\{file_name}', encoding='utf-8', mode='r+') as current_file:
        data = current_file.readlines()
        for line in data:
            if line[0] == '"':
                line = line[1:]

