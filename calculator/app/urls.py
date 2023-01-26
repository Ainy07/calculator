from django.urls import include, path

from . import views

urlpatterns = [
   path('',views.app,name="app"),
    path('cal/',views.cal,name="cal"),
    path('calculator/',views.calculator,name="calculator"),
]

