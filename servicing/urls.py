from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('main/',views.main,name ='main'),
    path('<int:id>/',views.cardetails,name = 'cardetails'),
    path('create/',views.create_car,name = 'create'),
    path('delete_order/<str:id>/',views.delete,name = 'delete_order'),
    path('signup/',views.signup,name = "signup"),
    path('login/',views.login,name = "login"),
    path('logout/',views.logout,name = 'logout')
    ]