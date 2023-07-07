
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('',include('tabela.urls')),
    path('admin/', admin.site.urls),
]
