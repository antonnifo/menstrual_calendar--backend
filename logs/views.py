from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SexualIntercourseLog, MoodLog, BloodFlowLog, MedicationLog, SymptomLog
from .serializers import (
    SexualIntercourseLogSerializer, MoodLogSerializer, BloodFlowLogSerializer,
    MedicationLogSerializer, SymptomLogSerializer
)
from users.models import CustomUser

class SexualIntercourseLogCreateView(generics.CreateAPIView):
    queryset = SexualIntercourseLog.objects.all()
    serializer_class = SexualIntercourseLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Sexual Intercourse Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MoodLogCreateView(generics.CreateAPIView):
    queryset = MoodLog.objects.all()
    serializer_class = MoodLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Mood Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BloodFlowLogCreateView(generics.CreateAPIView):
    queryset = BloodFlowLog.objects.all()
    serializer_class = BloodFlowLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Blood Flow Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MedicationLogCreateView(generics.CreateAPIView):
    queryset = MedicationLog.objects.all()
    serializer_class = MedicationLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Medication Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SymptomLogCreateView(generics.CreateAPIView):
    queryset = SymptomLog.objects.all()
    serializer_class = SymptomLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Symptom Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

