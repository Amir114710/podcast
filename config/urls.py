from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from django.conf import settings

urlpatterns = [
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('ckeditor/' , include('ckeditor_uploader.urls')),
    path("admin/", admin.site.urls),
    path('account/' , include('account.urls')),
    path('account/api/' , include('account.api.urls')),
    path('podcast/' , include('podcast.urls')),
    path('podcast/api/' , include('podcast.api.urls')),
    path('qs/' , include('qs_app.urls')),
    path('qs/api/' , include('qs_app.api.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)