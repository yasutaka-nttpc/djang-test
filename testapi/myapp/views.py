# coding: utf-8
from django.shortcuts import render

#import django_filters
from rest_framework import viewsets, filters

from .models import Pop3, Imap, Smtpauth, Submission
from .serializer import Pop3Serializer, ImapSerializer, SmtpauthSerializer, SubmissionSerializer


class Pop3ViewSet(viewsets.ModelViewSet):
    queryset = Pop3.objects.all()
    serializer_class = Pop3Serializer


class ImapViewSet(viewsets.ModelViewSet):
    queryset = Imap.objects.all()
    serializer_class = ImapSerializer


class SmtpauthViewSet(viewsets.ModelViewSet):
    queryset = Smtpauth.objects.all()
    serializer_class = SmtpauthSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

