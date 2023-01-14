from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path("home/", views.user_v , name='home'),
    path('reports/<int:myid>/',views.reports,name='reports'),
    path('',views.home,name='blank')
    ]