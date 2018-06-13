from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
import os

#Gets the path for MEDIA_ROOT to the base MEDIA folder, so that the media gets uploaded to the right directory
def get_image_path(instance, filename):
    return os.path.join('appsec_media', str(instance.id), filename)

#APPUser inherited from the django USER for customized options and adding extra fields.
class APPUser(models.Model):
    user = models.OneToOneField(User, related_name='User')

    def __str__(self):
        return str(self.user.username) + ": " + str(self.user.email)

#Image model to upload Image to DB with fields specified as follows
#It has a foreing key user. So we can store user as a uploader in every image object
#Basically one user can upload multiple images
#All the images are uploaded to the Appsec_images folder under MEDIA folder
#Caption is editable and the IMages are filtered with their published dates
class Image(models.Model):
    user = models.ForeignKey(User)
    uploadimage = models.ImageField(upload_to='Appsec_images/%Y/%m/%d')
    caption = models.CharField(max_length=200, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
