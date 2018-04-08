import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import JSONField

from utils import BaseModel


class EventSource(BaseModel):

    UPVOTE, DOWNVOTE, CLOSE_POOL = 1, 2, 3
    KINDS = (
        (UPVOTE, _('upvote')),
        (DOWNVOTE, _('downvote')),
        (CLOSE_POOL, _('close_pool')),
    )

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    resource = models.URLField()
    kind = models.IntegerField(choices=KINDS)
    source_ip = models.GenericIPAddressField(null=True)
    data = JSONField(default=dict)
    processed = models.BooleanField(default=False)
