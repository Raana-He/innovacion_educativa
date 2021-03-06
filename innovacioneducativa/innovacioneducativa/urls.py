from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from search import views as search_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from asistentes import views as asistentes_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^inscripciones/activar$', asistentes_views.inscripcion, name="inscripcion"),
    url(r'^inscripciones/gracias$', asistentes_views.gracias, name="gracias"),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    #url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

 

# For anything not caught by a more specific rule above, hand over to
# Wagtail's serving mechanism (must come last)
urlpatterns += [
    url(r'', include(wagtail_urls)),
]

from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

#handler400 = 'home.views.bad_request'
#handler403 = 'home.views.permission_denied'
handler404 = 'home.views.page_not_found'
#handler500 = 'home.views.server_error'