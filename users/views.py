from .models import CustomUser
from rest_framework.decorators import APIView
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

# Create your views here.
class UserSignupView(generics.CreateAPIView):
    """
    Handling user signup.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # Allow anyone to access this view
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)

        response_data = {
            'user': serializer.data,
            'token': token.key
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    
class UserLoginView(APIView):
    """
    handling user login.
    """
    # Allow anyone to access this view
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)

            token, created = Token.objects.get_or_create(user=user)

            response_data = {
                'token': token.key,
                'user': {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'phone_number': user.phone_number,
                    'gender': user.gender,
                    'birth_date': user.birth_date,
                }
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
class UserLogoutView(APIView):
    """
    Handle user logout.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            #Get the token for the current user
            request.user.auth_token.delete()
            logout(request)

            return Response({"message: Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
   
# Retrieve User Info View
class UserDetailView(generics.RetrieveAPIView):
    """
    Retrieve user info.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Returns the current logged-in user's data
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

# Edit User View
class UserEditView(generics.UpdateAPIView):
    """
    Class-based view to handle editing user information.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Only allow editing the current logged-in user
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False) # Allow partial updates (PATCH requests)
        instance = self.get_object()
        
        # Get the serializer with the instance (current user)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response({
            'message':'User credentials successfully updated',
            'user': serializer.data
        }, status=status.HTTP_200_OK)

# Delete User View
class UserDeleteView(generics.DestroyAPIView):
    """
    Class-based view to handle deleting the user account.
    """
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({
            'message': 'User successfully deleted'
        }, status=status.HTTP_200_OK)


