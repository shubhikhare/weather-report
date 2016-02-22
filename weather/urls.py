from django.conf.urls import include, url
from django.contrib import admin
from weather_api import views

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'weather_api.views.home', name='home'),
     url(r'^register/','weather_api.views.signup'),
     url(r'^weather/','weather_api.views.weather'),
     url(r'^login/','weather_api.views.login'),
     url(r'^logout/','weather_api.views.logout'),
     url(r'^weather_update/','weather_api.views.weather_update'),
    # url(r'^blog/', include('blog.urls')),

]
