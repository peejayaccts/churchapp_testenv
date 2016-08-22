"""ChMS_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView

#from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token

from api.urls import router

urlpatterns = [
    #url(r'^api/token/', obtain_auth_token, name="api-token"),
    #url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/token/', obtain_jwt_token, name="api-token"),
    url(r'^api/', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name='ChMS/index.html')),
    # Experimental Django App to show simple ui app
    url(r'^ui/', TemplateView.as_view(template_name='index.html')),
    url(r'^uichms/', TemplateView.as_view(template_name='uichms/index.html')),
]
