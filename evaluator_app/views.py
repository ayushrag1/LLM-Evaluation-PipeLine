from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EvaluationRequest
from .serializers import EvaluationRequestSerializer
from .tasks import process_evaluation


class HealthCheck(APIView):
    def get(self, request):
        return Response(
            data={
                "data": "Health Check True!",
            },
            status=status.HTTP_200_OK,
        )


class EvaluationRequestViewSet(viewsets.ModelViewSet):
    queryset = EvaluationRequest.objects.all()
    serializer_class = EvaluationRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        evaluation = serializer.save()

        # Trigger async processing
        result = process_evaluation.delay(evaluation.id)
        headers = self.get_success_headers(serializer.data)
        return Response(
            data={
                "task_id": result.id,
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
