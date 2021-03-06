"""blog URL Configuration

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
from django.conf import settings
from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
                       (r'^$', 'blogpost.views.index'),
                       url(r'^blog/(?P<slug>[^\.]+).html', 'blogpost.views.view_post', name='view_blog_post'),
                       url(r'^pages/', include('django.contrib.flatpages.urls')),
                       url(r'^comments/', include('django_comments.urls')),
                       url(r'^admin/', include(admin.site.urls))
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)