from django.urls import path
from app import views
urlpatterns = [
    path('',views.index,name='home'),
    path('details',views.details,name='details'),
    path('list/ <int:pk>',views.list,name='lis'),
    path('edit/ <int:pk>',views.edit,name='edi'),
    path('history',views.history,name='history'),


]