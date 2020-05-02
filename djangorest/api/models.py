from django.db import models

class User(models.Model):
    """This class represents the user model."""
    username = models.CharField(max_length=255, blank=False, unique=True)
    user_email = models.EmailField(max_length=254)
    name = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=8, blank=False)
    dob = models.DateField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} {} {}".format(self.username, self.name, self.gender)

class Post(models.Model):
    """This class represents the post model."""
    caption = models.CharField(max_length=255)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
