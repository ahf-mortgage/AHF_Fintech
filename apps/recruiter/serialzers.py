from rest_framework import serializers
from rest_framework import generics
from .models import Edge,Node, LoanAmount

class EdgeSerializer(serializers.ModelSerializer):
    from_ = serializers.SerializerMethodField()
    to = serializers.SerializerMethodField()
    class Meta:
        model = Edge
        fields = "from_","to"

    def get_from_(self, obj):
        return obj.source_node.mlo_agent.user.username

    def get_to(self, obj):
        return obj.target_node.mlo_agent.user.username



class LoanAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAmount
        fields = '__all__'  # Include all fields in the serialization

class NodeSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = Node
        fields = "label","id"

    def get_label(self, obj):
        return obj.mlo_agent.user.username

    def get_id(self, obj):
        return obj.node_id