from rest_framework import serializers
from portfolio.models import Question

class votingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"