# coding: utf-8

from rest_framework import serializers

from .models import Pop3, Imap, Smtpauth, Submission


class Pop3Serializer(serializers.ModelSerializer):
  class Meta:
    model = Pop3
    fields = ('mode', 'ip_list')


class ImapSerializer(serializers.ModelSerializer):
  class Meta:
    model = Imap
    fields = ('mode', 'ip_list')


class SmtpauthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Smtpauth
    fields = ('setting')


class SubmissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Submission
    fields = ('mode', 'ip_list')

