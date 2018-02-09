from django.db import models

class Pop3(models.Model):
  mode = models.CharField(max_length=10)
  ip_list = models.TextField()


class Imap(models.Model):
  mode = models.CharField(max_length=10)
  ip_list = models.TextField()


class Smtpauth(models.Model):
  smtpauth = models.CharField(max_length=5)


class Submission(models.Model):
  mode = models.CharField(max_length=10)
  ip_list = models.TextField()

