from django.urls import path
from myapp import views
app_name = '[myapp]'
urlpatterns = [
    path('change/',views.change,name = 'change'),
    path('find/',views.find,name = 'find'),
    path('phone/',views.phone,name = 'phone'),
    path('computer/',views.computer,name = 'computer'),
    path('ear/',views.ear,name = 'ear'),
    path('^detail/(?P<id>\d+)$',views.detail,name='detail'),
    path('logout/',views.logout,name = 'logout'),
    path('register/',views.register,name = 'register'),
    path('login/',views.login,name = 'login'),
]