from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  UserView, UserDetailsView, PostView, PostDetailsView
from rest_framework.authtoken.views import obtain_auth_token # add this import

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^user/$', UserView.as_view(), name="users"),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
    url(r'^post/$', PostView.as_view(), name="create"),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailsView.as_view(), name="details"),
    url(r'^get-token/', obtain_auth_token), # Add this line

}

urlpatterns = format_suffix_patterns(urlpatterns)