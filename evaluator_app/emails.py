import logging
import os
from datetime import datetime

from django.apps import apps
from django.conf import settings
from django.core.mail import EmailMessage

# Setup Logger
logger = logging.getLogger(__name__)


def send_evaluation_email(
    task_id: int,
    input_prompt: str,
    request_datetime: datetime,
    completion_datetime: datetime,
    task_status: str,
    result: str,
    recipient_email: str,
) -> bool:
    """
    Send an HTML email notification for completed evaluation requests with timing details in IST timezone.
    """
    try:
        subject = f"LLM Evaluation Task #{task_id} - Results"

        # Calculate processing duration
        duration_seconds = (
            completion_datetime - request_datetime
        ).total_seconds()

        # Format the datetime objects
        formatted_request_time = request_datetime.strftime(
            "%Y-%m-%d %H:%M:%S IST"
        )
        formatted_completion_time = completion_datetime.strftime(
            "%Y-%m-%d %H:%M:%S IST"
        )

        # Get the current app name and template path
        current_app_name = apps.get_containing_app_config(__name__).name
        template_path = os.path.join(
            settings.BASE_DIR, current_app_name, "evaluation_email_template.html"
        )

        # Verify template exists
        if not os.path.exists(template_path):
            logger.error(f"Email template not found at: {template_path}")
            return False

        # Read the template
        with open(template_path, encoding="utf-8") as f:
            template = f.read()

        # Format template with values
        email_body = template.format(
            duration_seconds=duration_seconds,
            task_id=task_id,
            task_status=task_status,
            request_datetime=formatted_request_time,
            completion_datetime=formatted_completion_time,
            input_prompt=input_prompt,
            result=result,
        )

        # Send the email
        email = EmailMessage(
            subject=subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient_email],
        )
        email.content_subtype = "html"  # Ensure the email is sent as HTML
        email.send()

        logger.info(
            f"Evaluation email sent successfully for task {task_id} to {recipient_email}"
        )
        return True

    except Exception as e:
        logger.error(
            f"Failed to send evaluation email for task {task_id}: {str(e)}",
            exc_info=True,
        )
        return False
