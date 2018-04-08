from django.contrib import admin
from core.models import Resource


class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'url', 'upvotes', 'downvotes', 'rewardable',
        'editors_vote',
    )
    readonly_fields = ('url', 'upvotes', 'downvotes')
    exclude = ('deleted_by', 'deleted')


admin.site.register(Resource, ResourceAdmin)
