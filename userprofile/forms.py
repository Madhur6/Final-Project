from django import forms
from .models import UserProfile
from django.conf import settings
from django_countries.widgets import CountrySelectWidget
from django.core.exceptions import ValidationError

class CreateUserProfileForm(forms.ModelForm):

    date_of_birth = forms.DateField(required=False, label="Date of birth:" , widget=forms.DateInput(attrs={
            "type": "date",
            "placeholder": "Select a date",
            "class": "form-control"
        }),
    )

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if "default-user.png" not in image:
            if image.size > settings.MAX_UPLOAD_SIZE * 1024 * 1024:
                raise ValidationError(f"Image file exceeds {settings.MAX_UPLOAD_SIZE} mb size limit!")
        return image
    
    class Meta:
        model = UserProfile
        fields = ["name", "date_of_birth", "about", "country", "image"]
        labels = {
            "name": "Name:",
            "about": "About:",
            "country": "Country:",
            "image": "Image:"
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Your name",
                "class": "form-control"
                }),
            "about": forms.Textarea(attrs={
                "placeholder": "Tell about yourself",
                "class": "form-control",
                "id": "about-input",
                "rows": "3"
            }),
            "country": CountrySelectWidget(attrs={
                "class": "form-control"
            }),
        }