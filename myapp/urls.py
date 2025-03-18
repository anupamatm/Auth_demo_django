from django.urls import path
from .views import home, register, custom_login, custom_logout

urlpatterns = [
    path('', home, name='home'),  # Protected home page
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]
