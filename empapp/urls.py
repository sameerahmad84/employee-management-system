
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.listemployee, name="listemployee"),
    path('new/',views.addemployee, name="newemployee"),
    path('edit/<str:empcode>/',views.editemployee, name="editemployee"),
    path('delete/<str:empcode>/',views.delemployee, name="delemployee")
    
]
