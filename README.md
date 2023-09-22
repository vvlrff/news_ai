# NaturaLP

Команда "NaturaLP" представляет удобное и эффективное решение для улучшения работы сервиса "AI News" путем внедрения технологий искусственного интеллекта и машинного обучения, а также инновационных подходов визуализации данных.

![image](https://github.com/vvlrff/news_ai/assets/125179070/9df08848-05e3-4b0f-a4dd-6ae380d62960)

## Пример входных данных:
![image](https://github.com/vvlrff/news_ai/assets/125179070/ba5a87c5-188f-4bd5-9aa5-2b632fe6ff32)

## Пример выходных данных:
![image](https://github.com/vvlrff/news_ai/assets/125179070/cd1f1d6d-7b08-4a91-a635-b899d22060eb)
![image](https://github.com/vvlrff/news_ai/assets/125179070/9bf67de8-7c97-4f57-93bf-e15aec10df6d)
![image](https://github.com/vvlrff/news_ai/assets/125179070/406c8929-6ae0-4fb8-aab2-3a4844cc8a1e)
![image](https://github.com/vvlrff/news_ai/assets/125179070/3d0d70c3-80de-4819-8257-555efca3e603)
![image](https://github.com/vvlrff/news_ai/assets/125179070/c1b2cb16-d263-4edd-baa2-01fe87c85e08)

# Инструкция для запуска Docker'a
Для запуска Docker'a требуется выполнить следующие команды в консоли:
```
    news_ai/docker-compose up --build
```

# Наша модель
## Набор данных:
Для обчения модели необходим большой объем качественных размеченных данных. Для его создания мы использовали VK-API, предоставляющий возможность поиска по HASH-teg'ам. Таким образом, у нас получилось по каждой категории набрать по 2000 отборных качественных новостных сообщений. На этапе сбора данных мы ограничивали минимальную и максимальную длину новости, удаляли ссылки и неинформативные знаки, и, конечно же, не пропускали рекламные посты. Для того, чтобы новости в датасете были уникальными, мы брали информационно-новостные сообщения по 200 штук в неделю, предобрабытывали их и, с использованием технологий нечеткого сравнения, удаляли новости, схожие с уже имеющимися более чем на 80%. Такой подход позволил нам собрать большой качественный набор данных, размеченных реальными людьми, более чем за 5 лет.

Процесс обучения:   
![image](https://github.com/vvlrff/news_ai/assets/125179070/a9dc1c1a-6df9-49a0-9fb4-55418bf4caaf)

Score на тестовых данных:      
Precision: 0.876   
Recall: 0.874   
F1-score: 0.874   

Для обучения модели мы использовали Google-colab, в котором нам временно была предоставлена видеокарта NVIDIA Tesla T4 16GB, вычислительные возможности которой позволили проходить 1 эпоху обучения за 1.5 часа. Таким образом, успешно прошли первые 4 эпохи, затем Google-colab ограничил доступ к GPU. Если взять большее количество данных и пройти больше эпох обучения, есть возможность получить более качественную модель.

## Обучение модели:
Ссылка для скачивания модели: https://drive.google.com/drive/folders/1V_Uw9D60grLkRahNTjOXuBdIT-yB-Sne   
Блокнот для обучения: bert_train_classifier.ipynb   
Нами была создана модель для классификации новостей на 29 категорий на основе BERT-Classiier. Для токенизации и векторизации используется русско-английская модель LaBSE (768-мерные вектора в едином векторном пространстве для разных языков - решение является мультиязычным, т.к. схожие новости на разных языках будут относиться к одной категории).

# Описание алгорита решения
## Задача классификаии:
1) Получение данных в виде Excel-файла;
2) Векторизация данных с использованием русско-английский нейросетевой модели LaBSE;
3) Классификация данных на 29 категорий с использованием собстввенной модели, созданной на основе BERT-Classifier;
4) Отображение результатов классификации в WEB-сервисе и и виде Excel-документов.

## Задача удаления дубликатов:
1) Получение данных в виде Excel-файла;
2) Векторизация данных с использованием русско-английский нейросетевой модели LaBSE;
3) Классификация данных на 29 категорий с использованием собстввенной модели, созданной на основе BERT-Classifier;
4) Использование доработанных алгоритмов продвинутого нечеткого сравнения внутри категорий после классификации (тем самым решается проблемма и семантической, и синтаксической схожести новостных сообщений);
5) Отображение результатов классификации в WEB-сервисе и и виде Excel-документов.

# Цели, задачи и особенности
## Цели:
1) Улучшении сервиса «AI News»;
2) Внедрение технологий ИИ;
3) Реализация механизма идентификации и удаления дубликатов;
4) Внедрение инновационных методов визуализации.

## Задачи:
1) Создание качественной модели классификации новостей на 29 категорий;
2) Разработка алгоритма для идентификации схожих и идентичных новостей.

## В созданном веб-приложении используется:
1) нейросетевая модель глубокого обучения, предназначенная для векторизации текста в 768-мерном пространстве;
2) датасет из более чем 50 000 РАЗМЕЧЕННЫХ данных по 28 категориям;
3) алгоритм идентификации схожих и идентичных новостей, использующий продвинутые алгоритмы нечеткого сравнения;
4) для создания быстрого HTTP API-сервера со встроенными валидацией, сериализацией и асинхронностью - фреймворк FAST API;
5) для создания интуитивно понятного и приятного интерфейса - фреймворк React.js.

## Технические особенности:
Мультиязычность, многопоточность, развертываемость, автономность, user-friendly интерфейс, state-of-art technology.

## Уникальность решения:
Отсеивание бессмысленных новостей, собственный качетсвенный размеченый датасет, высочайшая стабильность доработанного алгоритма классификации, инновационный подход визуализации данных, использование ТОЛЬКО open-source технологий.

## Дальнейшее развитие проекта:
1) Расширение функциональности;
2) Дообучение модели;
3) Развитие алгоритма;
4) Выпуск в Production.

## Ссылка на Google диск (презентация и демонстрация):
https://drive.google.com/drive/folders/1V_Uw9D60grLkRahNTjOXuBdIT-yB-Sne?usp=sharing


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/

[FastApi.py]: https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png
[FastApi-url]: https://fastapi.tiangolo.com/
