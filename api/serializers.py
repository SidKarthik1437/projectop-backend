from rest_framework.serializers import ModelSerializer
from .models import Prob


class ProbSerializer(ModelSerializer):
    class Meta:
        model = Prob
        fields = '__all__'
