from django.conf.urls import patterns, include, url
from aiai.views import DemoView, ItemView, StoreView, DemoListView, DemoUpdateView, ItemListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meemee.views.home', name='home'),
    # url(r'^meemee/', include('meemee.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'aiai.views.index'),
     url(r'^demo/request/', DemoView.as_view(), name='demo'),
     url(r'^demo/request/followed_up', DemoUpdateView.as_view(), name='demo followed_up'),
     url(r'^demo/list/', DemoListView.as_view(), name='demo list'),
     url(r'^item/new/', ItemView.as_view(), name='item new'),
     url(r'^item/list/', ItemListView.as_view(), name='item list'),
     url(r'^store/new', StoreView.as_view(), name="store new"),
     
)
