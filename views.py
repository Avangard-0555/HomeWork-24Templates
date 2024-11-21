# Привязка к проекту (Django пример)
# Теперь, когда у нас есть HTML и CSS, давай создадим представления. Тем кто  использует Django.
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
