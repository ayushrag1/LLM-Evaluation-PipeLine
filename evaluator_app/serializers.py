from rest_framework import serializers

from .models import EvaluationRequest


class EvaluationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationRequest
        fields = "__all__"  # Include all fields for read operations

    def get_fields(self):
        """
        This method is called when the serializer fields are being accessed.
        We customize it to return only specific fields for creation.
        """
        fields = super().get_fields()

        if self.context.get("request") and self.context["request"].method == "POST":
            # For create (POST) requests, only input_prompt and notification_email are required
            return {key: fields[key] for key in ["id", "input_prompt", "notification_email"]}

        # For other methods (GET, PUT, etc.), return all fields
        return fields

    def create(self, validated_data):
        # Ensure other fields like status and result are set to default values during creation
        validated_data["status"] = "pending"  # Default status
        validated_data["result"] = None  # Default value for result
        return super().create(validated_data)
