from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Cycles
from .serializers import CyclesSerializer
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser

class CycleCreateView(generics.CreateAPIView):
    queryset = Cycles.objects.all()
    serializer_class = CyclesSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to create cycle for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Cycle created successfully',
                'cycle': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class CycleDetailView(generics.RetrieveAPIView):
    queryset = Cycles.objects.all()
    serializer_class = CyclesSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = self.get_object()
            if str(instance.user.user_id) != user_id:
                return Response({"message": "Unauthorized access to cycle"}, status=status.HTTP_403_FORBIDDEN)

            serializer = self.get_serializer(instance)
            return Response({
                'message': 'Cycle retrieved successfully',
                'cycle': serializer.data
            }, status=status.HTTP_200_OK)
        except Cycles.DoesNotExist:
            return Response({"message": "Cycle does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
class UserCycleListView(generics.ListAPIView):
    serializer_class = CyclesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        user = get_object_or_404(CustomUser, user_id=user_id)
        return Cycles.objects.filter(user=user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'message': 'User cycles retrieved successfully',
            'cycles': serializer.data
        }, status=status.HTTP_200_OK)


#Edit a cycle
class CycleUpdateView(generics.UpdateAPIView):
    queryset = Cycles.objects.all()
    serializer_class = CyclesSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def update(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")  # Get `user_id` from request body
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()

            if str(instance.user.user_id) != user_id:
                return Response({"message": "Unauthorized access to cycle"}, status=status.HTTP_403_FORBIDDEN)

            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
               'message': 'Cycle updated successfully',
               'cycle': serializer.data
            }, status=status.HTTP_200_OK)
        except Cycles.DoesNotExist:
            return Response({"message": "Cycle does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Delete a Cycle 
class CycleDeleteView(generics.DestroyAPIView):
    queryset = Cycles.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def delete(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")  # Get `user_id` from request body
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = self.get_object()
            if str(instance.user.user_id) != user_id:
                return Response({"message": "Unauthorized access to cycle"}, status=status.HTTP_403_FORBIDDEN)

            self.perform_destroy(instance)
            return Response({
                'message': 'Cycle deleted successfully'
            }, status=status.HTTP_200_OK)
        except Cycles.DoesNotExist:
            return Response({"message": "Cycle does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)