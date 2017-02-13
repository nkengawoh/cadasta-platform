from django.conf.urls import include, url

from ..views import async


urls = [
    url(
        r'^overview/$',
        async.ProjectDashboard.as_view(),
        name='project-overview'),
    url(
        r'^$',
        async.ProjectDashboard.as_view(),
        name='project-dashboard'),
]


urlpatterns = [
    url(
        r'^organizations/(?P<organization>[-\w]+)/projects/'
        '(?P<project>[-\w]+)/',
        include(urls)),
]