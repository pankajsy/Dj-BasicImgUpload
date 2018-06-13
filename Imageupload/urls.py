from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
#This file includes all the app urls you create under this project eg:imageupload in this case
urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'', include('imageupload.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
