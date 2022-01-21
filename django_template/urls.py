from django.conf.urls import url

from . import views

app_name = "django_template"


urlpatterns = [
    url(r"^$", views.landing_page, name="landing_page"),
    url(r"^django_template/landing_page/", views.landing_page, name="landing_page"),
]
