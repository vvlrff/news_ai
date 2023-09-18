# import torch

# from Clussifier.bert_classifier import  BertClassifier

# clussifier = BertClassifier(model_path='LaBSE_5.pt', tokenizer_path='cointegrated/LaBSE-en-ru')


# decoding = {0: 'спорт',
#             1: 'технологии',
#             2: 'финансы',
#             3: 'Политика',
#             4: 'Шоубиз',
#             5: 'Fashion',
#             6: 'Крипта',
#             7: 'Путешествия',
#             8: 'Образование',
#             9: 'Развлечения',
#             10: 'Общее'} 

# print(decoding[clussifier.predict('ВИДЕО: новичок «Пари НН» пяткой (!) сравнял счет на 88-й минуте в дебютном (!!) матче, выйдя за 6 минут (!!!) до этого')])
# print(decoding[clussifier.predict('Александр Головин забил мяч за «Монако» во втором матче подряд')])
# print(decoding[clussifier.predict('«Tesla заново изобретает автомобилестроение». Компания хочет создавать почти всю нижнюю часть авто в виде одной детали')])
# print(decoding[clussifier.predict('Первая в мире GeForce RTX 4070, к которой не нужно подключать никаких кабелей питания. Представлена Asus GeForce RTX 4070 Gaming BTF')])
# print(decoding[clussifier.predict('Как одеться в стиле old money: берем пример с «Наследников» и «Короны»')])
# print(decoding[clussifier.predict('Платье, брюки, рюкзаки и самокат: что понадобится подросткам осенью')])
# print(decoding[clussifier.predict('В России запустили отечественную блокчейн-платформу «Конфидент» В России запустили полностью отечественную блокчейн-платформу «Конфидент»Новая разработка представляет собой готовую инфраструктуру для информационных блокчейн-систем — от слоя для работы нод сети до уровня приложений, где выполняются автоматизированные бизнес-процессы')])
# print(decoding[clussifier.predict('Швейцария обогнала США по уровню принятия криптовалютm. Лидирующую позицию в рейтинге стран по готовности к внедрению цифровых активов второй год подряд занимает Гонконг')])
# print(decoding[clussifier.predict('Новости шоу-бизнеса. Павел Прилучный устроил разборку в центре Москвы, на шоу "Ледниковый период" снова замены и другие')])
# print(decoding[clussifier.predict('Звезда турецкого шоу-бизнеса Демет Оздемир вновь оказалась в центре скандала. Недавно появились сообщения о том, что актриса приобрела дом в Афинах и обрела вторую половинку в лице греческого диджея Серджио.')])
from fuzzywuzzy import fuzz


def drop_dublikates(target, param):
        cleaned_target = []

        for i in range(len(target)-1):
            for j in range(i+1, len(target)):
                if fuzz.WRatio(target[i], target[j]) >  param:
                    if len(target[i]) >= len(target[j]):
                        target[j] = '_'
                    else:
                        target[i] = '_'

        for i in range(len(target)):
            if target[i] != '_':
                cleaned_target.append(target[i])

        return cleaned_target

print(drop_dublikates(['Я пошел в спортивный зал, меня зовут Семен', 'Я пошел в спортивный зал!', 'Меня зовут Семен!', 'Меня зовут Семен'], 80))