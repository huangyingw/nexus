from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    url('^login/$', views.login_or_signup),
    # url(r'^logout/', 'django.contrib.auth.views.logout'), # , {'next_page':'/'}
    url(r'^logout/', logout),
    url('^register/$', views.register),
    url(r'^authenticate/', views.authenticate_user),

    url(r'^preferences/$', views.preferences),
    url(r'^update-password/$', views.update_password),

    url(r'^stats/$', views.stats),    

    url(r'^user/(?P<username>[^\.]+)/about', views.about),
    url(r'^user/(?P<username>[^\.]+)/subscribe', views.subscribe),
    url(r'^user/(?P<username>[^\.]+)/unsubscribe', views.unsubscribe),
    # url(r'^user/(?P<username>[^\.]+)', views.user_new), # new posts
    url(r'^preferences/$', views.preferences),
    # TODO: View top/hot posts, view user comments
    # url(r'^user/(?P<username>[^\.]+)/top', views.user_top, name='user_top'),
    # url(r'^user/(?P<username>[^\.]+)/comments', views.user_comments, name='user_comments'),

    url(r'^early-access/', views.email_subscribe),
    
    url(r'^grant-reddit-access', views.grant_reddit_access),

    # Top Users
    url(r'^users/top/$', views.users),
    
]
