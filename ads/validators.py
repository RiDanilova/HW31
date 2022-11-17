from rest_framework import serializers


def is_published_validator(value):
    if value:
        raise serializers.ValidationError("Объявление может быть опубликовано только после модерации!")
    return value
