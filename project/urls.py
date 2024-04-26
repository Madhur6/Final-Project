from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('post', views.post, name='post'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('detail_post/<int:post_id>/', views.detail_post, name='detail_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('upload_image_edit/<int:post_id>/', views.upload_image_edit, name='upload_image_edit'),
    
    # path('get_image_url/<int:image_id>/', views.get_image_url, name='get_image_url'),
    path('delete/', views.delete_images, name='deleteImages'),
    path('get-temporary-image-url/<int:image_id>/', views.get_temporary_image_url, name='get_temporary_image_url'),
    path('edit_post/<int:post_id>/get-temporary-image-url-edit/<int:image_id>/', views.get_temporary_image_url_edit, name='get_temporary_image_url_edit'),
    path('get-image/<str:signed_value>/', views.get_image, name='get_image'),
    path('edit_post/<int:post_id>/get-image/<str:signed_value>/', views.get_image_edit, name='get_image_edit'),
    path('detail_post/<int:post_id>/get-image/<str:signed_value>/', views.get_image_detail_post, name='get_image_detail_post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)