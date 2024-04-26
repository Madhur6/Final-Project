from django.db import models
from core.models import User

from django.urls import reverse
from django.conf import settings
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
    
# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def num_posts_todo(self):
        return self.posts.filter(status=Post.TODO).count()


class Post(models.Model):
    TODO = 'todo'
    DONE = 'done'
    ARCHIVED = 'archived'

    CHOICES_STATUS = [
        (TODO, 'Todo'),
        (DONE, 'Done'),
        (ARCHIVED, 'Archived')
    ]

    project = models.OneToOneField(Project, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=TODO)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post {self.id}: {self.title}"
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": str(self.pk)})


def user_directory_path(instance, filename):
    base_name = os.path.basename(filename)
    name,ext = os.path.splitext(base_name)

    return "post/user/"+ str(instance.user.id)+"/"+name +ext #removing and adding spaces might cause some errors in the path structure...
    # return "post/user/"+ str(instance.post.project.user.id) + "/"+ str(instance.post.id)+ "/"+"IMG_" + str(instance.post.id)+"_"+name +ext

    
# class Images(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=user_directory_path)

# @receiver(post_delete, sender=Images)
# def delete_image_file(sender, instance, **kwargs):
#     # Delete the file from the media folder when the record is deleted
#     if instance.image:
#         try:
#             if os.path.isfile(instance.image.path):
#                 os.remove(instance.image.path)
#         except Exception as e:
#             # Log any errors that occur during file deletion
#             print(f"Error deleting file: {str(e)}")

class Img(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_images')
    img = models.ImageField(upload_to=user_directory_path)

@receiver(post_delete, sender=Img)
def delete_image_file(sender, instance, **kwargs):
    # Delete the file from the media folder when the record is deleted
    if instance.img:
        try:
            if os.path.isfile(instance.img.path):
                os.remove(instance.img.path)
        except Exception as e:
            # Log any errors that occur during file deletion
            print(f"Error deleting file: {str(e)}")