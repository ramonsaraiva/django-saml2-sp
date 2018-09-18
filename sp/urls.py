from django.conf.urls import (
    include,
    url,
)
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^saml2/', include('djangosaml2.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(
        r'^protected-resource/',
        login_required(TemplateView.as_view(template_name="protected.html"))
    ),
]
