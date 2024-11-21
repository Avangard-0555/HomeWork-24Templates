# Теперь определим путь для нашего представления. 
# В urls.py добавим маршруты.
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    # Добавьте другие пути по мере необходимости.
]
# Запуск проекта
# Теперь, когда все установлено, вы можете запустить сервер разработки Django и открыть сайт.
python manage.py runserver








































































































Создание структуры проекта
Убедитесь, что файлы находятся в правильной структуре в вашем Django проекте:
myproject/
│
├── appname/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   ├── static/
│   │   ├── styles.css
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
└── myproject/
    ├── settings.py
    ├── urls.py
    └── wsgi.py




  
