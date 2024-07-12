
from django.contrib import admin
from django.urls import path
from halloapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('gallary/',views.gallary,name="images"),
    path('info/',views.info,name="info"),
    path('form/',views.form,name="form"),
    path('login/',views.login,name="login"),
    path('registration/',views.registration,name="registration"),
]
