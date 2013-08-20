from django.conf.urls import patterns, include, url
from greenhouse import views

urlpatterns = patterns('',
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^logout$', views.site_logout, name='logout'),
    url(r'^denied(.+)', views.access_denied, name='denied'),
    url(r'^$', views.index, name='home'),
    url(r'^contributors/(?P<email>.+)/edit', views.edit_person,
        name='edit_person'),
    url(r'^contributors/(?P<email>.+)', views.person_detail,
        name='person_detail'),
    url(r'^users/(?P<user>.+)', views.user_profile, name='user_profile'),
    url(r'^delete_comment/(?P<email>.+)/(?P<comment_id>.+)',
        views.delete_comment,
        name='delete_comment'),
    url(r'^unify', views.unify_identities, name='unify_identities'),
    url(r'^comments/', include('django.contrib.comments.urls'))
)
