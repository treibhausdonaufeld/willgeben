from django.urls import path
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog

from .views import set_theme

app_name = "core"

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path("set-theme/", set_theme, name="set_theme"),
]
