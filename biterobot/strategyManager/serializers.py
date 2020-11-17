from rest_framework import serializers

from .models import StrategyModel


# class StrategySerializer(serializers.ModelSerializer):
#     code = serializers.IntegerField()
#     body = serializers.CharField(max_length=1000)
#     class Meta:
#         model = StrategyModel
#         fields = ('name', 'description', 'version', 'code', 'body')
#
#         def create(self, validated_data):
#             print(validated_data.pop('code'), validated_data.pop('body'))
#             validated_data.update({'filePath': 'testPath'})
#             return StrategyModel.objects.create(**validated_data)

class StrategySerializerGET(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    version = serializers.IntegerField()
    description = serializers.CharField(max_length=1000)

class StrategySerializerPOST(serializers.Serializer):
    code = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)
    body = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        print(validated_data.pop('code'), validated_data.pop('body'))
        validated_data.update({'filePath': 'testPath'})
        return StrategyModel.objects.create(**validated_data)
