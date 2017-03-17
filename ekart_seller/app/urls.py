from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'item/list/$', views.ItemList.as_view(), name='item-list'),
    url(r'item/create/$', views.ItemCreate.as_view(), name='item-create'),
    url(r'item/detail/(?P<pk>\d+)/$', views.ItemDetail.as_view(), name='item-detail'),
]
