from django.forms import ModelForm
from home.models import ConsumerState


class ConsumerStateForm(ModelForm):
    class Meta:
        model = ConsumerState
        fields = '__all__'
