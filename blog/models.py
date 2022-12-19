from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.post.title

