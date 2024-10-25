from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", homepage, name='home'),
    path("about", about, name='about'),
    path("shop", shop, name='shop'),
    path("projects", projects, name='projects'),
    path("contact", contact, name='contact'),
    path("detail", shopDetail, name='shopDetail'),
    path('aproject/', addProject, name='add_design_project'),
    path('aproduct/', addProduct, name='add_product'),
    path('projects/<int:pk>/', project, name='project_detail'),
    path('projects/<int:pk>/update', edit_project, name='edit_project'),
]

# if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)