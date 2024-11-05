from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'middle_name', 'last_name' ,'email', 'phone_number','gender', 'birth_date', 'date_joined', 'password']
        extra_kwargs = {'date_joined': {'read_only': True}} 

    def create(self, validated_data):
        user = CustomUser.objects.create_user(email=validated_data['email'], 
                                              first_name=validated_data['first_name'], 
                                              last_name=validated_data['last_name'],
                                              middle_name=validated_data.get('middle_name', ''),
                                              phone_number=validated_data['phone_number'],
                                              gender=validated_data['gender'],
                                              birth_date=validated_data['birth_date'],
                                              password=validated_data['password']
                                            )
        return user
    