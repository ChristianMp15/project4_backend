from .models import Suit
from rest_framework import serializers

class SuitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Which model will get serialized by this class
        model = Suit
        # Which fields should be included in the output
        fields = ['id','subject', 'details']