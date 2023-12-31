from django.urls import path, include
from .views import *

app_name = 'quizes'
urlpatterns = [
    path('', Quiz_list.as_view(),name='main-view'),
    path('<pk>/',quiz_view,name='quiz_view')

]