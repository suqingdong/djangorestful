from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import renderers
from snippets.views import api_root, SnippetViewSet, UserViewSet

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'    
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'    
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'    
})


urlpatterns = format_suffix_patterns([
    # /
    url(r'^$', api_root, name='root'),

    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>\d+)/$', snippet_detail, name='snippet-detail'),
    url(r'^snippets/(?P<pk>\d+)/highlight/$', snippet_highlight, name='snippet-highlight'),

    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', user_detail, name='user-detail'),
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),        
]
