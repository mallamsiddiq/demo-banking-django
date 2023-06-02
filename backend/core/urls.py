from django.contrib import admin
from django.urls import include, path


from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView


# handler404 = TemplateView.as_view(template_name='index.html')


urlpatterns = [
    path('our-admin', admin.site.urls),
    path('api/', include('api.urls')),

    # path('web/', include('web.urls')),
]



# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)