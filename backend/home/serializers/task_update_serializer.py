from rest_framework import serializers

from ..models import Task


class TaskUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model: Task = Task
        fields: list[str] = ['name', 'is_done', 'space']

    def to_internal_value(self, data: dict[str, str | bool]):
        fields: set[str] = set(self.fields.keys())

        for key in data.keys():
            if key not in fields:
                raise serializers.ValidationError({
                    'message': 'Campo não permitido.'
                })

        return super().to_internal_value(data)
