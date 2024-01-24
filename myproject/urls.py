"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from foodapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hotels/all/",views.Hotelappview.as_view(),name="hotels-list"),
    path("hotels/<int:pk>/",views.Hotelappdetailview.as_view(),name="hotels-detail"),
    path("hotels/<int:pk>/remove/",views.Hotelappdelete.as_view(),name="hotel-delete"),
    path("hotels/add/",views.Hotelappcreate.as_view(),name="hotel-add"),
    path("hotels/<int:pk>/change/",views.Hotelappupdate.as_view(),name="hotel-update"),


]
