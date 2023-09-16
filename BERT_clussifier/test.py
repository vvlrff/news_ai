from bert_classifier import BertClassifier
import torch

model = torch.load('bert.pt', map_location=torch.device('cpu'))
classifier = BertClassifier(
        model_path='cointegrated/rubert-tiny',
        tokenizer_path='cointegrated/rubert-tiny',
        model_save_path='bert.pt'
)
classifier.model = model

print(classifier.predict('Я люблю пиво'))
print(classifier.predict('Я не люблю тебя тварину тупую пидор бля'))
print(classifier.predict('Я люблю тебя'))
print(classifier.predict('Я люблю тебя'))
print(classifier.predict('Я люблю тебя'))
print(classifier.predict('Я ненавижу тебя'))
print(classifier.predict('Я ненавижу тебя'))
print(classifier.predict('Я ненавижу тебя'))
print(classifier.predict('Я ненавижу тебя'))
print(classifier.predict('Я ненавижу тебя'))