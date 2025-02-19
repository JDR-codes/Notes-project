from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('update/<int:id>',views.update_note,name='update'),
    path('delete/<int:id>',views.delete_note,name='delete'),
]