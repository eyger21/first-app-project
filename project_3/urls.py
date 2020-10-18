from django.contrib import admin
from django.urls import path
from project_app.views import detail_view, new_meme, HomeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>/', detail_view.as_view(), name="detail"),
    path('new/', new_meme, name="new"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
