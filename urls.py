from django.urls import path 


from .views import dylan

urlpatterns = [ 
    path('', dylan, name='dylan')
]