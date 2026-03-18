from django import forms
from .models import Card

class CardAdminForm(forms.ModelForm):
    photo = forms.ImageField(
        required=False,
        label="Зображення",
        help_text="Оберіть файл — зображення буде автоматично завантажене"
    )

    class Meta:
        model = Card
        fields = ("title",)