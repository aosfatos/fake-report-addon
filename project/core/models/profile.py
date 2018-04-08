from django.db import models
from django.contrib.auth import get_user_model
from utils import BaseModel

USER = get_user_model()


class Profile(BaseModel):
    user = models.ForeignKey(USER, on_delete=models.PROTECT)
    editor = models.BooleanField(default=False)
    professional_id = models.CharField(max_length=55, null=True,
                                       blank=True)
