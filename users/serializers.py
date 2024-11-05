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
    
# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def get_token(cls, user):
#         token = super().get_token(user)
        
#         #Adding additional user information
#         token['first_name'] = user.first_name
#         token['last_name'] = user.last_name
#         token['email'] = user.email
#         token['phone_number'] = user.phone_number,
#         token['gender'] = user.gender,
#         token['birth_date'] = user.birth_date
        
#         return token
    
#     def validate(self, attrs):
#         # Override the username to use email
#         username = attrs.get('email')
#         password = attrs.get('password')
        
#         user = authenticate(request=self.context.get('request'), username=username, password=password)
        
#         if not user:
#             raise Exception('No active account found with the given credentials')
        
#         data = super().validate(attrs)
        
#         # Add additional response data
#         data.update({
#             'user': {
#                 'id': self.user.id,
#                 'first_name': self.user.first_name,
#                 'last_name': self.user.last_name,
#                 'email': self.user.email,
#                 'phone_number': self.user.phone_number,
#                 'gender': self.user.gender,
#                 'birth_date': self.user.birth_date,
#             }
#         })
        
#         return data