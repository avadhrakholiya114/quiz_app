from django.urls import path, include
from .views import *



app_name = 'quizes'
urlpatterns = [
    path('', Quiz_list.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz_view'),
    path('<pk>/data', quiz_data_view, name='quiz_data_view'),
    path('<int:pk>/save/', save_quiz_view, name='save_quiz_view'),


]
