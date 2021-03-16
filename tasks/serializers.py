from rest_framework import serializers

from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import *

class TaskSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Task
        fields = (
            'id', 'title', 'complete', 'created'
        )