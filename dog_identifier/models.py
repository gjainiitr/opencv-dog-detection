from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations


class Image(models.Model):
    # name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    # def __str__(image):
    #     return image.


class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.caption

