from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('error', views.error, name='error'),
    path('post/<str:pk>', views.post, name='post'),
    path('category/<str:foo>', views.category, name='category'),
    path('create_post', views.create_post, name='create_post'),
    path('dashboard', views.dashboard, name ='dashboard'),
    path('delete_post', views.delete_post, name ='delete_post'),
    
]
