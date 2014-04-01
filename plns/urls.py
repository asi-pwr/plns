from django.conf.urls import patterns, include, url
from plns.payments.views import Categories
from plns.users.views import LoginView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plns.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', LoginView.as_view(success_url='/home/')),
    url(r'^categorys/$','plns.payments.views.show_categorys'),
    url(r'^categories/$',Categories.as_view()),

)
