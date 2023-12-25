from django.contrib import admin
from django.urls import path
from Portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('skills/', views.skills),
    path('projects/', views.projects),
    path('academics/', views.academics),
    path('contact-me/', views.contact, name='contact'),
]
