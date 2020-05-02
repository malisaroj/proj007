from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  UserView, UserDetailsView, PostView, PostDetailsView

urlpatterns = {

    url(r'^user/$', UserView.as_view(), name="create"),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="details"),
    url(r'^post/$', PostView.as_view(), name="create"),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailsView.as_view(), name="details")

}

urlpatterns = format_suffix_patterns(urlpatterns)