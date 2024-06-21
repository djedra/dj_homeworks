from django.urls import path

from school.views import students_list, sample_view

urlpatterns = [
    path('', students_list, name='students'),
    path('sample/', sample_view, name='debug'),
]