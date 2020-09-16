from django.urls import path
from myweb import views

urlpatterns = [
    path('', views.queryUsers),
    path('queryUsers/', views.queryUsers),
    path('openAdd/', views.openAdd),
    path('saveUser/', views.saveUser),
    path('openEdit/', views.openEdit),
    path('updateUser/', views.updateUser),
    path('deleteUser/', views.deleteUser),
    path('queryByid/', views.queryByid),
    path('openQuery/', views.openQuery),
    path('openupLoad/', views.openupLoad),
    path('upLoad/', views.upLoad),
]
