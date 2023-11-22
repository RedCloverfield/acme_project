from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday


# Создаём миксин.
class BirthdayMixin:
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # Указываем namespace:name страницы, куда будет перенаправлен пользователь
    # после создания объекта:
    success_url = reverse_lazy('birthday:list')


class BirthdayCreateView(BirthdayMixin, CreateView):
    # Указываем имя формы:
    form_class = BirthdayForm
    # Явным образом указываем шаблон:
    template_name = 'birthday/birthday.html'


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass


# Наследуем класс от встроенного ListView:
class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 10
