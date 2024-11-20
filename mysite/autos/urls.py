from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'autos'
urlpatterns = [

    path('', views.MainView.as_view(), name='main'), 

    path('make/', views.MakeView.as_view(), name='make_list'),
    path('make/create', views.MakeCreate.as_view(), name='make_create'),
    path('make/<int:pk>/update', views.MakeView.as_view(), name='make_update'),
    path('make/<int:pk>/delete', views.MakeView.as_view(), name='make_delete'),

    path('auto/create', views.MakeView.as_view(), name='auto_create'),
    path('auto/<int:pk>/update', views.MakeView.as_view(), name='auto_update'),
    path('auto/<int:pk>/delete', views.MakeView.as_view(), name='auto_delete'),
]