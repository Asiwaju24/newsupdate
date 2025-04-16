from django.urls import path
from . import views
from .views import send_newsletter

urlpatterns = [
    path('newsletter_home', views.index, name='newsletter_home'),
    path('create_newsletter', views.create_newsletter , name='create_newsletter'),
    path('add_subscriber/<int:pk>/', views.add_subscriber, name='add_subscriber'),
    path('newsletter_dashboard', views.newsletter_dashboard, name='newsletter_dashboard'),
    path('send_newsletter/<int:newsletter_id>/', views.send_newsletter, name='send_newsletter'),
]