from django.urls import path
from . import views
urlpatterns= [
    path('',views.homepage, name='homepage'),
    path('question/<question_id>',views.question, name='question'),
]