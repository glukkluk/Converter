from django.db import models


class User(models.Model):
    user_id = models.BigIntegerField()
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
