from django.db import models
from django.utils import timezone

class Post(models.Model):
    # title, body, show, datetime, image

    PUBLIC = 'public'
    PRIVATE = 'private'
    MY = 'my'

    SHOW_TYPES = [
        (PUBLIC, 'PUBLIC'),
        (PRIVATE, 'PRIVATE'),
        (MY, 'MY')
    ]

    title = models.CharField(max_length = 40, help_text="제목")
    body = models.TextField(help_text="포스트 본문 내용")
    show = models.CharField(max_length = 10, choices=SHOW_TYPES, default=PUBLIC, help_text="비공개 여부")
    datetime = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title