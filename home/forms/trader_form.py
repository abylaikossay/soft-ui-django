from django.forms import ModelForm
from home.models import Trader


class TraderForm(ModelForm):

    class Meta:
        model = Trader
        fields = '__all__'
