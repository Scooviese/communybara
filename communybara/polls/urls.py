from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

app_name = 'polls'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^users/$', views.UserViewSet.as_view(), name='users'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]