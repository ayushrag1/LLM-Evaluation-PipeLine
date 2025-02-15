from django.db import models


class EvaluationRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PROCESSING = "processing", "Processing"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"

    input_prompt = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Evaluation Status",
    )
    result = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notification_email = models.EmailField()

    def __str__(self):
        return f"Evaluation Request {self.id} - {self.get_status_display()}"

    class Meta:
        verbose_name = "Evaluation Request"
        verbose_name_plural = "Evaluation Requests"
        ordering = ["-created_at"]
