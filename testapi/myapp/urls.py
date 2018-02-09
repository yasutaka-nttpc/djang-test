# coding: utf-8

from rest_framework import routers
from .views import Pop3ViewSet, ImapViewSet, SmtpauthViewSet, SubmissionViewPort


router = routers.DefaultRouter()
router.register(r'pop3', Pop3ViewSet)
router.register(r'imap', ImapViewSet)
router.register(r'smtpauth', SmtpauthViewSet)
router.register(r'Submission', SubmissionViewSet)
