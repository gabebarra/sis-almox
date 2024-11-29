from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('login', views.login_sistema, name='login'),
    path('', views.index, name='index'),
    path('logout', views.logout_sistema, name='logout'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)