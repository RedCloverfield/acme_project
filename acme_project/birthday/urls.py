from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.birthday, name='create'),
    # Добавим новый маршрут страницы с перечнем дней рождения
    path('list', views.birthday_list, name='list')
]
