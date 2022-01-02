from djoser.serializers import TokenSerializer as BaseTokenSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class TokenSerializer(BaseTokenSerializer):
    class Meta(BaseTokenSerializer.Meta):
        fields = ('auth_token','user',)

class UserCreateSerializer(BaseUserCreateSerializer):
    def validate(self, attrs):
        phone = attrs.get("phone")
        #verify phone number
        return super().validate(attrs)