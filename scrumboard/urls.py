from django.urls import path

from scrumboard import views
from scrumboard.api import CardViewSet,ListViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter() #instead of urlpatterns list
router.register(r'lists',ListViewSet)
router.register(r'cards', CardViewSet)


#calling a bad url shows a lot of urls created automaticallyt
urlpatterns = [
                path('register/', views.registerPage, name="register"),
                path('login/', views.loginPage, name="login"),
                path('logout/', views.logoutUser, name="logout"),
                #path('home/', views.home, name="home"),
                #path('page0/', views.page0, name="page0"),
                #path('', views.index, name="index"),
                #path('<str:room_name>/', views.room, name='room'),
                path('', views.page0, name='welcome'),
                path('chat/', views.home, name='home'),
                path('<str:room>/', views.room, name='room'),
                path('chat/checkview', views.checkview, name='checkview'),
                path('send', views.send, name='send'),
                path('getMessages/<str:room>/', views.getMessages, name='getMessages')
               ]
