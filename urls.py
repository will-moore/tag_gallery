from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns(
    'django.views.generic.simple',

    # index 'home page' of the app
    url(r'^$', views.index, name='tag_gallery_index'),

    # Show thumbnails for images in chosen gallery (tag)
    url(r'gallery/(?P<tag_id>[0-9]+)/$', views.tag,
        name='tag_gallery_tag'),

)