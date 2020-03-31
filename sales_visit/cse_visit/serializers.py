from .models import *
from rest_framework import serializers


class CustomerDetailSerializer(serializers.ModelSerializer):
    branch = serializers.SlugRelatedField(slug_field='name', read_only=True)
    assigned_cse = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    status = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = CustomerVisitDetails
        fields = '__all__'


class CustomerDetailPostSerializer(serializers.ModelSerializer):
    branch = serializers.SlugRelatedField(queryset=Branch.objects.all(), slug_field='id',  required=False)
    assigned_cse = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id',  required=False)
    status = serializers.SlugRelatedField(queryset=Status.objects.all(),slug_field='id', required=False)

    class Meta:
        model = CustomerVisitDetails
        fields = '__all__'