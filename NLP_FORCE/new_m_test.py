from bert_classifier import BertClassifier


classifier = BertClassifier(model_path=r'NLP_FORCE\RuBERT_NaturaLP.pt', tokenizer_path='cointegrated/rubert-tiny')

print(classifier.predict('Сбербанк на 0,1 процентного пункта увеличил размер первого взноса по ипотеке. Теперь он составляет не меньше 10,1%. Изменение относительно небольшое: например, для кредита на 10 млн рублей придется заплатить на 10 000 рублей больше. Ранее ЦБ ужесточил требования к выдаче ипотеки для банков, а правительство повысило величину первого взноса по ипотечным госпрограммам'))

