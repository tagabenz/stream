from rest_framework import serializers


class Key_Generate_Serializer(serializers.Serializer):
    stream_key = serializers.CharField()

    def update(self,instance,validated_data):
        instance.stream_key = validated_data.get('stream_key',instance.stream_key)
        instance.save()
        
        return instance