"""
URL configuration for e_learning_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from courses import views  # Importer la vue de l'application courses
from courses.views import course_detail
from login.views import user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Associer la vue home de courses à l'URL /home
    path('cours/', views.cours, name='cours'),  # Associer la vue home de courses à l'URL /home
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
]
