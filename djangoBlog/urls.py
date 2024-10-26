from django.contrib import admin
from django.urls import path, include
from .import views
from .import vahab
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('a /' , vahab.beutifull),
    path('sume/' , views.sum),
    path('', views.home),
    path('articles/',include('articles.urls')),
]
urlpatterns += staticfiles_urlpatterns()