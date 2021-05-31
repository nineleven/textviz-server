from rest_framework import serializers


class SampleTextsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)


class SpecificTextSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)
