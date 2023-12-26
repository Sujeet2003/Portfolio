from django.contrib import admin
from django.urls import path
from Portfolio import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('skills/', views.skills),
    path('projects/', views.projects),
    path('academics/', views.academics),
    path('contact-me/', views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()
