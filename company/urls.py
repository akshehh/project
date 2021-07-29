from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from company import views


urlpatterns = [

    path('get/',views.get,name='get'),
    path('post/',views.post,name='post'),
    path('getId/<int:id>/',views.getId,name='getId'),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('display/',views.display,name='display')
     
 
]
