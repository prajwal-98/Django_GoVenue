from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# configuring the Admin Title

admin.site.site_header = "My club Administration"
admin.site.site_title = "Admin Page"
admin.site.index_title = "Welcome to admin page"
