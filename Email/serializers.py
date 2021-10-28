from django.db.models.fields import AutoField
from rest_framework import viewsets, serializers
from .models import EmailModel



class EmailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(allow_blank=True, required=False)


    def create(self, validated_data):
        return EmailModel.objects.create(validated_data)



class PhoneModel(serializers.Serialize):
    id = serializers.IntegerField(read_only=True)
    phone = serializers.CharField(allow_blank=True, required=False)

    def create(self, validated_data):
        return PhoneModel.objects.create(validated_data)