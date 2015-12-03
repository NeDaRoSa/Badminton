from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import (handler400, handler403, handler404, handler500)
from birdie import views

handler400 = 'birdie.views.bad_request'
handler403 = 'birdie.views.permission_denied'
handler404 = 'birdie.views.page_not_found'
handler500 = 'birdie.views.server_error'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^create_game/', views.create_game, name='create_game'),
    url(r'^upcoming/', views.upcoming_games, name='upcoming_games'),
    url(r'^joined_games/', views.joined_games, name='joined_games'),
    url(r'^my_games/', views.my_games, name='my_games'),
    url(r'^past_games/', views.past_games, name='past_games'),
    url(r'^update_password/', views.update_password, name='update_password'),
    url(r'^password_updated/', views.password_updated, name='password-updated'),
    url(r'^game/(?P<game_id>\w+)/$', views.game, name='view_game'),
    url(r'^home/', views.upcoming_games, name='home'),
    url(r'^members/', views.members, name='members')
]
