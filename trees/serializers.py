from .models import TreeNode
from rest_framework import serializers


class TreeNodeDescendantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeNode
        fields = ["pk", "root", "level", "parent"]


class TreeNodeSerializer(serializers.ModelSerializer):
    descendants = serializers.SerializerMethodField()
    parent = serializers.PrimaryKeyRelatedField(queryset=TreeNode.objects.all())
    root = serializers.PrimaryKeyRelatedField(
        queryset=TreeNode.objects.all(), required=False
    )

    class Meta:
        model = TreeNode
        fields = ["pk", "descendants", "root", "level", "parent"]

    def get_descendants(self, obj):
        descendants = obj.get_descendants()
        return [
            TreeNodeDescendantSerializer(instance=d, context=self.context).data
            for d in descendants
        ]

    def validate_root(self, data):
        if data:
            raise serializers.ValidationError(
                "This field should be null for a TreeNode. We attach it ourselves."
            )
        return data

    def validate_level(self, data):
        if data:
            raise serializers.ValidationError(
                "This field should be null for a TreeNode. We attach it ourselves."
            )
        return data

    def validate_descendants(self, data):
        if data:
            raise serializers.ValidationError(
                "This field should be null for a TreeNode. We attach it ourselves."
            )
        return data
