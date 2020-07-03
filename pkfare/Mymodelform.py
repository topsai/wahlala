from django.forms import ModelForm
from pkfare import models


class AirLegsList(ModelForm):
    class Meta:
        model = models.searchAirLegs  # 对应的Model中的类
        # 字段，如果是__all__,就是表示列出所有的字段
        fields = "__all__"
        widgets = {
        }
