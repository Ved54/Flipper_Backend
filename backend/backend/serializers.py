from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarUpload
        fields = '__all__'
        
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyUpload
        fields = '__all__'
        
class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileUpload
        fields = '__all__'
        
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobUpload
        fields = '__all__'
        
class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeUpload
        fields = '__all__'
        
class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureUpload
        fields = '__all__'
        
class FashionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionUpload
        fields = '__all__'
        
class ElectronicAppliancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicAppliancesUpload
        fields = '__all__'

class CommSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommUpload
        fields = '__all__'
        
class BSHSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSportsHobbiesUpload
        fields = '__all__'
        
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetUpload
        fields = '__all__'
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceUpload
        fields = '__all__'
        
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        
class BarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barter
        fields = '__all__'
    
class FavoriteBarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteBarter
        fields = '__all__'
        