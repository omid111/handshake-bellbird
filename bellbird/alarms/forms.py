from django import forms

from alarms.models import Alarm

class AlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm
        exclude = ['votes']
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

    def clean_text(self):
        return self.cleaned_data.get("text").upper()
