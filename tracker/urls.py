from django.urls import path, include, re_path
from django.conf.urls import url
from . import views
from django.views.generic import View
from django.conf.urls.static import static

urlpatterns = [
    path('novo', views.novo, name='novo'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.timesheet, name='timesheet'),
    path('update/<int:id>/', views.update, name="update"),
    path('update/<int:id>/delete/', views.delete, name="delete"),
    path('accounts/', include('django.contrib.auth.urls')),
]
