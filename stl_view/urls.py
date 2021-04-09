from django.urls import path
from stl_view import views

urlpatterns = [
  path('<int:pk>/', views.stl_view, name='stl_view'),
  path('', views.home_page, name='home_page'),
]