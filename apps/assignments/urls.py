from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_view),
    path('list/',views.list_view),
    path('delete/<int:pk>/',views.delete_view),
    path('update/<int:pk>/',views.update_view),
]