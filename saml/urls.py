from django.conf.urls import (
    include,
    url,
)
from django.contrib.auth import logout
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^logout/', logout),
    url(r'^saml2/', include('djangosaml2.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
