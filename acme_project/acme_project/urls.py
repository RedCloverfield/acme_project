# Импортируем настройки проекта.
from django.conf import settings
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    # В конце добавляем к списку вызов функции static.
    # Этот способ передачи статических файлов пользователю будет работать
    # только в режиме разработки (когда проект запускается командой
    # python manage.py runserver) и при настройке DEBUG = True в settings.py.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
