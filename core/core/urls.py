from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    # Django / Admin
    path('admin/', admin.site.urls),
    # Home / Root page
    path('', TemplateView.as_view(template_name="home.html")),
    # Accounts
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name="users/profile.html")),
    # Legal Pages
    path('legal/terms-service',
         TemplateView.as_view(template_name="legal/terms.html")),
    path('legal/privacy', TemplateView.as_view(template_name="legal/privacy.html")),
    # Application
]
