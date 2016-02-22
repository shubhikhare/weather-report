from django.conf.urls import include, url
from django.contrib import admin
from weather_api import views

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'weather_api.views.home', name='home'),
     url(r'^register/','weather_api.views.signup'),
     #url(r'^profile/','weather_api.views.profile'),
     url(r'^login/','weather_api.views.login'),
    # url(r'^blog/', include('blog.urls')),

]
