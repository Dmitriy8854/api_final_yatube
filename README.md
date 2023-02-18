## Проект api final

api final - это REST API для социальной сети Yatube. Позволяет просматривать и отправлять посты, просматривать группы, подписываться на авторов. Для аутентификации используется JWT-токен.


### С помощью этого проекта можно:

- Публиковать записи/сообщения и просматривать сообщению других пользователей
- Подписываться на авторов
- Оставлять комментарии к записям
- Регистрация пользователей

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/Dmitriy8854/api_final_yatube.git
cd kittygram
**Cоздать и активировать виртуальное окружение:**

py -m venv env
source env/bin/activate
**Установить зависимости из файла requirements.txt:**

python -m pip install --upgrade pip
pip install -r requirements.txt
**Выполнить миграции:**

python manage.py migrate
**Запустить проект:**

python manage.py runserver

### Примеры запросов и ответов:

POST запрос на добавление новой публикации в коллекцию 
публикаций. Анонимные запросы запрещены: http://127.0.0.1:8000/api/v1/posts/
ответ: {
  "text": "string",
  "image": "string",
  "group": 0
}

GET запрос на получение списка всех публикаций: http://127.0.0.1:8000/api/v1/posts/
ответ: {
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}

GET запрос на получение публикации по id: http://127.0.0.1:8000/api/v1/posts/{id}/
ответ: {
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}

GET запрос возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены: http://127.0.0.1:8000/api/v1/follow/
ответ: [
  {
    "user": "string",
    "following": "string"
  }
]

POST запрос - подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены: http://127.0.0.1:8000/api/v1/follow/
ответ: {
  "following": "string"
}