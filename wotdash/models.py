from django.db import models


class Member(models.Model):
    nickname = models.CharField(max_length=60)
    account_id = models.BigIntegerField()
    email = models.CharField(max_length=100)


