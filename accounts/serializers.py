from djoser.serializers import TokenSerializer as BaseTokenSerializer

class TokenSerializer(BaseTokenSerializer):
    class Meta(BaseTokenSerializer.Meta):
        fields = ('auth_token','user',)
