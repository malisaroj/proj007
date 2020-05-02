from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class User(models.Model):
    """This class represents the user model."""
    username = models.CharField(max_length=255, blank=False, unique=True)
    user_email = models.EmailField(max_length=254)
    name = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=8, blank=False)
    dob = models.DateTimeField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} {} {}".format(self.username, self.name, self.gender)


# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Post(models.Model):
    """This class represents the Post model."""
    image = models.ImageField
    caption = models.TextField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
 
class Comment(models.Model):
    """This class represents the Comment Model."""
    comment = models.TextField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.comment)
