from rest_framework import serializers

from ..models import Task


class TaskCreationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Task
        fields = ['name', 'is_done', 'space']
        read_only_fields: list[str] = ['is_done']

    def to_internal_value(self, data: dict[str, str | bool]):
        fields: set[str] = set(self.fields.keys())

        for key in data.keys():
            if key not in fields:
                raise serializers.ValidationError({
                    'message': 'Campo não permitido.'
                })

        return super().to_internal_value(data)