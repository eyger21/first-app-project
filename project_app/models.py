from django.db import models

# Create your models here.

class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Mem(models.Model):
    title = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=256)
    comments = models.ManyToManyField(Comment)
    pic = models.ImageField(upload_to="picture", null=True, blank=True)
    def __str__(self):
        return self.title