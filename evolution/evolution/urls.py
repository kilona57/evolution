"""
URL configuration for evolution project.

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
from website.views import veiw_all_nodes, term_detail_view, search, add_node
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', veiw_all_nodes, name='home'),
    path("search/", search, name = "search"),
    path("add_new_nodes/", add_node, name= "add_new_nodes"),
    path('terms/<str:term_name>', term_detail_view, name="term_detail_view"),
]
