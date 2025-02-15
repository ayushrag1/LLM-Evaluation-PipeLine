import random
import time

from celery import shared_task

from .constants import EVALUATION_RESULT
from .emails import send_evaluation_email
from .models import EvaluationRequest


@shared_task
def process_evaluation(evaluation_id):
    try:
        evaluation = EvaluationRequest.objects.get(id=evaluation_id)

        # Simulate evaluation process
        time.sleep(30)  # Simulating processing time

        evaluation.result = random.choice(EVALUATION_RESULT)
        evaluation.status = EvaluationRequest.Status.COMPLETED
        evaluation.save()

        send_evaluation_email(
            task_id=evaluation.id,
            input_prompt=evaluation.input_prompt,
            request_datetime=evaluation.created_at,
            completion_datetime=evaluation.updated_at,
            task_status=evaluation.status,
            result=evaluation.result,
            recipient_email=evaluation.notification_email,
        )

    except Exception as e:
        if evaluation:
            evaluation.status = EvaluationRequest.Status.FAILED
            evaluation.result = f"Error: {str(e)}"
            evaluation.save()
        raise e
