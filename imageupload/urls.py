import views
from django.conf.urls import url

#All the urls under the 'imageupload' app reside here. They can be referred using the app_name cariable:<name of the url> for simplicity
app_name = 'appsec'
urlpatterns = [
    #Index url
    url(r'^$', views.IndexView.as_view(), name='index'),
    #image related urls
    url(r'^upload_image/$', views.GetImage.as_view(), name='get_image'),
    url(r'^update_image/(?P<image_id>.*)/$', views.ImageUpdate.as_view(), name='get_image_update'),
    url(r'^list_images/$', views.ListImage.as_view(), name='list'),
    url(r'^delete_image/$', views.Delete.as_view(), name='delete'),
    # Login urls
    url(r'^login/$', views.LoginView.as_view(), name='hl_login'),
    url(r'^logout/$', views.logout_user, name='hl_logout'),
    url(r'^register/$', views.Register.as_view(), name='register'),
]
