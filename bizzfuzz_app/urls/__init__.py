from django.conf.urls import url

from bizzfuzz_app.views import user

urlpatterns = [
  url(r'^$', user.UserList.as_view(), name='user_list'),
  url(r'^new$', user.UserCreate.as_view(), name='user_new'),
  url(r'^edit/(?P<pk>\d+)$', user.UserUpdate.as_view(), name='user_edit'),
  url(r'^delete/(?P<pk>\d+)$', user.UserDelete.as_view(), name='user_delete'),
  url(r'^export$', user.export_users_xls, name='export_users'),
]
