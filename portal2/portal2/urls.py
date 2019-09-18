"""portal2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from portal2.employees.views import EmployeeViewSet, PositionViewSet
from portal2.customers.views import FileViewSet, CustomerViewSet
from portal2.support.views import ProjectViewSet, TicketViewSet
from portal2.blog.views import ArticleViewSet, CommentViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'files', FileViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
