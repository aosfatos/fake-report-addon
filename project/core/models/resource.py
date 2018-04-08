from django.db import models
from django.utils.translation import gettext_lazy as _
from utils import BaseModel
from utils.base_model import SoftDeletedQuerySet


class ResourceQuerySet(SoftDeletedQuerySet):

    def fake(self):
        return self.filter(editors_vote=Resource.FAKE)


class Resource(BaseModel):

    LEGIT, FAKE, INCONCLUSIVE = 1, 2, 3
    CHOICES = (
        (LEGIT, _('legit')),
        (FAKE, _('fake')),
        (INCONCLUSIVE, _('inconclusive')),
    )

    stored = ResourceQuerySet.as_manager()

    url = models.URLField(unique=True)
    same_as = models.ManyToManyField('self', blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    editors_vote = models.IntegerField(
        choices=CHOICES, null=True, blank=True
    )
    rewardable = models.BooleanField(default=True)

    @classmethod
    def handle_event(cls, event):
        resource, created = cls.stored.get_or_create(url=event.resource)
        cls._handle_upvote(resource, event)
        cls._handle_downvote(resource, event)
        resource.save()
        event.processed = True
        event.save()

    @classmethod
    def _handle_upvote(cls, resource, event):
        if event.kind == event.UPVOTE:
            resource.upvotes = models.F('upvotes') + 1

    @classmethod
    def _handle_downvote(cls, resource, event):
        if event.kind == event.DOWNVOTE:
            resource.downvotes = models.F('downvotes') + 1

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['-editors_vote', '-downvotes']
