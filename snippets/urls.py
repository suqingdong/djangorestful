from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns([
    # /
    url(r'^$', views.api_root, name='root'),

    # /snippets/    
    #url(r'^$', views.snippet_list, name='list'),        
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    
    # /snippets/2/
    #url(r'^(?P<pk>\d+)/$', views.snippet_detail, name='detail'),         
    url(r'^snippets/(?P<pk>\d+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),

    # /snippets/2/highlight/
    url(r'^snippets/(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),


    # /users/
    url(r'^users/$', views.UserList.as_view(), name='user-list'),

    # /users/2/ 
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),

])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),        
]
