from rest_framework import serializers
 
from django.contrib.auth.models import File, Customer


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['description', 'file_dump', 'upload_date']
        
        
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'company', 'account', 'email', 'address', 'is_active']