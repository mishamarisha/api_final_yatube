# YATUBE API
## Описание
Проект [YaTube]() - социальная сеть, где можно выкладывать посты, добавлять их к тематическим группам, комментировать свои и чужие тексты и картинки, подписываться на авторов. 

В этом репозитории находится код API для сервиса YaTube. Через API YaTube можно:
* просматривать посты, комментарии, группы (доступно всем пользователям);
* добавлять посты и комментарии (только для авторизованных пользователей);
* редактировать и удалять свои посты и комментарии;
* подписываться на авторов и получать список своих подписок (только для авторизованных пользователей);

Для авторизации в проекте используются JWT-токены.


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:MashaZd/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов к API
Энпоинт: 
__/api/v1/posts__
Метод: __GET__
Доступные параметры: __linit__, __offset__

```{
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
```
Энпоинт: 
__/api/v1/posts__
Метод: __POST__
```{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Энпоинт: 
__/api/v1/follow__
Метод: __POST__
```[
  {
    "user": "string",
    "following": "string"
  }
]
```


Все доступные эндпоинты и методы, а также примеры запросов можно посмотреть в [документации](https://github.com/MashaZd/api_final_yatube/blob/master/yatube_api/static/redoc.yaml).