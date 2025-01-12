from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_List_view ),
    path('detail/<int:pk>/',views.detail_view),
    path('delete/<int:pk>/',views.delete_view),
    path('update/<int:pk>/',views.update_view),
]