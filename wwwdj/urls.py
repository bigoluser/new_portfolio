from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from wwwdj import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^', views.home, name='home'),
]+static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
