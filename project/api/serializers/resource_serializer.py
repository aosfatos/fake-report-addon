from rest_framework import serializers
from core.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    stamp = serializers.SerializerMethodField()
    same_as = serializers.SerializerMethodField()

    def get_same_as(self, obj):
        return [r.url for r in obj.same_as.all()]

    def get_stamp(self, obj):
        return obj.get_editors_vote_display()

    class Meta:
        model = Resource
        fields = ('url', 'stamp', 'rewardable', 'same_as')
